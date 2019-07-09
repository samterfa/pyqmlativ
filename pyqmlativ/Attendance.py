# This module contains Attendance functions.

from . import make_request

def getAttendancePeriod(AttendancePeriodID, EntityID = 1, returnAttendancePeriodIDClonedFrom = False, returnAttendancePeriodIDClonedTo = False, returnCode = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTeacherEntryCutOffTime = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "get", params_list = params_list)

	return(response)

def deleteAttendancePeriod(AttendancePeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

	return(response)

def getAttendancePeriodConfigEntityGroupYear(AttendancePeriodConfigEntityGroupYearID, EntityID = 1, returnAttendancePeriodConfigEntityGroupYearIDClonedFrom = False, returnAttendancePeriodID = False, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnTeacherEntryCutoffDuration = False, returnTeacherEntryCutoffNumberOfMinutesAfter = False, returnTeacherEntryCutoffTime = False, returnTeacherEntryCutoffTimeCode = False, returnTeacherEntryCutoffWindowEndTime = False, returnTeacherEntryCutoffWindowStartTime = False, returnTeacherEntrySpecificCutoffTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriodConfigEntityGroupYear/" + str(AttendancePeriodConfigEntityGroupYearID), verb = "get", params_list = params_list)

	return(response)

def deleteAttendancePeriodConfigEntityGroupYear(AttendancePeriodConfigEntityGroupYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriodConfigEntityGroupYear/" + str(AttendancePeriodConfigEntityGroupYearID), verb = "delete")

	return(response)

def getAttendanceReason(AttendanceReasonID, EntityID = 1, returnAttendanceReasonIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnTeacherEntryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReason/" + str(AttendanceReasonID), verb = "get", params_list = params_list)

	return(response)

def deleteAttendanceReason(AttendanceReasonID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReason/" + str(AttendanceReasonID), verb = "delete")

	return(response)

def getAttendanceReportRunHistory(AttendanceReportRunHistoryID, EntityID = 1, returnCountType = False, returnCreatedTime = False, returnDate = False, returnEntityID = False, returnFilterType = False, returnFilterTypeCode = False, returnGracePeriod = False, returnIsActive = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnRunDescription = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistory/" + str(AttendanceReportRunHistoryID), verb = "get", params_list = params_list)

	return(response)

def deleteAttendanceReportRunHistory(AttendanceReportRunHistoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistory/" + str(AttendanceReportRunHistoryID), verb = "delete")

	return(response)

def getAttendanceReportRunHistoryThresholdResetRange(AttendanceReportRunHistoryThresholdResetRangeID, EntityID = 1, returnAttendanceReportRunHistoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistoryThresholdResetRange/" + str(AttendanceReportRunHistoryThresholdResetRangeID), verb = "get", params_list = params_list)

	return(response)

def deleteAttendanceReportRunHistoryThresholdResetRange(AttendanceReportRunHistoryThresholdResetRangeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistoryThresholdResetRange/" + str(AttendanceReportRunHistoryThresholdResetRangeID), verb = "delete")

	return(response)

def getAttendanceTerm(AttendanceTermID, EntityID = 1, returnAttendanceTermIDClonedFrom = False, returnCalendarID = False, returnCode = False, returnCreatedTime = False, returnDaysInTerm = False, returnEndDate = False, returnModifiedTime = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceTerm/" + str(AttendanceTermID), verb = "get", params_list = params_list)

	return(response)

def deleteAttendanceTerm(AttendanceTermID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceTerm/" + str(AttendanceTermID), verb = "delete")

	return(response)

def getAttendanceType(AttendanceTypeID, EntityID = 1, returnAttendanceTypeIDClonedFrom = False, returnAttendanceTypeMNID = False, returnCategory = False, returnCategoryCode = False, returnCategoryDescription = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnIncludeInClassCounts = False, returnIncludeInSpecialClassCounts = False, returnIncludeInTotals = False, returnIsTruant = False, returnModifiedTime = False, returnSchoolYearID = False, returnShowOnGradesheetAssignments = False, returnTeacherEntryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceType/" + str(AttendanceTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteAttendanceType(AttendanceTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceType/" + str(AttendanceTypeID), verb = "delete")

	return(response)

def getBellSchedule(BellScheduleID, EntityID = 1, returnBellScheduleIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedule/" + str(BellScheduleID), verb = "get", params_list = params_list)

	return(response)

def deleteBellSchedule(BellScheduleID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedule/" + str(BellScheduleID), verb = "delete")

	return(response)

def getBellScheduleGroup(BellScheduleGroupID, EntityID = 1, returnAttendancePeriodIDAsOfDate = False, returnBellScheduleGroupIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroup/" + str(BellScheduleGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteBellScheduleGroup(BellScheduleGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroup/" + str(BellScheduleGroupID), verb = "delete")

	return(response)

def getBellScheduleGroupBellSchedule(BellScheduleGroupBellScheduleID, EntityID = 1, returnBellScheduleGroupID = False, returnBellScheduleID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroupBellSchedule/" + str(BellScheduleGroupBellScheduleID), verb = "get", params_list = params_list)

	return(response)

def deleteBellScheduleGroupBellSchedule(BellScheduleGroupBellScheduleID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroupBellSchedule/" + str(BellScheduleGroupBellScheduleID), verb = "delete")

	return(response)

def getBellSchedulingPeriod(BellSchedulingPeriodID, EntityID = 1, returnBellScheduleID = False, returnBellSchedulingPeriodIDClonedFrom = False, returnCreatedTime = False, returnEndTime = False, returnEndTimeWithOverride = False, returnLengthInMinutes = False, returnModifiedTime = False, returnSchedulingPeriodID = False, returnStartTime = False, returnStartTimeWithOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedulingPeriod/" + str(BellSchedulingPeriodID), verb = "get", params_list = params_list)

	return(response)

def deleteBellSchedulingPeriod(BellSchedulingPeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedulingPeriod/" + str(BellSchedulingPeriodID), verb = "delete")

	return(response)

def getCalendarDay(CalendarDayID, EntityID = 1, returnAttendanceTerm = False, returnBellScheduleGroupSummary = False, returnBellScheduleID = False, returnCalendarID = False, returnComment = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDateWithDayOfWeekAbbreviated = False, returnDayOfTheWeek = False, returnDayOfTheWeekNumber = False, returnDayRotationID = False, returnModifiedTime = False, returnNumberOfCalendarDayEvents = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDay/" + str(CalendarDayID), verb = "get", params_list = params_list)

	return(response)

def deleteCalendarDay(CalendarDayID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDay/" + str(CalendarDayID), verb = "delete")

	return(response)

def getCalendarDayBellScheduleGroupBellSchedule(CalendarDayBellScheduleGroupBellScheduleID, EntityID = 1, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupID = False, returnCalendarDayID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayBellScheduleGroupBellSchedule/" + str(CalendarDayBellScheduleGroupBellScheduleID), verb = "get", params_list = params_list)

	return(response)

def deleteCalendarDayBellScheduleGroupBellSchedule(CalendarDayBellScheduleGroupBellScheduleID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayBellScheduleGroupBellSchedule/" + str(CalendarDayBellScheduleGroupBellScheduleID), verb = "delete")

	return(response)

def getCalendarDayCalendarEvent(CalendarDayCalendarEventID, EntityID = 1, returnCalendarDayID = False, returnCalendarEventID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayCalendarEvent/" + str(CalendarDayCalendarEventID), verb = "get", params_list = params_list)

	return(response)

def deleteCalendarDayCalendarEvent(CalendarDayCalendarEventID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayCalendarEvent/" + str(CalendarDayCalendarEventID), verb = "delete")

	return(response)

def getCalendarDayDisplayPeriodOverride(CalendarDayDisplayPeriodOverrideID, EntityID = 1, returnCalendarDayID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnLengthMinutes = False, returnModifiedTime = False, returnRemovePeriod = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayDisplayPeriodOverride/" + str(CalendarDayDisplayPeriodOverrideID), verb = "get", params_list = params_list)

	return(response)

def deleteCalendarDayDisplayPeriodOverride(CalendarDayDisplayPeriodOverrideID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayDisplayPeriodOverride/" + str(CalendarDayDisplayPeriodOverrideID), verb = "delete")

	return(response)

def getCalendarDaySchedulingPeriodTimesOverride(CalendarDaySchedulingPeriodTimesOverrideID, EntityID = 1, returnCalendarDayID = False, returnCreatedTime = False, returnDurationInMinutes = False, returnEndTime = False, returnModifiedTime = False, returnSchedulingPeriodID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDaySchedulingPeriodTimesOverride/" + str(CalendarDaySchedulingPeriodTimesOverrideID), verb = "get", params_list = params_list)

	return(response)

def deleteCalendarDaySchedulingPeriodTimesOverride(CalendarDaySchedulingPeriodTimesOverrideID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDaySchedulingPeriodTimesOverride/" + str(CalendarDaySchedulingPeriodTimesOverrideID), verb = "delete")

	return(response)

def getCalendarDisplayPeriod(CalendarDisplayPeriodID, EntityID = 1, returnCalendarDisplayPeriodIDClonedFrom = False, returnCalendarID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnIncludeInClassCounts = False, returnIncludeInTotalCounts = False, returnModifiedTime = False, returnTakeAttendance = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDisplayPeriod/" + str(CalendarDisplayPeriodID), verb = "get", params_list = params_list)

	return(response)

def deleteCalendarDisplayPeriod(CalendarDisplayPeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDisplayPeriod/" + str(CalendarDisplayPeriodID), verb = "delete")

	return(response)

def getCalendarEvent(CalendarEventID, EntityID = 1, returnCalendarEventIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiCalendarEventID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarEvent/" + str(CalendarEventID), verb = "get", params_list = params_list)

	return(response)

def deleteCalendarEvent(CalendarEventID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarEvent/" + str(CalendarEventID), verb = "delete")

	return(response)

def getCalendar(CalendarID, EntityID = 1, returnAttendanceCalculationMethod = False, returnAttendanceCalculationMethodCode = False, returnCalendarIDClonedFrom = False, returnCalendarIDClonedTo = False, returnCalendarMNID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDefaultDayLengthMinutes = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHalfDayHighPeriodCount = False, returnIsDefault = False, returnMCCCAcademicYearImportID = False, returnMCCCCalendarImportID = False, returnModifiedTime = False, returnNorthEastSemesterReportData = False, returnSchoolYearID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZeroDayHighPeriodCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/Calendar/" + str(CalendarID), verb = "get", params_list = params_list)

	return(response)

def deleteCalendar(CalendarID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/Calendar/" + str(CalendarID), verb = "delete")

	return(response)

def getConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, returnAttendanceReasonIDTardyDefault = False, returnAttendanceTypeIDTardyDefault = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnEnableInOutTime = False, returnEntityGroupKey = False, returnEntityID = False, returnIncludeGradeLevelOnLetter = False, returnIncludeParentNameAndOrPhoneNumberOnLetter = False, returnIncludeSchoolOrCampusOnLetter = False, returnIncludeSignatureLineForOfficeOnLetter = False, returnIncludeSignatureLineForParentOnLetter = False, returnIncludeSignatureLineForStudentOnLetter = False, returnIncludeStudentNameAndOrNumberOnLetter = False, returnIncludeTardyCountOnLetter = False, returnModifiedTime = False, returnMultiPeriodClassCountMethod = False, returnMultiPeriodClassCountMethodCode = False, returnPresentBackgroundColor = False, returnPresentBackgroundColorHex = False, returnPresentBackgroundColorRgba = False, returnRestrictTeacherAttendanceUpdates = False, returnSchoolYearID = False, returnSpecialClassCountsLabel = False, returnTardyDefaultComment = False, returnTardyKioskTardySlipTitle = False, returnTeacherEntryCutoffDuration = False, returnTeacherEntryCutOffNumberOfMinutesAfter = False, returnTeacherEntryCutOffTime = False, returnTeacherEntryCutOffTimeCode = False, returnTeacherEntryCutoffWindowEndTime = False, returnTeacherEntryCutoffWindowStartTime = False, returnTeacherEntrySpecificCutOffTime = False, returnUseInOutTimeForCalculations = False, returnUseMarkAllStudentsPresentOnTile = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSpecialClassCounts = False, returnUseTardyCalculator = False, returnUseTardyKiosk = False, returnUseTeacherPerfectAttendanceConfirmation = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "delete")

	return(response)

def getCrossEntityAttendanceReason(CrossEntityAttendanceReasonID, EntityID = 1, returnAttendanceReasonIDFrom = False, returnAttendanceReasonIDTo = False, returnCreatedTime = False, returnEntityIDTo = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceReason/" + str(CrossEntityAttendanceReasonID), verb = "get", params_list = params_list)

	return(response)

def deleteCrossEntityAttendanceReason(CrossEntityAttendanceReasonID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceReason/" + str(CrossEntityAttendanceReasonID), verb = "delete")

	return(response)

def getCrossEntityAttendanceType(CrossEntityAttendanceTypeID, EntityID = 1, returnAttendanceTypeIDFrom = False, returnAttendanceTypeIDTo = False, returnCreatedTime = False, returnEntityIDTo = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceType/" + str(CrossEntityAttendanceTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteCrossEntityAttendanceType(CrossEntityAttendanceTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceType/" + str(CrossEntityAttendanceTypeID), verb = "delete")

	return(response)

def getCrossEntityCalendarDisplayPeriod(CrossEntityCalendarDisplayPeriodID, EntityID = 1, returnCalendarDisplayPeriodIDFrom = False, returnCalendarDisplayPeriodIDTo = False, returnCreatedTime = False, returnIsAutoCreated = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityCalendarDisplayPeriod/" + str(CrossEntityCalendarDisplayPeriodID), verb = "get", params_list = params_list)

	return(response)

def deleteCrossEntityCalendarDisplayPeriod(CrossEntityCalendarDisplayPeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityCalendarDisplayPeriod/" + str(CrossEntityCalendarDisplayPeriodID), verb = "delete")

	return(response)

def getDailySectionAttendance(DailySectionAttendanceID, EntityID = 1, returnAttendancePeriodID = False, returnCalendarDayID = False, returnCreatedTime = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DailySectionAttendance/" + str(DailySectionAttendanceID), verb = "get", params_list = params_list)

	return(response)

def deleteDailySectionAttendance(DailySectionAttendanceID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DailySectionAttendance/" + str(DailySectionAttendanceID), verb = "delete")

	return(response)

def getDayRotationPattern(DayRotationPatternID, EntityID = 1, returnCreatedTime = False, returnDayNumber = False, returnDayRotationID = False, returnDayRotationPatternIDClonedFrom = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DayRotationPattern/" + str(DayRotationPatternID), verb = "get", params_list = params_list)

	return(response)

def deleteDayRotationPattern(DayRotationPatternID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DayRotationPattern/" + str(DayRotationPatternID), verb = "delete")

	return(response)

def getDisciplineThreshold(DisciplineThresholdID, EntityID = 1, returnActionID = False, returnAllowDisciplineOnCurrentDay = False, returnAttendanceLettersRan = False, returnAttendanceSlipComment = False, returnBuildingIDServing = False, returnCreateDisciplineRecord = False, returnCreatedTime = False, returnDisciplineSlipComment = False, returnDurationToServe = False, returnDurationToServePerDay = False, returnFooterComment = False, returnGenerateActionDetail = False, returnGreeting = False, returnIncidentDefaultComment = False, returnIncidentDescription = False, returnIsRepeatable = False, returnLocationIDServing = False, returnModifiedTime = False, returnOffenseID = False, returnRangeDisplay = False, returnRoomIDServing = False, returnServeOnFriday = False, returnServeOnMonday = False, returnServeOnSaturday = False, returnServeOnSunday = False, returnServeOnThursday = False, returnServeOnTuesday = False, returnServeOnWednesday = False, returnServingTime = False, returnStaffIDAuthorizedBy = False, returnThresholdRangeHigh = False, returnThresholdRangeLow = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DisciplineThreshold/" + str(DisciplineThresholdID), verb = "get", params_list = params_list)

	return(response)

def deleteDisciplineThreshold(DisciplineThresholdID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DisciplineThreshold/" + str(DisciplineThresholdID), verb = "delete")

	return(response)

def getDroppedStudentAttendancePeriod(DroppedStudentAttendancePeriodID, EntityID = 1, returnAttendancePeriodID = False, returnAttendanceReasonID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnComment = False, returnCreatedTime = False, returnIncidentOffenseNameActionDetailID = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DroppedStudentAttendancePeriod/" + str(DroppedStudentAttendancePeriodID), verb = "get", params_list = params_list)

	return(response)

def deleteDroppedStudentAttendancePeriod(DroppedStudentAttendancePeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DroppedStudentAttendancePeriod/" + str(DroppedStudentAttendancePeriodID), verb = "delete")

	return(response)

def getRecordedUnrecordedAttendance(MeetDisplayPeriodID, EntityID = 1, returnAttendanceTaken = False, returnCountAs = False, returnCreatedTime = False, returnDailySectionAttendanceID = False, returnDate = False, returnDayOfTheWeek = False, returnDisplayPeriodCode = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RecordedUnrecordedAttendance/" + str(MeetDisplayPeriodID), verb = "get", params_list = params_list)

	return(response)

def deleteRecordedUnrecordedAttendance(MeetDisplayPeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RecordedUnrecordedAttendance/" + str(MeetDisplayPeriodID), verb = "delete")

	return(response)

def getRoomLayout(RoomLayoutID, EntityID = 1, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoomID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayout/" + str(RoomLayoutID), verb = "get", params_list = params_list)

	return(response)

def deleteRoomLayout(RoomLayoutID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayout/" + str(RoomLayoutID), verb = "delete")

	return(response)

def getRoomLayoutObject(RoomLayoutObjectID, EntityID = 1, returnCreatedTime = False, returnModifiedTime = False, returnRoomLayoutID = False, returnRoomObjectID = False, returnRotation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXLocation = False, returnYLocation = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayoutObject/" + str(RoomLayoutObjectID), verb = "get", params_list = params_list)

	return(response)

def deleteRoomLayoutObject(RoomLayoutObjectID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayoutObject/" + str(RoomLayoutObjectID), verb = "delete")

	return(response)

def getRoomObject(RoomObjectID, EntityID = 1, returnCreatedTime = False, returnIsStudentSeat = False, returnLabel = False, returnModifiedTime = False, returnParameters = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomObject/" + str(RoomObjectID), verb = "get", params_list = params_list)

	return(response)

def deleteRoomObject(RoomObjectID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomObject/" + str(RoomObjectID), verb = "delete")

	return(response)

def getSeatingChart(SeatingChartID, EntityID = 1, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoomLayoutID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChart/" + str(SeatingChartID), verb = "get", params_list = params_list)

	return(response)

def deleteSeatingChart(SeatingChartID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChart/" + str(SeatingChartID), verb = "delete")

	return(response)

def getSeatingChartMeet(SeatingChartMeetID, EntityID = 1, returnCreatedTime = False, returnIsCurrent = False, returnMeetID = False, returnModifiedTime = False, returnSeatingChartID = False, returnSectionList = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartMeet/" + str(SeatingChartMeetID), verb = "get", params_list = params_list)

	return(response)

def deleteSeatingChartMeet(SeatingChartMeetID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartMeet/" + str(SeatingChartMeetID), verb = "delete")

	return(response)

def getSeatingChartSeat(SeatingChartSeatID, EntityID = 1, returnCreatedTime = False, returnModifiedTime = False, returnRoomLayoutObjectID = False, returnSeatingChartID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartSeat/" + str(SeatingChartSeatID), verb = "get", params_list = params_list)

	return(response)

def deleteSeatingChartSeat(SeatingChartSeatID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartSeat/" + str(SeatingChartSeatID), verb = "delete")

	return(response)

def getSeatingChartUsedLast(SeatingChartUsedLastID, EntityID = 1, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnRoomID = False, returnSeatingChartID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartUsedLast/" + str(SeatingChartUsedLastID), verb = "get", params_list = params_list)

	return(response)

def deleteSeatingChartUsedLast(SeatingChartUsedLastID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartUsedLast/" + str(SeatingChartUsedLastID), verb = "delete")

	return(response)

def getStaffMeetSetting(StaffMeetSettingID, EntityID = 1, returnCreatedTime = False, returnDisplayAttendanceTotalsOnDesktop = False, returnDisplayAttendanceTotalsOnMobile = False, returnDisplayHistoricalAttendanceOnDesktop = False, returnDisplayHistoricalAttendanceOnMobile = False, returnModifiedTime = False, returnStaffMeetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StaffMeetSetting/" + str(StaffMeetSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteStaffMeetSetting(StaffMeetSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StaffMeetSetting/" + str(StaffMeetSettingID), verb = "delete")

	return(response)

def getStudentAttendance(StudentAttendanceID, EntityID = 1, returnCalendarDayID = False, returnComment = False, returnCommentsExistForStudentAttendance = False, returnCreatedTime = False, returnDaysAbsent = False, returnDaysExcused = False, returnDaysOther = False, returnDaysUnexcused = False, returnEntityID = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnTardyCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendance/" + str(StudentAttendanceID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentAttendance(StudentAttendanceID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendance/" + str(StudentAttendanceID), verb = "delete")

	return(response)

def getStudentAttendancePeriod(StudentAttendancePeriodID, EntityID = 1, returnAttendancePeriodID = False, returnAttendanceReasonID = False, returnAttendanceTypeID = False, returnAttendanceTypeWithReason = False, returnComment = False, returnCreatedTime = False, returnCrossWalkedAttendanceTypeWithReason = False, returnEntityIDAttendancePeriod = False, returnEntityIDCourse = False, returnIncidentOffenseNameActionDetailID = False, returnModifiedTime = False, returnStudentAttendanceID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromAttendanceEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriod/" + str(StudentAttendancePeriodID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentAttendancePeriod(StudentAttendancePeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriod/" + str(StudentAttendancePeriodID), verb = "delete")

	return(response)

def getStudentAttendancePeriodGroup(StudentAttendancePeriodID, EntityID = 1, returnAttendancePeriodID = False, returnEntityID = False, returnSchoolYearID = False, returnStudentAttendanceID = False, returnStudentID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriodGroup/" + str(StudentAttendancePeriodID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentAttendancePeriodGroup(StudentAttendancePeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriodGroup/" + str(StudentAttendancePeriodID), verb = "delete")

	return(response)

def getStudentAttendanceTerm(StudentID, EntityID = 1, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnEndDate = False, returnEntityID = False, returnIsDefault = False, returnSchoolYearID = False, returnStartDate = False, returnTotalDaysAbsent = False, returnTotalDaysExcused = False, returnTotalDaysOther = False, returnTotalDaysUnexcused = False, returnTotalTardyCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceTerm/" + str(StudentID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentAttendanceTerm(StudentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceTerm/" + str(StudentID), verb = "delete")

	return(response)

def getStudentDisciplineThresholdAttendanceReportRunHistory(StudentDisciplineThresholdAttendanceReportRunHistoryID, EntityID = 1, returnAttendanceReportRunHistoryID = False, returnCreatedTime = False, returnDisciplineThresholdID = False, returnIsActive = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentDisciplineThresholdAttendanceReportRunHistory/" + str(StudentDisciplineThresholdAttendanceReportRunHistoryID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentDisciplineThresholdAttendanceReportRunHistory(StudentDisciplineThresholdAttendanceReportRunHistoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentDisciplineThresholdAttendanceReportRunHistory/" + str(StudentDisciplineThresholdAttendanceReportRunHistoryID), verb = "delete")

	return(response)

def getStudentInOutTime(StudentInOutTimeID, EntityID = 1, returnCreatedTime = False, returnMinutesPresent = False, returnModifiedTime = False, returnPeriodTimes = False, returnStudentAttendanceID = False, returnTimeIn = False, returnTimeOut = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentInOutTime/" + str(StudentInOutTimeID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentInOutTime(StudentInOutTimeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentInOutTime/" + str(StudentInOutTimeID), verb = "delete")

	return(response)

def getStudentThresholdPeriod(StudentThresholdPeriodID, EntityID = 1, returnAttendancePeriodID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCountsTowardsThreshold = False, returnCreatedTime = False, returnDate = False, returnModifiedTime = False, returnSectionID = False, returnStudentAttendancePeriodID = False, returnStudentDisciplineThresholdAttendanceReportRunHistoryID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentThresholdPeriod/" + str(StudentThresholdPeriodID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentThresholdPeriod(StudentThresholdPeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentThresholdPeriod/" + str(StudentThresholdPeriodID), verb = "delete")

	return(response)

def getTeacherEntry(TeacherEntryID, EntityID = 1, returnBackgroundColor = False, returnBackgroundColorHex = False, returnBackgroundColorRgba = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnLabel = False, returnModifiedTime = False, returnSchoolYearID = False, returnTeacherEntryIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TeacherEntry/" + str(TeacherEntryID), verb = "get", params_list = params_list)

	return(response)

def deleteTeacherEntry(TeacherEntryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TeacherEntry/" + str(TeacherEntryID), verb = "delete")

	return(response)

def getTempAffectedCalendarDayRecord(TempAffectedCalendarDayRecordID, EntityID = 1, returnAction = False, returnActionCode = False, returnAffectedPrimaryKey = False, returnCalendar = False, returnCalendarID = False, returnComment = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDayOfTheWeek = False, returnEntity = False, returnFailureReason = False, returnModifiedTime = False, returnNewBellSchedule = False, returnNewCountAs = False, returnNewDayRotation = False, returnNewDayRotationID = False, returnNewFundingPeriod = False, returnNewFundingPeriodID = False, returnNewInstructionalMinutesOverride = False, returnNewOperationalMinutesOverride = False, returnNewStateCalendarWaiverEventTypeCodeTX = False, returnNewStateCalendarWaiverEventTypeCodeTXID = False, returnNewStateSchoolDayEventCodeTX = False, returnNewStateSchoolDayEventCodeTXID = False, returnNewUseInstructionalMinutesOverride = False, returnNewUseOperationalMinutesOverride = False, returnNewWaiverMinutes = False, returnOldBellSchedule = False, returnOldDayRotation = False, returnOldDayRotationID = False, returnOldFundingPeriod = False, returnOldFundingPeriodID = False, returnOldInstructionalMinutesOverride = False, returnOldOperationalMinutesOverride = False, returnOldStateCalendarWaiverEventTypeCodeTX = False, returnOldStateCalendarWaiverEventTypeCodeTXID = False, returnOldStateSchoolDayEventCodeTX = False, returnOldStateSchoolDayEventCodeTXID = False, returnOldUseInstructionalMinutesOverride = False, returnOldUseOperationalMinutesOverride = False, returnOldWaiverMinutes = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedCalendarDayRecord/" + str(TempAffectedCalendarDayRecordID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAffectedCalendarDayRecord(TempAffectedCalendarDayRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedCalendarDayRecord/" + str(TempAffectedCalendarDayRecordID), verb = "delete")

	return(response)

def getTempAffectedStudentAttendancePeriodRecord(TempAffectedStudentAttendancePeriodRecordID, EntityID = 1, returnAction = False, returnActionCode = False, returnAffectedPrimaryKey = False, returnAttendanceCategory = False, returnAttendancePeriodID = False, returnAttendanceReasonCodeDescription = False, returnAttendanceReasonID = False, returnAttendanceTypeCodeDescription = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCECEAttendancePeriodID = False, returnCECEAttendanceReasonID = False, returnCECEAttendanceTypeID = False, returnComment = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnEntity = False, returnFailureReason = False, returnFullName = False, returnIsForCECEAttendancePeriod = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnNewStudentSectionCode = False, returnNewStudentSectionID = False, returnOldStudentSectionCode = False, returnOldStudentSectionID = False, returnPeriodCode = False, returnProcessFromCECEEntity = False, returnStudentAttendanceID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendancePeriodRecord/" + str(TempAffectedStudentAttendancePeriodRecordID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAffectedStudentAttendancePeriodRecord(TempAffectedStudentAttendancePeriodRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendancePeriodRecord/" + str(TempAffectedStudentAttendancePeriodRecordID), verb = "delete")

	return(response)

def getTempAffectedStudentAttendanceRecord(TempAffectedStudentAttendanceRecordID, EntityID = 1, returnAffectedPrimaryKey = False, returnCalendarDayID = False, returnComment = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnFailedStudentAttendancePeriods = False, returnFailureReason = False, returnFullName = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnNewDaysAbsent = False, returnNewDaysExcused = False, returnNewDaysOther = False, returnNewDaysUnexcused = False, returnNewGuardianNotified = False, returnNewStudentAttendancePeriods = False, returnNewTardyCount = False, returnOldDaysAbsent = False, returnOldDaysExcused = False, returnOldDaysOther = False, returnOldDaysUnexcused = False, returnOldStudentAttendancePeriods = False, returnOldTardyCount = False, returnPreviousGuardianNotified = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendanceRecord/" + str(TempAffectedStudentAttendanceRecordID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAffectedStudentAttendanceRecord(TempAffectedStudentAttendanceRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendanceRecord/" + str(TempAffectedStudentAttendanceRecordID), verb = "delete")

	return(response)

def getTempAttendanceTerm(TempAttendanceTermID, EntityID = 1, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnCalendarCode = False, returnCalendarID = False, returnCreatedTime = False, returnEndDate = False, returnIsUpdated = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAttendanceTerm/" + str(TempAttendanceTermID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAttendanceTerm(TempAttendanceTermID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAttendanceTerm/" + str(TempAttendanceTermID), verb = "delete")

	return(response)

def getTempCalendar(TempCalendarID, EntityID = 1, returnAffectedPrimaryKey = False, returnCalendarID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnOldEndDate = False, returnOldStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendar/" + str(TempCalendarID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCalendar(TempCalendarID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendar/" + str(TempCalendarID), verb = "delete")

	return(response)

def getTempCalendarAttendanceTerm(TempCalendarAttendanceTermID, EntityID = 1, returnAttendanceTermID = False, returnCalendarID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnStartDate = False, returnTableType = False, returnTableTypeCode = False, returnTableTypeString = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarAttendanceTerm/" + str(TempCalendarAttendanceTermID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCalendarAttendanceTerm(TempCalendarAttendanceTermID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarAttendanceTerm/" + str(TempCalendarAttendanceTermID), verb = "delete")

	return(response)

def getTempCalendarDayCalendarEventRecord(TempCalendarDayCalendarEventRecordID, EntityID = 1, returnCalendar = False, returnCalendarDayID = False, returnCalendarEvent = False, returnCalendarEventID = False, returnCreatedTime = False, returnDate = False, returnFailureReason = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarDayCalendarEventRecord/" + str(TempCalendarDayCalendarEventRecordID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCalendarDayCalendarEventRecord(TempCalendarDayCalendarEventRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarDayCalendarEventRecord/" + str(TempCalendarDayCalendarEventRecordID), verb = "delete")

	return(response)

def getTempCloneCalendarError(TempCloneCalendarErrorID, EntityID = 1, returnCreatedTime = False, returnDescription = False, returnEntityName = False, returnFailureReason = False, returnModifiedTime = False, returnRecordType = False, returnRecordTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarError/" + str(TempCloneCalendarErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCloneCalendarError(TempCloneCalendarErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarError/" + str(TempCloneCalendarErrorID), verb = "delete")

	return(response)

def getTempCloneCalendarRecord(TempCloneCalendarRecordID, EntityID = 1, returnAffectedPrimaryKey = False, returnAttendanceCalculationMethod = False, returnAttendanceCalculationMethodCode = False, returnCode = False, returnCreatedTime = False, returnDefaultDayLengthMinutes = False, returnDescription = False, returnEndDate = False, returnEntity = False, returnEntityID = False, returnHalfDayHighPeriodCount = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZeroDayHighPeriodCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarRecord/" + str(TempCloneCalendarRecordID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCloneCalendarRecord(TempCloneCalendarRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarRecord/" + str(TempCloneCalendarRecordID), verb = "delete")

	return(response)

def getTempStudentAttendanceRecord(TempStudentAttendanceRecordID, EntityID = 1, returnAffectedPrimaryKey = False, returnAttendanceTakenByPeriod = False, returnCreatedTime = False, returnDate = False, returnDayOfTheWeek = False, returnDayRotation = False, returnDayRotationID = False, returnGuardianNotified = False, returnModifiedTime = False, returnStudentName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentAttendanceRecord/" + str(TempStudentAttendanceRecordID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStudentAttendanceRecord(TempStudentAttendanceRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentAttendanceRecord/" + str(TempStudentAttendanceRecordID), verb = "delete")

	return(response)

def getTempStudentDisciplineThresholdAttendanceReportRunHistoryRecord(TempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID, EntityID = 1, returnCountType = False, returnCountTypeCode = False, returnCreatedTime = False, returnDateHigh = False, returnDateLow = False, returnDisciplineThresholdID = False, returnModifiedTime = False, returnResetRangeAttendanceTypes = False, returnStudentID = False, returnStudentName = False, returnThresholdValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentDisciplineThresholdAttendanceReportRunHistoryRecord/" + str(TempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStudentDisciplineThresholdAttendanceReportRunHistoryRecord(TempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentDisciplineThresholdAttendanceReportRunHistoryRecord/" + str(TempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID), verb = "delete")

	return(response)

def getTempStudentThresholdPeriodRecord(TempStudentThresholdPeriodRecordID, EntityID = 1, returnAttendancePeriodID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCreatedTime = False, returnDate = False, returnModifiedTime = False, returnSectionID = False, returnStudentAttendancePeriodID = False, returnStudentSectionID = False, returnTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentThresholdPeriodRecord/" + str(TempStudentThresholdPeriodRecordID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStudentThresholdPeriodRecord(TempStudentThresholdPeriodRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentThresholdPeriodRecord/" + str(TempStudentThresholdPeriodRecordID), verb = "delete")

	return(response)

def getThresholdResetRange(ThresholdResetRangeID, EntityID = 1, returnAttendanceLettersRan = False, returnCountType = False, returnCountTypeCode = False, returnCreatedTime = False, returnDateDisplay = False, returnDateHigh = False, returnDateLow = False, returnEntityID = False, returnIsForAttendanceLetters = False, returnModifiedTime = False, returnNumberPerDay = False, returnResetRangeAttendanceTypes = False, returnSchoolYearID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRange/" + str(ThresholdResetRangeID), verb = "get", params_list = params_list)

	return(response)

def deleteThresholdResetRange(ThresholdResetRangeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRange/" + str(ThresholdResetRangeID), verb = "delete")

	return(response)

def getThresholdResetRangeAttendancePeriod(ThresholdResetRangeAttendancePeriodID, EntityID = 1, returnAttendancePeriodID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendancePeriod/" + str(ThresholdResetRangeAttendancePeriodID), verb = "get", params_list = params_list)

	return(response)

def deleteThresholdResetRangeAttendancePeriod(ThresholdResetRangeAttendancePeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendancePeriod/" + str(ThresholdResetRangeAttendancePeriodID), verb = "delete")

	return(response)

def getThresholdResetRangeAttendanceType(ThresholdResetRangeAttendanceTypeID, EntityID = 1, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendanceType/" + str(ThresholdResetRangeAttendanceTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteThresholdResetRangeAttendanceType(ThresholdResetRangeAttendanceTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendanceType/" + str(ThresholdResetRangeAttendanceTypeID), verb = "delete")

	return(response)