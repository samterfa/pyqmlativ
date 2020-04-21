# This module contains Family functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryChangeRequest(searchConditions = [], EntityID = 1, returnChangeRequestID = False, returnArea = False, returnAreaCode = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnNameID = False, returnSchoolYearID = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ChangeRequest in the district.

	This function returns a dataframe of every ChangeRequest in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequest/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequest/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryChangeRequestDetail(searchConditions = [], EntityID = 1, returnChangeRequestDetailID = False, returnChangeRequestID = False, returnCreatedTime = False, returnFieldName = False, returnFieldNameCode = False, returnModifiedTime = False, returnOriginalValue = False, returnRequestedTime = False, returnRequestedValue = False, returnSourceID = False, returnStatus = False, returnStatusCode = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRequestedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ChangeRequestDetail in the district.

	This function returns a dataframe of every ChangeRequestDetail in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryChangeRequestDetailApproval(searchConditions = [], EntityID = 1, returnChangeRequestDetailApprovalID = False, returnChangeRequestDetailID = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ChangeRequestDetailApproval in the district.

	This function returns a dataframe of every ChangeRequestDetailApproval in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetailApproval/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetailApproval/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigDistrictYear(searchConditions = [], EntityID = 1, returnConfigDistrictYearID = False, returnCreatedTime = False, returnDisplayDefaultContact = False, returnDisplayModuleContact = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ConfigDistrictYear in the district.

	This function returns a dataframe of every ConfigDistrictYear in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigDistrictYearContact(searchConditions = [], EntityID = 1, returnConfigDistrictYearContactID = False, returnCanDisplayEmail = False, returnCanDisplayPhone = False, returnConfigDistrictYearID = False, returnCreatedTime = False, returnDisplayEmail = False, returnDisplayPhone = False, returnModifiedTime = False, returnModule = False, returnModuleCode = False, returnModuleDisplay = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ConfigDistrictYearContact in the district.

	This function returns a dataframe of every ConfigDistrictYearContact in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigDistrictYearContact/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigDistrictYearContact/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigEntityGroupYear(searchConditions = [], EntityID = 1, returnConfigEntityGroupYearID = False, returnChangeRequestFamilyEmail = False, returnChangeRequestFamilyEmailCode = False, returnChangeRequestFamilyPhone = False, returnChangeRequestFamilyPhoneCode = False, returnChangeRequestStudentEmail = False, returnChangeRequestStudentEmailCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDefaultFeeManagementOnlinePaymentAccess = False, returnDefaultFeeManagementOnlinePaymentAccessCode = False, returnDefaultFoodServiceOnlinePaymentAccess = False, returnDefaultFoodServiceOnlinePaymentAccessCode = False, returnDisplayAssignments = False, returnDisplayCalendarEvents = False, returnDisplayDistrictActivityEvents = False, returnDisplayStudentActivityEvents = False, returnEmailTypeIDToDisplayFamilyStudentAccess = False, returnEndorsementSignatureOption = False, returnEndorsementSignatureOptionCode = False, returnEndorsementSignatureStatement = False, returnEntityGroupKey = False, returnEntityID = False, returnFamilyAccessAccountInfoEmailBody = False, returnFamilyAccessAccountInfoEmailIncludeResetPasswordText = False, returnFamilyAccessAccountInfoEmailSubject = False, returnFamilyAccessCareerPlanDisplayShowDroppedCourses = False, returnFamilyAccessDisplayCommentCodes = False, returnFamilyAccessDisplayFreeFormComments = False, returnFamilyAccessDisplayGradeBucketsAfterEndDate = False, returnFamilyAccessDisplayHonorRoll = False, returnFamilyAccessDisplayLockerCombination = False, returnFamilyAccessDisplayLockerNumber = False, returnFamilyAccessDisplayOnlyCurrentAndCompleteGrades = False, returnFamilyAccessDisplayOnlyCurrentMissingAssignments = False, returnFamilyAccessDisplayShowActualEarnedCredits = False, returnFamilyAccessDisplayShowAttendance = False, returnFamilyAccessDisplayShowDroppedCourses = False, returnFamilyAccessDisplayShowEndedAttendanceTerms = False, returnFamilyAccessDisplayShowPossibleEarnedCredits = False, returnFamilyAccessDisplayStudentAddress = False, returnFamilyAccessDisplayStudentRank = False, returnFamilyAccessDisplayUseReportCardGradeBucketSettings = False, returnFamilyAccessLinkStudentSectionsOnReportCard = False, returnFamilyStudentAccessDisplayTeacherEmail = False, returnFamilyStudentAccessDisplayTeacherPhoneNumber = False, returnHideScheduleMessage = False, returnHideSchedulePriorToCalendarDays = False, returnIsFamilyInformationApprovalWorkflowUpdated = False, returnIsStudentInformationApprovalWorkflowUpdated = False, returnModifiedTime = False, returnPhoneTypeIDToDisplayFamilyStudentAccess = False, returnRankMethodIDFamilyAccessReportCardGrading = False, returnRankMethodIDFamilyAccessReportCardStudent = False, returnReportCardGPADisplay = False, returnReportCardGPADisplayCode = False, returnReportCardHeaderAddressType = False, returnReportCardHeaderAddressTypeCode = False, returnReportCardStudentRankDisplay = False, returnReportCardStudentRankDisplayCode = False, returnSchoolYearID = False, returnStaffNameDisplayType = False, returnStaffNameDisplayTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ConfigEntityGroupYear in the district.

	This function returns a dataframe of every ConfigEntityGroupYear in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigSystem(searchConditions = [], EntityID = 1, returnConfigSystemID = False, returnAddressValidationMessage = False, returnAllowFamilyAccessDefault = False, returnAllowOutOfRangeAddressesToSubmit = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnEnableAddressValidation = False, returnEnableNewStudentEnrollment = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCOPPAConsentObjectMA(searchConditions = [], EntityID = 1, returnCOPPAConsentObjectMAID = False, returnCOPPAConsent = False, returnCreatedTime = False, returnFamilyGuardianID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every COPPAConsentObjectMA in the district.

	This function returns a dataframe of every COPPAConsentObjectMA in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/COPPAConsentObjectMA/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/COPPAConsentObjectMA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryFamily(searchConditions = [], EntityID = 1, returnFamilyID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnHasStudentInSpecificDistrict = False, returnLanguageIDHome = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Family in the district.

	This function returns a dataframe of every Family in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/Family/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/Family/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryFamilyGuardian(searchConditions = [], EntityID = 1, returnFamilyGuardianID = False, returnCreatedTime = False, returnFamilyID = False, returnHasActiveStudentGuardianRestrictedAccess = False, returnModifiedTime = False, returnNameID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnAPIOptionFlags = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every FamilyGuardian in the district.

	This function returns a dataframe of every FamilyGuardian in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/FamilyGuardian/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/FamilyGuardian/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentFamily(searchConditions = [], EntityID = 1, returnStudentFamilyID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnFamilyID = False, returnHasEmployeeGuardian = False, returnIsEmergencyContact = False, returnIsPrimaryEmergencyContact = False, returnModifiedTime = False, returnRank = False, returnReceivesForms = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnAPIOptionFlags = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentFamily in the district.

	This function returns a dataframe of every StudentFamily in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentFamily/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentFamily/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentGuardian(searchConditions = [], EntityID = 1, returnStudentGuardianID = False, returnAllowFamilyAccess = False, returnAllowStudentPickup = False, returnCreatedTime = False, returnFeeOnlinePaymentOverrideType = False, returnFeeOnlinePaymentOverrideTypeCode = False, returnFoodOnlinePaymentOverrideType = False, returnFoodOnlinePaymentOverrideTypeCode = False, returnGuardianCategory = False, returnGuardianNameIDAndFamilyID = False, returnHasActiveRestrictedAccess = False, returnHasUnrestrictedAccess = False, returnIsCustodialGuardian = False, returnIsEmergencyContact = False, returnModifiedTime = False, returnNameIDGuardian = False, returnNeedsSecurityGroupAudit = False, returnOverrideFeeOnlinePaymentAccess = False, returnOverrideFoodOnlinePaymentAccess = False, returnRank = False, returnRelationshipID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentGuardian in the district.

	This function returns a dataframe of every StudentGuardian in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardian/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardian/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentGuardianRestrictedAccess(searchConditions = [], EntityID = 1, returnStudentGuardianRestrictedAccessID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnReason = False, returnStartDate = False, returnStudentGuardianID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentGuardianRestrictedAccess in the district.

	This function returns a dataframe of every StudentGuardianRestrictedAccess in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardianRestrictedAccess/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardianRestrictedAccess/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempFamilyGuardian(searchConditions = [], EntityID = 1, returnTempFamilyGuardianID = False, returnCreatedTime = False, returnGuardianNameID = False, returnGuardianNameLFM = False, returnIsFamilyAccessUser = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempFamilyGuardian in the district.

	This function returns a dataframe of every TempFamilyGuardian in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/TempFamilyGuardian/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/TempFamilyGuardian/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)