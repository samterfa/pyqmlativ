# This module contains Family functions.

from . import make_request

def getChangeRequest(ChangeRequestID, EntityID = 1, returnArea = False, returnAreaCode = False, returnCreatedTime = False, returnEntityID = False, returnLevelPendingApproval = False, returnModifiedTime = False, returnNameID = False, returnSchoolYearID = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequest/" + str(ChangeRequestID), verb = "get", params_list = params_list)

	return(response)

def deleteChangeRequest(ChangeRequestID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequest/" + str(ChangeRequestID), verb = "delete")

	return(response)

def getChangeRequestApprovalTask(ChangeRequestApprovalTaskID, EntityID = 1, returnArea = False, returnAreaCode = False, returnChangeRequestApprovalTaskIDClonedFrom = False, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnDescription = False, returnLevel = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestApprovalTask/" + str(ChangeRequestApprovalTaskID), verb = "get", params_list = params_list)

	return(response)

def deleteChangeRequestApprovalTask(ChangeRequestApprovalTaskID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestApprovalTask/" + str(ChangeRequestApprovalTaskID), verb = "delete")

	return(response)

def getChangeRequestApprovalTaskSecurityGroup(ChangeRequestApprovalTaskSecurityGroupID, EntityID = 1, returnChangeRequestApprovalTaskID = False, returnChangeRequestApprovalTaskSecurityGroupIDClonedFrom = False, returnCreatedTime = False, returnGroupIDSecurity = False, returnIsAlternate = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestApprovalTaskSecurityGroup/" + str(ChangeRequestApprovalTaskSecurityGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteChangeRequestApprovalTaskSecurityGroup(ChangeRequestApprovalTaskSecurityGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestApprovalTaskSecurityGroup/" + str(ChangeRequestApprovalTaskSecurityGroupID), verb = "delete")

	return(response)

def getChangeRequestDetail(ChangeRequestDetailID, EntityID = 1, returnChangeRequestID = False, returnCreatedTime = False, returnFieldName = False, returnFieldNameCode = False, returnModifiedTime = False, returnOriginalValue = False, returnRequestedTime = False, returnRequestedValue = False, returnSourceID = False, returnStatus = False, returnStatusCode = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRequestedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetail/" + str(ChangeRequestDetailID), verb = "get", params_list = params_list)

	return(response)

def deleteChangeRequestDetail(ChangeRequestDetailID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetail/" + str(ChangeRequestDetailID), verb = "delete")

	return(response)

def getChangeRequestDetailApproval(ChangeRequestDetailApprovalID, EntityID = 1, returnChangeRequestDetailID = False, returnComment = False, returnCreatedTime = False, returnIsLastLevel = False, returnLevel = False, returnLevelDescription = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnTaskInstanceID = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetailApproval/" + str(ChangeRequestDetailApprovalID), verb = "get", params_list = params_list)

	return(response)

def deleteChangeRequestDetailApproval(ChangeRequestDetailApprovalID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetailApproval/" + str(ChangeRequestDetailApprovalID), verb = "delete")

	return(response)

def getConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, returnChangeRequestFamilyEmail = False, returnChangeRequestFamilyEmailCode = False, returnChangeRequestFamilyPhone = False, returnChangeRequestFamilyPhoneCode = False, returnChangeRequestStudentEmail = False, returnChangeRequestStudentEmailCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDefaultFeeManagementOnlinePaymentAccess = False, returnDefaultFeeManagementOnlinePaymentAccessCode = False, returnDefaultFoodServiceOnlinePaymentAccess = False, returnDefaultFoodServiceOnlinePaymentAccessCode = False, returnDisplayAssignments = False, returnDisplayCalendarEvents = False, returnDisplayDistrictActivityEvents = False, returnDisplayStudentActivityEvents = False, returnEmailTypeIDToDisplayFamilyStudentAccess = False, returnEndorsementSignatureOption = False, returnEndorsementSignatureOptionCode = False, returnEndorsementSignatureStatement = False, returnEntityGroupKey = False, returnEntityID = False, returnFamilyAccessAccountInfoEmailBody = False, returnFamilyAccessAccountInfoEmailIncludeResetPasswordText = False, returnFamilyAccessAccountInfoEmailSubject = False, returnFamilyAccessCareerPlanDisplayShowDroppedCourses = False, returnFamilyAccessDisplayCommentCodes = False, returnFamilyAccessDisplayFreeFormComments = False, returnFamilyAccessDisplayGradeBucketsAfterEndDate = False, returnFamilyAccessDisplayHonorRoll = False, returnFamilyAccessDisplayOnlyCurrentAndCompleteGrades = False, returnFamilyAccessDisplayOnlyCurrentMissingAssignments = False, returnFamilyAccessDisplayShowActualEarnedCredits = False, returnFamilyAccessDisplayShowAttendance = False, returnFamilyAccessDisplayShowDroppedCourses = False, returnFamilyAccessDisplayShowEndedAttendanceTerms = False, returnFamilyAccessDisplayShowPossibleEarnedCredits = False, returnFamilyAccessDisplayStudentAddress = False, returnFamilyAccessDisplayStudentRank = False, returnFamilyAccessDisplayUseReportCardGradeBucketSettings = False, returnFamilyAccessLinkStudentSectionsOnReportCard = False, returnFamilyStudentAccessDisplayTeacherEmail = False, returnFamilyStudentAccessDisplayTeacherPhoneNumber = False, returnHideScheduleMessage = False, returnHideSchedulePriorToCalendarDays = False, returnIsFamilyInformationApprovalWorkflowUpdated = False, returnIsStudentInformationApprovalWorkflowUpdated = False, returnModifiedTime = False, returnPhoneTypeIDToDisplayFamilyStudentAccess = False, returnRankMethodIDFamilyAccessReportCardGrading = False, returnRankMethodIDFamilyAccessReportCardStudent = False, returnReportCardGPADisplay = False, returnReportCardGPADisplayCode = False, returnReportCardHeaderAddressType = False, returnReportCardHeaderAddressTypeCode = False, returnReportCardStudentRankDisplay = False, returnReportCardStudentRankDisplayCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "delete")

	return(response)

def getConfigSystem(ConfigSystemID, EntityID = 1, returnAddressValidationMessage = False, returnAllowFamilyAccessDefault = False, returnAllowOutOfRangeAddressesToSubmit = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnEnableAddressValidation = False, returnEnableNewStudentEnrollment = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigSystem/" + str(ConfigSystemID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigSystem(ConfigSystemID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigSystem/" + str(ConfigSystemID), verb = "delete")

	return(response)

def getFamily(FamilyID, EntityID = 1, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnHasStudentInSpecificDistrict = False, returnLanguageIDHome = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/Family/" + str(FamilyID), verb = "get", params_list = params_list)

	return(response)

def deleteFamily(FamilyID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/Family/" + str(FamilyID), verb = "delete")

	return(response)

def getFamilyGuardian(FamilyGuardianID, EntityID = 1, returnCreatedTime = False, returnFamilyID = False, returnHasActiveStudentGuardianRestrictedAccess = False, returnModifiedTime = False, returnNameID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/FamilyGuardian/" + str(FamilyGuardianID), verb = "get", params_list = params_list)

	return(response)

def deleteFamilyGuardian(FamilyGuardianID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/FamilyGuardian/" + str(FamilyGuardianID), verb = "delete")

	return(response)

def getStudentFamily(StudentFamilyID, EntityID = 1, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnFamilyID = False, returnHasEmployeeGuardian = False, returnIsEmergencyContact = False, returnIsPrimaryEmergencyContact = False, returnModifiedTime = False, returnRank = False, returnReceivesForms = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentFamily/" + str(StudentFamilyID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentFamily(StudentFamilyID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentFamily/" + str(StudentFamilyID), verb = "delete")

	return(response)

def getStudentGuardian(StudentGuardianID, EntityID = 1, returnAllowFamilyAccess = False, returnAllowStudentPickup = False, returnCreatedTime = False, returnFeeOnlinePaymentOverrideType = False, returnFeeOnlinePaymentOverrideTypeCode = False, returnFoodOnlinePaymentOverrideType = False, returnFoodOnlinePaymentOverrideTypeCode = False, returnGuardianCategory = False, returnGuardianNameIDAndFamilyID = False, returnHasActiveRestrictedAccess = False, returnHasUnrestrictedAccess = False, returnIsCustodialGuardian = False, returnIsEmergencyContact = False, returnModifiedTime = False, returnNameIDGuardian = False, returnNeedsSecurityGroupAudit = False, returnOverrideFeeOnlinePaymentAccess = False, returnOverrideFoodOnlinePaymentAccess = False, returnRank = False, returnRelationshipID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardian/" + str(StudentGuardianID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentGuardian(StudentGuardianID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardian/" + str(StudentGuardianID), verb = "delete")

	return(response)

def getStudentGuardianRestrictedAccess(StudentGuardianRestrictedAccessID, EntityID = 1, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnReason = False, returnStartDate = False, returnStudentGuardianID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardianRestrictedAccess/" + str(StudentGuardianRestrictedAccessID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentGuardianRestrictedAccess(StudentGuardianRestrictedAccessID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardianRestrictedAccess/" + str(StudentGuardianRestrictedAccessID), verb = "delete")

	return(response)

def getTempFamilyGuardian(TempFamilyGuardianID, EntityID = 1, returnCreatedTime = False, returnGuardianNameID = False, returnGuardianNameLFM = False, returnIsFamilyAccessUser = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/TempFamilyGuardian/" + str(TempFamilyGuardianID), verb = "get", params_list = params_list)

	return(response)

def deleteTempFamilyGuardian(TempFamilyGuardianID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/TempFamilyGuardian/" + str(TempFamilyGuardianID), verb = "delete")

	return(response)