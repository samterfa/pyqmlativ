# This module contains Enrollment functions.

from .Utilities import make_request

import pandas as pd

import json

import re

def getEveryAwardsListMA(EntityID = 1, page = 1, pageSize = 100, returnAwardsListMAID = True, returnAwardID = False, returnCreatedTime = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AwardsListMA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAwardsListMA(AwardsListMAID, EntityID = 1, returnAwardsListMAID = True, returnAwardID = False, returnCreatedTime = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AwardsListMA/" + str(AwardsListMAID), verb = "get", return_params_list = return_params_list)

def modifyAwardsListMA(AwardsListMAID, EntityID = 1, setAwardID = None, setSchoolYearID = None, setStudentID = None, setRelationships = None, returnAwardsListMAID = True, returnAwardID = False, returnCreatedTime = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AwardsListMA/" + str(AwardsListMAID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAwardsListMA(EntityID = 1, setAwardID = None, setSchoolYearID = None, setStudentID = None, setRelationships = None, returnAwardsListMAID = True, returnAwardID = False, returnCreatedTime = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AwardsListMA/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAwardsListMA(AwardsListMAID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAwardsMA(EntityID = 1, page = 1, pageSize = 100, returnAwardsMAID = True, returnAward = False, returnCode = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AwardsMA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAwardsMA(AwardsMAID, EntityID = 1, returnAwardsMAID = True, returnAward = False, returnCode = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AwardsMA/" + str(AwardsMAID), verb = "get", return_params_list = return_params_list)

def modifyAwardsMA(AwardsMAID, EntityID = 1, setAward = None, setCode = None, setRelationships = None, returnAwardsMAID = True, returnAward = False, returnCode = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AwardsMA/" + str(AwardsMAID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAwardsMA(EntityID = 1, setAward = None, setCode = None, setRelationships = None, returnAwardsMAID = True, returnAward = False, returnCode = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AwardsMA/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAwardsMA(AwardsMAID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigDistrict(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictID = True, returnAllowDualEnrollment = False, returnCreatedTime = False, returnDistrictID = False, returnEntryDaysBeforeCalendarStart = False, returnModifiedTime = False, returnNumberDaysBackdateEntry = False, returnNumberDaysBackdateWithdrawal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDaysAfterCalendarEnd = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigDistrict(ConfigDistrictID, EntityID = 1, returnConfigDistrictID = True, returnAllowDualEnrollment = False, returnCreatedTime = False, returnDistrictID = False, returnEntryDaysBeforeCalendarStart = False, returnModifiedTime = False, returnNumberDaysBackdateEntry = False, returnNumberDaysBackdateWithdrawal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDaysAfterCalendarEnd = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrict/" + str(ConfigDistrictID), verb = "get", return_params_list = return_params_list)

def modifyConfigDistrict(ConfigDistrictID, EntityID = 1, setAllowDualEnrollment = None, setDistrictID = None, setEntryDaysBeforeCalendarStart = None, setNumberDaysBackdateEntry = None, setNumberDaysBackdateWithdrawal = None, setWithdrawalDaysAfterCalendarEnd = None, setRelationships = None, returnConfigDistrictID = True, returnAllowDualEnrollment = False, returnCreatedTime = False, returnDistrictID = False, returnEntryDaysBeforeCalendarStart = False, returnModifiedTime = False, returnNumberDaysBackdateEntry = False, returnNumberDaysBackdateWithdrawal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDaysAfterCalendarEnd = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrict/" + str(ConfigDistrictID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigDistrict(EntityID = 1, setAllowDualEnrollment = None, setDistrictID = None, setEntryDaysBeforeCalendarStart = None, setNumberDaysBackdateEntry = None, setNumberDaysBackdateWithdrawal = None, setWithdrawalDaysAfterCalendarEnd = None, setRelationships = None, returnConfigDistrictID = True, returnAllowDualEnrollment = False, returnCreatedTime = False, returnDistrictID = False, returnEntryDaysBeforeCalendarStart = False, returnModifiedTime = False, returnNumberDaysBackdateEntry = False, returnNumberDaysBackdateWithdrawal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDaysAfterCalendarEnd = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrict/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigDistrict(ConfigDistrictID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigDistrictYear(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictYearID = True, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnEnableNoShow = False, returnEnrolledDifferentEntityNoShowActionType = False, returnEnrolledDifferentEntityNoShowActionTypeCode = False, returnEnrolledDifferentEntityNoShowEntryDate = False, returnEnrolledDifferentEntityNoShowWithdrawalDate = False, returnModifiedTime = False, returnNoDistrictEnrollmentNoShowActionType = False, returnNoDistrictEnrollmentNoShowActionTypeCode = False, returnNoDistrictEnrollmentNoShowEntryDate = False, returnNoDistrictEnrollmentNoShowWithdrawalDate = False, returnPreviouslyEnrolledSameEntityNoShowActionType = False, returnPreviouslyEnrolledSameEntityNoShowActionTypeCode = False, returnPreviouslyEnrolledSameEntityNoShowEntryDate = False, returnPreviouslyEnrolledSameEntityNoShowWithdrawalDate = False, returnPriorNoShowRecord = False, returnPriorNoShowRecordCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, returnConfigDistrictYearID = True, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnEnableNoShow = False, returnEnrolledDifferentEntityNoShowActionType = False, returnEnrolledDifferentEntityNoShowActionTypeCode = False, returnEnrolledDifferentEntityNoShowEntryDate = False, returnEnrolledDifferentEntityNoShowWithdrawalDate = False, returnModifiedTime = False, returnNoDistrictEnrollmentNoShowActionType = False, returnNoDistrictEnrollmentNoShowActionTypeCode = False, returnNoDistrictEnrollmentNoShowEntryDate = False, returnNoDistrictEnrollmentNoShowWithdrawalDate = False, returnPreviouslyEnrolledSameEntityNoShowActionType = False, returnPreviouslyEnrolledSameEntityNoShowActionTypeCode = False, returnPreviouslyEnrolledSameEntityNoShowEntryDate = False, returnPreviouslyEnrolledSameEntityNoShowWithdrawalDate = False, returnPriorNoShowRecord = False, returnPriorNoShowRecordCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "get", return_params_list = return_params_list)

def modifyConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, setConfigDistrictYearIDClonedFrom = None, setDistrictID = None, setEnableNoShow = None, setEnrolledDifferentEntityNoShowActionType = None, setEnrolledDifferentEntityNoShowActionTypeCode = None, setEnrolledDifferentEntityNoShowEntryDate = None, setEnrolledDifferentEntityNoShowWithdrawalDate = None, setNoDistrictEnrollmentNoShowActionType = None, setNoDistrictEnrollmentNoShowActionTypeCode = None, setNoDistrictEnrollmentNoShowEntryDate = None, setNoDistrictEnrollmentNoShowWithdrawalDate = None, setPreviouslyEnrolledSameEntityNoShowActionType = None, setPreviouslyEnrolledSameEntityNoShowActionTypeCode = None, setPreviouslyEnrolledSameEntityNoShowEntryDate = None, setPreviouslyEnrolledSameEntityNoShowWithdrawalDate = None, setPriorNoShowRecord = None, setPriorNoShowRecordCode = None, setSchoolYearID = None, setRelationships = None, returnConfigDistrictYearID = True, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnEnableNoShow = False, returnEnrolledDifferentEntityNoShowActionType = False, returnEnrolledDifferentEntityNoShowActionTypeCode = False, returnEnrolledDifferentEntityNoShowEntryDate = False, returnEnrolledDifferentEntityNoShowWithdrawalDate = False, returnModifiedTime = False, returnNoDistrictEnrollmentNoShowActionType = False, returnNoDistrictEnrollmentNoShowActionTypeCode = False, returnNoDistrictEnrollmentNoShowEntryDate = False, returnNoDistrictEnrollmentNoShowWithdrawalDate = False, returnPreviouslyEnrolledSameEntityNoShowActionType = False, returnPreviouslyEnrolledSameEntityNoShowActionTypeCode = False, returnPreviouslyEnrolledSameEntityNoShowEntryDate = False, returnPreviouslyEnrolledSameEntityNoShowWithdrawalDate = False, returnPriorNoShowRecord = False, returnPriorNoShowRecordCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigDistrictYear(EntityID = 1, setConfigDistrictYearIDClonedFrom = None, setDistrictID = None, setEnableNoShow = None, setEnrolledDifferentEntityNoShowActionType = None, setEnrolledDifferentEntityNoShowActionTypeCode = None, setEnrolledDifferentEntityNoShowEntryDate = None, setEnrolledDifferentEntityNoShowWithdrawalDate = None, setNoDistrictEnrollmentNoShowActionType = None, setNoDistrictEnrollmentNoShowActionTypeCode = None, setNoDistrictEnrollmentNoShowEntryDate = None, setNoDistrictEnrollmentNoShowWithdrawalDate = None, setPreviouslyEnrolledSameEntityNoShowActionType = None, setPreviouslyEnrolledSameEntityNoShowActionTypeCode = None, setPreviouslyEnrolledSameEntityNoShowEntryDate = None, setPreviouslyEnrolledSameEntityNoShowWithdrawalDate = None, setPriorNoShowRecord = None, setPriorNoShowRecordCode = None, setSchoolYearID = None, setRelationships = None, returnConfigDistrictYearID = True, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnEnableNoShow = False, returnEnrolledDifferentEntityNoShowActionType = False, returnEnrolledDifferentEntityNoShowActionTypeCode = False, returnEnrolledDifferentEntityNoShowEntryDate = False, returnEnrolledDifferentEntityNoShowWithdrawalDate = False, returnModifiedTime = False, returnNoDistrictEnrollmentNoShowActionType = False, returnNoDistrictEnrollmentNoShowActionTypeCode = False, returnNoDistrictEnrollmentNoShowEntryDate = False, returnNoDistrictEnrollmentNoShowWithdrawalDate = False, returnPreviouslyEnrolledSameEntityNoShowActionType = False, returnPreviouslyEnrolledSameEntityNoShowActionTypeCode = False, returnPreviouslyEnrolledSameEntityNoShowEntryDate = False, returnPreviouslyEnrolledSameEntityNoShowWithdrawalDate = False, returnPriorNoShowRecord = False, returnPriorNoShowRecordCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigDistrictYear(ConfigDistrictYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigDistrictYearWithdrawalCode(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictYearWithdrawalCodeID = True, returnConfigDistrictYearID = False, returnConfigDistrictYearWithdrawalCodeIDClonedFrom = False, returnCreatedTime = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYearWithdrawalCode/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigDistrictYearWithdrawalCode(ConfigDistrictYearWithdrawalCodeID, EntityID = 1, returnConfigDistrictYearWithdrawalCodeID = True, returnConfigDistrictYearID = False, returnConfigDistrictYearWithdrawalCodeIDClonedFrom = False, returnCreatedTime = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYearWithdrawalCode/" + str(ConfigDistrictYearWithdrawalCodeID), verb = "get", return_params_list = return_params_list)

def modifyConfigDistrictYearWithdrawalCode(ConfigDistrictYearWithdrawalCodeID, EntityID = 1, setConfigDistrictYearID = None, setConfigDistrictYearWithdrawalCodeIDClonedFrom = None, setType = None, setTypeCode = None, setWithdrawalCodeID = None, setRelationships = None, returnConfigDistrictYearWithdrawalCodeID = True, returnConfigDistrictYearID = False, returnConfigDistrictYearWithdrawalCodeIDClonedFrom = False, returnCreatedTime = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYearWithdrawalCode/" + str(ConfigDistrictYearWithdrawalCodeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigDistrictYearWithdrawalCode(EntityID = 1, setConfigDistrictYearID = None, setConfigDistrictYearWithdrawalCodeIDClonedFrom = None, setType = None, setTypeCode = None, setWithdrawalCodeID = None, setRelationships = None, returnConfigDistrictYearWithdrawalCodeID = True, returnConfigDistrictYearID = False, returnConfigDistrictYearWithdrawalCodeIDClonedFrom = False, returnCreatedTime = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYearWithdrawalCode/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigDistrictYearWithdrawalCode(ConfigDistrictYearWithdrawalCodeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEntitySchool(EntityID = 1, page = 1, pageSize = 100, returnEntitySchoolID = True, returnCreatedTime = False, returnEntityID = False, returnEntitySchoolIDClonedFrom = False, returnEntitySchoolIDClonedTo = False, returnIsDefaultEntityForSchool = False, returnIsDefaultSchoolForEntity = False, returnIsOnlySchoolInEntity = False, returnModifiedTime = False, returnSchoolID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchool/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEntitySchool(EntitySchoolID, EntityID = 1, returnEntitySchoolID = True, returnCreatedTime = False, returnEntityID = False, returnEntitySchoolIDClonedFrom = False, returnEntitySchoolIDClonedTo = False, returnIsDefaultEntityForSchool = False, returnIsDefaultSchoolForEntity = False, returnIsOnlySchoolInEntity = False, returnModifiedTime = False, returnSchoolID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchool/" + str(EntitySchoolID), verb = "get", return_params_list = return_params_list)

def modifyEntitySchool(EntitySchoolID, EntityID = 1, setEntityID = None, setEntitySchoolIDClonedFrom = None, setIsDefaultEntityForSchool = None, setIsDefaultSchoolForEntity = None, setSchoolID = None, setRelationships = None, returnEntitySchoolID = True, returnCreatedTime = False, returnEntityID = False, returnEntitySchoolIDClonedFrom = False, returnEntitySchoolIDClonedTo = False, returnIsDefaultEntityForSchool = False, returnIsDefaultSchoolForEntity = False, returnIsOnlySchoolInEntity = False, returnModifiedTime = False, returnSchoolID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchool/" + str(EntitySchoolID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEntitySchool(EntityID = 1, setEntityID = None, setEntitySchoolIDClonedFrom = None, setIsDefaultEntityForSchool = None, setIsDefaultSchoolForEntity = None, setSchoolID = None, setRelationships = None, returnEntitySchoolID = True, returnCreatedTime = False, returnEntityID = False, returnEntitySchoolIDClonedFrom = False, returnEntitySchoolIDClonedTo = False, returnIsDefaultEntityForSchool = False, returnIsDefaultSchoolForEntity = False, returnIsOnlySchoolInEntity = False, returnModifiedTime = False, returnSchoolID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchool/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEntitySchool(EntitySchoolID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEntitySchoolBuilding(EntityID = 1, page = 1, pageSize = 100, returnEntitySchoolBuildingID = True, returnBuildingID = False, returnCreatedTime = False, returnEntitySchoolBuildingIDClonedFrom = False, returnEntitySchoolID = False, returnIsPrimary = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchoolBuilding/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEntitySchoolBuilding(EntitySchoolBuildingID, EntityID = 1, returnEntitySchoolBuildingID = True, returnBuildingID = False, returnCreatedTime = False, returnEntitySchoolBuildingIDClonedFrom = False, returnEntitySchoolID = False, returnIsPrimary = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchoolBuilding/" + str(EntitySchoolBuildingID), verb = "get", return_params_list = return_params_list)

def modifyEntitySchoolBuilding(EntitySchoolBuildingID, EntityID = 1, setBuildingID = None, setEntitySchoolBuildingIDClonedFrom = None, setEntitySchoolID = None, setIsPrimary = None, setSchoolYearID = None, setRelationships = None, returnEntitySchoolBuildingID = True, returnBuildingID = False, returnCreatedTime = False, returnEntitySchoolBuildingIDClonedFrom = False, returnEntitySchoolID = False, returnIsPrimary = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchoolBuilding/" + str(EntitySchoolBuildingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEntitySchoolBuilding(EntityID = 1, setBuildingID = None, setEntitySchoolBuildingIDClonedFrom = None, setEntitySchoolID = None, setIsPrimary = None, setSchoolYearID = None, setRelationships = None, returnEntitySchoolBuildingID = True, returnBuildingID = False, returnCreatedTime = False, returnEntitySchoolBuildingIDClonedFrom = False, returnEntitySchoolID = False, returnIsPrimary = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchoolBuilding/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEntitySchoolBuilding(EntitySchoolBuildingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEntryCode(EntityID = 1, page = 1, pageSize = 100, returnEntryCodeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEntryCodeIDClonedFrom = False, returnIsCrossEntityCourseEnrollment = False, returnModifiedTime = False, returnSchoolYearID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryCode/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEntryCode(EntryCodeID, EntityID = 1, returnEntryCodeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEntryCodeIDClonedFrom = False, returnIsCrossEntityCourseEnrollment = False, returnModifiedTime = False, returnSchoolYearID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryCode/" + str(EntryCodeID), verb = "get", return_params_list = return_params_list)

def modifyEntryCode(EntryCodeID, EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setEntryCodeIDClonedFrom = None, setIsCrossEntityCourseEnrollment = None, setSchoolYearID = None, setType = None, setTypeCode = None, setRelationships = None, returnEntryCodeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEntryCodeIDClonedFrom = False, returnIsCrossEntityCourseEnrollment = False, returnModifiedTime = False, returnSchoolYearID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryCode/" + str(EntryCodeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEntryCode(EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setEntryCodeIDClonedFrom = None, setIsCrossEntityCourseEnrollment = None, setSchoolYearID = None, setType = None, setTypeCode = None, setRelationships = None, returnEntryCodeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEntryCodeIDClonedFrom = False, returnIsCrossEntityCourseEnrollment = False, returnModifiedTime = False, returnSchoolYearID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryCode/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEntryCode(EntryCodeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEntryWithdrawal(EntityID = 1, page = 1, pageSize = 100, returnEntryWithdrawalID = True, returnAttendanceDays = False, returnCalendarID = False, returnCreatedTime = False, returnEndDate = False, returnEnrolledAtLeastOneDay = False, returnEntityID = False, returnEntryCodeID = False, returnEntryComment = False, returnEntryWithdrawalIDStatusChangePrevious = False, returnEntryWithdrawalMNID = False, returnGradeReferenceID = False, returnHasMessageCenterAllowedWithdrawalCodeOverride = False, returnIsCombinedEnrollmentFullTime = False, returnIsCrossEntityCourseEnrollment = False, returnIsCurrentOrFutureEnrollment = False, returnIsDefaultEntity = False, returnIsHistoricalEnrollment = False, returnIsIndependentStudy = False, returnIsNoShow = False, returnIsPostSecondaryOption = False, returnIsPSEOConcurrentEnrollment = False, returnIsStartDateOnOrAfterFirstDayOfSchool = False, returnMembershipDays = False, returnModifiedTime = False, returnPercentEnrolled = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnPSEOHours = False, returnRenderDeleteOption = False, returnRenderNoShowOption = False, returnRenderPrintWithdrawalFormOption = False, returnRenderUndoStatusChangeOption = False, returnRenderWithdrawalAndStatusChangeOptions = False, returnSchoolID = False, returnSchoolYearID = False, returnSpecialEdServiceHours = False, returnStartDate = False, returnStateAidCategoryCodeMNID = False, returnStateDistrictMNID = False, returnStateLastAttendanceLocationCodeMNID = False, returnStatusChangeEntry = False, returnStatusChangeWithdrawal = False, returnStudentID = False, returnStudentTypeID = False, returnTotalMembershipDays = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnWithdrawalComment = False, returnWithdrawalDate = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryWithdrawal/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEntryWithdrawal(EntryWithdrawalID, EntityID = 1, returnEntryWithdrawalID = True, returnAttendanceDays = False, returnCalendarID = False, returnCreatedTime = False, returnEndDate = False, returnEnrolledAtLeastOneDay = False, returnEntityID = False, returnEntryCodeID = False, returnEntryComment = False, returnEntryWithdrawalIDStatusChangePrevious = False, returnEntryWithdrawalMNID = False, returnGradeReferenceID = False, returnHasMessageCenterAllowedWithdrawalCodeOverride = False, returnIsCombinedEnrollmentFullTime = False, returnIsCrossEntityCourseEnrollment = False, returnIsCurrentOrFutureEnrollment = False, returnIsDefaultEntity = False, returnIsHistoricalEnrollment = False, returnIsIndependentStudy = False, returnIsNoShow = False, returnIsPostSecondaryOption = False, returnIsPSEOConcurrentEnrollment = False, returnIsStartDateOnOrAfterFirstDayOfSchool = False, returnMembershipDays = False, returnModifiedTime = False, returnPercentEnrolled = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnPSEOHours = False, returnRenderDeleteOption = False, returnRenderNoShowOption = False, returnRenderPrintWithdrawalFormOption = False, returnRenderUndoStatusChangeOption = False, returnRenderWithdrawalAndStatusChangeOptions = False, returnSchoolID = False, returnSchoolYearID = False, returnSpecialEdServiceHours = False, returnStartDate = False, returnStateAidCategoryCodeMNID = False, returnStateDistrictMNID = False, returnStateLastAttendanceLocationCodeMNID = False, returnStatusChangeEntry = False, returnStatusChangeWithdrawal = False, returnStudentID = False, returnStudentTypeID = False, returnTotalMembershipDays = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnWithdrawalComment = False, returnWithdrawalDate = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryWithdrawal/" + str(EntryWithdrawalID), verb = "get", return_params_list = return_params_list)

def modifyEntryWithdrawal(EntryWithdrawalID, EntityID = 1, setAttendanceDays = None, setCalendarID = None, setEndDate = None, setEntityID = None, setEntryCodeID = None, setEntryComment = None, setEntryWithdrawalIDStatusChangePrevious = None, setGradeReferenceID = None, setIsDefaultEntity = None, setIsIndependentStudy = None, setIsNoShow = None, setIsPostSecondaryOption = None, setIsPSEOConcurrentEnrollment = None, setMembershipDays = None, setPercentEnrolled = None, setPromotionStatus = None, setPromotionStatusCode = None, setPSEOHours = None, setSchoolID = None, setSchoolYearID = None, setSpecialEdServiceHours = None, setStartDate = None, setStateAidCategoryCodeMNID = None, setStateDistrictMNID = None, setStateLastAttendanceLocationCodeMNID = None, setStudentID = None, setStudentTypeID = None, setWithdrawalCodeID = None, setWithdrawalComment = None, setRelationships = None, returnEntryWithdrawalID = True, returnAttendanceDays = False, returnCalendarID = False, returnCreatedTime = False, returnEndDate = False, returnEnrolledAtLeastOneDay = False, returnEntityID = False, returnEntryCodeID = False, returnEntryComment = False, returnEntryWithdrawalIDStatusChangePrevious = False, returnEntryWithdrawalMNID = False, returnGradeReferenceID = False, returnHasMessageCenterAllowedWithdrawalCodeOverride = False, returnIsCombinedEnrollmentFullTime = False, returnIsCrossEntityCourseEnrollment = False, returnIsCurrentOrFutureEnrollment = False, returnIsDefaultEntity = False, returnIsHistoricalEnrollment = False, returnIsIndependentStudy = False, returnIsNoShow = False, returnIsPostSecondaryOption = False, returnIsPSEOConcurrentEnrollment = False, returnIsStartDateOnOrAfterFirstDayOfSchool = False, returnMembershipDays = False, returnModifiedTime = False, returnPercentEnrolled = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnPSEOHours = False, returnRenderDeleteOption = False, returnRenderNoShowOption = False, returnRenderPrintWithdrawalFormOption = False, returnRenderUndoStatusChangeOption = False, returnRenderWithdrawalAndStatusChangeOptions = False, returnSchoolID = False, returnSchoolYearID = False, returnSpecialEdServiceHours = False, returnStartDate = False, returnStateAidCategoryCodeMNID = False, returnStateDistrictMNID = False, returnStateLastAttendanceLocationCodeMNID = False, returnStatusChangeEntry = False, returnStatusChangeWithdrawal = False, returnStudentID = False, returnStudentTypeID = False, returnTotalMembershipDays = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnWithdrawalComment = False, returnWithdrawalDate = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryWithdrawal/" + str(EntryWithdrawalID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEntryWithdrawal(EntityID = 1, setAttendanceDays = None, setCalendarID = None, setEndDate = None, setEntityID = None, setEntryCodeID = None, setEntryComment = None, setEntryWithdrawalIDStatusChangePrevious = None, setGradeReferenceID = None, setIsDefaultEntity = None, setIsIndependentStudy = None, setIsNoShow = None, setIsPostSecondaryOption = None, setIsPSEOConcurrentEnrollment = None, setMembershipDays = None, setPercentEnrolled = None, setPromotionStatus = None, setPromotionStatusCode = None, setPSEOHours = None, setSchoolID = None, setSchoolYearID = None, setSpecialEdServiceHours = None, setStartDate = None, setStateAidCategoryCodeMNID = None, setStateDistrictMNID = None, setStateLastAttendanceLocationCodeMNID = None, setStudentID = None, setStudentTypeID = None, setWithdrawalCodeID = None, setWithdrawalComment = None, setRelationships = None, returnEntryWithdrawalID = True, returnAttendanceDays = False, returnCalendarID = False, returnCreatedTime = False, returnEndDate = False, returnEnrolledAtLeastOneDay = False, returnEntityID = False, returnEntryCodeID = False, returnEntryComment = False, returnEntryWithdrawalIDStatusChangePrevious = False, returnEntryWithdrawalMNID = False, returnGradeReferenceID = False, returnHasMessageCenterAllowedWithdrawalCodeOverride = False, returnIsCombinedEnrollmentFullTime = False, returnIsCrossEntityCourseEnrollment = False, returnIsCurrentOrFutureEnrollment = False, returnIsDefaultEntity = False, returnIsHistoricalEnrollment = False, returnIsIndependentStudy = False, returnIsNoShow = False, returnIsPostSecondaryOption = False, returnIsPSEOConcurrentEnrollment = False, returnIsStartDateOnOrAfterFirstDayOfSchool = False, returnMembershipDays = False, returnModifiedTime = False, returnPercentEnrolled = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnPSEOHours = False, returnRenderDeleteOption = False, returnRenderNoShowOption = False, returnRenderPrintWithdrawalFormOption = False, returnRenderUndoStatusChangeOption = False, returnRenderWithdrawalAndStatusChangeOptions = False, returnSchoolID = False, returnSchoolYearID = False, returnSpecialEdServiceHours = False, returnStartDate = False, returnStateAidCategoryCodeMNID = False, returnStateDistrictMNID = False, returnStateLastAttendanceLocationCodeMNID = False, returnStatusChangeEntry = False, returnStatusChangeWithdrawal = False, returnStudentID = False, returnStudentTypeID = False, returnTotalMembershipDays = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnWithdrawalComment = False, returnWithdrawalDate = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryWithdrawal/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEntryWithdrawal(EntryWithdrawalID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeLevel(EntityID = 1, page = 1, pageSize = 100, returnGradeLevelID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnFederalGradeLevel = False, returnFederalGradeLevelCode = False, returnModifiedTime = False, returnNumericValue = False, returnStateGradeLevel = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeLevel(GradeLevelID, EntityID = 1, returnGradeLevelID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnFederalGradeLevel = False, returnFederalGradeLevelCode = False, returnModifiedTime = False, returnNumericValue = False, returnStateGradeLevel = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeLevel/" + str(GradeLevelID), verb = "get", return_params_list = return_params_list)

def modifyGradeLevel(GradeLevelID, EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setFederalGradeLevel = None, setFederalGradeLevelCode = None, setNumericValue = None, setRelationships = None, returnGradeLevelID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnFederalGradeLevel = False, returnFederalGradeLevelCode = False, returnModifiedTime = False, returnNumericValue = False, returnStateGradeLevel = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeLevel/" + str(GradeLevelID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeLevel(EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setFederalGradeLevel = None, setFederalGradeLevelCode = None, setNumericValue = None, setRelationships = None, returnGradeLevelID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnFederalGradeLevel = False, returnFederalGradeLevelCode = False, returnModifiedTime = False, returnNumericValue = False, returnStateGradeLevel = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeLevel/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeLevel(GradeLevelID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReference(EntityID = 1, page = 1, pageSize = 100, returnGradeReferenceID = True, returnCreatedTime = False, returnDistrictGroupKey = False, returnGradeLevelID = False, returnGradeReferenceIDClonedFrom = False, returnGradeReferenceIDClonedTo = False, returnGradeReferenceMNID = False, returnGradYear = False, returnMinutesPresentFullDay = False, returnMinutesPresentHalfDay = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateGradeLevel = False, returnStateSTARGradeLevelMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeReference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReference(GradeReferenceID, EntityID = 1, returnGradeReferenceID = True, returnCreatedTime = False, returnDistrictGroupKey = False, returnGradeLevelID = False, returnGradeReferenceIDClonedFrom = False, returnGradeReferenceIDClonedTo = False, returnGradeReferenceMNID = False, returnGradYear = False, returnMinutesPresentFullDay = False, returnMinutesPresentHalfDay = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateGradeLevel = False, returnStateSTARGradeLevelMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeReference/" + str(GradeReferenceID), verb = "get", return_params_list = return_params_list)

def modifyGradeReference(GradeReferenceID, EntityID = 1, setDistrictGroupKey = None, setGradeLevelID = None, setGradeReferenceIDClonedFrom = None, setGradYear = None, setMinutesPresentFullDay = None, setMinutesPresentHalfDay = None, setSchoolYearID = None, setStateSTARGradeLevelMNID = None, setRelationships = None, returnGradeReferenceID = True, returnCreatedTime = False, returnDistrictGroupKey = False, returnGradeLevelID = False, returnGradeReferenceIDClonedFrom = False, returnGradeReferenceIDClonedTo = False, returnGradeReferenceMNID = False, returnGradYear = False, returnMinutesPresentFullDay = False, returnMinutesPresentHalfDay = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateGradeLevel = False, returnStateSTARGradeLevelMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeReference/" + str(GradeReferenceID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReference(EntityID = 1, setDistrictGroupKey = None, setGradeLevelID = None, setGradeReferenceIDClonedFrom = None, setGradYear = None, setMinutesPresentFullDay = None, setMinutesPresentHalfDay = None, setSchoolYearID = None, setStateSTARGradeLevelMNID = None, setRelationships = None, returnGradeReferenceID = True, returnCreatedTime = False, returnDistrictGroupKey = False, returnGradeLevelID = False, returnGradeReferenceIDClonedFrom = False, returnGradeReferenceIDClonedTo = False, returnGradeReferenceMNID = False, returnGradYear = False, returnMinutesPresentFullDay = False, returnMinutesPresentHalfDay = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateGradeLevel = False, returnStateSTARGradeLevelMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeReference/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReference(GradeReferenceID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryHomeroom(EntityID = 1, page = 1, pageSize = 100, returnHomeroomID = True, returnCode = False, returnCreatedTime = False, returnEntityID = False, returnHomeroomDetails = False, returnHomeroomIDClonedFrom = False, returnHomeroomIDClonedTo = False, returnModifiedTime = False, returnRoomID = False, returnSchoolYearID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Homeroom/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getHomeroom(HomeroomID, EntityID = 1, returnHomeroomID = True, returnCode = False, returnCreatedTime = False, returnEntityID = False, returnHomeroomDetails = False, returnHomeroomIDClonedFrom = False, returnHomeroomIDClonedTo = False, returnModifiedTime = False, returnRoomID = False, returnSchoolYearID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Homeroom/" + str(HomeroomID), verb = "get", return_params_list = return_params_list)

def modifyHomeroom(HomeroomID, EntityID = 1, setCode = None, setEntityID = None, setHomeroomIDClonedFrom = None, setRoomID = None, setSchoolYearID = None, setStaffID = None, setRelationships = None, returnHomeroomID = True, returnCode = False, returnCreatedTime = False, returnEntityID = False, returnHomeroomDetails = False, returnHomeroomIDClonedFrom = False, returnHomeroomIDClonedTo = False, returnModifiedTime = False, returnRoomID = False, returnSchoolYearID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Homeroom/" + str(HomeroomID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createHomeroom(EntityID = 1, setCode = None, setEntityID = None, setHomeroomIDClonedFrom = None, setRoomID = None, setSchoolYearID = None, setStaffID = None, setRelationships = None, returnHomeroomID = True, returnCode = False, returnCreatedTime = False, returnEntityID = False, returnHomeroomDetails = False, returnHomeroomIDClonedFrom = False, returnHomeroomIDClonedTo = False, returnModifiedTime = False, returnRoomID = False, returnSchoolYearID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Homeroom/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteHomeroom(HomeroomID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPaymentPlanMA(EntityID = 1, page = 1, pageSize = 100, returnPaymentPlanMAID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PaymentPlanMA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPaymentPlanMA(PaymentPlanMAID, EntityID = 1, returnPaymentPlanMAID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PaymentPlanMA/" + str(PaymentPlanMAID), verb = "get", return_params_list = return_params_list)

def modifyPaymentPlanMA(PaymentPlanMAID, EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnPaymentPlanMAID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PaymentPlanMA/" + str(PaymentPlanMAID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPaymentPlanMA(EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnPaymentPlanMAID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PaymentPlanMA/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePaymentPlanMA(PaymentPlanMAID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPermit(EntityID = 1, page = 1, pageSize = 100, returnPermitID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEndDate = False, returnModifiedTime = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Permit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPermit(PermitID, EntityID = 1, returnPermitID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEndDate = False, returnModifiedTime = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Permit/" + str(PermitID), verb = "get", return_params_list = return_params_list)

def modifyPermit(PermitID, EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setEndDate = None, setStartDate = None, setRelationships = None, returnPermitID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEndDate = False, returnModifiedTime = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Permit/" + str(PermitID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPermit(EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setEndDate = None, setStartDate = None, setRelationships = None, returnPermitID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEndDate = False, returnModifiedTime = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Permit/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePermit(PermitID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySchool(EntityID = 1, page = 1, pageSize = 100, returnSchoolID = True, returnAllowsSchoolDevices = False, returnAllowsStudentDevices = False, returnBuildingID = False, returnCampusAccountabilityRatingID = False, returnCEEBCode = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnDaysInRegularSchoolYear = False, returnDaysPriorForAlgebraICounts = False, returnDistrictID = False, returnEdFiSchoolCategoryID = False, returnEdFiSchoolID = False, returnEducationalProgramHoursPerWeek = False, returnExcludeFromCRDC = False, returnFaxNumber = False, returnFaxNumberIsInternational = False, returnFederalAlternativeSchoolDetailID = False, returnFederalJusticeFacilityTypeID = False, returnFederalNCESSchoolID = False, returnFormattedFaxNumber = False, returnFormattedPhoneNumber = False, returnGradeLevelIDHigh = False, returnGradeLevelIDLow = False, returnHasAlcoholDrugEducation = False, returnHasAntiBullying = False, returnHasAntiViolence = False, returnHasAPCourses = False, returnHasAPSelfSelection = False, returnHasCorporalPunishment = False, returnHasCreditRecovery = False, returnHasCrisisPlan = False, returnHasDualEnrollment = False, returnHasFiberOptic = False, returnHasGifted = False, returnHasHomicideOccurred = False, returnHasIBDiplomaProgramme = False, returnHasPreschoolNonIDEAAge3 = False, returnHasPreschoolNonIDEAAge4 = False, returnHasPreschoolNonIDEAAge5 = False, returnHasSafetyPlan = False, returnHasShootingOccurred = False, returnHasSingleSexAthletics = False, returnHasSingleSexClasses = False, returnHasUngraded = False, returnHasUngradedMainlyElementary = False, returnHasUngradedMainlyHighSchool = False, returnHasUngradedMainlyMiddleSchool = False, returnHasWiFi = False, returnHasZeroTolerance = False, returnIsALCSchool = False, returnIsAlternative = False, returnIsCEP = False, returnIsCharter = False, returnIsCRDCCollectedForSchoolYear = False, returnIsEntireSchoolMagnet = False, returnIsMagnet = False, returnIsNonLEA = False, returnIsSpecialEducation = False, returnIsTitleIII = False, returnModifiedTime = False, returnName = False, returnNameIDSafetySpecialist = False, returnNumberWiFiDevices = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnSchoolIDClonedFrom = False, returnSchoolIDClonedTo = False, returnSchoolMNID = False, returnSchoolNumber = False, returnSchoolYearID = False, returnStaffIDPrincipal = False, returnStateKindergartenScheduleIndicatorCodeMNID = False, returnStateSchoolMNID = False, returnStateTitleISchoolIndicatorCodeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/School/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSchool(SchoolID, EntityID = 1, returnSchoolID = True, returnAllowsSchoolDevices = False, returnAllowsStudentDevices = False, returnBuildingID = False, returnCampusAccountabilityRatingID = False, returnCEEBCode = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnDaysInRegularSchoolYear = False, returnDaysPriorForAlgebraICounts = False, returnDistrictID = False, returnEdFiSchoolCategoryID = False, returnEdFiSchoolID = False, returnEducationalProgramHoursPerWeek = False, returnExcludeFromCRDC = False, returnFaxNumber = False, returnFaxNumberIsInternational = False, returnFederalAlternativeSchoolDetailID = False, returnFederalJusticeFacilityTypeID = False, returnFederalNCESSchoolID = False, returnFormattedFaxNumber = False, returnFormattedPhoneNumber = False, returnGradeLevelIDHigh = False, returnGradeLevelIDLow = False, returnHasAlcoholDrugEducation = False, returnHasAntiBullying = False, returnHasAntiViolence = False, returnHasAPCourses = False, returnHasAPSelfSelection = False, returnHasCorporalPunishment = False, returnHasCreditRecovery = False, returnHasCrisisPlan = False, returnHasDualEnrollment = False, returnHasFiberOptic = False, returnHasGifted = False, returnHasHomicideOccurred = False, returnHasIBDiplomaProgramme = False, returnHasPreschoolNonIDEAAge3 = False, returnHasPreschoolNonIDEAAge4 = False, returnHasPreschoolNonIDEAAge5 = False, returnHasSafetyPlan = False, returnHasShootingOccurred = False, returnHasSingleSexAthletics = False, returnHasSingleSexClasses = False, returnHasUngraded = False, returnHasUngradedMainlyElementary = False, returnHasUngradedMainlyHighSchool = False, returnHasUngradedMainlyMiddleSchool = False, returnHasWiFi = False, returnHasZeroTolerance = False, returnIsALCSchool = False, returnIsAlternative = False, returnIsCEP = False, returnIsCharter = False, returnIsCRDCCollectedForSchoolYear = False, returnIsEntireSchoolMagnet = False, returnIsMagnet = False, returnIsNonLEA = False, returnIsSpecialEducation = False, returnIsTitleIII = False, returnModifiedTime = False, returnName = False, returnNameIDSafetySpecialist = False, returnNumberWiFiDevices = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnSchoolIDClonedFrom = False, returnSchoolIDClonedTo = False, returnSchoolMNID = False, returnSchoolNumber = False, returnSchoolYearID = False, returnStaffIDPrincipal = False, returnStateKindergartenScheduleIndicatorCodeMNID = False, returnStateSchoolMNID = False, returnStateTitleISchoolIndicatorCodeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/School/" + str(SchoolID), verb = "get", return_params_list = return_params_list)

def modifySchool(SchoolID, EntityID = 1, setAllowsSchoolDevices = None, setAllowsStudentDevices = None, setCampusAccountabilityRatingID = None, setCEEBCode = None, setCode = None, setDaysInRegularSchoolYear = None, setDaysPriorForAlgebraICounts = None, setDistrictID = None, setEdFiSchoolCategoryID = None, setEdFiSchoolID = None, setEducationalProgramHoursPerWeek = None, setExcludeFromCRDC = None, setFaxNumber = None, setFaxNumberIsInternational = None, setFederalAlternativeSchoolDetailID = None, setFederalJusticeFacilityTypeID = None, setFederalNCESSchoolID = None, setGradeLevelIDHigh = None, setGradeLevelIDLow = None, setHasAlcoholDrugEducation = None, setHasAntiBullying = None, setHasAntiViolence = None, setHasAPCourses = None, setHasAPSelfSelection = None, setHasCorporalPunishment = None, setHasCreditRecovery = None, setHasCrisisPlan = None, setHasDualEnrollment = None, setHasFiberOptic = None, setHasGifted = None, setHasHomicideOccurred = None, setHasIBDiplomaProgramme = None, setHasPreschoolNonIDEAAge3 = None, setHasPreschoolNonIDEAAge4 = None, setHasPreschoolNonIDEAAge5 = None, setHasSafetyPlan = None, setHasShootingOccurred = None, setHasSingleSexAthletics = None, setHasSingleSexClasses = None, setHasUngraded = None, setHasUngradedMainlyElementary = None, setHasUngradedMainlyHighSchool = None, setHasUngradedMainlyMiddleSchool = None, setHasWiFi = None, setHasZeroTolerance = None, setIsALCSchool = None, setIsAlternative = None, setIsCEP = None, setIsCharter = None, setIsEntireSchoolMagnet = None, setIsMagnet = None, setIsNonLEA = None, setIsSpecialEducation = None, setIsTitleIII = None, setName = None, setNameIDSafetySpecialist = None, setNumberWiFiDevices = None, setPhoneNumber = None, setPhoneNumberIsInternational = None, setSchoolIDClonedFrom = None, setSchoolNumber = None, setSchoolYearID = None, setStaffIDPrincipal = None, setStateKindergartenScheduleIndicatorCodeMNID = None, setStateSchoolMNID = None, setStateTitleISchoolIndicatorCodeMNID = None, setType = None, setTypeCode = None, setRelationships = None, returnSchoolID = True, returnAllowsSchoolDevices = False, returnAllowsStudentDevices = False, returnBuildingID = False, returnCampusAccountabilityRatingID = False, returnCEEBCode = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnDaysInRegularSchoolYear = False, returnDaysPriorForAlgebraICounts = False, returnDistrictID = False, returnEdFiSchoolCategoryID = False, returnEdFiSchoolID = False, returnEducationalProgramHoursPerWeek = False, returnExcludeFromCRDC = False, returnFaxNumber = False, returnFaxNumberIsInternational = False, returnFederalAlternativeSchoolDetailID = False, returnFederalJusticeFacilityTypeID = False, returnFederalNCESSchoolID = False, returnFormattedFaxNumber = False, returnFormattedPhoneNumber = False, returnGradeLevelIDHigh = False, returnGradeLevelIDLow = False, returnHasAlcoholDrugEducation = False, returnHasAntiBullying = False, returnHasAntiViolence = False, returnHasAPCourses = False, returnHasAPSelfSelection = False, returnHasCorporalPunishment = False, returnHasCreditRecovery = False, returnHasCrisisPlan = False, returnHasDualEnrollment = False, returnHasFiberOptic = False, returnHasGifted = False, returnHasHomicideOccurred = False, returnHasIBDiplomaProgramme = False, returnHasPreschoolNonIDEAAge3 = False, returnHasPreschoolNonIDEAAge4 = False, returnHasPreschoolNonIDEAAge5 = False, returnHasSafetyPlan = False, returnHasShootingOccurred = False, returnHasSingleSexAthletics = False, returnHasSingleSexClasses = False, returnHasUngraded = False, returnHasUngradedMainlyElementary = False, returnHasUngradedMainlyHighSchool = False, returnHasUngradedMainlyMiddleSchool = False, returnHasWiFi = False, returnHasZeroTolerance = False, returnIsALCSchool = False, returnIsAlternative = False, returnIsCEP = False, returnIsCharter = False, returnIsCRDCCollectedForSchoolYear = False, returnIsEntireSchoolMagnet = False, returnIsMagnet = False, returnIsNonLEA = False, returnIsSpecialEducation = False, returnIsTitleIII = False, returnModifiedTime = False, returnName = False, returnNameIDSafetySpecialist = False, returnNumberWiFiDevices = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnSchoolIDClonedFrom = False, returnSchoolIDClonedTo = False, returnSchoolMNID = False, returnSchoolNumber = False, returnSchoolYearID = False, returnStaffIDPrincipal = False, returnStateKindergartenScheduleIndicatorCodeMNID = False, returnStateSchoolMNID = False, returnStateTitleISchoolIndicatorCodeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/School/" + str(SchoolID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSchool(EntityID = 1, setAllowsSchoolDevices = None, setAllowsStudentDevices = None, setCampusAccountabilityRatingID = None, setCEEBCode = None, setCode = None, setDaysInRegularSchoolYear = None, setDaysPriorForAlgebraICounts = None, setDistrictID = None, setEdFiSchoolCategoryID = None, setEdFiSchoolID = None, setEducationalProgramHoursPerWeek = None, setExcludeFromCRDC = None, setFaxNumber = None, setFaxNumberIsInternational = None, setFederalAlternativeSchoolDetailID = None, setFederalJusticeFacilityTypeID = None, setFederalNCESSchoolID = None, setGradeLevelIDHigh = None, setGradeLevelIDLow = None, setHasAlcoholDrugEducation = None, setHasAntiBullying = None, setHasAntiViolence = None, setHasAPCourses = None, setHasAPSelfSelection = None, setHasCorporalPunishment = None, setHasCreditRecovery = None, setHasCrisisPlan = None, setHasDualEnrollment = None, setHasFiberOptic = None, setHasGifted = None, setHasHomicideOccurred = None, setHasIBDiplomaProgramme = None, setHasPreschoolNonIDEAAge3 = None, setHasPreschoolNonIDEAAge4 = None, setHasPreschoolNonIDEAAge5 = None, setHasSafetyPlan = None, setHasShootingOccurred = None, setHasSingleSexAthletics = None, setHasSingleSexClasses = None, setHasUngraded = None, setHasUngradedMainlyElementary = None, setHasUngradedMainlyHighSchool = None, setHasUngradedMainlyMiddleSchool = None, setHasWiFi = None, setHasZeroTolerance = None, setIsALCSchool = None, setIsAlternative = None, setIsCEP = None, setIsCharter = None, setIsEntireSchoolMagnet = None, setIsMagnet = None, setIsNonLEA = None, setIsSpecialEducation = None, setIsTitleIII = None, setName = None, setNameIDSafetySpecialist = None, setNumberWiFiDevices = None, setPhoneNumber = None, setPhoneNumberIsInternational = None, setSchoolIDClonedFrom = None, setSchoolNumber = None, setSchoolYearID = None, setStaffIDPrincipal = None, setStateKindergartenScheduleIndicatorCodeMNID = None, setStateSchoolMNID = None, setStateTitleISchoolIndicatorCodeMNID = None, setType = None, setTypeCode = None, setRelationships = None, returnSchoolID = True, returnAllowsSchoolDevices = False, returnAllowsStudentDevices = False, returnBuildingID = False, returnCampusAccountabilityRatingID = False, returnCEEBCode = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnDaysInRegularSchoolYear = False, returnDaysPriorForAlgebraICounts = False, returnDistrictID = False, returnEdFiSchoolCategoryID = False, returnEdFiSchoolID = False, returnEducationalProgramHoursPerWeek = False, returnExcludeFromCRDC = False, returnFaxNumber = False, returnFaxNumberIsInternational = False, returnFederalAlternativeSchoolDetailID = False, returnFederalJusticeFacilityTypeID = False, returnFederalNCESSchoolID = False, returnFormattedFaxNumber = False, returnFormattedPhoneNumber = False, returnGradeLevelIDHigh = False, returnGradeLevelIDLow = False, returnHasAlcoholDrugEducation = False, returnHasAntiBullying = False, returnHasAntiViolence = False, returnHasAPCourses = False, returnHasAPSelfSelection = False, returnHasCorporalPunishment = False, returnHasCreditRecovery = False, returnHasCrisisPlan = False, returnHasDualEnrollment = False, returnHasFiberOptic = False, returnHasGifted = False, returnHasHomicideOccurred = False, returnHasIBDiplomaProgramme = False, returnHasPreschoolNonIDEAAge3 = False, returnHasPreschoolNonIDEAAge4 = False, returnHasPreschoolNonIDEAAge5 = False, returnHasSafetyPlan = False, returnHasShootingOccurred = False, returnHasSingleSexAthletics = False, returnHasSingleSexClasses = False, returnHasUngraded = False, returnHasUngradedMainlyElementary = False, returnHasUngradedMainlyHighSchool = False, returnHasUngradedMainlyMiddleSchool = False, returnHasWiFi = False, returnHasZeroTolerance = False, returnIsALCSchool = False, returnIsAlternative = False, returnIsCEP = False, returnIsCharter = False, returnIsCRDCCollectedForSchoolYear = False, returnIsEntireSchoolMagnet = False, returnIsMagnet = False, returnIsNonLEA = False, returnIsSpecialEducation = False, returnIsTitleIII = False, returnModifiedTime = False, returnName = False, returnNameIDSafetySpecialist = False, returnNumberWiFiDevices = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnSchoolIDClonedFrom = False, returnSchoolIDClonedTo = False, returnSchoolMNID = False, returnSchoolNumber = False, returnSchoolYearID = False, returnStaffIDPrincipal = False, returnStateKindergartenScheduleIndicatorCodeMNID = False, returnStateSchoolMNID = False, returnStateTitleISchoolIndicatorCodeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/School/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSchool(SchoolID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentAccountsMA(EntityID = 1, page = 1, pageSize = 100, returnStudentAccountsMAID = True, returnCreatedTime = False, returnFinancialAid = False, returniPadLease = False, returnModifiedTime = False, returnPaymentPlanMAID = False, returnPlaceofWorship = False, returnReligionID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentAccountsMA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentAccountsMA(StudentAccountsMAID, EntityID = 1, returnStudentAccountsMAID = True, returnCreatedTime = False, returnFinancialAid = False, returniPadLease = False, returnModifiedTime = False, returnPaymentPlanMAID = False, returnPlaceofWorship = False, returnReligionID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentAccountsMA/" + str(StudentAccountsMAID), verb = "get", return_params_list = return_params_list)

def modifyStudentAccountsMA(StudentAccountsMAID, EntityID = 1, setFinancialAid = None, setiPadLease = None, setPaymentPlanMAID = None, setPlaceofWorship = None, setReligionID = None, setStudentID = None, setRelationships = None, returnStudentAccountsMAID = True, returnCreatedTime = False, returnFinancialAid = False, returniPadLease = False, returnModifiedTime = False, returnPaymentPlanMAID = False, returnPlaceofWorship = False, returnReligionID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentAccountsMA/" + str(StudentAccountsMAID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentAccountsMA(EntityID = 1, setFinancialAid = None, setiPadLease = None, setPaymentPlanMAID = None, setPlaceofWorship = None, setReligionID = None, setStudentID = None, setRelationships = None, returnStudentAccountsMAID = True, returnCreatedTime = False, returnFinancialAid = False, returniPadLease = False, returnModifiedTime = False, returnPaymentPlanMAID = False, returnPlaceofWorship = False, returnReligionID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentAccountsMA/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentAccountsMA(StudentAccountsMAID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentEntityYear(EntityID = 1, page = 1, pageSize = 100, returnStudentEntityYearID = True, returnChromebookDocumentsReturned = False, returnCreatedTime = False, returnDaysAbsentYTD = False, returnDaysEnrolledYTD = False, returnDaysExcusedYTD = False, returnDaysOtherYTD = False, returnDaysUnexcusedYTD = False, returnEntityID = False, returnEntryWithdrawalIDLatest = False, returnExcludeFromHonorRoll = False, returnExcludeFromRank = False, returnExistsConflictedStudentCourseRequests = False, returnExistsUnscheduleableStudentSections = False, returnFeeAmountDue = False, returnFeeChargeAmount = False, returnFeePaidAmount = False, returnFeePaidAndWaivedAmount = False, returnFeeUnappliedAmount = False, returnFeeWaivedAmount = False, returnFirstName = False, returnFlaggedMissingAssignmentsCount = False, returnGrade = False, returnHandbookSigned = False, returnHasActiveCareerPlanDeclarationTimePeriod = False, returnHasActiveEndorsementDeclarationTimePeriod = False, returnHasConflictedStudentCourseRequest = False, returnHasFlaggedMissingAssignments = False, returnHasMissingAssignments = False, returnHasNoAttendanceToday = False, returnHasOpenDisplayPeriodsInRegularSchoolDay = False, returnHasOverscheduledPeriod = False, returnHasValidStudentPlan = False, returnHomeroomCodeFollettDestiny = False, returnHomeroomID = False, returnHomeroomPeriodFollettDestiny = False, returnHomeroomStaffNameFollettDestiny = False, returnIncludeAsProspectiveRank = False, returnIsActive = False, returnIsCrossEntityCourseEnrollment = False, returnIsDefaultEntity = False, returnIsTransportationRequested = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNumberOfStudentCourseRequests = False, returnNumberOfStudentSections = False, returnOptOutOfMedia = False, returnSchedulingCategories = False, returnSchedulingTeamID = False, returnSchoolYearID = False, returnSectionLengthAbsent = False, returnSectionLengthEnrolled = False, returnSemester2Absent = False, returnSemester2Enrolled = False, returnSignedAcceptableUsePolicy = False, returnStaffIDAdvisor = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnTardyCountYTD = False, returnTardyKioskTotals = False, returnTotalEarnedCreditsPossibleAnticipatedNonTransferStudentSectionsNonAlternateRequestCredits = False, returnTotalMissedAssignmentCount = False, returnUILFeeReceived = False, returnUnscheduleableStudentSectionCount = False, returnUnscheduledStudentCourseRequestCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDate = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentEntityYear(StudentEntityYearID, EntityID = 1, returnStudentEntityYearID = True, returnChromebookDocumentsReturned = False, returnCreatedTime = False, returnDaysAbsentYTD = False, returnDaysEnrolledYTD = False, returnDaysExcusedYTD = False, returnDaysOtherYTD = False, returnDaysUnexcusedYTD = False, returnEntityID = False, returnEntryWithdrawalIDLatest = False, returnExcludeFromHonorRoll = False, returnExcludeFromRank = False, returnExistsConflictedStudentCourseRequests = False, returnExistsUnscheduleableStudentSections = False, returnFeeAmountDue = False, returnFeeChargeAmount = False, returnFeePaidAmount = False, returnFeePaidAndWaivedAmount = False, returnFeeUnappliedAmount = False, returnFeeWaivedAmount = False, returnFirstName = False, returnFlaggedMissingAssignmentsCount = False, returnGrade = False, returnHandbookSigned = False, returnHasActiveCareerPlanDeclarationTimePeriod = False, returnHasActiveEndorsementDeclarationTimePeriod = False, returnHasConflictedStudentCourseRequest = False, returnHasFlaggedMissingAssignments = False, returnHasMissingAssignments = False, returnHasNoAttendanceToday = False, returnHasOpenDisplayPeriodsInRegularSchoolDay = False, returnHasOverscheduledPeriod = False, returnHasValidStudentPlan = False, returnHomeroomCodeFollettDestiny = False, returnHomeroomID = False, returnHomeroomPeriodFollettDestiny = False, returnHomeroomStaffNameFollettDestiny = False, returnIncludeAsProspectiveRank = False, returnIsActive = False, returnIsCrossEntityCourseEnrollment = False, returnIsDefaultEntity = False, returnIsTransportationRequested = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNumberOfStudentCourseRequests = False, returnNumberOfStudentSections = False, returnOptOutOfMedia = False, returnSchedulingCategories = False, returnSchedulingTeamID = False, returnSchoolYearID = False, returnSectionLengthAbsent = False, returnSectionLengthEnrolled = False, returnSemester2Absent = False, returnSemester2Enrolled = False, returnSignedAcceptableUsePolicy = False, returnStaffIDAdvisor = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnTardyCountYTD = False, returnTardyKioskTotals = False, returnTotalEarnedCreditsPossibleAnticipatedNonTransferStudentSectionsNonAlternateRequestCredits = False, returnTotalMissedAssignmentCount = False, returnUILFeeReceived = False, returnUnscheduleableStudentSectionCount = False, returnUnscheduledStudentCourseRequestCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDate = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentEntityYear/" + str(StudentEntityYearID), verb = "get", return_params_list = return_params_list)

def modifyStudentEntityYear(StudentEntityYearID, EntityID = 1, setChromebookDocumentsReturned = None, setEntityID = None, setEntryWithdrawalIDLatest = None, setExcludeFromHonorRoll = None, setExcludeFromRank = None, setFirstName = None, setGrade = None, setHandbookSigned = None, setHomeroomID = None, setIncludeAsProspectiveRank = None, setIsActive = None, setIsCrossEntityCourseEnrollment = None, setIsDefaultEntity = None, setIsTransportationRequested = None, setLastName = None, setMiddleName = None, setNameID = None, setOptOutOfMedia = None, setSchedulingCategories = None, setSchedulingTeamID = None, setSchoolYearID = None, setSignedAcceptableUsePolicy = None, setStaffIDAdvisor = None, setStaffIDDisciplineOfficer = None, setStudentID = None, setStudentNumber = None, setUILFeeReceived = None, setRelationships = None, returnStudentEntityYearID = True, returnChromebookDocumentsReturned = False, returnCreatedTime = False, returnDaysAbsentYTD = False, returnDaysEnrolledYTD = False, returnDaysExcusedYTD = False, returnDaysOtherYTD = False, returnDaysUnexcusedYTD = False, returnEntityID = False, returnEntryWithdrawalIDLatest = False, returnExcludeFromHonorRoll = False, returnExcludeFromRank = False, returnExistsConflictedStudentCourseRequests = False, returnExistsUnscheduleableStudentSections = False, returnFeeAmountDue = False, returnFeeChargeAmount = False, returnFeePaidAmount = False, returnFeePaidAndWaivedAmount = False, returnFeeUnappliedAmount = False, returnFeeWaivedAmount = False, returnFirstName = False, returnFlaggedMissingAssignmentsCount = False, returnGrade = False, returnHandbookSigned = False, returnHasActiveCareerPlanDeclarationTimePeriod = False, returnHasActiveEndorsementDeclarationTimePeriod = False, returnHasConflictedStudentCourseRequest = False, returnHasFlaggedMissingAssignments = False, returnHasMissingAssignments = False, returnHasNoAttendanceToday = False, returnHasOpenDisplayPeriodsInRegularSchoolDay = False, returnHasOverscheduledPeriod = False, returnHasValidStudentPlan = False, returnHomeroomCodeFollettDestiny = False, returnHomeroomID = False, returnHomeroomPeriodFollettDestiny = False, returnHomeroomStaffNameFollettDestiny = False, returnIncludeAsProspectiveRank = False, returnIsActive = False, returnIsCrossEntityCourseEnrollment = False, returnIsDefaultEntity = False, returnIsTransportationRequested = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNumberOfStudentCourseRequests = False, returnNumberOfStudentSections = False, returnOptOutOfMedia = False, returnSchedulingCategories = False, returnSchedulingTeamID = False, returnSchoolYearID = False, returnSectionLengthAbsent = False, returnSectionLengthEnrolled = False, returnSemester2Absent = False, returnSemester2Enrolled = False, returnSignedAcceptableUsePolicy = False, returnStaffIDAdvisor = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnTardyCountYTD = False, returnTardyKioskTotals = False, returnTotalEarnedCreditsPossibleAnticipatedNonTransferStudentSectionsNonAlternateRequestCredits = False, returnTotalMissedAssignmentCount = False, returnUILFeeReceived = False, returnUnscheduleableStudentSectionCount = False, returnUnscheduledStudentCourseRequestCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDate = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentEntityYear/" + str(StudentEntityYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentEntityYear(EntityID = 1, setChromebookDocumentsReturned = None, setEntityID = None, setEntryWithdrawalIDLatest = None, setExcludeFromHonorRoll = None, setExcludeFromRank = None, setFirstName = None, setGrade = None, setHandbookSigned = None, setHomeroomID = None, setIncludeAsProspectiveRank = None, setIsActive = None, setIsCrossEntityCourseEnrollment = None, setIsDefaultEntity = None, setIsTransportationRequested = None, setLastName = None, setMiddleName = None, setNameID = None, setOptOutOfMedia = None, setSchedulingCategories = None, setSchedulingTeamID = None, setSchoolYearID = None, setSignedAcceptableUsePolicy = None, setStaffIDAdvisor = None, setStaffIDDisciplineOfficer = None, setStudentID = None, setStudentNumber = None, setUILFeeReceived = None, setRelationships = None, returnStudentEntityYearID = True, returnChromebookDocumentsReturned = False, returnCreatedTime = False, returnDaysAbsentYTD = False, returnDaysEnrolledYTD = False, returnDaysExcusedYTD = False, returnDaysOtherYTD = False, returnDaysUnexcusedYTD = False, returnEntityID = False, returnEntryWithdrawalIDLatest = False, returnExcludeFromHonorRoll = False, returnExcludeFromRank = False, returnExistsConflictedStudentCourseRequests = False, returnExistsUnscheduleableStudentSections = False, returnFeeAmountDue = False, returnFeeChargeAmount = False, returnFeePaidAmount = False, returnFeePaidAndWaivedAmount = False, returnFeeUnappliedAmount = False, returnFeeWaivedAmount = False, returnFirstName = False, returnFlaggedMissingAssignmentsCount = False, returnGrade = False, returnHandbookSigned = False, returnHasActiveCareerPlanDeclarationTimePeriod = False, returnHasActiveEndorsementDeclarationTimePeriod = False, returnHasConflictedStudentCourseRequest = False, returnHasFlaggedMissingAssignments = False, returnHasMissingAssignments = False, returnHasNoAttendanceToday = False, returnHasOpenDisplayPeriodsInRegularSchoolDay = False, returnHasOverscheduledPeriod = False, returnHasValidStudentPlan = False, returnHomeroomCodeFollettDestiny = False, returnHomeroomID = False, returnHomeroomPeriodFollettDestiny = False, returnHomeroomStaffNameFollettDestiny = False, returnIncludeAsProspectiveRank = False, returnIsActive = False, returnIsCrossEntityCourseEnrollment = False, returnIsDefaultEntity = False, returnIsTransportationRequested = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNumberOfStudentCourseRequests = False, returnNumberOfStudentSections = False, returnOptOutOfMedia = False, returnSchedulingCategories = False, returnSchedulingTeamID = False, returnSchoolYearID = False, returnSectionLengthAbsent = False, returnSectionLengthEnrolled = False, returnSemester2Absent = False, returnSemester2Enrolled = False, returnSignedAcceptableUsePolicy = False, returnStaffIDAdvisor = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnTardyCountYTD = False, returnTardyKioskTotals = False, returnTotalEarnedCreditsPossibleAnticipatedNonTransferStudentSectionsNonAlternateRequestCredits = False, returnTotalMissedAssignmentCount = False, returnUILFeeReceived = False, returnUnscheduleableStudentSectionCount = False, returnUnscheduledStudentCourseRequestCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDate = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentEntityYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentEntityYear(StudentEntityYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentType(EntityID = 1, page = 1, pageSize = 100, returnStudentTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentType(StudentTypeID, EntityID = 1, returnStudentTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentType/" + str(StudentTypeID), verb = "get", return_params_list = return_params_list)

def modifyStudentType(StudentTypeID, EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setRelationships = None, returnStudentTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentType/" + str(StudentTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentType(EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setRelationships = None, returnStudentTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentType(StudentTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempAffectedWithdrawalRecord(EntityID = 1, page = 1, pageSize = 100, returnTempAffectedWithdrawalRecordID = True, returnAction = False, returnActionCode = False, returnActionMessage = False, returnAffectedPrimaryKey = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHasAttendance = False, returnHasFutureAttendance = False, returnHasFutureGrades = False, returnHasGrades = False, returnHasPartiallyPaidFees = False, returnIsFutureEntryWithdrawal = False, returnModifiedTime = False, returnMostFutureGradeStartDate = False, returnNameIDRequestedBy = False, returnNewEndDate = False, returnRecordType = False, returnRecordTypeCode = False, returnSchoolYearID = False, returnSection = False, returnSectionID = False, returnStartDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempAffectedWithdrawalRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempAffectedWithdrawalRecord(TempAffectedWithdrawalRecordID, EntityID = 1, returnTempAffectedWithdrawalRecordID = True, returnAction = False, returnActionCode = False, returnActionMessage = False, returnAffectedPrimaryKey = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHasAttendance = False, returnHasFutureAttendance = False, returnHasFutureGrades = False, returnHasGrades = False, returnHasPartiallyPaidFees = False, returnIsFutureEntryWithdrawal = False, returnModifiedTime = False, returnMostFutureGradeStartDate = False, returnNameIDRequestedBy = False, returnNewEndDate = False, returnRecordType = False, returnRecordTypeCode = False, returnSchoolYearID = False, returnSection = False, returnSectionID = False, returnStartDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempAffectedWithdrawalRecord/" + str(TempAffectedWithdrawalRecordID), verb = "get", return_params_list = return_params_list)

def modifyTempAffectedWithdrawalRecord(TempAffectedWithdrawalRecordID, EntityID = 1, setAction = None, setActionCode = None, setActionMessage = None, setAffectedPrimaryKey = None, setCourseID = None, setDescription = None, setEndDate = None, setEntityID = None, setHasAttendance = None, setHasFutureAttendance = None, setHasFutureGrades = None, setHasGrades = None, setHasPartiallyPaidFees = None, setIsFutureEntryWithdrawal = None, setMostFutureGradeStartDate = None, setNameIDRequestedBy = None, setNewEndDate = None, setRecordType = None, setRecordTypeCode = None, setSchoolYearID = None, setSection = None, setSectionID = None, setStartDate = None, setStudentID = None, setRelationships = None, returnTempAffectedWithdrawalRecordID = True, returnAction = False, returnActionCode = False, returnActionMessage = False, returnAffectedPrimaryKey = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHasAttendance = False, returnHasFutureAttendance = False, returnHasFutureGrades = False, returnHasGrades = False, returnHasPartiallyPaidFees = False, returnIsFutureEntryWithdrawal = False, returnModifiedTime = False, returnMostFutureGradeStartDate = False, returnNameIDRequestedBy = False, returnNewEndDate = False, returnRecordType = False, returnRecordTypeCode = False, returnSchoolYearID = False, returnSection = False, returnSectionID = False, returnStartDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempAffectedWithdrawalRecord/" + str(TempAffectedWithdrawalRecordID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempAffectedWithdrawalRecord(EntityID = 1, setAction = None, setActionCode = None, setActionMessage = None, setAffectedPrimaryKey = None, setCourseID = None, setDescription = None, setEndDate = None, setEntityID = None, setHasAttendance = None, setHasFutureAttendance = None, setHasFutureGrades = None, setHasGrades = None, setHasPartiallyPaidFees = None, setIsFutureEntryWithdrawal = None, setMostFutureGradeStartDate = None, setNameIDRequestedBy = None, setNewEndDate = None, setRecordType = None, setRecordTypeCode = None, setSchoolYearID = None, setSection = None, setSectionID = None, setStartDate = None, setStudentID = None, setRelationships = None, returnTempAffectedWithdrawalRecordID = True, returnAction = False, returnActionCode = False, returnActionMessage = False, returnAffectedPrimaryKey = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHasAttendance = False, returnHasFutureAttendance = False, returnHasFutureGrades = False, returnHasGrades = False, returnHasPartiallyPaidFees = False, returnIsFutureEntryWithdrawal = False, returnModifiedTime = False, returnMostFutureGradeStartDate = False, returnNameIDRequestedBy = False, returnNewEndDate = False, returnRecordType = False, returnRecordTypeCode = False, returnSchoolYearID = False, returnSection = False, returnSectionID = False, returnStartDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempAffectedWithdrawalRecord/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempAffectedWithdrawalRecord(TempAffectedWithdrawalRecordID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempHomeroomError(EntityID = 1, page = 1, pageSize = 100, returnTempHomeroomErrorID = True, returnCode = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnTempHomeroomRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempHomeroomError(TempHomeroomErrorID, EntityID = 1, returnTempHomeroomErrorID = True, returnCode = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnTempHomeroomRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomError/" + str(TempHomeroomErrorID), verb = "get", return_params_list = return_params_list)

def modifyTempHomeroomError(TempHomeroomErrorID, EntityID = 1, setCode = None, setFailureReason = None, setTempHomeroomRecordID = None, setRelationships = None, returnTempHomeroomErrorID = True, returnCode = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnTempHomeroomRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomError/" + str(TempHomeroomErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempHomeroomError(EntityID = 1, setCode = None, setFailureReason = None, setTempHomeroomRecordID = None, setRelationships = None, returnTempHomeroomErrorID = True, returnCode = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnTempHomeroomRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempHomeroomError(TempHomeroomErrorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempHomeroomRecord(EntityID = 1, page = 1, pageSize = 100, returnTempHomeroomRecordID = True, returnBuilding = False, returnBuildingID = False, returnCode = False, returnColumnIndex = False, returnCreatedTime = False, returnHasSaveError = False, returnHomeroomID = False, returnIsOverwrite = False, returnModifiedTime = False, returnRoom = False, returnRoomID = False, returnSchoolYear = False, returnSchoolYearID = False, returnStaff = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempHomeroomRecord(TempHomeroomRecordID, EntityID = 1, returnTempHomeroomRecordID = True, returnBuilding = False, returnBuildingID = False, returnCode = False, returnColumnIndex = False, returnCreatedTime = False, returnHasSaveError = False, returnHomeroomID = False, returnIsOverwrite = False, returnModifiedTime = False, returnRoom = False, returnRoomID = False, returnSchoolYear = False, returnSchoolYearID = False, returnStaff = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomRecord/" + str(TempHomeroomRecordID), verb = "get", return_params_list = return_params_list)

def modifyTempHomeroomRecord(TempHomeroomRecordID, EntityID = 1, setBuilding = None, setBuildingID = None, setCode = None, setColumnIndex = None, setHasSaveError = None, setHomeroomID = None, setIsOverwrite = None, setRoom = None, setRoomID = None, setSchoolYear = None, setSchoolYearID = None, setStaff = None, setStaffID = None, setRelationships = None, returnTempHomeroomRecordID = True, returnBuilding = False, returnBuildingID = False, returnCode = False, returnColumnIndex = False, returnCreatedTime = False, returnHasSaveError = False, returnHomeroomID = False, returnIsOverwrite = False, returnModifiedTime = False, returnRoom = False, returnRoomID = False, returnSchoolYear = False, returnSchoolYearID = False, returnStaff = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomRecord/" + str(TempHomeroomRecordID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempHomeroomRecord(EntityID = 1, setBuilding = None, setBuildingID = None, setCode = None, setColumnIndex = None, setHasSaveError = None, setHomeroomID = None, setIsOverwrite = None, setRoom = None, setRoomID = None, setSchoolYear = None, setSchoolYearID = None, setStaff = None, setStaffID = None, setRelationships = None, returnTempHomeroomRecordID = True, returnBuilding = False, returnBuildingID = False, returnCode = False, returnColumnIndex = False, returnCreatedTime = False, returnHasSaveError = False, returnHomeroomID = False, returnIsOverwrite = False, returnModifiedTime = False, returnRoom = False, returnRoomID = False, returnSchoolYear = False, returnSchoolYearID = False, returnStaff = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomRecord/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempHomeroomRecord(TempHomeroomRecordID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempNoShowEntryWithdrawal(EntityID = 1, page = 1, pageSize = 100, returnTempNoShowEntryWithdrawalID = True, returnCreatedTime = False, returnDisplayAction = False, returnDisplayActionCode = False, returnEndDate = False, returnEntity = False, returnEntryCode = False, returnEntryWithdrawalID = False, returnFailureReason = False, returnGradeLevel = False, returnModifiedTime = False, returnNoShowAction = False, returnNoShowActionCode = False, returnNoShowEntryWithdrawalType = False, returnNoShowEntryWithdrawalTypeCode = False, returnNoShowTypeOfNoShow = False, returnNoShowTypeOfNoShowCode = False, returnSchoolYear = False, returnSchoolYearID = False, returnStartDate = False, returnStudent = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCode = False, returnWithdrawalCodeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNoShowEntryWithdrawal/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempNoShowEntryWithdrawal(TempNoShowEntryWithdrawalID, EntityID = 1, returnTempNoShowEntryWithdrawalID = True, returnCreatedTime = False, returnDisplayAction = False, returnDisplayActionCode = False, returnEndDate = False, returnEntity = False, returnEntryCode = False, returnEntryWithdrawalID = False, returnFailureReason = False, returnGradeLevel = False, returnModifiedTime = False, returnNoShowAction = False, returnNoShowActionCode = False, returnNoShowEntryWithdrawalType = False, returnNoShowEntryWithdrawalTypeCode = False, returnNoShowTypeOfNoShow = False, returnNoShowTypeOfNoShowCode = False, returnSchoolYear = False, returnSchoolYearID = False, returnStartDate = False, returnStudent = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCode = False, returnWithdrawalCodeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNoShowEntryWithdrawal/" + str(TempNoShowEntryWithdrawalID), verb = "get", return_params_list = return_params_list)

def modifyTempNoShowEntryWithdrawal(TempNoShowEntryWithdrawalID, EntityID = 1, setDisplayAction = None, setDisplayActionCode = None, setEndDate = None, setEntity = None, setEntryCode = None, setEntryWithdrawalID = None, setFailureReason = None, setGradeLevel = None, setNoShowAction = None, setNoShowActionCode = None, setNoShowEntryWithdrawalType = None, setNoShowEntryWithdrawalTypeCode = None, setNoShowTypeOfNoShow = None, setNoShowTypeOfNoShowCode = None, setSchoolYear = None, setSchoolYearID = None, setStartDate = None, setStudent = None, setStudentID = None, setStudentNumber = None, setWithdrawalCode = None, setWithdrawalCodeID = None, setRelationships = None, returnTempNoShowEntryWithdrawalID = True, returnCreatedTime = False, returnDisplayAction = False, returnDisplayActionCode = False, returnEndDate = False, returnEntity = False, returnEntryCode = False, returnEntryWithdrawalID = False, returnFailureReason = False, returnGradeLevel = False, returnModifiedTime = False, returnNoShowAction = False, returnNoShowActionCode = False, returnNoShowEntryWithdrawalType = False, returnNoShowEntryWithdrawalTypeCode = False, returnNoShowTypeOfNoShow = False, returnNoShowTypeOfNoShowCode = False, returnSchoolYear = False, returnSchoolYearID = False, returnStartDate = False, returnStudent = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCode = False, returnWithdrawalCodeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNoShowEntryWithdrawal/" + str(TempNoShowEntryWithdrawalID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempNoShowEntryWithdrawal(EntityID = 1, setDisplayAction = None, setDisplayActionCode = None, setEndDate = None, setEntity = None, setEntryCode = None, setEntryWithdrawalID = None, setFailureReason = None, setGradeLevel = None, setNoShowAction = None, setNoShowActionCode = None, setNoShowEntryWithdrawalType = None, setNoShowEntryWithdrawalTypeCode = None, setNoShowTypeOfNoShow = None, setNoShowTypeOfNoShowCode = None, setSchoolYear = None, setSchoolYearID = None, setStartDate = None, setStudent = None, setStudentID = None, setStudentNumber = None, setWithdrawalCode = None, setWithdrawalCodeID = None, setRelationships = None, returnTempNoShowEntryWithdrawalID = True, returnCreatedTime = False, returnDisplayAction = False, returnDisplayActionCode = False, returnEndDate = False, returnEntity = False, returnEntryCode = False, returnEntryWithdrawalID = False, returnFailureReason = False, returnGradeLevel = False, returnModifiedTime = False, returnNoShowAction = False, returnNoShowActionCode = False, returnNoShowEntryWithdrawalType = False, returnNoShowEntryWithdrawalTypeCode = False, returnNoShowTypeOfNoShow = False, returnNoShowTypeOfNoShowCode = False, returnSchoolYear = False, returnSchoolYearID = False, returnStartDate = False, returnStudent = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCode = False, returnWithdrawalCodeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNoShowEntryWithdrawal/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempNoShowEntryWithdrawal(TempNoShowEntryWithdrawalID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentEnrollmentRecord(EntityID = 1, page = 1, pageSize = 100, returnTempStudentEnrollmentRecordID = True, returnAdvisorFullName = False, returnCalendarCode = False, returnCalendarID = False, returnCompletedSchoolYearOverride = False, returnCreatedTime = False, returnCreateFeeManagementCustomer = False, returnCreateFeeManagementCustomerEntityYear = False, returnDisciplineOfficerFullName = False, returnEdFiDistrictIDResidence = False, returnEdFiDistrictIDTransfer = False, returnEdFiDistrictResidenceCodeDescription = False, returnEdFiSchoolIDTransfer = False, returnEndDate = False, returnEnrollIntoEntityCode = False, returnEnrollmentMoveable = False, returnEntityCode = False, returnEntityID = False, returnEntryCode = False, returnEntryCodeID = False, returnEntryComment = False, returnEntryWithdrawalID = False, returnExcludeFromHonorRoll = False, returnExcludeFromRank = False, returnExcludeFromThirdFridaySeptemberCount = False, returnFailureReason = False, returnFeeManagementCustomerID = False, returnGradeLevelCode = False, returnGradeReferenceID = False, returnGradYear = False, returnGSAADAClaimableOverrideCode = False, returnGSAADAClaimableOverrideCodeDisplayName = False, returnHomeroomCode = False, returnHomeroomID = False, returnIncludeAsProspectiveRank = False, returnIsCurrentActive = False, returnIsDefaultEntityForEntryWithdrawal = False, returnIsDefaultEntityForStudentEntityYear = False, returnIsPermanentExit = False, returnIsPrivateSchoolChoiceStudent = False, returnIsTuitionPaidOutOfDistrict = False, returnModifiedTime = False, returnNumericYear = False, returnOutgoingStudent = False, returnPercentEnrolled = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnScheduledSectionCount = False, returnSchoolCode = False, returnSchoolID = False, returnSchoolYearID = False, returnServingRCDTSOverrideCode = False, returnServingRCDTSOverrideCodeDisplayName = False, returnServingRCDTSOverrideID = False, returnSourceEntryWithdrawalID = False, returnStaffIDAdvisor = False, returnStaffIDDisciplineOfficer = False, returnStartDate = False, returnStateAidCategoryMNID = False, returnStateDistrictMNCodeName = False, returnStateDistrictMNID = False, returnStateLastAttendanceLocationCodeMNID = False, returnStudentCourseRequestNotMoveableCount = False, returnStudentCourseRequestToDeleteCount = False, returnStudentFullName = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnStudentTypeID = False, returnTestingSchoolCode = False, returnTestingSchoolCodeDisplayName = False, returnTestingSchoolRCDTSOverrideCode = False, returnTestingSchoolRCDTSOverrideCodeDisplayName = False, returnTestingSchoolRCDTSOverrideID = False, returnTotalStudentCourseRequestCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCode = False, returnWithdrawalCodeID = False, returnWithdrawalComment = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentEnrollmentRecord(TempStudentEnrollmentRecordID, EntityID = 1, returnTempStudentEnrollmentRecordID = True, returnAdvisorFullName = False, returnCalendarCode = False, returnCalendarID = False, returnCompletedSchoolYearOverride = False, returnCreatedTime = False, returnCreateFeeManagementCustomer = False, returnCreateFeeManagementCustomerEntityYear = False, returnDisciplineOfficerFullName = False, returnEdFiDistrictIDResidence = False, returnEdFiDistrictIDTransfer = False, returnEdFiDistrictResidenceCodeDescription = False, returnEdFiSchoolIDTransfer = False, returnEndDate = False, returnEnrollIntoEntityCode = False, returnEnrollmentMoveable = False, returnEntityCode = False, returnEntityID = False, returnEntryCode = False, returnEntryCodeID = False, returnEntryComment = False, returnEntryWithdrawalID = False, returnExcludeFromHonorRoll = False, returnExcludeFromRank = False, returnExcludeFromThirdFridaySeptemberCount = False, returnFailureReason = False, returnFeeManagementCustomerID = False, returnGradeLevelCode = False, returnGradeReferenceID = False, returnGradYear = False, returnGSAADAClaimableOverrideCode = False, returnGSAADAClaimableOverrideCodeDisplayName = False, returnHomeroomCode = False, returnHomeroomID = False, returnIncludeAsProspectiveRank = False, returnIsCurrentActive = False, returnIsDefaultEntityForEntryWithdrawal = False, returnIsDefaultEntityForStudentEntityYear = False, returnIsPermanentExit = False, returnIsPrivateSchoolChoiceStudent = False, returnIsTuitionPaidOutOfDistrict = False, returnModifiedTime = False, returnNumericYear = False, returnOutgoingStudent = False, returnPercentEnrolled = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnScheduledSectionCount = False, returnSchoolCode = False, returnSchoolID = False, returnSchoolYearID = False, returnServingRCDTSOverrideCode = False, returnServingRCDTSOverrideCodeDisplayName = False, returnServingRCDTSOverrideID = False, returnSourceEntryWithdrawalID = False, returnStaffIDAdvisor = False, returnStaffIDDisciplineOfficer = False, returnStartDate = False, returnStateAidCategoryMNID = False, returnStateDistrictMNCodeName = False, returnStateDistrictMNID = False, returnStateLastAttendanceLocationCodeMNID = False, returnStudentCourseRequestNotMoveableCount = False, returnStudentCourseRequestToDeleteCount = False, returnStudentFullName = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnStudentTypeID = False, returnTestingSchoolCode = False, returnTestingSchoolCodeDisplayName = False, returnTestingSchoolRCDTSOverrideCode = False, returnTestingSchoolRCDTSOverrideCodeDisplayName = False, returnTestingSchoolRCDTSOverrideID = False, returnTotalStudentCourseRequestCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCode = False, returnWithdrawalCodeID = False, returnWithdrawalComment = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentRecord/" + str(TempStudentEnrollmentRecordID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentEnrollmentRecord(TempStudentEnrollmentRecordID, EntityID = 1, setAdvisorFullName = None, setCalendarCode = None, setCalendarID = None, setCompletedSchoolYearOverride = None, setCreateFeeManagementCustomer = None, setCreateFeeManagementCustomerEntityYear = None, setDisciplineOfficerFullName = None, setEdFiDistrictIDResidence = None, setEdFiDistrictIDTransfer = None, setEdFiDistrictResidenceCodeDescription = None, setEdFiSchoolIDTransfer = None, setEndDate = None, setEnrollIntoEntityCode = None, setEnrollmentMoveable = None, setEntityCode = None, setEntityID = None, setEntryCode = None, setEntryCodeID = None, setEntryComment = None, setEntryWithdrawalID = None, setExcludeFromHonorRoll = None, setExcludeFromRank = None, setExcludeFromThirdFridaySeptemberCount = None, setFailureReason = None, setFeeManagementCustomerID = None, setGradeLevelCode = None, setGradeReferenceID = None, setGradYear = None, setGSAADAClaimableOverrideCode = None, setGSAADAClaimableOverrideCodeDisplayName = None, setHomeroomCode = None, setHomeroomID = None, setIncludeAsProspectiveRank = None, setIsCurrentActive = None, setIsDefaultEntityForEntryWithdrawal = None, setIsDefaultEntityForStudentEntityYear = None, setIsPermanentExit = None, setIsPrivateSchoolChoiceStudent = None, setIsTuitionPaidOutOfDistrict = None, setNumericYear = None, setOutgoingStudent = None, setPercentEnrolled = None, setPromotionStatus = None, setPromotionStatusCode = None, setScheduledSectionCount = None, setSchoolCode = None, setSchoolID = None, setSchoolYearID = None, setServingRCDTSOverrideCode = None, setServingRCDTSOverrideCodeDisplayName = None, setServingRCDTSOverrideID = None, setSourceEntryWithdrawalID = None, setStaffIDAdvisor = None, setStaffIDDisciplineOfficer = None, setStartDate = None, setStateAidCategoryMNID = None, setStateDistrictMNCodeName = None, setStateDistrictMNID = None, setStateLastAttendanceLocationCodeMNID = None, setStudentCourseRequestNotMoveableCount = None, setStudentCourseRequestToDeleteCount = None, setStudentFullName = None, setStudentID = None, setStudentNumber = None, setStudentTypeCode = None, setStudentTypeID = None, setTestingSchoolCode = None, setTestingSchoolCodeDisplayName = None, setTestingSchoolRCDTSOverrideCode = None, setTestingSchoolRCDTSOverrideCodeDisplayName = None, setTestingSchoolRCDTSOverrideID = None, setTotalStudentCourseRequestCount = None, setWithdrawalCode = None, setWithdrawalCodeID = None, setWithdrawalComment = None, setRelationships = None, returnTempStudentEnrollmentRecordID = True, returnAdvisorFullName = False, returnCalendarCode = False, returnCalendarID = False, returnCompletedSchoolYearOverride = False, returnCreatedTime = False, returnCreateFeeManagementCustomer = False, returnCreateFeeManagementCustomerEntityYear = False, returnDisciplineOfficerFullName = False, returnEdFiDistrictIDResidence = False, returnEdFiDistrictIDTransfer = False, returnEdFiDistrictResidenceCodeDescription = False, returnEdFiSchoolIDTransfer = False, returnEndDate = False, returnEnrollIntoEntityCode = False, returnEnrollmentMoveable = False, returnEntityCode = False, returnEntityID = False, returnEntryCode = False, returnEntryCodeID = False, returnEntryComment = False, returnEntryWithdrawalID = False, returnExcludeFromHonorRoll = False, returnExcludeFromRank = False, returnExcludeFromThirdFridaySeptemberCount = False, returnFailureReason = False, returnFeeManagementCustomerID = False, returnGradeLevelCode = False, returnGradeReferenceID = False, returnGradYear = False, returnGSAADAClaimableOverrideCode = False, returnGSAADAClaimableOverrideCodeDisplayName = False, returnHomeroomCode = False, returnHomeroomID = False, returnIncludeAsProspectiveRank = False, returnIsCurrentActive = False, returnIsDefaultEntityForEntryWithdrawal = False, returnIsDefaultEntityForStudentEntityYear = False, returnIsPermanentExit = False, returnIsPrivateSchoolChoiceStudent = False, returnIsTuitionPaidOutOfDistrict = False, returnModifiedTime = False, returnNumericYear = False, returnOutgoingStudent = False, returnPercentEnrolled = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnScheduledSectionCount = False, returnSchoolCode = False, returnSchoolID = False, returnSchoolYearID = False, returnServingRCDTSOverrideCode = False, returnServingRCDTSOverrideCodeDisplayName = False, returnServingRCDTSOverrideID = False, returnSourceEntryWithdrawalID = False, returnStaffIDAdvisor = False, returnStaffIDDisciplineOfficer = False, returnStartDate = False, returnStateAidCategoryMNID = False, returnStateDistrictMNCodeName = False, returnStateDistrictMNID = False, returnStateLastAttendanceLocationCodeMNID = False, returnStudentCourseRequestNotMoveableCount = False, returnStudentCourseRequestToDeleteCount = False, returnStudentFullName = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnStudentTypeID = False, returnTestingSchoolCode = False, returnTestingSchoolCodeDisplayName = False, returnTestingSchoolRCDTSOverrideCode = False, returnTestingSchoolRCDTSOverrideCodeDisplayName = False, returnTestingSchoolRCDTSOverrideID = False, returnTotalStudentCourseRequestCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCode = False, returnWithdrawalCodeID = False, returnWithdrawalComment = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentRecord/" + str(TempStudentEnrollmentRecordID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentEnrollmentRecord(EntityID = 1, setAdvisorFullName = None, setCalendarCode = None, setCalendarID = None, setCompletedSchoolYearOverride = None, setCreateFeeManagementCustomer = None, setCreateFeeManagementCustomerEntityYear = None, setDisciplineOfficerFullName = None, setEdFiDistrictIDResidence = None, setEdFiDistrictIDTransfer = None, setEdFiDistrictResidenceCodeDescription = None, setEdFiSchoolIDTransfer = None, setEndDate = None, setEnrollIntoEntityCode = None, setEnrollmentMoveable = None, setEntityCode = None, setEntityID = None, setEntryCode = None, setEntryCodeID = None, setEntryComment = None, setEntryWithdrawalID = None, setExcludeFromHonorRoll = None, setExcludeFromRank = None, setExcludeFromThirdFridaySeptemberCount = None, setFailureReason = None, setFeeManagementCustomerID = None, setGradeLevelCode = None, setGradeReferenceID = None, setGradYear = None, setGSAADAClaimableOverrideCode = None, setGSAADAClaimableOverrideCodeDisplayName = None, setHomeroomCode = None, setHomeroomID = None, setIncludeAsProspectiveRank = None, setIsCurrentActive = None, setIsDefaultEntityForEntryWithdrawal = None, setIsDefaultEntityForStudentEntityYear = None, setIsPermanentExit = None, setIsPrivateSchoolChoiceStudent = None, setIsTuitionPaidOutOfDistrict = None, setNumericYear = None, setOutgoingStudent = None, setPercentEnrolled = None, setPromotionStatus = None, setPromotionStatusCode = None, setScheduledSectionCount = None, setSchoolCode = None, setSchoolID = None, setSchoolYearID = None, setServingRCDTSOverrideCode = None, setServingRCDTSOverrideCodeDisplayName = None, setServingRCDTSOverrideID = None, setSourceEntryWithdrawalID = None, setStaffIDAdvisor = None, setStaffIDDisciplineOfficer = None, setStartDate = None, setStateAidCategoryMNID = None, setStateDistrictMNCodeName = None, setStateDistrictMNID = None, setStateLastAttendanceLocationCodeMNID = None, setStudentCourseRequestNotMoveableCount = None, setStudentCourseRequestToDeleteCount = None, setStudentFullName = None, setStudentID = None, setStudentNumber = None, setStudentTypeCode = None, setStudentTypeID = None, setTestingSchoolCode = None, setTestingSchoolCodeDisplayName = None, setTestingSchoolRCDTSOverrideCode = None, setTestingSchoolRCDTSOverrideCodeDisplayName = None, setTestingSchoolRCDTSOverrideID = None, setTotalStudentCourseRequestCount = None, setWithdrawalCode = None, setWithdrawalCodeID = None, setWithdrawalComment = None, setRelationships = None, returnTempStudentEnrollmentRecordID = True, returnAdvisorFullName = False, returnCalendarCode = False, returnCalendarID = False, returnCompletedSchoolYearOverride = False, returnCreatedTime = False, returnCreateFeeManagementCustomer = False, returnCreateFeeManagementCustomerEntityYear = False, returnDisciplineOfficerFullName = False, returnEdFiDistrictIDResidence = False, returnEdFiDistrictIDTransfer = False, returnEdFiDistrictResidenceCodeDescription = False, returnEdFiSchoolIDTransfer = False, returnEndDate = False, returnEnrollIntoEntityCode = False, returnEnrollmentMoveable = False, returnEntityCode = False, returnEntityID = False, returnEntryCode = False, returnEntryCodeID = False, returnEntryComment = False, returnEntryWithdrawalID = False, returnExcludeFromHonorRoll = False, returnExcludeFromRank = False, returnExcludeFromThirdFridaySeptemberCount = False, returnFailureReason = False, returnFeeManagementCustomerID = False, returnGradeLevelCode = False, returnGradeReferenceID = False, returnGradYear = False, returnGSAADAClaimableOverrideCode = False, returnGSAADAClaimableOverrideCodeDisplayName = False, returnHomeroomCode = False, returnHomeroomID = False, returnIncludeAsProspectiveRank = False, returnIsCurrentActive = False, returnIsDefaultEntityForEntryWithdrawal = False, returnIsDefaultEntityForStudentEntityYear = False, returnIsPermanentExit = False, returnIsPrivateSchoolChoiceStudent = False, returnIsTuitionPaidOutOfDistrict = False, returnModifiedTime = False, returnNumericYear = False, returnOutgoingStudent = False, returnPercentEnrolled = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnScheduledSectionCount = False, returnSchoolCode = False, returnSchoolID = False, returnSchoolYearID = False, returnServingRCDTSOverrideCode = False, returnServingRCDTSOverrideCodeDisplayName = False, returnServingRCDTSOverrideID = False, returnSourceEntryWithdrawalID = False, returnStaffIDAdvisor = False, returnStaffIDDisciplineOfficer = False, returnStartDate = False, returnStateAidCategoryMNID = False, returnStateDistrictMNCodeName = False, returnStateDistrictMNID = False, returnStateLastAttendanceLocationCodeMNID = False, returnStudentCourseRequestNotMoveableCount = False, returnStudentCourseRequestToDeleteCount = False, returnStudentFullName = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnStudentTypeID = False, returnTestingSchoolCode = False, returnTestingSchoolCodeDisplayName = False, returnTestingSchoolRCDTSOverrideCode = False, returnTestingSchoolRCDTSOverrideCodeDisplayName = False, returnTestingSchoolRCDTSOverrideID = False, returnTotalStudentCourseRequestCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCode = False, returnWithdrawalCodeID = False, returnWithdrawalComment = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentRecord/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentEnrollmentRecord(TempStudentEnrollmentRecordID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentEntityYear(EntityID = 1, page = 1, pageSize = 100, returnTempStudentEntityYearID = True, returnAdvisorDetails = False, returnCreatedTime = False, returnCurrentAdvisorDetails = False, returnCurrentHomeroomDetails = False, returnGenderCode = False, returnGradeLevelCodeDescription = False, returnHomeroomDetails = False, returnHomeroomID = False, returnIsActive = False, returnMessage = False, returnModifiedTime = False, returnStaffIDAdvisor = False, returnStudentEntityYearID = False, returnStudentFullName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentEntityYear(TempStudentEntityYearID, EntityID = 1, returnTempStudentEntityYearID = True, returnAdvisorDetails = False, returnCreatedTime = False, returnCurrentAdvisorDetails = False, returnCurrentHomeroomDetails = False, returnGenderCode = False, returnGradeLevelCodeDescription = False, returnHomeroomDetails = False, returnHomeroomID = False, returnIsActive = False, returnMessage = False, returnModifiedTime = False, returnStaffIDAdvisor = False, returnStudentEntityYearID = False, returnStudentFullName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEntityYear/" + str(TempStudentEntityYearID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentEntityYear(TempStudentEntityYearID, EntityID = 1, setAdvisorDetails = None, setCurrentAdvisorDetails = None, setCurrentHomeroomDetails = None, setGenderCode = None, setGradeLevelCodeDescription = None, setHomeroomDetails = None, setHomeroomID = None, setIsActive = None, setMessage = None, setStaffIDAdvisor = None, setStudentEntityYearID = None, setStudentFullName = None, setStudentNumber = None, setRelationships = None, returnTempStudentEntityYearID = True, returnAdvisorDetails = False, returnCreatedTime = False, returnCurrentAdvisorDetails = False, returnCurrentHomeroomDetails = False, returnGenderCode = False, returnGradeLevelCodeDescription = False, returnHomeroomDetails = False, returnHomeroomID = False, returnIsActive = False, returnMessage = False, returnModifiedTime = False, returnStaffIDAdvisor = False, returnStudentEntityYearID = False, returnStudentFullName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEntityYear/" + str(TempStudentEntityYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentEntityYear(EntityID = 1, setAdvisorDetails = None, setCurrentAdvisorDetails = None, setCurrentHomeroomDetails = None, setGenderCode = None, setGradeLevelCodeDescription = None, setHomeroomDetails = None, setHomeroomID = None, setIsActive = None, setMessage = None, setStaffIDAdvisor = None, setStudentEntityYearID = None, setStudentFullName = None, setStudentNumber = None, setRelationships = None, returnTempStudentEntityYearID = True, returnAdvisorDetails = False, returnCreatedTime = False, returnCurrentAdvisorDetails = False, returnCurrentHomeroomDetails = False, returnGenderCode = False, returnGradeLevelCodeDescription = False, returnHomeroomDetails = False, returnHomeroomID = False, returnIsActive = False, returnMessage = False, returnModifiedTime = False, returnStaffIDAdvisor = False, returnStudentEntityYearID = False, returnStudentFullName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEntityYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentEntityYear(TempStudentEntityYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryWithdrawalCode(EntityID = 1, page = 1, pageSize = 100, returnWithdrawalCodeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEdFiExitWithdrawID = False, returnIsCrossEntityCourseEnrollment = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateStatusEndCodeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeIDClonedFrom = False, returnWithdrawalCodeMNID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/WithdrawalCode/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getWithdrawalCode(WithdrawalCodeID, EntityID = 1, returnWithdrawalCodeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEdFiExitWithdrawID = False, returnIsCrossEntityCourseEnrollment = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateStatusEndCodeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeIDClonedFrom = False, returnWithdrawalCodeMNID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/WithdrawalCode/" + str(WithdrawalCodeID), verb = "get", return_params_list = return_params_list)

def modifyWithdrawalCode(WithdrawalCodeID, EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setEdFiExitWithdrawID = None, setIsCrossEntityCourseEnrollment = None, setSchoolYearID = None, setStateStatusEndCodeMNID = None, setType = None, setTypeCode = None, setWithdrawalCodeIDClonedFrom = None, setRelationships = None, returnWithdrawalCodeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEdFiExitWithdrawID = False, returnIsCrossEntityCourseEnrollment = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateStatusEndCodeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeIDClonedFrom = False, returnWithdrawalCodeMNID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/WithdrawalCode/" + str(WithdrawalCodeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createWithdrawalCode(EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setEdFiExitWithdrawID = None, setIsCrossEntityCourseEnrollment = None, setSchoolYearID = None, setStateStatusEndCodeMNID = None, setType = None, setTypeCode = None, setWithdrawalCodeIDClonedFrom = None, setRelationships = None, returnWithdrawalCodeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEdFiExitWithdrawID = False, returnIsCrossEntityCourseEnrollment = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateStatusEndCodeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeIDClonedFrom = False, returnWithdrawalCodeMNID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/WithdrawalCode/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteWithdrawalCode(WithdrawalCodeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")