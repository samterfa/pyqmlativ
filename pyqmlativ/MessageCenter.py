# This module contains MessageCenter functions.

from .Utilities import make_request

import pandas as pd

def getEveryConfigDistrictYear(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictYearID = True, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnNumberOfDaysAfterWithdrawalToAllowMessages = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, returnreturnConfigDistrictYearID = False, returnreturnConfigDistrictYearIDClonedFrom = False, returnreturnCreatedTime = False, returnreturnDistrictID = False, returnreturnModifiedTime = False, returnreturnNumberOfDaysAfterWithdrawalToAllowMessages = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigDistrictYear(ConfigDistrictYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "delete")

	return(response)

def getEveryConfigDistrictYearWithdrawalCode(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictYearWithdrawalCodeID = True, returnConfigDistrictYearID = False, returnConfigDistrictYearWithdrawalCodeIDClonedFrom = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYearWithdrawalCode/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigDistrictYearWithdrawalCode(ConfigDistrictYearWithdrawalCodeID, EntityID = 1, returnreturnConfigDistrictYearWithdrawalCodeID = False, returnreturnConfigDistrictYearID = False, returnreturnConfigDistrictYearWithdrawalCodeIDClonedFrom = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWithdrawalCodeID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYearWithdrawalCode/" + str(ConfigDistrictYearWithdrawalCodeID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigDistrictYearWithdrawalCode(ConfigDistrictYearWithdrawalCodeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYearWithdrawalCode/" + str(ConfigDistrictYearWithdrawalCodeID), verb = "delete")

	return(response)

def getEveryMessage(EntityID = 1, page = 1, pageSize = 100, returnMessageID = True, returnContent = False, returnCreatedTime = False, returnFromInformation = False, returnIncludeLinkToObject = False, returnIsHidden = False, returnIsRead = False, returnMessageIDCopiedFrom = False, returnMessageMasterID = False, returnModifiedTime = False, returnNoSourceIDRequired = False, returnObjectIDCreatedFor = False, returnObjectPrimaryKey = False, returnPostDate = False, returnPriorityType = False, returnPriorityTypeCode = False, returnSourceIDCreatedFor = False, returnSubject = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRecipient = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Message/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getMessage(MessageID, EntityID = 1, returnreturnMessageID = False, returnreturnContent = False, returnreturnCreatedTime = False, returnreturnFromInformation = False, returnreturnIncludeLinkToObject = False, returnreturnIsHidden = False, returnreturnIsRead = False, returnreturnMessageIDCopiedFrom = False, returnreturnMessageMasterID = False, returnreturnModifiedTime = False, returnreturnNoSourceIDRequired = False, returnreturnObjectIDCreatedFor = False, returnreturnObjectPrimaryKey = False, returnreturnPostDate = False, returnreturnPriorityType = False, returnreturnPriorityTypeCode = False, returnreturnSourceIDCreatedFor = False, returnreturnSubject = False, returnreturnType = False, returnreturnTypeCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserIDRecipient = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Message/" + str(MessageID), verb = "get", params_list = params_list)

	return(response)

def deleteMessage(MessageID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Message/" + str(MessageID), verb = "delete")

	return(response)

def getEveryMessageMaster(EntityID = 1, page = 1, pageSize = 100, returnMessageMasterID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCarbonCopyStaffIDList = False, returnContent = False, returnCreatedTime = False, returnCustomMessageData = False, returnEntityID = False, returnIncludeRestrictedGuardians = False, returnIsDraft = False, returnIsRetracted = False, returnLargestMessagePrimaryKey = False, returnModifiedTime = False, returnObjectIDCreatedFor = False, returnPostedTime = False, returnPriorityType = False, returnPriorityTypeCode = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnSourceIDCreatedFor = False, returnStatus = False, returnStatusCode = False, returnSubject = False, returnSubjectCleaned = False, returnToWhom = False, returnToWhomCode = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLFilter = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/MessageMaster/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getMessageMaster(MessageMasterID, EntityID = 1, returnreturnMessageMasterID = False, returnreturnAttachmentCount = False, returnreturnAttachmentIndicatorColumn = False, returnreturnCarbonCopyStaffIDList = False, returnreturnContent = False, returnreturnCreatedTime = False, returnreturnCustomMessageData = False, returnreturnEntityID = False, returnreturnIncludeRestrictedGuardians = False, returnreturnIsDraft = False, returnreturnIsRetracted = False, returnreturnLargestMessagePrimaryKey = False, returnreturnModifiedTime = False, returnreturnObjectIDCreatedFor = False, returnreturnPostedTime = False, returnreturnPriorityType = False, returnreturnPriorityTypeCode = False, returnreturnSchoolYearID = False, returnreturnSearchConditionFilter = False, returnreturnSourceIDCreatedFor = False, returnreturnStatus = False, returnreturnStatusCode = False, returnreturnSubject = False, returnreturnSubjectCleaned = False, returnreturnToWhom = False, returnreturnToWhomCode = False, returnreturnType = False, returnreturnTypeCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnXMLFilter = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/MessageMaster/" + str(MessageMasterID), verb = "get", params_list = params_list)

	return(response)

def deleteMessageMaster(MessageMasterID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/MessageMaster/" + str(MessageMasterID), verb = "delete")

	return(response)

def getEveryNotification(EntityID = 1, page = 1, pageSize = 100, returnNotificationID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnAttendanceCategoryForCount = False, returnAttendanceCategoryForCountCode = False, returnAttendanceCountHigh = False, returnAttendanceCountLow = False, returnAttendanceCountMethod = False, returnAttendanceCountMethodCode = False, returnConsiderAllStaffMeets = False, returnCreatedTime = False, returnDayType = False, returnDayTypeCode = False, returnEntityID = False, returnFeeManagementBalanceHigh = False, returnFeeManagementBalanceLow = False, returnFoodServiceBalanceHigh = False, returnFoodServiceBalanceLow = False, returnGradingPeriodEndDaysAfter = False, returnGradingPeriodEndDaysBefore = False, returnIncludeAutoGeneratedMessage = False, returnLastEntryType = False, returnLastEntryTypeCode = False, returnMessage = False, returnModifiedTime = False, returnNumberOfDays = False, returnPriorityType = False, returnPriorityTypeCode = False, returnScheduledTaskID = False, returnScheduleIsAvailableDaysBefore = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnSendNotificationForDay = False, returnSendNotificationForDayCode = False, returnSendNotificationForPriorDayCount = False, returnSendOnlyIfGuardianNotNotified = False, returnSendToDisciplineOfficer = False, returnSubject = False, returnSubjectCleaned = False, returnToWhom = False, returnToWhomCode = False, returnType = False, returnTypeCode = False, returnUnrecordedAttendanceMinutes = False, returnUnrecordedAttendancePeriodType = False, returnUnrecordedAttendancePeriodTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLFilter = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Notification/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNotification(NotificationID, EntityID = 1, returnreturnNotificationID = False, returnreturnAttachmentCount = False, returnreturnAttachmentIndicatorColumn = False, returnreturnAttendanceCategoryForCount = False, returnreturnAttendanceCategoryForCountCode = False, returnreturnAttendanceCountHigh = False, returnreturnAttendanceCountLow = False, returnreturnAttendanceCountMethod = False, returnreturnAttendanceCountMethodCode = False, returnreturnConsiderAllStaffMeets = False, returnreturnCreatedTime = False, returnreturnDayType = False, returnreturnDayTypeCode = False, returnreturnEntityID = False, returnreturnFeeManagementBalanceHigh = False, returnreturnFeeManagementBalanceLow = False, returnreturnFoodServiceBalanceHigh = False, returnreturnFoodServiceBalanceLow = False, returnreturnGradingPeriodEndDaysAfter = False, returnreturnGradingPeriodEndDaysBefore = False, returnreturnIncludeAutoGeneratedMessage = False, returnreturnLastEntryType = False, returnreturnLastEntryTypeCode = False, returnreturnMessage = False, returnreturnModifiedTime = False, returnreturnNumberOfDays = False, returnreturnPriorityType = False, returnreturnPriorityTypeCode = False, returnreturnScheduledTaskID = False, returnreturnScheduleIsAvailableDaysBefore = False, returnreturnSchoolYearID = False, returnreturnSearchConditionFilter = False, returnreturnSendNotificationForDay = False, returnreturnSendNotificationForDayCode = False, returnreturnSendNotificationForPriorDayCount = False, returnreturnSendOnlyIfGuardianNotNotified = False, returnreturnSendToDisciplineOfficer = False, returnreturnSubject = False, returnreturnSubjectCleaned = False, returnreturnToWhom = False, returnreturnToWhomCode = False, returnreturnType = False, returnreturnTypeCode = False, returnreturnUnrecordedAttendanceMinutes = False, returnreturnUnrecordedAttendancePeriodType = False, returnreturnUnrecordedAttendancePeriodTypeCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnXMLFilter = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Notification/" + str(NotificationID), verb = "get", params_list = params_list)

	return(response)

def deleteNotification(NotificationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Notification/" + str(NotificationID), verb = "delete")

	return(response)

def getEveryNotificationAction(EntityID = 1, page = 1, pageSize = 100, returnNotificationActionID = True, returnActionID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAction/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNotificationAction(NotificationActionID, EntityID = 1, returnreturnNotificationActionID = False, returnreturnActionID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNotificationID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAction/" + str(NotificationActionID), verb = "get", params_list = params_list)

	return(response)

def deleteNotificationAction(NotificationActionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAction/" + str(NotificationActionID), verb = "delete")

	return(response)

def getEveryNotificationAttendanceType(EntityID = 1, page = 1, pageSize = 100, returnNotificationAttendanceTypeID = True, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAttendanceType/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNotificationAttendanceType(NotificationAttendanceTypeID, EntityID = 1, returnreturnNotificationAttendanceTypeID = False, returnreturnAttendanceTypeID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNotificationID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAttendanceType/" + str(NotificationAttendanceTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteNotificationAttendanceType(NotificationAttendanceTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAttendanceType/" + str(NotificationAttendanceTypeID), verb = "delete")

	return(response)

def getEveryNotificationCarbonCopyStaff(EntityID = 1, page = 1, pageSize = 100, returnNotificationCarbonCopyStaffID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationCarbonCopyStaff/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNotificationCarbonCopyStaff(NotificationCarbonCopyStaffID, EntityID = 1, returnreturnNotificationCarbonCopyStaffID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNotificationID = False, returnreturnStaffID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationCarbonCopyStaff/" + str(NotificationCarbonCopyStaffID), verb = "get", params_list = params_list)

	return(response)

def deleteNotificationCarbonCopyStaff(NotificationCarbonCopyStaffID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationCarbonCopyStaff/" + str(NotificationCarbonCopyStaffID), verb = "delete")

	return(response)

def getEveryNotificationDisciplineThreshold(EntityID = 1, page = 1, pageSize = 100, returnNotificationDisciplineThresholdID = True, returnCreatedTime = False, returnDisciplineThresholdID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationDisciplineThreshold/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNotificationDisciplineThreshold(NotificationDisciplineThresholdID, EntityID = 1, returnreturnNotificationDisciplineThresholdID = False, returnreturnCreatedTime = False, returnreturnDisciplineThresholdID = False, returnreturnModifiedTime = False, returnreturnNotificationID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationDisciplineThreshold/" + str(NotificationDisciplineThresholdID), verb = "get", params_list = params_list)

	return(response)

def deleteNotificationDisciplineThreshold(NotificationDisciplineThresholdID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationDisciplineThreshold/" + str(NotificationDisciplineThresholdID), verb = "delete")

	return(response)

def getEveryNotificationGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnNotificationGradeBucketID = True, returnCreatedTime = False, returnGradeBucketID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNotificationGradeBucket(NotificationGradeBucketID, EntityID = 1, returnreturnNotificationGradeBucketID = False, returnreturnCreatedTime = False, returnreturnGradeBucketID = False, returnreturnModifiedTime = False, returnreturnNotificationID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeBucket/" + str(NotificationGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteNotificationGradeBucket(NotificationGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeBucket/" + str(NotificationGradeBucketID), verb = "delete")

	return(response)

def getEveryNotificationGradeMark(EntityID = 1, page = 1, pageSize = 100, returnNotificationGradeMarkID = True, returnCreatedTime = False, returnGradeMarkID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeMark/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNotificationGradeMark(NotificationGradeMarkID, EntityID = 1, returnreturnNotificationGradeMarkID = False, returnreturnCreatedTime = False, returnreturnGradeMarkID = False, returnreturnModifiedTime = False, returnreturnNotificationID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeMark/" + str(NotificationGradeMarkID), verb = "get", params_list = params_list)

	return(response)

def deleteNotificationGradeMark(NotificationGradeMarkID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeMark/" + str(NotificationGradeMarkID), verb = "delete")

	return(response)

def getEveryNotificationGradeReference(EntityID = 1, page = 1, pageSize = 100, returnNotificationGradeReferenceID = True, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeReference/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNotificationGradeReference(NotificationGradeReferenceID, EntityID = 1, returnreturnNotificationGradeReferenceID = False, returnreturnCreatedTime = False, returnreturnGradeReferenceID = False, returnreturnModifiedTime = False, returnreturnNotificationID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeReference/" + str(NotificationGradeReferenceID), verb = "get", params_list = params_list)

	return(response)

def deleteNotificationGradeReference(NotificationGradeReferenceID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeReference/" + str(NotificationGradeReferenceID), verb = "delete")

	return(response)

def getEveryNotificationOffense(EntityID = 1, page = 1, pageSize = 100, returnNotificationOffenseID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOffense/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNotificationOffense(NotificationOffenseID, EntityID = 1, returnreturnNotificationOffenseID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNotificationID = False, returnreturnOffenseID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOffense/" + str(NotificationOffenseID), verb = "get", params_list = params_list)

	return(response)

def deleteNotificationOffense(NotificationOffenseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOffense/" + str(NotificationOffenseID), verb = "delete")

	return(response)

def getEveryNotificationOnlineForm(EntityID = 1, page = 1, pageSize = 100, returnNotificationOnlineFormID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOnlineForm/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNotificationOnlineForm(NotificationOnlineFormID, EntityID = 1, returnreturnNotificationOnlineFormID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNotificationID = False, returnreturnOnlineFormID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOnlineForm/" + str(NotificationOnlineFormID), verb = "get", params_list = params_list)

	return(response)

def deleteNotificationOnlineForm(NotificationOnlineFormID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOnlineForm/" + str(NotificationOnlineFormID), verb = "delete")

	return(response)

def getEveryNotificationScheduleIsAvailableSectionLength(EntityID = 1, page = 1, pageSize = 100, returnNotificationScheduleIsAvailableSectionLengthID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationScheduleIsAvailableSectionLength/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNotificationScheduleIsAvailableSectionLength(NotificationScheduleIsAvailableSectionLengthID, EntityID = 1, returnreturnNotificationScheduleIsAvailableSectionLengthID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNotificationID = False, returnreturnSectionLengthID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationScheduleIsAvailableSectionLength/" + str(NotificationScheduleIsAvailableSectionLengthID), verb = "get", params_list = params_list)

	return(response)

def deleteNotificationScheduleIsAvailableSectionLength(NotificationScheduleIsAvailableSectionLengthID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationScheduleIsAvailableSectionLength/" + str(NotificationScheduleIsAvailableSectionLengthID), verb = "delete")

	return(response)

def getEveryNotificationUnrecordedClassAttendance(EntityID = 1, page = 1, pageSize = 100, returnNotificationUnrecordedClassAttendanceID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationUnrecordedClassAttendance/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNotificationUnrecordedClassAttendance(NotificationUnrecordedClassAttendanceID, EntityID = 1, returnreturnNotificationUnrecordedClassAttendanceID = False, returnreturnCreatedTime = False, returnreturnDisplayPeriodID = False, returnreturnModifiedTime = False, returnreturnNotificationID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationUnrecordedClassAttendance/" + str(NotificationUnrecordedClassAttendanceID), verb = "get", params_list = params_list)

	return(response)

def deleteNotificationUnrecordedClassAttendance(NotificationUnrecordedClassAttendanceID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationUnrecordedClassAttendance/" + str(NotificationUnrecordedClassAttendanceID), verb = "delete")

	return(response)

def getEveryNotificationWithdrawalCode(EntityID = 1, page = 1, pageSize = 100, returnNotificationWithdrawalCodeID = True, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationWithdrawalCode/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNotificationWithdrawalCode(NotificationWithdrawalCodeID, EntityID = 1, returnreturnNotificationWithdrawalCodeID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNotificationID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWithdrawalCodeID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationWithdrawalCode/" + str(NotificationWithdrawalCodeID), verb = "get", params_list = params_list)

	return(response)

def deleteNotificationWithdrawalCode(NotificationWithdrawalCodeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationWithdrawalCode/" + str(NotificationWithdrawalCodeID), verb = "delete")

	return(response)

def getEveryQueuedCompletedCareerPlanChangeNotification(EntityID = 1, page = 1, pageSize = 100, returnQueuedCompletedCareerPlanChangeNotificationID = True, returnCareerPlanGradeLevelIDCurrent = False, returnCareerPlanGradeLevelIDPrevious = False, returnCreatedTime = False, returnCreditsCurrent = False, returnCreditsPrevious = False, returnCurriculumID = False, returnEntityID = False, returnIsDeletedRecord = False, returnIsNewRecord = False, returnIsSent = False, returnIsStudentPermittedToChangeGradeLevelCurrent = False, returnIsStudentPermittedToChangeGradeLevelPrevious = False, returnIsStudentPermittedToDeleteCurrent = False, returnIsStudentPermittedToDeletePrevious = False, returnModifiedTime = False, returnNotificationID = False, returnSchoolYearID = False, returnStudentCareerPlanID = False, returnStudentCourseRequestIDCurrent = False, returnStudentCourseRequestIDPrevious = False, returnStudentID = False, returnStudentSubAreaIDCurrent = False, returnStudentSubAreaIDPrevious = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedCareerPlanChangeNotification/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getQueuedCompletedCareerPlanChangeNotification(QueuedCompletedCareerPlanChangeNotificationID, EntityID = 1, returnreturnQueuedCompletedCareerPlanChangeNotificationID = False, returnreturnCareerPlanGradeLevelIDCurrent = False, returnreturnCareerPlanGradeLevelIDPrevious = False, returnreturnCreatedTime = False, returnreturnCreditsCurrent = False, returnreturnCreditsPrevious = False, returnreturnCurriculumID = False, returnreturnEntityID = False, returnreturnIsDeletedRecord = False, returnreturnIsNewRecord = False, returnreturnIsSent = False, returnreturnIsStudentPermittedToChangeGradeLevelCurrent = False, returnreturnIsStudentPermittedToChangeGradeLevelPrevious = False, returnreturnIsStudentPermittedToDeleteCurrent = False, returnreturnIsStudentPermittedToDeletePrevious = False, returnreturnModifiedTime = False, returnreturnNotificationID = False, returnreturnSchoolYearID = False, returnreturnStudentCareerPlanID = False, returnreturnStudentCourseRequestIDCurrent = False, returnreturnStudentCourseRequestIDPrevious = False, returnreturnStudentID = False, returnreturnStudentSubAreaIDCurrent = False, returnreturnStudentSubAreaIDPrevious = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedCareerPlanChangeNotification/" + str(QueuedCompletedCareerPlanChangeNotificationID), verb = "get", params_list = params_list)

	return(response)

def deleteQueuedCompletedCareerPlanChangeNotification(QueuedCompletedCareerPlanChangeNotificationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedCareerPlanChangeNotification/" + str(QueuedCompletedCareerPlanChangeNotificationID), verb = "delete")

	return(response)

def getEveryQueuedCompletedGradeChangeNotification(EntityID = 1, page = 1, pageSize = 100, returnQueuedCompletedGradeChangeNotificationID = True, returnCreatedTime = False, returnEntityID = False, returnGradeMarkIDCurrent = False, returnGradeMarkIDPrevious = False, returnIsSent = False, returnModifiedTime = False, returnNotificationID = False, returnSchoolYearID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedGradeChangeNotification/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getQueuedCompletedGradeChangeNotification(QueuedCompletedGradeChangeNotificationID, EntityID = 1, returnreturnQueuedCompletedGradeChangeNotificationID = False, returnreturnCreatedTime = False, returnreturnEntityID = False, returnreturnGradeMarkIDCurrent = False, returnreturnGradeMarkIDPrevious = False, returnreturnIsSent = False, returnreturnModifiedTime = False, returnreturnNotificationID = False, returnreturnSchoolYearID = False, returnreturnStudentGradeBucketID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedGradeChangeNotification/" + str(QueuedCompletedGradeChangeNotificationID), verb = "get", params_list = params_list)

	return(response)

def deleteQueuedCompletedGradeChangeNotification(QueuedCompletedGradeChangeNotificationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedGradeChangeNotification/" + str(QueuedCompletedGradeChangeNotificationID), verb = "delete")

	return(response)

def getEveryTempMessage(EntityID = 1, page = 1, pageSize = 100, returnTempMessageID = True, returnCreatedTime = False, returnModifiedTime = False, returnRecipientName = False, returnRelationship = False, returnSectionInfo = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/TempMessage/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempMessage(TempMessageID, EntityID = 1, returnreturnTempMessageID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnRecipientName = False, returnreturnRelationship = False, returnreturnSectionInfo = False, returnreturnStudentName = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/TempMessage/" + str(TempMessageID), verb = "get", params_list = params_list)

	return(response)

def deleteTempMessage(TempMessageID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/TempMessage/" + str(TempMessageID), verb = "delete")

	return(response)

def getEveryUserMessageSetting(EntityID = 1, page = 1, pageSize = 100, returnUserMessageSettingID = True, returnAssignmentScoreHighNotification = False, returnAssignmentScoreHighNotificationEmail = False, returnAssignmentScoreLowNotification = False, returnAssignmentScoreLowNotificationEmail = False, returnCopyAttendanceMessagesToEmail = False, returnCopyDisciplineMessagesToEmail = False, returnCopyEnrollmentMessagesToEmail = False, returnCopyFeeManagementMessagesToEmail = False, returnCopyFoodServiceMessagesToEmail = False, returnCopyGradebookMessagesToEmail = False, returnCopyGradingMessagesToEmail = False, returnCopyGraduationRequirementsMessagesToEmail = False, returnCopyMessagesToEmail = False, returnCopyOnlineFormMessagesToEmail = False, returnCopySchedulingMessagesToEmail = False, returnCreatedTime = False, returnCurrentGradeScoreHighNotification = False, returnCurrentGradeScoreHighNotificationEmail = False, returnCurrentGradeScoreLowNotification = False, returnCurrentGradeScoreLowNotificationEmail = False, returnEnableCompletedCareerPlanChangeNotification = False, returnEnableCompletedCareerPlanChangeNotificationEmail = False, returnEnableCompletedGradeChangeNotification = False, returnEnableCompletedGradeChangeNotificationEmail = False, returnEnableGradebookGradeChangeRequestDeniedEmail = False, returnEnableGradebookGradeChangeRequestNotificationEmail = False, returnEnableGradebookLastEntryNotificationEmail = False, returnEnableOnlineAssignmentAvailableNotificationEmail = False, returnEnableOnlineAssingmentScoresAvailableNotificationEmail = False, returnEnableStudentScheduleChangeNotification = False, returnEnableStudentScheduleChangeNotificationEmail = False, returnGradebookHighAssignmentThreshold = False, returnGradebookHighThreshold = False, returnGradebookLowAssignmentThreshold = False, returnGradebookLowThreshold = False, returnMissingAssignmentNotification = False, returnMissingAssignmentNotificationEmail = False, returnModifiedTime = False, returnOnlySendAssignmentScoreHighNotificationsOncePerAssignment = False, returnOnlySendAssignmentScoreLowNotificationsOncePerAssignment = False, returnOnlySendCurrentGradeScoreHighNotificationsOnce = False, returnOnlySendCurrentGradeScoreLowNotificationsOnce = False, returnOnlySendMissingAssignmentNotificationForCurrentGradingPeriod = False, returnOnlySendMissingAssignmentNotificationsOncePerAssignment = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/UserMessageSetting/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getUserMessageSetting(UserMessageSettingID, EntityID = 1, returnreturnUserMessageSettingID = False, returnreturnAssignmentScoreHighNotification = False, returnreturnAssignmentScoreHighNotificationEmail = False, returnreturnAssignmentScoreLowNotification = False, returnreturnAssignmentScoreLowNotificationEmail = False, returnreturnCopyAttendanceMessagesToEmail = False, returnreturnCopyDisciplineMessagesToEmail = False, returnreturnCopyEnrollmentMessagesToEmail = False, returnreturnCopyFeeManagementMessagesToEmail = False, returnreturnCopyFoodServiceMessagesToEmail = False, returnreturnCopyGradebookMessagesToEmail = False, returnreturnCopyGradingMessagesToEmail = False, returnreturnCopyGraduationRequirementsMessagesToEmail = False, returnreturnCopyMessagesToEmail = False, returnreturnCopyOnlineFormMessagesToEmail = False, returnreturnCopySchedulingMessagesToEmail = False, returnreturnCreatedTime = False, returnreturnCurrentGradeScoreHighNotification = False, returnreturnCurrentGradeScoreHighNotificationEmail = False, returnreturnCurrentGradeScoreLowNotification = False, returnreturnCurrentGradeScoreLowNotificationEmail = False, returnreturnEnableCompletedCareerPlanChangeNotification = False, returnreturnEnableCompletedCareerPlanChangeNotificationEmail = False, returnreturnEnableCompletedGradeChangeNotification = False, returnreturnEnableCompletedGradeChangeNotificationEmail = False, returnreturnEnableGradebookGradeChangeRequestDeniedEmail = False, returnreturnEnableGradebookGradeChangeRequestNotificationEmail = False, returnreturnEnableGradebookLastEntryNotificationEmail = False, returnreturnEnableOnlineAssignmentAvailableNotificationEmail = False, returnreturnEnableOnlineAssingmentScoresAvailableNotificationEmail = False, returnreturnEnableStudentScheduleChangeNotification = False, returnreturnEnableStudentScheduleChangeNotificationEmail = False, returnreturnGradebookHighAssignmentThreshold = False, returnreturnGradebookHighThreshold = False, returnreturnGradebookLowAssignmentThreshold = False, returnreturnGradebookLowThreshold = False, returnreturnMissingAssignmentNotification = False, returnreturnMissingAssignmentNotificationEmail = False, returnreturnModifiedTime = False, returnreturnOnlySendAssignmentScoreHighNotificationsOncePerAssignment = False, returnreturnOnlySendAssignmentScoreLowNotificationsOncePerAssignment = False, returnreturnOnlySendCurrentGradeScoreHighNotificationsOnce = False, returnreturnOnlySendCurrentGradeScoreLowNotificationsOnce = False, returnreturnOnlySendMissingAssignmentNotificationForCurrentGradingPeriod = False, returnreturnOnlySendMissingAssignmentNotificationsOncePerAssignment = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserIDOwner = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/UserMessageSetting/" + str(UserMessageSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteUserMessageSetting(UserMessageSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/UserMessageSetting/" + str(UserMessageSettingID), verb = "delete")

	return(response)