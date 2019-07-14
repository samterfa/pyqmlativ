# This module contains Student functions.

from .Utilities import make_request

import pandas as pd

import json

import re

def getEveryActivity(EntityID = 1, page = 1, pageSize = 100, returnActivityID = True, returnActivityIDClonedFrom = False, returnActivityIDClonedTo = False, returnActivityLeaderNames = False, returnActivityTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHideInFamilyAccess = False, returnModifiedTime = False, returnSchoolYearID = False, returnSingleSex = False, returnSingleSexCode = False, returnStartDate = False, returnUseForAthleticEligibilityReporting = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Activity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getActivity(ActivityID, EntityID = 1, returnActivityID = True, returnActivityIDClonedFrom = False, returnActivityIDClonedTo = False, returnActivityLeaderNames = False, returnActivityTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHideInFamilyAccess = False, returnModifiedTime = False, returnSchoolYearID = False, returnSingleSex = False, returnSingleSexCode = False, returnStartDate = False, returnUseForAthleticEligibilityReporting = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Activity/" + str(ActivityID), verb = "get", return_params_list = return_params_list)

def modifyActivity(ActivityID, EntityID = 1, setActivityIDClonedFrom = None, setActivityTypeID = None, setCode = None, setDescription = None, setEndDate = None, setEntityID = None, setHideInFamilyAccess = None, setSchoolYearID = None, setSingleSex = None, setSingleSexCode = None, setStartDate = None, setUseForAthleticEligibilityReporting = None, setRelationships = None, returnActivityID = True, returnActivityIDClonedFrom = False, returnActivityIDClonedTo = False, returnActivityLeaderNames = False, returnActivityTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHideInFamilyAccess = False, returnModifiedTime = False, returnSchoolYearID = False, returnSingleSex = False, returnSingleSexCode = False, returnStartDate = False, returnUseForAthleticEligibilityReporting = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Activity/" + str(ActivityID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createActivity(EntityID = 1, setActivityIDClonedFrom = None, setActivityTypeID = None, setCode = None, setDescription = None, setEndDate = None, setEntityID = None, setHideInFamilyAccess = None, setSchoolYearID = None, setSingleSex = None, setSingleSexCode = None, setStartDate = None, setUseForAthleticEligibilityReporting = None, setRelationships = None, returnActivityID = True, returnActivityIDClonedFrom = False, returnActivityIDClonedTo = False, returnActivityLeaderNames = False, returnActivityTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHideInFamilyAccess = False, returnModifiedTime = False, returnSchoolYearID = False, returnSingleSex = False, returnSingleSexCode = False, returnStartDate = False, returnUseForAthleticEligibilityReporting = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Activity/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteActivity(ActivityID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryActivityEvent(EntityID = 1, page = 1, pageSize = 100, returnActivityEventID = True, returnActivityID = False, returnCodeSummary = False, returnContactType = False, returnContactTypeCode = False, returnCost = False, returnCreatedTime = False, returnDate = False, returnDescription = False, returnDisplayOnDistrictCalendar = False, returnEndTime = False, returnEventTypeID = False, returnLocationID = False, returnModifiedTime = False, returnNameIDContact = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnSummary = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVisibleTo = False, returnVisibleToCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityEvent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getActivityEvent(ActivityEventID, EntityID = 1, returnActivityEventID = True, returnActivityID = False, returnCodeSummary = False, returnContactType = False, returnContactTypeCode = False, returnCost = False, returnCreatedTime = False, returnDate = False, returnDescription = False, returnDisplayOnDistrictCalendar = False, returnEndTime = False, returnEventTypeID = False, returnLocationID = False, returnModifiedTime = False, returnNameIDContact = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnSummary = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVisibleTo = False, returnVisibleToCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityEvent/" + str(ActivityEventID), verb = "get", return_params_list = return_params_list)

def modifyActivityEvent(ActivityEventID, EntityID = 1, setActivityID = None, setContactType = None, setContactTypeCode = None, setCost = None, setDate = None, setDescription = None, setDisplayOnDistrictCalendar = None, setEndTime = None, setEventTypeID = None, setLocationID = None, setNameIDContact = None, setStartTime = None, setStatus = None, setStatusCode = None, setSummary = None, setVisibleTo = None, setVisibleToCode = None, setRelationships = None, returnActivityEventID = True, returnActivityID = False, returnCodeSummary = False, returnContactType = False, returnContactTypeCode = False, returnCost = False, returnCreatedTime = False, returnDate = False, returnDescription = False, returnDisplayOnDistrictCalendar = False, returnEndTime = False, returnEventTypeID = False, returnLocationID = False, returnModifiedTime = False, returnNameIDContact = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnSummary = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVisibleTo = False, returnVisibleToCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityEvent/" + str(ActivityEventID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createActivityEvent(EntityID = 1, setActivityID = None, setContactType = None, setContactTypeCode = None, setCost = None, setDate = None, setDescription = None, setDisplayOnDistrictCalendar = None, setEndTime = None, setEventTypeID = None, setLocationID = None, setNameIDContact = None, setStartTime = None, setStatus = None, setStatusCode = None, setSummary = None, setVisibleTo = None, setVisibleToCode = None, setRelationships = None, returnActivityEventID = True, returnActivityID = False, returnCodeSummary = False, returnContactType = False, returnContactTypeCode = False, returnCost = False, returnCreatedTime = False, returnDate = False, returnDescription = False, returnDisplayOnDistrictCalendar = False, returnEndTime = False, returnEventTypeID = False, returnLocationID = False, returnModifiedTime = False, returnNameIDContact = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnSummary = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVisibleTo = False, returnVisibleToCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityEvent/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteActivityEvent(ActivityEventID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryActivityPersonnel(EntityID = 1, page = 1, pageSize = 100, returnActivityPersonnelID = True, returnActivityID = False, returnActivityPersonnelIDClonedFrom = False, returnCreatedTime = False, returnIsLeader = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityPersonnel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getActivityPersonnel(ActivityPersonnelID, EntityID = 1, returnActivityPersonnelID = True, returnActivityID = False, returnActivityPersonnelIDClonedFrom = False, returnCreatedTime = False, returnIsLeader = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityPersonnel/" + str(ActivityPersonnelID), verb = "get", return_params_list = return_params_list)

def modifyActivityPersonnel(ActivityPersonnelID, EntityID = 1, setActivityID = None, setActivityPersonnelIDClonedFrom = None, setIsLeader = None, setNameID = None, setRelationships = None, returnActivityPersonnelID = True, returnActivityID = False, returnActivityPersonnelIDClonedFrom = False, returnCreatedTime = False, returnIsLeader = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityPersonnel/" + str(ActivityPersonnelID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createActivityPersonnel(EntityID = 1, setActivityID = None, setActivityPersonnelIDClonedFrom = None, setIsLeader = None, setNameID = None, setRelationships = None, returnActivityPersonnelID = True, returnActivityID = False, returnActivityPersonnelIDClonedFrom = False, returnCreatedTime = False, returnIsLeader = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityPersonnel/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteActivityPersonnel(ActivityPersonnelID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryActivityType(EntityID = 1, page = 1, pageSize = 100, returnActivityTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getActivityType(ActivityTypeID, EntityID = 1, returnActivityTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityType/" + str(ActivityTypeID), verb = "get", return_params_list = return_params_list)

def modifyActivityType(ActivityTypeID, EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnActivityTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityType/" + str(ActivityTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createActivityType(EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnActivityTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteActivityType(ActivityTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAlert(EntityID = 1, page = 1, pageSize = 100, returnAlertID = True, returnCreatedTime = False, returnEndDate = False, returnInformation = False, returnIsActive = False, returnIsCritical = False, returnModifiedTime = False, returnStartDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Alert/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAlert(AlertID, EntityID = 1, returnAlertID = True, returnCreatedTime = False, returnEndDate = False, returnInformation = False, returnIsActive = False, returnIsCritical = False, returnModifiedTime = False, returnStartDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Alert/" + str(AlertID), verb = "get", return_params_list = return_params_list)

def modifyAlert(AlertID, EntityID = 1, setEndDate = None, setInformation = None, setIsCritical = None, setStartDate = None, setStudentID = None, setRelationships = None, returnAlertID = True, returnCreatedTime = False, returnEndDate = False, returnInformation = False, returnIsActive = False, returnIsCritical = False, returnModifiedTime = False, returnStartDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Alert/" + str(AlertID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAlert(EntityID = 1, setEndDate = None, setInformation = None, setIsCritical = None, setStartDate = None, setStudentID = None, setRelationships = None, returnAlertID = True, returnCreatedTime = False, returnEndDate = False, returnInformation = False, returnIsActive = False, returnIsCritical = False, returnModifiedTime = False, returnStartDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Alert/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAlert(AlertID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigDistrict(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictID = True, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigDistrict(ConfigDistrictID, EntityID = 1, returnConfigDistrictID = True, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigDistrict/" + str(ConfigDistrictID), verb = "get", return_params_list = return_params_list)

def modifyConfigDistrict(ConfigDistrictID, EntityID = 1, setDistrictID = None, setRelationships = None, returnConfigDistrictID = True, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigDistrict/" + str(ConfigDistrictID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigDistrict(EntityID = 1, setDistrictID = None, setRelationships = None, returnConfigDistrictID = True, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigDistrict/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigDistrict(ConfigDistrictID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigEntityGroupYear(EntityID = 1, page = 1, pageSize = 100, returnConfigEntityGroupYearID = True, returnCourseSubjectIDFollettDestinyRoomTeacher = False, returnCreatedTime = False, returnDefaultAllowFeeManagementOnlinePaymentAccess = False, returnDefaultAllowFoodServiceOnlinePaymentAccess = False, returnEntityGroupKey = False, returnEntityID = False, returnFollettDestinyCustomEntityCode = False, returnFollettDestinyRoomTeacherPeriod = False, returnFollettDestinyRoomTeacherType = False, returnFollettDestinyRoomTeacherTypeCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentAccessAccountInfoEmailBody = False, returnStudentAccessAccountInfoEmailIncludeResetPasswordText = False, returnStudentAccessAccountInfoEmailSubject = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, returnConfigEntityGroupYearID = True, returnCourseSubjectIDFollettDestinyRoomTeacher = False, returnCreatedTime = False, returnDefaultAllowFeeManagementOnlinePaymentAccess = False, returnDefaultAllowFoodServiceOnlinePaymentAccess = False, returnEntityGroupKey = False, returnEntityID = False, returnFollettDestinyCustomEntityCode = False, returnFollettDestinyRoomTeacherPeriod = False, returnFollettDestinyRoomTeacherType = False, returnFollettDestinyRoomTeacherTypeCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentAccessAccountInfoEmailBody = False, returnStudentAccessAccountInfoEmailIncludeResetPasswordText = False, returnStudentAccessAccountInfoEmailSubject = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "get", return_params_list = return_params_list)

def modifyConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, setCourseSubjectIDFollettDestinyRoomTeacher = None, setDefaultAllowFeeManagementOnlinePaymentAccess = None, setDefaultAllowFoodServiceOnlinePaymentAccess = None, setEntityGroupKey = None, setEntityID = None, setFollettDestinyCustomEntityCode = None, setFollettDestinyRoomTeacherPeriod = None, setFollettDestinyRoomTeacherType = None, setFollettDestinyRoomTeacherTypeCode = None, setSchoolYearID = None, setStudentAccessAccountInfoEmailBody = None, setStudentAccessAccountInfoEmailIncludeResetPasswordText = None, setStudentAccessAccountInfoEmailSubject = None, setRelationships = None, returnConfigEntityGroupYearID = True, returnCourseSubjectIDFollettDestinyRoomTeacher = False, returnCreatedTime = False, returnDefaultAllowFeeManagementOnlinePaymentAccess = False, returnDefaultAllowFoodServiceOnlinePaymentAccess = False, returnEntityGroupKey = False, returnEntityID = False, returnFollettDestinyCustomEntityCode = False, returnFollettDestinyRoomTeacherPeriod = False, returnFollettDestinyRoomTeacherType = False, returnFollettDestinyRoomTeacherTypeCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentAccessAccountInfoEmailBody = False, returnStudentAccessAccountInfoEmailIncludeResetPasswordText = False, returnStudentAccessAccountInfoEmailSubject = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigEntityGroupYear(EntityID = 1, setCourseSubjectIDFollettDestinyRoomTeacher = None, setDefaultAllowFeeManagementOnlinePaymentAccess = None, setDefaultAllowFoodServiceOnlinePaymentAccess = None, setEntityGroupKey = None, setEntityID = None, setFollettDestinyCustomEntityCode = None, setFollettDestinyRoomTeacherPeriod = None, setFollettDestinyRoomTeacherType = None, setFollettDestinyRoomTeacherTypeCode = None, setSchoolYearID = None, setStudentAccessAccountInfoEmailBody = None, setStudentAccessAccountInfoEmailIncludeResetPasswordText = None, setStudentAccessAccountInfoEmailSubject = None, setRelationships = None, returnConfigEntityGroupYearID = True, returnCourseSubjectIDFollettDestinyRoomTeacher = False, returnCreatedTime = False, returnDefaultAllowFeeManagementOnlinePaymentAccess = False, returnDefaultAllowFoodServiceOnlinePaymentAccess = False, returnEntityGroupKey = False, returnEntityID = False, returnFollettDestinyCustomEntityCode = False, returnFollettDestinyRoomTeacherPeriod = False, returnFollettDestinyRoomTeacherType = False, returnFollettDestinyRoomTeacherTypeCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentAccessAccountInfoEmailBody = False, returnStudentAccessAccountInfoEmailIncludeResetPasswordText = False, returnStudentAccessAccountInfoEmailSubject = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigEntityGroupYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigSystem(EntityID = 1, page = 1, pageSize = 100, returnConfigSystemID = True, returnAllowStudentAccessDefault = False, returnAutoGenerateEmail = False, returnAutoGenerateEmailCode = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnEasyIEPSection504ImportFilePath = False, returnEasyIEPSpecEdImportFilePath = False, returnEmailDomain = False, returnEmailTypeIDDefault = False, returnModifiedTime = False, returnStudentAttachmentVisibility = False, returnStudentAttachmentVisibilityCode = False, returnStudentNumberMask = False, returnStudentNumberStartValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigSystem(ConfigSystemID, EntityID = 1, returnConfigSystemID = True, returnAllowStudentAccessDefault = False, returnAutoGenerateEmail = False, returnAutoGenerateEmailCode = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnEasyIEPSection504ImportFilePath = False, returnEasyIEPSpecEdImportFilePath = False, returnEmailDomain = False, returnEmailTypeIDDefault = False, returnModifiedTime = False, returnStudentAttachmentVisibility = False, returnStudentAttachmentVisibilityCode = False, returnStudentNumberMask = False, returnStudentNumberStartValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigSystem/" + str(ConfigSystemID), verb = "get", return_params_list = return_params_list)

def modifyConfigSystem(ConfigSystemID, EntityID = 1, setAllowStudentAccessDefault = None, setAutoGenerateEmail = None, setAutoGenerateEmailCode = None, setAutoGenerateSecurityUser = None, setAutoGenerateSecurityUserCode = None, setEasyIEPSection504ImportFilePath = None, setEasyIEPSpecEdImportFilePath = None, setEmailDomain = None, setEmailTypeIDDefault = None, setStudentAttachmentVisibility = None, setStudentAttachmentVisibilityCode = None, setStudentNumberMask = None, setStudentNumberStartValue = None, setRelationships = None, returnConfigSystemID = True, returnAllowStudentAccessDefault = False, returnAutoGenerateEmail = False, returnAutoGenerateEmailCode = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnEasyIEPSection504ImportFilePath = False, returnEasyIEPSpecEdImportFilePath = False, returnEmailDomain = False, returnEmailTypeIDDefault = False, returnModifiedTime = False, returnStudentAttachmentVisibility = False, returnStudentAttachmentVisibilityCode = False, returnStudentNumberMask = False, returnStudentNumberStartValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigSystem/" + str(ConfigSystemID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigSystem(EntityID = 1, setAllowStudentAccessDefault = None, setAutoGenerateEmail = None, setAutoGenerateEmailCode = None, setAutoGenerateSecurityUser = None, setAutoGenerateSecurityUserCode = None, setEasyIEPSection504ImportFilePath = None, setEasyIEPSpecEdImportFilePath = None, setEmailDomain = None, setEmailTypeIDDefault = None, setStudentAttachmentVisibility = None, setStudentAttachmentVisibilityCode = None, setStudentNumberMask = None, setStudentNumberStartValue = None, setRelationships = None, returnConfigSystemID = True, returnAllowStudentAccessDefault = False, returnAutoGenerateEmail = False, returnAutoGenerateEmailCode = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnEasyIEPSection504ImportFilePath = False, returnEasyIEPSpecEdImportFilePath = False, returnEmailDomain = False, returnEmailTypeIDDefault = False, returnModifiedTime = False, returnStudentAttachmentVisibility = False, returnStudentAttachmentVisibilityCode = False, returnStudentNumberMask = False, returnStudentNumberStartValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigSystem/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigSystem(ConfigSystemID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCurrentSportsSelections(EntityID = 1, page = 1, pageSize = 100, returnCurrentSportsSelectionsID = True, returnCreatedTime = False, returnFallSportID = False, returnModifiedTime = False, returnSpringSportID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSportID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CurrentSportsSelections/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCurrentSportsSelections(CurrentSportsSelectionsID, EntityID = 1, returnCurrentSportsSelectionsID = True, returnCreatedTime = False, returnFallSportID = False, returnModifiedTime = False, returnSpringSportID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSportID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CurrentSportsSelections/" + str(CurrentSportsSelectionsID), verb = "get", return_params_list = return_params_list)

def modifyCurrentSportsSelections(CurrentSportsSelectionsID, EntityID = 1, setFallSportID = None, setSpringSportID = None, setStudentID = None, setWinterSportID = None, setRelationships = None, returnCurrentSportsSelectionsID = True, returnCreatedTime = False, returnFallSportID = False, returnModifiedTime = False, returnSpringSportID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSportID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CurrentSportsSelections/" + str(CurrentSportsSelectionsID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCurrentSportsSelections(EntityID = 1, setFallSportID = None, setSpringSportID = None, setStudentID = None, setWinterSportID = None, setRelationships = None, returnCurrentSportsSelectionsID = True, returnCreatedTime = False, returnFallSportID = False, returnModifiedTime = False, returnSpringSportID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSportID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CurrentSportsSelections/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCurrentSportsSelections(CurrentSportsSelectionsID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCustomCode(EntityID = 1, page = 1, pageSize = 100, returnCustomCodeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCustomCodeTypeID = False, returnDescription = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CustomCode/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCustomCode(CustomCodeID, EntityID = 1, returnCustomCodeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCustomCodeTypeID = False, returnDescription = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CustomCode/" + str(CustomCodeID), verb = "get", return_params_list = return_params_list)

def modifyCustomCode(CustomCodeID, EntityID = 1, setCode = None, setCustomCodeTypeID = None, setDescription = None, setDistrictGroupKey = None, setRelationships = None, returnCustomCodeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCustomCodeTypeID = False, returnDescription = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CustomCode/" + str(CustomCodeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCustomCode(EntityID = 1, setCode = None, setCustomCodeTypeID = None, setDescription = None, setDistrictGroupKey = None, setRelationships = None, returnCustomCodeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCustomCodeTypeID = False, returnDescription = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CustomCode/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCustomCode(CustomCodeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCustomCodeType(EntityID = 1, page = 1, pageSize = 100, returnCustomCodeTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CustomCodeType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCustomCodeType(CustomCodeTypeID, EntityID = 1, returnCustomCodeTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CustomCodeType/" + str(CustomCodeTypeID), verb = "get", return_params_list = return_params_list)

def modifyCustomCodeType(CustomCodeTypeID, EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setRelationships = None, returnCustomCodeTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CustomCodeType/" + str(CustomCodeTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCustomCodeType(EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setRelationships = None, returnCustomCodeTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CustomCodeType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCustomCodeType(CustomCodeTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEventType(EntityID = 1, page = 1, pageSize = 100, returnEventTypeID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/EventType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEventType(EventTypeID, EntityID = 1, returnEventTypeID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/EventType/" + str(EventTypeID), verb = "get", return_params_list = return_params_list)

def modifyEventType(EventTypeID, EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnEventTypeID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/EventType/" + str(EventTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEventType(EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnEventTypeID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/EventType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEventType(EventTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryFallSport(EntityID = 1, page = 1, pageSize = 100, returnFallSportID = True, returnCode = False, returnCreatedTime = False, returnFallSport = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FallSport/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getFallSport(FallSportID, EntityID = 1, returnFallSportID = True, returnCode = False, returnCreatedTime = False, returnFallSport = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FallSport/" + str(FallSportID), verb = "get", return_params_list = return_params_list)

def modifyFallSport(FallSportID, EntityID = 1, setCode = None, setFallSport = None, setRelationships = None, returnFallSportID = True, returnCode = False, returnCreatedTime = False, returnFallSport = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FallSport/" + str(FallSportID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createFallSport(EntityID = 1, setCode = None, setFallSport = None, setRelationships = None, returnFallSportID = True, returnCode = False, returnCreatedTime = False, returnFallSport = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FallSport/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteFallSport(FallSportID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryFallSportsTeam(EntityID = 1, page = 1, pageSize = 100, returnFallSportsTeamID = True, returnCaptain = False, returnCreatedTime = False, returnFallSportID = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FallSportsTeam/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getFallSportsTeam(FallSportsTeamID, EntityID = 1, returnFallSportsTeamID = True, returnCaptain = False, returnCreatedTime = False, returnFallSportID = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FallSportsTeam/" + str(FallSportsTeamID), verb = "get", return_params_list = return_params_list)

def modifyFallSportsTeam(FallSportsTeamID, EntityID = 1, setCaptain = None, setFallSportID = None, setLettered = None, setSchoolYearID = None, setStudentID = None, setRelationships = None, returnFallSportsTeamID = True, returnCaptain = False, returnCreatedTime = False, returnFallSportID = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FallSportsTeam/" + str(FallSportsTeamID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createFallSportsTeam(EntityID = 1, setCaptain = None, setFallSportID = None, setLettered = None, setSchoolYearID = None, setStudentID = None, setRelationships = None, returnFallSportsTeamID = True, returnCaptain = False, returnCreatedTime = False, returnFallSportID = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FallSportsTeam/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteFallSportsTeam(FallSportsTeamID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryFeederSchool(EntityID = 1, page = 1, pageSize = 100, returnFeederSchoolID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FeederSchool/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getFeederSchool(FeederSchoolID, EntityID = 1, returnFeederSchoolID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FeederSchool/" + str(FeederSchoolID), verb = "get", return_params_list = return_params_list)

def modifyFeederSchool(FeederSchoolID, EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setRelationships = None, returnFeederSchoolID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FeederSchool/" + str(FeederSchoolID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createFeederSchool(EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setRelationships = None, returnFeederSchoolID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FeederSchool/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteFeederSchool(FeederSchoolID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryIndicator(EntityID = 1, page = 1, pageSize = 100, returnIndicatorID = True, returnCreatedTime = False, returnImage = False, returnImageCode = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnRank = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Indicator/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getIndicator(IndicatorID, EntityID = 1, returnIndicatorID = True, returnCreatedTime = False, returnImage = False, returnImageCode = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnRank = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Indicator/" + str(IndicatorID), verb = "get", return_params_list = return_params_list)

def modifyIndicator(IndicatorID, EntityID = 1, setImage = None, setImageCode = None, setIsActive = None, setName = None, setRank = None, setSkywardID = None, setRelationships = None, returnIndicatorID = True, returnCreatedTime = False, returnImage = False, returnImageCode = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnRank = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Indicator/" + str(IndicatorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createIndicator(EntityID = 1, setImage = None, setImageCode = None, setIsActive = None, setName = None, setRank = None, setSkywardID = None, setRelationships = None, returnIndicatorID = True, returnCreatedTime = False, returnImage = False, returnImageCode = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnRank = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Indicator/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteIndicator(IndicatorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryLock(EntityID = 1, page = 1, pageSize = 100, returnLockID = True, returnBuildingID = False, returnCreatedTime = False, returnIsAssigned = False, returnIsAttached = False, returnIsAvailable = False, returnIsBuiltInLock = False, returnLockerID = False, returnLockMakeID = False, returnModifiedTime = False, returnOwnedBySchool = False, returnRenderRemoveLock = False, returnSerialNumber = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Lock/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getLock(LockID, EntityID = 1, returnLockID = True, returnBuildingID = False, returnCreatedTime = False, returnIsAssigned = False, returnIsAttached = False, returnIsAvailable = False, returnIsBuiltInLock = False, returnLockerID = False, returnLockMakeID = False, returnModifiedTime = False, returnOwnedBySchool = False, returnRenderRemoveLock = False, returnSerialNumber = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Lock/" + str(LockID), verb = "get", return_params_list = return_params_list)

def modifyLock(LockID, EntityID = 1, setBuildingID = None, setIsBuiltInLock = None, setLockerID = None, setLockMakeID = None, setOwnedBySchool = None, setSerialNumber = None, setStudentID = None, setRelationships = None, returnLockID = True, returnBuildingID = False, returnCreatedTime = False, returnIsAssigned = False, returnIsAttached = False, returnIsAvailable = False, returnIsBuiltInLock = False, returnLockerID = False, returnLockMakeID = False, returnModifiedTime = False, returnOwnedBySchool = False, returnRenderRemoveLock = False, returnSerialNumber = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Lock/" + str(LockID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createLock(EntityID = 1, setBuildingID = None, setIsBuiltInLock = None, setLockerID = None, setLockMakeID = None, setOwnedBySchool = None, setSerialNumber = None, setStudentID = None, setRelationships = None, returnLockID = True, returnBuildingID = False, returnCreatedTime = False, returnIsAssigned = False, returnIsAttached = False, returnIsAvailable = False, returnIsBuiltInLock = False, returnLockerID = False, returnLockMakeID = False, returnModifiedTime = False, returnOwnedBySchool = False, returnRenderRemoveLock = False, returnSerialNumber = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Lock/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteLock(LockID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryLockCombination(EntityID = 1, page = 1, pageSize = 100, returnLockCombinationID = True, returnCombination = False, returnCombinationNumber = False, returnCreatedTime = False, returnIsCurrentCombination = False, returnLockID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockCombination/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getLockCombination(LockCombinationID, EntityID = 1, returnLockCombinationID = True, returnCombination = False, returnCombinationNumber = False, returnCreatedTime = False, returnIsCurrentCombination = False, returnLockID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockCombination/" + str(LockCombinationID), verb = "get", return_params_list = return_params_list)

def modifyLockCombination(LockCombinationID, EntityID = 1, setCombination = None, setCombinationNumber = None, setIsCurrentCombination = None, setLockID = None, setRelationships = None, returnLockCombinationID = True, returnCombination = False, returnCombinationNumber = False, returnCreatedTime = False, returnIsCurrentCombination = False, returnLockID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockCombination/" + str(LockCombinationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createLockCombination(EntityID = 1, setCombination = None, setCombinationNumber = None, setIsCurrentCombination = None, setLockID = None, setRelationships = None, returnLockCombinationID = True, returnCombination = False, returnCombinationNumber = False, returnCreatedTime = False, returnIsCurrentCombination = False, returnLockID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockCombination/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteLockCombination(LockCombinationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryLocker(EntityID = 1, page = 1, pageSize = 100, returnLockerID = True, returnComment = False, returnCreatedTime = False, returnCurrentCombination = False, returnGender = False, returnGenderCode = False, returnGenderCount = False, returnHasBuiltInLock = False, returnIsActive = False, returnIsAvailable = False, returnIsDamaged = False, returnLockerAreaID = False, returnLockerNumber = False, returnModifiedTime = False, returnNeedsLock = False, returnStudentsPerLocker = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Locker/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getLocker(LockerID, EntityID = 1, returnLockerID = True, returnComment = False, returnCreatedTime = False, returnCurrentCombination = False, returnGender = False, returnGenderCode = False, returnGenderCount = False, returnHasBuiltInLock = False, returnIsActive = False, returnIsAvailable = False, returnIsDamaged = False, returnLockerAreaID = False, returnLockerNumber = False, returnModifiedTime = False, returnNeedsLock = False, returnStudentsPerLocker = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Locker/" + str(LockerID), verb = "get", return_params_list = return_params_list)

def modifyLocker(LockerID, EntityID = 1, setComment = None, setGender = None, setGenderCode = None, setGenderCount = None, setHasBuiltInLock = None, setIsActive = None, setIsDamaged = None, setLockerAreaID = None, setLockerNumber = None, setRelationships = None, returnLockerID = True, returnComment = False, returnCreatedTime = False, returnCurrentCombination = False, returnGender = False, returnGenderCode = False, returnGenderCount = False, returnHasBuiltInLock = False, returnIsActive = False, returnIsAvailable = False, returnIsDamaged = False, returnLockerAreaID = False, returnLockerNumber = False, returnModifiedTime = False, returnNeedsLock = False, returnStudentsPerLocker = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Locker/" + str(LockerID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createLocker(EntityID = 1, setComment = None, setGender = None, setGenderCode = None, setGenderCount = None, setHasBuiltInLock = None, setIsActive = None, setIsDamaged = None, setLockerAreaID = None, setLockerNumber = None, setRelationships = None, returnLockerID = True, returnComment = False, returnCreatedTime = False, returnCurrentCombination = False, returnGender = False, returnGenderCode = False, returnGenderCount = False, returnHasBuiltInLock = False, returnIsActive = False, returnIsAvailable = False, returnIsDamaged = False, returnLockerAreaID = False, returnLockerNumber = False, returnModifiedTime = False, returnNeedsLock = False, returnStudentsPerLocker = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Locker/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteLocker(LockerID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryLockerArea(EntityID = 1, page = 1, pageSize = 100, returnLockerAreaID = True, returnAllowCoedLocker = False, returnBuildingID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnHasBuiltInLockDefault = False, returnMaximumStudentsPerLocker = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockerArea/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getLockerArea(LockerAreaID, EntityID = 1, returnLockerAreaID = True, returnAllowCoedLocker = False, returnBuildingID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnHasBuiltInLockDefault = False, returnMaximumStudentsPerLocker = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockerArea/" + str(LockerAreaID), verb = "get", return_params_list = return_params_list)

def modifyLockerArea(LockerAreaID, EntityID = 1, setAllowCoedLocker = None, setBuildingID = None, setCode = None, setDescription = None, setHasBuiltInLockDefault = None, setMaximumStudentsPerLocker = None, setRelationships = None, returnLockerAreaID = True, returnAllowCoedLocker = False, returnBuildingID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnHasBuiltInLockDefault = False, returnMaximumStudentsPerLocker = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockerArea/" + str(LockerAreaID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createLockerArea(EntityID = 1, setAllowCoedLocker = None, setBuildingID = None, setCode = None, setDescription = None, setHasBuiltInLockDefault = None, setMaximumStudentsPerLocker = None, setRelationships = None, returnLockerAreaID = True, returnAllowCoedLocker = False, returnBuildingID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnHasBuiltInLockDefault = False, returnMaximumStudentsPerLocker = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockerArea/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteLockerArea(LockerAreaID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryLockMake(EntityID = 1, page = 1, pageSize = 100, returnLockMakeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockMake/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getLockMake(LockMakeID, EntityID = 1, returnLockMakeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockMake/" + str(LockMakeID), verb = "get", return_params_list = return_params_list)

def modifyLockMake(LockMakeID, EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnLockMakeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockMake/" + str(LockMakeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createLockMake(EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnLockMakeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockMake/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteLockMake(LockMakeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNextStudentNumber(EntityID = 1, page = 1, pageSize = 100, returnNextStudentNumberID = True, returnCreatedTime = False, returnIsForStateID = False, returnMaskPrefix = False, returnModifiedTime = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/NextStudentNumber/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNextStudentNumber(NextStudentNumberID, EntityID = 1, returnNextStudentNumberID = True, returnCreatedTime = False, returnIsForStateID = False, returnMaskPrefix = False, returnModifiedTime = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/NextStudentNumber/" + str(NextStudentNumberID), verb = "get", return_params_list = return_params_list)

def modifyNextStudentNumber(NextStudentNumberID, EntityID = 1, setIsForStateID = None, setMaskPrefix = None, setSequenceNumber = None, setRelationships = None, returnNextStudentNumberID = True, returnCreatedTime = False, returnIsForStateID = False, returnMaskPrefix = False, returnModifiedTime = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/NextStudentNumber/" + str(NextStudentNumberID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNextStudentNumber(EntityID = 1, setIsForStateID = None, setMaskPrefix = None, setSequenceNumber = None, setRelationships = None, returnNextStudentNumberID = True, returnCreatedTime = False, returnIsForStateID = False, returnMaskPrefix = False, returnModifiedTime = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/NextStudentNumber/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNextStudentNumber(NextStudentNumberID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNoteType(EntityID = 1, page = 1, pageSize = 100, returnNoteTypeID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnIndicatorID = False, returnIsActive = False, returnIsParentalConsent = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/NoteType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNoteType(NoteTypeID, EntityID = 1, returnNoteTypeID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnIndicatorID = False, returnIsActive = False, returnIsParentalConsent = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/NoteType/" + str(NoteTypeID), verb = "get", return_params_list = return_params_list)

def modifyNoteType(NoteTypeID, EntityID = 1, setCode = None, setDescription = None, setIndicatorID = None, setIsActive = None, setIsParentalConsent = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnNoteTypeID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnIndicatorID = False, returnIsActive = False, returnIsParentalConsent = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/NoteType/" + str(NoteTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNoteType(EntityID = 1, setCode = None, setDescription = None, setIndicatorID = None, setIsActive = None, setIsParentalConsent = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnNoteTypeID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnIndicatorID = False, returnIsActive = False, returnIsParentalConsent = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/NoteType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNoteType(NoteTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryReligion(EntityID = 1, page = 1, pageSize = 100, returnReligionID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Religion/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getReligion(ReligionID, EntityID = 1, returnReligionID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Religion/" + str(ReligionID), verb = "get", return_params_list = return_params_list)

def modifyReligion(ReligionID, EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnReligionID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Religion/" + str(ReligionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createReligion(EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnReligionID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Religion/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteReligion(ReligionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySkylertAttendanceExportAttendanceType(EntityID = 1, page = 1, pageSize = 100, returnSkylertAttendanceExportAttendanceTypeID = True, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnSkylertAttendanceExportSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportAttendanceType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSkylertAttendanceExportAttendanceType(SkylertAttendanceExportAttendanceTypeID, EntityID = 1, returnSkylertAttendanceExportAttendanceTypeID = True, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnSkylertAttendanceExportSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportAttendanceType/" + str(SkylertAttendanceExportAttendanceTypeID), verb = "get", return_params_list = return_params_list)

def modifySkylertAttendanceExportAttendanceType(SkylertAttendanceExportAttendanceTypeID, EntityID = 1, setAttendanceTypeID = None, setSkylertAttendanceExportSettingID = None, setRelationships = None, returnSkylertAttendanceExportAttendanceTypeID = True, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnSkylertAttendanceExportSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportAttendanceType/" + str(SkylertAttendanceExportAttendanceTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSkylertAttendanceExportAttendanceType(EntityID = 1, setAttendanceTypeID = None, setSkylertAttendanceExportSettingID = None, setRelationships = None, returnSkylertAttendanceExportAttendanceTypeID = True, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnSkylertAttendanceExportSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportAttendanceType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSkylertAttendanceExportAttendanceType(SkylertAttendanceExportAttendanceTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySkylertAttendanceExportSetting(EntityID = 1, page = 1, pageSize = 100, returnSkylertAttendanceExportSettingID = True, returnAttendancePeriodIDHigh = False, returnAttendancePeriodIDLow = False, returnCreatedTime = False, returnEntityID = False, returnFileSequence = False, returnMinimumPeriodsAbsent = False, returnModifiedTime = False, returnParentNotifiedOption = False, returnParentNotifiedOptionCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSkylertAttendanceExportSetting(SkylertAttendanceExportSettingID, EntityID = 1, returnSkylertAttendanceExportSettingID = True, returnAttendancePeriodIDHigh = False, returnAttendancePeriodIDLow = False, returnCreatedTime = False, returnEntityID = False, returnFileSequence = False, returnMinimumPeriodsAbsent = False, returnModifiedTime = False, returnParentNotifiedOption = False, returnParentNotifiedOptionCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportSetting/" + str(SkylertAttendanceExportSettingID), verb = "get", return_params_list = return_params_list)

def modifySkylertAttendanceExportSetting(SkylertAttendanceExportSettingID, EntityID = 1, setAttendancePeriodIDHigh = None, setAttendancePeriodIDLow = None, setEntityID = None, setFileSequence = None, setMinimumPeriodsAbsent = None, setParentNotifiedOption = None, setParentNotifiedOptionCode = None, setSchoolYearID = None, setRelationships = None, returnSkylertAttendanceExportSettingID = True, returnAttendancePeriodIDHigh = False, returnAttendancePeriodIDLow = False, returnCreatedTime = False, returnEntityID = False, returnFileSequence = False, returnMinimumPeriodsAbsent = False, returnModifiedTime = False, returnParentNotifiedOption = False, returnParentNotifiedOptionCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportSetting/" + str(SkylertAttendanceExportSettingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSkylertAttendanceExportSetting(EntityID = 1, setAttendancePeriodIDHigh = None, setAttendancePeriodIDLow = None, setEntityID = None, setFileSequence = None, setMinimumPeriodsAbsent = None, setParentNotifiedOption = None, setParentNotifiedOptionCode = None, setSchoolYearID = None, setRelationships = None, returnSkylertAttendanceExportSettingID = True, returnAttendancePeriodIDHigh = False, returnAttendancePeriodIDLow = False, returnCreatedTime = False, returnEntityID = False, returnFileSequence = False, returnMinimumPeriodsAbsent = False, returnModifiedTime = False, returnParentNotifiedOption = False, returnParentNotifiedOptionCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportSetting/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSkylertAttendanceExportSetting(SkylertAttendanceExportSettingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySkylertAttendanceExportSettingScheduledTask(EntityID = 1, page = 1, pageSize = 100, returnSkylertAttendanceExportSettingScheduledTaskID = True, returnCreatedTime = False, returnModifiedTime = False, returnScheduledTaskID = False, returnSkylertAttendanceExportSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportSettingScheduledTask/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSkylertAttendanceExportSettingScheduledTask(SkylertAttendanceExportSettingScheduledTaskID, EntityID = 1, returnSkylertAttendanceExportSettingScheduledTaskID = True, returnCreatedTime = False, returnModifiedTime = False, returnScheduledTaskID = False, returnSkylertAttendanceExportSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportSettingScheduledTask/" + str(SkylertAttendanceExportSettingScheduledTaskID), verb = "get", return_params_list = return_params_list)

def modifySkylertAttendanceExportSettingScheduledTask(SkylertAttendanceExportSettingScheduledTaskID, EntityID = 1, setScheduledTaskID = None, setSkylertAttendanceExportSettingID = None, setRelationships = None, returnSkylertAttendanceExportSettingScheduledTaskID = True, returnCreatedTime = False, returnModifiedTime = False, returnScheduledTaskID = False, returnSkylertAttendanceExportSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportSettingScheduledTask/" + str(SkylertAttendanceExportSettingScheduledTaskID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSkylertAttendanceExportSettingScheduledTask(EntityID = 1, setScheduledTaskID = None, setSkylertAttendanceExportSettingID = None, setRelationships = None, returnSkylertAttendanceExportSettingScheduledTaskID = True, returnCreatedTime = False, returnModifiedTime = False, returnScheduledTaskID = False, returnSkylertAttendanceExportSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportSettingScheduledTask/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSkylertAttendanceExportSettingScheduledTask(SkylertAttendanceExportSettingScheduledTaskID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySpringSport(EntityID = 1, page = 1, pageSize = 100, returnSpringSportID = True, returnCode = False, returnCreatedTime = False, returnModifiedTime = False, returnSpringSport = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SpringSport/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSpringSport(SpringSportID, EntityID = 1, returnSpringSportID = True, returnCode = False, returnCreatedTime = False, returnModifiedTime = False, returnSpringSport = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SpringSport/" + str(SpringSportID), verb = "get", return_params_list = return_params_list)

def modifySpringSport(SpringSportID, EntityID = 1, setCode = None, setSpringSport = None, setRelationships = None, returnSpringSportID = True, returnCode = False, returnCreatedTime = False, returnModifiedTime = False, returnSpringSport = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SpringSport/" + str(SpringSportID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSpringSport(EntityID = 1, setCode = None, setSpringSport = None, setRelationships = None, returnSpringSportID = True, returnCode = False, returnCreatedTime = False, returnModifiedTime = False, returnSpringSport = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SpringSport/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSpringSport(SpringSportID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySpringSportsTeam(EntityID = 1, page = 1, pageSize = 100, returnSpringSportsTeamID = True, returnCaptain = False, returnCreatedTime = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnSpringSportID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SpringSportsTeam/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSpringSportsTeam(SpringSportsTeamID, EntityID = 1, returnSpringSportsTeamID = True, returnCaptain = False, returnCreatedTime = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnSpringSportID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SpringSportsTeam/" + str(SpringSportsTeamID), verb = "get", return_params_list = return_params_list)

def modifySpringSportsTeam(SpringSportsTeamID, EntityID = 1, setCaptain = None, setLettered = None, setSchoolYearID = None, setSpringSportID = None, setStudentID = None, setRelationships = None, returnSpringSportsTeamID = True, returnCaptain = False, returnCreatedTime = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnSpringSportID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SpringSportsTeam/" + str(SpringSportsTeamID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSpringSportsTeam(EntityID = 1, setCaptain = None, setLettered = None, setSchoolYearID = None, setSpringSportID = None, setStudentID = None, setRelationships = None, returnSpringSportsTeamID = True, returnCaptain = False, returnCreatedTime = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnSpringSportID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SpringSportsTeam/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSpringSportsTeam(SpringSportsTeamID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentActivity(EntityID = 1, page = 1, pageSize = 100, returnStudentActivityID = True, returnActivityID = False, returnCourseID = False, returnCreatedTime = False, returnIsActive = False, returnModifiedTime = False, returnStudentActivityIDClonedFrom = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentActivity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentActivity(StudentActivityID, EntityID = 1, returnStudentActivityID = True, returnActivityID = False, returnCourseID = False, returnCreatedTime = False, returnIsActive = False, returnModifiedTime = False, returnStudentActivityIDClonedFrom = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentActivity/" + str(StudentActivityID), verb = "get", return_params_list = return_params_list)

def modifyStudentActivity(StudentActivityID, EntityID = 1, setActivityID = None, setCourseID = None, setIsActive = None, setStudentActivityIDClonedFrom = None, setStudentID = None, setRelationships = None, returnStudentActivityID = True, returnActivityID = False, returnCourseID = False, returnCreatedTime = False, returnIsActive = False, returnModifiedTime = False, returnStudentActivityIDClonedFrom = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentActivity/" + str(StudentActivityID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentActivity(EntityID = 1, setActivityID = None, setCourseID = None, setIsActive = None, setStudentActivityIDClonedFrom = None, setStudentID = None, setRelationships = None, returnStudentActivityID = True, returnActivityID = False, returnCourseID = False, returnCreatedTime = False, returnIsActive = False, returnModifiedTime = False, returnStudentActivityIDClonedFrom = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentActivity/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentActivity(StudentActivityID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentActivityTransaction(EntityID = 1, page = 1, pageSize = 100, returnStudentActivityTransactionID = True, returnCreatedTime = False, returnModifiedTime = False, returnParticipationEndDate = False, returnParticipationStartDate = False, returnStudentActivityID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentActivityTransaction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentActivityTransaction(StudentActivityTransactionID, EntityID = 1, returnStudentActivityTransactionID = True, returnCreatedTime = False, returnModifiedTime = False, returnParticipationEndDate = False, returnParticipationStartDate = False, returnStudentActivityID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentActivityTransaction/" + str(StudentActivityTransactionID), verb = "get", return_params_list = return_params_list)

def modifyStudentActivityTransaction(StudentActivityTransactionID, EntityID = 1, setParticipationEndDate = None, setParticipationStartDate = None, setStudentActivityID = None, setRelationships = None, returnStudentActivityTransactionID = True, returnCreatedTime = False, returnModifiedTime = False, returnParticipationEndDate = False, returnParticipationStartDate = False, returnStudentActivityID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentActivityTransaction/" + str(StudentActivityTransactionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentActivityTransaction(EntityID = 1, setParticipationEndDate = None, setParticipationStartDate = None, setStudentActivityID = None, setRelationships = None, returnStudentActivityTransactionID = True, returnCreatedTime = False, returnModifiedTime = False, returnParticipationEndDate = False, returnParticipationStartDate = False, returnStudentActivityID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentActivityTransaction/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentActivityTransaction(StudentActivityTransactionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentCustomCode(EntityID = 1, page = 1, pageSize = 100, returnStudentCustomCodeID = True, returnCreatedTime = False, returnCustomCodeID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentCustomCode/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentCustomCode(StudentCustomCodeID, EntityID = 1, returnStudentCustomCodeID = True, returnCreatedTime = False, returnCustomCodeID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentCustomCode/" + str(StudentCustomCodeID), verb = "get", return_params_list = return_params_list)

def modifyStudentCustomCode(StudentCustomCodeID, EntityID = 1, setCustomCodeID = None, setStudentID = None, setRelationships = None, returnStudentCustomCodeID = True, returnCreatedTime = False, returnCustomCodeID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentCustomCode/" + str(StudentCustomCodeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentCustomCode(EntityID = 1, setCustomCodeID = None, setStudentID = None, setRelationships = None, returnStudentCustomCodeID = True, returnCreatedTime = False, returnCustomCodeID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentCustomCode/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentCustomCode(StudentCustomCodeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentDistrict(EntityID = 1, page = 1, pageSize = 100, returnStudentDistrictID = True, returnCreatedTime = False, returnDistrictID = False, returnFeederSchoolID = False, returnFirstName = False, returnGrade = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnPermitID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentDistrict/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentDistrict(StudentDistrictID, EntityID = 1, returnStudentDistrictID = True, returnCreatedTime = False, returnDistrictID = False, returnFeederSchoolID = False, returnFirstName = False, returnGrade = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnPermitID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentDistrict/" + str(StudentDistrictID), verb = "get", return_params_list = return_params_list)

def modifyStudentDistrict(StudentDistrictID, EntityID = 1, setDistrictID = None, setFeederSchoolID = None, setFirstName = None, setGrade = None, setLastName = None, setMiddleName = None, setNameID = None, setPermitID = None, setStudentID = None, setStudentNumber = None, setRelationships = None, returnStudentDistrictID = True, returnCreatedTime = False, returnDistrictID = False, returnFeederSchoolID = False, returnFirstName = False, returnGrade = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnPermitID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentDistrict/" + str(StudentDistrictID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentDistrict(EntityID = 1, setDistrictID = None, setFeederSchoolID = None, setFirstName = None, setGrade = None, setLastName = None, setMiddleName = None, setNameID = None, setPermitID = None, setStudentID = None, setStudentNumber = None, setRelationships = None, returnStudentDistrictID = True, returnCreatedTime = False, returnDistrictID = False, returnFeederSchoolID = False, returnFirstName = False, returnGrade = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnPermitID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentDistrict/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentDistrict(StudentDistrictID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentLocker(EntityID = 1, page = 1, pageSize = 100, returnStudentLockerID = True, returnCreatedTime = False, returnIsPrimaryLocker = False, returnLockerID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentLocker/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentLocker(StudentLockerID, EntityID = 1, returnStudentLockerID = True, returnCreatedTime = False, returnIsPrimaryLocker = False, returnLockerID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentLocker/" + str(StudentLockerID), verb = "get", return_params_list = return_params_list)

def modifyStudentLocker(StudentLockerID, EntityID = 1, setIsPrimaryLocker = None, setLockerID = None, setStudentID = None, setRelationships = None, returnStudentLockerID = True, returnCreatedTime = False, returnIsPrimaryLocker = False, returnLockerID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentLocker/" + str(StudentLockerID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentLocker(EntityID = 1, setIsPrimaryLocker = None, setLockerID = None, setStudentID = None, setRelationships = None, returnStudentLockerID = True, returnCreatedTime = False, returnIsPrimaryLocker = False, returnLockerID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentLocker/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentLocker(StudentLockerID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentMassUpdate(EntityID = 1, page = 1, pageSize = 100, returnStudentMassUpdateID = True, returnAsOfDate = False, returnCreatedTime = False, returnDistrictID = False, returnFilterParameters = False, returnModifiedTime = False, returnRunReason = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRanBy = False, returnValueParameters = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentMassUpdate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentMassUpdate(StudentMassUpdateID, EntityID = 1, returnStudentMassUpdateID = True, returnAsOfDate = False, returnCreatedTime = False, returnDistrictID = False, returnFilterParameters = False, returnModifiedTime = False, returnRunReason = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRanBy = False, returnValueParameters = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentMassUpdate/" + str(StudentMassUpdateID), verb = "get", return_params_list = return_params_list)

def modifyStudentMassUpdate(StudentMassUpdateID, EntityID = 1, setAsOfDate = None, setDistrictID = None, setFilterParameters = None, setRunReason = None, setSchoolYearID = None, setUserIDRanBy = None, setValueParameters = None, setRelationships = None, returnStudentMassUpdateID = True, returnAsOfDate = False, returnCreatedTime = False, returnDistrictID = False, returnFilterParameters = False, returnModifiedTime = False, returnRunReason = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRanBy = False, returnValueParameters = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentMassUpdate/" + str(StudentMassUpdateID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentMassUpdate(EntityID = 1, setAsOfDate = None, setDistrictID = None, setFilterParameters = None, setRunReason = None, setSchoolYearID = None, setUserIDRanBy = None, setValueParameters = None, setRelationships = None, returnStudentMassUpdateID = True, returnAsOfDate = False, returnCreatedTime = False, returnDistrictID = False, returnFilterParameters = False, returnModifiedTime = False, returnRunReason = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRanBy = False, returnValueParameters = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentMassUpdate/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentMassUpdate(StudentMassUpdateID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentMedia(EntityID = 1, page = 1, pageSize = 100, returnStudentMediaID = True, returnAttachmentTypeID = False, returnCreatedTime = False, returnDisplayInTeacherAccess = False, returnDisplayName = False, returnDisplayNameOrMediaName = False, returnMediaID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentMedia/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentMedia(StudentMediaID, EntityID = 1, returnStudentMediaID = True, returnAttachmentTypeID = False, returnCreatedTime = False, returnDisplayInTeacherAccess = False, returnDisplayName = False, returnDisplayNameOrMediaName = False, returnMediaID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentMedia/" + str(StudentMediaID), verb = "get", return_params_list = return_params_list)

def modifyStudentMedia(StudentMediaID, EntityID = 1, setAttachmentTypeID = None, setDisplayInTeacherAccess = None, setDisplayName = None, setMediaID = None, setStudentID = None, setRelationships = None, returnStudentMediaID = True, returnAttachmentTypeID = False, returnCreatedTime = False, returnDisplayInTeacherAccess = False, returnDisplayName = False, returnDisplayNameOrMediaName = False, returnMediaID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentMedia/" + str(StudentMediaID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentMedia(EntityID = 1, setAttachmentTypeID = None, setDisplayInTeacherAccess = None, setDisplayName = None, setMediaID = None, setStudentID = None, setRelationships = None, returnStudentMediaID = True, returnAttachmentTypeID = False, returnCreatedTime = False, returnDisplayInTeacherAccess = False, returnDisplayName = False, returnDisplayNameOrMediaName = False, returnMediaID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentMedia/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentMedia(StudentMediaID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudent(EntityID = 1, page = 1, pageSize = 100, returnStudentID = True, returnAllowCustomerCategoryAdd = False, returnAllowDistrictDistribution = False, returnAllowHigherEdDistribution = False, returnAllowLocalDistribution = False, returnAllowMediaDistribution = False, returnAllowMilitaryDistribution = False, returnAllowPublicDistribution = False, returnAllowStudentAccess = False, returnAllowTripsDistribution = False, returnAllowVendorsDistribution = False, returnArrestCount = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCalculatedEntityYearIsActive = False, returnCalculatedGrade = False, returnCalculatedGradYear = False, returnCalculatedLocation = False, returnCalculatedPrimaryFormattedPhoneNumber = False, returnCalculatedStudentStateID = False, returnConversionKey = False, returnCorporalPunishmentIncidents = False, returnCreatedTime = False, returnCurrentDefaultEntityIsActive = False, returnCurrentEconomicIndicator = False, returnCurrentTransportationMaintenance = False, returnDateOfFirstEntryWithdrawalInEntity = False, returnDentalPolicyNumber = False, returnDisciplinedBullyingDisability = False, returnDisciplinedBullyingRace = False, returnDisciplinedBullyingSex = False, returnEarliestDistrictEnrollmentDate = False, returnEarnedCredits = False, returnEarnedCreditsPossible = False, returnEdFiCountryIDBirth = False, returnEntityConfigEarnedCredits = False, returnEntityConfigFailedCredits = False, returnEntryWithdrawalIDDefaultEntityToday = False, returnExpulsionWithoutServicesCount = False, returnExpulsionWithServicesCount = False, returnFailedCredits = False, returnFeeOnlinePaymentOverrideType = False, returnFeeOnlinePaymentOverrideTypeCode = False, returnFirstName = False, returnFoodServiceOnlinePaymentOverrideType = False, returnFoodServiceOnlinePaymentOverrideTypeCode = False, returnFormattedVaccinationDates = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnGrade = False, returnGradeNumeric = False, returnGraduationDate = False, returnGraduationRequirementYear = False, returnGradYear = False, returnHasActiveAlert = False, returnHasActiveCriticalAlert = False, returnHasActiveGeneralNote = False, returnHasActiveHealthCondition = False, returnHasActiveIHP = False, returnHasActiveParentalConsentNote = False, returnHasActiveSection504 = False, returnHasActiveSpecialEducation = False, returnHasActiveStudentGuardianRestrictedAccess = False, returnHasAdvancedMathGrade0912 = False, returnHasAlertIndicator = False, returnHasAlgebraIGrade07 = False, returnHasAlgebraIGrade08 = False, returnHasAlgebraIGrade0910 = False, returnHasAlgebraIGrade1112 = False, returnHasAlgebraIIGrade0912 = False, returnHasAllowStudentAccessButNoSecurity = False, returnHasAPComputerScienceGrade0912 = False, returnHasAPCourseGrade0912 = False, returnHasAPMathGrade0912 = False, returnHasAPOtherGrade0912 = False, returnHasAPScienceGrade0912 = False, returnHasBiologyGrade0912 = False, returnHasCalculusGrade0912 = False, returnHasChemistryGrade0912 = False, returnHasComputerScienceGrade0912 = False, returnHasCreditRecovery = False, returnHasCriticalAlertIndicator = False, returnHasDuplicateStudentNumber = False, returnHasGeneralNoteIndicator = False, returnHasGeometryGrade08 = False, returnHasGeometryGrade0912 = False, returnHasHealthIndicator = False, returnHasIHPIndicator = False, returnHasOneNormalEnrollmentInEntityDuringSchoolYear = False, returnHasParentalConsentNoteIndicator = False, returnHasPassedAlgebraIGrade07 = False, returnHasPassedAlgebraIGrade08 = False, returnHasPassedAlgebraIGrade0910 = False, returnHasPassedAlgebraIGrade1112 = False, returnHasPhysicsGrade0912 = False, returnHasSection504Indicator = False, returnHasSpecialEducationIndicator = False, returnHasStudentEntityYearForCurrentSchoolYear = False, returnHasStudentGuardianWithAllowFamilyAccessButNoSecurity = False, returnHasTakenACT0912 = False, returnHasTakenAPExam0912 = False, returnHasTakenSAT0912 = False, returnHealthPolicyNumber = False, returnHealthProfessionalIDDentist = False, returnHealthProfessionalIDPrimaryPhysician = False, returnIndicatorsXML = False, returnInSchoolSuspensionCount = False, returnIsActiveAsOfDate = False, returnIsChronicallyAbsent = False, returnIsCurrentActive = False, returnIsCurrentActiveDefaultEnrollment = False, returnIsCurrentlyTransported = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnIsGiftedTalentedSnapshot = False, returnIsGraduated = False, returnIsHealthProfessionalDentist = False, returnIsHealthProfessionalPrimaryPhysician = False, returnIsIBDiplomaProgramme = False, returnIsIDEA = False, returnIsIDEASnapshot = False, returnIsLEP = False, returnIsLEPSnapshot = False, returnIsSection504 = False, returnIsSection504Snapshot = False, returnIsStateReportingUnknownGender = False, returnLanguageIDNative = False, returnLanguageIDPrimary = False, returnLastName = False, returnLawEnforcementReferralCount = False, returnLocation = False, returnLocationDateToUse = False, returnLocationEntityID = False, returnLocationSchoolYearID = False, returnMaskedStudentNumber = False, returnMechanicalRestraintCount = False, returnMedicaidNumber = False, returnMiddleName = False, returnMMRStatus = False, returnModifiedTime = False, returnNameID = False, returnNameIDDentalInsuranceCompany = False, returnNameIDDentalPractice = False, returnNameIDHealthInsuranceCompany = False, returnNameIDHospital = False, returnOutOfSchoolSuspensionCount = False, returnOutOfSchoolSuspensionMissedDays = False, returnOverrideFeeOnlinePaymentAccess = False, returnOverrideFoodServiceOnlinePaymentAccess = False, returnPhysicalRestraintCount = False, returnReportedBulliedDisability = False, returnReportedBulliedRace = False, returnReportedBulliedSex = False, returnSchoolPathExpectedSchoolCode = False, returnSchoolPathExpectedSchoolName = False, returnSchoolYearIDSpecifiedCohort = False, returnSeclusionCount = False, returnSingleSexAthleticCount = False, returnSpecifiedCohortNumericSchoolYear = False, returnSpecifiedEntityYearNoShow = False, returnStateEthnicityRaceCodeMNID = False, returnStudentIDHash = False, returnStudentIndicatorColumn = False, returnStudentMNID = False, returnStudentNumber = False, returnStudentNumberForGradebook = False, returnStudentRankSort = False, returnStudentStateID = False, returnTransferToAlternativeSchool = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLIndicators = False, returnZeroToleranceWithoutServicesCount = False, returnZeroToleranceWithServicesCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Student/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudent(StudentID, EntityID = 1, returnStudentID = True, returnAllowCustomerCategoryAdd = False, returnAllowDistrictDistribution = False, returnAllowHigherEdDistribution = False, returnAllowLocalDistribution = False, returnAllowMediaDistribution = False, returnAllowMilitaryDistribution = False, returnAllowPublicDistribution = False, returnAllowStudentAccess = False, returnAllowTripsDistribution = False, returnAllowVendorsDistribution = False, returnArrestCount = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCalculatedEntityYearIsActive = False, returnCalculatedGrade = False, returnCalculatedGradYear = False, returnCalculatedLocation = False, returnCalculatedPrimaryFormattedPhoneNumber = False, returnCalculatedStudentStateID = False, returnConversionKey = False, returnCorporalPunishmentIncidents = False, returnCreatedTime = False, returnCurrentDefaultEntityIsActive = False, returnCurrentEconomicIndicator = False, returnCurrentTransportationMaintenance = False, returnDateOfFirstEntryWithdrawalInEntity = False, returnDentalPolicyNumber = False, returnDisciplinedBullyingDisability = False, returnDisciplinedBullyingRace = False, returnDisciplinedBullyingSex = False, returnEarliestDistrictEnrollmentDate = False, returnEarnedCredits = False, returnEarnedCreditsPossible = False, returnEdFiCountryIDBirth = False, returnEntityConfigEarnedCredits = False, returnEntityConfigFailedCredits = False, returnEntryWithdrawalIDDefaultEntityToday = False, returnExpulsionWithoutServicesCount = False, returnExpulsionWithServicesCount = False, returnFailedCredits = False, returnFeeOnlinePaymentOverrideType = False, returnFeeOnlinePaymentOverrideTypeCode = False, returnFirstName = False, returnFoodServiceOnlinePaymentOverrideType = False, returnFoodServiceOnlinePaymentOverrideTypeCode = False, returnFormattedVaccinationDates = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnGrade = False, returnGradeNumeric = False, returnGraduationDate = False, returnGraduationRequirementYear = False, returnGradYear = False, returnHasActiveAlert = False, returnHasActiveCriticalAlert = False, returnHasActiveGeneralNote = False, returnHasActiveHealthCondition = False, returnHasActiveIHP = False, returnHasActiveParentalConsentNote = False, returnHasActiveSection504 = False, returnHasActiveSpecialEducation = False, returnHasActiveStudentGuardianRestrictedAccess = False, returnHasAdvancedMathGrade0912 = False, returnHasAlertIndicator = False, returnHasAlgebraIGrade07 = False, returnHasAlgebraIGrade08 = False, returnHasAlgebraIGrade0910 = False, returnHasAlgebraIGrade1112 = False, returnHasAlgebraIIGrade0912 = False, returnHasAllowStudentAccessButNoSecurity = False, returnHasAPComputerScienceGrade0912 = False, returnHasAPCourseGrade0912 = False, returnHasAPMathGrade0912 = False, returnHasAPOtherGrade0912 = False, returnHasAPScienceGrade0912 = False, returnHasBiologyGrade0912 = False, returnHasCalculusGrade0912 = False, returnHasChemistryGrade0912 = False, returnHasComputerScienceGrade0912 = False, returnHasCreditRecovery = False, returnHasCriticalAlertIndicator = False, returnHasDuplicateStudentNumber = False, returnHasGeneralNoteIndicator = False, returnHasGeometryGrade08 = False, returnHasGeometryGrade0912 = False, returnHasHealthIndicator = False, returnHasIHPIndicator = False, returnHasOneNormalEnrollmentInEntityDuringSchoolYear = False, returnHasParentalConsentNoteIndicator = False, returnHasPassedAlgebraIGrade07 = False, returnHasPassedAlgebraIGrade08 = False, returnHasPassedAlgebraIGrade0910 = False, returnHasPassedAlgebraIGrade1112 = False, returnHasPhysicsGrade0912 = False, returnHasSection504Indicator = False, returnHasSpecialEducationIndicator = False, returnHasStudentEntityYearForCurrentSchoolYear = False, returnHasStudentGuardianWithAllowFamilyAccessButNoSecurity = False, returnHasTakenACT0912 = False, returnHasTakenAPExam0912 = False, returnHasTakenSAT0912 = False, returnHealthPolicyNumber = False, returnHealthProfessionalIDDentist = False, returnHealthProfessionalIDPrimaryPhysician = False, returnIndicatorsXML = False, returnInSchoolSuspensionCount = False, returnIsActiveAsOfDate = False, returnIsChronicallyAbsent = False, returnIsCurrentActive = False, returnIsCurrentActiveDefaultEnrollment = False, returnIsCurrentlyTransported = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnIsGiftedTalentedSnapshot = False, returnIsGraduated = False, returnIsHealthProfessionalDentist = False, returnIsHealthProfessionalPrimaryPhysician = False, returnIsIBDiplomaProgramme = False, returnIsIDEA = False, returnIsIDEASnapshot = False, returnIsLEP = False, returnIsLEPSnapshot = False, returnIsSection504 = False, returnIsSection504Snapshot = False, returnIsStateReportingUnknownGender = False, returnLanguageIDNative = False, returnLanguageIDPrimary = False, returnLastName = False, returnLawEnforcementReferralCount = False, returnLocation = False, returnLocationDateToUse = False, returnLocationEntityID = False, returnLocationSchoolYearID = False, returnMaskedStudentNumber = False, returnMechanicalRestraintCount = False, returnMedicaidNumber = False, returnMiddleName = False, returnMMRStatus = False, returnModifiedTime = False, returnNameID = False, returnNameIDDentalInsuranceCompany = False, returnNameIDDentalPractice = False, returnNameIDHealthInsuranceCompany = False, returnNameIDHospital = False, returnOutOfSchoolSuspensionCount = False, returnOutOfSchoolSuspensionMissedDays = False, returnOverrideFeeOnlinePaymentAccess = False, returnOverrideFoodServiceOnlinePaymentAccess = False, returnPhysicalRestraintCount = False, returnReportedBulliedDisability = False, returnReportedBulliedRace = False, returnReportedBulliedSex = False, returnSchoolPathExpectedSchoolCode = False, returnSchoolPathExpectedSchoolName = False, returnSchoolYearIDSpecifiedCohort = False, returnSeclusionCount = False, returnSingleSexAthleticCount = False, returnSpecifiedCohortNumericSchoolYear = False, returnSpecifiedEntityYearNoShow = False, returnStateEthnicityRaceCodeMNID = False, returnStudentIDHash = False, returnStudentIndicatorColumn = False, returnStudentMNID = False, returnStudentNumber = False, returnStudentNumberForGradebook = False, returnStudentRankSort = False, returnStudentStateID = False, returnTransferToAlternativeSchool = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLIndicators = False, returnZeroToleranceWithoutServicesCount = False, returnZeroToleranceWithServicesCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Student/" + str(StudentID), verb = "get", return_params_list = return_params_list)

def modifyStudent(StudentID, EntityID = 1, setAllowDistrictDistribution = None, setAllowHigherEdDistribution = None, setAllowLocalDistribution = None, setAllowMediaDistribution = None, setAllowMilitaryDistribution = None, setAllowPublicDistribution = None, setAllowStudentAccess = None, setAllowTripsDistribution = None, setAllowVendorsDistribution = None, setArrestCount = None, setConversionKey = None, setCorporalPunishmentIncidents = None, setDentalPolicyNumber = None, setDisciplinedBullyingDisability = None, setDisciplinedBullyingRace = None, setDisciplinedBullyingSex = None, setEarliestDistrictEnrollmentDate = None, setEdFiCountryIDBirth = None, setExpulsionWithoutServicesCount = None, setExpulsionWithServicesCount = None, setFeeOnlinePaymentOverrideType = None, setFeeOnlinePaymentOverrideTypeCode = None, setFirstName = None, setFoodServiceOnlinePaymentOverrideType = None, setFoodServiceOnlinePaymentOverrideTypeCode = None, setFullNameFL = None, setFullNameFML = None, setFullNameLFM = None, setGrade = None, setGradeNumeric = None, setGraduationDate = None, setGraduationRequirementYear = None, setGradYear = None, setHasAdvancedMathGrade0912 = None, setHasAlertIndicator = None, setHasAlgebraIGrade07 = None, setHasAlgebraIGrade08 = None, setHasAlgebraIGrade0910 = None, setHasAlgebraIGrade1112 = None, setHasAlgebraIIGrade0912 = None, setHasAPComputerScienceGrade0912 = None, setHasAPCourseGrade0912 = None, setHasAPMathGrade0912 = None, setHasAPOtherGrade0912 = None, setHasAPScienceGrade0912 = None, setHasBiologyGrade0912 = None, setHasCalculusGrade0912 = None, setHasChemistryGrade0912 = None, setHasComputerScienceGrade0912 = None, setHasCreditRecovery = None, setHasCriticalAlertIndicator = None, setHasGeneralNoteIndicator = None, setHasGeometryGrade08 = None, setHasGeometryGrade0912 = None, setHasHealthIndicator = None, setHasIHPIndicator = None, setHasParentalConsentNoteIndicator = None, setHasPassedAlgebraIGrade07 = None, setHasPassedAlgebraIGrade08 = None, setHasPassedAlgebraIGrade0910 = None, setHasPassedAlgebraIGrade1112 = None, setHasPhysicsGrade0912 = None, setHasSection504Indicator = None, setHasSpecialEducationIndicator = None, setHasTakenACT0912 = None, setHasTakenAPExam0912 = None, setHasTakenSAT0912 = None, setHealthPolicyNumber = None, setHealthProfessionalIDDentist = None, setHealthProfessionalIDPrimaryPhysician = None, setIndicatorsXML = None, setInSchoolSuspensionCount = None, setIsChronicallyAbsent = None, setIsFederalDistanceEducation = None, setIsFederalDualEnrollment = None, setIsGiftedTalentedSnapshot = None, setIsGraduated = None, setIsIBDiplomaProgramme = None, setIsIDEA = None, setIsIDEASnapshot = None, setIsLEP = None, setIsLEPSnapshot = None, setIsSection504 = None, setIsSection504Snapshot = None, setIsStateReportingUnknownGender = None, setLanguageIDNative = None, setLanguageIDPrimary = None, setLastName = None, setLawEnforcementReferralCount = None, setMechanicalRestraintCount = None, setMedicaidNumber = None, setMiddleName = None, setMMRStatus = None, setNameID = None, setNameIDDentalInsuranceCompany = None, setNameIDDentalPractice = None, setNameIDHealthInsuranceCompany = None, setNameIDHospital = None, setOutOfSchoolSuspensionCount = None, setOutOfSchoolSuspensionMissedDays = None, setOverrideFeeOnlinePaymentAccess = None, setOverrideFoodServiceOnlinePaymentAccess = None, setPhysicalRestraintCount = None, setReportedBulliedDisability = None, setReportedBulliedRace = None, setReportedBulliedSex = None, setSeclusionCount = None, setSingleSexAthleticCount = None, setStateEthnicityRaceCodeMNID = None, setStudentNumber = None, setStudentStateID = None, setTransferToAlternativeSchool = None, setXMLIndicators = None, setZeroToleranceWithoutServicesCount = None, setZeroToleranceWithServicesCount = None, setRelationships = None, returnStudentID = True, returnAllowCustomerCategoryAdd = False, returnAllowDistrictDistribution = False, returnAllowHigherEdDistribution = False, returnAllowLocalDistribution = False, returnAllowMediaDistribution = False, returnAllowMilitaryDistribution = False, returnAllowPublicDistribution = False, returnAllowStudentAccess = False, returnAllowTripsDistribution = False, returnAllowVendorsDistribution = False, returnArrestCount = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCalculatedEntityYearIsActive = False, returnCalculatedGrade = False, returnCalculatedGradYear = False, returnCalculatedLocation = False, returnCalculatedPrimaryFormattedPhoneNumber = False, returnCalculatedStudentStateID = False, returnConversionKey = False, returnCorporalPunishmentIncidents = False, returnCreatedTime = False, returnCurrentDefaultEntityIsActive = False, returnCurrentEconomicIndicator = False, returnCurrentTransportationMaintenance = False, returnDateOfFirstEntryWithdrawalInEntity = False, returnDentalPolicyNumber = False, returnDisciplinedBullyingDisability = False, returnDisciplinedBullyingRace = False, returnDisciplinedBullyingSex = False, returnEarliestDistrictEnrollmentDate = False, returnEarnedCredits = False, returnEarnedCreditsPossible = False, returnEdFiCountryIDBirth = False, returnEntityConfigEarnedCredits = False, returnEntityConfigFailedCredits = False, returnEntryWithdrawalIDDefaultEntityToday = False, returnExpulsionWithoutServicesCount = False, returnExpulsionWithServicesCount = False, returnFailedCredits = False, returnFeeOnlinePaymentOverrideType = False, returnFeeOnlinePaymentOverrideTypeCode = False, returnFirstName = False, returnFoodServiceOnlinePaymentOverrideType = False, returnFoodServiceOnlinePaymentOverrideTypeCode = False, returnFormattedVaccinationDates = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnGrade = False, returnGradeNumeric = False, returnGraduationDate = False, returnGraduationRequirementYear = False, returnGradYear = False, returnHasActiveAlert = False, returnHasActiveCriticalAlert = False, returnHasActiveGeneralNote = False, returnHasActiveHealthCondition = False, returnHasActiveIHP = False, returnHasActiveParentalConsentNote = False, returnHasActiveSection504 = False, returnHasActiveSpecialEducation = False, returnHasActiveStudentGuardianRestrictedAccess = False, returnHasAdvancedMathGrade0912 = False, returnHasAlertIndicator = False, returnHasAlgebraIGrade07 = False, returnHasAlgebraIGrade08 = False, returnHasAlgebraIGrade0910 = False, returnHasAlgebraIGrade1112 = False, returnHasAlgebraIIGrade0912 = False, returnHasAllowStudentAccessButNoSecurity = False, returnHasAPComputerScienceGrade0912 = False, returnHasAPCourseGrade0912 = False, returnHasAPMathGrade0912 = False, returnHasAPOtherGrade0912 = False, returnHasAPScienceGrade0912 = False, returnHasBiologyGrade0912 = False, returnHasCalculusGrade0912 = False, returnHasChemistryGrade0912 = False, returnHasComputerScienceGrade0912 = False, returnHasCreditRecovery = False, returnHasCriticalAlertIndicator = False, returnHasDuplicateStudentNumber = False, returnHasGeneralNoteIndicator = False, returnHasGeometryGrade08 = False, returnHasGeometryGrade0912 = False, returnHasHealthIndicator = False, returnHasIHPIndicator = False, returnHasOneNormalEnrollmentInEntityDuringSchoolYear = False, returnHasParentalConsentNoteIndicator = False, returnHasPassedAlgebraIGrade07 = False, returnHasPassedAlgebraIGrade08 = False, returnHasPassedAlgebraIGrade0910 = False, returnHasPassedAlgebraIGrade1112 = False, returnHasPhysicsGrade0912 = False, returnHasSection504Indicator = False, returnHasSpecialEducationIndicator = False, returnHasStudentEntityYearForCurrentSchoolYear = False, returnHasStudentGuardianWithAllowFamilyAccessButNoSecurity = False, returnHasTakenACT0912 = False, returnHasTakenAPExam0912 = False, returnHasTakenSAT0912 = False, returnHealthPolicyNumber = False, returnHealthProfessionalIDDentist = False, returnHealthProfessionalIDPrimaryPhysician = False, returnIndicatorsXML = False, returnInSchoolSuspensionCount = False, returnIsActiveAsOfDate = False, returnIsChronicallyAbsent = False, returnIsCurrentActive = False, returnIsCurrentActiveDefaultEnrollment = False, returnIsCurrentlyTransported = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnIsGiftedTalentedSnapshot = False, returnIsGraduated = False, returnIsHealthProfessionalDentist = False, returnIsHealthProfessionalPrimaryPhysician = False, returnIsIBDiplomaProgramme = False, returnIsIDEA = False, returnIsIDEASnapshot = False, returnIsLEP = False, returnIsLEPSnapshot = False, returnIsSection504 = False, returnIsSection504Snapshot = False, returnIsStateReportingUnknownGender = False, returnLanguageIDNative = False, returnLanguageIDPrimary = False, returnLastName = False, returnLawEnforcementReferralCount = False, returnLocation = False, returnLocationDateToUse = False, returnLocationEntityID = False, returnLocationSchoolYearID = False, returnMaskedStudentNumber = False, returnMechanicalRestraintCount = False, returnMedicaidNumber = False, returnMiddleName = False, returnMMRStatus = False, returnModifiedTime = False, returnNameID = False, returnNameIDDentalInsuranceCompany = False, returnNameIDDentalPractice = False, returnNameIDHealthInsuranceCompany = False, returnNameIDHospital = False, returnOutOfSchoolSuspensionCount = False, returnOutOfSchoolSuspensionMissedDays = False, returnOverrideFeeOnlinePaymentAccess = False, returnOverrideFoodServiceOnlinePaymentAccess = False, returnPhysicalRestraintCount = False, returnReportedBulliedDisability = False, returnReportedBulliedRace = False, returnReportedBulliedSex = False, returnSchoolPathExpectedSchoolCode = False, returnSchoolPathExpectedSchoolName = False, returnSchoolYearIDSpecifiedCohort = False, returnSeclusionCount = False, returnSingleSexAthleticCount = False, returnSpecifiedCohortNumericSchoolYear = False, returnSpecifiedEntityYearNoShow = False, returnStateEthnicityRaceCodeMNID = False, returnStudentIDHash = False, returnStudentIndicatorColumn = False, returnStudentMNID = False, returnStudentNumber = False, returnStudentNumberForGradebook = False, returnStudentRankSort = False, returnStudentStateID = False, returnTransferToAlternativeSchool = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLIndicators = False, returnZeroToleranceWithoutServicesCount = False, returnZeroToleranceWithServicesCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Student/" + str(StudentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudent(EntityID = 1, setAllowDistrictDistribution = None, setAllowHigherEdDistribution = None, setAllowLocalDistribution = None, setAllowMediaDistribution = None, setAllowMilitaryDistribution = None, setAllowPublicDistribution = None, setAllowStudentAccess = None, setAllowTripsDistribution = None, setAllowVendorsDistribution = None, setArrestCount = None, setConversionKey = None, setCorporalPunishmentIncidents = None, setDentalPolicyNumber = None, setDisciplinedBullyingDisability = None, setDisciplinedBullyingRace = None, setDisciplinedBullyingSex = None, setEarliestDistrictEnrollmentDate = None, setEdFiCountryIDBirth = None, setExpulsionWithoutServicesCount = None, setExpulsionWithServicesCount = None, setFeeOnlinePaymentOverrideType = None, setFeeOnlinePaymentOverrideTypeCode = None, setFirstName = None, setFoodServiceOnlinePaymentOverrideType = None, setFoodServiceOnlinePaymentOverrideTypeCode = None, setFullNameFL = None, setFullNameFML = None, setFullNameLFM = None, setGrade = None, setGradeNumeric = None, setGraduationDate = None, setGraduationRequirementYear = None, setGradYear = None, setHasAdvancedMathGrade0912 = None, setHasAlertIndicator = None, setHasAlgebraIGrade07 = None, setHasAlgebraIGrade08 = None, setHasAlgebraIGrade0910 = None, setHasAlgebraIGrade1112 = None, setHasAlgebraIIGrade0912 = None, setHasAPComputerScienceGrade0912 = None, setHasAPCourseGrade0912 = None, setHasAPMathGrade0912 = None, setHasAPOtherGrade0912 = None, setHasAPScienceGrade0912 = None, setHasBiologyGrade0912 = None, setHasCalculusGrade0912 = None, setHasChemistryGrade0912 = None, setHasComputerScienceGrade0912 = None, setHasCreditRecovery = None, setHasCriticalAlertIndicator = None, setHasGeneralNoteIndicator = None, setHasGeometryGrade08 = None, setHasGeometryGrade0912 = None, setHasHealthIndicator = None, setHasIHPIndicator = None, setHasParentalConsentNoteIndicator = None, setHasPassedAlgebraIGrade07 = None, setHasPassedAlgebraIGrade08 = None, setHasPassedAlgebraIGrade0910 = None, setHasPassedAlgebraIGrade1112 = None, setHasPhysicsGrade0912 = None, setHasSection504Indicator = None, setHasSpecialEducationIndicator = None, setHasTakenACT0912 = None, setHasTakenAPExam0912 = None, setHasTakenSAT0912 = None, setHealthPolicyNumber = None, setHealthProfessionalIDDentist = None, setHealthProfessionalIDPrimaryPhysician = None, setIndicatorsXML = None, setInSchoolSuspensionCount = None, setIsChronicallyAbsent = None, setIsFederalDistanceEducation = None, setIsFederalDualEnrollment = None, setIsGiftedTalentedSnapshot = None, setIsGraduated = None, setIsIBDiplomaProgramme = None, setIsIDEA = None, setIsIDEASnapshot = None, setIsLEP = None, setIsLEPSnapshot = None, setIsSection504 = None, setIsSection504Snapshot = None, setIsStateReportingUnknownGender = None, setLanguageIDNative = None, setLanguageIDPrimary = None, setLastName = None, setLawEnforcementReferralCount = None, setMechanicalRestraintCount = None, setMedicaidNumber = None, setMiddleName = None, setMMRStatus = None, setNameID = None, setNameIDDentalInsuranceCompany = None, setNameIDDentalPractice = None, setNameIDHealthInsuranceCompany = None, setNameIDHospital = None, setOutOfSchoolSuspensionCount = None, setOutOfSchoolSuspensionMissedDays = None, setOverrideFeeOnlinePaymentAccess = None, setOverrideFoodServiceOnlinePaymentAccess = None, setPhysicalRestraintCount = None, setReportedBulliedDisability = None, setReportedBulliedRace = None, setReportedBulliedSex = None, setSeclusionCount = None, setSingleSexAthleticCount = None, setStateEthnicityRaceCodeMNID = None, setStudentNumber = None, setStudentStateID = None, setTransferToAlternativeSchool = None, setXMLIndicators = None, setZeroToleranceWithoutServicesCount = None, setZeroToleranceWithServicesCount = None, setRelationships = None, returnStudentID = True, returnAllowCustomerCategoryAdd = False, returnAllowDistrictDistribution = False, returnAllowHigherEdDistribution = False, returnAllowLocalDistribution = False, returnAllowMediaDistribution = False, returnAllowMilitaryDistribution = False, returnAllowPublicDistribution = False, returnAllowStudentAccess = False, returnAllowTripsDistribution = False, returnAllowVendorsDistribution = False, returnArrestCount = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCalculatedEntityYearIsActive = False, returnCalculatedGrade = False, returnCalculatedGradYear = False, returnCalculatedLocation = False, returnCalculatedPrimaryFormattedPhoneNumber = False, returnCalculatedStudentStateID = False, returnConversionKey = False, returnCorporalPunishmentIncidents = False, returnCreatedTime = False, returnCurrentDefaultEntityIsActive = False, returnCurrentEconomicIndicator = False, returnCurrentTransportationMaintenance = False, returnDateOfFirstEntryWithdrawalInEntity = False, returnDentalPolicyNumber = False, returnDisciplinedBullyingDisability = False, returnDisciplinedBullyingRace = False, returnDisciplinedBullyingSex = False, returnEarliestDistrictEnrollmentDate = False, returnEarnedCredits = False, returnEarnedCreditsPossible = False, returnEdFiCountryIDBirth = False, returnEntityConfigEarnedCredits = False, returnEntityConfigFailedCredits = False, returnEntryWithdrawalIDDefaultEntityToday = False, returnExpulsionWithoutServicesCount = False, returnExpulsionWithServicesCount = False, returnFailedCredits = False, returnFeeOnlinePaymentOverrideType = False, returnFeeOnlinePaymentOverrideTypeCode = False, returnFirstName = False, returnFoodServiceOnlinePaymentOverrideType = False, returnFoodServiceOnlinePaymentOverrideTypeCode = False, returnFormattedVaccinationDates = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnGrade = False, returnGradeNumeric = False, returnGraduationDate = False, returnGraduationRequirementYear = False, returnGradYear = False, returnHasActiveAlert = False, returnHasActiveCriticalAlert = False, returnHasActiveGeneralNote = False, returnHasActiveHealthCondition = False, returnHasActiveIHP = False, returnHasActiveParentalConsentNote = False, returnHasActiveSection504 = False, returnHasActiveSpecialEducation = False, returnHasActiveStudentGuardianRestrictedAccess = False, returnHasAdvancedMathGrade0912 = False, returnHasAlertIndicator = False, returnHasAlgebraIGrade07 = False, returnHasAlgebraIGrade08 = False, returnHasAlgebraIGrade0910 = False, returnHasAlgebraIGrade1112 = False, returnHasAlgebraIIGrade0912 = False, returnHasAllowStudentAccessButNoSecurity = False, returnHasAPComputerScienceGrade0912 = False, returnHasAPCourseGrade0912 = False, returnHasAPMathGrade0912 = False, returnHasAPOtherGrade0912 = False, returnHasAPScienceGrade0912 = False, returnHasBiologyGrade0912 = False, returnHasCalculusGrade0912 = False, returnHasChemistryGrade0912 = False, returnHasComputerScienceGrade0912 = False, returnHasCreditRecovery = False, returnHasCriticalAlertIndicator = False, returnHasDuplicateStudentNumber = False, returnHasGeneralNoteIndicator = False, returnHasGeometryGrade08 = False, returnHasGeometryGrade0912 = False, returnHasHealthIndicator = False, returnHasIHPIndicator = False, returnHasOneNormalEnrollmentInEntityDuringSchoolYear = False, returnHasParentalConsentNoteIndicator = False, returnHasPassedAlgebraIGrade07 = False, returnHasPassedAlgebraIGrade08 = False, returnHasPassedAlgebraIGrade0910 = False, returnHasPassedAlgebraIGrade1112 = False, returnHasPhysicsGrade0912 = False, returnHasSection504Indicator = False, returnHasSpecialEducationIndicator = False, returnHasStudentEntityYearForCurrentSchoolYear = False, returnHasStudentGuardianWithAllowFamilyAccessButNoSecurity = False, returnHasTakenACT0912 = False, returnHasTakenAPExam0912 = False, returnHasTakenSAT0912 = False, returnHealthPolicyNumber = False, returnHealthProfessionalIDDentist = False, returnHealthProfessionalIDPrimaryPhysician = False, returnIndicatorsXML = False, returnInSchoolSuspensionCount = False, returnIsActiveAsOfDate = False, returnIsChronicallyAbsent = False, returnIsCurrentActive = False, returnIsCurrentActiveDefaultEnrollment = False, returnIsCurrentlyTransported = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnIsGiftedTalentedSnapshot = False, returnIsGraduated = False, returnIsHealthProfessionalDentist = False, returnIsHealthProfessionalPrimaryPhysician = False, returnIsIBDiplomaProgramme = False, returnIsIDEA = False, returnIsIDEASnapshot = False, returnIsLEP = False, returnIsLEPSnapshot = False, returnIsSection504 = False, returnIsSection504Snapshot = False, returnIsStateReportingUnknownGender = False, returnLanguageIDNative = False, returnLanguageIDPrimary = False, returnLastName = False, returnLawEnforcementReferralCount = False, returnLocation = False, returnLocationDateToUse = False, returnLocationEntityID = False, returnLocationSchoolYearID = False, returnMaskedStudentNumber = False, returnMechanicalRestraintCount = False, returnMedicaidNumber = False, returnMiddleName = False, returnMMRStatus = False, returnModifiedTime = False, returnNameID = False, returnNameIDDentalInsuranceCompany = False, returnNameIDDentalPractice = False, returnNameIDHealthInsuranceCompany = False, returnNameIDHospital = False, returnOutOfSchoolSuspensionCount = False, returnOutOfSchoolSuspensionMissedDays = False, returnOverrideFeeOnlinePaymentAccess = False, returnOverrideFoodServiceOnlinePaymentAccess = False, returnPhysicalRestraintCount = False, returnReportedBulliedDisability = False, returnReportedBulliedRace = False, returnReportedBulliedSex = False, returnSchoolPathExpectedSchoolCode = False, returnSchoolPathExpectedSchoolName = False, returnSchoolYearIDSpecifiedCohort = False, returnSeclusionCount = False, returnSingleSexAthleticCount = False, returnSpecifiedCohortNumericSchoolYear = False, returnSpecifiedEntityYearNoShow = False, returnStateEthnicityRaceCodeMNID = False, returnStudentIDHash = False, returnStudentIndicatorColumn = False, returnStudentMNID = False, returnStudentNumber = False, returnStudentNumberForGradebook = False, returnStudentRankSort = False, returnStudentStateID = False, returnTransferToAlternativeSchool = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLIndicators = False, returnZeroToleranceWithoutServicesCount = False, returnZeroToleranceWithServicesCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Student/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudent(StudentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentNote(EntityID = 1, page = 1, pageSize = 100, returnStudentNoteID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnNoteTypeID = False, returnStartDate = False, returnStudentID = False, returnStudentTransportationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentNote(StudentNoteID, EntityID = 1, returnStudentNoteID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnNoteTypeID = False, returnStartDate = False, returnStudentID = False, returnStudentTransportationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentNote/" + str(StudentNoteID), verb = "get", return_params_list = return_params_list)

def modifyStudentNote(StudentNoteID, EntityID = 1, setDescription = None, setEndDate = None, setIsActive = None, setNoteTypeID = None, setStartDate = None, setStudentID = None, setStudentTransportationID = None, setRelationships = None, returnStudentNoteID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnNoteTypeID = False, returnStartDate = False, returnStudentID = False, returnStudentTransportationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentNote/" + str(StudentNoteID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentNote(EntityID = 1, setDescription = None, setEndDate = None, setIsActive = None, setNoteTypeID = None, setStartDate = None, setStudentID = None, setStudentTransportationID = None, setRelationships = None, returnStudentNoteID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnNoteTypeID = False, returnStartDate = False, returnStudentID = False, returnStudentTransportationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentNote/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentNote(StudentNoteID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempActivityRecord(EntityID = 1, page = 1, pageSize = 100, returnTempActivityRecordID = True, returnActivityID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempActivityRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempActivityRecord(TempActivityRecordID, EntityID = 1, returnTempActivityRecordID = True, returnActivityID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempActivityRecord/" + str(TempActivityRecordID), verb = "get", return_params_list = return_params_list)

def modifyTempActivityRecord(TempActivityRecordID, EntityID = 1, setActivityID = None, setCode = None, setDescription = None, setNewEndDate = None, setNewStartDate = None, setRelationships = None, returnTempActivityRecordID = True, returnActivityID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempActivityRecord/" + str(TempActivityRecordID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempActivityRecord(EntityID = 1, setActivityID = None, setCode = None, setDescription = None, setNewEndDate = None, setNewStartDate = None, setRelationships = None, returnTempActivityRecordID = True, returnActivityID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempActivityRecord/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempActivityRecord(TempActivityRecordID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempFitnessGram(EntityID = 1, page = 1, pageSize = 100, returnTempFitnessGramID = True, returnClassDescription = False, returnClassEndDate = False, returnClassID = False, returnClassName = False, returnClassStartDate = False, returnCourseCodeDescription = False, returnCreatedTime = False, returnHasMissingData = False, returnMessage = False, returnModifiedTime = False, returnParentReportEmail1 = False, returnParentReportEmail2 = False, returnSchoolID = False, returnSectionCode = False, returnStudentBirthdate = False, returnStudentFirstName = False, returnStudentGender = False, returnStudentGrade = False, returnStudentID = False, returnStudentLastName = False, returnStudentMiddleInitial = False, returnStudentPassword = False, returnStudentReportEmail = False, returnStudentSSOID = False, returnTeacherBirthDate = False, returnTeacherEmail = False, returnTeacherFirstName = False, returnTeacherID = False, returnTeacherLastName = False, returnTeacherMiddleInitial = False, returnTeacherPassword = False, returnTeacherSSOID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempFitnessGram/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempFitnessGram(TempFitnessGramID, EntityID = 1, returnTempFitnessGramID = True, returnClassDescription = False, returnClassEndDate = False, returnClassID = False, returnClassName = False, returnClassStartDate = False, returnCourseCodeDescription = False, returnCreatedTime = False, returnHasMissingData = False, returnMessage = False, returnModifiedTime = False, returnParentReportEmail1 = False, returnParentReportEmail2 = False, returnSchoolID = False, returnSectionCode = False, returnStudentBirthdate = False, returnStudentFirstName = False, returnStudentGender = False, returnStudentGrade = False, returnStudentID = False, returnStudentLastName = False, returnStudentMiddleInitial = False, returnStudentPassword = False, returnStudentReportEmail = False, returnStudentSSOID = False, returnTeacherBirthDate = False, returnTeacherEmail = False, returnTeacherFirstName = False, returnTeacherID = False, returnTeacherLastName = False, returnTeacherMiddleInitial = False, returnTeacherPassword = False, returnTeacherSSOID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempFitnessGram/" + str(TempFitnessGramID), verb = "get", return_params_list = return_params_list)

def modifyTempFitnessGram(TempFitnessGramID, EntityID = 1, setClassDescription = None, setClassEndDate = None, setClassID = None, setClassName = None, setClassStartDate = None, setCourseCodeDescription = None, setHasMissingData = None, setMessage = None, setParentReportEmail1 = None, setParentReportEmail2 = None, setSchoolID = None, setSectionCode = None, setStudentBirthdate = None, setStudentFirstName = None, setStudentGender = None, setStudentGrade = None, setStudentID = None, setStudentLastName = None, setStudentMiddleInitial = None, setStudentPassword = None, setStudentReportEmail = None, setStudentSSOID = None, setTeacherBirthDate = None, setTeacherEmail = None, setTeacherFirstName = None, setTeacherID = None, setTeacherLastName = None, setTeacherMiddleInitial = None, setTeacherPassword = None, setTeacherSSOID = None, setRelationships = None, returnTempFitnessGramID = True, returnClassDescription = False, returnClassEndDate = False, returnClassID = False, returnClassName = False, returnClassStartDate = False, returnCourseCodeDescription = False, returnCreatedTime = False, returnHasMissingData = False, returnMessage = False, returnModifiedTime = False, returnParentReportEmail1 = False, returnParentReportEmail2 = False, returnSchoolID = False, returnSectionCode = False, returnStudentBirthdate = False, returnStudentFirstName = False, returnStudentGender = False, returnStudentGrade = False, returnStudentID = False, returnStudentLastName = False, returnStudentMiddleInitial = False, returnStudentPassword = False, returnStudentReportEmail = False, returnStudentSSOID = False, returnTeacherBirthDate = False, returnTeacherEmail = False, returnTeacherFirstName = False, returnTeacherID = False, returnTeacherLastName = False, returnTeacherMiddleInitial = False, returnTeacherPassword = False, returnTeacherSSOID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempFitnessGram/" + str(TempFitnessGramID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempFitnessGram(EntityID = 1, setClassDescription = None, setClassEndDate = None, setClassID = None, setClassName = None, setClassStartDate = None, setCourseCodeDescription = None, setHasMissingData = None, setMessage = None, setParentReportEmail1 = None, setParentReportEmail2 = None, setSchoolID = None, setSectionCode = None, setStudentBirthdate = None, setStudentFirstName = None, setStudentGender = None, setStudentGrade = None, setStudentID = None, setStudentLastName = None, setStudentMiddleInitial = None, setStudentPassword = None, setStudentReportEmail = None, setStudentSSOID = None, setTeacherBirthDate = None, setTeacherEmail = None, setTeacherFirstName = None, setTeacherID = None, setTeacherLastName = None, setTeacherMiddleInitial = None, setTeacherPassword = None, setTeacherSSOID = None, setRelationships = None, returnTempFitnessGramID = True, returnClassDescription = False, returnClassEndDate = False, returnClassID = False, returnClassName = False, returnClassStartDate = False, returnCourseCodeDescription = False, returnCreatedTime = False, returnHasMissingData = False, returnMessage = False, returnModifiedTime = False, returnParentReportEmail1 = False, returnParentReportEmail2 = False, returnSchoolID = False, returnSectionCode = False, returnStudentBirthdate = False, returnStudentFirstName = False, returnStudentGender = False, returnStudentGrade = False, returnStudentID = False, returnStudentLastName = False, returnStudentMiddleInitial = False, returnStudentPassword = False, returnStudentReportEmail = False, returnStudentSSOID = False, returnTeacherBirthDate = False, returnTeacherEmail = False, returnTeacherFirstName = False, returnTeacherID = False, returnTeacherLastName = False, returnTeacherMiddleInitial = False, returnTeacherPassword = False, returnTeacherSSOID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempFitnessGram/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempFitnessGram(TempFitnessGramID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempLockCombination(EntityID = 1, page = 1, pageSize = 100, returnTempLockCombinationID = True, returnCombination = False, returnCombinationNumber = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnTempLockerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempLockCombination/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempLockCombination(TempLockCombinationID, EntityID = 1, returnTempLockCombinationID = True, returnCombination = False, returnCombinationNumber = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnTempLockerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempLockCombination/" + str(TempLockCombinationID), verb = "get", return_params_list = return_params_list)

def modifyTempLockCombination(TempLockCombinationID, EntityID = 1, setCombination = None, setCombinationNumber = None, setFailureReason = None, setTempLockerID = None, setRelationships = None, returnTempLockCombinationID = True, returnCombination = False, returnCombinationNumber = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnTempLockerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempLockCombination/" + str(TempLockCombinationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempLockCombination(EntityID = 1, setCombination = None, setCombinationNumber = None, setFailureReason = None, setTempLockerID = None, setRelationships = None, returnTempLockCombinationID = True, returnCombination = False, returnCombinationNumber = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnTempLockerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempLockCombination/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempLockCombination(TempLockCombinationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempLocker(EntityID = 1, page = 1, pageSize = 100, returnTempLockerID = True, returnBuilding = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnFailureReason = False, returnLockerArea = False, returnLockerAreaID = False, returnLockerID = False, returnLockerNumber = False, returnLockerNumberDigitLength = False, returnModifiedTime = False, returnNewLockerNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempLocker/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempLocker(TempLockerID, EntityID = 1, returnTempLockerID = True, returnBuilding = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnFailureReason = False, returnLockerArea = False, returnLockerAreaID = False, returnLockerID = False, returnLockerNumber = False, returnLockerNumberDigitLength = False, returnModifiedTime = False, returnNewLockerNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempLocker/" + str(TempLockerID), verb = "get", return_params_list = return_params_list)

def modifyTempLocker(TempLockerID, EntityID = 1, setBuilding = None, setBuildingID = None, setComment = None, setFailureReason = None, setLockerArea = None, setLockerAreaID = None, setLockerID = None, setLockerNumber = None, setLockerNumberDigitLength = None, setNewLockerNumber = None, setRelationships = None, returnTempLockerID = True, returnBuilding = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnFailureReason = False, returnLockerArea = False, returnLockerAreaID = False, returnLockerID = False, returnLockerNumber = False, returnLockerNumberDigitLength = False, returnModifiedTime = False, returnNewLockerNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempLocker/" + str(TempLockerID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempLocker(EntityID = 1, setBuilding = None, setBuildingID = None, setComment = None, setFailureReason = None, setLockerArea = None, setLockerAreaID = None, setLockerID = None, setLockerNumber = None, setLockerNumberDigitLength = None, setNewLockerNumber = None, setRelationships = None, returnTempLockerID = True, returnBuilding = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnFailureReason = False, returnLockerArea = False, returnLockerAreaID = False, returnLockerID = False, returnLockerNumber = False, returnLockerNumberDigitLength = False, returnModifiedTime = False, returnNewLockerNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempLocker/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempLocker(TempLockerID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentActivity(EntityID = 1, page = 1, pageSize = 100, returnTempStudentActivityID = True, returnActivityID = False, returnAge = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityCode = False, returnErrorNumber = False, returnFullNameLFM = False, returnGenderCodeAndGender = False, returnGradeLevel = False, returnGradYear = False, returnIsActive = False, returnModifiedTime = False, returnParticipationEndDate = False, returnParticipationStartDate = False, returnStartDate = False, returnStudentID = False, returnStudentName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentActivity(TempStudentActivityID, EntityID = 1, returnTempStudentActivityID = True, returnActivityID = False, returnAge = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityCode = False, returnErrorNumber = False, returnFullNameLFM = False, returnGenderCodeAndGender = False, returnGradeLevel = False, returnGradYear = False, returnIsActive = False, returnModifiedTime = False, returnParticipationEndDate = False, returnParticipationStartDate = False, returnStartDate = False, returnStudentID = False, returnStudentName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivity/" + str(TempStudentActivityID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentActivity(TempStudentActivityID, EntityID = 1, setActivityID = None, setAge = None, setCode = None, setDescription = None, setEndDate = None, setEntityCode = None, setErrorNumber = None, setFullNameLFM = None, setGenderCodeAndGender = None, setGradeLevel = None, setGradYear = None, setIsActive = None, setParticipationEndDate = None, setParticipationStartDate = None, setStartDate = None, setStudentID = None, setStudentName = None, setStudentNumber = None, setRelationships = None, returnTempStudentActivityID = True, returnActivityID = False, returnAge = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityCode = False, returnErrorNumber = False, returnFullNameLFM = False, returnGenderCodeAndGender = False, returnGradeLevel = False, returnGradYear = False, returnIsActive = False, returnModifiedTime = False, returnParticipationEndDate = False, returnParticipationStartDate = False, returnStartDate = False, returnStudentID = False, returnStudentName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivity/" + str(TempStudentActivityID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentActivity(EntityID = 1, setActivityID = None, setAge = None, setCode = None, setDescription = None, setEndDate = None, setEntityCode = None, setErrorNumber = None, setFullNameLFM = None, setGenderCodeAndGender = None, setGradeLevel = None, setGradYear = None, setIsActive = None, setParticipationEndDate = None, setParticipationStartDate = None, setStartDate = None, setStudentID = None, setStudentName = None, setStudentNumber = None, setRelationships = None, returnTempStudentActivityID = True, returnActivityID = False, returnAge = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityCode = False, returnErrorNumber = False, returnFullNameLFM = False, returnGenderCodeAndGender = False, returnGradeLevel = False, returnGradYear = False, returnIsActive = False, returnModifiedTime = False, returnParticipationEndDate = False, returnParticipationStartDate = False, returnStartDate = False, returnStudentID = False, returnStudentName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivity/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentActivity(TempStudentActivityID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentActivityError(EntityID = 1, page = 1, pageSize = 100, returnTempStudentActivityErrorID = True, returnCreatedTime = False, returnErrorNumber = False, returnErrorText = False, returnModifiedTime = False, returnTempStudentActivityID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivityError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentActivityError(TempStudentActivityErrorID, EntityID = 1, returnTempStudentActivityErrorID = True, returnCreatedTime = False, returnErrorNumber = False, returnErrorText = False, returnModifiedTime = False, returnTempStudentActivityID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivityError/" + str(TempStudentActivityErrorID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentActivityError(TempStudentActivityErrorID, EntityID = 1, setErrorNumber = None, setErrorText = None, setTempStudentActivityID = None, setRelationships = None, returnTempStudentActivityErrorID = True, returnCreatedTime = False, returnErrorNumber = False, returnErrorText = False, returnModifiedTime = False, returnTempStudentActivityID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivityError/" + str(TempStudentActivityErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentActivityError(EntityID = 1, setErrorNumber = None, setErrorText = None, setTempStudentActivityID = None, setRelationships = None, returnTempStudentActivityErrorID = True, returnCreatedTime = False, returnErrorNumber = False, returnErrorText = False, returnModifiedTime = False, returnTempStudentActivityID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivityError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentActivityError(TempStudentActivityErrorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentActivityTransactionRecord(EntityID = 1, page = 1, pageSize = 100, returnTempStudentActivityTransactionRecordID = True, returnActivityID = False, returnCreatedTime = False, returnIsValidTransaction = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnStudentActivityTransactionID = False, returnStudentFullNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivityTransactionRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentActivityTransactionRecord(TempStudentActivityTransactionRecordID, EntityID = 1, returnTempStudentActivityTransactionRecordID = True, returnActivityID = False, returnCreatedTime = False, returnIsValidTransaction = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnStudentActivityTransactionID = False, returnStudentFullNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivityTransactionRecord/" + str(TempStudentActivityTransactionRecordID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentActivityTransactionRecord(TempStudentActivityTransactionRecordID, EntityID = 1, setActivityID = None, setIsValidTransaction = None, setNewEndDate = None, setNewStartDate = None, setStudentActivityTransactionID = None, setStudentFullNameLFM = None, setRelationships = None, returnTempStudentActivityTransactionRecordID = True, returnActivityID = False, returnCreatedTime = False, returnIsValidTransaction = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnStudentActivityTransactionID = False, returnStudentFullNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivityTransactionRecord/" + str(TempStudentActivityTransactionRecordID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentActivityTransactionRecord(EntityID = 1, setActivityID = None, setIsValidTransaction = None, setNewEndDate = None, setNewStartDate = None, setStudentActivityTransactionID = None, setStudentFullNameLFM = None, setRelationships = None, returnTempStudentActivityTransactionRecordID = True, returnActivityID = False, returnCreatedTime = False, returnIsValidTransaction = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnStudentActivityTransactionID = False, returnStudentFullNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivityTransactionRecord/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentActivityTransactionRecord(TempStudentActivityTransactionRecordID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentAssignedLockCombinationRecord(EntityID = 1, page = 1, pageSize = 100, returnTempStudentAssignedLockCombinationRecordID = True, returnAge = False, returnBirthDate = False, returnBuilding = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGrade = False, returnGradYear = False, returnLockerArea = False, returnLockerID = False, returnLockerNumber = False, returnLockID = False, returnModifiedTime = False, returnNewCombination = False, returnNewCombinationNumber = False, returnNewLockCombinationID = False, returnOldCombination = False, returnOldCombinationNumber = False, returnOldLockCombinationID = False, returnStudentID = False, returnStudentNumber = False, returnUnoccupiedLockersOnly = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentAssignedLockCombinationRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentAssignedLockCombinationRecord(TempStudentAssignedLockCombinationRecordID, EntityID = 1, returnTempStudentAssignedLockCombinationRecordID = True, returnAge = False, returnBirthDate = False, returnBuilding = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGrade = False, returnGradYear = False, returnLockerArea = False, returnLockerID = False, returnLockerNumber = False, returnLockID = False, returnModifiedTime = False, returnNewCombination = False, returnNewCombinationNumber = False, returnNewLockCombinationID = False, returnOldCombination = False, returnOldCombinationNumber = False, returnOldLockCombinationID = False, returnStudentID = False, returnStudentNumber = False, returnUnoccupiedLockersOnly = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentAssignedLockCombinationRecord/" + str(TempStudentAssignedLockCombinationRecordID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentAssignedLockCombinationRecord(TempStudentAssignedLockCombinationRecordID, EntityID = 1, setAge = None, setBirthDate = None, setBuilding = None, setFullName = None, setGender = None, setGrade = None, setGradYear = None, setLockerArea = None, setLockerID = None, setLockerNumber = None, setLockID = None, setNewCombination = None, setNewCombinationNumber = None, setNewLockCombinationID = None, setOldCombination = None, setOldCombinationNumber = None, setOldLockCombinationID = None, setStudentID = None, setStudentNumber = None, setUnoccupiedLockersOnly = None, setRelationships = None, returnTempStudentAssignedLockCombinationRecordID = True, returnAge = False, returnBirthDate = False, returnBuilding = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGrade = False, returnGradYear = False, returnLockerArea = False, returnLockerID = False, returnLockerNumber = False, returnLockID = False, returnModifiedTime = False, returnNewCombination = False, returnNewCombinationNumber = False, returnNewLockCombinationID = False, returnOldCombination = False, returnOldCombinationNumber = False, returnOldLockCombinationID = False, returnStudentID = False, returnStudentNumber = False, returnUnoccupiedLockersOnly = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentAssignedLockCombinationRecord/" + str(TempStudentAssignedLockCombinationRecordID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentAssignedLockCombinationRecord(EntityID = 1, setAge = None, setBirthDate = None, setBuilding = None, setFullName = None, setGender = None, setGrade = None, setGradYear = None, setLockerArea = None, setLockerID = None, setLockerNumber = None, setLockID = None, setNewCombination = None, setNewCombinationNumber = None, setNewLockCombinationID = None, setOldCombination = None, setOldCombinationNumber = None, setOldLockCombinationID = None, setStudentID = None, setStudentNumber = None, setUnoccupiedLockersOnly = None, setRelationships = None, returnTempStudentAssignedLockCombinationRecordID = True, returnAge = False, returnBirthDate = False, returnBuilding = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGrade = False, returnGradYear = False, returnLockerArea = False, returnLockerID = False, returnLockerNumber = False, returnLockID = False, returnModifiedTime = False, returnNewCombination = False, returnNewCombinationNumber = False, returnNewLockCombinationID = False, returnOldCombination = False, returnOldCombinationNumber = False, returnOldLockCombinationID = False, returnStudentID = False, returnStudentNumber = False, returnUnoccupiedLockersOnly = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentAssignedLockCombinationRecord/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentAssignedLockCombinationRecord(TempStudentAssignedLockCombinationRecordID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentAssignedLockerRecord(EntityID = 1, page = 1, pageSize = 100, returnTempStudentAssignedLockerRecordID = True, returnAge = False, returnBirthDate = False, returnBuilding = False, returnCombination = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGrade = False, returnGradYear = False, returnIsStudentAccessUser = False, returnLockerArea = False, returnLockerID = False, returnLockerNumber = False, returnModifiedTime = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentAssignedLockerRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentAssignedLockerRecord(TempStudentAssignedLockerRecordID, EntityID = 1, returnTempStudentAssignedLockerRecordID = True, returnAge = False, returnBirthDate = False, returnBuilding = False, returnCombination = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGrade = False, returnGradYear = False, returnIsStudentAccessUser = False, returnLockerArea = False, returnLockerID = False, returnLockerNumber = False, returnModifiedTime = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentAssignedLockerRecord/" + str(TempStudentAssignedLockerRecordID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentAssignedLockerRecord(TempStudentAssignedLockerRecordID, EntityID = 1, setAge = None, setBirthDate = None, setBuilding = None, setCombination = None, setFullName = None, setGender = None, setGrade = None, setGradYear = None, setIsStudentAccessUser = None, setLockerArea = None, setLockerID = None, setLockerNumber = None, setStudentID = None, setStudentNumber = None, setRelationships = None, returnTempStudentAssignedLockerRecordID = True, returnAge = False, returnBirthDate = False, returnBuilding = False, returnCombination = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGrade = False, returnGradYear = False, returnIsStudentAccessUser = False, returnLockerArea = False, returnLockerID = False, returnLockerNumber = False, returnModifiedTime = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentAssignedLockerRecord/" + str(TempStudentAssignedLockerRecordID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentAssignedLockerRecord(EntityID = 1, setAge = None, setBirthDate = None, setBuilding = None, setCombination = None, setFullName = None, setGender = None, setGrade = None, setGradYear = None, setIsStudentAccessUser = None, setLockerArea = None, setLockerID = None, setLockerNumber = None, setStudentID = None, setStudentNumber = None, setRelationships = None, returnTempStudentAssignedLockerRecordID = True, returnAge = False, returnBirthDate = False, returnBuilding = False, returnCombination = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGrade = False, returnGradYear = False, returnIsStudentAccessUser = False, returnLockerArea = False, returnLockerID = False, returnLockerNumber = False, returnModifiedTime = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentAssignedLockerRecord/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentAssignedLockerRecord(TempStudentAssignedLockerRecordID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentError(EntityID = 1, page = 1, pageSize = 100, returnTempStudentErrorID = True, returnCreatedTime = False, returnErrorCount = False, returnFullStudentNameLFM = False, returnGender = False, returnGradeLevelCode = False, returnGraduationRequirementYear = False, returnGradYear = False, returnIsCurrentActive = False, returnLockerNumber = False, returnModifiedTime = False, returnNote = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnStudentTypeDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentError(TempStudentErrorID, EntityID = 1, returnTempStudentErrorID = True, returnCreatedTime = False, returnErrorCount = False, returnFullStudentNameLFM = False, returnGender = False, returnGradeLevelCode = False, returnGraduationRequirementYear = False, returnGradYear = False, returnIsCurrentActive = False, returnLockerNumber = False, returnModifiedTime = False, returnNote = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnStudentTypeDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentError/" + str(TempStudentErrorID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentError(TempStudentErrorID, EntityID = 1, setErrorCount = None, setFullStudentNameLFM = None, setGender = None, setGradeLevelCode = None, setGraduationRequirementYear = None, setGradYear = None, setIsCurrentActive = None, setLockerNumber = None, setNote = None, setStudentID = None, setStudentNumber = None, setStudentTypeCode = None, setStudentTypeDescription = None, setRelationships = None, returnTempStudentErrorID = True, returnCreatedTime = False, returnErrorCount = False, returnFullStudentNameLFM = False, returnGender = False, returnGradeLevelCode = False, returnGraduationRequirementYear = False, returnGradYear = False, returnIsCurrentActive = False, returnLockerNumber = False, returnModifiedTime = False, returnNote = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnStudentTypeDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentError/" + str(TempStudentErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentError(EntityID = 1, setErrorCount = None, setFullStudentNameLFM = None, setGender = None, setGradeLevelCode = None, setGraduationRequirementYear = None, setGradYear = None, setIsCurrentActive = None, setLockerNumber = None, setNote = None, setStudentID = None, setStudentNumber = None, setStudentTypeCode = None, setStudentTypeDescription = None, setRelationships = None, returnTempStudentErrorID = True, returnCreatedTime = False, returnErrorCount = False, returnFullStudentNameLFM = False, returnGender = False, returnGradeLevelCode = False, returnGraduationRequirementYear = False, returnGradYear = False, returnIsCurrentActive = False, returnLockerNumber = False, returnModifiedTime = False, returnNote = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnStudentTypeDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentError(TempStudentErrorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentErrorMessage(EntityID = 1, page = 1, pageSize = 100, returnTempStudentErrorMessageID = True, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnModifiedTime = False, returnTempStudentErrorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentErrorMessage/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentErrorMessage(TempStudentErrorMessageID, EntityID = 1, returnTempStudentErrorMessageID = True, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnModifiedTime = False, returnTempStudentErrorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentErrorMessage/" + str(TempStudentErrorMessageID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentErrorMessage(TempStudentErrorMessageID, EntityID = 1, setError = None, setErrorDetail = None, setTempStudentErrorID = None, setRelationships = None, returnTempStudentErrorMessageID = True, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnModifiedTime = False, returnTempStudentErrorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentErrorMessage/" + str(TempStudentErrorMessageID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentErrorMessage(EntityID = 1, setError = None, setErrorDetail = None, setTempStudentErrorID = None, setRelationships = None, returnTempStudentErrorMessageID = True, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnModifiedTime = False, returnTempStudentErrorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentErrorMessage/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentErrorMessage(TempStudentErrorMessageID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentMassUpdateError(EntityID = 1, page = 1, pageSize = 100, returnTempStudentMassUpdateErrorID = True, returnCreatedTime = False, returnFailureReason = False, returnFullNameLFM = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMassUpdateError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentMassUpdateError(TempStudentMassUpdateErrorID, EntityID = 1, returnTempStudentMassUpdateErrorID = True, returnCreatedTime = False, returnFailureReason = False, returnFullNameLFM = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMassUpdateError/" + str(TempStudentMassUpdateErrorID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentMassUpdateError(TempStudentMassUpdateErrorID, EntityID = 1, setFailureReason = None, setFullNameLFM = None, setType = None, setTypeCode = None, setRelationships = None, returnTempStudentMassUpdateErrorID = True, returnCreatedTime = False, returnFailureReason = False, returnFullNameLFM = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMassUpdateError/" + str(TempStudentMassUpdateErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentMassUpdateError(EntityID = 1, setFailureReason = None, setFullNameLFM = None, setType = None, setTypeCode = None, setRelationships = None, returnTempStudentMassUpdateErrorID = True, returnCreatedTime = False, returnFailureReason = False, returnFullNameLFM = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMassUpdateError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentMassUpdateError(TempStudentMassUpdateErrorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentMassUpdateField(EntityID = 1, page = 1, pageSize = 100, returnTempStudentMassUpdateFieldID = True, returnAffectedPrimaryKey = False, returnCreatedTime = False, returnFieldName = False, returnFriendlyOriginalValue = False, returnFriendlyUpdatedValue = False, returnFullNameLFM = False, returnModifiedTime = False, returnOriginalValue = False, returnRelatedType = False, returnRelatedTypeCode = False, returnStudentID = False, returnUpdatedValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMassUpdateField/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentMassUpdateField(TempStudentMassUpdateFieldID, EntityID = 1, returnTempStudentMassUpdateFieldID = True, returnAffectedPrimaryKey = False, returnCreatedTime = False, returnFieldName = False, returnFriendlyOriginalValue = False, returnFriendlyUpdatedValue = False, returnFullNameLFM = False, returnModifiedTime = False, returnOriginalValue = False, returnRelatedType = False, returnRelatedTypeCode = False, returnStudentID = False, returnUpdatedValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMassUpdateField/" + str(TempStudentMassUpdateFieldID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentMassUpdateField(TempStudentMassUpdateFieldID, EntityID = 1, setAffectedPrimaryKey = None, setFieldName = None, setFriendlyOriginalValue = None, setFriendlyUpdatedValue = None, setFullNameLFM = None, setOriginalValue = None, setRelatedType = None, setRelatedTypeCode = None, setStudentID = None, setUpdatedValue = None, setRelationships = None, returnTempStudentMassUpdateFieldID = True, returnAffectedPrimaryKey = False, returnCreatedTime = False, returnFieldName = False, returnFriendlyOriginalValue = False, returnFriendlyUpdatedValue = False, returnFullNameLFM = False, returnModifiedTime = False, returnOriginalValue = False, returnRelatedType = False, returnRelatedTypeCode = False, returnStudentID = False, returnUpdatedValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMassUpdateField/" + str(TempStudentMassUpdateFieldID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentMassUpdateField(EntityID = 1, setAffectedPrimaryKey = None, setFieldName = None, setFriendlyOriginalValue = None, setFriendlyUpdatedValue = None, setFullNameLFM = None, setOriginalValue = None, setRelatedType = None, setRelatedTypeCode = None, setStudentID = None, setUpdatedValue = None, setRelationships = None, returnTempStudentMassUpdateFieldID = True, returnAffectedPrimaryKey = False, returnCreatedTime = False, returnFieldName = False, returnFriendlyOriginalValue = False, returnFriendlyUpdatedValue = False, returnFullNameLFM = False, returnModifiedTime = False, returnOriginalValue = False, returnRelatedType = False, returnRelatedTypeCode = False, returnStudentID = False, returnUpdatedValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMassUpdateField/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentMassUpdateField(TempStudentMassUpdateFieldID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentMergeObject(EntityID = 1, page = 1, pageSize = 100, returnTempStudentMergeObjectID = True, returnCreatedTime = False, returnFieldToShow = False, returnHandlingType = False, returnHandlingTypeCode = False, returnModifiedTime = False, returnRecordType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMergeObject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentMergeObject(TempStudentMergeObjectID, EntityID = 1, returnTempStudentMergeObjectID = True, returnCreatedTime = False, returnFieldToShow = False, returnHandlingType = False, returnHandlingTypeCode = False, returnModifiedTime = False, returnRecordType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMergeObject/" + str(TempStudentMergeObjectID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentMergeObject(TempStudentMergeObjectID, EntityID = 1, setFieldToShow = None, setHandlingType = None, setHandlingTypeCode = None, setRecordType = None, setRelationships = None, returnTempStudentMergeObjectID = True, returnCreatedTime = False, returnFieldToShow = False, returnHandlingType = False, returnHandlingTypeCode = False, returnModifiedTime = False, returnRecordType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMergeObject/" + str(TempStudentMergeObjectID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentMergeObject(EntityID = 1, setFieldToShow = None, setHandlingType = None, setHandlingTypeCode = None, setRecordType = None, setRelationships = None, returnTempStudentMergeObjectID = True, returnCreatedTime = False, returnFieldToShow = False, returnHandlingType = False, returnHandlingTypeCode = False, returnModifiedTime = False, returnRecordType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMergeObject/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentMergeObject(TempStudentMergeObjectID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentPermit(EntityID = 1, page = 1, pageSize = 100, returnTempStudentPermitID = True, returnAddressID = False, returnAge = False, returnCreatedTime = False, returnEntityName = False, returnExceptionNote = False, returnFullNameLFM = False, returnGenderCode = False, returnGradYear = False, returnHasExceptions = False, returnModifiedTime = False, returnPermitID = False, returnStudentDistrictID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentPermit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentPermit(TempStudentPermitID, EntityID = 1, returnTempStudentPermitID = True, returnAddressID = False, returnAge = False, returnCreatedTime = False, returnEntityName = False, returnExceptionNote = False, returnFullNameLFM = False, returnGenderCode = False, returnGradYear = False, returnHasExceptions = False, returnModifiedTime = False, returnPermitID = False, returnStudentDistrictID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentPermit/" + str(TempStudentPermitID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentPermit(TempStudentPermitID, EntityID = 1, setAddressID = None, setAge = None, setEntityName = None, setExceptionNote = None, setFullNameLFM = None, setGenderCode = None, setGradYear = None, setHasExceptions = None, setPermitID = None, setStudentDistrictID = None, setStudentID = None, setStudentNumber = None, setRelationships = None, returnTempStudentPermitID = True, returnAddressID = False, returnAge = False, returnCreatedTime = False, returnEntityName = False, returnExceptionNote = False, returnFullNameLFM = False, returnGenderCode = False, returnGradYear = False, returnHasExceptions = False, returnModifiedTime = False, returnPermitID = False, returnStudentDistrictID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentPermit/" + str(TempStudentPermitID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentPermit(EntityID = 1, setAddressID = None, setAge = None, setEntityName = None, setExceptionNote = None, setFullNameLFM = None, setGenderCode = None, setGradYear = None, setHasExceptions = None, setPermitID = None, setStudentDistrictID = None, setStudentID = None, setStudentNumber = None, setRelationships = None, returnTempStudentPermitID = True, returnAddressID = False, returnAge = False, returnCreatedTime = False, returnEntityName = False, returnExceptionNote = False, returnFullNameLFM = False, returnGenderCode = False, returnGradYear = False, returnHasExceptions = False, returnModifiedTime = False, returnPermitID = False, returnStudentDistrictID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentPermit/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentPermit(TempStudentPermitID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentWithoutLockerRecord(EntityID = 1, page = 1, pageSize = 100, returnTempStudentWithoutLockerRecordID = True, returnAge = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGradYear = False, returnModifiedTime = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentWithoutLockerRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentWithoutLockerRecord(TempStudentWithoutLockerRecordID, EntityID = 1, returnTempStudentWithoutLockerRecordID = True, returnAge = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGradYear = False, returnModifiedTime = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentWithoutLockerRecord/" + str(TempStudentWithoutLockerRecordID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentWithoutLockerRecord(TempStudentWithoutLockerRecordID, EntityID = 1, setAge = None, setFullName = None, setGender = None, setGradYear = None, setStudentID = None, setStudentNumber = None, setRelationships = None, returnTempStudentWithoutLockerRecordID = True, returnAge = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGradYear = False, returnModifiedTime = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentWithoutLockerRecord/" + str(TempStudentWithoutLockerRecordID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentWithoutLockerRecord(EntityID = 1, setAge = None, setFullName = None, setGender = None, setGradYear = None, setStudentID = None, setStudentNumber = None, setRelationships = None, returnTempStudentWithoutLockerRecordID = True, returnAge = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGradYear = False, returnModifiedTime = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentWithoutLockerRecord/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentWithoutLockerRecord(TempStudentWithoutLockerRecordID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryWinterSport(EntityID = 1, page = 1, pageSize = 100, returnWinterSportID = True, returnCode = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSport = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/WinterSport/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getWinterSport(WinterSportID, EntityID = 1, returnWinterSportID = True, returnCode = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSport = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/WinterSport/" + str(WinterSportID), verb = "get", return_params_list = return_params_list)

def modifyWinterSport(WinterSportID, EntityID = 1, setCode = None, setWinterSport = None, setRelationships = None, returnWinterSportID = True, returnCode = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSport = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/WinterSport/" + str(WinterSportID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createWinterSport(EntityID = 1, setCode = None, setWinterSport = None, setRelationships = None, returnWinterSportID = True, returnCode = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSport = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/WinterSport/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteWinterSport(WinterSportID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryWinterSportsTeam(EntityID = 1, page = 1, pageSize = 100, returnWinterSportsTeamID = True, returnCaptain = False, returnCreatedTime = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSportID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/WinterSportsTeam/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getWinterSportsTeam(WinterSportsTeamID, EntityID = 1, returnWinterSportsTeamID = True, returnCaptain = False, returnCreatedTime = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSportID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/WinterSportsTeam/" + str(WinterSportsTeamID), verb = "get", return_params_list = return_params_list)

def modifyWinterSportsTeam(WinterSportsTeamID, EntityID = 1, setCaptain = None, setLettered = None, setSchoolYearID = None, setStudentID = None, setWinterSportID = None, setRelationships = None, returnWinterSportsTeamID = True, returnCaptain = False, returnCreatedTime = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSportID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/WinterSportsTeam/" + str(WinterSportsTeamID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createWinterSportsTeam(EntityID = 1, setCaptain = None, setLettered = None, setSchoolYearID = None, setStudentID = None, setWinterSportID = None, setRelationships = None, returnWinterSportsTeamID = True, returnCaptain = False, returnCreatedTime = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSportID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/WinterSportsTeam/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteWinterSportsTeam(WinterSportsTeamID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")