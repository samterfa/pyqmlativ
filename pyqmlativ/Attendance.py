# This module contains Attendance functions.

def deleteAttendancePeriod(AttendancePeriodID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/AttendancePeriod/" + AttendancePeriodID, verb = "delete")

def deleteAttendancePeriodConfigEntityGroupYear(AttendancePeriodConfigEntityGroupYearID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/AttendancePeriodConfigEntityGroupYear/" + AttendancePeriodConfigEntityGroupYearID, verb = "delete")

def deleteAttendanceReason(AttendanceReasonID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/AttendanceReason/" + AttendanceReasonID, verb = "delete")

def deleteAttendanceReportRunHistory(AttendanceReportRunHistoryID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/AttendanceReportRunHistory/" + AttendanceReportRunHistoryID, verb = "delete")

def deleteAttendanceReportRunHistoryThresholdResetRange(AttendanceReportRunHistoryThresholdResetRangeID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/AttendanceReportRunHistoryThresholdResetRange/" + AttendanceReportRunHistoryThresholdResetRangeID, verb = "delete")

def deleteAttendanceTerm(AttendanceTermID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/AttendanceTerm/" + AttendanceTermID, verb = "delete")

def deleteAttendanceType(AttendanceTypeID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/AttendanceType/" + AttendanceTypeID, verb = "delete")

def deleteBellSchedule(BellScheduleID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/BellSchedule/" + BellScheduleID, verb = "delete")

def deleteBellSchedulingPeriod(BellSchedulingPeriodID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/BellSchedulingPeriod/" + BellSchedulingPeriodID, verb = "delete")

def deleteCalendarDay(CalendarDayID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/CalendarDay/" + CalendarDayID, verb = "delete")

def deleteCalendarDayCalendarEvent(CalendarDayCalendarEventID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/CalendarDayCalendarEvent/" + CalendarDayCalendarEventID, verb = "delete")

def deleteCalendarDayDisplayPeriodOverride(CalendarDayDisplayPeriodOverrideID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/CalendarDayDisplayPeriodOverride/" + CalendarDayDisplayPeriodOverrideID, verb = "delete")

def deleteCalendarDaySchedulingPeriodTimesOverride(CalendarDaySchedulingPeriodTimesOverrideID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/CalendarDaySchedulingPeriodTimesOverride/" + CalendarDaySchedulingPeriodTimesOverrideID, verb = "delete")

def deleteCalendarDisplayPeriod(CalendarDisplayPeriodID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/CalendarDisplayPeriod/" + CalendarDisplayPeriodID, verb = "delete")

def deleteCalendarEvent(CalendarEventID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/CalendarEvent/" + CalendarEventID, verb = "delete")

def deleteCalendar(CalendarID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/Calendar/" + CalendarID, verb = "delete")

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/ConfigEntityGroupYear/" + ConfigEntityGroupYearID, verb = "delete")

def deleteCrossEntityAttendanceReason(CrossEntityAttendanceReasonID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/CrossEntityAttendanceReason/" + CrossEntityAttendanceReasonID, verb = "delete")

def deleteCrossEntityAttendanceType(CrossEntityAttendanceTypeID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/CrossEntityAttendanceType/" + CrossEntityAttendanceTypeID, verb = "delete")

def deleteCrossEntityCalendarDisplayPeriod(CrossEntityCalendarDisplayPeriodID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/CrossEntityCalendarDisplayPeriod/" + CrossEntityCalendarDisplayPeriodID, verb = "delete")

def deleteDailySectionAttendance(DailySectionAttendanceID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/DailySectionAttendance/" + DailySectionAttendanceID, verb = "delete")

def deleteDayRotationPattern(DayRotationPatternID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/DayRotationPattern/" + DayRotationPatternID, verb = "delete")

def deleteDisciplineThreshold(DisciplineThresholdID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/DisciplineThreshold/" + DisciplineThresholdID, verb = "delete")

def deleteDroppedStudentAttendancePeriod(DroppedStudentAttendancePeriodID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/DroppedStudentAttendancePeriod/" + DroppedStudentAttendancePeriodID, verb = "delete")

def deleteRecordedUnrecordedAttendance(MeetDisplayPeriodID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/RecordedUnrecordedAttendance/" + MeetDisplayPeriodID, verb = "delete")

def deleteRoomLayout(RoomLayoutID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/RoomLayout/" + RoomLayoutID, verb = "delete")

def deleteRoomLayoutObject(RoomLayoutObjectID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/RoomLayoutObject/" + RoomLayoutObjectID, verb = "delete")

def deleteRoomObject(RoomObjectID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/RoomObject/" + RoomObjectID, verb = "delete")

def deleteSeatingChart(SeatingChartID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/SeatingChart/" + SeatingChartID, verb = "delete")

def deleteSeatingChartMeet(SeatingChartMeetID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/SeatingChartMeet/" + SeatingChartMeetID, verb = "delete")

def deleteSeatingChartSeat(SeatingChartSeatID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/SeatingChartSeat/" + SeatingChartSeatID, verb = "delete")

def deleteSeatingChartUsedLast(SeatingChartUsedLastID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/SeatingChartUsedLast/" + SeatingChartUsedLastID, verb = "delete")

def deleteStaffMeetSetting(StaffMeetSettingID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/StaffMeetSetting/" + StaffMeetSettingID, verb = "delete")

def deleteStudentAttendance(StudentAttendanceID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/StudentAttendance/" + StudentAttendanceID, verb = "delete")

def deleteStudentAttendancePeriod(StudentAttendancePeriodID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/StudentAttendancePeriod/" + StudentAttendancePeriodID, verb = "delete")

def deleteStudentAttendancePeriodGroup(StudentAttendancePeriodID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/StudentAttendancePeriodGroup/" + StudentAttendancePeriodID, verb = "delete")

def deleteStudentAttendanceTerm(StudentID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/StudentAttendanceTerm/" + StudentID, verb = "delete")

def deleteStudentDisciplineThresholdAttendanceReportRunHistory(StudentDisciplineThresholdAttendanceReportRunHistoryID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/StudentDisciplineThresholdAttendanceReportRunHistory/" + StudentDisciplineThresholdAttendanceReportRunHistoryID, verb = "delete")

def deleteStudentInOutTime(StudentInOutTimeID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/StudentInOutTime/" + StudentInOutTimeID, verb = "delete")

def deleteStudentThresholdPeriod(StudentThresholdPeriodID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/StudentThresholdPeriod/" + StudentThresholdPeriodID, verb = "delete")

def deleteTeacherEntry(TeacherEntryID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/TeacherEntry/" + TeacherEntryID, verb = "delete")

def deleteTempAffectedCalendarDayRecord(TempAffectedCalendarDayRecordID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/TempAffectedCalendarDayRecord/" + TempAffectedCalendarDayRecordID, verb = "delete")

def deleteTempAffectedStudentAttendancePeriodRecord(TempAffectedStudentAttendancePeriodRecordID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/TempAffectedStudentAttendancePeriodRecord/" + TempAffectedStudentAttendancePeriodRecordID, verb = "delete")

def deleteTempAffectedStudentAttendanceRecord(TempAffectedStudentAttendanceRecordID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/TempAffectedStudentAttendanceRecord/" + TempAffectedStudentAttendanceRecordID, verb = "delete")

def deleteTempAttendanceTerm(TempAttendanceTermID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/TempAttendanceTerm/" + TempAttendanceTermID, verb = "delete")

def deleteTempCalendar(TempCalendarID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/TempCalendar/" + TempCalendarID, verb = "delete")

def deleteTempCalendarAttendanceTerm(TempCalendarAttendanceTermID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/TempCalendarAttendanceTerm/" + TempCalendarAttendanceTermID, verb = "delete")

def deleteTempCalendarDayCalendarEventRecord(TempCalendarDayCalendarEventRecordID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/TempCalendarDayCalendarEventRecord/" + TempCalendarDayCalendarEventRecordID, verb = "delete")

def deleteTempCloneCalendarError(TempCloneCalendarErrorID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/TempCloneCalendarError/" + TempCloneCalendarErrorID, verb = "delete")

def deleteTempCloneCalendarRecord(TempCloneCalendarRecordID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/TempCloneCalendarRecord/" + TempCloneCalendarRecordID, verb = "delete")

def deleteTempStudentAttendanceRecord(TempStudentAttendanceRecordID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/TempStudentAttendanceRecord/" + TempStudentAttendanceRecordID, verb = "delete")

def deleteTempStudentDisciplineThresholdAttendanceReportRunHistoryRecord(TempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/TempStudentDisciplineThresholdAttendanceReportRunHistoryRecord/" + TempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID, verb = "delete")

def deleteTempStudentThresholdPeriodRecord(TempStudentThresholdPeriodRecordID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/TempStudentThresholdPeriodRecord/" + TempStudentThresholdPeriodRecordID, verb = "delete")

def deleteThresholdResetRange(ThresholdResetRangeID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/ThresholdResetRange/" + ThresholdResetRangeID, verb = "delete")

def deleteThresholdResetRangeAttendancePeriod(ThresholdResetRangeAttendancePeriodID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/ThresholdResetRangeAttendancePeriod/" + ThresholdResetRangeAttendancePeriodID, verb = "delete")

def deleteThresholdResetRangeAttendanceType(ThresholdResetRangeAttendanceTypeID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Attendance/ThresholdResetRangeAttendanceType/" + ThresholdResetRangeAttendanceTypeID, verb = "delete")