# This module contains Family functions.

from .Utilities import make_request

import pandas as pd

def getEveryChangeRequest(EntityID = 1, page = 1, pageSize = 100, returnChangeRequestID = True, returnArea = False, returnAreaCode = False, returnCreatedTime = False, returnEntityID = False, returnLevelPendingApproval = False, returnModifiedTime = False, returnNameID = False, returnSchoolYearID = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequest/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getChangeRequest(ChangeRequestID, EntityID = 1, returnreturnChangeRequestID = False, returnreturnArea = False, returnreturnAreaCode = False, returnreturnCreatedTime = False, returnreturnEntityID = False, returnreturnLevelPendingApproval = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnSchoolYearID = False, returnreturnStatus = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequest/" + str(ChangeRequestID), verb = "get", params_list = params_list)

	return(response)

def deleteChangeRequest(ChangeRequestID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequest/" + str(ChangeRequestID), verb = "delete")

	return(response)

def getEveryChangeRequestApprovalTask(EntityID = 1, page = 1, pageSize = 100, returnChangeRequestApprovalTaskID = True, returnArea = False, returnAreaCode = False, returnChangeRequestApprovalTaskIDClonedFrom = False, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnDescription = False, returnLevel = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestApprovalTask/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getChangeRequestApprovalTask(ChangeRequestApprovalTaskID, EntityID = 1, returnreturnChangeRequestApprovalTaskID = False, returnreturnArea = False, returnreturnAreaCode = False, returnreturnChangeRequestApprovalTaskIDClonedFrom = False, returnreturnConfigEntityGroupYearID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnLevel = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestApprovalTask/" + str(ChangeRequestApprovalTaskID), verb = "get", params_list = params_list)

	return(response)

def deleteChangeRequestApprovalTask(ChangeRequestApprovalTaskID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestApprovalTask/" + str(ChangeRequestApprovalTaskID), verb = "delete")

	return(response)

def getEveryChangeRequestApprovalTaskSecurityGroup(EntityID = 1, page = 1, pageSize = 100, returnChangeRequestApprovalTaskSecurityGroupID = True, returnChangeRequestApprovalTaskID = False, returnChangeRequestApprovalTaskSecurityGroupIDClonedFrom = False, returnCreatedTime = False, returnGroupIDSecurity = False, returnIsAlternate = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestApprovalTaskSecurityGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getChangeRequestApprovalTaskSecurityGroup(ChangeRequestApprovalTaskSecurityGroupID, EntityID = 1, returnreturnChangeRequestApprovalTaskSecurityGroupID = False, returnreturnChangeRequestApprovalTaskID = False, returnreturnChangeRequestApprovalTaskSecurityGroupIDClonedFrom = False, returnreturnCreatedTime = False, returnreturnGroupIDSecurity = False, returnreturnIsAlternate = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestApprovalTaskSecurityGroup/" + str(ChangeRequestApprovalTaskSecurityGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteChangeRequestApprovalTaskSecurityGroup(ChangeRequestApprovalTaskSecurityGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestApprovalTaskSecurityGroup/" + str(ChangeRequestApprovalTaskSecurityGroupID), verb = "delete")

	return(response)

def getEveryChangeRequestDetail(EntityID = 1, page = 1, pageSize = 100, returnChangeRequestDetailID = True, returnChangeRequestID = False, returnCreatedTime = False, returnFieldName = False, returnFieldNameCode = False, returnModifiedTime = False, returnOriginalValue = False, returnRequestedTime = False, returnRequestedValue = False, returnSourceID = False, returnStatus = False, returnStatusCode = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRequestedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetail/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getChangeRequestDetail(ChangeRequestDetailID, EntityID = 1, returnreturnChangeRequestDetailID = False, returnreturnChangeRequestID = False, returnreturnCreatedTime = False, returnreturnFieldName = False, returnreturnFieldNameCode = False, returnreturnModifiedTime = False, returnreturnOriginalValue = False, returnreturnRequestedTime = False, returnreturnRequestedValue = False, returnreturnSourceID = False, returnreturnStatus = False, returnreturnStatusCode = False, returnreturnUserIDApprover = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserIDRequestedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetail/" + str(ChangeRequestDetailID), verb = "get", params_list = params_list)

	return(response)

def deleteChangeRequestDetail(ChangeRequestDetailID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetail/" + str(ChangeRequestDetailID), verb = "delete")

	return(response)

def getEveryChangeRequestDetailApproval(EntityID = 1, page = 1, pageSize = 100, returnChangeRequestDetailApprovalID = True, returnChangeRequestDetailID = False, returnComment = False, returnCreatedTime = False, returnIsLastLevel = False, returnLevel = False, returnLevelDescription = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnTaskInstanceID = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetailApproval/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getChangeRequestDetailApproval(ChangeRequestDetailApprovalID, EntityID = 1, returnreturnChangeRequestDetailApprovalID = False, returnreturnChangeRequestDetailID = False, returnreturnComment = False, returnreturnCreatedTime = False, returnreturnIsLastLevel = False, returnreturnLevel = False, returnreturnLevelDescription = False, returnreturnModifiedTime = False, returnreturnStatus = False, returnreturnStatusCode = False, returnreturnTaskInstanceID = False, returnreturnUserIDApprover = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetailApproval/" + str(ChangeRequestDetailApprovalID), verb = "get", params_list = params_list)

	return(response)

def deleteChangeRequestDetailApproval(ChangeRequestDetailApprovalID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetailApproval/" + str(ChangeRequestDetailApprovalID), verb = "delete")

	return(response)

def getEveryConfigEntityGroupYear(EntityID = 1, page = 1, pageSize = 100, returnConfigEntityGroupYearID = True, returnChangeRequestFamilyEmail = False, returnChangeRequestFamilyEmailCode = False, returnChangeRequestFamilyPhone = False, returnChangeRequestFamilyPhoneCode = False, returnChangeRequestStudentEmail = False, returnChangeRequestStudentEmailCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDefaultFeeManagementOnlinePaymentAccess = False, returnDefaultFeeManagementOnlinePaymentAccessCode = False, returnDefaultFoodServiceOnlinePaymentAccess = False, returnDefaultFoodServiceOnlinePaymentAccessCode = False, returnDisplayAssignments = False, returnDisplayCalendarEvents = False, returnDisplayDistrictActivityEvents = False, returnDisplayStudentActivityEvents = False, returnEmailTypeIDToDisplayFamilyStudentAccess = False, returnEndorsementSignatureOption = False, returnEndorsementSignatureOptionCode = False, returnEndorsementSignatureStatement = False, returnEntityGroupKey = False, returnEntityID = False, returnFamilyAccessAccountInfoEmailBody = False, returnFamilyAccessAccountInfoEmailIncludeResetPasswordText = False, returnFamilyAccessAccountInfoEmailSubject = False, returnFamilyAccessCareerPlanDisplayShowDroppedCourses = False, returnFamilyAccessDisplayCommentCodes = False, returnFamilyAccessDisplayFreeFormComments = False, returnFamilyAccessDisplayGradeBucketsAfterEndDate = False, returnFamilyAccessDisplayHonorRoll = False, returnFamilyAccessDisplayOnlyCurrentAndCompleteGrades = False, returnFamilyAccessDisplayOnlyCurrentMissingAssignments = False, returnFamilyAccessDisplayShowActualEarnedCredits = False, returnFamilyAccessDisplayShowAttendance = False, returnFamilyAccessDisplayShowDroppedCourses = False, returnFamilyAccessDisplayShowEndedAttendanceTerms = False, returnFamilyAccessDisplayShowPossibleEarnedCredits = False, returnFamilyAccessDisplayStudentAddress = False, returnFamilyAccessDisplayStudentRank = False, returnFamilyAccessDisplayUseReportCardGradeBucketSettings = False, returnFamilyAccessLinkStudentSectionsOnReportCard = False, returnFamilyStudentAccessDisplayTeacherEmail = False, returnFamilyStudentAccessDisplayTeacherPhoneNumber = False, returnHideScheduleMessage = False, returnHideSchedulePriorToCalendarDays = False, returnIsFamilyInformationApprovalWorkflowUpdated = False, returnIsStudentInformationApprovalWorkflowUpdated = False, returnModifiedTime = False, returnPhoneTypeIDToDisplayFamilyStudentAccess = False, returnRankMethodIDFamilyAccessReportCardGrading = False, returnRankMethodIDFamilyAccessReportCardStudent = False, returnReportCardGPADisplay = False, returnReportCardGPADisplayCode = False, returnReportCardHeaderAddressType = False, returnReportCardHeaderAddressTypeCode = False, returnReportCardStudentRankDisplay = False, returnReportCardStudentRankDisplayCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, returnreturnConfigEntityGroupYearID = False, returnreturnChangeRequestFamilyEmail = False, returnreturnChangeRequestFamilyEmailCode = False, returnreturnChangeRequestFamilyPhone = False, returnreturnChangeRequestFamilyPhoneCode = False, returnreturnChangeRequestStudentEmail = False, returnreturnChangeRequestStudentEmailCode = False, returnreturnConfigEntityGroupYearIDClonedFrom = False, returnreturnCreatedTime = False, returnreturnDefaultFeeManagementOnlinePaymentAccess = False, returnreturnDefaultFeeManagementOnlinePaymentAccessCode = False, returnreturnDefaultFoodServiceOnlinePaymentAccess = False, returnreturnDefaultFoodServiceOnlinePaymentAccessCode = False, returnreturnDisplayAssignments = False, returnreturnDisplayCalendarEvents = False, returnreturnDisplayDistrictActivityEvents = False, returnreturnDisplayStudentActivityEvents = False, returnreturnEmailTypeIDToDisplayFamilyStudentAccess = False, returnreturnEndorsementSignatureOption = False, returnreturnEndorsementSignatureOptionCode = False, returnreturnEndorsementSignatureStatement = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnFamilyAccessAccountInfoEmailBody = False, returnreturnFamilyAccessAccountInfoEmailIncludeResetPasswordText = False, returnreturnFamilyAccessAccountInfoEmailSubject = False, returnreturnFamilyAccessCareerPlanDisplayShowDroppedCourses = False, returnreturnFamilyAccessDisplayCommentCodes = False, returnreturnFamilyAccessDisplayFreeFormComments = False, returnreturnFamilyAccessDisplayGradeBucketsAfterEndDate = False, returnreturnFamilyAccessDisplayHonorRoll = False, returnreturnFamilyAccessDisplayOnlyCurrentAndCompleteGrades = False, returnreturnFamilyAccessDisplayOnlyCurrentMissingAssignments = False, returnreturnFamilyAccessDisplayShowActualEarnedCredits = False, returnreturnFamilyAccessDisplayShowAttendance = False, returnreturnFamilyAccessDisplayShowDroppedCourses = False, returnreturnFamilyAccessDisplayShowEndedAttendanceTerms = False, returnreturnFamilyAccessDisplayShowPossibleEarnedCredits = False, returnreturnFamilyAccessDisplayStudentAddress = False, returnreturnFamilyAccessDisplayStudentRank = False, returnreturnFamilyAccessDisplayUseReportCardGradeBucketSettings = False, returnreturnFamilyAccessLinkStudentSectionsOnReportCard = False, returnreturnFamilyStudentAccessDisplayTeacherEmail = False, returnreturnFamilyStudentAccessDisplayTeacherPhoneNumber = False, returnreturnHideScheduleMessage = False, returnreturnHideSchedulePriorToCalendarDays = False, returnreturnIsFamilyInformationApprovalWorkflowUpdated = False, returnreturnIsStudentInformationApprovalWorkflowUpdated = False, returnreturnModifiedTime = False, returnreturnPhoneTypeIDToDisplayFamilyStudentAccess = False, returnreturnRankMethodIDFamilyAccessReportCardGrading = False, returnreturnRankMethodIDFamilyAccessReportCardStudent = False, returnreturnReportCardGPADisplay = False, returnreturnReportCardGPADisplayCode = False, returnreturnReportCardHeaderAddressType = False, returnreturnReportCardHeaderAddressTypeCode = False, returnreturnReportCardStudentRankDisplay = False, returnreturnReportCardStudentRankDisplayCode = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "delete")

	return(response)

def getEveryConfigSystem(EntityID = 1, page = 1, pageSize = 100, returnConfigSystemID = True, returnAddressValidationMessage = False, returnAllowFamilyAccessDefault = False, returnAllowOutOfRangeAddressesToSubmit = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnEnableAddressValidation = False, returnEnableNewStudentEnrollment = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigSystem(ConfigSystemID, EntityID = 1, returnreturnConfigSystemID = False, returnreturnAddressValidationMessage = False, returnreturnAllowFamilyAccessDefault = False, returnreturnAllowOutOfRangeAddressesToSubmit = False, returnreturnAutoGenerateSecurityUser = False, returnreturnAutoGenerateSecurityUserCode = False, returnreturnCreatedTime = False, returnreturnEnableAddressValidation = False, returnreturnEnableNewStudentEnrollment = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigSystem/" + str(ConfigSystemID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigSystem(ConfigSystemID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigSystem/" + str(ConfigSystemID), verb = "delete")

	return(response)

def getEveryFamily(EntityID = 1, page = 1, pageSize = 100, returnFamilyID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnHasStudentInSpecificDistrict = False, returnLanguageIDHome = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/Family/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getFamily(FamilyID, EntityID = 1, returnreturnFamilyID = False, returnreturnAttachmentCount = False, returnreturnAttachmentIndicatorColumn = False, returnreturnCreatedTime = False, returnreturnHasStudentInSpecificDistrict = False, returnreturnLanguageIDHome = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/Family/" + str(FamilyID), verb = "get", params_list = params_list)

	return(response)

def deleteFamily(FamilyID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/Family/" + str(FamilyID), verb = "delete")

	return(response)

def getEveryFamilyGuardian(EntityID = 1, page = 1, pageSize = 100, returnFamilyGuardianID = True, returnCreatedTime = False, returnFamilyID = False, returnHasActiveStudentGuardianRestrictedAccess = False, returnModifiedTime = False, returnNameID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/FamilyGuardian/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getFamilyGuardian(FamilyGuardianID, EntityID = 1, returnreturnFamilyGuardianID = False, returnreturnCreatedTime = False, returnreturnFamilyID = False, returnreturnHasActiveStudentGuardianRestrictedAccess = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnRank = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/FamilyGuardian/" + str(FamilyGuardianID), verb = "get", params_list = params_list)

	return(response)

def deleteFamilyGuardian(FamilyGuardianID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/FamilyGuardian/" + str(FamilyGuardianID), verb = "delete")

	return(response)

def getEveryStudentFamily(EntityID = 1, page = 1, pageSize = 100, returnStudentFamilyID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnFamilyID = False, returnHasEmployeeGuardian = False, returnIsEmergencyContact = False, returnIsPrimaryEmergencyContact = False, returnModifiedTime = False, returnRank = False, returnReceivesForms = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentFamily/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentFamily(StudentFamilyID, EntityID = 1, returnreturnStudentFamilyID = False, returnreturnAttachmentCount = False, returnreturnAttachmentIndicatorColumn = False, returnreturnCreatedTime = False, returnreturnFamilyID = False, returnreturnHasEmployeeGuardian = False, returnreturnIsEmergencyContact = False, returnreturnIsPrimaryEmergencyContact = False, returnreturnModifiedTime = False, returnreturnRank = False, returnreturnReceivesForms = False, returnreturnStudentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentFamily/" + str(StudentFamilyID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentFamily(StudentFamilyID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentFamily/" + str(StudentFamilyID), verb = "delete")

	return(response)

def getEveryStudentGuardian(EntityID = 1, page = 1, pageSize = 100, returnStudentGuardianID = True, returnAllowFamilyAccess = False, returnAllowStudentPickup = False, returnCreatedTime = False, returnFeeOnlinePaymentOverrideType = False, returnFeeOnlinePaymentOverrideTypeCode = False, returnFoodOnlinePaymentOverrideType = False, returnFoodOnlinePaymentOverrideTypeCode = False, returnGuardianCategory = False, returnGuardianNameIDAndFamilyID = False, returnHasActiveRestrictedAccess = False, returnHasUnrestrictedAccess = False, returnIsCustodialGuardian = False, returnIsEmergencyContact = False, returnModifiedTime = False, returnNameIDGuardian = False, returnNeedsSecurityGroupAudit = False, returnOverrideFeeOnlinePaymentAccess = False, returnOverrideFoodOnlinePaymentAccess = False, returnRank = False, returnRelationshipID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardian/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentGuardian(StudentGuardianID, EntityID = 1, returnreturnStudentGuardianID = False, returnreturnAllowFamilyAccess = False, returnreturnAllowStudentPickup = False, returnreturnCreatedTime = False, returnreturnFeeOnlinePaymentOverrideType = False, returnreturnFeeOnlinePaymentOverrideTypeCode = False, returnreturnFoodOnlinePaymentOverrideType = False, returnreturnFoodOnlinePaymentOverrideTypeCode = False, returnreturnGuardianCategory = False, returnreturnGuardianNameIDAndFamilyID = False, returnreturnHasActiveRestrictedAccess = False, returnreturnHasUnrestrictedAccess = False, returnreturnIsCustodialGuardian = False, returnreturnIsEmergencyContact = False, returnreturnModifiedTime = False, returnreturnNameIDGuardian = False, returnreturnNeedsSecurityGroupAudit = False, returnreturnOverrideFeeOnlinePaymentAccess = False, returnreturnOverrideFoodOnlinePaymentAccess = False, returnreturnRank = False, returnreturnRelationshipID = False, returnreturnStudentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardian/" + str(StudentGuardianID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentGuardian(StudentGuardianID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardian/" + str(StudentGuardianID), verb = "delete")

	return(response)

def getEveryStudentGuardianRestrictedAccess(EntityID = 1, page = 1, pageSize = 100, returnStudentGuardianRestrictedAccessID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnReason = False, returnStartDate = False, returnStudentGuardianID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardianRestrictedAccess/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentGuardianRestrictedAccess(StudentGuardianRestrictedAccessID, EntityID = 1, returnreturnStudentGuardianRestrictedAccessID = False, returnreturnAttachmentCount = False, returnreturnAttachmentIndicatorColumn = False, returnreturnCreatedTime = False, returnreturnEndDate = False, returnreturnModifiedTime = False, returnreturnReason = False, returnreturnStartDate = False, returnreturnStudentGuardianID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardianRestrictedAccess/" + str(StudentGuardianRestrictedAccessID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentGuardianRestrictedAccess(StudentGuardianRestrictedAccessID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardianRestrictedAccess/" + str(StudentGuardianRestrictedAccessID), verb = "delete")

	return(response)

def getEveryTempFamilyGuardian(EntityID = 1, page = 1, pageSize = 100, returnTempFamilyGuardianID = True, returnCreatedTime = False, returnGuardianNameID = False, returnGuardianNameLFM = False, returnIsFamilyAccessUser = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/TempFamilyGuardian/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempFamilyGuardian(TempFamilyGuardianID, EntityID = 1, returnreturnTempFamilyGuardianID = False, returnreturnCreatedTime = False, returnreturnGuardianNameID = False, returnreturnGuardianNameLFM = False, returnreturnIsFamilyAccessUser = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/TempFamilyGuardian/" + str(TempFamilyGuardianID), verb = "get", params_list = params_list)

	return(response)

def deleteTempFamilyGuardian(TempFamilyGuardianID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/TempFamilyGuardian/" + str(TempFamilyGuardianID), verb = "delete")

	return(response)