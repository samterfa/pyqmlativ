# This module contains Attendance functions.

def deleteAttendancePeriod(AttendancePeriodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/AttendancePeriod/" + AttendancePeriodID, verb = "delete")

def deleteAttendancePeriodConfigEntityGroupYear(AttendancePeriodConfigEntityGroupYearID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/AttendancePeriodConfigEntityGroupYear/" + AttendancePeriodConfigEntityGroupYearID, verb = "delete")

def deleteAttendanceReason(AttendanceReasonID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/AttendanceReason/" + AttendanceReasonID, verb = "delete")

def deleteAttendanceReportRunHistory(AttendanceReportRunHistoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/AttendanceReportRunHistory/" + AttendanceReportRunHistoryID, verb = "delete")

def deleteAttendanceReportRunHistoryThresholdResetRange(AttendanceReportRunHistoryThresholdResetRangeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/AttendanceReportRunHistoryThresholdResetRange/" + AttendanceReportRunHistoryThresholdResetRangeID, verb = "delete")

def deleteAttendanceTerm(AttendanceTermID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/AttendanceTerm/" + AttendanceTermID, verb = "delete")

def deleteAttendanceType(AttendanceTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/AttendanceType/" + AttendanceTypeID, verb = "delete")

def deleteBellSchedule(BellScheduleID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/BellSchedule/" + BellScheduleID, verb = "delete")

def deleteBellSchedulingPeriod(BellSchedulingPeriodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/BellSchedulingPeriod/" + BellSchedulingPeriodID, verb = "delete")

def deleteCalendarDay(CalendarDayID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/CalendarDay/" + CalendarDayID, verb = "delete")

def deleteCalendarDayCalendarEvent(CalendarDayCalendarEventID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/CalendarDayCalendarEvent/" + CalendarDayCalendarEventID, verb = "delete")

def deleteCalendarDayDisplayPeriodOverride(CalendarDayDisplayPeriodOverrideID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/CalendarDayDisplayPeriodOverride/" + CalendarDayDisplayPeriodOverrideID, verb = "delete")

def deleteCalendarDaySchedulingPeriodTimesOverride(CalendarDaySchedulingPeriodTimesOverrideID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/CalendarDaySchedulingPeriodTimesOverride/" + CalendarDaySchedulingPeriodTimesOverrideID, verb = "delete")

def deleteCalendarDisplayPeriod(CalendarDisplayPeriodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/CalendarDisplayPeriod/" + CalendarDisplayPeriodID, verb = "delete")

def deleteCalendarEvent(CalendarEventID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/CalendarEvent/" + CalendarEventID, verb = "delete")

def deleteCalendar(CalendarID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/Calendar/" + CalendarID, verb = "delete")

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/ConfigEntityGroupYear/" + ConfigEntityGroupYearID, verb = "delete")

def deleteCrossEntityAttendanceReason(CrossEntityAttendanceReasonID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/CrossEntityAttendanceReason/" + CrossEntityAttendanceReasonID, verb = "delete")

def deleteCrossEntityAttendanceType(CrossEntityAttendanceTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/CrossEntityAttendanceType/" + CrossEntityAttendanceTypeID, verb = "delete")

def deleteCrossEntityCalendarDisplayPeriod(CrossEntityCalendarDisplayPeriodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/CrossEntityCalendarDisplayPeriod/" + CrossEntityCalendarDisplayPeriodID, verb = "delete")

def deleteDailySectionAttendance(DailySectionAttendanceID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/DailySectionAttendance/" + DailySectionAttendanceID, verb = "delete")

def deleteDayRotationPattern(DayRotationPatternID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/DayRotationPattern/" + DayRotationPatternID, verb = "delete")

def deleteDisciplineThreshold(DisciplineThresholdID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/DisciplineThreshold/" + DisciplineThresholdID, verb = "delete")

def deleteDroppedStudentAttendancePeriod(DroppedStudentAttendancePeriodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/DroppedStudentAttendancePeriod/" + DroppedStudentAttendancePeriodID, verb = "delete")

def deleteRecordedUnrecordedAttendance(MeetDisplayPeriodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/RecordedUnrecordedAttendance/" + MeetDisplayPeriodID, verb = "delete")

def deleteRoomLayout(RoomLayoutID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/RoomLayout/" + RoomLayoutID, verb = "delete")

def deleteRoomLayoutObject(RoomLayoutObjectID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/RoomLayoutObject/" + RoomLayoutObjectID, verb = "delete")

def deleteRoomObject(RoomObjectID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/RoomObject/" + RoomObjectID, verb = "delete")

def deleteSeatingChart(SeatingChartID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/SeatingChart/" + SeatingChartID, verb = "delete")

def deleteSeatingChartMeet(SeatingChartMeetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/SeatingChartMeet/" + SeatingChartMeetID, verb = "delete")

def deleteSeatingChartSeat(SeatingChartSeatID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/SeatingChartSeat/" + SeatingChartSeatID, verb = "delete")

def deleteSeatingChartUsedLast(SeatingChartUsedLastID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/SeatingChartUsedLast/" + SeatingChartUsedLastID, verb = "delete")

def deleteStaffMeetSetting(StaffMeetSettingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/StaffMeetSetting/" + StaffMeetSettingID, verb = "delete")

def deleteStudentAttendance(StudentAttendanceID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/StudentAttendance/" + StudentAttendanceID, verb = "delete")

def deleteStudentAttendancePeriod(StudentAttendancePeriodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/StudentAttendancePeriod/" + StudentAttendancePeriodID, verb = "delete")

def deleteStudentAttendancePeriodGroup(StudentAttendancePeriodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/StudentAttendancePeriodGroup/" + StudentAttendancePeriodID, verb = "delete")

def deleteStudentAttendanceTerm(StudentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/StudentAttendanceTerm/" + StudentID, verb = "delete")

def deleteStudentDisciplineThresholdAttendanceReportRunHistory(StudentDisciplineThresholdAttendanceReportRunHistoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/StudentDisciplineThresholdAttendanceReportRunHistory/" + StudentDisciplineThresholdAttendanceReportRunHistoryID, verb = "delete")

def deleteStudentInOutTime(StudentInOutTimeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/StudentInOutTime/" + StudentInOutTimeID, verb = "delete")

def deleteStudentThresholdPeriod(StudentThresholdPeriodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/StudentThresholdPeriod/" + StudentThresholdPeriodID, verb = "delete")

def deleteTeacherEntry(TeacherEntryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/TeacherEntry/" + TeacherEntryID, verb = "delete")

def deleteTempAffectedCalendarDayRecord(TempAffectedCalendarDayRecordID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/TempAffectedCalendarDayRecord/" + TempAffectedCalendarDayRecordID, verb = "delete")

def deleteTempAffectedStudentAttendancePeriodRecord(TempAffectedStudentAttendancePeriodRecordID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/TempAffectedStudentAttendancePeriodRecord/" + TempAffectedStudentAttendancePeriodRecordID, verb = "delete")

def deleteTempAffectedStudentAttendanceRecord(TempAffectedStudentAttendanceRecordID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/TempAffectedStudentAttendanceRecord/" + TempAffectedStudentAttendanceRecordID, verb = "delete")

def deleteTempAttendanceTerm(TempAttendanceTermID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/TempAttendanceTerm/" + TempAttendanceTermID, verb = "delete")

def deleteTempCalendar(TempCalendarID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/TempCalendar/" + TempCalendarID, verb = "delete")

def deleteTempCalendarAttendanceTerm(TempCalendarAttendanceTermID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/TempCalendarAttendanceTerm/" + TempCalendarAttendanceTermID, verb = "delete")

def deleteTempCalendarDayCalendarEventRecord(TempCalendarDayCalendarEventRecordID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/TempCalendarDayCalendarEventRecord/" + TempCalendarDayCalendarEventRecordID, verb = "delete")

def deleteTempCloneCalendarError(TempCloneCalendarErrorID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/TempCloneCalendarError/" + TempCloneCalendarErrorID, verb = "delete")

def deleteTempCloneCalendarRecord(TempCloneCalendarRecordID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/TempCloneCalendarRecord/" + TempCloneCalendarRecordID, verb = "delete")

def deleteTempStudentAttendanceRecord(TempStudentAttendanceRecordID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/TempStudentAttendanceRecord/" + TempStudentAttendanceRecordID, verb = "delete")

def deleteTempStudentDisciplineThresholdAttendanceReportRunHistoryRecord(TempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/TempStudentDisciplineThresholdAttendanceReportRunHistoryRecord/" + TempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID, verb = "delete")

def deleteTempStudentThresholdPeriodRecord(TempStudentThresholdPeriodRecordID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/TempStudentThresholdPeriodRecord/" + TempStudentThresholdPeriodRecordID, verb = "delete")

def deleteThresholdResetRange(ThresholdResetRangeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/ThresholdResetRange/" + ThresholdResetRangeID, verb = "delete")

def deleteThresholdResetRangeAttendancePeriod(ThresholdResetRangeAttendancePeriodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/ThresholdResetRangeAttendancePeriod/" + ThresholdResetRangeAttendancePeriodID, verb = "delete")

def deleteThresholdResetRangeAttendanceType(ThresholdResetRangeAttendanceTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Attendance/ThresholdResetRangeAttendanceType/" + ThresholdResetRangeAttendanceTypeID, verb = "delete")