# This module contains Scheduling functions.

def deleteAvailabilityCourseFilter(AvailabilityCourseFilterID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/AvailabilityCourseFilter/" + AvailabilityCourseFilterID, verb = "delete")

def deleteAvailabilityFilterCourseStudent(AvailabilityFilterCourseStudentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/AvailabilityFilterCourseStudent/" + AvailabilityFilterCourseStudentID, verb = "delete")

def deleteAvailabilityFilterCourseStudentCourse(AvailabilityFilterCourseStudentCourseID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/AvailabilityFilterCourseStudentCourse/" + AvailabilityFilterCourseStudentCourseID, verb = "delete")

def deleteAvailabilityFilterCourseStudentStudent(AvailabilityFilterCourseStudentStudentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/AvailabilityFilterCourseStudentStudent/" + AvailabilityFilterCourseStudentStudentID, verb = "delete")

def deleteAvailabilityStudentFilter(AvailabilityStudentFilterID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/AvailabilityStudentFilter/" + AvailabilityStudentFilterID, verb = "delete")

def deleteBaseRunAnalysis(BaseRunAnalysisID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/BaseRunAnalysis/" + BaseRunAnalysisID, verb = "delete")

def deleteBlockPeriod(BlockPeriodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/BlockPeriod/" + BlockPeriodID, verb = "delete")

def deleteBlockPeriodDisplayPeriod(BlockPeriodDisplayPeriodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/BlockPeriodDisplayPeriod/" + BlockPeriodDisplayPeriodID, verb = "delete")

def deleteConfigEntityYear(ConfigEntityYearID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/ConfigEntityYear/" + ConfigEntityYearID, verb = "delete")

def deleteCourseAlternate(CourseAlternateID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/CourseAlternate/" + CourseAlternateID, verb = "delete")

def deleteCourseCorequisiteGroup(CourseCorequisiteGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/CourseCorequisiteGroup/" + CourseCorequisiteGroupID, verb = "delete")

def deleteCourseCorequisiteGroupCourse(CourseCorequisiteGroupCourseID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/CourseCorequisiteGroupCourse/" + CourseCorequisiteGroupCourseID, verb = "delete")

def deleteCourseCustomRequirement(CourseCustomRequirementID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/CourseCustomRequirement/" + CourseCustomRequirementID, verb = "delete")

def deleteCourseEntityOfferedTo(CourseEntityOfferedToID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/CourseEntityOfferedTo/" + CourseEntityOfferedToID, verb = "delete")

def deleteCourseEntityOfferedToSection(CourseEntityOfferedToSectionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/CourseEntityOfferedToSection/" + CourseEntityOfferedToSectionID, verb = "delete")

def deleteCourseEntityOfferedToSectionMeet(CourseEntityOfferedToSectionMeetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/CourseEntityOfferedToSectionMeet/" + CourseEntityOfferedToSectionMeetID, verb = "delete")

def deleteCourseEntityOfferedToSectionMeetDisplayPeriod(CourseEntityOfferedToSectionMeetDisplayPeriodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/CourseEntityOfferedToSectionMeetDisplayPeriod/" + CourseEntityOfferedToSectionMeetDisplayPeriodID, verb = "delete")

def deleteCourseEntityOfferedToSectionStaffMeet(CourseEntityOfferedToSectionStaffMeetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/CourseEntityOfferedToSectionStaffMeet/" + CourseEntityOfferedToSectionStaffMeetID, verb = "delete")

def deleteCourseGradeReference(CourseGradeReferenceID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/CourseGradeReference/" + CourseGradeReferenceID, verb = "delete")

def deleteCourseGroup(CourseGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/CourseGroup/" + CourseGroupID, verb = "delete")

def deleteCourseGroupCourse(CourseGroupCourseID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/CourseGroupCourse/" + CourseGroupCourseID, verb = "delete")

def deleteCourseLength(CourseLengthID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/CourseLength/" + CourseLengthID, verb = "delete")

def deleteCourseLevelMN(CourseLevelMNID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/CourseLevelMN/" + CourseLevelMNID, verb = "delete")

def deleteCourseMasterMassUpdate(CourseMasterMassUpdateID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/CourseMasterMassUpdate/" + CourseMasterMassUpdateID, verb = "delete")

def deleteCourse(CourseID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/Course/" + CourseID, verb = "delete")

def deleteCourseSectionLengthExclude(CourseSectionLengthExcludeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/CourseSectionLengthExclude/" + CourseSectionLengthExcludeID, verb = "delete")

def deleteCourseSubject(CourseSubjectID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/CourseSubject/" + CourseSubjectID, verb = "delete")

def deleteCourseType(CourseTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/CourseType/" + CourseTypeID, verb = "delete")

def deleteCustomRequirement(CustomRequirementID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/CustomRequirement/" + CustomRequirementID, verb = "delete")

def deleteDateRangePreset(DateRangePresetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/DateRangePreset/" + DateRangePresetID, verb = "delete")

def deleteDayRotation(DayRotationID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/DayRotation/" + DayRotationID, verb = "delete")

def deleteDisplayPeriod(DisplayPeriodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/DisplayPeriod/" + DisplayPeriodID, verb = "delete")

def deleteDisplayPeriodConflict(DisplayPeriodConflictID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/DisplayPeriodConflict/" + DisplayPeriodConflictID, verb = "delete")

def deleteDisplayPeriodRotation(DisplayPeriodRotationID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/DisplayPeriodRotation/" + DisplayPeriodRotationID, verb = "delete")

def deleteDisplayPeriodRotationDisplayPeriod(DisplayPeriodRotationDisplayPeriodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/DisplayPeriodRotationDisplayPeriod/" + DisplayPeriodRotationDisplayPeriodID, verb = "delete")

def deleteEarlyExitReason(EarlyExitReasonID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/EarlyExitReason/" + EarlyExitReasonID, verb = "delete")

def deleteMassPrintStudentScheduleRunHistory(MassPrintStudentScheduleRunHistoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/MassPrintStudentScheduleRunHistory/" + MassPrintStudentScheduleRunHistoryID, verb = "delete")

def deleteMaximumTeachingHourOverride(MaximumTeachingHourOverrideID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/MaximumTeachingHourOverride/" + MaximumTeachingHourOverrideID, verb = "delete")

def deleteMCCCTermGradeBucketMN(MCCCTermGradeBucketMNID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/MCCCTermGradeBucketMN/" + MCCCTermGradeBucketMNID, verb = "delete")

def deleteMeet(MeetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/Meet/" + MeetID, verb = "delete")

def deleteMeetDisplayPeriod(MeetDisplayPeriodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/MeetDisplayPeriod/" + MeetDisplayPeriodID, verb = "delete")

def deleteMeetRequirement(MeetRequirementID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/MeetRequirement/" + MeetRequirementID, verb = "delete")

def deleteMeetSummary(MeetSummaryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/MeetSummary/" + MeetSummaryID, verb = "delete")

def deleteMeetSummaryDetail(MeetSummaryDetailID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/MeetSummaryDetail/" + MeetSummaryDetailID, verb = "delete")

def deleteOpenPeriodAnalysis(OpenPeriodAnalysisID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/OpenPeriodAnalysis/" + OpenPeriodAnalysisID, verb = "delete")

def deleteOpenPeriodAnalysisStudent(OpenPeriodAnalysisStudentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/OpenPeriodAnalysisStudent/" + OpenPeriodAnalysisStudentID, verb = "delete")

def deleteProcessRestriction(ProcessRestrictionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/ProcessRestriction/" + ProcessRestrictionID, verb = "delete")

def deleteScheduleRestorePoint(ScheduleRestorePointID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/ScheduleRestorePoint/" + ScheduleRestorePointID, verb = "delete")

def deleteSchedulingBoardFilter(SchedulingBoardFilterID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SchedulingBoardFilter/" + SchedulingBoardFilterID, verb = "delete")

def deleteSchedulingCategory(SchedulingCategoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SchedulingCategory/" + SchedulingCategoryID, verb = "delete")

def deleteSchedulingGroup(SchedulingGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SchedulingGroup/" + SchedulingGroupID, verb = "delete")

def deleteSchedulingGroupCourse(SchedulingGroupCourseID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SchedulingGroupCourse/" + SchedulingGroupCourseID, verb = "delete")

def deleteSchedulingGroupSection(SchedulingGroupSectionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SchedulingGroupSection/" + SchedulingGroupSectionID, verb = "delete")

def deleteSchedulingPeriod(SchedulingPeriodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SchedulingPeriod/" + SchedulingPeriodID, verb = "delete")

def deleteSchedulingPeriodDisplayPeriod(SchedulingPeriodDisplayPeriodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SchedulingPeriodDisplayPeriod/" + SchedulingPeriodDisplayPeriodID, verb = "delete")

def deleteSchedulingTeam(SchedulingTeamID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SchedulingTeam/" + SchedulingTeamID, verb = "delete")

def deleteSchedulingTeamGradeReference(SchedulingTeamGradeReferenceID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SchedulingTeamGradeReference/" + SchedulingTeamGradeReferenceID, verb = "delete")

def deleteSectionCorequisiteGroup(SectionCorequisiteGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SectionCorequisiteGroup/" + SectionCorequisiteGroupID, verb = "delete")

def deleteSectionCorequisiteGroupSection(SectionCorequisiteGroupSectionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SectionCorequisiteGroupSection/" + SectionCorequisiteGroupSectionID, verb = "delete")

def deleteSectionCustomRequirement(SectionCustomRequirementID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SectionCustomRequirement/" + SectionCustomRequirementID, verb = "delete")

def deleteSectionDefault(SectionDefaultID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SectionDefault/" + SectionDefaultID, verb = "delete")

def deleteSectionEnrollmentTotalForSectionLengthSubset(SectionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SectionEnrollmentTotalForSectionLengthSubset/" + SectionID, verb = "delete")

def deleteSectionEnrollmentTotalForSectionLengthSubsetAndEntity(SectionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SectionEnrollmentTotalForSectionLengthSubsetAndEntity/" + SectionID, verb = "delete")

def deleteSectionLength(SectionLengthID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SectionLength/" + SectionLengthID, verb = "delete")

def deleteSectionLengthSubset(SectionLengthSubsetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SectionLengthSubset/" + SectionLengthSubsetID, verb = "delete")

def deleteSectionMeetSummary(SectionMeetSummaryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SectionMeetSummary/" + SectionMeetSummaryID, verb = "delete")

def deleteSection(SectionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/Section/" + SectionID, verb = "delete")

def deleteSectionSchedulerCourseConstraint(SectionSchedulerCourseConstraintID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SectionSchedulerCourseConstraint/" + SectionSchedulerCourseConstraintID, verb = "delete")

def deleteSectionSchedulerDayRotationForMeet(SectionSchedulerDayRotationForMeetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SectionSchedulerDayRotationForMeet/" + SectionSchedulerDayRotationForMeetID, verb = "delete")

def deleteSectionSchedulerDisplayPeriodExcludedForCourse(SectionSchedulerDisplayPeriodExcludedForCourseID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SectionSchedulerDisplayPeriodExcludedForCourse/" + SectionSchedulerDisplayPeriodExcludedForCourseID, verb = "delete")

def deleteSectionSchedulerPattern(SectionSchedulerPatternID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SectionSchedulerPattern/" + SectionSchedulerPatternID, verb = "delete")

def deleteSectionSchedulerPatternDayRotation(SectionSchedulerPatternDayRotationID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SectionSchedulerPatternDayRotation/" + SectionSchedulerPatternDayRotationID, verb = "delete")

def deleteSectionSchedulerPatternExcludedForMeetRequirement(SectionSchedulerPatternExcludedForMeetRequirementID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SectionSchedulerPatternExcludedForMeetRequirement/" + SectionSchedulerPatternExcludedForMeetRequirementID, verb = "delete")

def deleteSectionSchedulerProposedMeet(SectionSchedulerProposedMeetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SectionSchedulerProposedMeet/" + SectionSchedulerProposedMeetID, verb = "delete")

def deleteSectionSchedulerProposedMeetConflict(SectionSchedulerProposedMeetConflictID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SectionSchedulerProposedMeetConflict/" + SectionSchedulerProposedMeetConflictID, verb = "delete")

def deleteSectionSchedulerProposedMeetDisplayPeriod(SectionSchedulerProposedMeetDisplayPeriodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SectionSchedulerProposedMeetDisplayPeriod/" + SectionSchedulerProposedMeetDisplayPeriodID, verb = "delete")

def deleteSectionSchedulerProposedStaffMeet(SectionSchedulerProposedStaffMeetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SectionSchedulerProposedStaffMeet/" + SectionSchedulerProposedStaffMeetID, verb = "delete")

def deleteSectionSchedulerRoomTypeForCourse(SectionSchedulerRoomTypeForCourseID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SectionSchedulerRoomTypeForCourse/" + SectionSchedulerRoomTypeForCourseID, verb = "delete")

def deleteSectionSchedulerRunAnalysis(SectionSchedulerRunAnalysisID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SectionSchedulerRunAnalysis/" + SectionSchedulerRunAnalysisID, verb = "delete")

def deleteSectionSchedulerStaffForCourse(SectionSchedulerStaffForCourseID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SectionSchedulerStaffForCourse/" + SectionSchedulerStaffForCourseID, verb = "delete")

def deleteSectionSchedulingCategory(SectionSchedulingCategoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SectionSchedulingCategory/" + SectionSchedulingCategoryID, verb = "delete")

def deleteSectionSchedulingTeam(SectionSchedulingTeamID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/SectionSchedulingTeam/" + SectionSchedulingTeamID, verb = "delete")

def deleteStaffMeet(StaffMeetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/StaffMeet/" + StaffMeetID, verb = "delete")

def deleteStaffStudent(StudentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/StaffStudent/" + StudentID, verb = "delete")

def deleteStudentAutoSchedulerCourse(StudentAutoSchedulerCourseID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/StudentAutoSchedulerCourse/" + StudentAutoSchedulerCourseID, verb = "delete")

def deleteStudentAutoSchedulerProposedStudentCourseRequest(StudentAutoSchedulerProposedStudentCourseRequestID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/StudentAutoSchedulerProposedStudentCourseRequest/" + StudentAutoSchedulerProposedStudentCourseRequestID, verb = "delete")

def deleteStudentAutoSchedulerProposedStudentSection(StudentAutoSchedulerProposedStudentSectionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/StudentAutoSchedulerProposedStudentSection/" + StudentAutoSchedulerProposedStudentSectionID, verb = "delete")

def deleteStudentAutoSchedulerProposedStudentSectionTransaction(StudentAutoSchedulerProposedStudentSectionTransactionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/StudentAutoSchedulerProposedStudentSectionTransaction/" + StudentAutoSchedulerProposedStudentSectionTransactionID, verb = "delete")

def deleteStudentAutoSchedulerRunAnalysis(StudentAutoSchedulerRunAnalysisID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/StudentAutoSchedulerRunAnalysis/" + StudentAutoSchedulerRunAnalysisID, verb = "delete")

def deleteStudentAutoSchedulerRunAnalysisException(StudentAutoSchedulerRunAnalysisExceptionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/StudentAutoSchedulerRunAnalysisException/" + StudentAutoSchedulerRunAnalysisExceptionID, verb = "delete")

def deleteStudentAutoSchedulerRunAnalysisTotal(StudentAutoSchedulerRunAnalysisTotalID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/StudentAutoSchedulerRunAnalysisTotal/" + StudentAutoSchedulerRunAnalysisTotalID, verb = "delete")

def deleteStudentAutoSchedulerSection(StudentAutoSchedulerSectionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/StudentAutoSchedulerSection/" + StudentAutoSchedulerSectionID, verb = "delete")

def deleteStudentAutoSchedulerStudent(StudentAutoSchedulerStudentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/StudentAutoSchedulerStudent/" + StudentAutoSchedulerStudentID, verb = "delete")

def deleteStudentAutoSchedulerStudentCourseRequest(StudentAutoSchedulerStudentCourseRequestID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/StudentAutoSchedulerStudentCourseRequest/" + StudentAutoSchedulerStudentCourseRequestID, verb = "delete")

def deleteStudentAutoSchedulerStudentCourseRequestSection(StudentAutoSchedulerStudentCourseRequestSectionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/StudentAutoSchedulerStudentCourseRequestSection/" + StudentAutoSchedulerStudentCourseRequestSectionID, verb = "delete")

def deleteStudentAutoSchedulerStudentCourseRequestSectionDetail(StudentAutoSchedulerStudentCourseRequestSectionDetailID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/StudentAutoSchedulerStudentCourseRequestSectionDetail/" + StudentAutoSchedulerStudentCourseRequestSectionDetailID, verb = "delete")

def deleteStudentCourseRequest(StudentCourseRequestID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/StudentCourseRequest/" + StudentCourseRequestID, verb = "delete")

def deleteStudentCourseRequestSectionLengthSubset(StudentCourseRequestSectionLengthSubsetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/StudentCourseRequestSectionLengthSubset/" + StudentCourseRequestSectionLengthSubsetID, verb = "delete")

def deleteStudentEntityYearSchedulingCategory(StudentEntityYearSchedulingCategoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/StudentEntityYearSchedulingCategory/" + StudentEntityYearSchedulingCategoryID, verb = "delete")

def deleteStudentSection(StudentSectionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/StudentSection/" + StudentSectionID, verb = "delete")

def deleteStudentSectionTransaction(StudentSectionTransactionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/StudentSectionTransaction/" + StudentSectionTransactionID, verb = "delete")

def deleteStudyHallSchedulerRunAnalysis(StudyHallSchedulerRunAnalysisID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/StudyHallSchedulerRunAnalysis/" + StudyHallSchedulerRunAnalysisID, verb = "delete")

def deleteTempCourse(TempCourseID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempCourse/" + TempCourseID, verb = "delete")

def deleteTempCourseEntityOfferedToSection(TempCourseEntityOfferedToSectionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempCourseEntityOfferedToSection/" + TempCourseEntityOfferedToSectionID, verb = "delete")

def deleteTempCourseMasterMassUpdateError(TempCourseMasterMassUpdateErrorID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempCourseMasterMassUpdateError/" + TempCourseMasterMassUpdateErrorID, verb = "delete")

def deleteTempCourseMasterMassUpdateErrorDetail(TempCourseMasterMassUpdateErrorDetailID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempCourseMasterMassUpdateErrorDetail/" + TempCourseMasterMassUpdateErrorDetailID, verb = "delete")

def deleteTempCourseMasterMassUpdateField(TempCourseMasterMassUpdateFieldID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempCourseMasterMassUpdateField/" + TempCourseMasterMassUpdateFieldID, verb = "delete")

def deleteTempDayRotation(TempDayRotationID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempDayRotation/" + TempDayRotationID, verb = "delete")

def deleteTempException(TempExceptionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempException/" + TempExceptionID, verb = "delete")

def deleteTempFailedCourse(TempFailedCourseID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempFailedCourse/" + TempFailedCourseID, verb = "delete")

def deleteTempFailedDayRotation(TempFailedDayRotationID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempFailedDayRotation/" + TempFailedDayRotationID, verb = "delete")

def deleteTempFailedSection(TempFailedSectionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempFailedSection/" + TempFailedSectionID, verb = "delete")

def deleteTempFailedSectionLengthSubset(TempFailedSectionLengthSubsetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempFailedSectionLengthSubset/" + TempFailedSectionLengthSubsetID, verb = "delete")

def deleteTempFailedStudentCourseRequest(TempFailedStudentCourseRequestID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempFailedStudentCourseRequest/" + TempFailedStudentCourseRequestID, verb = "delete")

def deleteTempFailedStudentCourseRequestToReactivate(TempFailedStudentCourseRequestToReactivateID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempFailedStudentCourseRequestToReactivate/" + TempFailedStudentCourseRequestToReactivateID, verb = "delete")

def deleteTempFailedStudentCourseRequestToReactivateDetail(TempFailedStudentCourseRequestToReactivateDetailID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempFailedStudentCourseRequestToReactivateDetail/" + TempFailedStudentCourseRequestToReactivateDetailID, verb = "delete")

def deleteTempFailedStudentSection(TempFailedStudentSectionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempFailedStudentSection/" + TempFailedStudentSectionID, verb = "delete")

def deleteTempFailedStudentSectionTransaction(TempFailedStudentSectionTransactionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempFailedStudentSectionTransaction/" + TempFailedStudentSectionTransactionID, verb = "delete")

def deleteTempMeet(TempMeetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempMeet/" + TempMeetID, verb = "delete")

def deleteTempSchedulingTeamGradeReference(TempSchedulingTeamGradeReferenceID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempSchedulingTeamGradeReference/" + TempSchedulingTeamGradeReferenceID, verb = "delete")

def deleteTempSection(TempSectionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempSection/" + TempSectionID, verb = "delete")

def deleteTempSectionLength(TempSectionLengthID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempSectionLength/" + TempSectionLengthID, verb = "delete")

def deleteTempSectionLengthSubset(TempSectionLengthSubsetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempSectionLengthSubset/" + TempSectionLengthSubsetID, verb = "delete")

def deleteTempStaffMeet(TempStaffMeetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempStaffMeet/" + TempStaffMeetID, verb = "delete")

def deleteTempStudent(TempStudentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempStudent/" + TempStudentID, verb = "delete")

def deleteTempStudentCourseRequest(TempStudentCourseRequestID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempStudentCourseRequest/" + TempStudentCourseRequestID, verb = "delete")

def deleteTempStudentCourseRequestSectionLengthSubset(TempStudentCourseRequestSectionLengthSubsetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempStudentCourseRequestSectionLengthSubset/" + TempStudentCourseRequestSectionLengthSubsetID, verb = "delete")

def deleteTempStudentCourseRequestToReactivateMN(TempStudentCourseRequestToReactivateMNID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempStudentCourseRequestToReactivateMN/" + TempStudentCourseRequestToReactivateMNID, verb = "delete")

def deleteTempStudentCourseRequestToReactivateNonState(TempStudentCourseRequestToReactivateNonStateID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempStudentCourseRequestToReactivateNonState/" + TempStudentCourseRequestToReactivateNonStateID, verb = "delete")

def deleteTempStudentSchedulingCategory(TempStudentSchedulingCategoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempStudentSchedulingCategory/" + TempStudentSchedulingCategoryID, verb = "delete")

def deleteTempStudentSchedulingTeam(TempStudentSchedulingTeamID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempStudentSchedulingTeam/" + TempStudentSchedulingTeamID, verb = "delete")

def deleteTempStudentSection(TempStudentSectionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempStudentSection/" + TempStudentSectionID, verb = "delete")

def deleteTempStudentSectionTransaction(TempStudentSectionTransactionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempStudentSectionTransaction/" + TempStudentSectionTransactionID, verb = "delete")

def deleteTempSubstituteAssignment(TempSubstituteAssignmentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Scheduling/TempSubstituteAssignment/" + TempSubstituteAssignmentID, verb = "delete")