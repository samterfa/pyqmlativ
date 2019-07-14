# This module contains MessageCenter functions.

from .Utilities import make_request

import pandas as pd

import json

import re

def getEveryConfigDistrictYear(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictYearID = True, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnNumberOfDaysAfterWithdrawalToAllowMessages = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, returnConfigDistrictYearID = True, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnNumberOfDaysAfterWithdrawalToAllowMessages = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "get", return_params_list = return_params_list)

def modifyConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, setConfigDistrictYearIDClonedFrom = None, setDistrictID = None, setNumberOfDaysAfterWithdrawalToAllowMessages = None, setSchoolYearID = None, setRelationships = None, returnConfigDistrictYearID = True, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnNumberOfDaysAfterWithdrawalToAllowMessages = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigDistrictYear(EntityID = 1, setConfigDistrictYearIDClonedFrom = None, setDistrictID = None, setNumberOfDaysAfterWithdrawalToAllowMessages = None, setSchoolYearID = None, setRelationships = None, returnConfigDistrictYearID = True, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnNumberOfDaysAfterWithdrawalToAllowMessages = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigDistrictYear(ConfigDistrictYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigDistrictYearWithdrawalCode(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictYearWithdrawalCodeID = True, returnConfigDistrictYearID = False, returnConfigDistrictYearWithdrawalCodeIDClonedFrom = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYearWithdrawalCode/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigDistrictYearWithdrawalCode(ConfigDistrictYearWithdrawalCodeID, EntityID = 1, returnConfigDistrictYearWithdrawalCodeID = True, returnConfigDistrictYearID = False, returnConfigDistrictYearWithdrawalCodeIDClonedFrom = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYearWithdrawalCode/" + str(ConfigDistrictYearWithdrawalCodeID), verb = "get", return_params_list = return_params_list)

def modifyConfigDistrictYearWithdrawalCode(ConfigDistrictYearWithdrawalCodeID, EntityID = 1, setConfigDistrictYearID = None, setConfigDistrictYearWithdrawalCodeIDClonedFrom = None, setWithdrawalCodeID = None, setRelationships = None, returnConfigDistrictYearWithdrawalCodeID = True, returnConfigDistrictYearID = False, returnConfigDistrictYearWithdrawalCodeIDClonedFrom = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYearWithdrawalCode/" + str(ConfigDistrictYearWithdrawalCodeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigDistrictYearWithdrawalCode(EntityID = 1, setConfigDistrictYearID = None, setConfigDistrictYearWithdrawalCodeIDClonedFrom = None, setWithdrawalCodeID = None, setRelationships = None, returnConfigDistrictYearWithdrawalCodeID = True, returnConfigDistrictYearID = False, returnConfigDistrictYearWithdrawalCodeIDClonedFrom = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYearWithdrawalCode/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigDistrictYearWithdrawalCode(ConfigDistrictYearWithdrawalCodeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryMessage(EntityID = 1, page = 1, pageSize = 100, returnMessageID = True, returnContent = False, returnCreatedTime = False, returnFromInformation = False, returnIncludeLinkToObject = False, returnIsHidden = False, returnIsRead = False, returnMessageIDCopiedFrom = False, returnMessageMasterID = False, returnModifiedTime = False, returnNoSourceIDRequired = False, returnObjectIDCreatedFor = False, returnObjectPrimaryKey = False, returnPostDate = False, returnPriorityType = False, returnPriorityTypeCode = False, returnSourceIDCreatedFor = False, returnSubject = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRecipient = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Message/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getMessage(MessageID, EntityID = 1, returnMessageID = True, returnContent = False, returnCreatedTime = False, returnFromInformation = False, returnIncludeLinkToObject = False, returnIsHidden = False, returnIsRead = False, returnMessageIDCopiedFrom = False, returnMessageMasterID = False, returnModifiedTime = False, returnNoSourceIDRequired = False, returnObjectIDCreatedFor = False, returnObjectPrimaryKey = False, returnPostDate = False, returnPriorityType = False, returnPriorityTypeCode = False, returnSourceIDCreatedFor = False, returnSubject = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRecipient = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Message/" + str(MessageID), verb = "get", return_params_list = return_params_list)

def modifyMessage(MessageID, EntityID = 1, setContent = None, setFromInformation = None, setIsHidden = None, setIsRead = None, setMessageIDCopiedFrom = None, setMessageMasterID = None, setNoSourceIDRequired = None, setObjectIDCreatedFor = None, setObjectPrimaryKey = None, setPostDate = None, setPriorityType = None, setPriorityTypeCode = None, setSourceIDCreatedFor = None, setSubject = None, setType = None, setTypeCode = None, setUserIDRecipient = None, setRelationships = None, returnMessageID = True, returnContent = False, returnCreatedTime = False, returnFromInformation = False, returnIncludeLinkToObject = False, returnIsHidden = False, returnIsRead = False, returnMessageIDCopiedFrom = False, returnMessageMasterID = False, returnModifiedTime = False, returnNoSourceIDRequired = False, returnObjectIDCreatedFor = False, returnObjectPrimaryKey = False, returnPostDate = False, returnPriorityType = False, returnPriorityTypeCode = False, returnSourceIDCreatedFor = False, returnSubject = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRecipient = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Message/" + str(MessageID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createMessage(EntityID = 1, setContent = None, setFromInformation = None, setIsHidden = None, setIsRead = None, setMessageIDCopiedFrom = None, setMessageMasterID = None, setNoSourceIDRequired = None, setObjectIDCreatedFor = None, setObjectPrimaryKey = None, setPostDate = None, setPriorityType = None, setPriorityTypeCode = None, setSourceIDCreatedFor = None, setSubject = None, setType = None, setTypeCode = None, setUserIDRecipient = None, setRelationships = None, returnMessageID = True, returnContent = False, returnCreatedTime = False, returnFromInformation = False, returnIncludeLinkToObject = False, returnIsHidden = False, returnIsRead = False, returnMessageIDCopiedFrom = False, returnMessageMasterID = False, returnModifiedTime = False, returnNoSourceIDRequired = False, returnObjectIDCreatedFor = False, returnObjectPrimaryKey = False, returnPostDate = False, returnPriorityType = False, returnPriorityTypeCode = False, returnSourceIDCreatedFor = False, returnSubject = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRecipient = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Message/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteMessage(MessageID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryMessageMaster(EntityID = 1, page = 1, pageSize = 100, returnMessageMasterID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCarbonCopyStaffIDList = False, returnContent = False, returnCreatedTime = False, returnCustomMessageData = False, returnEntityID = False, returnIncludeRestrictedGuardians = False, returnIsDraft = False, returnIsRetracted = False, returnLargestMessagePrimaryKey = False, returnModifiedTime = False, returnObjectIDCreatedFor = False, returnPostedTime = False, returnPriorityType = False, returnPriorityTypeCode = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnSourceIDCreatedFor = False, returnStatus = False, returnStatusCode = False, returnSubject = False, returnSubjectCleaned = False, returnToWhom = False, returnToWhomCode = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLFilter = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/MessageMaster/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getMessageMaster(MessageMasterID, EntityID = 1, returnMessageMasterID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCarbonCopyStaffIDList = False, returnContent = False, returnCreatedTime = False, returnCustomMessageData = False, returnEntityID = False, returnIncludeRestrictedGuardians = False, returnIsDraft = False, returnIsRetracted = False, returnLargestMessagePrimaryKey = False, returnModifiedTime = False, returnObjectIDCreatedFor = False, returnPostedTime = False, returnPriorityType = False, returnPriorityTypeCode = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnSourceIDCreatedFor = False, returnStatus = False, returnStatusCode = False, returnSubject = False, returnSubjectCleaned = False, returnToWhom = False, returnToWhomCode = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLFilter = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/MessageMaster/" + str(MessageMasterID), verb = "get", return_params_list = return_params_list)

def modifyMessageMaster(MessageMasterID, EntityID = 1, setCarbonCopyStaffIDList = None, setContent = None, setCustomMessageData = None, setEntityID = None, setIncludeRestrictedGuardians = None, setIsDraft = None, setObjectIDCreatedFor = None, setPostedTime = None, setPriorityType = None, setPriorityTypeCode = None, setSchoolYearID = None, setSearchConditionFilter = None, setSourceIDCreatedFor = None, setStatus = None, setStatusCode = None, setSubject = None, setToWhom = None, setToWhomCode = None, setType = None, setTypeCode = None, setXMLFilter = None, setRelationships = None, returnMessageMasterID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCarbonCopyStaffIDList = False, returnContent = False, returnCreatedTime = False, returnCustomMessageData = False, returnEntityID = False, returnIncludeRestrictedGuardians = False, returnIsDraft = False, returnIsRetracted = False, returnLargestMessagePrimaryKey = False, returnModifiedTime = False, returnObjectIDCreatedFor = False, returnPostedTime = False, returnPriorityType = False, returnPriorityTypeCode = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnSourceIDCreatedFor = False, returnStatus = False, returnStatusCode = False, returnSubject = False, returnSubjectCleaned = False, returnToWhom = False, returnToWhomCode = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLFilter = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/MessageMaster/" + str(MessageMasterID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createMessageMaster(EntityID = 1, setCarbonCopyStaffIDList = None, setContent = None, setCustomMessageData = None, setEntityID = None, setIncludeRestrictedGuardians = None, setIsDraft = None, setObjectIDCreatedFor = None, setPostedTime = None, setPriorityType = None, setPriorityTypeCode = None, setSchoolYearID = None, setSearchConditionFilter = None, setSourceIDCreatedFor = None, setStatus = None, setStatusCode = None, setSubject = None, setToWhom = None, setToWhomCode = None, setType = None, setTypeCode = None, setXMLFilter = None, setRelationships = None, returnMessageMasterID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCarbonCopyStaffIDList = False, returnContent = False, returnCreatedTime = False, returnCustomMessageData = False, returnEntityID = False, returnIncludeRestrictedGuardians = False, returnIsDraft = False, returnIsRetracted = False, returnLargestMessagePrimaryKey = False, returnModifiedTime = False, returnObjectIDCreatedFor = False, returnPostedTime = False, returnPriorityType = False, returnPriorityTypeCode = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnSourceIDCreatedFor = False, returnStatus = False, returnStatusCode = False, returnSubject = False, returnSubjectCleaned = False, returnToWhom = False, returnToWhomCode = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLFilter = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/MessageMaster/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteMessageMaster(MessageMasterID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNotification(EntityID = 1, page = 1, pageSize = 100, returnNotificationID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnAttendanceCategoryForCount = False, returnAttendanceCategoryForCountCode = False, returnAttendanceCountHigh = False, returnAttendanceCountLow = False, returnAttendanceCountMethod = False, returnAttendanceCountMethodCode = False, returnConsiderAllStaffMeets = False, returnCreatedTime = False, returnDayType = False, returnDayTypeCode = False, returnEntityID = False, returnFeeManagementBalanceHigh = False, returnFeeManagementBalanceLow = False, returnFoodServiceBalanceHigh = False, returnFoodServiceBalanceLow = False, returnGradingPeriodEndDaysAfter = False, returnGradingPeriodEndDaysBefore = False, returnIncludeAutoGeneratedMessage = False, returnLastEntryType = False, returnLastEntryTypeCode = False, returnMessage = False, returnModifiedTime = False, returnNumberOfDays = False, returnPriorityType = False, returnPriorityTypeCode = False, returnScheduledTaskID = False, returnScheduleIsAvailableDaysBefore = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnSendNotificationForDay = False, returnSendNotificationForDayCode = False, returnSendNotificationForPriorDayCount = False, returnSendOnlyIfGuardianNotNotified = False, returnSendToDisciplineOfficer = False, returnSubject = False, returnSubjectCleaned = False, returnToWhom = False, returnToWhomCode = False, returnType = False, returnTypeCode = False, returnUnrecordedAttendanceMinutes = False, returnUnrecordedAttendancePeriodType = False, returnUnrecordedAttendancePeriodTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLFilter = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Notification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNotification(NotificationID, EntityID = 1, returnNotificationID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnAttendanceCategoryForCount = False, returnAttendanceCategoryForCountCode = False, returnAttendanceCountHigh = False, returnAttendanceCountLow = False, returnAttendanceCountMethod = False, returnAttendanceCountMethodCode = False, returnConsiderAllStaffMeets = False, returnCreatedTime = False, returnDayType = False, returnDayTypeCode = False, returnEntityID = False, returnFeeManagementBalanceHigh = False, returnFeeManagementBalanceLow = False, returnFoodServiceBalanceHigh = False, returnFoodServiceBalanceLow = False, returnGradingPeriodEndDaysAfter = False, returnGradingPeriodEndDaysBefore = False, returnIncludeAutoGeneratedMessage = False, returnLastEntryType = False, returnLastEntryTypeCode = False, returnMessage = False, returnModifiedTime = False, returnNumberOfDays = False, returnPriorityType = False, returnPriorityTypeCode = False, returnScheduledTaskID = False, returnScheduleIsAvailableDaysBefore = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnSendNotificationForDay = False, returnSendNotificationForDayCode = False, returnSendNotificationForPriorDayCount = False, returnSendOnlyIfGuardianNotNotified = False, returnSendToDisciplineOfficer = False, returnSubject = False, returnSubjectCleaned = False, returnToWhom = False, returnToWhomCode = False, returnType = False, returnTypeCode = False, returnUnrecordedAttendanceMinutes = False, returnUnrecordedAttendancePeriodType = False, returnUnrecordedAttendancePeriodTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLFilter = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Notification/" + str(NotificationID), verb = "get", return_params_list = return_params_list)

def modifyNotification(NotificationID, EntityID = 1, setAttendanceCategoryForCount = None, setAttendanceCategoryForCountCode = None, setAttendanceCountHigh = None, setAttendanceCountLow = None, setAttendanceCountMethod = None, setAttendanceCountMethodCode = None, setConsiderAllStaffMeets = None, setDayType = None, setDayTypeCode = None, setEntityID = None, setFeeManagementBalanceHigh = None, setFeeManagementBalanceLow = None, setFoodServiceBalanceHigh = None, setFoodServiceBalanceLow = None, setGradingPeriodEndDaysAfter = None, setGradingPeriodEndDaysBefore = None, setIncludeAutoGeneratedMessage = None, setLastEntryType = None, setLastEntryTypeCode = None, setMessage = None, setNumberOfDays = None, setPriorityType = None, setPriorityTypeCode = None, setScheduledTaskID = None, setScheduleIsAvailableDaysBefore = None, setSchoolYearID = None, setSearchConditionFilter = None, setSendNotificationForDay = None, setSendNotificationForDayCode = None, setSendNotificationForPriorDayCount = None, setSendOnlyIfGuardianNotNotified = None, setSendToDisciplineOfficer = None, setSubject = None, setToWhom = None, setToWhomCode = None, setType = None, setTypeCode = None, setUnrecordedAttendanceMinutes = None, setUnrecordedAttendancePeriodType = None, setUnrecordedAttendancePeriodTypeCode = None, setXMLFilter = None, setRelationships = None, returnNotificationID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnAttendanceCategoryForCount = False, returnAttendanceCategoryForCountCode = False, returnAttendanceCountHigh = False, returnAttendanceCountLow = False, returnAttendanceCountMethod = False, returnAttendanceCountMethodCode = False, returnConsiderAllStaffMeets = False, returnCreatedTime = False, returnDayType = False, returnDayTypeCode = False, returnEntityID = False, returnFeeManagementBalanceHigh = False, returnFeeManagementBalanceLow = False, returnFoodServiceBalanceHigh = False, returnFoodServiceBalanceLow = False, returnGradingPeriodEndDaysAfter = False, returnGradingPeriodEndDaysBefore = False, returnIncludeAutoGeneratedMessage = False, returnLastEntryType = False, returnLastEntryTypeCode = False, returnMessage = False, returnModifiedTime = False, returnNumberOfDays = False, returnPriorityType = False, returnPriorityTypeCode = False, returnScheduledTaskID = False, returnScheduleIsAvailableDaysBefore = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnSendNotificationForDay = False, returnSendNotificationForDayCode = False, returnSendNotificationForPriorDayCount = False, returnSendOnlyIfGuardianNotNotified = False, returnSendToDisciplineOfficer = False, returnSubject = False, returnSubjectCleaned = False, returnToWhom = False, returnToWhomCode = False, returnType = False, returnTypeCode = False, returnUnrecordedAttendanceMinutes = False, returnUnrecordedAttendancePeriodType = False, returnUnrecordedAttendancePeriodTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLFilter = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Notification/" + str(NotificationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNotification(EntityID = 1, setAttendanceCategoryForCount = None, setAttendanceCategoryForCountCode = None, setAttendanceCountHigh = None, setAttendanceCountLow = None, setAttendanceCountMethod = None, setAttendanceCountMethodCode = None, setConsiderAllStaffMeets = None, setDayType = None, setDayTypeCode = None, setEntityID = None, setFeeManagementBalanceHigh = None, setFeeManagementBalanceLow = None, setFoodServiceBalanceHigh = None, setFoodServiceBalanceLow = None, setGradingPeriodEndDaysAfter = None, setGradingPeriodEndDaysBefore = None, setIncludeAutoGeneratedMessage = None, setLastEntryType = None, setLastEntryTypeCode = None, setMessage = None, setNumberOfDays = None, setPriorityType = None, setPriorityTypeCode = None, setScheduledTaskID = None, setScheduleIsAvailableDaysBefore = None, setSchoolYearID = None, setSearchConditionFilter = None, setSendNotificationForDay = None, setSendNotificationForDayCode = None, setSendNotificationForPriorDayCount = None, setSendOnlyIfGuardianNotNotified = None, setSendToDisciplineOfficer = None, setSubject = None, setToWhom = None, setToWhomCode = None, setType = None, setTypeCode = None, setUnrecordedAttendanceMinutes = None, setUnrecordedAttendancePeriodType = None, setUnrecordedAttendancePeriodTypeCode = None, setXMLFilter = None, setRelationships = None, returnNotificationID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnAttendanceCategoryForCount = False, returnAttendanceCategoryForCountCode = False, returnAttendanceCountHigh = False, returnAttendanceCountLow = False, returnAttendanceCountMethod = False, returnAttendanceCountMethodCode = False, returnConsiderAllStaffMeets = False, returnCreatedTime = False, returnDayType = False, returnDayTypeCode = False, returnEntityID = False, returnFeeManagementBalanceHigh = False, returnFeeManagementBalanceLow = False, returnFoodServiceBalanceHigh = False, returnFoodServiceBalanceLow = False, returnGradingPeriodEndDaysAfter = False, returnGradingPeriodEndDaysBefore = False, returnIncludeAutoGeneratedMessage = False, returnLastEntryType = False, returnLastEntryTypeCode = False, returnMessage = False, returnModifiedTime = False, returnNumberOfDays = False, returnPriorityType = False, returnPriorityTypeCode = False, returnScheduledTaskID = False, returnScheduleIsAvailableDaysBefore = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnSendNotificationForDay = False, returnSendNotificationForDayCode = False, returnSendNotificationForPriorDayCount = False, returnSendOnlyIfGuardianNotNotified = False, returnSendToDisciplineOfficer = False, returnSubject = False, returnSubjectCleaned = False, returnToWhom = False, returnToWhomCode = False, returnType = False, returnTypeCode = False, returnUnrecordedAttendanceMinutes = False, returnUnrecordedAttendancePeriodType = False, returnUnrecordedAttendancePeriodTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLFilter = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Notification/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNotification(NotificationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNotificationAction(EntityID = 1, page = 1, pageSize = 100, returnNotificationActionID = True, returnActionID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNotificationAction(NotificationActionID, EntityID = 1, returnNotificationActionID = True, returnActionID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAction/" + str(NotificationActionID), verb = "get", return_params_list = return_params_list)

def modifyNotificationAction(NotificationActionID, EntityID = 1, setActionID = None, setNotificationID = None, setRelationships = None, returnNotificationActionID = True, returnActionID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAction/" + str(NotificationActionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNotificationAction(EntityID = 1, setActionID = None, setNotificationID = None, setRelationships = None, returnNotificationActionID = True, returnActionID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAction/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNotificationAction(NotificationActionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNotificationAttendanceType(EntityID = 1, page = 1, pageSize = 100, returnNotificationAttendanceTypeID = True, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAttendanceType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNotificationAttendanceType(NotificationAttendanceTypeID, EntityID = 1, returnNotificationAttendanceTypeID = True, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAttendanceType/" + str(NotificationAttendanceTypeID), verb = "get", return_params_list = return_params_list)

def modifyNotificationAttendanceType(NotificationAttendanceTypeID, EntityID = 1, setAttendanceTypeID = None, setNotificationID = None, setRelationships = None, returnNotificationAttendanceTypeID = True, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAttendanceType/" + str(NotificationAttendanceTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNotificationAttendanceType(EntityID = 1, setAttendanceTypeID = None, setNotificationID = None, setRelationships = None, returnNotificationAttendanceTypeID = True, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAttendanceType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNotificationAttendanceType(NotificationAttendanceTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNotificationCarbonCopyStaff(EntityID = 1, page = 1, pageSize = 100, returnNotificationCarbonCopyStaffID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationCarbonCopyStaff/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNotificationCarbonCopyStaff(NotificationCarbonCopyStaffID, EntityID = 1, returnNotificationCarbonCopyStaffID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationCarbonCopyStaff/" + str(NotificationCarbonCopyStaffID), verb = "get", return_params_list = return_params_list)

def modifyNotificationCarbonCopyStaff(NotificationCarbonCopyStaffID, EntityID = 1, setNotificationID = None, setStaffID = None, setRelationships = None, returnNotificationCarbonCopyStaffID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationCarbonCopyStaff/" + str(NotificationCarbonCopyStaffID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNotificationCarbonCopyStaff(EntityID = 1, setNotificationID = None, setStaffID = None, setRelationships = None, returnNotificationCarbonCopyStaffID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationCarbonCopyStaff/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNotificationCarbonCopyStaff(NotificationCarbonCopyStaffID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNotificationDisciplineThreshold(EntityID = 1, page = 1, pageSize = 100, returnNotificationDisciplineThresholdID = True, returnCreatedTime = False, returnDisciplineThresholdID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationDisciplineThreshold/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNotificationDisciplineThreshold(NotificationDisciplineThresholdID, EntityID = 1, returnNotificationDisciplineThresholdID = True, returnCreatedTime = False, returnDisciplineThresholdID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationDisciplineThreshold/" + str(NotificationDisciplineThresholdID), verb = "get", return_params_list = return_params_list)

def modifyNotificationDisciplineThreshold(NotificationDisciplineThresholdID, EntityID = 1, setDisciplineThresholdID = None, setNotificationID = None, setRelationships = None, returnNotificationDisciplineThresholdID = True, returnCreatedTime = False, returnDisciplineThresholdID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationDisciplineThreshold/" + str(NotificationDisciplineThresholdID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNotificationDisciplineThreshold(EntityID = 1, setDisciplineThresholdID = None, setNotificationID = None, setRelationships = None, returnNotificationDisciplineThresholdID = True, returnCreatedTime = False, returnDisciplineThresholdID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationDisciplineThreshold/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNotificationDisciplineThreshold(NotificationDisciplineThresholdID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNotificationGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnNotificationGradeBucketID = True, returnCreatedTime = False, returnGradeBucketID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNotificationGradeBucket(NotificationGradeBucketID, EntityID = 1, returnNotificationGradeBucketID = True, returnCreatedTime = False, returnGradeBucketID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeBucket/" + str(NotificationGradeBucketID), verb = "get", return_params_list = return_params_list)

def modifyNotificationGradeBucket(NotificationGradeBucketID, EntityID = 1, setGradeBucketID = None, setNotificationID = None, setRelationships = None, returnNotificationGradeBucketID = True, returnCreatedTime = False, returnGradeBucketID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeBucket/" + str(NotificationGradeBucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNotificationGradeBucket(EntityID = 1, setGradeBucketID = None, setNotificationID = None, setRelationships = None, returnNotificationGradeBucketID = True, returnCreatedTime = False, returnGradeBucketID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeBucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNotificationGradeBucket(NotificationGradeBucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNotificationGradeMark(EntityID = 1, page = 1, pageSize = 100, returnNotificationGradeMarkID = True, returnCreatedTime = False, returnGradeMarkID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeMark/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNotificationGradeMark(NotificationGradeMarkID, EntityID = 1, returnNotificationGradeMarkID = True, returnCreatedTime = False, returnGradeMarkID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeMark/" + str(NotificationGradeMarkID), verb = "get", return_params_list = return_params_list)

def modifyNotificationGradeMark(NotificationGradeMarkID, EntityID = 1, setGradeMarkID = None, setNotificationID = None, setRelationships = None, returnNotificationGradeMarkID = True, returnCreatedTime = False, returnGradeMarkID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeMark/" + str(NotificationGradeMarkID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNotificationGradeMark(EntityID = 1, setGradeMarkID = None, setNotificationID = None, setRelationships = None, returnNotificationGradeMarkID = True, returnCreatedTime = False, returnGradeMarkID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeMark/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNotificationGradeMark(NotificationGradeMarkID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNotificationGradeReference(EntityID = 1, page = 1, pageSize = 100, returnNotificationGradeReferenceID = True, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeReference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNotificationGradeReference(NotificationGradeReferenceID, EntityID = 1, returnNotificationGradeReferenceID = True, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeReference/" + str(NotificationGradeReferenceID), verb = "get", return_params_list = return_params_list)

def modifyNotificationGradeReference(NotificationGradeReferenceID, EntityID = 1, setGradeReferenceID = None, setNotificationID = None, setRelationships = None, returnNotificationGradeReferenceID = True, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeReference/" + str(NotificationGradeReferenceID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNotificationGradeReference(EntityID = 1, setGradeReferenceID = None, setNotificationID = None, setRelationships = None, returnNotificationGradeReferenceID = True, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeReference/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNotificationGradeReference(NotificationGradeReferenceID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNotificationOffense(EntityID = 1, page = 1, pageSize = 100, returnNotificationOffenseID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOffense/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNotificationOffense(NotificationOffenseID, EntityID = 1, returnNotificationOffenseID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOffense/" + str(NotificationOffenseID), verb = "get", return_params_list = return_params_list)

def modifyNotificationOffense(NotificationOffenseID, EntityID = 1, setNotificationID = None, setOffenseID = None, setRelationships = None, returnNotificationOffenseID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOffense/" + str(NotificationOffenseID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNotificationOffense(EntityID = 1, setNotificationID = None, setOffenseID = None, setRelationships = None, returnNotificationOffenseID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOffense/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNotificationOffense(NotificationOffenseID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNotificationOnlineForm(EntityID = 1, page = 1, pageSize = 100, returnNotificationOnlineFormID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOnlineForm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNotificationOnlineForm(NotificationOnlineFormID, EntityID = 1, returnNotificationOnlineFormID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOnlineForm/" + str(NotificationOnlineFormID), verb = "get", return_params_list = return_params_list)

def modifyNotificationOnlineForm(NotificationOnlineFormID, EntityID = 1, setNotificationID = None, setOnlineFormID = None, setRelationships = None, returnNotificationOnlineFormID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOnlineForm/" + str(NotificationOnlineFormID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNotificationOnlineForm(EntityID = 1, setNotificationID = None, setOnlineFormID = None, setRelationships = None, returnNotificationOnlineFormID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOnlineForm/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNotificationOnlineForm(NotificationOnlineFormID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNotificationScheduleIsAvailableSectionLength(EntityID = 1, page = 1, pageSize = 100, returnNotificationScheduleIsAvailableSectionLengthID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationScheduleIsAvailableSectionLength/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNotificationScheduleIsAvailableSectionLength(NotificationScheduleIsAvailableSectionLengthID, EntityID = 1, returnNotificationScheduleIsAvailableSectionLengthID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationScheduleIsAvailableSectionLength/" + str(NotificationScheduleIsAvailableSectionLengthID), verb = "get", return_params_list = return_params_list)

def modifyNotificationScheduleIsAvailableSectionLength(NotificationScheduleIsAvailableSectionLengthID, EntityID = 1, setNotificationID = None, setSectionLengthID = None, setRelationships = None, returnNotificationScheduleIsAvailableSectionLengthID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationScheduleIsAvailableSectionLength/" + str(NotificationScheduleIsAvailableSectionLengthID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNotificationScheduleIsAvailableSectionLength(EntityID = 1, setNotificationID = None, setSectionLengthID = None, setRelationships = None, returnNotificationScheduleIsAvailableSectionLengthID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationScheduleIsAvailableSectionLength/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNotificationScheduleIsAvailableSectionLength(NotificationScheduleIsAvailableSectionLengthID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNotificationUnrecordedClassAttendance(EntityID = 1, page = 1, pageSize = 100, returnNotificationUnrecordedClassAttendanceID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationUnrecordedClassAttendance/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNotificationUnrecordedClassAttendance(NotificationUnrecordedClassAttendanceID, EntityID = 1, returnNotificationUnrecordedClassAttendanceID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationUnrecordedClassAttendance/" + str(NotificationUnrecordedClassAttendanceID), verb = "get", return_params_list = return_params_list)

def modifyNotificationUnrecordedClassAttendance(NotificationUnrecordedClassAttendanceID, EntityID = 1, setDisplayPeriodID = None, setNotificationID = None, setRelationships = None, returnNotificationUnrecordedClassAttendanceID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationUnrecordedClassAttendance/" + str(NotificationUnrecordedClassAttendanceID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNotificationUnrecordedClassAttendance(EntityID = 1, setDisplayPeriodID = None, setNotificationID = None, setRelationships = None, returnNotificationUnrecordedClassAttendanceID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationUnrecordedClassAttendance/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNotificationUnrecordedClassAttendance(NotificationUnrecordedClassAttendanceID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNotificationWithdrawalCode(EntityID = 1, page = 1, pageSize = 100, returnNotificationWithdrawalCodeID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationWithdrawalCode/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNotificationWithdrawalCode(NotificationWithdrawalCodeID, EntityID = 1, returnNotificationWithdrawalCodeID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationWithdrawalCode/" + str(NotificationWithdrawalCodeID), verb = "get", return_params_list = return_params_list)

def modifyNotificationWithdrawalCode(NotificationWithdrawalCodeID, EntityID = 1, setNotificationID = None, setWithdrawalCodeID = None, setRelationships = None, returnNotificationWithdrawalCodeID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationWithdrawalCode/" + str(NotificationWithdrawalCodeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNotificationWithdrawalCode(EntityID = 1, setNotificationID = None, setWithdrawalCodeID = None, setRelationships = None, returnNotificationWithdrawalCodeID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationWithdrawalCode/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNotificationWithdrawalCode(NotificationWithdrawalCodeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryQueuedCompletedCareerPlanChangeNotification(EntityID = 1, page = 1, pageSize = 100, returnQueuedCompletedCareerPlanChangeNotificationID = True, returnCareerPlanGradeLevelIDCurrent = False, returnCareerPlanGradeLevelIDPrevious = False, returnCreatedTime = False, returnCreditsCurrent = False, returnCreditsPrevious = False, returnCurriculumID = False, returnEntityID = False, returnIsDeletedRecord = False, returnIsNewRecord = False, returnIsSent = False, returnIsStudentPermittedToChangeGradeLevelCurrent = False, returnIsStudentPermittedToChangeGradeLevelPrevious = False, returnIsStudentPermittedToDeleteCurrent = False, returnIsStudentPermittedToDeletePrevious = False, returnModifiedTime = False, returnNotificationID = False, returnSchoolYearID = False, returnStudentCareerPlanID = False, returnStudentCourseRequestIDCurrent = False, returnStudentCourseRequestIDPrevious = False, returnStudentID = False, returnStudentSubAreaIDCurrent = False, returnStudentSubAreaIDPrevious = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedCareerPlanChangeNotification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getQueuedCompletedCareerPlanChangeNotification(QueuedCompletedCareerPlanChangeNotificationID, EntityID = 1, returnQueuedCompletedCareerPlanChangeNotificationID = True, returnCareerPlanGradeLevelIDCurrent = False, returnCareerPlanGradeLevelIDPrevious = False, returnCreatedTime = False, returnCreditsCurrent = False, returnCreditsPrevious = False, returnCurriculumID = False, returnEntityID = False, returnIsDeletedRecord = False, returnIsNewRecord = False, returnIsSent = False, returnIsStudentPermittedToChangeGradeLevelCurrent = False, returnIsStudentPermittedToChangeGradeLevelPrevious = False, returnIsStudentPermittedToDeleteCurrent = False, returnIsStudentPermittedToDeletePrevious = False, returnModifiedTime = False, returnNotificationID = False, returnSchoolYearID = False, returnStudentCareerPlanID = False, returnStudentCourseRequestIDCurrent = False, returnStudentCourseRequestIDPrevious = False, returnStudentID = False, returnStudentSubAreaIDCurrent = False, returnStudentSubAreaIDPrevious = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedCareerPlanChangeNotification/" + str(QueuedCompletedCareerPlanChangeNotificationID), verb = "get", return_params_list = return_params_list)

def modifyQueuedCompletedCareerPlanChangeNotification(QueuedCompletedCareerPlanChangeNotificationID, EntityID = 1, setCareerPlanGradeLevelIDCurrent = None, setCareerPlanGradeLevelIDPrevious = None, setCreditsCurrent = None, setCreditsPrevious = None, setCurriculumID = None, setEntityID = None, setIsDeletedRecord = None, setIsNewRecord = None, setIsSent = None, setIsStudentPermittedToChangeGradeLevelCurrent = None, setIsStudentPermittedToChangeGradeLevelPrevious = None, setIsStudentPermittedToDeleteCurrent = None, setIsStudentPermittedToDeletePrevious = None, setNotificationID = None, setSchoolYearID = None, setStudentCareerPlanID = None, setStudentCourseRequestIDCurrent = None, setStudentCourseRequestIDPrevious = None, setStudentID = None, setStudentSubAreaIDCurrent = None, setStudentSubAreaIDPrevious = None, setRelationships = None, returnQueuedCompletedCareerPlanChangeNotificationID = True, returnCareerPlanGradeLevelIDCurrent = False, returnCareerPlanGradeLevelIDPrevious = False, returnCreatedTime = False, returnCreditsCurrent = False, returnCreditsPrevious = False, returnCurriculumID = False, returnEntityID = False, returnIsDeletedRecord = False, returnIsNewRecord = False, returnIsSent = False, returnIsStudentPermittedToChangeGradeLevelCurrent = False, returnIsStudentPermittedToChangeGradeLevelPrevious = False, returnIsStudentPermittedToDeleteCurrent = False, returnIsStudentPermittedToDeletePrevious = False, returnModifiedTime = False, returnNotificationID = False, returnSchoolYearID = False, returnStudentCareerPlanID = False, returnStudentCourseRequestIDCurrent = False, returnStudentCourseRequestIDPrevious = False, returnStudentID = False, returnStudentSubAreaIDCurrent = False, returnStudentSubAreaIDPrevious = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedCareerPlanChangeNotification/" + str(QueuedCompletedCareerPlanChangeNotificationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createQueuedCompletedCareerPlanChangeNotification(EntityID = 1, setCareerPlanGradeLevelIDCurrent = None, setCareerPlanGradeLevelIDPrevious = None, setCreditsCurrent = None, setCreditsPrevious = None, setCurriculumID = None, setEntityID = None, setIsDeletedRecord = None, setIsNewRecord = None, setIsSent = None, setIsStudentPermittedToChangeGradeLevelCurrent = None, setIsStudentPermittedToChangeGradeLevelPrevious = None, setIsStudentPermittedToDeleteCurrent = None, setIsStudentPermittedToDeletePrevious = None, setNotificationID = None, setSchoolYearID = None, setStudentCareerPlanID = None, setStudentCourseRequestIDCurrent = None, setStudentCourseRequestIDPrevious = None, setStudentID = None, setStudentSubAreaIDCurrent = None, setStudentSubAreaIDPrevious = None, setRelationships = None, returnQueuedCompletedCareerPlanChangeNotificationID = True, returnCareerPlanGradeLevelIDCurrent = False, returnCareerPlanGradeLevelIDPrevious = False, returnCreatedTime = False, returnCreditsCurrent = False, returnCreditsPrevious = False, returnCurriculumID = False, returnEntityID = False, returnIsDeletedRecord = False, returnIsNewRecord = False, returnIsSent = False, returnIsStudentPermittedToChangeGradeLevelCurrent = False, returnIsStudentPermittedToChangeGradeLevelPrevious = False, returnIsStudentPermittedToDeleteCurrent = False, returnIsStudentPermittedToDeletePrevious = False, returnModifiedTime = False, returnNotificationID = False, returnSchoolYearID = False, returnStudentCareerPlanID = False, returnStudentCourseRequestIDCurrent = False, returnStudentCourseRequestIDPrevious = False, returnStudentID = False, returnStudentSubAreaIDCurrent = False, returnStudentSubAreaIDPrevious = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedCareerPlanChangeNotification/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteQueuedCompletedCareerPlanChangeNotification(QueuedCompletedCareerPlanChangeNotificationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryQueuedCompletedGradeChangeNotification(EntityID = 1, page = 1, pageSize = 100, returnQueuedCompletedGradeChangeNotificationID = True, returnCreatedTime = False, returnEntityID = False, returnGradeMarkIDCurrent = False, returnGradeMarkIDPrevious = False, returnIsSent = False, returnModifiedTime = False, returnNotificationID = False, returnSchoolYearID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedGradeChangeNotification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getQueuedCompletedGradeChangeNotification(QueuedCompletedGradeChangeNotificationID, EntityID = 1, returnQueuedCompletedGradeChangeNotificationID = True, returnCreatedTime = False, returnEntityID = False, returnGradeMarkIDCurrent = False, returnGradeMarkIDPrevious = False, returnIsSent = False, returnModifiedTime = False, returnNotificationID = False, returnSchoolYearID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedGradeChangeNotification/" + str(QueuedCompletedGradeChangeNotificationID), verb = "get", return_params_list = return_params_list)

def modifyQueuedCompletedGradeChangeNotification(QueuedCompletedGradeChangeNotificationID, EntityID = 1, setEntityID = None, setGradeMarkIDCurrent = None, setGradeMarkIDPrevious = None, setIsSent = None, setNotificationID = None, setSchoolYearID = None, setStudentGradeBucketID = None, setRelationships = None, returnQueuedCompletedGradeChangeNotificationID = True, returnCreatedTime = False, returnEntityID = False, returnGradeMarkIDCurrent = False, returnGradeMarkIDPrevious = False, returnIsSent = False, returnModifiedTime = False, returnNotificationID = False, returnSchoolYearID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedGradeChangeNotification/" + str(QueuedCompletedGradeChangeNotificationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createQueuedCompletedGradeChangeNotification(EntityID = 1, setEntityID = None, setGradeMarkIDCurrent = None, setGradeMarkIDPrevious = None, setIsSent = None, setNotificationID = None, setSchoolYearID = None, setStudentGradeBucketID = None, setRelationships = None, returnQueuedCompletedGradeChangeNotificationID = True, returnCreatedTime = False, returnEntityID = False, returnGradeMarkIDCurrent = False, returnGradeMarkIDPrevious = False, returnIsSent = False, returnModifiedTime = False, returnNotificationID = False, returnSchoolYearID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedGradeChangeNotification/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteQueuedCompletedGradeChangeNotification(QueuedCompletedGradeChangeNotificationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempMessage(EntityID = 1, page = 1, pageSize = 100, returnTempMessageID = True, returnCreatedTime = False, returnModifiedTime = False, returnRecipientName = False, returnRelationship = False, returnSectionInfo = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/TempMessage/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempMessage(TempMessageID, EntityID = 1, returnTempMessageID = True, returnCreatedTime = False, returnModifiedTime = False, returnRecipientName = False, returnRelationship = False, returnSectionInfo = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/TempMessage/" + str(TempMessageID), verb = "get", return_params_list = return_params_list)

def modifyTempMessage(TempMessageID, EntityID = 1, setRecipientName = None, setRelationship = None, setSectionInfo = None, setStudentName = None, setRelationships = None, returnTempMessageID = True, returnCreatedTime = False, returnModifiedTime = False, returnRecipientName = False, returnRelationship = False, returnSectionInfo = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/TempMessage/" + str(TempMessageID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempMessage(EntityID = 1, setRecipientName = None, setRelationship = None, setSectionInfo = None, setStudentName = None, setRelationships = None, returnTempMessageID = True, returnCreatedTime = False, returnModifiedTime = False, returnRecipientName = False, returnRelationship = False, returnSectionInfo = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/TempMessage/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempMessage(TempMessageID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryUserMessageSetting(EntityID = 1, page = 1, pageSize = 100, returnUserMessageSettingID = True, returnAssignmentScoreHighNotification = False, returnAssignmentScoreHighNotificationEmail = False, returnAssignmentScoreLowNotification = False, returnAssignmentScoreLowNotificationEmail = False, returnCopyAttendanceMessagesToEmail = False, returnCopyDisciplineMessagesToEmail = False, returnCopyEnrollmentMessagesToEmail = False, returnCopyFeeManagementMessagesToEmail = False, returnCopyFoodServiceMessagesToEmail = False, returnCopyGradebookMessagesToEmail = False, returnCopyGradingMessagesToEmail = False, returnCopyGraduationRequirementsMessagesToEmail = False, returnCopyMessagesToEmail = False, returnCopyOnlineFormMessagesToEmail = False, returnCopySchedulingMessagesToEmail = False, returnCreatedTime = False, returnCurrentGradeScoreHighNotification = False, returnCurrentGradeScoreHighNotificationEmail = False, returnCurrentGradeScoreLowNotification = False, returnCurrentGradeScoreLowNotificationEmail = False, returnEnableCompletedCareerPlanChangeNotification = False, returnEnableCompletedCareerPlanChangeNotificationEmail = False, returnEnableCompletedGradeChangeNotification = False, returnEnableCompletedGradeChangeNotificationEmail = False, returnEnableGradebookGradeChangeRequestDeniedEmail = False, returnEnableGradebookGradeChangeRequestNotificationEmail = False, returnEnableGradebookLastEntryNotificationEmail = False, returnEnableOnlineAssignmentAvailableNotificationEmail = False, returnEnableOnlineAssingmentScoresAvailableNotificationEmail = False, returnEnableStudentScheduleChangeNotification = False, returnEnableStudentScheduleChangeNotificationEmail = False, returnGradebookHighAssignmentThreshold = False, returnGradebookHighThreshold = False, returnGradebookLowAssignmentThreshold = False, returnGradebookLowThreshold = False, returnMissingAssignmentNotification = False, returnMissingAssignmentNotificationEmail = False, returnModifiedTime = False, returnOnlySendAssignmentScoreHighNotificationsOncePerAssignment = False, returnOnlySendAssignmentScoreLowNotificationsOncePerAssignment = False, returnOnlySendCurrentGradeScoreHighNotificationsOnce = False, returnOnlySendCurrentGradeScoreLowNotificationsOnce = False, returnOnlySendMissingAssignmentNotificationForCurrentGradingPeriod = False, returnOnlySendMissingAssignmentNotificationsOncePerAssignment = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/UserMessageSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getUserMessageSetting(UserMessageSettingID, EntityID = 1, returnUserMessageSettingID = True, returnAssignmentScoreHighNotification = False, returnAssignmentScoreHighNotificationEmail = False, returnAssignmentScoreLowNotification = False, returnAssignmentScoreLowNotificationEmail = False, returnCopyAttendanceMessagesToEmail = False, returnCopyDisciplineMessagesToEmail = False, returnCopyEnrollmentMessagesToEmail = False, returnCopyFeeManagementMessagesToEmail = False, returnCopyFoodServiceMessagesToEmail = False, returnCopyGradebookMessagesToEmail = False, returnCopyGradingMessagesToEmail = False, returnCopyGraduationRequirementsMessagesToEmail = False, returnCopyMessagesToEmail = False, returnCopyOnlineFormMessagesToEmail = False, returnCopySchedulingMessagesToEmail = False, returnCreatedTime = False, returnCurrentGradeScoreHighNotification = False, returnCurrentGradeScoreHighNotificationEmail = False, returnCurrentGradeScoreLowNotification = False, returnCurrentGradeScoreLowNotificationEmail = False, returnEnableCompletedCareerPlanChangeNotification = False, returnEnableCompletedCareerPlanChangeNotificationEmail = False, returnEnableCompletedGradeChangeNotification = False, returnEnableCompletedGradeChangeNotificationEmail = False, returnEnableGradebookGradeChangeRequestDeniedEmail = False, returnEnableGradebookGradeChangeRequestNotificationEmail = False, returnEnableGradebookLastEntryNotificationEmail = False, returnEnableOnlineAssignmentAvailableNotificationEmail = False, returnEnableOnlineAssingmentScoresAvailableNotificationEmail = False, returnEnableStudentScheduleChangeNotification = False, returnEnableStudentScheduleChangeNotificationEmail = False, returnGradebookHighAssignmentThreshold = False, returnGradebookHighThreshold = False, returnGradebookLowAssignmentThreshold = False, returnGradebookLowThreshold = False, returnMissingAssignmentNotification = False, returnMissingAssignmentNotificationEmail = False, returnModifiedTime = False, returnOnlySendAssignmentScoreHighNotificationsOncePerAssignment = False, returnOnlySendAssignmentScoreLowNotificationsOncePerAssignment = False, returnOnlySendCurrentGradeScoreHighNotificationsOnce = False, returnOnlySendCurrentGradeScoreLowNotificationsOnce = False, returnOnlySendMissingAssignmentNotificationForCurrentGradingPeriod = False, returnOnlySendMissingAssignmentNotificationsOncePerAssignment = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/UserMessageSetting/" + str(UserMessageSettingID), verb = "get", return_params_list = return_params_list)

def modifyUserMessageSetting(UserMessageSettingID, EntityID = 1, setAssignmentScoreHighNotification = None, setAssignmentScoreHighNotificationEmail = None, setAssignmentScoreLowNotification = None, setAssignmentScoreLowNotificationEmail = None, setCopyAttendanceMessagesToEmail = None, setCopyDisciplineMessagesToEmail = None, setCopyEnrollmentMessagesToEmail = None, setCopyFeeManagementMessagesToEmail = None, setCopyFoodServiceMessagesToEmail = None, setCopyGradebookMessagesToEmail = None, setCopyGradingMessagesToEmail = None, setCopyGraduationRequirementsMessagesToEmail = None, setCopyMessagesToEmail = None, setCopyOnlineFormMessagesToEmail = None, setCopySchedulingMessagesToEmail = None, setCurrentGradeScoreHighNotification = None, setCurrentGradeScoreHighNotificationEmail = None, setCurrentGradeScoreLowNotification = None, setCurrentGradeScoreLowNotificationEmail = None, setEnableCompletedCareerPlanChangeNotification = None, setEnableCompletedCareerPlanChangeNotificationEmail = None, setEnableCompletedGradeChangeNotification = None, setEnableCompletedGradeChangeNotificationEmail = None, setEnableGradebookGradeChangeRequestDeniedEmail = None, setEnableGradebookGradeChangeRequestNotificationEmail = None, setEnableGradebookLastEntryNotificationEmail = None, setEnableOnlineAssignmentAvailableNotificationEmail = None, setEnableOnlineAssingmentScoresAvailableNotificationEmail = None, setEnableStudentScheduleChangeNotification = None, setEnableStudentScheduleChangeNotificationEmail = None, setGradebookHighAssignmentThreshold = None, setGradebookHighThreshold = None, setGradebookLowAssignmentThreshold = None, setGradebookLowThreshold = None, setMissingAssignmentNotification = None, setMissingAssignmentNotificationEmail = None, setOnlySendAssignmentScoreHighNotificationsOncePerAssignment = None, setOnlySendAssignmentScoreLowNotificationsOncePerAssignment = None, setOnlySendCurrentGradeScoreHighNotificationsOnce = None, setOnlySendCurrentGradeScoreLowNotificationsOnce = None, setOnlySendMissingAssignmentNotificationForCurrentGradingPeriod = None, setOnlySendMissingAssignmentNotificationsOncePerAssignment = None, setUserIDOwner = None, setRelationships = None, returnUserMessageSettingID = True, returnAssignmentScoreHighNotification = False, returnAssignmentScoreHighNotificationEmail = False, returnAssignmentScoreLowNotification = False, returnAssignmentScoreLowNotificationEmail = False, returnCopyAttendanceMessagesToEmail = False, returnCopyDisciplineMessagesToEmail = False, returnCopyEnrollmentMessagesToEmail = False, returnCopyFeeManagementMessagesToEmail = False, returnCopyFoodServiceMessagesToEmail = False, returnCopyGradebookMessagesToEmail = False, returnCopyGradingMessagesToEmail = False, returnCopyGraduationRequirementsMessagesToEmail = False, returnCopyMessagesToEmail = False, returnCopyOnlineFormMessagesToEmail = False, returnCopySchedulingMessagesToEmail = False, returnCreatedTime = False, returnCurrentGradeScoreHighNotification = False, returnCurrentGradeScoreHighNotificationEmail = False, returnCurrentGradeScoreLowNotification = False, returnCurrentGradeScoreLowNotificationEmail = False, returnEnableCompletedCareerPlanChangeNotification = False, returnEnableCompletedCareerPlanChangeNotificationEmail = False, returnEnableCompletedGradeChangeNotification = False, returnEnableCompletedGradeChangeNotificationEmail = False, returnEnableGradebookGradeChangeRequestDeniedEmail = False, returnEnableGradebookGradeChangeRequestNotificationEmail = False, returnEnableGradebookLastEntryNotificationEmail = False, returnEnableOnlineAssignmentAvailableNotificationEmail = False, returnEnableOnlineAssingmentScoresAvailableNotificationEmail = False, returnEnableStudentScheduleChangeNotification = False, returnEnableStudentScheduleChangeNotificationEmail = False, returnGradebookHighAssignmentThreshold = False, returnGradebookHighThreshold = False, returnGradebookLowAssignmentThreshold = False, returnGradebookLowThreshold = False, returnMissingAssignmentNotification = False, returnMissingAssignmentNotificationEmail = False, returnModifiedTime = False, returnOnlySendAssignmentScoreHighNotificationsOncePerAssignment = False, returnOnlySendAssignmentScoreLowNotificationsOncePerAssignment = False, returnOnlySendCurrentGradeScoreHighNotificationsOnce = False, returnOnlySendCurrentGradeScoreLowNotificationsOnce = False, returnOnlySendMissingAssignmentNotificationForCurrentGradingPeriod = False, returnOnlySendMissingAssignmentNotificationsOncePerAssignment = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/UserMessageSetting/" + str(UserMessageSettingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createUserMessageSetting(EntityID = 1, setAssignmentScoreHighNotification = None, setAssignmentScoreHighNotificationEmail = None, setAssignmentScoreLowNotification = None, setAssignmentScoreLowNotificationEmail = None, setCopyAttendanceMessagesToEmail = None, setCopyDisciplineMessagesToEmail = None, setCopyEnrollmentMessagesToEmail = None, setCopyFeeManagementMessagesToEmail = None, setCopyFoodServiceMessagesToEmail = None, setCopyGradebookMessagesToEmail = None, setCopyGradingMessagesToEmail = None, setCopyGraduationRequirementsMessagesToEmail = None, setCopyMessagesToEmail = None, setCopyOnlineFormMessagesToEmail = None, setCopySchedulingMessagesToEmail = None, setCurrentGradeScoreHighNotification = None, setCurrentGradeScoreHighNotificationEmail = None, setCurrentGradeScoreLowNotification = None, setCurrentGradeScoreLowNotificationEmail = None, setEnableCompletedCareerPlanChangeNotification = None, setEnableCompletedCareerPlanChangeNotificationEmail = None, setEnableCompletedGradeChangeNotification = None, setEnableCompletedGradeChangeNotificationEmail = None, setEnableGradebookGradeChangeRequestDeniedEmail = None, setEnableGradebookGradeChangeRequestNotificationEmail = None, setEnableGradebookLastEntryNotificationEmail = None, setEnableOnlineAssignmentAvailableNotificationEmail = None, setEnableOnlineAssingmentScoresAvailableNotificationEmail = None, setEnableStudentScheduleChangeNotification = None, setEnableStudentScheduleChangeNotificationEmail = None, setGradebookHighAssignmentThreshold = None, setGradebookHighThreshold = None, setGradebookLowAssignmentThreshold = None, setGradebookLowThreshold = None, setMissingAssignmentNotification = None, setMissingAssignmentNotificationEmail = None, setOnlySendAssignmentScoreHighNotificationsOncePerAssignment = None, setOnlySendAssignmentScoreLowNotificationsOncePerAssignment = None, setOnlySendCurrentGradeScoreHighNotificationsOnce = None, setOnlySendCurrentGradeScoreLowNotificationsOnce = None, setOnlySendMissingAssignmentNotificationForCurrentGradingPeriod = None, setOnlySendMissingAssignmentNotificationsOncePerAssignment = None, setUserIDOwner = None, setRelationships = None, returnUserMessageSettingID = True, returnAssignmentScoreHighNotification = False, returnAssignmentScoreHighNotificationEmail = False, returnAssignmentScoreLowNotification = False, returnAssignmentScoreLowNotificationEmail = False, returnCopyAttendanceMessagesToEmail = False, returnCopyDisciplineMessagesToEmail = False, returnCopyEnrollmentMessagesToEmail = False, returnCopyFeeManagementMessagesToEmail = False, returnCopyFoodServiceMessagesToEmail = False, returnCopyGradebookMessagesToEmail = False, returnCopyGradingMessagesToEmail = False, returnCopyGraduationRequirementsMessagesToEmail = False, returnCopyMessagesToEmail = False, returnCopyOnlineFormMessagesToEmail = False, returnCopySchedulingMessagesToEmail = False, returnCreatedTime = False, returnCurrentGradeScoreHighNotification = False, returnCurrentGradeScoreHighNotificationEmail = False, returnCurrentGradeScoreLowNotification = False, returnCurrentGradeScoreLowNotificationEmail = False, returnEnableCompletedCareerPlanChangeNotification = False, returnEnableCompletedCareerPlanChangeNotificationEmail = False, returnEnableCompletedGradeChangeNotification = False, returnEnableCompletedGradeChangeNotificationEmail = False, returnEnableGradebookGradeChangeRequestDeniedEmail = False, returnEnableGradebookGradeChangeRequestNotificationEmail = False, returnEnableGradebookLastEntryNotificationEmail = False, returnEnableOnlineAssignmentAvailableNotificationEmail = False, returnEnableOnlineAssingmentScoresAvailableNotificationEmail = False, returnEnableStudentScheduleChangeNotification = False, returnEnableStudentScheduleChangeNotificationEmail = False, returnGradebookHighAssignmentThreshold = False, returnGradebookHighThreshold = False, returnGradebookLowAssignmentThreshold = False, returnGradebookLowThreshold = False, returnMissingAssignmentNotification = False, returnMissingAssignmentNotificationEmail = False, returnModifiedTime = False, returnOnlySendAssignmentScoreHighNotificationsOncePerAssignment = False, returnOnlySendAssignmentScoreLowNotificationsOncePerAssignment = False, returnOnlySendCurrentGradeScoreHighNotificationsOnce = False, returnOnlySendCurrentGradeScoreLowNotificationsOnce = False, returnOnlySendMissingAssignmentNotificationForCurrentGradingPeriod = False, returnOnlySendMissingAssignmentNotificationsOncePerAssignment = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/UserMessageSetting/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteUserMessageSetting(UserMessageSettingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")