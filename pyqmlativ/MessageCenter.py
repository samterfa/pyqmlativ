# This module contains MessageCenter functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryConfigDistrictYear(searchConditions = [], EntityID = 1, returnConfigDistrictYearID = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnNumberOfDaysAfterWithdrawalToAllowMessages = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigDistrictYearWithdrawalCode(searchConditions = [], EntityID = 1, returnConfigDistrictYearWithdrawalCodeID = False, returnConfigDistrictYearID = False, returnConfigDistrictYearWithdrawalCodeIDClonedFrom = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ConfigDistrictYearWithdrawalCode in the district.

	This function returns a dataframe of every ConfigDistrictYearWithdrawalCode in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYearWithdrawalCode/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYearWithdrawalCode/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMessage(searchConditions = [], EntityID = 1, returnMessageID = False, returnContent = False, returnCreatedTime = False, returnEmailRecipientType = False, returnEmailsSent = False, returnFromInformation = False, returnIncludeLinkToObject = False, returnIsHidden = False, returnIsRead = False, returnMessageIDCopiedFrom = False, returnMessageMasterID = False, returnModifiedTime = False, returnNoSourceIDRequired = False, returnObjectIDCreatedFor = False, returnObjectPrimaryKey = False, returnPostDate = False, returnPriorityType = False, returnPriorityTypeCode = False, returnSourceIDCreatedFor = False, returnSubject = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRecipient = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Message in the district.

	This function returns a dataframe of every Message in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Message/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Message/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMessageMaster(searchConditions = [], EntityID = 1, returnMessageMasterID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCarbonCopyStaffIDList = False, returnContent = False, returnCreatedTime = False, returnCustomMessageData = False, returnEntityID = False, returnIncludeRestrictedGuardians = False, returnIsDraft = False, returnIsRetracted = False, returnLargestMessagePrimaryKey = False, returnModifiedTime = False, returnObjectIDCreatedFor = False, returnPostedTime = False, returnPriorityType = False, returnPriorityTypeCode = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnSourceIDCreatedFor = False, returnStatus = False, returnStatusCode = False, returnSubject = False, returnSubjectCleaned = False, returnToWhom = False, returnToWhomCode = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLFilter = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MessageMaster in the district.

	This function returns a dataframe of every MessageMaster in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/MessageMaster/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/MessageMaster/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNotification(searchConditions = [], EntityID = 1, returnNotificationID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnAttendanceCategoryForCount = False, returnAttendanceCategoryForCountCode = False, returnAttendanceCountHigh = False, returnAttendanceCountLow = False, returnAttendanceCountMethod = False, returnAttendanceCountMethodCode = False, returnConsiderAllStaffMeets = False, returnCreatedTime = False, returnDayType = False, returnDayTypeCode = False, returnEntityID = False, returnFeeManagementBalanceHigh = False, returnFeeManagementBalanceLow = False, returnFoodServiceBalanceHigh = False, returnFoodServiceBalanceLow = False, returnGradingPeriodEndDaysAfter = False, returnGradingPeriodEndDaysBefore = False, returnIncludeAutoGeneratedMessage = False, returnLastEntryType = False, returnLastEntryTypeCode = False, returnMessage = False, returnModifiedTime = False, returnNumberOfDays = False, returnPriorityType = False, returnPriorityTypeCode = False, returnScheduledTaskID = False, returnScheduleIsAvailableDaysBefore = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnSendNotificationForDay = False, returnSendNotificationForDayCode = False, returnSendNotificationForPriorDayCount = False, returnSendOnlyIfGuardianNotNotified = False, returnSendToDisciplineOfficer = False, returnSubject = False, returnSubjectCleaned = False, returnToWhom = False, returnToWhomCode = False, returnType = False, returnTypeCode = False, returnUnrecordedAttendanceMinutes = False, returnUnrecordedAttendancePeriodType = False, returnUnrecordedAttendancePeriodTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLFilter = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Notification in the district.

	This function returns a dataframe of every Notification in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Notification/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Notification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNotificationAction(searchConditions = [], EntityID = 1, returnNotificationActionID = False, returnActionID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NotificationAction in the district.

	This function returns a dataframe of every NotificationAction in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNotificationAttendanceType(searchConditions = [], EntityID = 1, returnNotificationAttendanceTypeID = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NotificationAttendanceType in the district.

	This function returns a dataframe of every NotificationAttendanceType in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAttendanceType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAttendanceType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNotificationCarbonCopyStaff(searchConditions = [], EntityID = 1, returnNotificationCarbonCopyStaffID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NotificationCarbonCopyStaff in the district.

	This function returns a dataframe of every NotificationCarbonCopyStaff in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationCarbonCopyStaff/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationCarbonCopyStaff/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNotificationDisciplineThreshold(searchConditions = [], EntityID = 1, returnNotificationDisciplineThresholdID = False, returnCreatedTime = False, returnDisciplineThresholdID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NotificationDisciplineThreshold in the district.

	This function returns a dataframe of every NotificationDisciplineThreshold in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationDisciplineThreshold/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationDisciplineThreshold/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNotificationGradeBucket(searchConditions = [], EntityID = 1, returnNotificationGradeBucketID = False, returnCreatedTime = False, returnGradeBucketID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NotificationGradeBucket in the district.

	This function returns a dataframe of every NotificationGradeBucket in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNotificationGradeMark(searchConditions = [], EntityID = 1, returnNotificationGradeMarkID = False, returnCreatedTime = False, returnGradeMarkID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NotificationGradeMark in the district.

	This function returns a dataframe of every NotificationGradeMark in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeMark/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeMark/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNotificationGradeReference(searchConditions = [], EntityID = 1, returnNotificationGradeReferenceID = False, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NotificationGradeReference in the district.

	This function returns a dataframe of every NotificationGradeReference in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeReference/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeReference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNotificationOffense(searchConditions = [], EntityID = 1, returnNotificationOffenseID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NotificationOffense in the district.

	This function returns a dataframe of every NotificationOffense in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOffense/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOffense/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNotificationOnlineForm(searchConditions = [], EntityID = 1, returnNotificationOnlineFormID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NotificationOnlineForm in the district.

	This function returns a dataframe of every NotificationOnlineForm in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOnlineForm/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOnlineForm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNotificationScheduleIsAvailableSectionLength(searchConditions = [], EntityID = 1, returnNotificationScheduleIsAvailableSectionLengthID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NotificationScheduleIsAvailableSectionLength in the district.

	This function returns a dataframe of every NotificationScheduleIsAvailableSectionLength in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationScheduleIsAvailableSectionLength/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationScheduleIsAvailableSectionLength/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNotificationUnrecordedClassAttendance(searchConditions = [], EntityID = 1, returnNotificationUnrecordedClassAttendanceID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NotificationUnrecordedClassAttendance in the district.

	This function returns a dataframe of every NotificationUnrecordedClassAttendance in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationUnrecordedClassAttendance/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationUnrecordedClassAttendance/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNotificationWithdrawalCode(searchConditions = [], EntityID = 1, returnNotificationWithdrawalCodeID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NotificationWithdrawalCode in the district.

	This function returns a dataframe of every NotificationWithdrawalCode in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationWithdrawalCode/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationWithdrawalCode/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryQueuedCompletedCareerPlanChangeNotification(searchConditions = [], EntityID = 1, returnQueuedCompletedCareerPlanChangeNotificationID = False, returnCareerPlanGradeLevelIDCurrent = False, returnCareerPlanGradeLevelIDPrevious = False, returnCreatedTime = False, returnCreditsCurrent = False, returnCreditsPrevious = False, returnCurriculumID = False, returnEntityID = False, returnIsDeletedRecord = False, returnIsNewRecord = False, returnIsSent = False, returnIsStudentPermittedToChangeGradeLevelCurrent = False, returnIsStudentPermittedToChangeGradeLevelPrevious = False, returnIsStudentPermittedToDeleteCurrent = False, returnIsStudentPermittedToDeletePrevious = False, returnModifiedTime = False, returnNotificationID = False, returnSchoolYearID = False, returnStudentCareerPlanID = False, returnStudentCourseRequestIDCurrent = False, returnStudentCourseRequestIDPrevious = False, returnStudentID = False, returnStudentSubAreaIDCurrent = False, returnStudentSubAreaIDPrevious = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every QueuedCompletedCareerPlanChangeNotification in the district.

	This function returns a dataframe of every QueuedCompletedCareerPlanChangeNotification in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedCareerPlanChangeNotification/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedCareerPlanChangeNotification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryQueuedCompletedGradeChangeNotification(searchConditions = [], EntityID = 1, returnQueuedCompletedGradeChangeNotificationID = False, returnCreatedTime = False, returnEntityID = False, returnGradeMarkIDCurrent = False, returnGradeMarkIDPrevious = False, returnIsSent = False, returnModifiedTime = False, returnNotificationID = False, returnSchoolYearID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every QueuedCompletedGradeChangeNotification in the district.

	This function returns a dataframe of every QueuedCompletedGradeChangeNotification in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedGradeChangeNotification/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedGradeChangeNotification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySystemEmailTypeConfig(searchConditions = [], EntityID = 1, returnSystemEmailTypeConfigID = False, returnCreatedTime = False, returnEmailRecipientType = False, returnEmailTypeID = False, returnModifiedTime = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SystemEmailTypeConfig in the district.

	This function returns a dataframe of every SystemEmailTypeConfig in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/SystemEmailTypeConfig/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/SystemEmailTypeConfig/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempMessage(searchConditions = [], EntityID = 1, returnTempMessageID = False, returnCreatedTime = False, returnModifiedTime = False, returnRecipientName = False, returnRelationship = False, returnSectionInfo = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempMessage in the district.

	This function returns a dataframe of every TempMessage in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/TempMessage/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/TempMessage/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUserMessageSetting(searchConditions = [], EntityID = 1, returnUserMessageSettingID = False, returnAssignmentScoreHighNotification = False, returnAssignmentScoreHighNotificationEmail = False, returnAssignmentScoreLowNotification = False, returnAssignmentScoreLowNotificationEmail = False, returnCopyAttendanceMessagesToEmail = False, returnCopyDisciplineMessagesToEmail = False, returnCopyEnrollmentMessagesToEmail = False, returnCopyFamilyAccessMessagesToEmail = False, returnCopyFeeManagementMessagesToEmail = False, returnCopyFoodServiceMessagesToEmail = False, returnCopyGradebookMessagesToEmail = False, returnCopyGradingMessagesToEmail = False, returnCopyGraduationRequirementsMessagesToEmail = False, returnCopyMessagesToEmail = False, returnCopyOnlineFormMessagesToEmail = False, returnCopySchedulingMessagesToEmail = False, returnCreatedTime = False, returnCurrentGradeScoreHighNotification = False, returnCurrentGradeScoreHighNotificationEmail = False, returnCurrentGradeScoreLowNotification = False, returnCurrentGradeScoreLowNotificationEmail = False, returnEnableCompletedCareerPlanChangeNotification = False, returnEnableCompletedCareerPlanChangeNotificationEmail = False, returnEnableCompletedGradeChangeNotification = False, returnEnableCompletedGradeChangeNotificationEmail = False, returnEnableGradebookGradeChangeRequestDeniedEmail = False, returnEnableGradebookGradeChangeRequestNotificationEmail = False, returnEnableGradebookLastEntryNotificationEmail = False, returnEnableOnlineAssignmentAvailableNotificationEmail = False, returnEnableOnlineAssingmentScoresAvailableNotificationEmail = False, returnEnableStudentScheduleChangeNotification = False, returnEnableStudentScheduleChangeNotificationEmail = False, returnGradebookHighAssignmentThreshold = False, returnGradebookHighThreshold = False, returnGradebookLowAssignmentThreshold = False, returnGradebookLowThreshold = False, returnMissingAssignmentNotification = False, returnMissingAssignmentNotificationEmail = False, returnModifiedTime = False, returnOnlySendAssignmentScoreHighNotificationsOncePerAssignment = False, returnOnlySendAssignmentScoreLowNotificationsOncePerAssignment = False, returnOnlySendCurrentGradeScoreHighNotificationsOnce = False, returnOnlySendCurrentGradeScoreLowNotificationsOnce = False, returnOnlySendMissingAssignmentNotificationForCurrentGradingPeriod = False, returnOnlySendMissingAssignmentNotificationsOncePerAssignment = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every UserMessageSetting in the district.

	This function returns a dataframe of every UserMessageSetting in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/UserMessageSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/UserMessageSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)