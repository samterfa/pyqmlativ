# This module contains Family functions.

from .Utilities import make_request

import pandas as pd

import json

import re

def getEveryChangeRequest(EntityID = 1, page = 1, pageSize = 100, returnChangeRequestID = True, returnArea = False, returnAreaCode = False, returnCreatedTime = False, returnEntityID = False, returnLevelPendingApproval = False, returnModifiedTime = False, returnNameID = False, returnSchoolYearID = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequest/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getChangeRequest(ChangeRequestID, EntityID = 1, returnChangeRequestID = True, returnArea = False, returnAreaCode = False, returnCreatedTime = False, returnEntityID = False, returnLevelPendingApproval = False, returnModifiedTime = False, returnNameID = False, returnSchoolYearID = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequest/" + str(ChangeRequestID), verb = "get", return_params_list = return_params_list)

def modifyChangeRequest(ChangeRequestID, EntityID = 1, setArea = None, setAreaCode = None, setEntityID = None, setNameID = None, setSchoolYearID = None, setRelationships = None, returnChangeRequestID = True, returnArea = False, returnAreaCode = False, returnCreatedTime = False, returnEntityID = False, returnLevelPendingApproval = False, returnModifiedTime = False, returnNameID = False, returnSchoolYearID = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequest/" + str(ChangeRequestID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createChangeRequest(EntityID = 1, setArea = None, setAreaCode = None, setEntityID = None, setNameID = None, setSchoolYearID = None, setRelationships = None, returnChangeRequestID = True, returnArea = False, returnAreaCode = False, returnCreatedTime = False, returnEntityID = False, returnLevelPendingApproval = False, returnModifiedTime = False, returnNameID = False, returnSchoolYearID = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequest/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteChangeRequest(ChangeRequestID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryChangeRequestApprovalTask(EntityID = 1, page = 1, pageSize = 100, returnChangeRequestApprovalTaskID = True, returnArea = False, returnAreaCode = False, returnChangeRequestApprovalTaskIDClonedFrom = False, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnDescription = False, returnLevel = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestApprovalTask/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getChangeRequestApprovalTask(ChangeRequestApprovalTaskID, EntityID = 1, returnChangeRequestApprovalTaskID = True, returnArea = False, returnAreaCode = False, returnChangeRequestApprovalTaskIDClonedFrom = False, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnDescription = False, returnLevel = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestApprovalTask/" + str(ChangeRequestApprovalTaskID), verb = "get", return_params_list = return_params_list)

def modifyChangeRequestApprovalTask(ChangeRequestApprovalTaskID, EntityID = 1, setArea = None, setAreaCode = None, setChangeRequestApprovalTaskIDClonedFrom = None, setConfigEntityGroupYearID = None, setDescription = None, setLevel = None, setRelationships = None, returnChangeRequestApprovalTaskID = True, returnArea = False, returnAreaCode = False, returnChangeRequestApprovalTaskIDClonedFrom = False, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnDescription = False, returnLevel = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestApprovalTask/" + str(ChangeRequestApprovalTaskID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createChangeRequestApprovalTask(EntityID = 1, setArea = None, setAreaCode = None, setChangeRequestApprovalTaskIDClonedFrom = None, setConfigEntityGroupYearID = None, setDescription = None, setLevel = None, setRelationships = None, returnChangeRequestApprovalTaskID = True, returnArea = False, returnAreaCode = False, returnChangeRequestApprovalTaskIDClonedFrom = False, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnDescription = False, returnLevel = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestApprovalTask/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteChangeRequestApprovalTask(ChangeRequestApprovalTaskID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryChangeRequestApprovalTaskSecurityGroup(EntityID = 1, page = 1, pageSize = 100, returnChangeRequestApprovalTaskSecurityGroupID = True, returnChangeRequestApprovalTaskID = False, returnChangeRequestApprovalTaskSecurityGroupIDClonedFrom = False, returnCreatedTime = False, returnGroupIDSecurity = False, returnIsAlternate = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestApprovalTaskSecurityGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getChangeRequestApprovalTaskSecurityGroup(ChangeRequestApprovalTaskSecurityGroupID, EntityID = 1, returnChangeRequestApprovalTaskSecurityGroupID = True, returnChangeRequestApprovalTaskID = False, returnChangeRequestApprovalTaskSecurityGroupIDClonedFrom = False, returnCreatedTime = False, returnGroupIDSecurity = False, returnIsAlternate = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestApprovalTaskSecurityGroup/" + str(ChangeRequestApprovalTaskSecurityGroupID), verb = "get", return_params_list = return_params_list)

def modifyChangeRequestApprovalTaskSecurityGroup(ChangeRequestApprovalTaskSecurityGroupID, EntityID = 1, setChangeRequestApprovalTaskID = None, setChangeRequestApprovalTaskSecurityGroupIDClonedFrom = None, setGroupIDSecurity = None, setIsAlternate = None, setRelationships = None, returnChangeRequestApprovalTaskSecurityGroupID = True, returnChangeRequestApprovalTaskID = False, returnChangeRequestApprovalTaskSecurityGroupIDClonedFrom = False, returnCreatedTime = False, returnGroupIDSecurity = False, returnIsAlternate = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestApprovalTaskSecurityGroup/" + str(ChangeRequestApprovalTaskSecurityGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createChangeRequestApprovalTaskSecurityGroup(EntityID = 1, setChangeRequestApprovalTaskID = None, setChangeRequestApprovalTaskSecurityGroupIDClonedFrom = None, setGroupIDSecurity = None, setIsAlternate = None, setRelationships = None, returnChangeRequestApprovalTaskSecurityGroupID = True, returnChangeRequestApprovalTaskID = False, returnChangeRequestApprovalTaskSecurityGroupIDClonedFrom = False, returnCreatedTime = False, returnGroupIDSecurity = False, returnIsAlternate = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestApprovalTaskSecurityGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteChangeRequestApprovalTaskSecurityGroup(ChangeRequestApprovalTaskSecurityGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryChangeRequestDetail(EntityID = 1, page = 1, pageSize = 100, returnChangeRequestDetailID = True, returnChangeRequestID = False, returnCreatedTime = False, returnFieldName = False, returnFieldNameCode = False, returnModifiedTime = False, returnOriginalValue = False, returnRequestedTime = False, returnRequestedValue = False, returnSourceID = False, returnStatus = False, returnStatusCode = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRequestedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getChangeRequestDetail(ChangeRequestDetailID, EntityID = 1, returnChangeRequestDetailID = True, returnChangeRequestID = False, returnCreatedTime = False, returnFieldName = False, returnFieldNameCode = False, returnModifiedTime = False, returnOriginalValue = False, returnRequestedTime = False, returnRequestedValue = False, returnSourceID = False, returnStatus = False, returnStatusCode = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRequestedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetail/" + str(ChangeRequestDetailID), verb = "get", return_params_list = return_params_list)

def modifyChangeRequestDetail(ChangeRequestDetailID, EntityID = 1, setChangeRequestID = None, setFieldName = None, setFieldNameCode = None, setOriginalValue = None, setRequestedTime = None, setRequestedValue = None, setSourceID = None, setStatus = None, setStatusCode = None, setUserIDApprover = None, setUserIDRequestedBy = None, setRelationships = None, returnChangeRequestDetailID = True, returnChangeRequestID = False, returnCreatedTime = False, returnFieldName = False, returnFieldNameCode = False, returnModifiedTime = False, returnOriginalValue = False, returnRequestedTime = False, returnRequestedValue = False, returnSourceID = False, returnStatus = False, returnStatusCode = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRequestedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetail/" + str(ChangeRequestDetailID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createChangeRequestDetail(EntityID = 1, setChangeRequestID = None, setFieldName = None, setFieldNameCode = None, setOriginalValue = None, setRequestedTime = None, setRequestedValue = None, setSourceID = None, setStatus = None, setStatusCode = None, setUserIDApprover = None, setUserIDRequestedBy = None, setRelationships = None, returnChangeRequestDetailID = True, returnChangeRequestID = False, returnCreatedTime = False, returnFieldName = False, returnFieldNameCode = False, returnModifiedTime = False, returnOriginalValue = False, returnRequestedTime = False, returnRequestedValue = False, returnSourceID = False, returnStatus = False, returnStatusCode = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRequestedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetail/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteChangeRequestDetail(ChangeRequestDetailID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryChangeRequestDetailApproval(EntityID = 1, page = 1, pageSize = 100, returnChangeRequestDetailApprovalID = True, returnChangeRequestDetailID = False, returnComment = False, returnCreatedTime = False, returnIsLastLevel = False, returnLevel = False, returnLevelDescription = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnTaskInstanceID = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetailApproval/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getChangeRequestDetailApproval(ChangeRequestDetailApprovalID, EntityID = 1, returnChangeRequestDetailApprovalID = True, returnChangeRequestDetailID = False, returnComment = False, returnCreatedTime = False, returnIsLastLevel = False, returnLevel = False, returnLevelDescription = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnTaskInstanceID = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetailApproval/" + str(ChangeRequestDetailApprovalID), verb = "get", return_params_list = return_params_list)

def modifyChangeRequestDetailApproval(ChangeRequestDetailApprovalID, EntityID = 1, setChangeRequestDetailID = None, setComment = None, setLevel = None, setLevelDescription = None, setStatus = None, setStatusCode = None, setTaskInstanceID = None, setUserIDApprover = None, setRelationships = None, returnChangeRequestDetailApprovalID = True, returnChangeRequestDetailID = False, returnComment = False, returnCreatedTime = False, returnIsLastLevel = False, returnLevel = False, returnLevelDescription = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnTaskInstanceID = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetailApproval/" + str(ChangeRequestDetailApprovalID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createChangeRequestDetailApproval(EntityID = 1, setChangeRequestDetailID = None, setComment = None, setLevel = None, setLevelDescription = None, setStatus = None, setStatusCode = None, setTaskInstanceID = None, setUserIDApprover = None, setRelationships = None, returnChangeRequestDetailApprovalID = True, returnChangeRequestDetailID = False, returnComment = False, returnCreatedTime = False, returnIsLastLevel = False, returnLevel = False, returnLevelDescription = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnTaskInstanceID = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetailApproval/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteChangeRequestDetailApproval(ChangeRequestDetailApprovalID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigEntityGroupYear(EntityID = 1, page = 1, pageSize = 100, returnConfigEntityGroupYearID = True, returnChangeRequestFamilyEmail = False, returnChangeRequestFamilyEmailCode = False, returnChangeRequestFamilyPhone = False, returnChangeRequestFamilyPhoneCode = False, returnChangeRequestStudentEmail = False, returnChangeRequestStudentEmailCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDefaultFeeManagementOnlinePaymentAccess = False, returnDefaultFeeManagementOnlinePaymentAccessCode = False, returnDefaultFoodServiceOnlinePaymentAccess = False, returnDefaultFoodServiceOnlinePaymentAccessCode = False, returnDisplayAssignments = False, returnDisplayCalendarEvents = False, returnDisplayDistrictActivityEvents = False, returnDisplayStudentActivityEvents = False, returnEmailTypeIDToDisplayFamilyStudentAccess = False, returnEndorsementSignatureOption = False, returnEndorsementSignatureOptionCode = False, returnEndorsementSignatureStatement = False, returnEntityGroupKey = False, returnEntityID = False, returnFamilyAccessAccountInfoEmailBody = False, returnFamilyAccessAccountInfoEmailIncludeResetPasswordText = False, returnFamilyAccessAccountInfoEmailSubject = False, returnFamilyAccessCareerPlanDisplayShowDroppedCourses = False, returnFamilyAccessDisplayCommentCodes = False, returnFamilyAccessDisplayFreeFormComments = False, returnFamilyAccessDisplayGradeBucketsAfterEndDate = False, returnFamilyAccessDisplayHonorRoll = False, returnFamilyAccessDisplayOnlyCurrentAndCompleteGrades = False, returnFamilyAccessDisplayOnlyCurrentMissingAssignments = False, returnFamilyAccessDisplayShowActualEarnedCredits = False, returnFamilyAccessDisplayShowAttendance = False, returnFamilyAccessDisplayShowDroppedCourses = False, returnFamilyAccessDisplayShowEndedAttendanceTerms = False, returnFamilyAccessDisplayShowPossibleEarnedCredits = False, returnFamilyAccessDisplayStudentAddress = False, returnFamilyAccessDisplayStudentRank = False, returnFamilyAccessDisplayUseReportCardGradeBucketSettings = False, returnFamilyAccessLinkStudentSectionsOnReportCard = False, returnFamilyStudentAccessDisplayTeacherEmail = False, returnFamilyStudentAccessDisplayTeacherPhoneNumber = False, returnHideScheduleMessage = False, returnHideSchedulePriorToCalendarDays = False, returnIsFamilyInformationApprovalWorkflowUpdated = False, returnIsStudentInformationApprovalWorkflowUpdated = False, returnModifiedTime = False, returnPhoneTypeIDToDisplayFamilyStudentAccess = False, returnRankMethodIDFamilyAccessReportCardGrading = False, returnRankMethodIDFamilyAccessReportCardStudent = False, returnReportCardGPADisplay = False, returnReportCardGPADisplayCode = False, returnReportCardHeaderAddressType = False, returnReportCardHeaderAddressTypeCode = False, returnReportCardStudentRankDisplay = False, returnReportCardStudentRankDisplayCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, returnConfigEntityGroupYearID = True, returnChangeRequestFamilyEmail = False, returnChangeRequestFamilyEmailCode = False, returnChangeRequestFamilyPhone = False, returnChangeRequestFamilyPhoneCode = False, returnChangeRequestStudentEmail = False, returnChangeRequestStudentEmailCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDefaultFeeManagementOnlinePaymentAccess = False, returnDefaultFeeManagementOnlinePaymentAccessCode = False, returnDefaultFoodServiceOnlinePaymentAccess = False, returnDefaultFoodServiceOnlinePaymentAccessCode = False, returnDisplayAssignments = False, returnDisplayCalendarEvents = False, returnDisplayDistrictActivityEvents = False, returnDisplayStudentActivityEvents = False, returnEmailTypeIDToDisplayFamilyStudentAccess = False, returnEndorsementSignatureOption = False, returnEndorsementSignatureOptionCode = False, returnEndorsementSignatureStatement = False, returnEntityGroupKey = False, returnEntityID = False, returnFamilyAccessAccountInfoEmailBody = False, returnFamilyAccessAccountInfoEmailIncludeResetPasswordText = False, returnFamilyAccessAccountInfoEmailSubject = False, returnFamilyAccessCareerPlanDisplayShowDroppedCourses = False, returnFamilyAccessDisplayCommentCodes = False, returnFamilyAccessDisplayFreeFormComments = False, returnFamilyAccessDisplayGradeBucketsAfterEndDate = False, returnFamilyAccessDisplayHonorRoll = False, returnFamilyAccessDisplayOnlyCurrentAndCompleteGrades = False, returnFamilyAccessDisplayOnlyCurrentMissingAssignments = False, returnFamilyAccessDisplayShowActualEarnedCredits = False, returnFamilyAccessDisplayShowAttendance = False, returnFamilyAccessDisplayShowDroppedCourses = False, returnFamilyAccessDisplayShowEndedAttendanceTerms = False, returnFamilyAccessDisplayShowPossibleEarnedCredits = False, returnFamilyAccessDisplayStudentAddress = False, returnFamilyAccessDisplayStudentRank = False, returnFamilyAccessDisplayUseReportCardGradeBucketSettings = False, returnFamilyAccessLinkStudentSectionsOnReportCard = False, returnFamilyStudentAccessDisplayTeacherEmail = False, returnFamilyStudentAccessDisplayTeacherPhoneNumber = False, returnHideScheduleMessage = False, returnHideSchedulePriorToCalendarDays = False, returnIsFamilyInformationApprovalWorkflowUpdated = False, returnIsStudentInformationApprovalWorkflowUpdated = False, returnModifiedTime = False, returnPhoneTypeIDToDisplayFamilyStudentAccess = False, returnRankMethodIDFamilyAccessReportCardGrading = False, returnRankMethodIDFamilyAccessReportCardStudent = False, returnReportCardGPADisplay = False, returnReportCardGPADisplayCode = False, returnReportCardHeaderAddressType = False, returnReportCardHeaderAddressTypeCode = False, returnReportCardStudentRankDisplay = False, returnReportCardStudentRankDisplayCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "get", return_params_list = return_params_list)

def modifyConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, setChangeRequestFamilyEmail = None, setChangeRequestFamilyEmailCode = None, setChangeRequestFamilyPhone = None, setChangeRequestFamilyPhoneCode = None, setChangeRequestStudentEmail = None, setChangeRequestStudentEmailCode = None, setConfigEntityGroupYearIDClonedFrom = None, setDefaultFeeManagementOnlinePaymentAccess = None, setDefaultFeeManagementOnlinePaymentAccessCode = None, setDefaultFoodServiceOnlinePaymentAccess = None, setDefaultFoodServiceOnlinePaymentAccessCode = None, setDisplayAssignments = None, setDisplayCalendarEvents = None, setDisplayDistrictActivityEvents = None, setDisplayStudentActivityEvents = None, setEmailTypeIDToDisplayFamilyStudentAccess = None, setEndorsementSignatureOption = None, setEndorsementSignatureOptionCode = None, setEndorsementSignatureStatement = None, setEntityGroupKey = None, setEntityID = None, setFamilyAccessAccountInfoEmailBody = None, setFamilyAccessAccountInfoEmailIncludeResetPasswordText = None, setFamilyAccessAccountInfoEmailSubject = None, setFamilyAccessCareerPlanDisplayShowDroppedCourses = None, setFamilyAccessDisplayCommentCodes = None, setFamilyAccessDisplayFreeFormComments = None, setFamilyAccessDisplayGradeBucketsAfterEndDate = None, setFamilyAccessDisplayHonorRoll = None, setFamilyAccessDisplayOnlyCurrentAndCompleteGrades = None, setFamilyAccessDisplayOnlyCurrentMissingAssignments = None, setFamilyAccessDisplayShowActualEarnedCredits = None, setFamilyAccessDisplayShowAttendance = None, setFamilyAccessDisplayShowDroppedCourses = None, setFamilyAccessDisplayShowEndedAttendanceTerms = None, setFamilyAccessDisplayShowPossibleEarnedCredits = None, setFamilyAccessDisplayStudentAddress = None, setFamilyAccessDisplayStudentRank = None, setFamilyAccessDisplayUseReportCardGradeBucketSettings = None, setFamilyAccessLinkStudentSectionsOnReportCard = None, setFamilyStudentAccessDisplayTeacherEmail = None, setFamilyStudentAccessDisplayTeacherPhoneNumber = None, setHideScheduleMessage = None, setHideSchedulePriorToCalendarDays = None, setIsFamilyInformationApprovalWorkflowUpdated = None, setIsStudentInformationApprovalWorkflowUpdated = None, setPhoneTypeIDToDisplayFamilyStudentAccess = None, setRankMethodIDFamilyAccessReportCardGrading = None, setRankMethodIDFamilyAccessReportCardStudent = None, setReportCardGPADisplay = None, setReportCardGPADisplayCode = None, setReportCardHeaderAddressType = None, setReportCardHeaderAddressTypeCode = None, setReportCardStudentRankDisplay = None, setReportCardStudentRankDisplayCode = None, setSchoolYearID = None, setRelationships = None, returnConfigEntityGroupYearID = True, returnChangeRequestFamilyEmail = False, returnChangeRequestFamilyEmailCode = False, returnChangeRequestFamilyPhone = False, returnChangeRequestFamilyPhoneCode = False, returnChangeRequestStudentEmail = False, returnChangeRequestStudentEmailCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDefaultFeeManagementOnlinePaymentAccess = False, returnDefaultFeeManagementOnlinePaymentAccessCode = False, returnDefaultFoodServiceOnlinePaymentAccess = False, returnDefaultFoodServiceOnlinePaymentAccessCode = False, returnDisplayAssignments = False, returnDisplayCalendarEvents = False, returnDisplayDistrictActivityEvents = False, returnDisplayStudentActivityEvents = False, returnEmailTypeIDToDisplayFamilyStudentAccess = False, returnEndorsementSignatureOption = False, returnEndorsementSignatureOptionCode = False, returnEndorsementSignatureStatement = False, returnEntityGroupKey = False, returnEntityID = False, returnFamilyAccessAccountInfoEmailBody = False, returnFamilyAccessAccountInfoEmailIncludeResetPasswordText = False, returnFamilyAccessAccountInfoEmailSubject = False, returnFamilyAccessCareerPlanDisplayShowDroppedCourses = False, returnFamilyAccessDisplayCommentCodes = False, returnFamilyAccessDisplayFreeFormComments = False, returnFamilyAccessDisplayGradeBucketsAfterEndDate = False, returnFamilyAccessDisplayHonorRoll = False, returnFamilyAccessDisplayOnlyCurrentAndCompleteGrades = False, returnFamilyAccessDisplayOnlyCurrentMissingAssignments = False, returnFamilyAccessDisplayShowActualEarnedCredits = False, returnFamilyAccessDisplayShowAttendance = False, returnFamilyAccessDisplayShowDroppedCourses = False, returnFamilyAccessDisplayShowEndedAttendanceTerms = False, returnFamilyAccessDisplayShowPossibleEarnedCredits = False, returnFamilyAccessDisplayStudentAddress = False, returnFamilyAccessDisplayStudentRank = False, returnFamilyAccessDisplayUseReportCardGradeBucketSettings = False, returnFamilyAccessLinkStudentSectionsOnReportCard = False, returnFamilyStudentAccessDisplayTeacherEmail = False, returnFamilyStudentAccessDisplayTeacherPhoneNumber = False, returnHideScheduleMessage = False, returnHideSchedulePriorToCalendarDays = False, returnIsFamilyInformationApprovalWorkflowUpdated = False, returnIsStudentInformationApprovalWorkflowUpdated = False, returnModifiedTime = False, returnPhoneTypeIDToDisplayFamilyStudentAccess = False, returnRankMethodIDFamilyAccessReportCardGrading = False, returnRankMethodIDFamilyAccessReportCardStudent = False, returnReportCardGPADisplay = False, returnReportCardGPADisplayCode = False, returnReportCardHeaderAddressType = False, returnReportCardHeaderAddressTypeCode = False, returnReportCardStudentRankDisplay = False, returnReportCardStudentRankDisplayCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigEntityGroupYear(EntityID = 1, setChangeRequestFamilyEmail = None, setChangeRequestFamilyEmailCode = None, setChangeRequestFamilyPhone = None, setChangeRequestFamilyPhoneCode = None, setChangeRequestStudentEmail = None, setChangeRequestStudentEmailCode = None, setConfigEntityGroupYearIDClonedFrom = None, setDefaultFeeManagementOnlinePaymentAccess = None, setDefaultFeeManagementOnlinePaymentAccessCode = None, setDefaultFoodServiceOnlinePaymentAccess = None, setDefaultFoodServiceOnlinePaymentAccessCode = None, setDisplayAssignments = None, setDisplayCalendarEvents = None, setDisplayDistrictActivityEvents = None, setDisplayStudentActivityEvents = None, setEmailTypeIDToDisplayFamilyStudentAccess = None, setEndorsementSignatureOption = None, setEndorsementSignatureOptionCode = None, setEndorsementSignatureStatement = None, setEntityGroupKey = None, setEntityID = None, setFamilyAccessAccountInfoEmailBody = None, setFamilyAccessAccountInfoEmailIncludeResetPasswordText = None, setFamilyAccessAccountInfoEmailSubject = None, setFamilyAccessCareerPlanDisplayShowDroppedCourses = None, setFamilyAccessDisplayCommentCodes = None, setFamilyAccessDisplayFreeFormComments = None, setFamilyAccessDisplayGradeBucketsAfterEndDate = None, setFamilyAccessDisplayHonorRoll = None, setFamilyAccessDisplayOnlyCurrentAndCompleteGrades = None, setFamilyAccessDisplayOnlyCurrentMissingAssignments = None, setFamilyAccessDisplayShowActualEarnedCredits = None, setFamilyAccessDisplayShowAttendance = None, setFamilyAccessDisplayShowDroppedCourses = None, setFamilyAccessDisplayShowEndedAttendanceTerms = None, setFamilyAccessDisplayShowPossibleEarnedCredits = None, setFamilyAccessDisplayStudentAddress = None, setFamilyAccessDisplayStudentRank = None, setFamilyAccessDisplayUseReportCardGradeBucketSettings = None, setFamilyAccessLinkStudentSectionsOnReportCard = None, setFamilyStudentAccessDisplayTeacherEmail = None, setFamilyStudentAccessDisplayTeacherPhoneNumber = None, setHideScheduleMessage = None, setHideSchedulePriorToCalendarDays = None, setIsFamilyInformationApprovalWorkflowUpdated = None, setIsStudentInformationApprovalWorkflowUpdated = None, setPhoneTypeIDToDisplayFamilyStudentAccess = None, setRankMethodIDFamilyAccessReportCardGrading = None, setRankMethodIDFamilyAccessReportCardStudent = None, setReportCardGPADisplay = None, setReportCardGPADisplayCode = None, setReportCardHeaderAddressType = None, setReportCardHeaderAddressTypeCode = None, setReportCardStudentRankDisplay = None, setReportCardStudentRankDisplayCode = None, setSchoolYearID = None, setRelationships = None, returnConfigEntityGroupYearID = True, returnChangeRequestFamilyEmail = False, returnChangeRequestFamilyEmailCode = False, returnChangeRequestFamilyPhone = False, returnChangeRequestFamilyPhoneCode = False, returnChangeRequestStudentEmail = False, returnChangeRequestStudentEmailCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDefaultFeeManagementOnlinePaymentAccess = False, returnDefaultFeeManagementOnlinePaymentAccessCode = False, returnDefaultFoodServiceOnlinePaymentAccess = False, returnDefaultFoodServiceOnlinePaymentAccessCode = False, returnDisplayAssignments = False, returnDisplayCalendarEvents = False, returnDisplayDistrictActivityEvents = False, returnDisplayStudentActivityEvents = False, returnEmailTypeIDToDisplayFamilyStudentAccess = False, returnEndorsementSignatureOption = False, returnEndorsementSignatureOptionCode = False, returnEndorsementSignatureStatement = False, returnEntityGroupKey = False, returnEntityID = False, returnFamilyAccessAccountInfoEmailBody = False, returnFamilyAccessAccountInfoEmailIncludeResetPasswordText = False, returnFamilyAccessAccountInfoEmailSubject = False, returnFamilyAccessCareerPlanDisplayShowDroppedCourses = False, returnFamilyAccessDisplayCommentCodes = False, returnFamilyAccessDisplayFreeFormComments = False, returnFamilyAccessDisplayGradeBucketsAfterEndDate = False, returnFamilyAccessDisplayHonorRoll = False, returnFamilyAccessDisplayOnlyCurrentAndCompleteGrades = False, returnFamilyAccessDisplayOnlyCurrentMissingAssignments = False, returnFamilyAccessDisplayShowActualEarnedCredits = False, returnFamilyAccessDisplayShowAttendance = False, returnFamilyAccessDisplayShowDroppedCourses = False, returnFamilyAccessDisplayShowEndedAttendanceTerms = False, returnFamilyAccessDisplayShowPossibleEarnedCredits = False, returnFamilyAccessDisplayStudentAddress = False, returnFamilyAccessDisplayStudentRank = False, returnFamilyAccessDisplayUseReportCardGradeBucketSettings = False, returnFamilyAccessLinkStudentSectionsOnReportCard = False, returnFamilyStudentAccessDisplayTeacherEmail = False, returnFamilyStudentAccessDisplayTeacherPhoneNumber = False, returnHideScheduleMessage = False, returnHideSchedulePriorToCalendarDays = False, returnIsFamilyInformationApprovalWorkflowUpdated = False, returnIsStudentInformationApprovalWorkflowUpdated = False, returnModifiedTime = False, returnPhoneTypeIDToDisplayFamilyStudentAccess = False, returnRankMethodIDFamilyAccessReportCardGrading = False, returnRankMethodIDFamilyAccessReportCardStudent = False, returnReportCardGPADisplay = False, returnReportCardGPADisplayCode = False, returnReportCardHeaderAddressType = False, returnReportCardHeaderAddressTypeCode = False, returnReportCardStudentRankDisplay = False, returnReportCardStudentRankDisplayCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigEntityGroupYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigSystem(EntityID = 1, page = 1, pageSize = 100, returnConfigSystemID = True, returnAddressValidationMessage = False, returnAllowFamilyAccessDefault = False, returnAllowOutOfRangeAddressesToSubmit = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnEnableAddressValidation = False, returnEnableNewStudentEnrollment = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigSystem(ConfigSystemID, EntityID = 1, returnConfigSystemID = True, returnAddressValidationMessage = False, returnAllowFamilyAccessDefault = False, returnAllowOutOfRangeAddressesToSubmit = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnEnableAddressValidation = False, returnEnableNewStudentEnrollment = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigSystem/" + str(ConfigSystemID), verb = "get", return_params_list = return_params_list)

def modifyConfigSystem(ConfigSystemID, EntityID = 1, setAddressValidationMessage = None, setAllowFamilyAccessDefault = None, setAllowOutOfRangeAddressesToSubmit = None, setAutoGenerateSecurityUser = None, setAutoGenerateSecurityUserCode = None, setEnableAddressValidation = None, setEnableNewStudentEnrollment = None, setRelationships = None, returnConfigSystemID = True, returnAddressValidationMessage = False, returnAllowFamilyAccessDefault = False, returnAllowOutOfRangeAddressesToSubmit = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnEnableAddressValidation = False, returnEnableNewStudentEnrollment = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigSystem/" + str(ConfigSystemID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigSystem(EntityID = 1, setAddressValidationMessage = None, setAllowFamilyAccessDefault = None, setAllowOutOfRangeAddressesToSubmit = None, setAutoGenerateSecurityUser = None, setAutoGenerateSecurityUserCode = None, setEnableAddressValidation = None, setEnableNewStudentEnrollment = None, setRelationships = None, returnConfigSystemID = True, returnAddressValidationMessage = False, returnAllowFamilyAccessDefault = False, returnAllowOutOfRangeAddressesToSubmit = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnEnableAddressValidation = False, returnEnableNewStudentEnrollment = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigSystem/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigSystem(ConfigSystemID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryFamily(EntityID = 1, page = 1, pageSize = 100, returnFamilyID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnHasStudentInSpecificDistrict = False, returnLanguageIDHome = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/Family/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getFamily(FamilyID, EntityID = 1, returnFamilyID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnHasStudentInSpecificDistrict = False, returnLanguageIDHome = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/Family/" + str(FamilyID), verb = "get", return_params_list = return_params_list)

def modifyFamily(FamilyID, EntityID = 1, setLanguageIDHome = None, setRelationships = None, returnFamilyID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnHasStudentInSpecificDistrict = False, returnLanguageIDHome = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/Family/" + str(FamilyID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createFamily(EntityID = 1, setLanguageIDHome = None, setRelationships = None, returnFamilyID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnHasStudentInSpecificDistrict = False, returnLanguageIDHome = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/Family/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteFamily(FamilyID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryFamilyGuardian(EntityID = 1, page = 1, pageSize = 100, returnFamilyGuardianID = True, returnCreatedTime = False, returnFamilyID = False, returnHasActiveStudentGuardianRestrictedAccess = False, returnModifiedTime = False, returnNameID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/FamilyGuardian/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getFamilyGuardian(FamilyGuardianID, EntityID = 1, returnFamilyGuardianID = True, returnCreatedTime = False, returnFamilyID = False, returnHasActiveStudentGuardianRestrictedAccess = False, returnModifiedTime = False, returnNameID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/FamilyGuardian/" + str(FamilyGuardianID), verb = "get", return_params_list = return_params_list)

def modifyFamilyGuardian(FamilyGuardianID, EntityID = 1, setFamilyID = None, setNameID = None, setRank = None, setRelationships = None, returnFamilyGuardianID = True, returnCreatedTime = False, returnFamilyID = False, returnHasActiveStudentGuardianRestrictedAccess = False, returnModifiedTime = False, returnNameID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/FamilyGuardian/" + str(FamilyGuardianID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createFamilyGuardian(EntityID = 1, setFamilyID = None, setNameID = None, setRank = None, setRelationships = None, returnFamilyGuardianID = True, returnCreatedTime = False, returnFamilyID = False, returnHasActiveStudentGuardianRestrictedAccess = False, returnModifiedTime = False, returnNameID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/FamilyGuardian/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteFamilyGuardian(FamilyGuardianID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentFamily(EntityID = 1, page = 1, pageSize = 100, returnStudentFamilyID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnFamilyID = False, returnHasEmployeeGuardian = False, returnIsEmergencyContact = False, returnIsPrimaryEmergencyContact = False, returnModifiedTime = False, returnRank = False, returnReceivesForms = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentFamily/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentFamily(StudentFamilyID, EntityID = 1, returnStudentFamilyID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnFamilyID = False, returnHasEmployeeGuardian = False, returnIsEmergencyContact = False, returnIsPrimaryEmergencyContact = False, returnModifiedTime = False, returnRank = False, returnReceivesForms = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentFamily/" + str(StudentFamilyID), verb = "get", return_params_list = return_params_list)

def modifyStudentFamily(StudentFamilyID, EntityID = 1, setFamilyID = None, setRank = None, setReceivesForms = None, setStudentID = None, setRelationships = None, returnStudentFamilyID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnFamilyID = False, returnHasEmployeeGuardian = False, returnIsEmergencyContact = False, returnIsPrimaryEmergencyContact = False, returnModifiedTime = False, returnRank = False, returnReceivesForms = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentFamily/" + str(StudentFamilyID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentFamily(EntityID = 1, setFamilyID = None, setRank = None, setReceivesForms = None, setStudentID = None, setRelationships = None, returnStudentFamilyID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnFamilyID = False, returnHasEmployeeGuardian = False, returnIsEmergencyContact = False, returnIsPrimaryEmergencyContact = False, returnModifiedTime = False, returnRank = False, returnReceivesForms = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentFamily/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentFamily(StudentFamilyID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentGuardian(EntityID = 1, page = 1, pageSize = 100, returnStudentGuardianID = True, returnAllowFamilyAccess = False, returnAllowStudentPickup = False, returnCreatedTime = False, returnFeeOnlinePaymentOverrideType = False, returnFeeOnlinePaymentOverrideTypeCode = False, returnFoodOnlinePaymentOverrideType = False, returnFoodOnlinePaymentOverrideTypeCode = False, returnGuardianCategory = False, returnGuardianNameIDAndFamilyID = False, returnHasActiveRestrictedAccess = False, returnHasUnrestrictedAccess = False, returnIsCustodialGuardian = False, returnIsEmergencyContact = False, returnModifiedTime = False, returnNameIDGuardian = False, returnNeedsSecurityGroupAudit = False, returnOverrideFeeOnlinePaymentAccess = False, returnOverrideFoodOnlinePaymentAccess = False, returnRank = False, returnRelationshipID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardian/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentGuardian(StudentGuardianID, EntityID = 1, returnStudentGuardianID = True, returnAllowFamilyAccess = False, returnAllowStudentPickup = False, returnCreatedTime = False, returnFeeOnlinePaymentOverrideType = False, returnFeeOnlinePaymentOverrideTypeCode = False, returnFoodOnlinePaymentOverrideType = False, returnFoodOnlinePaymentOverrideTypeCode = False, returnGuardianCategory = False, returnGuardianNameIDAndFamilyID = False, returnHasActiveRestrictedAccess = False, returnHasUnrestrictedAccess = False, returnIsCustodialGuardian = False, returnIsEmergencyContact = False, returnModifiedTime = False, returnNameIDGuardian = False, returnNeedsSecurityGroupAudit = False, returnOverrideFeeOnlinePaymentAccess = False, returnOverrideFoodOnlinePaymentAccess = False, returnRank = False, returnRelationshipID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardian/" + str(StudentGuardianID), verb = "get", return_params_list = return_params_list)

def modifyStudentGuardian(StudentGuardianID, EntityID = 1, setAllowFamilyAccess = None, setAllowStudentPickup = None, setFeeOnlinePaymentOverrideType = None, setFeeOnlinePaymentOverrideTypeCode = None, setFoodOnlinePaymentOverrideType = None, setFoodOnlinePaymentOverrideTypeCode = None, setIsCustodialGuardian = None, setNameIDGuardian = None, setOverrideFeeOnlinePaymentAccess = None, setOverrideFoodOnlinePaymentAccess = None, setRelationshipID = None, setStudentID = None, setRelationships = None, returnStudentGuardianID = True, returnAllowFamilyAccess = False, returnAllowStudentPickup = False, returnCreatedTime = False, returnFeeOnlinePaymentOverrideType = False, returnFeeOnlinePaymentOverrideTypeCode = False, returnFoodOnlinePaymentOverrideType = False, returnFoodOnlinePaymentOverrideTypeCode = False, returnGuardianCategory = False, returnGuardianNameIDAndFamilyID = False, returnHasActiveRestrictedAccess = False, returnHasUnrestrictedAccess = False, returnIsCustodialGuardian = False, returnIsEmergencyContact = False, returnModifiedTime = False, returnNameIDGuardian = False, returnNeedsSecurityGroupAudit = False, returnOverrideFeeOnlinePaymentAccess = False, returnOverrideFoodOnlinePaymentAccess = False, returnRank = False, returnRelationshipID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardian/" + str(StudentGuardianID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentGuardian(EntityID = 1, setAllowFamilyAccess = None, setAllowStudentPickup = None, setFeeOnlinePaymentOverrideType = None, setFeeOnlinePaymentOverrideTypeCode = None, setFoodOnlinePaymentOverrideType = None, setFoodOnlinePaymentOverrideTypeCode = None, setIsCustodialGuardian = None, setNameIDGuardian = None, setOverrideFeeOnlinePaymentAccess = None, setOverrideFoodOnlinePaymentAccess = None, setRelationshipID = None, setStudentID = None, setRelationships = None, returnStudentGuardianID = True, returnAllowFamilyAccess = False, returnAllowStudentPickup = False, returnCreatedTime = False, returnFeeOnlinePaymentOverrideType = False, returnFeeOnlinePaymentOverrideTypeCode = False, returnFoodOnlinePaymentOverrideType = False, returnFoodOnlinePaymentOverrideTypeCode = False, returnGuardianCategory = False, returnGuardianNameIDAndFamilyID = False, returnHasActiveRestrictedAccess = False, returnHasUnrestrictedAccess = False, returnIsCustodialGuardian = False, returnIsEmergencyContact = False, returnModifiedTime = False, returnNameIDGuardian = False, returnNeedsSecurityGroupAudit = False, returnOverrideFeeOnlinePaymentAccess = False, returnOverrideFoodOnlinePaymentAccess = False, returnRank = False, returnRelationshipID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardian/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentGuardian(StudentGuardianID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentGuardianRestrictedAccess(EntityID = 1, page = 1, pageSize = 100, returnStudentGuardianRestrictedAccessID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnReason = False, returnStartDate = False, returnStudentGuardianID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardianRestrictedAccess/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentGuardianRestrictedAccess(StudentGuardianRestrictedAccessID, EntityID = 1, returnStudentGuardianRestrictedAccessID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnReason = False, returnStartDate = False, returnStudentGuardianID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardianRestrictedAccess/" + str(StudentGuardianRestrictedAccessID), verb = "get", return_params_list = return_params_list)

def modifyStudentGuardianRestrictedAccess(StudentGuardianRestrictedAccessID, EntityID = 1, setEndDate = None, setReason = None, setStartDate = None, setStudentGuardianID = None, setRelationships = None, returnStudentGuardianRestrictedAccessID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnReason = False, returnStartDate = False, returnStudentGuardianID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardianRestrictedAccess/" + str(StudentGuardianRestrictedAccessID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentGuardianRestrictedAccess(EntityID = 1, setEndDate = None, setReason = None, setStartDate = None, setStudentGuardianID = None, setRelationships = None, returnStudentGuardianRestrictedAccessID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnReason = False, returnStartDate = False, returnStudentGuardianID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardianRestrictedAccess/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentGuardianRestrictedAccess(StudentGuardianRestrictedAccessID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempFamilyGuardian(EntityID = 1, page = 1, pageSize = 100, returnTempFamilyGuardianID = True, returnCreatedTime = False, returnGuardianNameID = False, returnGuardianNameLFM = False, returnIsFamilyAccessUser = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/TempFamilyGuardian/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempFamilyGuardian(TempFamilyGuardianID, EntityID = 1, returnTempFamilyGuardianID = True, returnCreatedTime = False, returnGuardianNameID = False, returnGuardianNameLFM = False, returnIsFamilyAccessUser = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/TempFamilyGuardian/" + str(TempFamilyGuardianID), verb = "get", return_params_list = return_params_list)

def modifyTempFamilyGuardian(TempFamilyGuardianID, EntityID = 1, setGuardianNameID = None, setGuardianNameLFM = None, setIsFamilyAccessUser = None, setRelationships = None, returnTempFamilyGuardianID = True, returnCreatedTime = False, returnGuardianNameID = False, returnGuardianNameLFM = False, returnIsFamilyAccessUser = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/TempFamilyGuardian/" + str(TempFamilyGuardianID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempFamilyGuardian(EntityID = 1, setGuardianNameID = None, setGuardianNameLFM = None, setIsFamilyAccessUser = None, setRelationships = None, returnTempFamilyGuardianID = True, returnCreatedTime = False, returnGuardianNameID = False, returnGuardianNameLFM = False, returnIsFamilyAccessUser = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/TempFamilyGuardian/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempFamilyGuardian(TempFamilyGuardianID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")