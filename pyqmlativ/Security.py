# This module contains Security functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryAuthenticationAssertion(searchConditions = [], EntityID = 1, returnAuthenticationAssertionID = False, returnAssertionGuid = False, returnAuthenticationMethodID = False, returnCreatedTime = False, returnMobileDevice = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AuthenticationAssertion in the district.

	This function returns a dataframe of every AuthenticationAssertion in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationAssertion/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationAssertion/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAuthenticationMethod(searchConditions = [], EntityID = 1, returnAuthenticationMethodID = False, returnCertificate = False, returnCompareNameIDAsNumeric = False, returnCreatedTime = False, returnIsSkywardMaintained = False, returnMetadata = False, returnMetadataURL = False, returnModifiedTime = False, returnName = False, returnNameIdentifierSkywardField = False, returnNameIdentifierSkywardFieldFriendlyName = False, returnNameIdentifierType = False, returnSkywardHash = False, returnSkywardID = False, returnSSOURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AuthenticationMethod in the district.

	This function returns a dataframe of every AuthenticationMethod in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationMethod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAuthenticationRole(searchConditions = [], EntityID = 1, returnAuthenticationRoleID = False, returnAllowSkywardCredentials = False, returnCreatedTime = False, returnDisplayText = False, returnHasAuthenticationMethod = False, returnHasLDAPProvider = False, returnMediaID = False, returnModifiedTime = False, returnName = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AuthenticationRole in the district.

	This function returns a dataframe of every AuthenticationRole in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRole/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRole/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAuthenticationRoleLDAPProvider(searchConditions = [], EntityID = 1, returnAuthenticationRoleLDAPProviderID = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnLDAPProviderID = False, returnModifiedTime = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AuthenticationRoleLDAPProvider in the district.

	This function returns a dataframe of every AuthenticationRoleLDAPProvider in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRoleLDAPProvider/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRoleLDAPProvider/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAuthenticationRoleMethod(searchConditions = [], EntityID = 1, returnAuthenticationRoleMethodID = False, returnAuthenticationMethodID = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AuthenticationRoleMethod in the district.

	This function returns a dataframe of every AuthenticationRoleMethod in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRoleMethod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRoleMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBrowseFieldPath(searchConditions = [], EntityID = 1, returnBrowseFieldPathID = False, returnBrowseID = False, returnCreatedTime = False, returnFieldPath = False, returnGuidFieldPath = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnRoleID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BrowseFieldPath in the district.

	This function returns a dataframe of every BrowseFieldPath in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/BrowseFieldPath/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/BrowseFieldPath/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigSystem(searchConditions = [], EntityID = 1, returnConfigSystemID = False, returnAccessCodeLength = False, returnAdminEmployeeTeacherActivityAllowUsernameChange = False, returnAdminMissedSessionPingCountLimit = False, returnAdminSessionClientPingSeconds = False, returnAdminSessionTimeoutSeconds = False, returnAdminSessionWarnSeconds = False, returnAuthenticationRoleIDActivity = False, returnAuthenticationRoleIDAdministrative = False, returnAuthenticationRoleIDEmployee = False, returnAuthenticationRoleIDFamilyNewStudentEnrollment = False, returnAuthenticationRoleIDStudent = False, returnAuthenticationRoleIDTeacher = False, returnAutogenerateEmployeeAccessCodes = False, returnAutogenerateStaffAccessCodes = False, returnAutogenerateStudentAccessCodes = False, returnCombineAuthenticationRolesOnSignIn = False, returnCreatedTime = False, returnDaysUntilPasswordExpires = False, returnFailedSignInCountLimit = False, returnFamilyAllowUsernameChange = False, returnFamilyStudentEmployeeMissedSessionPingCountLimit = False, returnFamilyStudentEmployeeSessionClientPingSeconds = False, returnFamilyStudentEmployeeSessionTimeoutSeconds = False, returnFamilyStudentEmployeeSessionWarnSeconds = False, returnForcePasswordExpirationOnSkywardLoginIfPasswordRequirementsNotMet = False, returnLoginLockRetryDelayMinutes = False, returnMaximumPasswordLength = False, returnMinimumPasswordLength = False, returnModifiedTime = False, returnMultifactorAuthenticationIDActivity = False, returnMultifactorAuthenticationIDAdministrative = False, returnMultifactorAuthenticationIDEmployee = False, returnMultifactorAuthenticationIDFamilyNewStudentEnrollment = False, returnMultifactorAuthenticationIDStudent = False, returnMultifactorAuthenticationIDTeacher = False, returnRequiredNumericCharacters = False, returnRequiredSpecialCharacters = False, returnSessionAccessDeniedLimit = False, returnStudentAllowUsernameChange = False, returnTeacherMissedSessionPingCountLimit = False, returnTeacherSessionClientPingSeconds = False, returnTeacherSessionTimeoutSeconds = False, returnTeacherSessionWarnSeconds = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportChangeThreshold = False, returnUserImportDeleteThreshold = False, returnUserImportFilePath = False, returnUserImportFileType = False, returnUserImportFileTypeCode = False, returnUserImportShouldMaintainExistingUsers = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ConfigSystem in the district.

	This function returns a dataframe of every ConfigSystem in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDataObjectFieldPath(searchConditions = [], EntityID = 1, returnDataObjectFieldPathID = False, returnCreatedTime = False, returnDisplayLevel = False, returnExactSystemTypeName = False, returnField = False, returnFieldIDSkySys = False, returnFieldPath = False, returnFriendlyName = False, returnGuidFieldPath = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnNumberOfRelationships = False, returnObjectID = False, returnObjectSchemaObject = False, returnRoleID = False, returnSkywardDisplayLevel = False, returnSkywardDisplayLevelCode = False, returnSkywardFriendlyName = False, returnSkywardHash = False, returnSkywardID = False, returnUserDisplayLevel = False, returnUserDisplayLevelCode = False, returnUserFriendlyName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DataObjectFieldPath in the district.

	This function returns a dataframe of every DataObjectFieldPath in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/DataObjectFieldPath/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/DataObjectFieldPath/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicSignature(searchConditions = [], EntityID = 1, returnElectronicSignatureID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEntityID = False, returnEntityName = False, returnIsForGrading = False, returnIsForPurchasing = False, returnIsForStateReporting = False, returnMediaID = False, returnModifiedTime = False, returnSignatureLocationKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicSignature in the district.

	This function returns a dataframe of every ElectronicSignature in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ElectronicSignature/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ElectronicSignature/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryFieldRestriction(searchConditions = [], EntityID = 1, returnFieldRestrictionID = False, returnCreatedTime = False, returnFieldID = False, returnModifiedTime = False, returnName = False, returnRestrictionType = False, returnRestrictionTypeCode = False, returnRoleSetType = False, returnRoleSetTypeCode = False, returnRoleSetTypeRequiresRoles = False, returnScreenSetType = False, returnScreenSetTypeCode = False, returnScreenSetTypeRequiresScreens = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every FieldRestriction in the district.

	This function returns a dataframe of every FieldRestriction in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestriction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestriction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryFieldRestrictionRole(searchConditions = [], EntityID = 1, returnFieldRestrictionRoleID = False, returnCreatedTime = False, returnFieldRestrictionID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every FieldRestrictionRole in the district.

	This function returns a dataframe of every FieldRestrictionRole in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestrictionRole/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestrictionRole/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryFieldRestrictionScreen(searchConditions = [], EntityID = 1, returnFieldRestrictionScreenID = False, returnCreatedTime = False, returnFieldRestrictionID = False, returnModifiedTime = False, returnSecurityLocationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every FieldRestrictionScreen in the district.

	This function returns a dataframe of every FieldRestrictionScreen in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestrictionScreen/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestrictionScreen/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGroup(searchConditions = [], EntityID = 1, returnGroupID = False, returnAutoAddToUserType = False, returnAutoAddToUserTypeCode = False, returnCreatedTime = False, returnDescription = False, returnEdFiStaffClassificationID = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnPositionTitleOverride = False, returnUsedForEmployeeAccess = False, returnUsedForFamilyAccess = False, returnUsedForNewStudentEnrollment = False, returnUsedForStudentAccess = False, returnUsedForTeacherAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Group in the district.

	This function returns a dataframe of every Group in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Group/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Group/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGroupEntityAutoAdd(searchConditions = [], EntityID = 1, returnGroupEntityAutoAddID = False, returnCreatedTime = False, returnEntityID = False, returnGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GroupEntityAutoAdd in the district.

	This function returns a dataframe of every GroupEntityAutoAdd in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupEntityAutoAdd/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupEntityAutoAdd/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGroupImpersonationRole(searchConditions = [], EntityID = 1, returnGroupImpersonationRoleID = False, returnCreatedTime = False, returnGroupID = False, returnIsReadOnly = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GroupImpersonationRole in the district.

	This function returns a dataframe of every GroupImpersonationRole in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupImpersonationRole/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupImpersonationRole/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGroupLDAPSynchronization(searchConditions = [], EntityID = 1, returnGroupLDAPSynchronizationID = False, returnCommonName = False, returnCreatedTime = False, returnDistinguishedName = False, returnEntityID = False, returnGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GroupLDAPSynchronization in the district.

	This function returns a dataframe of every GroupLDAPSynchronization in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupLDAPSynchronization/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupLDAPSynchronization/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGroupMembership(searchConditions = [], EntityID = 1, returnGroupMembershipID = False, returnCreatedTime = False, returnEntityID = False, returnExternalUniqueIdentifier = False, returnGroupIDParent = False, returnMembershipSource = False, returnMembershipSourceCode = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDMember = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GroupMembership in the district.

	This function returns a dataframe of every GroupMembership in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupMembership/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupMembership/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGroupRole(searchConditions = [], EntityID = 1, returnGroupRoleID = False, returnCreatedTime = False, returnGroupID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GroupRole in the district.

	This function returns a dataframe of every GroupRole in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupRole/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupRole/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryImpersonation(searchConditions = [], EntityID = 1, returnImpersonationID = False, returnCreatedTime = False, returnImpersonationEnded = False, returnImpersonationStarted = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDImpersonated = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Impersonation in the district.

	This function returns a dataframe of every Impersonation in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Impersonation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Impersonation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryIPRange(searchConditions = [], EntityID = 1, returnIPRangeID = False, returnCreatedTime = False, returnDescription = False, returnHigh = False, returnIPAddressHigh = False, returnIPAddressLow = False, returnLow = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every IPRange in the district.

	This function returns a dataframe of every IPRange in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/IPRange/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/IPRange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryLDAPGroup(searchConditions = [], EntityID = 1, returnLDAPGroupID = False, returnCommonName = False, returnCreatedTime = False, returnDistinguishedName = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every LDAPGroup in the district.

	This function returns a dataframe of every LDAPGroup in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/LDAPGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/LDAPGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryLDAPProvider(searchConditions = [], EntityID = 1, returnLDAPProviderID = False, returnCreatedTime = False, returnDisableReferrals = False, returnDomainName = False, returnGroupBaseDN = False, returnGroupFilter = False, returnGroupMemberFilter = False, returnHost = False, returnIgnoreCertificationErrors = False, returnModifiedTime = False, returnName = False, returnPort = False, returnProtocol = False, returnProtocolCode = False, returnSearchBaseDN = False, returnSearchFilter = False, returnSearchPassword = False, returnSearchUserDN = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsernameAttribute = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every LDAPProvider in the district.

	This function returns a dataframe of every LDAPProvider in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/LDAPProvider/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/LDAPProvider/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMenuSecurityItem(searchConditions = [], EntityID = 1, returnMenuSecurityItemID = False, returnCreatedTime = False, returnMenuScreenID = False, returnModifiedTime = False, returnProfileScreenID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MenuSecurityItem in the district.

	This function returns a dataframe of every MenuSecurityItem in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MenuSecurityItem/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MenuSecurityItem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMobileSSO(searchConditions = [], EntityID = 1, returnMobileSSOID = False, returnCreatedTime = False, returnMobileDevice = False, returnModifiedTime = False, returnSSOToken = False, returnSSOTokenExpirationDate = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MobileSSO in the district.

	This function returns a dataframe of every MobileSSO in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MobileSSO/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MobileSSO/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMultifactorAuthentication(searchConditions = [], EntityID = 1, returnMultifactorAuthenticationID = False, returnCode = False, returnCreatedTime = False, returnDaysToExpiration = False, returnDescription = False, returnIsRequired = False, returnModifiedTime = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsesEmail = False, returnUsesSMS = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MultifactorAuthentication in the district.

	This function returns a dataframe of every MultifactorAuthentication in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MultifactorAuthentication/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MultifactorAuthentication/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMultifactorAuthenticationAssertion(searchConditions = [], EntityID = 1, returnMultifactorAuthenticationAssertionID = False, returnAssertionCode = False, returnAssertionIdentifier = False, returnCreatedTime = False, returnExpirationTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MultifactorAuthenticationAssertion in the district.

	This function returns a dataframe of every MultifactorAuthenticationAssertion in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MultifactorAuthenticationAssertion/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MultifactorAuthenticationAssertion/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryProduct(searchConditions = [], EntityID = 1, returnProductID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnRMSID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Product in the district.

	This function returns a dataframe of every Product in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Product/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Product/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryProductModulePath(searchConditions = [], EntityID = 1, returnProductModulePathID = False, returnController = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnProductID = False, returnScreen = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ProductModulePath in the district.

	This function returns a dataframe of every ProductModulePath in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ProductModulePath/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ProductModulePath/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryProductOwned(searchConditions = [], EntityID = 1, returnProductOwnedID = False, returnCreatedTime = False, returnEndDate = False, returnExpirationDate = False, returnModifiedTime = False, returnProductID = False, returnRMSID = False, returnStartDate = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ProductOwned in the district.

	This function returns a dataframe of every ProductOwned in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ProductOwned/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ProductOwned/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryRole(searchConditions = [], EntityID = 1, returnRoleID = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnDescription = False, returnDocumentationPersona = False, returnDocumentationPersonaCode = False, returnIsActive = False, returnModifiedTime = False, returnMultifactorAuthenticationID = False, returnName = False, returnReportCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Role in the district.

	This function returns a dataframe of every Role in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Role/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Role/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryRoleAttachmentType(searchConditions = [], EntityID = 1, returnRoleMenuSecurityItemID = False, returnAllowCreate = False, returnAllowDelete = False, returnAllowRead = False, returnAllowUpdate = False, returnAttachmentTypeID = False, returnPortal = False, returnPortalCode = False, returnRoleID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every RoleAttachmentType in the district.

	This function returns a dataframe of every RoleAttachmentType in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleAttachmentType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleAttachmentType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryRoleField(searchConditions = [], EntityID = 1, returnRoleFieldID = False, returnAllowRead = False, returnCreatedTime = False, returnField = False, returnFullField = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every RoleField in the district.

	This function returns a dataframe of every RoleField in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleField/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleField/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryRoleIPRange(searchConditions = [], EntityID = 1, returnRoleIPRangeID = False, returnCreatedTime = False, returnIPRangeID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every RoleIPRange in the district.

	This function returns a dataframe of every RoleIPRange in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleIPRange/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleIPRange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryRoleMenuSecurityItem(searchConditions = [], EntityID = 1, returnRoleMenuSecurityItemID = False, returnAllowCreate = False, returnAllowDelete = False, returnAllowMassCreate = False, returnAllowMassDelete = False, returnAllowMassUpdate = False, returnAllowRead = False, returnAllowUpdate = False, returnCreatedTime = False, returnMenuSecurityItemID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every RoleMenuSecurityItem in the district.

	This function returns a dataframe of every RoleMenuSecurityItem in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleMenuSecurityItem/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleMenuSecurityItem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryRoleModulePath(searchConditions = [], EntityID = 1, returnRoleModulePathID = False, returnAllowCreate = False, returnAllowDelete = False, returnAllowMassCreate = False, returnAllowMassDelete = False, returnAllowMassUpdate = False, returnAllowRead = False, returnAllowUpdate = False, returnCreatedTime = False, returnModifiedTime = False, returnModulePath = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every RoleModulePath in the district.

	This function returns a dataframe of every RoleModulePath in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleModulePath/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleModulePath/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryRolePortal(searchConditions = [], EntityID = 1, returnRolePortalID = False, returnCreatedTime = False, returnModifiedTime = False, returnPortal = False, returnPortalCode = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every RolePortal in the district.

	This function returns a dataframe of every RolePortal in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RolePortal/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RolePortal/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySecurityLocation(searchConditions = [], EntityID = 1, returnSecurityLocationID = False, returnAttachmentTypeGUID = False, returnCanAllowCreate = False, returnCanAllowDelete = False, returnCanAllowMassCreate = False, returnCanAllowMassDelete = False, returnCanAllowMassUpdate = False, returnCanAllowRead = False, returnCanAllowUpdate = False, returnCreatedTime = False, returnMobileCanAllowCreate = False, returnMobileCanAllowDelete = False, returnMobileCanAllowMassCreate = False, returnMobileCanAllowMassDelete = False, returnMobileCanAllowMassUpdate = False, returnMobileCanAllowRead = False, returnMobileCanAllowUpdate = False, returnModifiedTime = False, returnModulePathID = False, returnPath = False, returnPortal = False, returnPortalCode = False, returnReportID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SecurityLocation in the district.

	This function returns a dataframe of every SecurityLocation in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SecurityLocation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SecurityLocation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySecurityLocationMenuSecurityItem(searchConditions = [], EntityID = 1, returnSecurityLocationMenuSecurityItemID = False, returnCreatedTime = False, returnMenuSecurityItemID = False, returnModifiedTime = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SecurityLocationMenuSecurityItem in the district.

	This function returns a dataframe of every SecurityLocationMenuSecurityItem in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SecurityLocationMenuSecurityItem/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SecurityLocationMenuSecurityItem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySessionFileUpload(searchConditions = [], EntityID = 1, returnSessionFileUploadID = False, returnBytes = False, returnCreatedTime = False, returnFileContents = False, returnFileExtension = False, returnFileName = False, returnFilePath = False, returnMetaData = False, returnMetaDataXml = False, returnModifiedTime = False, returnSessionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXDimension = False, returnYDimension = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SessionFileUpload in the district.

	This function returns a dataframe of every SessionFileUpload in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SessionFileUpload/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SessionFileUpload/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySkywardSupportAccess(searchConditions = [], EntityID = 1, returnSkywardSupportAccessID = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnNotes = False, returnServiceCallNumber = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SkywardSupportAccess in the district.

	This function returns a dataframe of every SkywardSupportAccess in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SkywardSupportAccess/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SkywardSupportAccess/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySkywardSupportAccessLoginHistory(searchConditions = [], EntityID = 1, returnSkywardSupportAccessLoginHistoryID = False, returnAccessedTime = False, returnCreatedTime = False, returnModifiedTime = False, returnSessionID = False, returnSkywardEmployeeName = False, returnSkywardSupportAccessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SkywardSupportAccessLoginHistory in the district.

	This function returns a dataframe of every SkywardSupportAccessLoginHistory in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SkywardSupportAccessLoginHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SkywardSupportAccessLoginHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempDeletedPortalAccessSecurityUser(searchConditions = [], EntityID = 1, returnTempDeletedPortalAccessSecurityUserID = False, returnCreatedTime = False, returnFullNameLFM = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempDeletedPortalAccessSecurityUser in the district.

	This function returns a dataframe of every TempDeletedPortalAccessSecurityUser in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempDeletedPortalAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempDeletedPortalAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempEmployeeAccessSecurityUser(searchConditions = [], EntityID = 1, returnTempEmployeeAccessSecurityUserID = False, returnAddToEmployeeAccess = False, returnAllowEmployeeAccess = False, returnCreatedTime = False, returnEmailAddress = False, returnEmployeeID = False, returnEmployeeNameLFM = False, returnEmployeeNumber = False, returnForUserCreation = False, returnGroup = False, returnIsAuditEmployeeAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromEmployeeAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempEmployeeAccessSecurityUser in the district.

	This function returns a dataframe of every TempEmployeeAccessSecurityUser in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempEmployeeAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempEmployeeAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempEntityForClone(searchConditions = [], EntityID = 1, returnTempEntityForCloneID = False, returnCreatedTime = False, returnEntityCode = False, returnEntityName = False, returnEntityPrimaryKey = False, returnModifiedTime = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempEntityForClone in the district.

	This function returns a dataframe of every TempEntityForClone in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempEntityForClone/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempEntityForClone/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempFailedPortalAccessSecurityUser(searchConditions = [], EntityID = 1, returnTempFailedPortalAccessSecurityUserID = False, returnCreatedTime = False, returnFullNameLFM = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempFailedPortalAccessSecurityUser in the district.

	This function returns a dataframe of every TempFailedPortalAccessSecurityUser in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFailedPortalAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFailedPortalAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempFamilyAccessSecurityUser(searchConditions = [], EntityID = 1, returnTempFamilyAccessSecurityUserID = False, returnAddToFamilyAccess = False, returnCreatedTime = False, returnEmailAddress = False, returnEntityCodeName = False, returnForUserCreation = False, returnGuardianNameLFM = False, returnIsAuditFamilyAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromFamilyAccess = False, returnStudentGuardianID = False, returnStudentNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempFamilyAccessSecurityUser in the district.

	This function returns a dataframe of every TempFamilyAccessSecurityUser in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFamilyAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFamilyAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempFieldRestrictionScreen(searchConditions = [], EntityID = 1, returnTempFieldRestrictionScreenID = False, returnCreatedTime = False, returnDisplayText = False, returnModifiedTime = False, returnSecurityLocationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempFieldRestrictionScreen in the district.

	This function returns a dataframe of every TempFieldRestrictionScreen in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFieldRestrictionScreen/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFieldRestrictionScreen/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempImpersonationRoleForClone(searchConditions = [], EntityID = 1, returnTempImpersonationRoleForCloneID = False, returnCreatedTime = False, returnDescription = False, returnIsReadOnly = False, returnModifiedTime = False, returnRoleName = False, returnRolePrimaryKey = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempImpersonationRoleForClone in the district.

	This function returns a dataframe of every TempImpersonationRoleForClone in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempImpersonationRoleForClone/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempImpersonationRoleForClone/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempRoleForClone(searchConditions = [], EntityID = 1, returnTempRoleForCloneID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoleName = False, returnRolePrimaryKey = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempRoleForClone in the district.

	This function returns a dataframe of every TempRoleForClone in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempRoleForClone/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempRoleForClone/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempSecurityImportError(searchConditions = [], EntityID = 1, returnTempSecurityImportErrorID = False, returnCreatedTime = False, returnErrorMessage = False, returnErrorObject = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempSecurityImportError in the district.

	This function returns a dataframe of every TempSecurityImportError in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempSecurityImportGroupMembership(searchConditions = [], EntityID = 1, returnTempSecurityImportGroupMembershipID = False, returnCreatedTime = False, returnEntityName = False, returnExistingUserID = False, returnExternalUniqueIdentifier = False, returnGroupName = False, returnImportExternalUniqueIdentifier = False, returnImportUserNameBirthDate = False, returnImportUserNameFullNameLegalLFM = False, returnImportUserNameFullNameLFM = False, returnImportUserNamePrimaryEmailAddress = False, returnMatches = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserNameBirthDate = False, returnUserNameFullNameLegalLFM = False, returnUserNameFullNameLFM = False, returnUserNamePrimaryEmailAddress = False, returnUserUsername = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempSecurityImportGroupMembership in the district.

	This function returns a dataframe of every TempSecurityImportGroupMembership in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportGroupMembership/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportGroupMembership/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempSecurityImportPreview(searchConditions = [], EntityID = 1, returnTempSecurityImportPreviewID = False, returnCreatedTime = False, returnIdentifier = False, returnModifiedTime = False, returnObject = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempSecurityImportPreview in the district.

	This function returns a dataframe of every TempSecurityImportPreview in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportPreview/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportPreview/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempSpecialtyAccessGroup(searchConditions = [], EntityID = 1, returnTempSpecialtyAccessGroupID = False, returnCreatedTime = False, returnGroupName = False, returnIdentifier = False, returnModifiedTime = False, returnSelected = False, returnSpecialtyAccessGroupPrimaryKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempSpecialtyAccessGroup in the district.

	This function returns a dataframe of every TempSpecialtyAccessGroup in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSpecialtyAccessGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSpecialtyAccessGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentAccessSecurityUser(searchConditions = [], EntityID = 1, returnTempStudentAccessSecurityUserID = False, returnAddToStudentAccess = False, returnCreatedTime = False, returnDeleteUserAfterAudit = False, returnEmailAddress = False, returnForUserCreation = False, returnGroup = False, returnIsAuditStudentAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromStudentAccess = False, returnStudentID = False, returnStudentNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentAccessSecurityUser in the district.

	This function returns a dataframe of every TempStudentAccessSecurityUser in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempStudentAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempStudentAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempTeacherAccessSecurityUser(searchConditions = [], EntityID = 1, returnTempTeacherAccessSecurityUserID = False, returnAddToTeacherAccess = False, returnAllowTeacherAccess = False, returnCreatedTime = False, returnDeleteUserAfterAudit = False, returnEmailAddress = False, returnForUserCreation = False, returnGroup = False, returnIsAuditTeacherAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnNote = False, returnRemoveFromTeacherAccess = False, returnStaffID = False, returnStaffNameLFM = False, returnStaffNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempTeacherAccessSecurityUser in the district.

	This function returns a dataframe of every TempTeacherAccessSecurityUser in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempTeacherAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempTeacherAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTrustedDevice(searchConditions = [], EntityID = 1, returnTrustedDeviceID = False, returnBrowserType = False, returnBrowserVersion = False, returnCreatedTime = False, returnDeviceType = False, returnHostAddress = False, returnIdentifier = False, returnModifiedTime = False, returnOperatingSystemType = False, returnUserAgent = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TrustedDevice in the district.

	This function returns a dataframe of every TrustedDevice in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TrustedDevice/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TrustedDevice/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUserAuthenticationMethod(searchConditions = [], EntityID = 1, returnUserAuthenticationMethodID = False, returnAuthenticationMethodID = False, returnCreatedTime = False, returnModifiedTime = False, returnProviderUserIdentity = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every UserAuthenticationMethod in the district.

	This function returns a dataframe of every UserAuthenticationMethod in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserAuthenticationMethod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserAuthenticationMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUserCalendarPreference(searchConditions = [], EntityID = 1, returnUserCalendarPreferenceID = False, returnApprovedTimeOffEventBackgroundColor = False, returnBirthdayEventBackgroundColor = False, returnCalendarEventBackgroundColor = False, returnCalendarType = False, returnCalendarTypeCode = False, returnCreatedTime = False, returnDistrictActivityEventBackgroundColor = False, returnModifiedTime = False, returnPayDayEventBackgroundColor = False, returnSelectedView = False, returnShowAllMyEmployeesTimeOff = False, returnShowAllocatedTimeOff = False, returnShowBirthdays = False, returnShowCalendarEvents = False, returnShowDistrictActivityEvents = False, returnShowMyDirectEmployeesTimeOff = False, returnShowMyTimeOff = False, returnShowTransactionsIHadASubFor = False, returnShowTransactionsISubbedFor = False, returnShowWeekends = False, returnTransactionsIHadASubForEventBackgroundColor = False, returnTransactionsISubbedForEventBackgroundColor = False, returnUnapprovedTimeOffEventBackgroundColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every UserCalendarPreference in the district.

	This function returns a dataframe of every UserCalendarPreference in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserCalendarPreference/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserCalendarPreference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUserImport(searchConditions = [], EntityID = 1, returnUserImportID = False, returnAboveChangeThreshold = False, returnAboveDeleteThreshold = False, returnCreatedTime = False, returnDateExecuted = False, returnHasErrors = False, returnMediaID = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every UserImport in the district.

	This function returns a dataframe of every UserImport in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImport/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImport/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUserImportResult(searchConditions = [], EntityID = 1, returnUserImportResultID = False, returnCreatedTime = False, returnEntityCode = False, returnGroupMembershipChangeType = False, returnGroupMembershipChangeTypeCode = False, returnGroupName = False, returnHasErrors = False, returnIsStaff = False, returnLineNumber = False, returnModifiedTime = False, returnNameChangeType = False, returnNameChangeTypeCode = False, returnSchoolYear = False, returnStaffChangeType = False, returnStaffChangeTypeCode = False, returnUserChangeType = False, returnUserChangeTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportID = False, returnUsername = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every UserImportResult in the district.

	This function returns a dataframe of every UserImportResult in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImportResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImportResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUserImportResultError(searchConditions = [], EntityID = 1, returnUserImportResultErrorID = False, returnCreatedTime = False, returnErrorMessage = False, returnFieldName = False, returnFromPreview = False, returnModifiedTime = False, returnObjectName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportResultID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every UserImportResultError in the district.

	This function returns a dataframe of every UserImportResultError in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImportResultError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImportResultError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUserPasswordReset(searchConditions = [], EntityID = 1, returnUserPasswordResetID = False, returnCreatedTime = False, returnExpirationTime = False, returnHostAddressRequestedFrom = False, returnModifiedTime = False, returnResetGuid = False, returnResetSalt = False, returnUsed = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every UserPasswordReset in the district.

	This function returns a dataframe of every UserPasswordReset in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserPasswordReset/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserPasswordReset/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUserPreference(searchConditions = [], EntityID = 1, returnUserPreferenceID = False, returnAccountSelection = False, returnAccountSelectionCode = False, returnCreatedTime = False, returnModifiedTime = False, returnThemeID = False, returnUseEmailMultifactorAuthentication = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSecurity = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every UserPreference in the district.

	This function returns a dataframe of every UserPreference in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserPreference/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserPreference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUserProfileData(searchConditions = [], EntityID = 1, returnUserProfileDataID = False, returnBrowseObject = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnRelatedRecord = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every UserProfileData in the district.

	This function returns a dataframe of every UserProfileData in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserProfileData/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserProfileData/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUserProfileTabStatus(searchConditions = [], EntityID = 1, returnUserProfileTabStatusID = False, returnCreatedTime = False, returnModifiedTime = False, returnOpenTabs = False, returnProfileID = False, returnProfileScreenIDLastTab = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every UserProfileTabStatus in the district.

	This function returns a dataframe of every UserProfileTabStatus in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserProfileTabStatus/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserProfileTabStatus/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUserSetting(searchConditions = [], EntityID = 1, returnUserSettingID = False, returnAction = False, returnArea = False, returnCode = False, returnController = False, returnCreatedTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every UserSetting in the district.

	This function returns a dataframe of every UserSetting in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUserStudentCalendarPreference(searchConditions = [], EntityID = 1, returnUserStudentCalendarPreferenceID = False, returnAssignmentBackgroundColor = False, returnCreatedTime = False, returnModifiedTime = False, returnShowAssignments = False, returnShowStudentActivityEvents = False, returnStudentActivityEventBackgroundColor = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every UserStudentCalendarPreference in the district.

	This function returns a dataframe of every UserStudentCalendarPreference in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserStudentCalendarPreference/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserStudentCalendarPreference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUser(searchConditions = [], EntityID = 1, returnUserID = False, returnAccessCode = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnCurrentPortal = False, returnCurrentPortalCode = False, returnCustomerAccessID = False, returnDatabaseUsername = False, returnDockDisplayOpen = False, returnEffectiveAuthenticationRoleID = False, returnEffectiveAuthenticationRoleName = False, returnEffectiveCachedAuthenticationRole = False, returnEffectiveMultifactorAuthenticationCode = False, returnEffectiveMultifactorAuthenticationID = False, returnEmulatingMobile = False, returnEntityIDCurrent = False, returnFailedMultifactorAuthenticationCount = False, returnFailedSignInCount = False, returnFiscalYearIDCurrent = False, returnForcePasswordChange = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnGroupMembershipCount = False, returnIsActive = False, returnIsDeleted = False, returnIsExpired = False, returnIsLockedOut = False, returnIsSuperUser = False, returnLastPasswordChangeTime = False, returnLockedOutTime = False, returnMessageCount = False, returnModifiedTime = False, returnMultifactorAuthenticationID = False, returnNameID = False, returnPasswordExpirationDate = False, returnPasswordHash = False, returnPasswordSalt = False, returnPasswordStrategy = False, returnPasswordStrategyCode = False, returnRolesAuthenticationRoleID = False, returnRolesMultifactorAuthenticationID = False, returnUserHasFamilyAccess = False, returnUserHasStudentAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsername = False, returnUserUncachedID = False, returnUsesSkywardAuthentication = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every User in the district.

	This function returns a dataframe of every User in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/User/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/User/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)