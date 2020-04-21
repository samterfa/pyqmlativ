# This module contains Attendance functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryAttendancePeriod(searchConditions = [], EntityID = 1, returnAttendancePeriodID = False, returnAttendancePeriodIDClonedFrom = False, returnAttendancePeriodIDClonedTo = False, returnCode = False, returnCreatedTime = False, returnDisplayOrder = False, returnDynamicRelationshipID = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUseForSchoolTrakPositiveAttendance = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTeacherEntryCutOffTime = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AttendancePeriod in the district.

	This function returns a dataframe of every AttendancePeriod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAttendancePeriodConfigEntityGroupYear(searchConditions = [], EntityID = 1, returnAttendancePeriodConfigEntityGroupYearID = False, returnAttendancePeriodConfigEntityGroupYearIDClonedFrom = False, returnAttendancePeriodID = False, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnTeacherEntryCutoffDuration = False, returnTeacherEntryCutoffNumberOfMinutesAfter = False, returnTeacherEntryCutoffTime = False, returnTeacherEntryCutoffTimeCode = False, returnTeacherEntryCutoffWindowEndTime = False, returnTeacherEntryCutoffWindowStartTime = False, returnTeacherEntrySpecificCutoffTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AttendancePeriodConfigEntityGroupYear in the district.

	This function returns a dataframe of every AttendancePeriodConfigEntityGroupYear in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriodConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriodConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAttendanceReason(searchConditions = [], EntityID = 1, returnAttendanceReasonID = False, returnAttendanceReasonIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnTeacherEntryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AttendanceReason in the district.

	This function returns a dataframe of every AttendanceReason in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReason/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAttendanceReportRunHistory(searchConditions = [], EntityID = 1, returnAttendanceReportRunHistoryID = False, returnAttachmentDisplayName = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedSchoolYear = False, returnCountType = False, returnCreatedTime = False, returnDate = False, returnEntityID = False, returnEntityIDList = False, returnFilterType = False, returnFilterTypeCode = False, returnFiscalYearID = False, returnGracePeriod = False, returnIsActive = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnPostToFASA = False, returnPrintAttendanceLetterForWindowedEnvelope = False, returnReportRunInfoID = False, returnRunDescription = False, returnSchoolYearID = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AttendanceReportRunHistory in the district.

	This function returns a dataframe of every AttendanceReportRunHistory in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAttendanceReportRunHistoryThresholdResetRange(searchConditions = [], EntityID = 1, returnAttendanceReportRunHistoryThresholdResetRangeID = False, returnAttendanceReportRunHistoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AttendanceReportRunHistoryThresholdResetRange in the district.

	This function returns a dataframe of every AttendanceReportRunHistoryThresholdResetRange in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistoryThresholdResetRange/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistoryThresholdResetRange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAttendanceTerm(searchConditions = [], EntityID = 1, returnAttendanceTermID = False, returnAttendanceTermIDClonedFrom = False, returnCalendarID = False, returnCode = False, returnCreatedTime = False, returnDaysInTerm = False, returnEndDate = False, returnModifiedTime = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AttendanceTerm in the district.

	This function returns a dataframe of every AttendanceTerm in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAttendanceType(searchConditions = [], EntityID = 1, returnAttendanceTypeID = False, returnAttendanceTypeIDClonedFrom = False, returnAttendanceTypeMNID = False, returnCategory = False, returnCategoryCode = False, returnCategoryDescription = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnIncludeInClassCounts = False, returnIncludeInSpecialClassCounts = False, returnIncludeInTotals = False, returnIsTruant = False, returnModifiedTime = False, returnSchoolYearID = False, returnShowOnGradesheetAssignments = False, returnTeacherEntryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AttendanceType in the district.

	This function returns a dataframe of every AttendanceType in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBellSchedule(searchConditions = [], EntityID = 1, returnBellScheduleID = False, returnBellScheduleIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BellSchedule in the district.

	This function returns a dataframe of every BellSchedule in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBellScheduleGroup(searchConditions = [], EntityID = 1, returnBellScheduleGroupID = False, returnAttendancePeriodIDAsOfDate = False, returnBellScheduleGroupIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BellScheduleGroup in the district.

	This function returns a dataframe of every BellScheduleGroup in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBellScheduleGroupBellSchedule(searchConditions = [], EntityID = 1, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupID = False, returnBellScheduleID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BellScheduleGroupBellSchedule in the district.

	This function returns a dataframe of every BellScheduleGroupBellSchedule in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroupBellSchedule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroupBellSchedule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBellSchedulingPeriod(searchConditions = [], EntityID = 1, returnBellSchedulingPeriodID = False, returnBellScheduleID = False, returnBellSchedulingPeriodIDClonedFrom = False, returnCreatedTime = False, returnEndTime = False, returnEndTimeWithOverride = False, returnLengthInMinutes = False, returnModifiedTime = False, returnSchedulingPeriodID = False, returnStartTime = False, returnStartTimeWithOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BellSchedulingPeriod in the district.

	This function returns a dataframe of every BellSchedulingPeriod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedulingPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedulingPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCalendarDay(searchConditions = [], EntityID = 1, returnCalendarDayID = False, returnAttendanceTerm = False, returnBellScheduleGroupSummary = False, returnBellScheduleID = False, returnCalendarID = False, returnComment = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDateWithDayOfWeekAbbreviated = False, returnDayOfTheWeek = False, returnDayOfTheWeekNumber = False, returnDayRotationID = False, returnDynamicRelationshipID = False, returnFoodServicePurchaseExists = False, returnModifiedTime = False, returnNumberOfCalendarDayEvents = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CalendarDay in the district.

	This function returns a dataframe of every CalendarDay in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDay/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDay/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCalendarDayBellScheduleGroupBellSchedule(searchConditions = [], EntityID = 1, returnCalendarDayBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupID = False, returnCalendarDayID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CalendarDayBellScheduleGroupBellSchedule in the district.

	This function returns a dataframe of every CalendarDayBellScheduleGroupBellSchedule in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayBellScheduleGroupBellSchedule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayBellScheduleGroupBellSchedule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCalendarDayCalendarEvent(searchConditions = [], EntityID = 1, returnCalendarDayCalendarEventID = False, returnCalendarDayID = False, returnCalendarEventID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CalendarDayCalendarEvent in the district.

	This function returns a dataframe of every CalendarDayCalendarEvent in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayCalendarEvent/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayCalendarEvent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCalendarDayDisplayPeriodOverride(searchConditions = [], EntityID = 1, returnCalendarDayDisplayPeriodOverrideID = False, returnCalendarDayID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnLengthMinutes = False, returnModifiedTime = False, returnRemovePeriod = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CalendarDayDisplayPeriodOverride in the district.

	This function returns a dataframe of every CalendarDayDisplayPeriodOverride in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayDisplayPeriodOverride/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayDisplayPeriodOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCalendarDaySchedulingPeriodTimesOverride(searchConditions = [], EntityID = 1, returnCalendarDaySchedulingPeriodTimesOverrideID = False, returnCalendarDayID = False, returnCreatedTime = False, returnDurationInMinutes = False, returnEndTime = False, returnModifiedTime = False, returnSchedulingPeriodID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CalendarDaySchedulingPeriodTimesOverride in the district.

	This function returns a dataframe of every CalendarDaySchedulingPeriodTimesOverride in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDaySchedulingPeriodTimesOverride/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDaySchedulingPeriodTimesOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCalendarDisplayPeriod(searchConditions = [], EntityID = 1, returnCalendarDisplayPeriodID = False, returnCalendarDisplayPeriodIDClonedFrom = False, returnCalendarDisplayPeriodIDClonedTo = False, returnCalendarID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnIncludeInClassCounts = False, returnIncludeInTotalCounts = False, returnModifiedTime = False, returnTakeAttendance = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CalendarDisplayPeriod in the district.

	This function returns a dataframe of every CalendarDisplayPeriod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCalendarEvent(searchConditions = [], EntityID = 1, returnCalendarEventID = False, returnCalendarEventIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiCalendarEventID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CalendarEvent in the district.

	This function returns a dataframe of every CalendarEvent in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarEvent/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarEvent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCalendar(searchConditions = [], EntityID = 1, returnCalendarID = False, returnAttendanceCalculationMethod = False, returnAttendanceCalculationMethodCode = False, returnCalendarIDClonedFrom = False, returnCalendarIDClonedTo = False, returnCalendarMNID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDefaultDayLengthMinutes = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHalfDayHighPeriodCount = False, returnIsDefault = False, returnMCCCAcademicYearImportID = False, returnMCCCCalendarImportID = False, returnModifiedTime = False, returnNorthEastSemesterReportData = False, returnSchoolYearID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZeroDayHighPeriodCount = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Calendar in the district.

	This function returns a dataframe of every Calendar in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/Calendar/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/Calendar/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigEntityGroupYear(searchConditions = [], EntityID = 1, returnConfigEntityGroupYearID = False, returnAttendanceReasonIDTardyDefault = False, returnAttendanceTypeIDTardyDefault = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnEnableInOutTime = False, returnEntityGroupKey = False, returnEntityID = False, returnIncludeGradeLevelOnLetter = False, returnIncludeParentNameAndOrPhoneNumberOnLetter = False, returnIncludeSchoolOrCampusOnLetter = False, returnIncludeSignatureLineForOfficeOnLetter = False, returnIncludeSignatureLineForParentOnLetter = False, returnIncludeSignatureLineForStudentOnLetter = False, returnIncludeStudentNameAndOrNumberOnLetter = False, returnIncludeTardyCountOnLetter = False, returnModifiedTime = False, returnMultiPeriodClassCountMethod = False, returnMultiPeriodClassCountMethodCode = False, returnPresentBackgroundColor = False, returnPresentBackgroundColorHex = False, returnPresentBackgroundColorRgba = False, returnPrintAttendanceLetterForWindowedEnvelope = False, returnRestrictTeacherAttendanceUpdates = False, returnSchoolYearID = False, returnSpecialClassCountsLabel = False, returnTardyDefaultComment = False, returnTardyKioskTardySlipTitle = False, returnTeacherEntryCutoffDuration = False, returnTeacherEntryCutOffNumberOfMinutesAfter = False, returnTeacherEntryCutOffTime = False, returnTeacherEntryCutOffTimeCode = False, returnTeacherEntryCutoffWindowEndTime = False, returnTeacherEntryCutoffWindowStartTime = False, returnTeacherEntrySpecificCutOffTime = False, returnUseInOutTimeForCalculations = False, returnUseMarkAllStudentsPresentOnTile = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSpecialClassCounts = False, returnUseTardyCalculator = False, returnUseTardyKiosk = False, returnUseTeacherPerfectAttendanceConfirmation = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCrossEntityAttendanceReason(searchConditions = [], EntityID = 1, returnCrossEntityAttendanceReasonID = False, returnAttendanceReasonIDFrom = False, returnAttendanceReasonIDTo = False, returnCreatedTime = False, returnEntityIDTo = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CrossEntityAttendanceReason in the district.

	This function returns a dataframe of every CrossEntityAttendanceReason in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceReason/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCrossEntityAttendanceType(searchConditions = [], EntityID = 1, returnCrossEntityAttendanceTypeID = False, returnAttendanceTypeIDFrom = False, returnAttendanceTypeIDTo = False, returnCreatedTime = False, returnEntityIDTo = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CrossEntityAttendanceType in the district.

	This function returns a dataframe of every CrossEntityAttendanceType in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCrossEntityCalendarDisplayPeriod(searchConditions = [], EntityID = 1, returnCrossEntityCalendarDisplayPeriodID = False, returnCalendarDisplayPeriodIDFrom = False, returnCalendarDisplayPeriodIDTo = False, returnCreatedTime = False, returnCrossEntityCalendarDisplayPeriodIDClonedFrom = False, returnIsAutoCreated = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CrossEntityCalendarDisplayPeriod in the district.

	This function returns a dataframe of every CrossEntityCalendarDisplayPeriod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityCalendarDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityCalendarDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDailySectionAttendance(searchConditions = [], EntityID = 1, returnDailySectionAttendanceID = False, returnAttendancePeriodID = False, returnCalendarDayID = False, returnCreatedTime = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DailySectionAttendance in the district.

	This function returns a dataframe of every DailySectionAttendance in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DailySectionAttendance/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DailySectionAttendance/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDayRotationPattern(searchConditions = [], EntityID = 1, returnDayRotationPatternID = False, returnCreatedTime = False, returnDayNumber = False, returnDayRotationID = False, returnDayRotationPatternIDClonedFrom = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DayRotationPattern in the district.

	This function returns a dataframe of every DayRotationPattern in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DayRotationPattern/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DayRotationPattern/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDisciplineThreshold(searchConditions = [], EntityID = 1, returnDisciplineThresholdID = False, returnActionID = False, returnAllowDisciplineOnCurrentDay = False, returnAttendanceLettersRan = False, returnAttendanceSlipComment = False, returnBuildingIDServing = False, returnCreateDisciplineRecord = False, returnCreatedTime = False, returnDisciplineSlipComment = False, returnDurationToServe = False, returnDurationToServePerDay = False, returnFooterComment = False, returnGenerateActionDetail = False, returnGreeting = False, returnIncidentDefaultComment = False, returnIncidentDescription = False, returnIsRepeatable = False, returnLocationIDServing = False, returnModifiedTime = False, returnOffenseID = False, returnRangeDisplay = False, returnRoomIDServing = False, returnServeOnFriday = False, returnServeOnMonday = False, returnServeOnSaturday = False, returnServeOnSunday = False, returnServeOnThursday = False, returnServeOnTuesday = False, returnServeOnWednesday = False, returnServingTime = False, returnStaffIDAuthorizedBy = False, returnThresholdRangeHigh = False, returnThresholdRangeLow = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DisciplineThreshold in the district.

	This function returns a dataframe of every DisciplineThreshold in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DisciplineThreshold/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DisciplineThreshold/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDroppedStudentAttendancePeriod(searchConditions = [], EntityID = 1, returnDroppedStudentAttendancePeriodID = False, returnAttendancePeriodID = False, returnAttendanceReasonID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnComment = False, returnCreatedTime = False, returnIncidentOffenseNameActionDetailID = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DroppedStudentAttendancePeriod in the district.

	This function returns a dataframe of every DroppedStudentAttendancePeriod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DroppedStudentAttendancePeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DroppedStudentAttendancePeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMassCreateAttendanceByClassActivityRangeRun(searchConditions = [], EntityID = 1, returnMassCreateAttendanceByClassActivityRangeRunID = False, returnAffectedStudentAttendanceCount = False, returnCreatedTime = False, returnEntityID = False, returnIsActive = False, returnModifiedTime = False, returnRunTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRunBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MassCreateAttendanceByClassActivityRangeRun in the district.

	This function returns a dataframe of every MassCreateAttendanceByClassActivityRangeRun in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/MassCreateAttendanceByClassActivityRangeRun/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/MassCreateAttendanceByClassActivityRangeRun/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryRecordedUnrecordedAttendance(searchConditions = [], EntityID = 1, returnMeetDisplayPeriodID = False, returnAttendanceTaken = False, returnCountAs = False, returnCreatedTime = False, returnDailySectionAttendanceID = False, returnDate = False, returnDayOfTheWeek = False, returnDisplayPeriodCode = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every RecordedUnrecordedAttendance in the district.

	This function returns a dataframe of every RecordedUnrecordedAttendance in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RecordedUnrecordedAttendance/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RecordedUnrecordedAttendance/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryRoomLayout(searchConditions = [], EntityID = 1, returnRoomLayoutID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoomID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every RoomLayout in the district.

	This function returns a dataframe of every RoomLayout in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayout/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayout/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryRoomLayoutObject(searchConditions = [], EntityID = 1, returnRoomLayoutObjectID = False, returnCreatedTime = False, returnModifiedTime = False, returnRoomLayoutID = False, returnRoomObjectID = False, returnRotation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXLocation = False, returnYLocation = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every RoomLayoutObject in the district.

	This function returns a dataframe of every RoomLayoutObject in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayoutObject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayoutObject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryRoomObject(searchConditions = [], EntityID = 1, returnRoomObjectID = False, returnCreatedTime = False, returnIsStudentSeat = False, returnLabel = False, returnModifiedTime = False, returnParameters = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every RoomObject in the district.

	This function returns a dataframe of every RoomObject in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomObject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomObject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySeatingChart(searchConditions = [], EntityID = 1, returnSeatingChartID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoomLayoutID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SeatingChart in the district.

	This function returns a dataframe of every SeatingChart in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChart/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChart/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySeatingChartMeet(searchConditions = [], EntityID = 1, returnSeatingChartMeetID = False, returnCreatedTime = False, returnIsCurrent = False, returnMeetID = False, returnModifiedTime = False, returnSeatingChartID = False, returnSectionList = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SeatingChartMeet in the district.

	This function returns a dataframe of every SeatingChartMeet in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartMeet/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartMeet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySeatingChartSeat(searchConditions = [], EntityID = 1, returnSeatingChartSeatID = False, returnCreatedTime = False, returnModifiedTime = False, returnRoomLayoutObjectID = False, returnSeatingChartID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SeatingChartSeat in the district.

	This function returns a dataframe of every SeatingChartSeat in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartSeat/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartSeat/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySeatingChartUsedLast(searchConditions = [], EntityID = 1, returnSeatingChartUsedLastID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnRoomID = False, returnSeatingChartID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SeatingChartUsedLast in the district.

	This function returns a dataframe of every SeatingChartUsedLast in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartUsedLast/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartUsedLast/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStaffMeetSetting(searchConditions = [], EntityID = 1, returnStaffMeetSettingID = False, returnBrowseViewID = False, returnCreatedTime = False, returnDisplayAttendanceTotalsOnDesktop = False, returnDisplayAttendanceTotalsOnMobile = False, returnDisplayCourseDescription = False, returnDisplayHistoricalAttendanceOnDesktop = False, returnDisplayHistoricalAttendanceOnMobile = False, returnDisplayStudentGradeLevel = False, returnDisplayStudentNumber = False, returnHideLockedColumns = False, returnModifiedTime = False, returnStaffMeetID = False, returnStudentNameDisplayType = False, returnStudentNameDisplayTypeCode = False, returnUseCustomClassRosterSort = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StaffMeetSetting in the district.

	This function returns a dataframe of every StaffMeetSetting in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StaffMeetSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StaffMeetSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentAttendance(searchConditions = [], EntityID = 1, returnStudentAttendanceID = False, returnCalendarDayID = False, returnComment = False, returnCommentsExistForStudentAttendance = False, returnCreatedTime = False, returnDaysAbsent = False, returnDaysExcused = False, returnDaysOther = False, returnDaysUnexcused = False, returnEntityID = False, returnHideRecordMA = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnTardyCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentAttendance in the district.

	This function returns a dataframe of every StudentAttendance in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendance/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendance/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentAttendanceEntity(searchConditions = [], EntityID = 1, returnStudentAttendanceID = False, returnEntityID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentAttendanceEntity in the district.

	This function returns a dataframe of every StudentAttendanceEntity in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceEntity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentAttendancePeriod(searchConditions = [], EntityID = 1, returnStudentAttendancePeriodID = False, returnAttendancePeriodID = False, returnAttendanceReasonID = False, returnAttendanceTypeID = False, returnAttendanceTypeWithReason = False, returnComment = False, returnCreatedTime = False, returnCrossWalkedAttendanceTypeWithReason = False, returnEntityIDAttendancePeriod = False, returnEntityIDCourse = False, returnIncidentOffenseNameActionDetailID = False, returnModifiedTime = False, returnStudentAttendanceID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromAttendanceEntity = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentAttendancePeriod in the district.

	This function returns a dataframe of every StudentAttendancePeriod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentAttendancePeriodGroup(searchConditions = [], EntityID = 1, returnStudentAttendancePeriodID = False, returnAttendancePeriodID = False, returnEntityID = False, returnSchoolYearID = False, returnStudentAttendanceID = False, returnStudentID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentAttendancePeriodGroup in the district.

	This function returns a dataframe of every StudentAttendancePeriodGroup in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriodGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriodGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentAttendancePeriodRunHistory(searchConditions = [], EntityID = 1, returnStudentAttendancePeriodRunHistoryID = False, returnAttendancePeriodID = False, returnCreatedTime = False, returnIsActive = False, returnIsInsert = False, returnModifiedTime = False, returnNewAttendanceReasonID = False, returnNewAttendanceTypeID = False, returnNewComment = False, returnOriginalAttendanceReasonID = False, returnOriginalAttendanceTypeID = False, returnOriginalComment = False, returnProcedure = False, returnStatus = False, returnStudentAttendancePeriodID = False, returnStudentAttendanceRunHistoryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentAttendancePeriodRunHistory in the district.

	This function returns a dataframe of every StudentAttendancePeriodRunHistory in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriodRunHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriodRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentAttendanceRunHistory(searchConditions = [], EntityID = 1, returnStudentAttendanceRunHistoryID = False, returnCalendarDayID = False, returnCreatedTime = False, returnIsActive = False, returnIsInsert = False, returnMassCreateAttendanceByClassActivityRangeRunID = False, returnModifiedTime = False, returnNewComment = False, returnNewIsGuardianNotified = False, returnOriginalComment = False, returnOriginalIsGuardianNotified = False, returnProcedure = False, returnStatus = False, returnStudentAttendanceID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentAttendanceRunHistory in the district.

	This function returns a dataframe of every StudentAttendanceRunHistory in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceRunHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentAttendanceTerm(searchConditions = [], EntityID = 1, returnStudentID = False, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnEndDate = False, returnEntityID = False, returnIsDefault = False, returnSchoolYearID = False, returnStartDate = False, returnTotalDaysAbsent = False, returnTotalDaysExcused = False, returnTotalDaysOther = False, returnTotalDaysPossible = False, returnTotalDaysPresent = False, returnTotalDaysUnexcused = False, returnTotalTardyCount = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentAttendanceTerm in the district.

	This function returns a dataframe of every StudentAttendanceTerm in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentDisciplineThresholdAttendanceReportRunHistory(searchConditions = [], EntityID = 1, returnStudentDisciplineThresholdAttendanceReportRunHistoryID = False, returnAttachmentID = False, returnAttendanceReportRunHistoryID = False, returnBody = False, returnBodyForReport = False, returnCreatedTime = False, returnDisciplineThresholdID = False, returnFooter = False, returnFooterForReport = False, returnHeader = False, returnHeaderForReport = False, returnIsActive = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentDisciplineThresholdAttendanceReportRunHistory in the district.

	This function returns a dataframe of every StudentDisciplineThresholdAttendanceReportRunHistory in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentDisciplineThresholdAttendanceReportRunHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentDisciplineThresholdAttendanceReportRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentInOutTime(searchConditions = [], EntityID = 1, returnStudentInOutTimeID = False, returnCreatedTime = False, returnMinutesPresent = False, returnModifiedTime = False, returnPeriodTimes = False, returnStudentAttendanceID = False, returnTimeIn = False, returnTimeOut = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentInOutTime in the district.

	This function returns a dataframe of every StudentInOutTime in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentInOutTime/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentInOutTime/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentThresholdPeriod(searchConditions = [], EntityID = 1, returnStudentThresholdPeriodID = False, returnAttendancePeriodID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCountsTowardsThreshold = False, returnCreatedTime = False, returnDate = False, returnModifiedTime = False, returnSectionID = False, returnStudentAttendancePeriodID = False, returnStudentDisciplineThresholdAttendanceReportRunHistoryID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentThresholdPeriod in the district.

	This function returns a dataframe of every StudentThresholdPeriod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentThresholdPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentThresholdPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTeacherEntry(searchConditions = [], EntityID = 1, returnTeacherEntryID = False, returnBackgroundColor = False, returnBackgroundColorHex = False, returnBackgroundColorRgba = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnLabel = False, returnModifiedTime = False, returnSchoolYearID = False, returnTeacherEntryIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TeacherEntry in the district.

	This function returns a dataframe of every TeacherEntry in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TeacherEntry/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TeacherEntry/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempAffectedCalendarDayRecord(searchConditions = [], EntityID = 1, returnTempAffectedCalendarDayRecordID = False, returnAction = False, returnActionCode = False, returnAffectedPrimaryKey = False, returnCalendar = False, returnCalendarID = False, returnComment = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDayOfTheWeek = False, returnEntity = False, returnFailureReason = False, returnModifiedTime = False, returnNewBellSchedule = False, returnNewCountAs = False, returnNewDayRotation = False, returnNewDayRotationID = False, returnNewFundingPeriod = False, returnNewFundingPeriodID = False, returnNewInstructionalMinutesOverride = False, returnNewOperationalMinutesOverride = False, returnNewStateCalendarWaiverEventTypeCodeTX = False, returnNewStateCalendarWaiverEventTypeCodeTXID = False, returnNewStateSchoolDayEventCodeTX = False, returnNewStateSchoolDayEventCodeTXID = False, returnNewUseInstructionalMinutesOverride = False, returnNewUseOperationalMinutesOverride = False, returnNewWaiverMinutes = False, returnOldBellSchedule = False, returnOldDayRotation = False, returnOldDayRotationID = False, returnOldFundingPeriod = False, returnOldFundingPeriodID = False, returnOldInstructionalMinutesOverride = False, returnOldOperationalMinutesOverride = False, returnOldStateCalendarWaiverEventTypeCodeTX = False, returnOldStateCalendarWaiverEventTypeCodeTXID = False, returnOldStateSchoolDayEventCodeTX = False, returnOldStateSchoolDayEventCodeTXID = False, returnOldUseInstructionalMinutesOverride = False, returnOldUseOperationalMinutesOverride = False, returnOldWaiverMinutes = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempAffectedCalendarDayRecord in the district.

	This function returns a dataframe of every TempAffectedCalendarDayRecord in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedCalendarDayRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedCalendarDayRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempAffectedStudentAttendancePeriodRecord(searchConditions = [], EntityID = 1, returnTempAffectedStudentAttendancePeriodRecordID = False, returnAction = False, returnActionCode = False, returnAffectedPrimaryKey = False, returnAttendanceCategory = False, returnAttendancePeriodID = False, returnAttendanceReasonCodeDescription = False, returnAttendanceReasonID = False, returnAttendanceTypeCodeDescription = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCECEAttendancePeriodID = False, returnCECEAttendanceReasonID = False, returnCECEAttendanceTypeID = False, returnComment = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnEntity = False, returnFailureReason = False, returnFullName = False, returnIsForCECEAttendancePeriod = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnNewStudentSectionCode = False, returnNewStudentSectionID = False, returnOldStudentSectionCode = False, returnOldStudentSectionID = False, returnPeriodCode = False, returnProcessFromCECEEntity = False, returnStudentAttendanceID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempAffectedStudentAttendancePeriodRecord in the district.

	This function returns a dataframe of every TempAffectedStudentAttendancePeriodRecord in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendancePeriodRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendancePeriodRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempAffectedStudentAttendanceRecord(searchConditions = [], EntityID = 1, returnTempAffectedStudentAttendanceRecordID = False, returnAffectedPrimaryKey = False, returnCalendarDayID = False, returnComment = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnFailedStudentAttendancePeriods = False, returnFailureReason = False, returnFullName = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnNewDaysAbsent = False, returnNewDaysExcused = False, returnNewDaysOther = False, returnNewDaysUnexcused = False, returnNewGuardianNotified = False, returnNewStudentAttendancePeriods = False, returnNewTardyCount = False, returnOldDaysAbsent = False, returnOldDaysExcused = False, returnOldDaysOther = False, returnOldDaysUnexcused = False, returnOldStudentAttendancePeriods = False, returnOldTardyCount = False, returnPreviousGuardianNotified = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempAffectedStudentAttendanceRecord in the district.

	This function returns a dataframe of every TempAffectedStudentAttendanceRecord in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendanceRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendanceRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempAttendanceTerm(searchConditions = [], EntityID = 1, returnTempAttendanceTermID = False, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnCalendarCode = False, returnCalendarEndDate = False, returnCalendarID = False, returnCalendarStartDate = False, returnCreatedTime = False, returnEndDate = False, returnIsUpdated = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempAttendanceTerm in the district.

	This function returns a dataframe of every TempAttendanceTerm in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempBellScheduleGroupBellSchedule(searchConditions = [], EntityID = 1, returnTempBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupCodeDescription = False, returnBellScheduleGroupID = False, returnBellScheduleID = False, returnCreatedTime = False, returnIsDefault = False, returnModifiedTime = False, returnShouldUpdate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempBellScheduleGroupBellSchedule in the district.

	This function returns a dataframe of every TempBellScheduleGroupBellSchedule in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempBellScheduleGroupBellSchedule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempBellScheduleGroupBellSchedule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempCalendar(searchConditions = [], EntityID = 1, returnTempCalendarID = False, returnAffectedPrimaryKey = False, returnCalendarID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndDate = False, returnIsDefault = False, returnIsUpdated = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnOldEndDate = False, returnOldStartDate = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempCalendar in the district.

	This function returns a dataframe of every TempCalendar in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendar/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendar/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempCalendarAttendanceTerm(searchConditions = [], EntityID = 1, returnTempCalendarAttendanceTermID = False, returnAttendanceTermID = False, returnCalendarID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnStartDate = False, returnTableType = False, returnTableTypeCode = False, returnTableTypeString = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempCalendarAttendanceTerm in the district.

	This function returns a dataframe of every TempCalendarAttendanceTerm in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempCalendarDayBellScheduleGroupBellSchedule(searchConditions = [], EntityID = 1, returnTempCalendarDayBellScheduleGroupBellScheduleID = False, returnBellScheduleDescription = False, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupCodeDescription = False, returnBellScheduleGroupID = False, returnBellScheduleID = False, returnCalendar = False, returnCalendarDayID = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnExistingBellScheduleCode = False, returnExistingBellScheduleGroupBellScheduleID = False, returnExistingCalendarDayBellScheduleGroupBellScheduleID = False, returnIsDefault = False, returnModifiedTime = False, returnUpdateBellSchedule = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempCalendarDayBellScheduleGroupBellSchedule in the district.

	This function returns a dataframe of every TempCalendarDayBellScheduleGroupBellSchedule in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarDayBellScheduleGroupBellSchedule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarDayBellScheduleGroupBellSchedule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempCalendarDayCalendarEventRecord(searchConditions = [], EntityID = 1, returnTempCalendarDayCalendarEventRecordID = False, returnCalendar = False, returnCalendarDayID = False, returnCalendarEvent = False, returnCalendarEventID = False, returnCreatedTime = False, returnDate = False, returnFailureReason = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempCalendarDayCalendarEventRecord in the district.

	This function returns a dataframe of every TempCalendarDayCalendarEventRecord in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarDayCalendarEventRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarDayCalendarEventRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempCloneCalendarError(searchConditions = [], EntityID = 1, returnTempCloneCalendarErrorID = False, returnCreatedTime = False, returnDescription = False, returnEntityName = False, returnFailureReason = False, returnModifiedTime = False, returnRecordType = False, returnRecordTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempCloneCalendarError in the district.

	This function returns a dataframe of every TempCloneCalendarError in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempCloneCalendarRecord(searchConditions = [], EntityID = 1, returnTempCloneCalendarRecordID = False, returnAffectedPrimaryKey = False, returnAttendanceCalculationMethod = False, returnAttendanceCalculationMethodCode = False, returnCode = False, returnCreatedTime = False, returnDefaultDayLengthMinutes = False, returnDescription = False, returnEndDate = False, returnEntity = False, returnEntityID = False, returnHalfDayHighPeriodCount = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZeroDayHighPeriodCount = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempCloneCalendarRecord in the district.

	This function returns a dataframe of every TempCloneCalendarRecord in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentAttendanceRecord(searchConditions = [], EntityID = 1, returnTempStudentAttendanceRecordID = False, returnAffectedPrimaryKey = False, returnAttendanceTakenByPeriod = False, returnCreatedTime = False, returnDate = False, returnDayOfTheWeek = False, returnDayRotation = False, returnDayRotationID = False, returnGuardianNotified = False, returnModifiedTime = False, returnStudentName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentAttendanceRecord in the district.

	This function returns a dataframe of every TempStudentAttendanceRecord in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentAttendanceRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentAttendanceRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentDisciplineThresholdAttendanceReportRunHistoryRecord(searchConditions = [], EntityID = 1, returnTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = False, returnCountType = False, returnCountTypeCode = False, returnCreatedTime = False, returnDateHigh = False, returnDateLow = False, returnDateType = False, returnDateTypeCode = False, returnDayCountType = False, returnDayCountTypeCode = False, returnDisciplineThresholdID = False, returnModifiedTime = False, returnNumberOfDays = False, returnResetRangeAttendanceTypes = False, returnStudentID = False, returnStudentName = False, returnThresholdValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentDisciplineThresholdAttendanceReportRunHistoryRecord in the district.

	This function returns a dataframe of every TempStudentDisciplineThresholdAttendanceReportRunHistoryRecord in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentDisciplineThresholdAttendanceReportRunHistoryRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentDisciplineThresholdAttendanceReportRunHistoryRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentThresholdPeriodRecord(searchConditions = [], EntityID = 1, returnTempStudentThresholdPeriodRecordID = False, returnAttendancePeriodID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCreatedTime = False, returnDate = False, returnModifiedTime = False, returnSectionID = False, returnStudentAttendancePeriodID = False, returnStudentSectionID = False, returnTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentThresholdPeriodRecord in the district.

	This function returns a dataframe of every TempStudentThresholdPeriodRecord in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentThresholdPeriodRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentThresholdPeriodRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryThresholdResetRange(searchConditions = [], EntityID = 1, returnThresholdResetRangeID = False, returnAttendanceLettersRan = False, returnAttendanceTypeCodes = False, returnCountType = False, returnCountTypeCode = False, returnCreatedTime = False, returnDateDisplay = False, returnDateHigh = False, returnDateLow = False, returnDateType = False, returnDateTypeCode = False, returnDayCountType = False, returnDayCountTypeCode = False, returnEntityID = False, returnIsForAttendanceLetters = False, returnIsForTardyKiosk = False, returnModifiedTime = False, returnNumberOfDays = False, returnNumberPerDay = False, returnResetRangeAttendanceTypes = False, returnSchoolYearID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ThresholdResetRange in the district.

	This function returns a dataframe of every ThresholdResetRange in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRange/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryThresholdResetRangeAttendancePeriod(searchConditions = [], EntityID = 1, returnThresholdResetRangeAttendancePeriodID = False, returnAttendancePeriodID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ThresholdResetRangeAttendancePeriod in the district.

	This function returns a dataframe of every ThresholdResetRangeAttendancePeriod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendancePeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendancePeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryThresholdResetRangeAttendanceType(searchConditions = [], EntityID = 1, returnThresholdResetRangeAttendanceTypeID = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ThresholdResetRangeAttendanceType in the district.

	This function returns a dataframe of every ThresholdResetRangeAttendanceType in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendanceType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendanceType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)