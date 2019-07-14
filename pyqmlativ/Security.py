# This module contains Security functions.

from .Utilities import make_request

import pandas as pd

import json

import re

def getEveryAuthenticationAssertion(EntityID = 1, page = 1, pageSize = 100, returnAuthenticationAssertionID = True, returnAssertionGuid = False, returnAuthenticationMethodID = False, returnCreatedTime = False, returnMobileDevice = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationAssertion/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAuthenticationAssertion(AuthenticationAssertionID, EntityID = 1, returnAuthenticationAssertionID = True, returnAssertionGuid = False, returnAuthenticationMethodID = False, returnCreatedTime = False, returnMobileDevice = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationAssertion/" + str(AuthenticationAssertionID), verb = "get", return_params_list = return_params_list)

def modifyAuthenticationAssertion(AuthenticationAssertionID, EntityID = 1, setAssertionGuid = None, setAuthenticationMethodID = None, setMobileDevice = None, setRelationships = None, returnAuthenticationAssertionID = True, returnAssertionGuid = False, returnAuthenticationMethodID = False, returnCreatedTime = False, returnMobileDevice = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationAssertion/" + str(AuthenticationAssertionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAuthenticationAssertion(EntityID = 1, setAssertionGuid = None, setAuthenticationMethodID = None, setMobileDevice = None, setRelationships = None, returnAuthenticationAssertionID = True, returnAssertionGuid = False, returnAuthenticationMethodID = False, returnCreatedTime = False, returnMobileDevice = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationAssertion/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAuthenticationAssertion(AuthenticationAssertionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAuthenticationMethod(EntityID = 1, page = 1, pageSize = 100, returnAuthenticationMethodID = True, returnCertificate = False, returnCompareNameIDAsNumeric = False, returnCreatedTime = False, returnIsSkywardMaintained = False, returnMetadata = False, returnMetadataURL = False, returnModifiedTime = False, returnName = False, returnNameIdentifierSkywardField = False, returnNameIdentifierSkywardFieldFriendlyName = False, returnNameIdentifierType = False, returnSkywardHash = False, returnSkywardID = False, returnSSOURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAuthenticationMethod(AuthenticationMethodID, EntityID = 1, returnAuthenticationMethodID = True, returnCertificate = False, returnCompareNameIDAsNumeric = False, returnCreatedTime = False, returnIsSkywardMaintained = False, returnMetadata = False, returnMetadataURL = False, returnModifiedTime = False, returnName = False, returnNameIdentifierSkywardField = False, returnNameIdentifierSkywardFieldFriendlyName = False, returnNameIdentifierType = False, returnSkywardHash = False, returnSkywardID = False, returnSSOURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationMethod/" + str(AuthenticationMethodID), verb = "get", return_params_list = return_params_list)

def modifyAuthenticationMethod(AuthenticationMethodID, EntityID = 1, setCertificate = None, setCompareNameIDAsNumeric = None, setIsSkywardMaintained = None, setMetadata = None, setMetadataURL = None, setName = None, setNameIdentifierSkywardField = None, setNameIdentifierType = None, setSkywardHash = None, setSkywardID = None, setSSOURL = None, setRelationships = None, returnAuthenticationMethodID = True, returnCertificate = False, returnCompareNameIDAsNumeric = False, returnCreatedTime = False, returnIsSkywardMaintained = False, returnMetadata = False, returnMetadataURL = False, returnModifiedTime = False, returnName = False, returnNameIdentifierSkywardField = False, returnNameIdentifierSkywardFieldFriendlyName = False, returnNameIdentifierType = False, returnSkywardHash = False, returnSkywardID = False, returnSSOURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationMethod/" + str(AuthenticationMethodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAuthenticationMethod(EntityID = 1, setCertificate = None, setCompareNameIDAsNumeric = None, setIsSkywardMaintained = None, setMetadata = None, setMetadataURL = None, setName = None, setNameIdentifierSkywardField = None, setNameIdentifierType = None, setSkywardHash = None, setSkywardID = None, setSSOURL = None, setRelationships = None, returnAuthenticationMethodID = True, returnCertificate = False, returnCompareNameIDAsNumeric = False, returnCreatedTime = False, returnIsSkywardMaintained = False, returnMetadata = False, returnMetadataURL = False, returnModifiedTime = False, returnName = False, returnNameIdentifierSkywardField = False, returnNameIdentifierSkywardFieldFriendlyName = False, returnNameIdentifierType = False, returnSkywardHash = False, returnSkywardID = False, returnSSOURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationMethod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAuthenticationMethod(AuthenticationMethodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAuthenticationRole(EntityID = 1, page = 1, pageSize = 100, returnAuthenticationRoleID = True, returnAllowSkywardCredentials = False, returnCreatedTime = False, returnDisplayText = False, returnHasAuthenticationMethod = False, returnHasLDAPProvider = False, returnMediaID = False, returnModifiedTime = False, returnName = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRole/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAuthenticationRole(AuthenticationRoleID, EntityID = 1, returnAuthenticationRoleID = True, returnAllowSkywardCredentials = False, returnCreatedTime = False, returnDisplayText = False, returnHasAuthenticationMethod = False, returnHasLDAPProvider = False, returnMediaID = False, returnModifiedTime = False, returnName = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRole/" + str(AuthenticationRoleID), verb = "get", return_params_list = return_params_list)

def modifyAuthenticationRole(AuthenticationRoleID, EntityID = 1, setAllowSkywardCredentials = None, setDisplayText = None, setMediaID = None, setName = None, setPriority = None, setRelationships = None, returnAuthenticationRoleID = True, returnAllowSkywardCredentials = False, returnCreatedTime = False, returnDisplayText = False, returnHasAuthenticationMethod = False, returnHasLDAPProvider = False, returnMediaID = False, returnModifiedTime = False, returnName = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRole/" + str(AuthenticationRoleID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAuthenticationRole(EntityID = 1, setAllowSkywardCredentials = None, setDisplayText = None, setMediaID = None, setName = None, setPriority = None, setRelationships = None, returnAuthenticationRoleID = True, returnAllowSkywardCredentials = False, returnCreatedTime = False, returnDisplayText = False, returnHasAuthenticationMethod = False, returnHasLDAPProvider = False, returnMediaID = False, returnModifiedTime = False, returnName = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRole/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAuthenticationRole(AuthenticationRoleID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAuthenticationRoleLDAPProvider(EntityID = 1, page = 1, pageSize = 100, returnAuthenticationRoleLDAPProviderID = True, returnAuthenticationRoleID = False, returnCreatedTime = False, returnLDAPProviderID = False, returnModifiedTime = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRoleLDAPProvider/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAuthenticationRoleLDAPProvider(AuthenticationRoleLDAPProviderID, EntityID = 1, returnAuthenticationRoleLDAPProviderID = True, returnAuthenticationRoleID = False, returnCreatedTime = False, returnLDAPProviderID = False, returnModifiedTime = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRoleLDAPProvider/" + str(AuthenticationRoleLDAPProviderID), verb = "get", return_params_list = return_params_list)

def modifyAuthenticationRoleLDAPProvider(AuthenticationRoleLDAPProviderID, EntityID = 1, setAuthenticationRoleID = None, setLDAPProviderID = None, setPriority = None, setRelationships = None, returnAuthenticationRoleLDAPProviderID = True, returnAuthenticationRoleID = False, returnCreatedTime = False, returnLDAPProviderID = False, returnModifiedTime = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRoleLDAPProvider/" + str(AuthenticationRoleLDAPProviderID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAuthenticationRoleLDAPProvider(EntityID = 1, setAuthenticationRoleID = None, setLDAPProviderID = None, setPriority = None, setRelationships = None, returnAuthenticationRoleLDAPProviderID = True, returnAuthenticationRoleID = False, returnCreatedTime = False, returnLDAPProviderID = False, returnModifiedTime = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRoleLDAPProvider/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAuthenticationRoleLDAPProvider(AuthenticationRoleLDAPProviderID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAuthenticationRoleMethod(EntityID = 1, page = 1, pageSize = 100, returnAuthenticationRoleMethodID = True, returnAuthenticationMethodID = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRoleMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAuthenticationRoleMethod(AuthenticationRoleMethodID, EntityID = 1, returnAuthenticationRoleMethodID = True, returnAuthenticationMethodID = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRoleMethod/" + str(AuthenticationRoleMethodID), verb = "get", return_params_list = return_params_list)

def modifyAuthenticationRoleMethod(AuthenticationRoleMethodID, EntityID = 1, setAuthenticationMethodID = None, setAuthenticationRoleID = None, setDisplayOrder = None, setRelationships = None, returnAuthenticationRoleMethodID = True, returnAuthenticationMethodID = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRoleMethod/" + str(AuthenticationRoleMethodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAuthenticationRoleMethod(EntityID = 1, setAuthenticationMethodID = None, setAuthenticationRoleID = None, setDisplayOrder = None, setRelationships = None, returnAuthenticationRoleMethodID = True, returnAuthenticationMethodID = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRoleMethod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAuthenticationRoleMethod(AuthenticationRoleMethodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryBrowseFieldPath(EntityID = 1, page = 1, pageSize = 100, returnBrowseFieldPathID = True, returnBrowseID = False, returnCreatedTime = False, returnFieldPath = False, returnGuidFieldPath = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnRoleID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/BrowseFieldPath/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getBrowseFieldPath(BrowseFieldPathID, EntityID = 1, returnBrowseFieldPathID = True, returnBrowseID = False, returnCreatedTime = False, returnFieldPath = False, returnGuidFieldPath = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnRoleID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/BrowseFieldPath/" + str(BrowseFieldPathID), verb = "get", return_params_list = return_params_list)

def modifyBrowseFieldPath(BrowseFieldPathID, EntityID = 1, setBrowseID = None, setFieldPath = None, setGuidFieldPath = None, setRoleID = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnBrowseFieldPathID = True, returnBrowseID = False, returnCreatedTime = False, returnFieldPath = False, returnGuidFieldPath = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnRoleID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/BrowseFieldPath/" + str(BrowseFieldPathID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createBrowseFieldPath(EntityID = 1, setBrowseID = None, setFieldPath = None, setGuidFieldPath = None, setRoleID = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnBrowseFieldPathID = True, returnBrowseID = False, returnCreatedTime = False, returnFieldPath = False, returnGuidFieldPath = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnRoleID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/BrowseFieldPath/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteBrowseFieldPath(BrowseFieldPathID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigSystem(EntityID = 1, page = 1, pageSize = 100, returnConfigSystemID = True, returnAccessCodeLength = False, returnAdminEmployeeTeacherActivityAllowUsernameChange = False, returnAdminMissedSessionPingCountLimit = False, returnAdminSessionClientPingSeconds = False, returnAdminSessionTimeoutSeconds = False, returnAdminSessionWarnSeconds = False, returnAuthenticationRoleIDActivity = False, returnAuthenticationRoleIDAdministrative = False, returnAuthenticationRoleIDEmployee = False, returnAuthenticationRoleIDFamilyNewStudentEnrollment = False, returnAuthenticationRoleIDStudent = False, returnAuthenticationRoleIDTeacher = False, returnAutogenerateEmployeeAccessCodes = False, returnAutogenerateStaffAccessCodes = False, returnAutogenerateStudentAccessCodes = False, returnCombineAuthenticationRolesOnSignIn = False, returnCreatedTime = False, returnDaysUntilPasswordExpires = False, returnFailedSignInCountLimit = False, returnFamilyAllowUsernameChange = False, returnFamilyStudentEmployeeMissedSessionPingCountLimit = False, returnFamilyStudentEmployeeSessionClientPingSeconds = False, returnFamilyStudentEmployeeSessionTimeoutSeconds = False, returnFamilyStudentEmployeeSessionWarnSeconds = False, returnForcePasswordExpirationOnSkywardLoginIfPasswordRequirementsNotMet = False, returnLoginLockRetryDelayMinutes = False, returnMaximumPasswordLength = False, returnMinimumPasswordLength = False, returnModifiedTime = False, returnMultifactorAuthenticationIDActivity = False, returnMultifactorAuthenticationIDAdministrative = False, returnMultifactorAuthenticationIDEmployee = False, returnMultifactorAuthenticationIDFamilyNewStudentEnrollment = False, returnMultifactorAuthenticationIDStudent = False, returnMultifactorAuthenticationIDTeacher = False, returnRequiredNumericCharacters = False, returnRequiredSpecialCharacters = False, returnSessionAccessDeniedLimit = False, returnStudentAllowUsernameChange = False, returnTeacherMissedSessionPingCountLimit = False, returnTeacherSessionClientPingSeconds = False, returnTeacherSessionTimeoutSeconds = False, returnTeacherSessionWarnSeconds = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportChangeThreshold = False, returnUserImportDeleteThreshold = False, returnUserImportFilePath = False, returnUserImportFileType = False, returnUserImportFileTypeCode = False, returnUserImportShouldMaintainExistingUsers = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigSystem(ConfigSystemID, EntityID = 1, returnConfigSystemID = True, returnAccessCodeLength = False, returnAdminEmployeeTeacherActivityAllowUsernameChange = False, returnAdminMissedSessionPingCountLimit = False, returnAdminSessionClientPingSeconds = False, returnAdminSessionTimeoutSeconds = False, returnAdminSessionWarnSeconds = False, returnAuthenticationRoleIDActivity = False, returnAuthenticationRoleIDAdministrative = False, returnAuthenticationRoleIDEmployee = False, returnAuthenticationRoleIDFamilyNewStudentEnrollment = False, returnAuthenticationRoleIDStudent = False, returnAuthenticationRoleIDTeacher = False, returnAutogenerateEmployeeAccessCodes = False, returnAutogenerateStaffAccessCodes = False, returnAutogenerateStudentAccessCodes = False, returnCombineAuthenticationRolesOnSignIn = False, returnCreatedTime = False, returnDaysUntilPasswordExpires = False, returnFailedSignInCountLimit = False, returnFamilyAllowUsernameChange = False, returnFamilyStudentEmployeeMissedSessionPingCountLimit = False, returnFamilyStudentEmployeeSessionClientPingSeconds = False, returnFamilyStudentEmployeeSessionTimeoutSeconds = False, returnFamilyStudentEmployeeSessionWarnSeconds = False, returnForcePasswordExpirationOnSkywardLoginIfPasswordRequirementsNotMet = False, returnLoginLockRetryDelayMinutes = False, returnMaximumPasswordLength = False, returnMinimumPasswordLength = False, returnModifiedTime = False, returnMultifactorAuthenticationIDActivity = False, returnMultifactorAuthenticationIDAdministrative = False, returnMultifactorAuthenticationIDEmployee = False, returnMultifactorAuthenticationIDFamilyNewStudentEnrollment = False, returnMultifactorAuthenticationIDStudent = False, returnMultifactorAuthenticationIDTeacher = False, returnRequiredNumericCharacters = False, returnRequiredSpecialCharacters = False, returnSessionAccessDeniedLimit = False, returnStudentAllowUsernameChange = False, returnTeacherMissedSessionPingCountLimit = False, returnTeacherSessionClientPingSeconds = False, returnTeacherSessionTimeoutSeconds = False, returnTeacherSessionWarnSeconds = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportChangeThreshold = False, returnUserImportDeleteThreshold = False, returnUserImportFilePath = False, returnUserImportFileType = False, returnUserImportFileTypeCode = False, returnUserImportShouldMaintainExistingUsers = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ConfigSystem/" + str(ConfigSystemID), verb = "get", return_params_list = return_params_list)

def modifyConfigSystem(ConfigSystemID, EntityID = 1, setAccessCodeLength = None, setAdminEmployeeTeacherActivityAllowUsernameChange = None, setAdminMissedSessionPingCountLimit = None, setAdminSessionClientPingSeconds = None, setAdminSessionTimeoutSeconds = None, setAdminSessionWarnSeconds = None, setAuthenticationRoleIDActivity = None, setAuthenticationRoleIDAdministrative = None, setAuthenticationRoleIDEmployee = None, setAuthenticationRoleIDFamilyNewStudentEnrollment = None, setAuthenticationRoleIDStudent = None, setAuthenticationRoleIDTeacher = None, setAutogenerateEmployeeAccessCodes = None, setAutogenerateStaffAccessCodes = None, setAutogenerateStudentAccessCodes = None, setCombineAuthenticationRolesOnSignIn = None, setDaysUntilPasswordExpires = None, setFailedSignInCountLimit = None, setFamilyAllowUsernameChange = None, setFamilyStudentEmployeeMissedSessionPingCountLimit = None, setFamilyStudentEmployeeSessionClientPingSeconds = None, setFamilyStudentEmployeeSessionTimeoutSeconds = None, setFamilyStudentEmployeeSessionWarnSeconds = None, setForcePasswordExpirationOnSkywardLoginIfPasswordRequirementsNotMet = None, setLoginLockRetryDelayMinutes = None, setMaximumPasswordLength = None, setMinimumPasswordLength = None, setMultifactorAuthenticationIDActivity = None, setMultifactorAuthenticationIDAdministrative = None, setMultifactorAuthenticationIDEmployee = None, setMultifactorAuthenticationIDFamilyNewStudentEnrollment = None, setMultifactorAuthenticationIDStudent = None, setMultifactorAuthenticationIDTeacher = None, setRequiredNumericCharacters = None, setRequiredSpecialCharacters = None, setSessionAccessDeniedLimit = None, setStudentAllowUsernameChange = None, setTeacherMissedSessionPingCountLimit = None, setTeacherSessionClientPingSeconds = None, setTeacherSessionTimeoutSeconds = None, setTeacherSessionWarnSeconds = None, setUserImportChangeThreshold = None, setUserImportDeleteThreshold = None, setUserImportFilePath = None, setUserImportFileType = None, setUserImportFileTypeCode = None, setUserImportShouldMaintainExistingUsers = None, setRelationships = None, returnConfigSystemID = True, returnAccessCodeLength = False, returnAdminEmployeeTeacherActivityAllowUsernameChange = False, returnAdminMissedSessionPingCountLimit = False, returnAdminSessionClientPingSeconds = False, returnAdminSessionTimeoutSeconds = False, returnAdminSessionWarnSeconds = False, returnAuthenticationRoleIDActivity = False, returnAuthenticationRoleIDAdministrative = False, returnAuthenticationRoleIDEmployee = False, returnAuthenticationRoleIDFamilyNewStudentEnrollment = False, returnAuthenticationRoleIDStudent = False, returnAuthenticationRoleIDTeacher = False, returnAutogenerateEmployeeAccessCodes = False, returnAutogenerateStaffAccessCodes = False, returnAutogenerateStudentAccessCodes = False, returnCombineAuthenticationRolesOnSignIn = False, returnCreatedTime = False, returnDaysUntilPasswordExpires = False, returnFailedSignInCountLimit = False, returnFamilyAllowUsernameChange = False, returnFamilyStudentEmployeeMissedSessionPingCountLimit = False, returnFamilyStudentEmployeeSessionClientPingSeconds = False, returnFamilyStudentEmployeeSessionTimeoutSeconds = False, returnFamilyStudentEmployeeSessionWarnSeconds = False, returnForcePasswordExpirationOnSkywardLoginIfPasswordRequirementsNotMet = False, returnLoginLockRetryDelayMinutes = False, returnMaximumPasswordLength = False, returnMinimumPasswordLength = False, returnModifiedTime = False, returnMultifactorAuthenticationIDActivity = False, returnMultifactorAuthenticationIDAdministrative = False, returnMultifactorAuthenticationIDEmployee = False, returnMultifactorAuthenticationIDFamilyNewStudentEnrollment = False, returnMultifactorAuthenticationIDStudent = False, returnMultifactorAuthenticationIDTeacher = False, returnRequiredNumericCharacters = False, returnRequiredSpecialCharacters = False, returnSessionAccessDeniedLimit = False, returnStudentAllowUsernameChange = False, returnTeacherMissedSessionPingCountLimit = False, returnTeacherSessionClientPingSeconds = False, returnTeacherSessionTimeoutSeconds = False, returnTeacherSessionWarnSeconds = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportChangeThreshold = False, returnUserImportDeleteThreshold = False, returnUserImportFilePath = False, returnUserImportFileType = False, returnUserImportFileTypeCode = False, returnUserImportShouldMaintainExistingUsers = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ConfigSystem/" + str(ConfigSystemID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigSystem(EntityID = 1, setAccessCodeLength = None, setAdminEmployeeTeacherActivityAllowUsernameChange = None, setAdminMissedSessionPingCountLimit = None, setAdminSessionClientPingSeconds = None, setAdminSessionTimeoutSeconds = None, setAdminSessionWarnSeconds = None, setAuthenticationRoleIDActivity = None, setAuthenticationRoleIDAdministrative = None, setAuthenticationRoleIDEmployee = None, setAuthenticationRoleIDFamilyNewStudentEnrollment = None, setAuthenticationRoleIDStudent = None, setAuthenticationRoleIDTeacher = None, setAutogenerateEmployeeAccessCodes = None, setAutogenerateStaffAccessCodes = None, setAutogenerateStudentAccessCodes = None, setCombineAuthenticationRolesOnSignIn = None, setDaysUntilPasswordExpires = None, setFailedSignInCountLimit = None, setFamilyAllowUsernameChange = None, setFamilyStudentEmployeeMissedSessionPingCountLimit = None, setFamilyStudentEmployeeSessionClientPingSeconds = None, setFamilyStudentEmployeeSessionTimeoutSeconds = None, setFamilyStudentEmployeeSessionWarnSeconds = None, setForcePasswordExpirationOnSkywardLoginIfPasswordRequirementsNotMet = None, setLoginLockRetryDelayMinutes = None, setMaximumPasswordLength = None, setMinimumPasswordLength = None, setMultifactorAuthenticationIDActivity = None, setMultifactorAuthenticationIDAdministrative = None, setMultifactorAuthenticationIDEmployee = None, setMultifactorAuthenticationIDFamilyNewStudentEnrollment = None, setMultifactorAuthenticationIDStudent = None, setMultifactorAuthenticationIDTeacher = None, setRequiredNumericCharacters = None, setRequiredSpecialCharacters = None, setSessionAccessDeniedLimit = None, setStudentAllowUsernameChange = None, setTeacherMissedSessionPingCountLimit = None, setTeacherSessionClientPingSeconds = None, setTeacherSessionTimeoutSeconds = None, setTeacherSessionWarnSeconds = None, setUserImportChangeThreshold = None, setUserImportDeleteThreshold = None, setUserImportFilePath = None, setUserImportFileType = None, setUserImportFileTypeCode = None, setUserImportShouldMaintainExistingUsers = None, setRelationships = None, returnConfigSystemID = True, returnAccessCodeLength = False, returnAdminEmployeeTeacherActivityAllowUsernameChange = False, returnAdminMissedSessionPingCountLimit = False, returnAdminSessionClientPingSeconds = False, returnAdminSessionTimeoutSeconds = False, returnAdminSessionWarnSeconds = False, returnAuthenticationRoleIDActivity = False, returnAuthenticationRoleIDAdministrative = False, returnAuthenticationRoleIDEmployee = False, returnAuthenticationRoleIDFamilyNewStudentEnrollment = False, returnAuthenticationRoleIDStudent = False, returnAuthenticationRoleIDTeacher = False, returnAutogenerateEmployeeAccessCodes = False, returnAutogenerateStaffAccessCodes = False, returnAutogenerateStudentAccessCodes = False, returnCombineAuthenticationRolesOnSignIn = False, returnCreatedTime = False, returnDaysUntilPasswordExpires = False, returnFailedSignInCountLimit = False, returnFamilyAllowUsernameChange = False, returnFamilyStudentEmployeeMissedSessionPingCountLimit = False, returnFamilyStudentEmployeeSessionClientPingSeconds = False, returnFamilyStudentEmployeeSessionTimeoutSeconds = False, returnFamilyStudentEmployeeSessionWarnSeconds = False, returnForcePasswordExpirationOnSkywardLoginIfPasswordRequirementsNotMet = False, returnLoginLockRetryDelayMinutes = False, returnMaximumPasswordLength = False, returnMinimumPasswordLength = False, returnModifiedTime = False, returnMultifactorAuthenticationIDActivity = False, returnMultifactorAuthenticationIDAdministrative = False, returnMultifactorAuthenticationIDEmployee = False, returnMultifactorAuthenticationIDFamilyNewStudentEnrollment = False, returnMultifactorAuthenticationIDStudent = False, returnMultifactorAuthenticationIDTeacher = False, returnRequiredNumericCharacters = False, returnRequiredSpecialCharacters = False, returnSessionAccessDeniedLimit = False, returnStudentAllowUsernameChange = False, returnTeacherMissedSessionPingCountLimit = False, returnTeacherSessionClientPingSeconds = False, returnTeacherSessionTimeoutSeconds = False, returnTeacherSessionWarnSeconds = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportChangeThreshold = False, returnUserImportDeleteThreshold = False, returnUserImportFilePath = False, returnUserImportFileType = False, returnUserImportFileTypeCode = False, returnUserImportShouldMaintainExistingUsers = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ConfigSystem/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigSystem(ConfigSystemID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDataObjectFieldPath(EntityID = 1, page = 1, pageSize = 100, returnDataObjectFieldPathID = True, returnCreatedTime = False, returnDisplayLevel = False, returnExactSystemTypeName = False, returnField = False, returnFieldIDSkySys = False, returnFieldPath = False, returnFriendlyName = False, returnGuidFieldPath = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnNumberOfRelationships = False, returnObjectID = False, returnObjectSchemaObject = False, returnRoleID = False, returnSkywardDisplayLevel = False, returnSkywardDisplayLevelCode = False, returnSkywardFriendlyName = False, returnSkywardHash = False, returnSkywardID = False, returnUserDisplayLevel = False, returnUserDisplayLevelCode = False, returnUserFriendlyName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/DataObjectFieldPath/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDataObjectFieldPath(DataObjectFieldPathID, EntityID = 1, returnDataObjectFieldPathID = True, returnCreatedTime = False, returnDisplayLevel = False, returnExactSystemTypeName = False, returnField = False, returnFieldIDSkySys = False, returnFieldPath = False, returnFriendlyName = False, returnGuidFieldPath = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnNumberOfRelationships = False, returnObjectID = False, returnObjectSchemaObject = False, returnRoleID = False, returnSkywardDisplayLevel = False, returnSkywardDisplayLevelCode = False, returnSkywardFriendlyName = False, returnSkywardHash = False, returnSkywardID = False, returnUserDisplayLevel = False, returnUserDisplayLevelCode = False, returnUserFriendlyName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/DataObjectFieldPath/" + str(DataObjectFieldPathID), verb = "get", return_params_list = return_params_list)

def modifyDataObjectFieldPath(DataObjectFieldPathID, EntityID = 1, setFieldIDSkySys = None, setFieldPath = None, setGuidFieldPath = None, setObjectID = None, setRoleID = None, setSkywardDisplayLevel = None, setSkywardDisplayLevelCode = None, setSkywardFriendlyName = None, setSkywardHash = None, setSkywardID = None, setUserDisplayLevel = None, setUserDisplayLevelCode = None, setUserFriendlyName = None, setRelationships = None, returnDataObjectFieldPathID = True, returnCreatedTime = False, returnDisplayLevel = False, returnExactSystemTypeName = False, returnField = False, returnFieldIDSkySys = False, returnFieldPath = False, returnFriendlyName = False, returnGuidFieldPath = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnNumberOfRelationships = False, returnObjectID = False, returnObjectSchemaObject = False, returnRoleID = False, returnSkywardDisplayLevel = False, returnSkywardDisplayLevelCode = False, returnSkywardFriendlyName = False, returnSkywardHash = False, returnSkywardID = False, returnUserDisplayLevel = False, returnUserDisplayLevelCode = False, returnUserFriendlyName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/DataObjectFieldPath/" + str(DataObjectFieldPathID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDataObjectFieldPath(EntityID = 1, setFieldIDSkySys = None, setFieldPath = None, setGuidFieldPath = None, setObjectID = None, setRoleID = None, setSkywardDisplayLevel = None, setSkywardDisplayLevelCode = None, setSkywardFriendlyName = None, setSkywardHash = None, setSkywardID = None, setUserDisplayLevel = None, setUserDisplayLevelCode = None, setUserFriendlyName = None, setRelationships = None, returnDataObjectFieldPathID = True, returnCreatedTime = False, returnDisplayLevel = False, returnExactSystemTypeName = False, returnField = False, returnFieldIDSkySys = False, returnFieldPath = False, returnFriendlyName = False, returnGuidFieldPath = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnNumberOfRelationships = False, returnObjectID = False, returnObjectSchemaObject = False, returnRoleID = False, returnSkywardDisplayLevel = False, returnSkywardDisplayLevelCode = False, returnSkywardFriendlyName = False, returnSkywardHash = False, returnSkywardID = False, returnUserDisplayLevel = False, returnUserDisplayLevelCode = False, returnUserFriendlyName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/DataObjectFieldPath/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDataObjectFieldPath(DataObjectFieldPathID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDeniedField(EntityID = 1, page = 1, pageSize = 100, returnDeniedFieldID = True, returnCreatedTime = False, returnFieldID = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/DeniedField/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDeniedField(DeniedFieldID, EntityID = 1, returnDeniedFieldID = True, returnCreatedTime = False, returnFieldID = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/DeniedField/" + str(DeniedFieldID), verb = "get", return_params_list = return_params_list)

def modifyDeniedField(DeniedFieldID, EntityID = 1, setFieldID = None, setIsSkywardDefined = None, setRoleID = None, setRelationships = None, returnDeniedFieldID = True, returnCreatedTime = False, returnFieldID = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/DeniedField/" + str(DeniedFieldID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDeniedField(EntityID = 1, setFieldID = None, setIsSkywardDefined = None, setRoleID = None, setRelationships = None, returnDeniedFieldID = True, returnCreatedTime = False, returnFieldID = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/DeniedField/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDeniedField(DeniedFieldID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryElectronicSignature(EntityID = 1, page = 1, pageSize = 100, returnElectronicSignatureID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEntityID = False, returnEntityName = False, returnIsForGrading = False, returnIsForPurchasing = False, returnIsForStateReporting = False, returnMediaID = False, returnModifiedTime = False, returnSignatureLocationKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ElectronicSignature/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getElectronicSignature(ElectronicSignatureID, EntityID = 1, returnElectronicSignatureID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEntityID = False, returnEntityName = False, returnIsForGrading = False, returnIsForPurchasing = False, returnIsForStateReporting = False, returnMediaID = False, returnModifiedTime = False, returnSignatureLocationKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ElectronicSignature/" + str(ElectronicSignatureID), verb = "get", return_params_list = return_params_list)

def modifyElectronicSignature(ElectronicSignatureID, EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setEntityID = None, setIsForGrading = None, setIsForPurchasing = None, setIsForStateReporting = None, setMediaID = None, setRelationships = None, returnElectronicSignatureID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEntityID = False, returnEntityName = False, returnIsForGrading = False, returnIsForPurchasing = False, returnIsForStateReporting = False, returnMediaID = False, returnModifiedTime = False, returnSignatureLocationKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ElectronicSignature/" + str(ElectronicSignatureID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createElectronicSignature(EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setEntityID = None, setIsForGrading = None, setIsForPurchasing = None, setIsForStateReporting = None, setMediaID = None, setRelationships = None, returnElectronicSignatureID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEntityID = False, returnEntityName = False, returnIsForGrading = False, returnIsForPurchasing = False, returnIsForStateReporting = False, returnMediaID = False, returnModifiedTime = False, returnSignatureLocationKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ElectronicSignature/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteElectronicSignature(ElectronicSignatureID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryFieldRestriction(EntityID = 1, page = 1, pageSize = 100, returnFieldRestrictionID = True, returnCreatedTime = False, returnFieldID = False, returnModifiedTime = False, returnName = False, returnRestrictionType = False, returnRestrictionTypeCode = False, returnRoleSetType = False, returnRoleSetTypeCode = False, returnRoleSetTypeRequiresRoles = False, returnScreenSetType = False, returnScreenSetTypeCode = False, returnScreenSetTypeRequiresScreens = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestriction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getFieldRestriction(FieldRestrictionID, EntityID = 1, returnFieldRestrictionID = True, returnCreatedTime = False, returnFieldID = False, returnModifiedTime = False, returnName = False, returnRestrictionType = False, returnRestrictionTypeCode = False, returnRoleSetType = False, returnRoleSetTypeCode = False, returnRoleSetTypeRequiresRoles = False, returnScreenSetType = False, returnScreenSetTypeCode = False, returnScreenSetTypeRequiresScreens = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestriction/" + str(FieldRestrictionID), verb = "get", return_params_list = return_params_list)

def modifyFieldRestriction(FieldRestrictionID, EntityID = 1, setFieldID = None, setName = None, setRestrictionType = None, setRestrictionTypeCode = None, setRoleSetType = None, setRoleSetTypeCode = None, setScreenSetType = None, setScreenSetTypeCode = None, setRelationships = None, returnFieldRestrictionID = True, returnCreatedTime = False, returnFieldID = False, returnModifiedTime = False, returnName = False, returnRestrictionType = False, returnRestrictionTypeCode = False, returnRoleSetType = False, returnRoleSetTypeCode = False, returnRoleSetTypeRequiresRoles = False, returnScreenSetType = False, returnScreenSetTypeCode = False, returnScreenSetTypeRequiresScreens = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestriction/" + str(FieldRestrictionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createFieldRestriction(EntityID = 1, setFieldID = None, setName = None, setRestrictionType = None, setRestrictionTypeCode = None, setRoleSetType = None, setRoleSetTypeCode = None, setScreenSetType = None, setScreenSetTypeCode = None, setRelationships = None, returnFieldRestrictionID = True, returnCreatedTime = False, returnFieldID = False, returnModifiedTime = False, returnName = False, returnRestrictionType = False, returnRestrictionTypeCode = False, returnRoleSetType = False, returnRoleSetTypeCode = False, returnRoleSetTypeRequiresRoles = False, returnScreenSetType = False, returnScreenSetTypeCode = False, returnScreenSetTypeRequiresScreens = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestriction/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteFieldRestriction(FieldRestrictionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryFieldRestrictionRole(EntityID = 1, page = 1, pageSize = 100, returnFieldRestrictionRoleID = True, returnCreatedTime = False, returnFieldRestrictionID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestrictionRole/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getFieldRestrictionRole(FieldRestrictionRoleID, EntityID = 1, returnFieldRestrictionRoleID = True, returnCreatedTime = False, returnFieldRestrictionID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestrictionRole/" + str(FieldRestrictionRoleID), verb = "get", return_params_list = return_params_list)

def modifyFieldRestrictionRole(FieldRestrictionRoleID, EntityID = 1, setFieldRestrictionID = None, setRoleID = None, setRelationships = None, returnFieldRestrictionRoleID = True, returnCreatedTime = False, returnFieldRestrictionID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestrictionRole/" + str(FieldRestrictionRoleID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createFieldRestrictionRole(EntityID = 1, setFieldRestrictionID = None, setRoleID = None, setRelationships = None, returnFieldRestrictionRoleID = True, returnCreatedTime = False, returnFieldRestrictionID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestrictionRole/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteFieldRestrictionRole(FieldRestrictionRoleID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryFieldRestrictionScreen(EntityID = 1, page = 1, pageSize = 100, returnFieldRestrictionScreenID = True, returnCreatedTime = False, returnFieldRestrictionID = False, returnModifiedTime = False, returnSecurityLocationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestrictionScreen/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getFieldRestrictionScreen(FieldRestrictionScreenID, EntityID = 1, returnFieldRestrictionScreenID = True, returnCreatedTime = False, returnFieldRestrictionID = False, returnModifiedTime = False, returnSecurityLocationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestrictionScreen/" + str(FieldRestrictionScreenID), verb = "get", return_params_list = return_params_list)

def modifyFieldRestrictionScreen(FieldRestrictionScreenID, EntityID = 1, setFieldRestrictionID = None, setSecurityLocationID = None, setRelationships = None, returnFieldRestrictionScreenID = True, returnCreatedTime = False, returnFieldRestrictionID = False, returnModifiedTime = False, returnSecurityLocationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestrictionScreen/" + str(FieldRestrictionScreenID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createFieldRestrictionScreen(EntityID = 1, setFieldRestrictionID = None, setSecurityLocationID = None, setRelationships = None, returnFieldRestrictionScreenID = True, returnCreatedTime = False, returnFieldRestrictionID = False, returnModifiedTime = False, returnSecurityLocationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestrictionScreen/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteFieldRestrictionScreen(FieldRestrictionScreenID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGroup(EntityID = 1, page = 1, pageSize = 100, returnGroupID = True, returnAutoAddToUserType = False, returnAutoAddToUserTypeCode = False, returnCreatedTime = False, returnDescription = False, returnEdFiStaffClassificationID = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnPositionTitleOverride = False, returnUsedForEmployeeAccess = False, returnUsedForFamilyAccess = False, returnUsedForNewStudentEnrollment = False, returnUsedForStudentAccess = False, returnUsedForTeacherAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Group/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGroup(GroupID, EntityID = 1, returnGroupID = True, returnAutoAddToUserType = False, returnAutoAddToUserTypeCode = False, returnCreatedTime = False, returnDescription = False, returnEdFiStaffClassificationID = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnPositionTitleOverride = False, returnUsedForEmployeeAccess = False, returnUsedForFamilyAccess = False, returnUsedForNewStudentEnrollment = False, returnUsedForStudentAccess = False, returnUsedForTeacherAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Group/" + str(GroupID), verb = "get", return_params_list = return_params_list)

def modifyGroup(GroupID, EntityID = 1, setAutoAddToUserType = None, setAutoAddToUserTypeCode = None, setDescription = None, setEdFiStaffClassificationID = None, setIsActive = None, setName = None, setPositionTitleOverride = None, setRelationships = None, returnGroupID = True, returnAutoAddToUserType = False, returnAutoAddToUserTypeCode = False, returnCreatedTime = False, returnDescription = False, returnEdFiStaffClassificationID = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnPositionTitleOverride = False, returnUsedForEmployeeAccess = False, returnUsedForFamilyAccess = False, returnUsedForNewStudentEnrollment = False, returnUsedForStudentAccess = False, returnUsedForTeacherAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Group/" + str(GroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGroup(EntityID = 1, setAutoAddToUserType = None, setAutoAddToUserTypeCode = None, setDescription = None, setEdFiStaffClassificationID = None, setIsActive = None, setName = None, setPositionTitleOverride = None, setRelationships = None, returnGroupID = True, returnAutoAddToUserType = False, returnAutoAddToUserTypeCode = False, returnCreatedTime = False, returnDescription = False, returnEdFiStaffClassificationID = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnPositionTitleOverride = False, returnUsedForEmployeeAccess = False, returnUsedForFamilyAccess = False, returnUsedForNewStudentEnrollment = False, returnUsedForStudentAccess = False, returnUsedForTeacherAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Group/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGroup(GroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGroupEntityAutoAdd(EntityID = 1, page = 1, pageSize = 100, returnGroupEntityAutoAddID = True, returnCreatedTime = False, returnEntityID = False, returnGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupEntityAutoAdd/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGroupEntityAutoAdd(GroupEntityAutoAddID, EntityID = 1, returnGroupEntityAutoAddID = True, returnCreatedTime = False, returnEntityID = False, returnGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupEntityAutoAdd/" + str(GroupEntityAutoAddID), verb = "get", return_params_list = return_params_list)

def modifyGroupEntityAutoAdd(GroupEntityAutoAddID, EntityID = 1, setEntityID = None, setGroupID = None, setRelationships = None, returnGroupEntityAutoAddID = True, returnCreatedTime = False, returnEntityID = False, returnGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupEntityAutoAdd/" + str(GroupEntityAutoAddID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGroupEntityAutoAdd(EntityID = 1, setEntityID = None, setGroupID = None, setRelationships = None, returnGroupEntityAutoAddID = True, returnCreatedTime = False, returnEntityID = False, returnGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupEntityAutoAdd/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGroupEntityAutoAdd(GroupEntityAutoAddID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGroupImpersonationRole(EntityID = 1, page = 1, pageSize = 100, returnGroupImpersonationRoleID = True, returnCreatedTime = False, returnGroupID = False, returnIsReadOnly = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupImpersonationRole/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGroupImpersonationRole(GroupImpersonationRoleID, EntityID = 1, returnGroupImpersonationRoleID = True, returnCreatedTime = False, returnGroupID = False, returnIsReadOnly = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupImpersonationRole/" + str(GroupImpersonationRoleID), verb = "get", return_params_list = return_params_list)

def modifyGroupImpersonationRole(GroupImpersonationRoleID, EntityID = 1, setGroupID = None, setIsReadOnly = None, setRoleID = None, setRelationships = None, returnGroupImpersonationRoleID = True, returnCreatedTime = False, returnGroupID = False, returnIsReadOnly = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupImpersonationRole/" + str(GroupImpersonationRoleID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGroupImpersonationRole(EntityID = 1, setGroupID = None, setIsReadOnly = None, setRoleID = None, setRelationships = None, returnGroupImpersonationRoleID = True, returnCreatedTime = False, returnGroupID = False, returnIsReadOnly = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupImpersonationRole/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGroupImpersonationRole(GroupImpersonationRoleID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGroupLDAPSynchronization(EntityID = 1, page = 1, pageSize = 100, returnGroupLDAPSynchronizationID = True, returnCommonName = False, returnCreatedTime = False, returnDistinguishedName = False, returnEntityID = False, returnGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupLDAPSynchronization/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGroupLDAPSynchronization(GroupLDAPSynchronizationID, EntityID = 1, returnGroupLDAPSynchronizationID = True, returnCommonName = False, returnCreatedTime = False, returnDistinguishedName = False, returnEntityID = False, returnGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupLDAPSynchronization/" + str(GroupLDAPSynchronizationID), verb = "get", return_params_list = return_params_list)

def modifyGroupLDAPSynchronization(GroupLDAPSynchronizationID, EntityID = 1, setCommonName = None, setDistinguishedName = None, setEntityID = None, setGroupID = None, setRelationships = None, returnGroupLDAPSynchronizationID = True, returnCommonName = False, returnCreatedTime = False, returnDistinguishedName = False, returnEntityID = False, returnGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupLDAPSynchronization/" + str(GroupLDAPSynchronizationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGroupLDAPSynchronization(EntityID = 1, setCommonName = None, setDistinguishedName = None, setEntityID = None, setGroupID = None, setRelationships = None, returnGroupLDAPSynchronizationID = True, returnCommonName = False, returnCreatedTime = False, returnDistinguishedName = False, returnEntityID = False, returnGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupLDAPSynchronization/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGroupLDAPSynchronization(GroupLDAPSynchronizationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGroupMembership(EntityID = 1, page = 1, pageSize = 100, returnGroupMembershipID = True, returnCreatedTime = False, returnEntityID = False, returnExternalUniqueIdentifier = False, returnGroupIDParent = False, returnMembershipSource = False, returnMembershipSourceCode = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDMember = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupMembership/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGroupMembership(GroupMembershipID, EntityID = 1, returnGroupMembershipID = True, returnCreatedTime = False, returnEntityID = False, returnExternalUniqueIdentifier = False, returnGroupIDParent = False, returnMembershipSource = False, returnMembershipSourceCode = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDMember = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupMembership/" + str(GroupMembershipID), verb = "get", return_params_list = return_params_list)

def modifyGroupMembership(GroupMembershipID, EntityID = 1, setEntityID = None, setExternalUniqueIdentifier = None, setGroupIDParent = None, setMembershipSource = None, setMembershipSourceCode = None, setUserIDMember = None, setRelationships = None, returnGroupMembershipID = True, returnCreatedTime = False, returnEntityID = False, returnExternalUniqueIdentifier = False, returnGroupIDParent = False, returnMembershipSource = False, returnMembershipSourceCode = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDMember = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupMembership/" + str(GroupMembershipID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGroupMembership(EntityID = 1, setEntityID = None, setExternalUniqueIdentifier = None, setGroupIDParent = None, setMembershipSource = None, setMembershipSourceCode = None, setUserIDMember = None, setRelationships = None, returnGroupMembershipID = True, returnCreatedTime = False, returnEntityID = False, returnExternalUniqueIdentifier = False, returnGroupIDParent = False, returnMembershipSource = False, returnMembershipSourceCode = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDMember = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupMembership/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGroupMembership(GroupMembershipID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGroupRole(EntityID = 1, page = 1, pageSize = 100, returnGroupRoleID = True, returnCreatedTime = False, returnGroupID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupRole/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGroupRole(GroupRoleID, EntityID = 1, returnGroupRoleID = True, returnCreatedTime = False, returnGroupID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupRole/" + str(GroupRoleID), verb = "get", return_params_list = return_params_list)

def modifyGroupRole(GroupRoleID, EntityID = 1, setGroupID = None, setRoleID = None, setRelationships = None, returnGroupRoleID = True, returnCreatedTime = False, returnGroupID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupRole/" + str(GroupRoleID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGroupRole(EntityID = 1, setGroupID = None, setRoleID = None, setRelationships = None, returnGroupRoleID = True, returnCreatedTime = False, returnGroupID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupRole/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGroupRole(GroupRoleID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryImpersonation(EntityID = 1, page = 1, pageSize = 100, returnImpersonationID = True, returnCreatedTime = False, returnImpersonationEnded = False, returnImpersonationStarted = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDImpersonated = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Impersonation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getImpersonation(ImpersonationID, EntityID = 1, returnImpersonationID = True, returnCreatedTime = False, returnImpersonationEnded = False, returnImpersonationStarted = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDImpersonated = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Impersonation/" + str(ImpersonationID), verb = "get", return_params_list = return_params_list)

def modifyImpersonation(ImpersonationID, EntityID = 1, setImpersonationEnded = None, setUserIDImpersonated = None, setUserIDImpersonator = None, setRelationships = None, returnImpersonationID = True, returnCreatedTime = False, returnImpersonationEnded = False, returnImpersonationStarted = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDImpersonated = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Impersonation/" + str(ImpersonationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createImpersonation(EntityID = 1, setImpersonationEnded = None, setUserIDImpersonated = None, setUserIDImpersonator = None, setRelationships = None, returnImpersonationID = True, returnCreatedTime = False, returnImpersonationEnded = False, returnImpersonationStarted = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDImpersonated = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Impersonation/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteImpersonation(ImpersonationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryIPRange(EntityID = 1, page = 1, pageSize = 100, returnIPRangeID = True, returnCreatedTime = False, returnDescription = False, returnHigh = False, returnIPAddressHigh = False, returnIPAddressLow = False, returnLow = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/IPRange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getIPRange(IPRangeID, EntityID = 1, returnIPRangeID = True, returnCreatedTime = False, returnDescription = False, returnHigh = False, returnIPAddressHigh = False, returnIPAddressLow = False, returnLow = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/IPRange/" + str(IPRangeID), verb = "get", return_params_list = return_params_list)

def modifyIPRange(IPRangeID, EntityID = 1, setDescription = None, setHigh = None, setLow = None, setRelationships = None, returnIPRangeID = True, returnCreatedTime = False, returnDescription = False, returnHigh = False, returnIPAddressHigh = False, returnIPAddressLow = False, returnLow = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/IPRange/" + str(IPRangeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createIPRange(EntityID = 1, setDescription = None, setHigh = None, setLow = None, setRelationships = None, returnIPRangeID = True, returnCreatedTime = False, returnDescription = False, returnHigh = False, returnIPAddressHigh = False, returnIPAddressLow = False, returnLow = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/IPRange/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteIPRange(IPRangeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryLDAPGroup(EntityID = 1, page = 1, pageSize = 100, returnLDAPGroupID = True, returnCommonName = False, returnCreatedTime = False, returnDistinguishedName = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/LDAPGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getLDAPGroup(LDAPGroupID, EntityID = 1, returnLDAPGroupID = True, returnCommonName = False, returnCreatedTime = False, returnDistinguishedName = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/LDAPGroup/" + str(LDAPGroupID), verb = "get", return_params_list = return_params_list)

def modifyLDAPGroup(LDAPGroupID, EntityID = 1, setCommonName = None, setDistinguishedName = None, setRelationships = None, returnLDAPGroupID = True, returnCommonName = False, returnCreatedTime = False, returnDistinguishedName = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/LDAPGroup/" + str(LDAPGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createLDAPGroup(EntityID = 1, setCommonName = None, setDistinguishedName = None, setRelationships = None, returnLDAPGroupID = True, returnCommonName = False, returnCreatedTime = False, returnDistinguishedName = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/LDAPGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteLDAPGroup(LDAPGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryLDAPProvider(EntityID = 1, page = 1, pageSize = 100, returnLDAPProviderID = True, returnCreatedTime = False, returnDisableReferrals = False, returnDomainName = False, returnGroupBaseDN = False, returnGroupFilter = False, returnGroupMemberFilter = False, returnHost = False, returnIgnoreCertificationErrors = False, returnModifiedTime = False, returnName = False, returnPort = False, returnProtocol = False, returnProtocolCode = False, returnSearchBaseDN = False, returnSearchFilter = False, returnSearchPassword = False, returnSearchUserDN = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsernameAttribute = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/LDAPProvider/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getLDAPProvider(LDAPProviderID, EntityID = 1, returnLDAPProviderID = True, returnCreatedTime = False, returnDisableReferrals = False, returnDomainName = False, returnGroupBaseDN = False, returnGroupFilter = False, returnGroupMemberFilter = False, returnHost = False, returnIgnoreCertificationErrors = False, returnModifiedTime = False, returnName = False, returnPort = False, returnProtocol = False, returnProtocolCode = False, returnSearchBaseDN = False, returnSearchFilter = False, returnSearchPassword = False, returnSearchUserDN = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsernameAttribute = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/LDAPProvider/" + str(LDAPProviderID), verb = "get", return_params_list = return_params_list)

def modifyLDAPProvider(LDAPProviderID, EntityID = 1, setDisableReferrals = None, setDomainName = None, setGroupBaseDN = None, setGroupFilter = None, setGroupMemberFilter = None, setHost = None, setIgnoreCertificationErrors = None, setName = None, setPort = None, setProtocol = None, setProtocolCode = None, setSearchBaseDN = None, setSearchFilter = None, setSearchPassword = None, setSearchUserDN = None, setUsernameAttribute = None, setRelationships = None, returnLDAPProviderID = True, returnCreatedTime = False, returnDisableReferrals = False, returnDomainName = False, returnGroupBaseDN = False, returnGroupFilter = False, returnGroupMemberFilter = False, returnHost = False, returnIgnoreCertificationErrors = False, returnModifiedTime = False, returnName = False, returnPort = False, returnProtocol = False, returnProtocolCode = False, returnSearchBaseDN = False, returnSearchFilter = False, returnSearchPassword = False, returnSearchUserDN = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsernameAttribute = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/LDAPProvider/" + str(LDAPProviderID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createLDAPProvider(EntityID = 1, setDisableReferrals = None, setDomainName = None, setGroupBaseDN = None, setGroupFilter = None, setGroupMemberFilter = None, setHost = None, setIgnoreCertificationErrors = None, setName = None, setPort = None, setProtocol = None, setProtocolCode = None, setSearchBaseDN = None, setSearchFilter = None, setSearchPassword = None, setSearchUserDN = None, setUsernameAttribute = None, setRelationships = None, returnLDAPProviderID = True, returnCreatedTime = False, returnDisableReferrals = False, returnDomainName = False, returnGroupBaseDN = False, returnGroupFilter = False, returnGroupMemberFilter = False, returnHost = False, returnIgnoreCertificationErrors = False, returnModifiedTime = False, returnName = False, returnPort = False, returnProtocol = False, returnProtocolCode = False, returnSearchBaseDN = False, returnSearchFilter = False, returnSearchPassword = False, returnSearchUserDN = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsernameAttribute = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/LDAPProvider/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteLDAPProvider(LDAPProviderID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryMenuSecurityItem(EntityID = 1, page = 1, pageSize = 100, returnMenuSecurityItemID = True, returnCreatedTime = False, returnMenuScreenID = False, returnModifiedTime = False, returnProfileScreenID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MenuSecurityItem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getMenuSecurityItem(MenuSecurityItemID, EntityID = 1, returnMenuSecurityItemID = True, returnCreatedTime = False, returnMenuScreenID = False, returnModifiedTime = False, returnProfileScreenID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MenuSecurityItem/" + str(MenuSecurityItemID), verb = "get", return_params_list = return_params_list)

def modifyMenuSecurityItem(MenuSecurityItemID, EntityID = 1, setMenuScreenID = None, setProfileScreenID = None, setRelationships = None, returnMenuSecurityItemID = True, returnCreatedTime = False, returnMenuScreenID = False, returnModifiedTime = False, returnProfileScreenID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MenuSecurityItem/" + str(MenuSecurityItemID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createMenuSecurityItem(EntityID = 1, setMenuScreenID = None, setProfileScreenID = None, setRelationships = None, returnMenuSecurityItemID = True, returnCreatedTime = False, returnMenuScreenID = False, returnModifiedTime = False, returnProfileScreenID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MenuSecurityItem/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteMenuSecurityItem(MenuSecurityItemID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryMobileSSO(EntityID = 1, page = 1, pageSize = 100, returnMobileSSOID = True, returnCreatedTime = False, returnMobileDevice = False, returnModifiedTime = False, returnSSOToken = False, returnSSOTokenExpirationDate = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MobileSSO/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getMobileSSO(MobileSSOID, EntityID = 1, returnMobileSSOID = True, returnCreatedTime = False, returnMobileDevice = False, returnModifiedTime = False, returnSSOToken = False, returnSSOTokenExpirationDate = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MobileSSO/" + str(MobileSSOID), verb = "get", return_params_list = return_params_list)

def modifyMobileSSO(MobileSSOID, EntityID = 1, setMobileDevice = None, setSSOToken = None, setUserID = None, setRelationships = None, returnMobileSSOID = True, returnCreatedTime = False, returnMobileDevice = False, returnModifiedTime = False, returnSSOToken = False, returnSSOTokenExpirationDate = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MobileSSO/" + str(MobileSSOID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createMobileSSO(EntityID = 1, setMobileDevice = None, setSSOToken = None, setUserID = None, setRelationships = None, returnMobileSSOID = True, returnCreatedTime = False, returnMobileDevice = False, returnModifiedTime = False, returnSSOToken = False, returnSSOTokenExpirationDate = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MobileSSO/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteMobileSSO(MobileSSOID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryMultifactorAuthentication(EntityID = 1, page = 1, pageSize = 100, returnMultifactorAuthenticationID = True, returnCode = False, returnCreatedTime = False, returnDaysToExpiration = False, returnDescription = False, returnIsRequired = False, returnModifiedTime = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsesEmail = False, returnUsesSMS = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MultifactorAuthentication/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getMultifactorAuthentication(MultifactorAuthenticationID, EntityID = 1, returnMultifactorAuthenticationID = True, returnCode = False, returnCreatedTime = False, returnDaysToExpiration = False, returnDescription = False, returnIsRequired = False, returnModifiedTime = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsesEmail = False, returnUsesSMS = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MultifactorAuthentication/" + str(MultifactorAuthenticationID), verb = "get", return_params_list = return_params_list)

def modifyMultifactorAuthentication(MultifactorAuthenticationID, EntityID = 1, setCode = None, setDaysToExpiration = None, setDescription = None, setIsRequired = None, setPriority = None, setUsesEmail = None, setUsesSMS = None, setRelationships = None, returnMultifactorAuthenticationID = True, returnCode = False, returnCreatedTime = False, returnDaysToExpiration = False, returnDescription = False, returnIsRequired = False, returnModifiedTime = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsesEmail = False, returnUsesSMS = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MultifactorAuthentication/" + str(MultifactorAuthenticationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createMultifactorAuthentication(EntityID = 1, setCode = None, setDaysToExpiration = None, setDescription = None, setIsRequired = None, setPriority = None, setUsesEmail = None, setUsesSMS = None, setRelationships = None, returnMultifactorAuthenticationID = True, returnCode = False, returnCreatedTime = False, returnDaysToExpiration = False, returnDescription = False, returnIsRequired = False, returnModifiedTime = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsesEmail = False, returnUsesSMS = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MultifactorAuthentication/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteMultifactorAuthentication(MultifactorAuthenticationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryMultifactorAuthenticationAssertion(EntityID = 1, page = 1, pageSize = 100, returnMultifactorAuthenticationAssertionID = True, returnAssertionCode = False, returnAssertionIdentifier = False, returnCreatedTime = False, returnExpirationTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MultifactorAuthenticationAssertion/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getMultifactorAuthenticationAssertion(MultifactorAuthenticationAssertionID, EntityID = 1, returnMultifactorAuthenticationAssertionID = True, returnAssertionCode = False, returnAssertionIdentifier = False, returnCreatedTime = False, returnExpirationTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MultifactorAuthenticationAssertion/" + str(MultifactorAuthenticationAssertionID), verb = "get", return_params_list = return_params_list)

def modifyMultifactorAuthenticationAssertion(MultifactorAuthenticationAssertionID, EntityID = 1, setAssertionCode = None, setAssertionIdentifier = None, setUserID = None, setRelationships = None, returnMultifactorAuthenticationAssertionID = True, returnAssertionCode = False, returnAssertionIdentifier = False, returnCreatedTime = False, returnExpirationTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MultifactorAuthenticationAssertion/" + str(MultifactorAuthenticationAssertionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createMultifactorAuthenticationAssertion(EntityID = 1, setAssertionCode = None, setAssertionIdentifier = None, setUserID = None, setRelationships = None, returnMultifactorAuthenticationAssertionID = True, returnAssertionCode = False, returnAssertionIdentifier = False, returnCreatedTime = False, returnExpirationTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MultifactorAuthenticationAssertion/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteMultifactorAuthenticationAssertion(MultifactorAuthenticationAssertionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryProduct(EntityID = 1, page = 1, pageSize = 100, returnProductID = True, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnRMSID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Product/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getProduct(ProductID, EntityID = 1, returnProductID = True, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnRMSID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Product/" + str(ProductID), verb = "get", return_params_list = return_params_list)

def modifyProduct(ProductID, EntityID = 1, setName = None, setRMSID = None, setRelationships = None, returnProductID = True, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnRMSID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Product/" + str(ProductID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createProduct(EntityID = 1, setName = None, setRMSID = None, setRelationships = None, returnProductID = True, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnRMSID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Product/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteProduct(ProductID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryProductModulePath(EntityID = 1, page = 1, pageSize = 100, returnProductModulePathID = True, returnController = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnProductID = False, returnScreen = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ProductModulePath/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getProductModulePath(ProductModulePathID, EntityID = 1, returnProductModulePathID = True, returnController = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnProductID = False, returnScreen = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ProductModulePath/" + str(ProductModulePathID), verb = "get", return_params_list = return_params_list)

def modifyProductModulePath(ProductModulePathID, EntityID = 1, setController = None, setModule = None, setProductID = None, setScreen = None, setRelationships = None, returnProductModulePathID = True, returnController = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnProductID = False, returnScreen = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ProductModulePath/" + str(ProductModulePathID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createProductModulePath(EntityID = 1, setController = None, setModule = None, setProductID = None, setScreen = None, setRelationships = None, returnProductModulePathID = True, returnController = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnProductID = False, returnScreen = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ProductModulePath/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteProductModulePath(ProductModulePathID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryProductOwned(EntityID = 1, page = 1, pageSize = 100, returnProductOwnedID = True, returnCreatedTime = False, returnEndDate = False, returnExpirationDate = False, returnModifiedTime = False, returnProductID = False, returnRMSID = False, returnStartDate = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ProductOwned/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getProductOwned(ProductOwnedID, EntityID = 1, returnProductOwnedID = True, returnCreatedTime = False, returnEndDate = False, returnExpirationDate = False, returnModifiedTime = False, returnProductID = False, returnRMSID = False, returnStartDate = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ProductOwned/" + str(ProductOwnedID), verb = "get", return_params_list = return_params_list)

def modifyProductOwned(ProductOwnedID, EntityID = 1, setEndDate = None, setExpirationDate = None, setProductID = None, setRMSID = None, setStartDate = None, setRelationships = None, returnProductOwnedID = True, returnCreatedTime = False, returnEndDate = False, returnExpirationDate = False, returnModifiedTime = False, returnProductID = False, returnRMSID = False, returnStartDate = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ProductOwned/" + str(ProductOwnedID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createProductOwned(EntityID = 1, setEndDate = None, setExpirationDate = None, setProductID = None, setRMSID = None, setStartDate = None, setRelationships = None, returnProductOwnedID = True, returnCreatedTime = False, returnEndDate = False, returnExpirationDate = False, returnModifiedTime = False, returnProductID = False, returnRMSID = False, returnStartDate = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ProductOwned/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteProductOwned(ProductOwnedID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryRole(EntityID = 1, page = 1, pageSize = 100, returnRoleID = True, returnAuthenticationRoleID = False, returnCreatedTime = False, returnDescription = False, returnDocumentationPersona = False, returnDocumentationPersonaCode = False, returnIsActive = False, returnModifiedTime = False, returnMultifactorAuthenticationID = False, returnName = False, returnReportCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Role/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getRole(RoleID, EntityID = 1, returnRoleID = True, returnAuthenticationRoleID = False, returnCreatedTime = False, returnDescription = False, returnDocumentationPersona = False, returnDocumentationPersonaCode = False, returnIsActive = False, returnModifiedTime = False, returnMultifactorAuthenticationID = False, returnName = False, returnReportCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Role/" + str(RoleID), verb = "get", return_params_list = return_params_list)

def modifyRole(RoleID, EntityID = 1, setAuthenticationRoleID = None, setDescription = None, setDocumentationPersona = None, setDocumentationPersonaCode = None, setIsActive = None, setMultifactorAuthenticationID = None, setName = None, setRelationships = None, returnRoleID = True, returnAuthenticationRoleID = False, returnCreatedTime = False, returnDescription = False, returnDocumentationPersona = False, returnDocumentationPersonaCode = False, returnIsActive = False, returnModifiedTime = False, returnMultifactorAuthenticationID = False, returnName = False, returnReportCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Role/" + str(RoleID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createRole(EntityID = 1, setAuthenticationRoleID = None, setDescription = None, setDocumentationPersona = None, setDocumentationPersonaCode = None, setIsActive = None, setMultifactorAuthenticationID = None, setName = None, setRelationships = None, returnRoleID = True, returnAuthenticationRoleID = False, returnCreatedTime = False, returnDescription = False, returnDocumentationPersona = False, returnDocumentationPersonaCode = False, returnIsActive = False, returnModifiedTime = False, returnMultifactorAuthenticationID = False, returnName = False, returnReportCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Role/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteRole(RoleID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryRoleField(EntityID = 1, page = 1, pageSize = 100, returnRoleFieldID = True, returnAllowRead = False, returnCreatedTime = False, returnField = False, returnFullField = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleField/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getRoleField(RoleFieldID, EntityID = 1, returnRoleFieldID = True, returnAllowRead = False, returnCreatedTime = False, returnField = False, returnFullField = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleField/" + str(RoleFieldID), verb = "get", return_params_list = return_params_list)

def modifyRoleField(RoleFieldID, EntityID = 1, setAllowRead = None, setField = None, setModule = None, setObject = None, setRoleID = None, setRelationships = None, returnRoleFieldID = True, returnAllowRead = False, returnCreatedTime = False, returnField = False, returnFullField = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleField/" + str(RoleFieldID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createRoleField(EntityID = 1, setAllowRead = None, setField = None, setModule = None, setObject = None, setRoleID = None, setRelationships = None, returnRoleFieldID = True, returnAllowRead = False, returnCreatedTime = False, returnField = False, returnFullField = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleField/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteRoleField(RoleFieldID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryRoleIPRange(EntityID = 1, page = 1, pageSize = 100, returnRoleIPRangeID = True, returnCreatedTime = False, returnIPRangeID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleIPRange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getRoleIPRange(RoleIPRangeID, EntityID = 1, returnRoleIPRangeID = True, returnCreatedTime = False, returnIPRangeID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleIPRange/" + str(RoleIPRangeID), verb = "get", return_params_list = return_params_list)

def modifyRoleIPRange(RoleIPRangeID, EntityID = 1, setIPRangeID = None, setRoleID = None, setRelationships = None, returnRoleIPRangeID = True, returnCreatedTime = False, returnIPRangeID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleIPRange/" + str(RoleIPRangeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createRoleIPRange(EntityID = 1, setIPRangeID = None, setRoleID = None, setRelationships = None, returnRoleIPRangeID = True, returnCreatedTime = False, returnIPRangeID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleIPRange/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteRoleIPRange(RoleIPRangeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryRoleMenuSecurityItem(EntityID = 1, page = 1, pageSize = 100, returnRoleMenuSecurityItemID = True, returnAllowCreate = False, returnAllowDelete = False, returnAllowMassCreate = False, returnAllowMassDelete = False, returnAllowMassUpdate = False, returnAllowRead = False, returnAllowUpdate = False, returnCreatedTime = False, returnMenuSecurityItemID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleMenuSecurityItem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getRoleMenuSecurityItem(RoleMenuSecurityItemID, EntityID = 1, returnRoleMenuSecurityItemID = True, returnAllowCreate = False, returnAllowDelete = False, returnAllowMassCreate = False, returnAllowMassDelete = False, returnAllowMassUpdate = False, returnAllowRead = False, returnAllowUpdate = False, returnCreatedTime = False, returnMenuSecurityItemID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleMenuSecurityItem/" + str(RoleMenuSecurityItemID), verb = "get", return_params_list = return_params_list)

def modifyRoleMenuSecurityItem(RoleMenuSecurityItemID, EntityID = 1, setAllowCreate = None, setAllowDelete = None, setAllowMassCreate = None, setAllowMassDelete = None, setAllowMassUpdate = None, setAllowRead = None, setAllowUpdate = None, setMenuSecurityItemID = None, setRoleID = None, setRelationships = None, returnRoleMenuSecurityItemID = True, returnAllowCreate = False, returnAllowDelete = False, returnAllowMassCreate = False, returnAllowMassDelete = False, returnAllowMassUpdate = False, returnAllowRead = False, returnAllowUpdate = False, returnCreatedTime = False, returnMenuSecurityItemID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleMenuSecurityItem/" + str(RoleMenuSecurityItemID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createRoleMenuSecurityItem(EntityID = 1, setAllowCreate = None, setAllowDelete = None, setAllowMassCreate = None, setAllowMassDelete = None, setAllowMassUpdate = None, setAllowRead = None, setAllowUpdate = None, setMenuSecurityItemID = None, setRoleID = None, setRelationships = None, returnRoleMenuSecurityItemID = True, returnAllowCreate = False, returnAllowDelete = False, returnAllowMassCreate = False, returnAllowMassDelete = False, returnAllowMassUpdate = False, returnAllowRead = False, returnAllowUpdate = False, returnCreatedTime = False, returnMenuSecurityItemID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleMenuSecurityItem/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteRoleMenuSecurityItem(RoleMenuSecurityItemID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryRoleModulePath(EntityID = 1, page = 1, pageSize = 100, returnRoleModulePathID = True, returnAllowCreate = False, returnAllowDelete = False, returnAllowMassCreate = False, returnAllowMassDelete = False, returnAllowMassUpdate = False, returnAllowRead = False, returnAllowUpdate = False, returnCreatedTime = False, returnModifiedTime = False, returnModulePath = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleModulePath/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getRoleModulePath(RoleModulePathID, EntityID = 1, returnRoleModulePathID = True, returnAllowCreate = False, returnAllowDelete = False, returnAllowMassCreate = False, returnAllowMassDelete = False, returnAllowMassUpdate = False, returnAllowRead = False, returnAllowUpdate = False, returnCreatedTime = False, returnModifiedTime = False, returnModulePath = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleModulePath/" + str(RoleModulePathID), verb = "get", return_params_list = return_params_list)

def modifyRoleModulePath(RoleModulePathID, EntityID = 1, setAllowCreate = None, setAllowDelete = None, setAllowMassCreate = None, setAllowMassDelete = None, setAllowMassUpdate = None, setAllowRead = None, setAllowUpdate = None, setModulePath = None, setRoleID = None, setRelationships = None, returnRoleModulePathID = True, returnAllowCreate = False, returnAllowDelete = False, returnAllowMassCreate = False, returnAllowMassDelete = False, returnAllowMassUpdate = False, returnAllowRead = False, returnAllowUpdate = False, returnCreatedTime = False, returnModifiedTime = False, returnModulePath = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleModulePath/" + str(RoleModulePathID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createRoleModulePath(EntityID = 1, setAllowCreate = None, setAllowDelete = None, setAllowMassCreate = None, setAllowMassDelete = None, setAllowMassUpdate = None, setAllowRead = None, setAllowUpdate = None, setModulePath = None, setRoleID = None, setRelationships = None, returnRoleModulePathID = True, returnAllowCreate = False, returnAllowDelete = False, returnAllowMassCreate = False, returnAllowMassDelete = False, returnAllowMassUpdate = False, returnAllowRead = False, returnAllowUpdate = False, returnCreatedTime = False, returnModifiedTime = False, returnModulePath = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleModulePath/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteRoleModulePath(RoleModulePathID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryRolePortal(EntityID = 1, page = 1, pageSize = 100, returnRolePortalID = True, returnCreatedTime = False, returnModifiedTime = False, returnPortal = False, returnPortalCode = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RolePortal/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getRolePortal(RolePortalID, EntityID = 1, returnRolePortalID = True, returnCreatedTime = False, returnModifiedTime = False, returnPortal = False, returnPortalCode = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RolePortal/" + str(RolePortalID), verb = "get", return_params_list = return_params_list)

def modifyRolePortal(RolePortalID, EntityID = 1, setPortal = None, setPortalCode = None, setRoleID = None, setRelationships = None, returnRolePortalID = True, returnCreatedTime = False, returnModifiedTime = False, returnPortal = False, returnPortalCode = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RolePortal/" + str(RolePortalID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createRolePortal(EntityID = 1, setPortal = None, setPortalCode = None, setRoleID = None, setRelationships = None, returnRolePortalID = True, returnCreatedTime = False, returnModifiedTime = False, returnPortal = False, returnPortalCode = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RolePortal/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteRolePortal(RolePortalID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySecurityLocation(EntityID = 1, page = 1, pageSize = 100, returnSecurityLocationID = True, returnAttachmentTypeGUID = False, returnCanAllowCreate = False, returnCanAllowDelete = False, returnCanAllowMassCreate = False, returnCanAllowMassDelete = False, returnCanAllowMassUpdate = False, returnCanAllowRead = False, returnCanAllowUpdate = False, returnCreatedTime = False, returnMobileCanAllowCreate = False, returnMobileCanAllowDelete = False, returnMobileCanAllowMassCreate = False, returnMobileCanAllowMassDelete = False, returnMobileCanAllowMassUpdate = False, returnMobileCanAllowRead = False, returnMobileCanAllowUpdate = False, returnModifiedTime = False, returnModulePathID = False, returnPath = False, returnPortal = False, returnPortalCode = False, returnReportID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SecurityLocation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSecurityLocation(SecurityLocationID, EntityID = 1, returnSecurityLocationID = True, returnAttachmentTypeGUID = False, returnCanAllowCreate = False, returnCanAllowDelete = False, returnCanAllowMassCreate = False, returnCanAllowMassDelete = False, returnCanAllowMassUpdate = False, returnCanAllowRead = False, returnCanAllowUpdate = False, returnCreatedTime = False, returnMobileCanAllowCreate = False, returnMobileCanAllowDelete = False, returnMobileCanAllowMassCreate = False, returnMobileCanAllowMassDelete = False, returnMobileCanAllowMassUpdate = False, returnMobileCanAllowRead = False, returnMobileCanAllowUpdate = False, returnModifiedTime = False, returnModulePathID = False, returnPath = False, returnPortal = False, returnPortalCode = False, returnReportID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SecurityLocation/" + str(SecurityLocationID), verb = "get", return_params_list = return_params_list)

def modifySecurityLocation(SecurityLocationID, EntityID = 1, setAttachmentTypeGUID = None, setCanAllowCreate = None, setCanAllowDelete = None, setCanAllowMassCreate = None, setCanAllowMassDelete = None, setCanAllowMassUpdate = None, setCanAllowRead = None, setCanAllowUpdate = None, setMobileCanAllowCreate = None, setMobileCanAllowDelete = None, setMobileCanAllowMassCreate = None, setMobileCanAllowMassDelete = None, setMobileCanAllowMassUpdate = None, setMobileCanAllowRead = None, setMobileCanAllowUpdate = None, setModulePathID = None, setPortal = None, setPortalCode = None, setReportID = None, setWorkflowID = None, setRelationships = None, returnSecurityLocationID = True, returnAttachmentTypeGUID = False, returnCanAllowCreate = False, returnCanAllowDelete = False, returnCanAllowMassCreate = False, returnCanAllowMassDelete = False, returnCanAllowMassUpdate = False, returnCanAllowRead = False, returnCanAllowUpdate = False, returnCreatedTime = False, returnMobileCanAllowCreate = False, returnMobileCanAllowDelete = False, returnMobileCanAllowMassCreate = False, returnMobileCanAllowMassDelete = False, returnMobileCanAllowMassUpdate = False, returnMobileCanAllowRead = False, returnMobileCanAllowUpdate = False, returnModifiedTime = False, returnModulePathID = False, returnPath = False, returnPortal = False, returnPortalCode = False, returnReportID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SecurityLocation/" + str(SecurityLocationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSecurityLocation(EntityID = 1, setAttachmentTypeGUID = None, setCanAllowCreate = None, setCanAllowDelete = None, setCanAllowMassCreate = None, setCanAllowMassDelete = None, setCanAllowMassUpdate = None, setCanAllowRead = None, setCanAllowUpdate = None, setMobileCanAllowCreate = None, setMobileCanAllowDelete = None, setMobileCanAllowMassCreate = None, setMobileCanAllowMassDelete = None, setMobileCanAllowMassUpdate = None, setMobileCanAllowRead = None, setMobileCanAllowUpdate = None, setModulePathID = None, setPortal = None, setPortalCode = None, setReportID = None, setWorkflowID = None, setRelationships = None, returnSecurityLocationID = True, returnAttachmentTypeGUID = False, returnCanAllowCreate = False, returnCanAllowDelete = False, returnCanAllowMassCreate = False, returnCanAllowMassDelete = False, returnCanAllowMassUpdate = False, returnCanAllowRead = False, returnCanAllowUpdate = False, returnCreatedTime = False, returnMobileCanAllowCreate = False, returnMobileCanAllowDelete = False, returnMobileCanAllowMassCreate = False, returnMobileCanAllowMassDelete = False, returnMobileCanAllowMassUpdate = False, returnMobileCanAllowRead = False, returnMobileCanAllowUpdate = False, returnModifiedTime = False, returnModulePathID = False, returnPath = False, returnPortal = False, returnPortalCode = False, returnReportID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SecurityLocation/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSecurityLocation(SecurityLocationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySecurityLocationMenuSecurityItem(EntityID = 1, page = 1, pageSize = 100, returnSecurityLocationMenuSecurityItemID = True, returnCreatedTime = False, returnMenuSecurityItemID = False, returnModifiedTime = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SecurityLocationMenuSecurityItem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSecurityLocationMenuSecurityItem(SecurityLocationMenuSecurityItemID, EntityID = 1, returnSecurityLocationMenuSecurityItemID = True, returnCreatedTime = False, returnMenuSecurityItemID = False, returnModifiedTime = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SecurityLocationMenuSecurityItem/" + str(SecurityLocationMenuSecurityItemID), verb = "get", return_params_list = return_params_list)

def modifySecurityLocationMenuSecurityItem(SecurityLocationMenuSecurityItemID, EntityID = 1, setMenuSecurityItemID = None, setSecurityLocationID = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnSecurityLocationMenuSecurityItemID = True, returnCreatedTime = False, returnMenuSecurityItemID = False, returnModifiedTime = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SecurityLocationMenuSecurityItem/" + str(SecurityLocationMenuSecurityItemID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSecurityLocationMenuSecurityItem(EntityID = 1, setMenuSecurityItemID = None, setSecurityLocationID = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnSecurityLocationMenuSecurityItemID = True, returnCreatedTime = False, returnMenuSecurityItemID = False, returnModifiedTime = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SecurityLocationMenuSecurityItem/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSecurityLocationMenuSecurityItem(SecurityLocationMenuSecurityItemID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySessionFileUpload(EntityID = 1, page = 1, pageSize = 100, returnSessionFileUploadID = True, returnBytes = False, returnCreatedTime = False, returnFileContents = False, returnFileName = False, returnFilePath = False, returnMetaData = False, returnMetaDataXml = False, returnModifiedTime = False, returnSessionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXDimension = False, returnYDimension = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SessionFileUpload/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSessionFileUpload(SessionFileUploadID, EntityID = 1, returnSessionFileUploadID = True, returnBytes = False, returnCreatedTime = False, returnFileContents = False, returnFileName = False, returnFilePath = False, returnMetaData = False, returnMetaDataXml = False, returnModifiedTime = False, returnSessionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXDimension = False, returnYDimension = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SessionFileUpload/" + str(SessionFileUploadID), verb = "get", return_params_list = return_params_list)

def modifySessionFileUpload(SessionFileUploadID, EntityID = 1, setFileContents = None, setFilePath = None, setMetaData = None, setSessionID = None, setRelationships = None, returnSessionFileUploadID = True, returnBytes = False, returnCreatedTime = False, returnFileContents = False, returnFileName = False, returnFilePath = False, returnMetaData = False, returnMetaDataXml = False, returnModifiedTime = False, returnSessionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXDimension = False, returnYDimension = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SessionFileUpload/" + str(SessionFileUploadID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSessionFileUpload(EntityID = 1, setFileContents = None, setFilePath = None, setMetaData = None, setSessionID = None, setRelationships = None, returnSessionFileUploadID = True, returnBytes = False, returnCreatedTime = False, returnFileContents = False, returnFileName = False, returnFilePath = False, returnMetaData = False, returnMetaDataXml = False, returnModifiedTime = False, returnSessionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXDimension = False, returnYDimension = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SessionFileUpload/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSessionFileUpload(SessionFileUploadID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySkywardSupportAccess(EntityID = 1, page = 1, pageSize = 100, returnSkywardSupportAccessID = True, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnNotes = False, returnServiceCallNumber = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SkywardSupportAccess/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSkywardSupportAccess(SkywardSupportAccessID, EntityID = 1, returnSkywardSupportAccessID = True, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnNotes = False, returnServiceCallNumber = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SkywardSupportAccess/" + str(SkywardSupportAccessID), verb = "get", return_params_list = return_params_list)

def modifySkywardSupportAccess(SkywardSupportAccessID, EntityID = 1, setEndDate = None, setIsActive = None, setNotes = None, setServiceCallNumber = None, setStartDate = None, setRelationships = None, returnSkywardSupportAccessID = True, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnNotes = False, returnServiceCallNumber = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SkywardSupportAccess/" + str(SkywardSupportAccessID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSkywardSupportAccess(EntityID = 1, setEndDate = None, setIsActive = None, setNotes = None, setServiceCallNumber = None, setStartDate = None, setRelationships = None, returnSkywardSupportAccessID = True, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnNotes = False, returnServiceCallNumber = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SkywardSupportAccess/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSkywardSupportAccess(SkywardSupportAccessID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySkywardSupportAccessLoginHistory(EntityID = 1, page = 1, pageSize = 100, returnSkywardSupportAccessLoginHistoryID = True, returnAccessedTime = False, returnCreatedTime = False, returnModifiedTime = False, returnSessionID = False, returnSkywardEmployeeName = False, returnSkywardSupportAccessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SkywardSupportAccessLoginHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSkywardSupportAccessLoginHistory(SkywardSupportAccessLoginHistoryID, EntityID = 1, returnSkywardSupportAccessLoginHistoryID = True, returnAccessedTime = False, returnCreatedTime = False, returnModifiedTime = False, returnSessionID = False, returnSkywardEmployeeName = False, returnSkywardSupportAccessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SkywardSupportAccessLoginHistory/" + str(SkywardSupportAccessLoginHistoryID), verb = "get", return_params_list = return_params_list)

def modifySkywardSupportAccessLoginHistory(SkywardSupportAccessLoginHistoryID, EntityID = 1, setAccessedTime = None, setSessionID = None, setSkywardEmployeeName = None, setSkywardSupportAccessID = None, setRelationships = None, returnSkywardSupportAccessLoginHistoryID = True, returnAccessedTime = False, returnCreatedTime = False, returnModifiedTime = False, returnSessionID = False, returnSkywardEmployeeName = False, returnSkywardSupportAccessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SkywardSupportAccessLoginHistory/" + str(SkywardSupportAccessLoginHistoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSkywardSupportAccessLoginHistory(EntityID = 1, setAccessedTime = None, setSessionID = None, setSkywardEmployeeName = None, setSkywardSupportAccessID = None, setRelationships = None, returnSkywardSupportAccessLoginHistoryID = True, returnAccessedTime = False, returnCreatedTime = False, returnModifiedTime = False, returnSessionID = False, returnSkywardEmployeeName = False, returnSkywardSupportAccessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SkywardSupportAccessLoginHistory/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSkywardSupportAccessLoginHistory(SkywardSupportAccessLoginHistoryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempDeletedPortalAccessSecurityUser(EntityID = 1, page = 1, pageSize = 100, returnTempDeletedPortalAccessSecurityUserID = True, returnCreatedTime = False, returnFullNameLFM = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempDeletedPortalAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempDeletedPortalAccessSecurityUser(TempDeletedPortalAccessSecurityUserID, EntityID = 1, returnTempDeletedPortalAccessSecurityUserID = True, returnCreatedTime = False, returnFullNameLFM = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempDeletedPortalAccessSecurityUser/" + str(TempDeletedPortalAccessSecurityUserID), verb = "get", return_params_list = return_params_list)

def modifyTempDeletedPortalAccessSecurityUser(TempDeletedPortalAccessSecurityUserID, EntityID = 1, setFullNameLFM = None, setUserName = None, setRelationships = None, returnTempDeletedPortalAccessSecurityUserID = True, returnCreatedTime = False, returnFullNameLFM = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempDeletedPortalAccessSecurityUser/" + str(TempDeletedPortalAccessSecurityUserID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempDeletedPortalAccessSecurityUser(EntityID = 1, setFullNameLFM = None, setUserName = None, setRelationships = None, returnTempDeletedPortalAccessSecurityUserID = True, returnCreatedTime = False, returnFullNameLFM = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempDeletedPortalAccessSecurityUser/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempDeletedPortalAccessSecurityUser(TempDeletedPortalAccessSecurityUserID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempEmployeeAccessSecurityUser(EntityID = 1, page = 1, pageSize = 100, returnTempEmployeeAccessSecurityUserID = True, returnAddToEmployeeAccess = False, returnAllowEmployeeAccess = False, returnCreatedTime = False, returnEmailAddress = False, returnEmployeeID = False, returnEmployeeNameLFM = False, returnEmployeeNumber = False, returnForUserCreation = False, returnGroup = False, returnIsAuditEmployeeAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromEmployeeAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempEmployeeAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempEmployeeAccessSecurityUser(TempEmployeeAccessSecurityUserID, EntityID = 1, returnTempEmployeeAccessSecurityUserID = True, returnAddToEmployeeAccess = False, returnAllowEmployeeAccess = False, returnCreatedTime = False, returnEmailAddress = False, returnEmployeeID = False, returnEmployeeNameLFM = False, returnEmployeeNumber = False, returnForUserCreation = False, returnGroup = False, returnIsAuditEmployeeAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromEmployeeAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempEmployeeAccessSecurityUser/" + str(TempEmployeeAccessSecurityUserID), verb = "get", return_params_list = return_params_list)

def modifyTempEmployeeAccessSecurityUser(TempEmployeeAccessSecurityUserID, EntityID = 1, setAddToEmployeeAccess = None, setAllowEmployeeAccess = None, setEmailAddress = None, setEmployeeID = None, setEmployeeNameLFM = None, setEmployeeNumber = None, setForUserCreation = None, setGroup = None, setIsAuditEmployeeAccessSecurity = None, setIsException = None, setIsSelected = None, setRemoveFromEmployeeAccess = None, setUserName = None, setRelationships = None, returnTempEmployeeAccessSecurityUserID = True, returnAddToEmployeeAccess = False, returnAllowEmployeeAccess = False, returnCreatedTime = False, returnEmailAddress = False, returnEmployeeID = False, returnEmployeeNameLFM = False, returnEmployeeNumber = False, returnForUserCreation = False, returnGroup = False, returnIsAuditEmployeeAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromEmployeeAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempEmployeeAccessSecurityUser/" + str(TempEmployeeAccessSecurityUserID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempEmployeeAccessSecurityUser(EntityID = 1, setAddToEmployeeAccess = None, setAllowEmployeeAccess = None, setEmailAddress = None, setEmployeeID = None, setEmployeeNameLFM = None, setEmployeeNumber = None, setForUserCreation = None, setGroup = None, setIsAuditEmployeeAccessSecurity = None, setIsException = None, setIsSelected = None, setRemoveFromEmployeeAccess = None, setUserName = None, setRelationships = None, returnTempEmployeeAccessSecurityUserID = True, returnAddToEmployeeAccess = False, returnAllowEmployeeAccess = False, returnCreatedTime = False, returnEmailAddress = False, returnEmployeeID = False, returnEmployeeNameLFM = False, returnEmployeeNumber = False, returnForUserCreation = False, returnGroup = False, returnIsAuditEmployeeAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromEmployeeAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempEmployeeAccessSecurityUser/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempEmployeeAccessSecurityUser(TempEmployeeAccessSecurityUserID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempEntityForClone(EntityID = 1, page = 1, pageSize = 100, returnTempEntityForCloneID = True, returnCreatedTime = False, returnEntityCode = False, returnEntityName = False, returnEntityPrimaryKey = False, returnModifiedTime = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempEntityForClone/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempEntityForClone(TempEntityForCloneID, EntityID = 1, returnTempEntityForCloneID = True, returnCreatedTime = False, returnEntityCode = False, returnEntityName = False, returnEntityPrimaryKey = False, returnModifiedTime = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempEntityForClone/" + str(TempEntityForCloneID), verb = "get", return_params_list = return_params_list)

def modifyTempEntityForClone(TempEntityForCloneID, EntityID = 1, setEntityCode = None, setEntityName = None, setEntityPrimaryKey = None, setSelected = None, setRelationships = None, returnTempEntityForCloneID = True, returnCreatedTime = False, returnEntityCode = False, returnEntityName = False, returnEntityPrimaryKey = False, returnModifiedTime = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempEntityForClone/" + str(TempEntityForCloneID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempEntityForClone(EntityID = 1, setEntityCode = None, setEntityName = None, setEntityPrimaryKey = None, setSelected = None, setRelationships = None, returnTempEntityForCloneID = True, returnCreatedTime = False, returnEntityCode = False, returnEntityName = False, returnEntityPrimaryKey = False, returnModifiedTime = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempEntityForClone/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempEntityForClone(TempEntityForCloneID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempFailedPortalAccessSecurityUser(EntityID = 1, page = 1, pageSize = 100, returnTempFailedPortalAccessSecurityUserID = True, returnCreatedTime = False, returnFullNameLFM = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFailedPortalAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempFailedPortalAccessSecurityUser(TempFailedPortalAccessSecurityUserID, EntityID = 1, returnTempFailedPortalAccessSecurityUserID = True, returnCreatedTime = False, returnFullNameLFM = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFailedPortalAccessSecurityUser/" + str(TempFailedPortalAccessSecurityUserID), verb = "get", return_params_list = return_params_list)

def modifyTempFailedPortalAccessSecurityUser(TempFailedPortalAccessSecurityUserID, EntityID = 1, setFullNameLFM = None, setNote = None, setUserName = None, setRelationships = None, returnTempFailedPortalAccessSecurityUserID = True, returnCreatedTime = False, returnFullNameLFM = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFailedPortalAccessSecurityUser/" + str(TempFailedPortalAccessSecurityUserID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempFailedPortalAccessSecurityUser(EntityID = 1, setFullNameLFM = None, setNote = None, setUserName = None, setRelationships = None, returnTempFailedPortalAccessSecurityUserID = True, returnCreatedTime = False, returnFullNameLFM = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFailedPortalAccessSecurityUser/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempFailedPortalAccessSecurityUser(TempFailedPortalAccessSecurityUserID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempFamilyAccessSecurityUser(EntityID = 1, page = 1, pageSize = 100, returnTempFamilyAccessSecurityUserID = True, returnAddToFamilyAccess = False, returnCreatedTime = False, returnEmailAddress = False, returnEntityCodeName = False, returnForUserCreation = False, returnGuardianNameLFM = False, returnIsAuditFamilyAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromFamilyAccess = False, returnStudentGuardianID = False, returnStudentNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFamilyAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempFamilyAccessSecurityUser(TempFamilyAccessSecurityUserID, EntityID = 1, returnTempFamilyAccessSecurityUserID = True, returnAddToFamilyAccess = False, returnCreatedTime = False, returnEmailAddress = False, returnEntityCodeName = False, returnForUserCreation = False, returnGuardianNameLFM = False, returnIsAuditFamilyAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromFamilyAccess = False, returnStudentGuardianID = False, returnStudentNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFamilyAccessSecurityUser/" + str(TempFamilyAccessSecurityUserID), verb = "get", return_params_list = return_params_list)

def modifyTempFamilyAccessSecurityUser(TempFamilyAccessSecurityUserID, EntityID = 1, setAddToFamilyAccess = None, setEmailAddress = None, setEntityCodeName = None, setForUserCreation = None, setGuardianNameLFM = None, setIsAuditFamilyAccessSecurity = None, setIsException = None, setIsSelected = None, setRemoveFromFamilyAccess = None, setStudentGuardianID = None, setStudentNameLFM = None, setUserName = None, setRelationships = None, returnTempFamilyAccessSecurityUserID = True, returnAddToFamilyAccess = False, returnCreatedTime = False, returnEmailAddress = False, returnEntityCodeName = False, returnForUserCreation = False, returnGuardianNameLFM = False, returnIsAuditFamilyAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromFamilyAccess = False, returnStudentGuardianID = False, returnStudentNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFamilyAccessSecurityUser/" + str(TempFamilyAccessSecurityUserID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempFamilyAccessSecurityUser(EntityID = 1, setAddToFamilyAccess = None, setEmailAddress = None, setEntityCodeName = None, setForUserCreation = None, setGuardianNameLFM = None, setIsAuditFamilyAccessSecurity = None, setIsException = None, setIsSelected = None, setRemoveFromFamilyAccess = None, setStudentGuardianID = None, setStudentNameLFM = None, setUserName = None, setRelationships = None, returnTempFamilyAccessSecurityUserID = True, returnAddToFamilyAccess = False, returnCreatedTime = False, returnEmailAddress = False, returnEntityCodeName = False, returnForUserCreation = False, returnGuardianNameLFM = False, returnIsAuditFamilyAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromFamilyAccess = False, returnStudentGuardianID = False, returnStudentNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFamilyAccessSecurityUser/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempFamilyAccessSecurityUser(TempFamilyAccessSecurityUserID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempFieldRestrictionScreen(EntityID = 1, page = 1, pageSize = 100, returnTempFieldRestrictionScreenID = True, returnCreatedTime = False, returnDisplayText = False, returnModifiedTime = False, returnSecurityLocationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFieldRestrictionScreen/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempFieldRestrictionScreen(TempFieldRestrictionScreenID, EntityID = 1, returnTempFieldRestrictionScreenID = True, returnCreatedTime = False, returnDisplayText = False, returnModifiedTime = False, returnSecurityLocationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFieldRestrictionScreen/" + str(TempFieldRestrictionScreenID), verb = "get", return_params_list = return_params_list)

def modifyTempFieldRestrictionScreen(TempFieldRestrictionScreenID, EntityID = 1, setDisplayText = None, setSecurityLocationID = None, setRelationships = None, returnTempFieldRestrictionScreenID = True, returnCreatedTime = False, returnDisplayText = False, returnModifiedTime = False, returnSecurityLocationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFieldRestrictionScreen/" + str(TempFieldRestrictionScreenID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempFieldRestrictionScreen(EntityID = 1, setDisplayText = None, setSecurityLocationID = None, setRelationships = None, returnTempFieldRestrictionScreenID = True, returnCreatedTime = False, returnDisplayText = False, returnModifiedTime = False, returnSecurityLocationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFieldRestrictionScreen/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempFieldRestrictionScreen(TempFieldRestrictionScreenID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempImpersonationRoleForClone(EntityID = 1, page = 1, pageSize = 100, returnTempImpersonationRoleForCloneID = True, returnCreatedTime = False, returnDescription = False, returnIsReadOnly = False, returnModifiedTime = False, returnRoleName = False, returnRolePrimaryKey = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempImpersonationRoleForClone/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempImpersonationRoleForClone(TempImpersonationRoleForCloneID, EntityID = 1, returnTempImpersonationRoleForCloneID = True, returnCreatedTime = False, returnDescription = False, returnIsReadOnly = False, returnModifiedTime = False, returnRoleName = False, returnRolePrimaryKey = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempImpersonationRoleForClone/" + str(TempImpersonationRoleForCloneID), verb = "get", return_params_list = return_params_list)

def modifyTempImpersonationRoleForClone(TempImpersonationRoleForCloneID, EntityID = 1, setDescription = None, setIsReadOnly = None, setRoleName = None, setRolePrimaryKey = None, setSelected = None, setRelationships = None, returnTempImpersonationRoleForCloneID = True, returnCreatedTime = False, returnDescription = False, returnIsReadOnly = False, returnModifiedTime = False, returnRoleName = False, returnRolePrimaryKey = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempImpersonationRoleForClone/" + str(TempImpersonationRoleForCloneID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempImpersonationRoleForClone(EntityID = 1, setDescription = None, setIsReadOnly = None, setRoleName = None, setRolePrimaryKey = None, setSelected = None, setRelationships = None, returnTempImpersonationRoleForCloneID = True, returnCreatedTime = False, returnDescription = False, returnIsReadOnly = False, returnModifiedTime = False, returnRoleName = False, returnRolePrimaryKey = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempImpersonationRoleForClone/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempImpersonationRoleForClone(TempImpersonationRoleForCloneID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempRoleForClone(EntityID = 1, page = 1, pageSize = 100, returnTempRoleForCloneID = True, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoleName = False, returnRolePrimaryKey = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempRoleForClone/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempRoleForClone(TempRoleForCloneID, EntityID = 1, returnTempRoleForCloneID = True, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoleName = False, returnRolePrimaryKey = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempRoleForClone/" + str(TempRoleForCloneID), verb = "get", return_params_list = return_params_list)

def modifyTempRoleForClone(TempRoleForCloneID, EntityID = 1, setDescription = None, setRoleName = None, setRolePrimaryKey = None, setSelected = None, setRelationships = None, returnTempRoleForCloneID = True, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoleName = False, returnRolePrimaryKey = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempRoleForClone/" + str(TempRoleForCloneID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempRoleForClone(EntityID = 1, setDescription = None, setRoleName = None, setRolePrimaryKey = None, setSelected = None, setRelationships = None, returnTempRoleForCloneID = True, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoleName = False, returnRolePrimaryKey = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempRoleForClone/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempRoleForClone(TempRoleForCloneID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempSecurityImportError(EntityID = 1, page = 1, pageSize = 100, returnTempSecurityImportErrorID = True, returnCreatedTime = False, returnErrorMessage = False, returnErrorObject = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempSecurityImportError(TempSecurityImportErrorID, EntityID = 1, returnTempSecurityImportErrorID = True, returnCreatedTime = False, returnErrorMessage = False, returnErrorObject = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportError/" + str(TempSecurityImportErrorID), verb = "get", return_params_list = return_params_list)

def modifyTempSecurityImportError(TempSecurityImportErrorID, EntityID = 1, setErrorMessage = None, setErrorObject = None, setRelationships = None, returnTempSecurityImportErrorID = True, returnCreatedTime = False, returnErrorMessage = False, returnErrorObject = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportError/" + str(TempSecurityImportErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempSecurityImportError(EntityID = 1, setErrorMessage = None, setErrorObject = None, setRelationships = None, returnTempSecurityImportErrorID = True, returnCreatedTime = False, returnErrorMessage = False, returnErrorObject = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempSecurityImportError(TempSecurityImportErrorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempSecurityImportGroupMembership(EntityID = 1, page = 1, pageSize = 100, returnTempSecurityImportGroupMembershipID = True, returnCreatedTime = False, returnEntityName = False, returnExistingUserID = False, returnExternalUniqueIdentifier = False, returnGroupName = False, returnImportExternalUniqueIdentifier = False, returnImportUserNameBirthDate = False, returnImportUserNameFullNameLegalLFM = False, returnImportUserNameFullNameLFM = False, returnImportUserNamePrimaryEmailAddress = False, returnMatches = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserNameBirthDate = False, returnUserNameFullNameLegalLFM = False, returnUserNameFullNameLFM = False, returnUserNamePrimaryEmailAddress = False, returnUserUsername = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportGroupMembership/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempSecurityImportGroupMembership(TempSecurityImportGroupMembershipID, EntityID = 1, returnTempSecurityImportGroupMembershipID = True, returnCreatedTime = False, returnEntityName = False, returnExistingUserID = False, returnExternalUniqueIdentifier = False, returnGroupName = False, returnImportExternalUniqueIdentifier = False, returnImportUserNameBirthDate = False, returnImportUserNameFullNameLegalLFM = False, returnImportUserNameFullNameLFM = False, returnImportUserNamePrimaryEmailAddress = False, returnMatches = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserNameBirthDate = False, returnUserNameFullNameLegalLFM = False, returnUserNameFullNameLFM = False, returnUserNamePrimaryEmailAddress = False, returnUserUsername = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportGroupMembership/" + str(TempSecurityImportGroupMembershipID), verb = "get", return_params_list = return_params_list)

def modifyTempSecurityImportGroupMembership(TempSecurityImportGroupMembershipID, EntityID = 1, setEntityName = None, setExistingUserID = None, setExternalUniqueIdentifier = None, setGroupName = None, setImportExternalUniqueIdentifier = None, setImportUserNameBirthDate = None, setImportUserNameFullNameLegalLFM = None, setImportUserNameFullNameLFM = None, setImportUserNamePrimaryEmailAddress = None, setMatches = None, setUserNameBirthDate = None, setUserNameFullNameLegalLFM = None, setUserNameFullNameLFM = None, setUserNamePrimaryEmailAddress = None, setUserUsername = None, setRelationships = None, returnTempSecurityImportGroupMembershipID = True, returnCreatedTime = False, returnEntityName = False, returnExistingUserID = False, returnExternalUniqueIdentifier = False, returnGroupName = False, returnImportExternalUniqueIdentifier = False, returnImportUserNameBirthDate = False, returnImportUserNameFullNameLegalLFM = False, returnImportUserNameFullNameLFM = False, returnImportUserNamePrimaryEmailAddress = False, returnMatches = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserNameBirthDate = False, returnUserNameFullNameLegalLFM = False, returnUserNameFullNameLFM = False, returnUserNamePrimaryEmailAddress = False, returnUserUsername = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportGroupMembership/" + str(TempSecurityImportGroupMembershipID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempSecurityImportGroupMembership(EntityID = 1, setEntityName = None, setExistingUserID = None, setExternalUniqueIdentifier = None, setGroupName = None, setImportExternalUniqueIdentifier = None, setImportUserNameBirthDate = None, setImportUserNameFullNameLegalLFM = None, setImportUserNameFullNameLFM = None, setImportUserNamePrimaryEmailAddress = None, setMatches = None, setUserNameBirthDate = None, setUserNameFullNameLegalLFM = None, setUserNameFullNameLFM = None, setUserNamePrimaryEmailAddress = None, setUserUsername = None, setRelationships = None, returnTempSecurityImportGroupMembershipID = True, returnCreatedTime = False, returnEntityName = False, returnExistingUserID = False, returnExternalUniqueIdentifier = False, returnGroupName = False, returnImportExternalUniqueIdentifier = False, returnImportUserNameBirthDate = False, returnImportUserNameFullNameLegalLFM = False, returnImportUserNameFullNameLFM = False, returnImportUserNamePrimaryEmailAddress = False, returnMatches = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserNameBirthDate = False, returnUserNameFullNameLegalLFM = False, returnUserNameFullNameLFM = False, returnUserNamePrimaryEmailAddress = False, returnUserUsername = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportGroupMembership/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempSecurityImportGroupMembership(TempSecurityImportGroupMembershipID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempSecurityImportPreview(EntityID = 1, page = 1, pageSize = 100, returnTempSecurityImportPreviewID = True, returnCreatedTime = False, returnIdentifier = False, returnModifiedTime = False, returnObject = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportPreview/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempSecurityImportPreview(TempSecurityImportPreviewID, EntityID = 1, returnTempSecurityImportPreviewID = True, returnCreatedTime = False, returnIdentifier = False, returnModifiedTime = False, returnObject = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportPreview/" + str(TempSecurityImportPreviewID), verb = "get", return_params_list = return_params_list)

def modifyTempSecurityImportPreview(TempSecurityImportPreviewID, EntityID = 1, setIdentifier = None, setObject = None, setRelationships = None, returnTempSecurityImportPreviewID = True, returnCreatedTime = False, returnIdentifier = False, returnModifiedTime = False, returnObject = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportPreview/" + str(TempSecurityImportPreviewID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempSecurityImportPreview(EntityID = 1, setIdentifier = None, setObject = None, setRelationships = None, returnTempSecurityImportPreviewID = True, returnCreatedTime = False, returnIdentifier = False, returnModifiedTime = False, returnObject = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportPreview/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempSecurityImportPreview(TempSecurityImportPreviewID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempSpecialtyAccessGroup(EntityID = 1, page = 1, pageSize = 100, returnTempSpecialtyAccessGroupID = True, returnCreatedTime = False, returnGroupName = False, returnIdentifier = False, returnModifiedTime = False, returnSelected = False, returnSpecialtyAccessGroupPrimaryKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSpecialtyAccessGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempSpecialtyAccessGroup(TempSpecialtyAccessGroupID, EntityID = 1, returnTempSpecialtyAccessGroupID = True, returnCreatedTime = False, returnGroupName = False, returnIdentifier = False, returnModifiedTime = False, returnSelected = False, returnSpecialtyAccessGroupPrimaryKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSpecialtyAccessGroup/" + str(TempSpecialtyAccessGroupID), verb = "get", return_params_list = return_params_list)

def modifyTempSpecialtyAccessGroup(TempSpecialtyAccessGroupID, EntityID = 1, setGroupName = None, setIdentifier = None, setSelected = None, setSpecialtyAccessGroupPrimaryKey = None, setRelationships = None, returnTempSpecialtyAccessGroupID = True, returnCreatedTime = False, returnGroupName = False, returnIdentifier = False, returnModifiedTime = False, returnSelected = False, returnSpecialtyAccessGroupPrimaryKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSpecialtyAccessGroup/" + str(TempSpecialtyAccessGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempSpecialtyAccessGroup(EntityID = 1, setGroupName = None, setIdentifier = None, setSelected = None, setSpecialtyAccessGroupPrimaryKey = None, setRelationships = None, returnTempSpecialtyAccessGroupID = True, returnCreatedTime = False, returnGroupName = False, returnIdentifier = False, returnModifiedTime = False, returnSelected = False, returnSpecialtyAccessGroupPrimaryKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSpecialtyAccessGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempSpecialtyAccessGroup(TempSpecialtyAccessGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentAccessSecurityUser(EntityID = 1, page = 1, pageSize = 100, returnTempStudentAccessSecurityUserID = True, returnAddToStudentAccess = False, returnCreatedTime = False, returnDeleteUserAfterAudit = False, returnEmailAddress = False, returnForUserCreation = False, returnGroup = False, returnIsAuditStudentAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromStudentAccess = False, returnStudentID = False, returnStudentNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempStudentAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentAccessSecurityUser(TempStudentAccessSecurityUserID, EntityID = 1, returnTempStudentAccessSecurityUserID = True, returnAddToStudentAccess = False, returnCreatedTime = False, returnDeleteUserAfterAudit = False, returnEmailAddress = False, returnForUserCreation = False, returnGroup = False, returnIsAuditStudentAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromStudentAccess = False, returnStudentID = False, returnStudentNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempStudentAccessSecurityUser/" + str(TempStudentAccessSecurityUserID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentAccessSecurityUser(TempStudentAccessSecurityUserID, EntityID = 1, setAddToStudentAccess = None, setDeleteUserAfterAudit = None, setEmailAddress = None, setForUserCreation = None, setGroup = None, setIsAuditStudentAccessSecurity = None, setIsException = None, setIsSelected = None, setRemoveFromStudentAccess = None, setStudentID = None, setStudentNameLFM = None, setUserName = None, setRelationships = None, returnTempStudentAccessSecurityUserID = True, returnAddToStudentAccess = False, returnCreatedTime = False, returnDeleteUserAfterAudit = False, returnEmailAddress = False, returnForUserCreation = False, returnGroup = False, returnIsAuditStudentAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromStudentAccess = False, returnStudentID = False, returnStudentNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempStudentAccessSecurityUser/" + str(TempStudentAccessSecurityUserID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentAccessSecurityUser(EntityID = 1, setAddToStudentAccess = None, setDeleteUserAfterAudit = None, setEmailAddress = None, setForUserCreation = None, setGroup = None, setIsAuditStudentAccessSecurity = None, setIsException = None, setIsSelected = None, setRemoveFromStudentAccess = None, setStudentID = None, setStudentNameLFM = None, setUserName = None, setRelationships = None, returnTempStudentAccessSecurityUserID = True, returnAddToStudentAccess = False, returnCreatedTime = False, returnDeleteUserAfterAudit = False, returnEmailAddress = False, returnForUserCreation = False, returnGroup = False, returnIsAuditStudentAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromStudentAccess = False, returnStudentID = False, returnStudentNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempStudentAccessSecurityUser/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentAccessSecurityUser(TempStudentAccessSecurityUserID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempTeacherAccessSecurityUser(EntityID = 1, page = 1, pageSize = 100, returnTempTeacherAccessSecurityUserID = True, returnAddToTeacherAccess = False, returnAllowTeacherAccess = False, returnCreatedTime = False, returnDeleteUserAfterAudit = False, returnEmailAddress = False, returnForUserCreation = False, returnGroup = False, returnIsAuditTeacherAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnNote = False, returnRemoveFromTeacherAccess = False, returnStaffID = False, returnStaffNameLFM = False, returnStaffNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempTeacherAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempTeacherAccessSecurityUser(TempTeacherAccessSecurityUserID, EntityID = 1, returnTempTeacherAccessSecurityUserID = True, returnAddToTeacherAccess = False, returnAllowTeacherAccess = False, returnCreatedTime = False, returnDeleteUserAfterAudit = False, returnEmailAddress = False, returnForUserCreation = False, returnGroup = False, returnIsAuditTeacherAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnNote = False, returnRemoveFromTeacherAccess = False, returnStaffID = False, returnStaffNameLFM = False, returnStaffNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempTeacherAccessSecurityUser/" + str(TempTeacherAccessSecurityUserID), verb = "get", return_params_list = return_params_list)

def modifyTempTeacherAccessSecurityUser(TempTeacherAccessSecurityUserID, EntityID = 1, setAddToTeacherAccess = None, setAllowTeacherAccess = None, setDeleteUserAfterAudit = None, setEmailAddress = None, setForUserCreation = None, setGroup = None, setIsAuditTeacherAccessSecurity = None, setIsException = None, setIsSelected = None, setNote = None, setRemoveFromTeacherAccess = None, setStaffID = None, setStaffNameLFM = None, setStaffNumber = None, setUserName = None, setRelationships = None, returnTempTeacherAccessSecurityUserID = True, returnAddToTeacherAccess = False, returnAllowTeacherAccess = False, returnCreatedTime = False, returnDeleteUserAfterAudit = False, returnEmailAddress = False, returnForUserCreation = False, returnGroup = False, returnIsAuditTeacherAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnNote = False, returnRemoveFromTeacherAccess = False, returnStaffID = False, returnStaffNameLFM = False, returnStaffNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempTeacherAccessSecurityUser/" + str(TempTeacherAccessSecurityUserID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempTeacherAccessSecurityUser(EntityID = 1, setAddToTeacherAccess = None, setAllowTeacherAccess = None, setDeleteUserAfterAudit = None, setEmailAddress = None, setForUserCreation = None, setGroup = None, setIsAuditTeacherAccessSecurity = None, setIsException = None, setIsSelected = None, setNote = None, setRemoveFromTeacherAccess = None, setStaffID = None, setStaffNameLFM = None, setStaffNumber = None, setUserName = None, setRelationships = None, returnTempTeacherAccessSecurityUserID = True, returnAddToTeacherAccess = False, returnAllowTeacherAccess = False, returnCreatedTime = False, returnDeleteUserAfterAudit = False, returnEmailAddress = False, returnForUserCreation = False, returnGroup = False, returnIsAuditTeacherAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnNote = False, returnRemoveFromTeacherAccess = False, returnStaffID = False, returnStaffNameLFM = False, returnStaffNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempTeacherAccessSecurityUser/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempTeacherAccessSecurityUser(TempTeacherAccessSecurityUserID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTrustedDevice(EntityID = 1, page = 1, pageSize = 100, returnTrustedDeviceID = True, returnBrowserType = False, returnBrowserVersion = False, returnCreatedTime = False, returnDeviceType = False, returnHostAddress = False, returnIdentifier = False, returnModifiedTime = False, returnOperatingSystemType = False, returnUserAgent = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TrustedDevice/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTrustedDevice(TrustedDeviceID, EntityID = 1, returnTrustedDeviceID = True, returnBrowserType = False, returnBrowserVersion = False, returnCreatedTime = False, returnDeviceType = False, returnHostAddress = False, returnIdentifier = False, returnModifiedTime = False, returnOperatingSystemType = False, returnUserAgent = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TrustedDevice/" + str(TrustedDeviceID), verb = "get", return_params_list = return_params_list)

def modifyTrustedDevice(TrustedDeviceID, EntityID = 1, setBrowserType = None, setBrowserVersion = None, setDeviceType = None, setHostAddress = None, setIdentifier = None, setOperatingSystemType = None, setUserAgent = None, setUserID = None, setRelationships = None, returnTrustedDeviceID = True, returnBrowserType = False, returnBrowserVersion = False, returnCreatedTime = False, returnDeviceType = False, returnHostAddress = False, returnIdentifier = False, returnModifiedTime = False, returnOperatingSystemType = False, returnUserAgent = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TrustedDevice/" + str(TrustedDeviceID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTrustedDevice(EntityID = 1, setBrowserType = None, setBrowserVersion = None, setDeviceType = None, setHostAddress = None, setIdentifier = None, setOperatingSystemType = None, setUserAgent = None, setUserID = None, setRelationships = None, returnTrustedDeviceID = True, returnBrowserType = False, returnBrowserVersion = False, returnCreatedTime = False, returnDeviceType = False, returnHostAddress = False, returnIdentifier = False, returnModifiedTime = False, returnOperatingSystemType = False, returnUserAgent = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TrustedDevice/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTrustedDevice(TrustedDeviceID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryUserAuthenticationMethod(EntityID = 1, page = 1, pageSize = 100, returnUserAuthenticationMethodID = True, returnAuthenticationMethodID = False, returnCreatedTime = False, returnModifiedTime = False, returnProviderUserIdentity = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserAuthenticationMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getUserAuthenticationMethod(UserAuthenticationMethodID, EntityID = 1, returnUserAuthenticationMethodID = True, returnAuthenticationMethodID = False, returnCreatedTime = False, returnModifiedTime = False, returnProviderUserIdentity = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserAuthenticationMethod/" + str(UserAuthenticationMethodID), verb = "get", return_params_list = return_params_list)

def modifyUserAuthenticationMethod(UserAuthenticationMethodID, EntityID = 1, setAuthenticationMethodID = None, setProviderUserIdentity = None, setUserID = None, setRelationships = None, returnUserAuthenticationMethodID = True, returnAuthenticationMethodID = False, returnCreatedTime = False, returnModifiedTime = False, returnProviderUserIdentity = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserAuthenticationMethod/" + str(UserAuthenticationMethodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createUserAuthenticationMethod(EntityID = 1, setAuthenticationMethodID = None, setProviderUserIdentity = None, setUserID = None, setRelationships = None, returnUserAuthenticationMethodID = True, returnAuthenticationMethodID = False, returnCreatedTime = False, returnModifiedTime = False, returnProviderUserIdentity = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserAuthenticationMethod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteUserAuthenticationMethod(UserAuthenticationMethodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryUserCalendarPreference(EntityID = 1, page = 1, pageSize = 100, returnUserCalendarPreferenceID = True, returnApprovedTimeOffEventBackgroundColor = False, returnBirthdayEventBackgroundColor = False, returnCalendarEventBackgroundColor = False, returnCalendarType = False, returnCalendarTypeCode = False, returnCreatedTime = False, returnDistrictActivityEventBackgroundColor = False, returnModifiedTime = False, returnPayDayEventBackgroundColor = False, returnSelectedView = False, returnShowAllMyEmployeesTimeOff = False, returnShowAllocatedTimeOff = False, returnShowBirthdays = False, returnShowCalendarEvents = False, returnShowDistrictActivityEvents = False, returnShowMyDirectEmployeesTimeOff = False, returnShowMyTimeOff = False, returnShowTransactionsIHadASubFor = False, returnShowTransactionsISubbedFor = False, returnShowWeekends = False, returnTransactionsIHadASubForEventBackgroundColor = False, returnTransactionsISubbedForEventBackgroundColor = False, returnUnapprovedTimeOffEventBackgroundColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserCalendarPreference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getUserCalendarPreference(UserCalendarPreferenceID, EntityID = 1, returnUserCalendarPreferenceID = True, returnApprovedTimeOffEventBackgroundColor = False, returnBirthdayEventBackgroundColor = False, returnCalendarEventBackgroundColor = False, returnCalendarType = False, returnCalendarTypeCode = False, returnCreatedTime = False, returnDistrictActivityEventBackgroundColor = False, returnModifiedTime = False, returnPayDayEventBackgroundColor = False, returnSelectedView = False, returnShowAllMyEmployeesTimeOff = False, returnShowAllocatedTimeOff = False, returnShowBirthdays = False, returnShowCalendarEvents = False, returnShowDistrictActivityEvents = False, returnShowMyDirectEmployeesTimeOff = False, returnShowMyTimeOff = False, returnShowTransactionsIHadASubFor = False, returnShowTransactionsISubbedFor = False, returnShowWeekends = False, returnTransactionsIHadASubForEventBackgroundColor = False, returnTransactionsISubbedForEventBackgroundColor = False, returnUnapprovedTimeOffEventBackgroundColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserCalendarPreference/" + str(UserCalendarPreferenceID), verb = "get", return_params_list = return_params_list)

def modifyUserCalendarPreference(UserCalendarPreferenceID, EntityID = 1, setApprovedTimeOffEventBackgroundColor = None, setBirthdayEventBackgroundColor = None, setCalendarEventBackgroundColor = None, setCalendarType = None, setCalendarTypeCode = None, setDistrictActivityEventBackgroundColor = None, setPayDayEventBackgroundColor = None, setSelectedView = None, setShowAllMyEmployeesTimeOff = None, setShowAllocatedTimeOff = None, setShowBirthdays = None, setShowCalendarEvents = None, setShowDistrictActivityEvents = None, setShowMyDirectEmployeesTimeOff = None, setShowMyTimeOff = None, setShowTransactionsIHadASubFor = None, setShowTransactionsISubbedFor = None, setShowWeekends = None, setTransactionsIHadASubForEventBackgroundColor = None, setTransactionsISubbedForEventBackgroundColor = None, setUnapprovedTimeOffEventBackgroundColor = None, setUserIDOwner = None, setRelationships = None, returnUserCalendarPreferenceID = True, returnApprovedTimeOffEventBackgroundColor = False, returnBirthdayEventBackgroundColor = False, returnCalendarEventBackgroundColor = False, returnCalendarType = False, returnCalendarTypeCode = False, returnCreatedTime = False, returnDistrictActivityEventBackgroundColor = False, returnModifiedTime = False, returnPayDayEventBackgroundColor = False, returnSelectedView = False, returnShowAllMyEmployeesTimeOff = False, returnShowAllocatedTimeOff = False, returnShowBirthdays = False, returnShowCalendarEvents = False, returnShowDistrictActivityEvents = False, returnShowMyDirectEmployeesTimeOff = False, returnShowMyTimeOff = False, returnShowTransactionsIHadASubFor = False, returnShowTransactionsISubbedFor = False, returnShowWeekends = False, returnTransactionsIHadASubForEventBackgroundColor = False, returnTransactionsISubbedForEventBackgroundColor = False, returnUnapprovedTimeOffEventBackgroundColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserCalendarPreference/" + str(UserCalendarPreferenceID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createUserCalendarPreference(EntityID = 1, setApprovedTimeOffEventBackgroundColor = None, setBirthdayEventBackgroundColor = None, setCalendarEventBackgroundColor = None, setCalendarType = None, setCalendarTypeCode = None, setDistrictActivityEventBackgroundColor = None, setPayDayEventBackgroundColor = None, setSelectedView = None, setShowAllMyEmployeesTimeOff = None, setShowAllocatedTimeOff = None, setShowBirthdays = None, setShowCalendarEvents = None, setShowDistrictActivityEvents = None, setShowMyDirectEmployeesTimeOff = None, setShowMyTimeOff = None, setShowTransactionsIHadASubFor = None, setShowTransactionsISubbedFor = None, setShowWeekends = None, setTransactionsIHadASubForEventBackgroundColor = None, setTransactionsISubbedForEventBackgroundColor = None, setUnapprovedTimeOffEventBackgroundColor = None, setUserIDOwner = None, setRelationships = None, returnUserCalendarPreferenceID = True, returnApprovedTimeOffEventBackgroundColor = False, returnBirthdayEventBackgroundColor = False, returnCalendarEventBackgroundColor = False, returnCalendarType = False, returnCalendarTypeCode = False, returnCreatedTime = False, returnDistrictActivityEventBackgroundColor = False, returnModifiedTime = False, returnPayDayEventBackgroundColor = False, returnSelectedView = False, returnShowAllMyEmployeesTimeOff = False, returnShowAllocatedTimeOff = False, returnShowBirthdays = False, returnShowCalendarEvents = False, returnShowDistrictActivityEvents = False, returnShowMyDirectEmployeesTimeOff = False, returnShowMyTimeOff = False, returnShowTransactionsIHadASubFor = False, returnShowTransactionsISubbedFor = False, returnShowWeekends = False, returnTransactionsIHadASubForEventBackgroundColor = False, returnTransactionsISubbedForEventBackgroundColor = False, returnUnapprovedTimeOffEventBackgroundColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserCalendarPreference/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteUserCalendarPreference(UserCalendarPreferenceID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryUserImport(EntityID = 1, page = 1, pageSize = 100, returnUserImportID = True, returnAboveChangeThreshold = False, returnAboveDeleteThreshold = False, returnCreatedTime = False, returnDateExecuted = False, returnHasErrors = False, returnMediaID = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImport/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getUserImport(UserImportID, EntityID = 1, returnUserImportID = True, returnAboveChangeThreshold = False, returnAboveDeleteThreshold = False, returnCreatedTime = False, returnDateExecuted = False, returnHasErrors = False, returnMediaID = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImport/" + str(UserImportID), verb = "get", return_params_list = return_params_list)

def modifyUserImport(UserImportID, EntityID = 1, setAboveChangeThreshold = None, setAboveDeleteThreshold = None, setDateExecuted = None, setMediaID = None, setStatus = None, setStatusCode = None, setRelationships = None, returnUserImportID = True, returnAboveChangeThreshold = False, returnAboveDeleteThreshold = False, returnCreatedTime = False, returnDateExecuted = False, returnHasErrors = False, returnMediaID = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImport/" + str(UserImportID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createUserImport(EntityID = 1, setAboveChangeThreshold = None, setAboveDeleteThreshold = None, setDateExecuted = None, setMediaID = None, setStatus = None, setStatusCode = None, setRelationships = None, returnUserImportID = True, returnAboveChangeThreshold = False, returnAboveDeleteThreshold = False, returnCreatedTime = False, returnDateExecuted = False, returnHasErrors = False, returnMediaID = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImport/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteUserImport(UserImportID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryUserImportResult(EntityID = 1, page = 1, pageSize = 100, returnUserImportResultID = True, returnCreatedTime = False, returnEntityCode = False, returnGroupMembershipChangeType = False, returnGroupMembershipChangeTypeCode = False, returnGroupName = False, returnHasErrors = False, returnIsStaff = False, returnLineNumber = False, returnModifiedTime = False, returnNameChangeType = False, returnNameChangeTypeCode = False, returnSchoolYear = False, returnStaffChangeType = False, returnStaffChangeTypeCode = False, returnUserChangeType = False, returnUserChangeTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportID = False, returnUsername = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImportResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getUserImportResult(UserImportResultID, EntityID = 1, returnUserImportResultID = True, returnCreatedTime = False, returnEntityCode = False, returnGroupMembershipChangeType = False, returnGroupMembershipChangeTypeCode = False, returnGroupName = False, returnHasErrors = False, returnIsStaff = False, returnLineNumber = False, returnModifiedTime = False, returnNameChangeType = False, returnNameChangeTypeCode = False, returnSchoolYear = False, returnStaffChangeType = False, returnStaffChangeTypeCode = False, returnUserChangeType = False, returnUserChangeTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportID = False, returnUsername = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImportResult/" + str(UserImportResultID), verb = "get", return_params_list = return_params_list)

def modifyUserImportResult(UserImportResultID, EntityID = 1, setEntityCode = None, setGroupMembershipChangeType = None, setGroupMembershipChangeTypeCode = None, setGroupName = None, setIsStaff = None, setLineNumber = None, setNameChangeType = None, setNameChangeTypeCode = None, setSchoolYear = None, setStaffChangeType = None, setStaffChangeTypeCode = None, setUserChangeType = None, setUserChangeTypeCode = None, setUserImportID = None, setUsername = None, setRelationships = None, returnUserImportResultID = True, returnCreatedTime = False, returnEntityCode = False, returnGroupMembershipChangeType = False, returnGroupMembershipChangeTypeCode = False, returnGroupName = False, returnHasErrors = False, returnIsStaff = False, returnLineNumber = False, returnModifiedTime = False, returnNameChangeType = False, returnNameChangeTypeCode = False, returnSchoolYear = False, returnStaffChangeType = False, returnStaffChangeTypeCode = False, returnUserChangeType = False, returnUserChangeTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportID = False, returnUsername = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImportResult/" + str(UserImportResultID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createUserImportResult(EntityID = 1, setEntityCode = None, setGroupMembershipChangeType = None, setGroupMembershipChangeTypeCode = None, setGroupName = None, setIsStaff = None, setLineNumber = None, setNameChangeType = None, setNameChangeTypeCode = None, setSchoolYear = None, setStaffChangeType = None, setStaffChangeTypeCode = None, setUserChangeType = None, setUserChangeTypeCode = None, setUserImportID = None, setUsername = None, setRelationships = None, returnUserImportResultID = True, returnCreatedTime = False, returnEntityCode = False, returnGroupMembershipChangeType = False, returnGroupMembershipChangeTypeCode = False, returnGroupName = False, returnHasErrors = False, returnIsStaff = False, returnLineNumber = False, returnModifiedTime = False, returnNameChangeType = False, returnNameChangeTypeCode = False, returnSchoolYear = False, returnStaffChangeType = False, returnStaffChangeTypeCode = False, returnUserChangeType = False, returnUserChangeTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportID = False, returnUsername = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImportResult/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteUserImportResult(UserImportResultID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryUserImportResultError(EntityID = 1, page = 1, pageSize = 100, returnUserImportResultErrorID = True, returnCreatedTime = False, returnErrorMessage = False, returnFieldName = False, returnFromPreview = False, returnModifiedTime = False, returnObjectName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportResultID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImportResultError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getUserImportResultError(UserImportResultErrorID, EntityID = 1, returnUserImportResultErrorID = True, returnCreatedTime = False, returnErrorMessage = False, returnFieldName = False, returnFromPreview = False, returnModifiedTime = False, returnObjectName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportResultID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImportResultError/" + str(UserImportResultErrorID), verb = "get", return_params_list = return_params_list)

def modifyUserImportResultError(UserImportResultErrorID, EntityID = 1, setErrorMessage = None, setFieldName = None, setFromPreview = None, setObjectName = None, setUserImportResultID = None, setRelationships = None, returnUserImportResultErrorID = True, returnCreatedTime = False, returnErrorMessage = False, returnFieldName = False, returnFromPreview = False, returnModifiedTime = False, returnObjectName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportResultID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImportResultError/" + str(UserImportResultErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createUserImportResultError(EntityID = 1, setErrorMessage = None, setFieldName = None, setFromPreview = None, setObjectName = None, setUserImportResultID = None, setRelationships = None, returnUserImportResultErrorID = True, returnCreatedTime = False, returnErrorMessage = False, returnFieldName = False, returnFromPreview = False, returnModifiedTime = False, returnObjectName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportResultID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImportResultError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteUserImportResultError(UserImportResultErrorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryUserPasswordReset(EntityID = 1, page = 1, pageSize = 100, returnUserPasswordResetID = True, returnCreatedTime = False, returnExpirationTime = False, returnModifiedTime = False, returnResetGuid = False, returnResetSalt = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserPasswordReset/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getUserPasswordReset(UserPasswordResetID, EntityID = 1, returnUserPasswordResetID = True, returnCreatedTime = False, returnExpirationTime = False, returnModifiedTime = False, returnResetGuid = False, returnResetSalt = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserPasswordReset/" + str(UserPasswordResetID), verb = "get", return_params_list = return_params_list)

def modifyUserPasswordReset(UserPasswordResetID, EntityID = 1, setExpirationTime = None, setResetGuid = None, setResetSalt = None, setUserID = None, setRelationships = None, returnUserPasswordResetID = True, returnCreatedTime = False, returnExpirationTime = False, returnModifiedTime = False, returnResetGuid = False, returnResetSalt = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserPasswordReset/" + str(UserPasswordResetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createUserPasswordReset(EntityID = 1, setExpirationTime = None, setResetGuid = None, setResetSalt = None, setUserID = None, setRelationships = None, returnUserPasswordResetID = True, returnCreatedTime = False, returnExpirationTime = False, returnModifiedTime = False, returnResetGuid = False, returnResetSalt = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserPasswordReset/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteUserPasswordReset(UserPasswordResetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryUserPreference(EntityID = 1, page = 1, pageSize = 100, returnUserPreferenceID = True, returnAccountSelection = False, returnAccountSelectionCode = False, returnCreatedTime = False, returnModifiedTime = False, returnThemeID = False, returnUseEmailMultifactorAuthentication = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSecurity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserPreference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getUserPreference(UserPreferenceID, EntityID = 1, returnUserPreferenceID = True, returnAccountSelection = False, returnAccountSelectionCode = False, returnCreatedTime = False, returnModifiedTime = False, returnThemeID = False, returnUseEmailMultifactorAuthentication = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSecurity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserPreference/" + str(UserPreferenceID), verb = "get", return_params_list = return_params_list)

def modifyUserPreference(UserPreferenceID, EntityID = 1, setAccountSelection = None, setAccountSelectionCode = None, setThemeID = None, setUseEmailMultifactorAuthentication = None, setUserIDSecurity = None, setRelationships = None, returnUserPreferenceID = True, returnAccountSelection = False, returnAccountSelectionCode = False, returnCreatedTime = False, returnModifiedTime = False, returnThemeID = False, returnUseEmailMultifactorAuthentication = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSecurity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserPreference/" + str(UserPreferenceID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createUserPreference(EntityID = 1, setAccountSelection = None, setAccountSelectionCode = None, setThemeID = None, setUseEmailMultifactorAuthentication = None, setUserIDSecurity = None, setRelationships = None, returnUserPreferenceID = True, returnAccountSelection = False, returnAccountSelectionCode = False, returnCreatedTime = False, returnModifiedTime = False, returnThemeID = False, returnUseEmailMultifactorAuthentication = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSecurity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserPreference/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteUserPreference(UserPreferenceID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryUserProfileData(EntityID = 1, page = 1, pageSize = 100, returnUserProfileDataID = True, returnBrowseObject = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnRelatedRecord = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserProfileData/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getUserProfileData(UserProfileDataID, EntityID = 1, returnUserProfileDataID = True, returnBrowseObject = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnRelatedRecord = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserProfileData/" + str(UserProfileDataID), verb = "get", return_params_list = return_params_list)

def modifyUserProfileData(UserProfileDataID, EntityID = 1, setBrowseObject = None, setModule = None, setRelatedRecord = None, setUserID = None, setRelationships = None, returnUserProfileDataID = True, returnBrowseObject = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnRelatedRecord = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserProfileData/" + str(UserProfileDataID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createUserProfileData(EntityID = 1, setBrowseObject = None, setModule = None, setRelatedRecord = None, setUserID = None, setRelationships = None, returnUserProfileDataID = True, returnBrowseObject = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnRelatedRecord = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserProfileData/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteUserProfileData(UserProfileDataID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryUserProfileTabStatus(EntityID = 1, page = 1, pageSize = 100, returnUserProfileTabStatusID = True, returnCreatedTime = False, returnModifiedTime = False, returnOpenTabs = False, returnProfileID = False, returnProfileScreenIDLastTab = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserProfileTabStatus/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getUserProfileTabStatus(UserProfileTabStatusID, EntityID = 1, returnUserProfileTabStatusID = True, returnCreatedTime = False, returnModifiedTime = False, returnOpenTabs = False, returnProfileID = False, returnProfileScreenIDLastTab = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserProfileTabStatus/" + str(UserProfileTabStatusID), verb = "get", return_params_list = return_params_list)

def modifyUserProfileTabStatus(UserProfileTabStatusID, EntityID = 1, setProfileID = None, setProfileScreenIDLastTab = None, setUserID = None, setRelationships = None, returnUserProfileTabStatusID = True, returnCreatedTime = False, returnModifiedTime = False, returnOpenTabs = False, returnProfileID = False, returnProfileScreenIDLastTab = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserProfileTabStatus/" + str(UserProfileTabStatusID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createUserProfileTabStatus(EntityID = 1, setProfileID = None, setProfileScreenIDLastTab = None, setUserID = None, setRelationships = None, returnUserProfileTabStatusID = True, returnCreatedTime = False, returnModifiedTime = False, returnOpenTabs = False, returnProfileID = False, returnProfileScreenIDLastTab = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserProfileTabStatus/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteUserProfileTabStatus(UserProfileTabStatusID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryUserSetting(EntityID = 1, page = 1, pageSize = 100, returnUserSettingID = True, returnAction = False, returnArea = False, returnCode = False, returnController = False, returnCreatedTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getUserSetting(UserSettingID, EntityID = 1, returnUserSettingID = True, returnAction = False, returnArea = False, returnCode = False, returnController = False, returnCreatedTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserSetting/" + str(UserSettingID), verb = "get", return_params_list = return_params_list)

def modifyUserSetting(UserSettingID, EntityID = 1, setAction = None, setArea = None, setCode = None, setController = None, setUserID = None, setValue = None, setRelationships = None, returnUserSettingID = True, returnAction = False, returnArea = False, returnCode = False, returnController = False, returnCreatedTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserSetting/" + str(UserSettingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createUserSetting(EntityID = 1, setAction = None, setArea = None, setCode = None, setController = None, setUserID = None, setValue = None, setRelationships = None, returnUserSettingID = True, returnAction = False, returnArea = False, returnCode = False, returnController = False, returnCreatedTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserSetting/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteUserSetting(UserSettingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryUserStudentCalendarPreference(EntityID = 1, page = 1, pageSize = 100, returnUserStudentCalendarPreferenceID = True, returnAssignmentBackgroundColor = False, returnCreatedTime = False, returnModifiedTime = False, returnShowAssignments = False, returnShowStudentActivityEvents = False, returnStudentActivityEventBackgroundColor = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserStudentCalendarPreference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getUserStudentCalendarPreference(UserStudentCalendarPreferenceID, EntityID = 1, returnUserStudentCalendarPreferenceID = True, returnAssignmentBackgroundColor = False, returnCreatedTime = False, returnModifiedTime = False, returnShowAssignments = False, returnShowStudentActivityEvents = False, returnStudentActivityEventBackgroundColor = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserStudentCalendarPreference/" + str(UserStudentCalendarPreferenceID), verb = "get", return_params_list = return_params_list)

def modifyUserStudentCalendarPreference(UserStudentCalendarPreferenceID, EntityID = 1, setAssignmentBackgroundColor = None, setShowAssignments = None, setShowStudentActivityEvents = None, setStudentActivityEventBackgroundColor = None, setStudentID = None, setUserIDOwner = None, setRelationships = None, returnUserStudentCalendarPreferenceID = True, returnAssignmentBackgroundColor = False, returnCreatedTime = False, returnModifiedTime = False, returnShowAssignments = False, returnShowStudentActivityEvents = False, returnStudentActivityEventBackgroundColor = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserStudentCalendarPreference/" + str(UserStudentCalendarPreferenceID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createUserStudentCalendarPreference(EntityID = 1, setAssignmentBackgroundColor = None, setShowAssignments = None, setShowStudentActivityEvents = None, setStudentActivityEventBackgroundColor = None, setStudentID = None, setUserIDOwner = None, setRelationships = None, returnUserStudentCalendarPreferenceID = True, returnAssignmentBackgroundColor = False, returnCreatedTime = False, returnModifiedTime = False, returnShowAssignments = False, returnShowStudentActivityEvents = False, returnStudentActivityEventBackgroundColor = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserStudentCalendarPreference/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteUserStudentCalendarPreference(UserStudentCalendarPreferenceID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryUser(EntityID = 1, page = 1, pageSize = 100, returnUserID = True, returnAccessCode = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnCurrentPortal = False, returnCurrentPortalCode = False, returnCustomerAccessID = False, returnDatabaseUsername = False, returnDockDisplayOpen = False, returnEffectiveAuthenticationRoleID = False, returnEffectiveAuthenticationRoleName = False, returnEffectiveCachedAuthenticationRole = False, returnEffectiveMultifactorAuthenticationCode = False, returnEffectiveMultifactorAuthenticationID = False, returnEmulatingMobile = False, returnEntityIDCurrent = False, returnFailedMultifactorAuthenticationCount = False, returnFailedSignInCount = False, returnFiscalYearIDCurrent = False, returnForcePasswordChange = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnIsActive = False, returnIsDeleted = False, returnIsExpired = False, returnIsLockedOut = False, returnIsSuperUser = False, returnLastPasswordChangeTime = False, returnLockedOutTime = False, returnMessageCount = False, returnModifiedTime = False, returnMultifactorAuthenticationID = False, returnNameID = False, returnPassword = False, returnPasswordExpirationDate = False, returnPasswordHash = False, returnPasswordSalt = False, returnPasswordStrategy = False, returnPasswordStrategyCode = False, returnRolesAuthenticationRoleID = False, returnRolesMultifactorAuthenticationID = False, returnUserHasAccessToReport = False, returnUserHasFamilyAccess = False, returnUserHasStudentAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsername = False, returnUserUncachedID = False, returnUsesSkywardAuthentication = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/User/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getUser(UserID, EntityID = 1, returnUserID = True, returnAccessCode = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnCurrentPortal = False, returnCurrentPortalCode = False, returnCustomerAccessID = False, returnDatabaseUsername = False, returnDockDisplayOpen = False, returnEffectiveAuthenticationRoleID = False, returnEffectiveAuthenticationRoleName = False, returnEffectiveCachedAuthenticationRole = False, returnEffectiveMultifactorAuthenticationCode = False, returnEffectiveMultifactorAuthenticationID = False, returnEmulatingMobile = False, returnEntityIDCurrent = False, returnFailedMultifactorAuthenticationCount = False, returnFailedSignInCount = False, returnFiscalYearIDCurrent = False, returnForcePasswordChange = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnIsActive = False, returnIsDeleted = False, returnIsExpired = False, returnIsLockedOut = False, returnIsSuperUser = False, returnLastPasswordChangeTime = False, returnLockedOutTime = False, returnMessageCount = False, returnModifiedTime = False, returnMultifactorAuthenticationID = False, returnNameID = False, returnPassword = False, returnPasswordExpirationDate = False, returnPasswordHash = False, returnPasswordSalt = False, returnPasswordStrategy = False, returnPasswordStrategyCode = False, returnRolesAuthenticationRoleID = False, returnRolesMultifactorAuthenticationID = False, returnUserHasAccessToReport = False, returnUserHasFamilyAccess = False, returnUserHasStudentAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsername = False, returnUserUncachedID = False, returnUsesSkywardAuthentication = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/User/" + str(UserID), verb = "get", return_params_list = return_params_list)

def modifyUser(UserID, EntityID = 1, setAccessCode = None, setAuthenticationRoleID = None, setCurrentPortal = None, setCurrentPortalCode = None, setCustomerAccessID = None, setDatabaseUsername = None, setDockDisplayOpen = None, setEmulatingMobile = None, setEntityIDCurrent = None, setFailedMultifactorAuthenticationCount = None, setFailedSignInCount = None, setFiscalYearIDCurrent = None, setForcePasswordChange = None, setFullNameFL = None, setFullNameFML = None, setFullNameLFM = None, setIsActive = None, setIsDeleted = None, setIsExpired = None, setIsSuperUser = None, setLastPasswordChangeTime = None, setLockedOutTime = None, setMultifactorAuthenticationID = None, setNameID = None, setPassword = None, setPasswordHash = None, setPasswordSalt = None, setPasswordStrategy = None, setPasswordStrategyCode = None, setUsername = None, setRelationships = None, returnUserID = True, returnAccessCode = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnCurrentPortal = False, returnCurrentPortalCode = False, returnCustomerAccessID = False, returnDatabaseUsername = False, returnDockDisplayOpen = False, returnEffectiveAuthenticationRoleID = False, returnEffectiveAuthenticationRoleName = False, returnEffectiveCachedAuthenticationRole = False, returnEffectiveMultifactorAuthenticationCode = False, returnEffectiveMultifactorAuthenticationID = False, returnEmulatingMobile = False, returnEntityIDCurrent = False, returnFailedMultifactorAuthenticationCount = False, returnFailedSignInCount = False, returnFiscalYearIDCurrent = False, returnForcePasswordChange = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnIsActive = False, returnIsDeleted = False, returnIsExpired = False, returnIsLockedOut = False, returnIsSuperUser = False, returnLastPasswordChangeTime = False, returnLockedOutTime = False, returnMessageCount = False, returnModifiedTime = False, returnMultifactorAuthenticationID = False, returnNameID = False, returnPassword = False, returnPasswordExpirationDate = False, returnPasswordHash = False, returnPasswordSalt = False, returnPasswordStrategy = False, returnPasswordStrategyCode = False, returnRolesAuthenticationRoleID = False, returnRolesMultifactorAuthenticationID = False, returnUserHasAccessToReport = False, returnUserHasFamilyAccess = False, returnUserHasStudentAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsername = False, returnUserUncachedID = False, returnUsesSkywardAuthentication = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/User/" + str(UserID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createUser(EntityID = 1, setAccessCode = None, setAuthenticationRoleID = None, setCurrentPortal = None, setCurrentPortalCode = None, setCustomerAccessID = None, setDatabaseUsername = None, setDockDisplayOpen = None, setEmulatingMobile = None, setEntityIDCurrent = None, setFailedMultifactorAuthenticationCount = None, setFailedSignInCount = None, setFiscalYearIDCurrent = None, setForcePasswordChange = None, setFullNameFL = None, setFullNameFML = None, setFullNameLFM = None, setIsActive = None, setIsDeleted = None, setIsExpired = None, setIsSuperUser = None, setLastPasswordChangeTime = None, setLockedOutTime = None, setMultifactorAuthenticationID = None, setNameID = None, setPassword = None, setPasswordHash = None, setPasswordSalt = None, setPasswordStrategy = None, setPasswordStrategyCode = None, setUsername = None, setRelationships = None, returnUserID = True, returnAccessCode = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnCurrentPortal = False, returnCurrentPortalCode = False, returnCustomerAccessID = False, returnDatabaseUsername = False, returnDockDisplayOpen = False, returnEffectiveAuthenticationRoleID = False, returnEffectiveAuthenticationRoleName = False, returnEffectiveCachedAuthenticationRole = False, returnEffectiveMultifactorAuthenticationCode = False, returnEffectiveMultifactorAuthenticationID = False, returnEmulatingMobile = False, returnEntityIDCurrent = False, returnFailedMultifactorAuthenticationCount = False, returnFailedSignInCount = False, returnFiscalYearIDCurrent = False, returnForcePasswordChange = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnIsActive = False, returnIsDeleted = False, returnIsExpired = False, returnIsLockedOut = False, returnIsSuperUser = False, returnLastPasswordChangeTime = False, returnLockedOutTime = False, returnMessageCount = False, returnModifiedTime = False, returnMultifactorAuthenticationID = False, returnNameID = False, returnPassword = False, returnPasswordExpirationDate = False, returnPasswordHash = False, returnPasswordSalt = False, returnPasswordStrategy = False, returnPasswordStrategyCode = False, returnRolesAuthenticationRoleID = False, returnRolesMultifactorAuthenticationID = False, returnUserHasAccessToReport = False, returnUserHasFamilyAccess = False, returnUserHasStudentAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsername = False, returnUserUncachedID = False, returnUsesSkywardAuthentication = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/User/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteUser(UserID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")