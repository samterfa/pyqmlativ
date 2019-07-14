# This module contains Staff functions.

from .Utilities import make_request

import pandas as pd

import json

import re

def getEveryConfigEntityGroupYear(EntityID = 1, page = 1, pageSize = 100, returnConfigEntityGroupYearID = True, returnAllowFoodServiceOnlinePaymentsAccessByDefault = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, returnConfigEntityGroupYearID = True, returnAllowFoodServiceOnlinePaymentsAccessByDefault = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "get", return_params_list = return_params_list)

def modifyConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, setAllowFoodServiceOnlinePaymentsAccessByDefault = None, setEntityGroupKey = None, setEntityID = None, setSchoolYearID = None, setRelationships = None, returnConfigEntityGroupYearID = True, returnAllowFoodServiceOnlinePaymentsAccessByDefault = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigEntityGroupYear(EntityID = 1, setAllowFoodServiceOnlinePaymentsAccessByDefault = None, setEntityGroupKey = None, setEntityID = None, setSchoolYearID = None, setRelationships = None, returnConfigEntityGroupYearID = True, returnAllowFoodServiceOnlinePaymentsAccessByDefault = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ConfigEntityGroupYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigSystem(EntityID = 1, page = 1, pageSize = 100, returnConfigSystemID = True, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnModifiedTime = False, returnNewTeacherAccessUserMessageContent = False, returnNewTeacherAccessUserMessageSubject = False, returnStaffNumberMask = False, returnStaffNumberStartValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigSystem(ConfigSystemID, EntityID = 1, returnConfigSystemID = True, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnModifiedTime = False, returnNewTeacherAccessUserMessageContent = False, returnNewTeacherAccessUserMessageSubject = False, returnStaffNumberMask = False, returnStaffNumberStartValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ConfigSystem/" + str(ConfigSystemID), verb = "get", return_params_list = return_params_list)

def modifyConfigSystem(ConfigSystemID, EntityID = 1, setAutoGenerateSecurityUser = None, setAutoGenerateSecurityUserCode = None, setNewTeacherAccessUserMessageContent = None, setNewTeacherAccessUserMessageSubject = None, setStaffNumberMask = None, setStaffNumberStartValue = None, setRelationships = None, returnConfigSystemID = True, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnModifiedTime = False, returnNewTeacherAccessUserMessageContent = False, returnNewTeacherAccessUserMessageSubject = False, returnStaffNumberMask = False, returnStaffNumberStartValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ConfigSystem/" + str(ConfigSystemID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigSystem(EntityID = 1, setAutoGenerateSecurityUser = None, setAutoGenerateSecurityUserCode = None, setNewTeacherAccessUserMessageContent = None, setNewTeacherAccessUserMessageSubject = None, setStaffNumberMask = None, setStaffNumberStartValue = None, setRelationships = None, returnConfigSystemID = True, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnModifiedTime = False, returnNewTeacherAccessUserMessageContent = False, returnNewTeacherAccessUserMessageSubject = False, returnStaffNumberMask = False, returnStaffNumberStartValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ConfigSystem/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigSystem(ConfigSystemID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDepartment(EntityID = 1, page = 1, pageSize = 100, returnDepartmentID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDepartmentIDClonedFrom = False, returnDepartmentIDClonedTo = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStaffIDDepartmentHead = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/Department/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDepartment(DepartmentID, EntityID = 1, returnDepartmentID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDepartmentIDClonedFrom = False, returnDepartmentIDClonedTo = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStaffIDDepartmentHead = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/Department/" + str(DepartmentID), verb = "get", return_params_list = return_params_list)

def modifyDepartment(DepartmentID, EntityID = 1, setCode = None, setDepartmentIDClonedFrom = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setSchoolYearID = None, setStaffIDDepartmentHead = None, setRelationships = None, returnDepartmentID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDepartmentIDClonedFrom = False, returnDepartmentIDClonedTo = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStaffIDDepartmentHead = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/Department/" + str(DepartmentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDepartment(EntityID = 1, setCode = None, setDepartmentIDClonedFrom = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setSchoolYearID = None, setStaffIDDepartmentHead = None, setRelationships = None, returnDepartmentID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDepartmentIDClonedFrom = False, returnDepartmentIDClonedTo = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStaffIDDepartmentHead = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/Department/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDepartment(DepartmentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryMassPrintStaffScheduleRunHistory(EntityID = 1, page = 1, pageSize = 100, returnMassPrintStaffScheduleRunHistoryID = True, returnCreatedTime = False, returnEntityID = False, returnMediaID = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnRequestIdentifier = False, returnRunDescription = False, returnSchoolYearID = False, returnSendMessageOnComplete = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/MassPrintStaffScheduleRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getMassPrintStaffScheduleRunHistory(MassPrintStaffScheduleRunHistoryID, EntityID = 1, returnMassPrintStaffScheduleRunHistoryID = True, returnCreatedTime = False, returnEntityID = False, returnMediaID = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnRequestIdentifier = False, returnRunDescription = False, returnSchoolYearID = False, returnSendMessageOnComplete = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/MassPrintStaffScheduleRunHistory/" + str(MassPrintStaffScheduleRunHistoryID), verb = "get", return_params_list = return_params_list)

def modifyMassPrintStaffScheduleRunHistory(MassPrintStaffScheduleRunHistoryID, EntityID = 1, setEntityID = None, setMediaID = None, setRequestIdentifier = None, setRunDescription = None, setSchoolYearID = None, setSendMessageOnComplete = None, setWorkflowInstanceID = None, setRelationships = None, returnMassPrintStaffScheduleRunHistoryID = True, returnCreatedTime = False, returnEntityID = False, returnMediaID = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnRequestIdentifier = False, returnRunDescription = False, returnSchoolYearID = False, returnSendMessageOnComplete = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/MassPrintStaffScheduleRunHistory/" + str(MassPrintStaffScheduleRunHistoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createMassPrintStaffScheduleRunHistory(EntityID = 1, setEntityID = None, setMediaID = None, setRequestIdentifier = None, setRunDescription = None, setSchoolYearID = None, setSendMessageOnComplete = None, setWorkflowInstanceID = None, setRelationships = None, returnMassPrintStaffScheduleRunHistoryID = True, returnCreatedTime = False, returnEntityID = False, returnMediaID = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnRequestIdentifier = False, returnRunDescription = False, returnSchoolYearID = False, returnSendMessageOnComplete = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/MassPrintStaffScheduleRunHistory/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteMassPrintStaffScheduleRunHistory(MassPrintStaffScheduleRunHistoryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNextStaffNumber(EntityID = 1, page = 1, pageSize = 100, returnNextStaffNumberID = True, returnCreatedTime = False, returnMaskPrefix = False, returnModifiedTime = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/NextStaffNumber/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNextStaffNumber(NextStaffNumberID, EntityID = 1, returnNextStaffNumberID = True, returnCreatedTime = False, returnMaskPrefix = False, returnModifiedTime = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/NextStaffNumber/" + str(NextStaffNumberID), verb = "get", return_params_list = return_params_list)

def modifyNextStaffNumber(NextStaffNumberID, EntityID = 1, setMaskPrefix = None, setSequenceNumber = None, setRelationships = None, returnNextStaffNumberID = True, returnCreatedTime = False, returnMaskPrefix = False, returnModifiedTime = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/NextStaffNumber/" + str(NextStaffNumberID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNextStaffNumber(EntityID = 1, setMaskPrefix = None, setSequenceNumber = None, setRelationships = None, returnNextStaffNumberID = True, returnCreatedTime = False, returnMaskPrefix = False, returnModifiedTime = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/NextStaffNumber/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNextStaffNumber(NextStaffNumberID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryScheduleBlocker(EntityID = 1, page = 1, pageSize = 100, returnScheduleBlockerID = True, returnCreatedTime = False, returnEndDate = False, returnEntityID = False, returnModifiedTime = False, returnReason = False, returnSchoolYearID = False, returnStaffID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ScheduleBlocker/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getScheduleBlocker(ScheduleBlockerID, EntityID = 1, returnScheduleBlockerID = True, returnCreatedTime = False, returnEndDate = False, returnEntityID = False, returnModifiedTime = False, returnReason = False, returnSchoolYearID = False, returnStaffID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ScheduleBlocker/" + str(ScheduleBlockerID), verb = "get", return_params_list = return_params_list)

def modifyScheduleBlocker(ScheduleBlockerID, EntityID = 1, setEndDate = None, setEntityID = None, setReason = None, setSchoolYearID = None, setStaffID = None, setStartDate = None, setRelationships = None, returnScheduleBlockerID = True, returnCreatedTime = False, returnEndDate = False, returnEntityID = False, returnModifiedTime = False, returnReason = False, returnSchoolYearID = False, returnStaffID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ScheduleBlocker/" + str(ScheduleBlockerID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createScheduleBlocker(EntityID = 1, setEndDate = None, setEntityID = None, setReason = None, setSchoolYearID = None, setStaffID = None, setStartDate = None, setRelationships = None, returnScheduleBlockerID = True, returnCreatedTime = False, returnEndDate = False, returnEntityID = False, returnModifiedTime = False, returnReason = False, returnSchoolYearID = False, returnStaffID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ScheduleBlocker/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteScheduleBlocker(ScheduleBlockerID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryScheduleBlockerDisplayPeriod(EntityID = 1, page = 1, pageSize = 100, returnScheduleBlockerDisplayPeriodID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnScheduleBlockerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ScheduleBlockerDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getScheduleBlockerDisplayPeriod(ScheduleBlockerDisplayPeriodID, EntityID = 1, returnScheduleBlockerDisplayPeriodID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnScheduleBlockerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ScheduleBlockerDisplayPeriod/" + str(ScheduleBlockerDisplayPeriodID), verb = "get", return_params_list = return_params_list)

def modifyScheduleBlockerDisplayPeriod(ScheduleBlockerDisplayPeriodID, EntityID = 1, setDisplayPeriodID = None, setScheduleBlockerID = None, setRelationships = None, returnScheduleBlockerDisplayPeriodID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnScheduleBlockerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ScheduleBlockerDisplayPeriod/" + str(ScheduleBlockerDisplayPeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createScheduleBlockerDisplayPeriod(EntityID = 1, setDisplayPeriodID = None, setScheduleBlockerID = None, setRelationships = None, returnScheduleBlockerDisplayPeriodID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnScheduleBlockerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ScheduleBlockerDisplayPeriod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteScheduleBlockerDisplayPeriod(ScheduleBlockerDisplayPeriodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStaffDepartment(EntityID = 1, page = 1, pageSize = 100, returnStaffDepartmentID = True, returnCreatedTime = False, returnDepartmentID = False, returnIsDefaultDepartment = False, returnModifiedTime = False, returnStaffDepartmentIDClonedFrom = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffDepartment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStaffDepartment(StaffDepartmentID, EntityID = 1, returnStaffDepartmentID = True, returnCreatedTime = False, returnDepartmentID = False, returnIsDefaultDepartment = False, returnModifiedTime = False, returnStaffDepartmentIDClonedFrom = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffDepartment/" + str(StaffDepartmentID), verb = "get", return_params_list = return_params_list)

def modifyStaffDepartment(StaffDepartmentID, EntityID = 1, setDepartmentID = None, setIsDefaultDepartment = None, setStaffDepartmentIDClonedFrom = None, setStaffID = None, setRelationships = None, returnStaffDepartmentID = True, returnCreatedTime = False, returnDepartmentID = False, returnIsDefaultDepartment = False, returnModifiedTime = False, returnStaffDepartmentIDClonedFrom = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffDepartment/" + str(StaffDepartmentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStaffDepartment(EntityID = 1, setDepartmentID = None, setIsDefaultDepartment = None, setStaffDepartmentIDClonedFrom = None, setStaffID = None, setRelationships = None, returnStaffDepartmentID = True, returnCreatedTime = False, returnDepartmentID = False, returnIsDefaultDepartment = False, returnModifiedTime = False, returnStaffDepartmentIDClonedFrom = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffDepartment/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStaffDepartment(StaffDepartmentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStaffEntityYear(EntityID = 1, page = 1, pageSize = 100, returnStaffEntityYearID = True, returnCreatedTime = False, returnEntityID = False, returnIsActive = False, returnIsAdditionalStaffOnNotification = False, returnIsCareerCenterCounselor = False, returnIsDisciplineOfficer = False, returnIsSubstituteTeacher = False, returnIsTeacher = False, returnModifiedTime = False, returnRoomIDDefault = False, returnSchoolYearID = False, returnSectionInformationStringNorthEastTXReport = False, returnStaffDepartmentSummary = False, returnStaffEntityYearClonedTo = False, returnStaffEntityYearIDClonedFrom = False, returnStaffID = False, returnTeacherNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStaffEntityYear(StaffEntityYearID, EntityID = 1, returnStaffEntityYearID = True, returnCreatedTime = False, returnEntityID = False, returnIsActive = False, returnIsAdditionalStaffOnNotification = False, returnIsCareerCenterCounselor = False, returnIsDisciplineOfficer = False, returnIsSubstituteTeacher = False, returnIsTeacher = False, returnModifiedTime = False, returnRoomIDDefault = False, returnSchoolYearID = False, returnSectionInformationStringNorthEastTXReport = False, returnStaffDepartmentSummary = False, returnStaffEntityYearClonedTo = False, returnStaffEntityYearIDClonedFrom = False, returnStaffID = False, returnTeacherNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffEntityYear/" + str(StaffEntityYearID), verb = "get", return_params_list = return_params_list)

def modifyStaffEntityYear(StaffEntityYearID, EntityID = 1, setEntityID = None, setIsActive = None, setIsCareerCenterCounselor = None, setIsDisciplineOfficer = None, setIsSubstituteTeacher = None, setIsTeacher = None, setRoomIDDefault = None, setSchoolYearID = None, setStaffEntityYearIDClonedFrom = None, setStaffID = None, setTeacherNumber = None, setRelationships = None, returnStaffEntityYearID = True, returnCreatedTime = False, returnEntityID = False, returnIsActive = False, returnIsAdditionalStaffOnNotification = False, returnIsCareerCenterCounselor = False, returnIsDisciplineOfficer = False, returnIsSubstituteTeacher = False, returnIsTeacher = False, returnModifiedTime = False, returnRoomIDDefault = False, returnSchoolYearID = False, returnSectionInformationStringNorthEastTXReport = False, returnStaffDepartmentSummary = False, returnStaffEntityYearClonedTo = False, returnStaffEntityYearIDClonedFrom = False, returnStaffID = False, returnTeacherNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffEntityYear/" + str(StaffEntityYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStaffEntityYear(EntityID = 1, setEntityID = None, setIsActive = None, setIsCareerCenterCounselor = None, setIsDisciplineOfficer = None, setIsSubstituteTeacher = None, setIsTeacher = None, setRoomIDDefault = None, setSchoolYearID = None, setStaffEntityYearIDClonedFrom = None, setStaffID = None, setTeacherNumber = None, setRelationships = None, returnStaffEntityYearID = True, returnCreatedTime = False, returnEntityID = False, returnIsActive = False, returnIsAdditionalStaffOnNotification = False, returnIsCareerCenterCounselor = False, returnIsDisciplineOfficer = False, returnIsSubstituteTeacher = False, returnIsTeacher = False, returnModifiedTime = False, returnRoomIDDefault = False, returnSchoolYearID = False, returnSectionInformationStringNorthEastTXReport = False, returnStaffDepartmentSummary = False, returnStaffEntityYearClonedTo = False, returnStaffEntityYearIDClonedFrom = False, returnStaffID = False, returnTeacherNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffEntityYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStaffEntityYear(StaffEntityYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStaff(EntityID = 1, page = 1, pageSize = 100, returnStaffID = True, returnActiveStudentCount = False, returnAssignmentCount = False, returnAssignmentCountForTerm = False, returnAssignmentCountForTermCalculated = False, returnAssignmentCountYTD = False, returnAssignmentCountYTDCalculated = False, returnAssignmentDataString = False, returnCreatedTime = False, returnDateTimeofLastScoredAssignment = False, returnDistrictID = False, returnDueDateOfLastAssignmentScored = False, returnFileFolderNumber = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnFutureAssignmentCountForTerm = False, returnFutureAssignmentCountForTermCalculated = False, returnGradebookLastAccessedTime = False, returnGradedAssignmentCountForTerm = False, returnGradedAssignmentCountForTermCalculated = False, returnGradeLevelLowerBound = False, returnGradeLevelUpperBound = False, returnIsActiveForDistrict = False, returnIsCurrentStaffEntityYear = False, returnMissingAssignmentCountForTerm = False, returnMissingAssignmentCountForTermCalculated = False, returnModifiedTime = False, returnNameID = False, returnNoCountAssignmentCountForTerm = False, returnNoCountAssignmentCountForTermCalculated = False, returnNonGradedAssignmentCountForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsYTD = False, returnPercentageOfAssignmentsScoredYTD = False, returnScoreClarifierAssignmentCountForTerm = False, returnScoreClarifierAssignmentCountForTermCalculated = False, returnStaffMeetCount = False, returnStaffMNID = False, returnStaffNumber = False, returnStaffWebsite = False, returnStudentAssignmentDataString = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/Staff/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStaff(StaffID, EntityID = 1, returnStaffID = True, returnActiveStudentCount = False, returnAssignmentCount = False, returnAssignmentCountForTerm = False, returnAssignmentCountForTermCalculated = False, returnAssignmentCountYTD = False, returnAssignmentCountYTDCalculated = False, returnAssignmentDataString = False, returnCreatedTime = False, returnDateTimeofLastScoredAssignment = False, returnDistrictID = False, returnDueDateOfLastAssignmentScored = False, returnFileFolderNumber = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnFutureAssignmentCountForTerm = False, returnFutureAssignmentCountForTermCalculated = False, returnGradebookLastAccessedTime = False, returnGradedAssignmentCountForTerm = False, returnGradedAssignmentCountForTermCalculated = False, returnGradeLevelLowerBound = False, returnGradeLevelUpperBound = False, returnIsActiveForDistrict = False, returnIsCurrentStaffEntityYear = False, returnMissingAssignmentCountForTerm = False, returnMissingAssignmentCountForTermCalculated = False, returnModifiedTime = False, returnNameID = False, returnNoCountAssignmentCountForTerm = False, returnNoCountAssignmentCountForTermCalculated = False, returnNonGradedAssignmentCountForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsYTD = False, returnPercentageOfAssignmentsScoredYTD = False, returnScoreClarifierAssignmentCountForTerm = False, returnScoreClarifierAssignmentCountForTermCalculated = False, returnStaffMeetCount = False, returnStaffMNID = False, returnStaffNumber = False, returnStaffWebsite = False, returnStudentAssignmentDataString = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/Staff/" + str(StaffID), verb = "get", return_params_list = return_params_list)

def modifyStaff(StaffID, EntityID = 1, setDistrictID = None, setFileFolderNumber = None, setFullNameFL = None, setFullNameFML = None, setFullNameLFM = None, setNameID = None, setStaffNumber = None, setStaffWebsite = None, setRelationships = None, returnStaffID = True, returnActiveStudentCount = False, returnAssignmentCount = False, returnAssignmentCountForTerm = False, returnAssignmentCountForTermCalculated = False, returnAssignmentCountYTD = False, returnAssignmentCountYTDCalculated = False, returnAssignmentDataString = False, returnCreatedTime = False, returnDateTimeofLastScoredAssignment = False, returnDistrictID = False, returnDueDateOfLastAssignmentScored = False, returnFileFolderNumber = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnFutureAssignmentCountForTerm = False, returnFutureAssignmentCountForTermCalculated = False, returnGradebookLastAccessedTime = False, returnGradedAssignmentCountForTerm = False, returnGradedAssignmentCountForTermCalculated = False, returnGradeLevelLowerBound = False, returnGradeLevelUpperBound = False, returnIsActiveForDistrict = False, returnIsCurrentStaffEntityYear = False, returnMissingAssignmentCountForTerm = False, returnMissingAssignmentCountForTermCalculated = False, returnModifiedTime = False, returnNameID = False, returnNoCountAssignmentCountForTerm = False, returnNoCountAssignmentCountForTermCalculated = False, returnNonGradedAssignmentCountForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsYTD = False, returnPercentageOfAssignmentsScoredYTD = False, returnScoreClarifierAssignmentCountForTerm = False, returnScoreClarifierAssignmentCountForTermCalculated = False, returnStaffMeetCount = False, returnStaffMNID = False, returnStaffNumber = False, returnStaffWebsite = False, returnStudentAssignmentDataString = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/Staff/" + str(StaffID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStaff(EntityID = 1, setDistrictID = None, setFileFolderNumber = None, setFullNameFL = None, setFullNameFML = None, setFullNameLFM = None, setNameID = None, setStaffNumber = None, setStaffWebsite = None, setRelationships = None, returnStaffID = True, returnActiveStudentCount = False, returnAssignmentCount = False, returnAssignmentCountForTerm = False, returnAssignmentCountForTermCalculated = False, returnAssignmentCountYTD = False, returnAssignmentCountYTDCalculated = False, returnAssignmentDataString = False, returnCreatedTime = False, returnDateTimeofLastScoredAssignment = False, returnDistrictID = False, returnDueDateOfLastAssignmentScored = False, returnFileFolderNumber = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnFutureAssignmentCountForTerm = False, returnFutureAssignmentCountForTermCalculated = False, returnGradebookLastAccessedTime = False, returnGradedAssignmentCountForTerm = False, returnGradedAssignmentCountForTermCalculated = False, returnGradeLevelLowerBound = False, returnGradeLevelUpperBound = False, returnIsActiveForDistrict = False, returnIsCurrentStaffEntityYear = False, returnMissingAssignmentCountForTerm = False, returnMissingAssignmentCountForTermCalculated = False, returnModifiedTime = False, returnNameID = False, returnNoCountAssignmentCountForTerm = False, returnNoCountAssignmentCountForTermCalculated = False, returnNonGradedAssignmentCountForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsYTD = False, returnPercentageOfAssignmentsScoredYTD = False, returnScoreClarifierAssignmentCountForTerm = False, returnScoreClarifierAssignmentCountForTermCalculated = False, returnStaffMeetCount = False, returnStaffMNID = False, returnStaffNumber = False, returnStaffWebsite = False, returnStudentAssignmentDataString = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/Staff/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStaff(StaffID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStaffStaffType(EntityID = 1, page = 1, pageSize = 100, returnStaffStaffTypeID = True, returnCreatedTime = False, returnEndDate = False, returnIsPrimary = False, returnModifiedTime = False, returnStaffID = False, returnStaffStaffTypeIDClonedFrom = False, returnStaffTypeID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffStaffType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStaffStaffType(StaffStaffTypeID, EntityID = 1, returnStaffStaffTypeID = True, returnCreatedTime = False, returnEndDate = False, returnIsPrimary = False, returnModifiedTime = False, returnStaffID = False, returnStaffStaffTypeIDClonedFrom = False, returnStaffTypeID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffStaffType/" + str(StaffStaffTypeID), verb = "get", return_params_list = return_params_list)

def modifyStaffStaffType(StaffStaffTypeID, EntityID = 1, setEndDate = None, setIsPrimary = None, setStaffID = None, setStaffStaffTypeIDClonedFrom = None, setStaffTypeID = None, setStartDate = None, setRelationships = None, returnStaffStaffTypeID = True, returnCreatedTime = False, returnEndDate = False, returnIsPrimary = False, returnModifiedTime = False, returnStaffID = False, returnStaffStaffTypeIDClonedFrom = False, returnStaffTypeID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffStaffType/" + str(StaffStaffTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStaffStaffType(EntityID = 1, setEndDate = None, setIsPrimary = None, setStaffID = None, setStaffStaffTypeIDClonedFrom = None, setStaffTypeID = None, setStartDate = None, setRelationships = None, returnStaffStaffTypeID = True, returnCreatedTime = False, returnEndDate = False, returnIsPrimary = False, returnModifiedTime = False, returnStaffID = False, returnStaffStaffTypeIDClonedFrom = False, returnStaffTypeID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffStaffType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStaffStaffType(StaffStaffTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStaffType(EntityID = 1, page = 1, pageSize = 100, returnStaffTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStaffTypeIDClonedFrom = False, returnStaffTypeIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStaffType(StaffTypeID, EntityID = 1, returnStaffTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStaffTypeIDClonedFrom = False, returnStaffTypeIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffType/" + str(StaffTypeID), verb = "get", return_params_list = return_params_list)

def modifyStaffType(StaffTypeID, EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setSchoolYearID = None, setStaffTypeIDClonedFrom = None, setRelationships = None, returnStaffTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStaffTypeIDClonedFrom = False, returnStaffTypeIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffType/" + str(StaffTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStaffType(EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setSchoolYearID = None, setStaffTypeIDClonedFrom = None, setRelationships = None, returnStaffTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStaffTypeIDClonedFrom = False, returnStaffTypeIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStaffType(StaffTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")