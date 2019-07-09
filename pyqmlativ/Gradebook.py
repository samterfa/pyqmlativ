# This module contains Gradebook functions.

def deleteAcademicStandardGradingScaleGroup(AcademicStandardGradingScaleGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/AcademicStandardGradingScaleGroup/" + AcademicStandardGradingScaleGroupID, verb = "delete")

def deleteAcademicStandardGradingScaleGroupAcademicStandard(AcademicStandardGradingScaleGroupAcademicStandardID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/AcademicStandardGradingScaleGroupAcademicStandard/" + AcademicStandardGradingScaleGroupAcademicStandardID, verb = "delete")

def deleteAssessment(AssessmentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/Assessment/" + AssessmentID, verb = "delete")

def deleteAssignment(AssignmentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/Assignment/" + AssignmentID, verb = "delete")

def deleteAssignmentAttachment(AssignmentAttachmentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/AssignmentAttachment/" + AssignmentAttachmentID, verb = "delete")

def deleteAssignmentQuestion(AssignmentQuestionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/AssignmentQuestion/" + AssignmentQuestionID, verb = "delete")

def deleteCalculationGroup(CalculationGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/CalculationGroup/" + CalculationGroupID, verb = "delete")

def deleteCalculationGroupAcademicStandard(CalculationGroupAcademicStandardID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/CalculationGroupAcademicStandard/" + CalculationGroupAcademicStandardID, verb = "delete")

def deleteCalculationGroupAcademicStandardCalculationGroupHierarchyDepth(CalculationGroupAcademicStandardCalculationGroupHierarchyDepthID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/CalculationGroupAcademicStandardCalculationGroupHierarchyDepth/" + CalculationGroupAcademicStandardCalculationGroupHierarchyDepthID, verb = "delete")

def deleteCalculationGroupAcademicStandardGradeBucket(CalculationGroupAcademicStandardGradeBucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/CalculationGroupAcademicStandardGradeBucket/" + CalculationGroupAcademicStandardGradeBucketID, verb = "delete")

def deleteCalculationGroupAcademicStandardWeighting(CalculationGroupAcademicStandardWeightingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/CalculationGroupAcademicStandardWeighting/" + CalculationGroupAcademicStandardWeightingID, verb = "delete")

def deleteCalculationGroupCategory(CalculationGroupCategoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/CalculationGroupCategory/" + CalculationGroupCategoryID, verb = "delete")

def deleteCalculationGroupCourse(CalculationGroupCourseID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/CalculationGroupCourse/" + CalculationGroupCourseID, verb = "delete")

def deleteCalculationGroupGradeBucket(CalculationGroupGradeBucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/CalculationGroupGradeBucket/" + CalculationGroupGradeBucketID, verb = "delete")

def deleteCalculationGroupHierarchyDepth(CalculationGroupHierarchyDepthID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/CalculationGroupHierarchyDepth/" + CalculationGroupHierarchyDepthID, verb = "delete")

def deleteCalculationGroupSubject(CalculationGroupSubjectID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/CalculationGroupSubject/" + CalculationGroupSubjectID, verb = "delete")

def deleteCalculationGroupSubjectAcademicStandard(CalculationGroupSubjectAcademicStandardID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/CalculationGroupSubjectAcademicStandard/" + CalculationGroupSubjectAcademicStandardID, verb = "delete")

def deleteCalculationGroupSubjectGradeBucket(CalculationGroupSubjectGradeBucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/CalculationGroupSubjectGradeBucket/" + CalculationGroupSubjectGradeBucketID, verb = "delete")

def deleteCalculationGroupSubjectWeighting(CalculationGroupSubjectWeightingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/CalculationGroupSubjectWeighting/" + CalculationGroupSubjectWeightingID, verb = "delete")

def deleteCalculationGroupWeighting(CalculationGroupWeightingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/CalculationGroupWeighting/" + CalculationGroupWeightingID, verb = "delete")

def deleteCategory(CategoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/Category/" + CategoryID, verb = "delete")

def deleteCategoryGradeBucketType(CategoryGradeBucketTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/CategoryGradeBucketType/" + CategoryGradeBucketTypeID, verb = "delete")

def deleteClassGroup(ClassGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/ClassGroup/" + ClassGroupID, verb = "delete")

def deleteClassGroupSection(ClassGroupSectionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/ClassGroupSection/" + ClassGroupSectionID, verb = "delete")

def deleteClosedGradingPeriodGradeChange(ClosedGradingPeriodGradeChangeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/ClosedGradingPeriodGradeChange/" + ClosedGradingPeriodGradeChangeID, verb = "delete")

def deleteClosedGradingPeriodStudentGradeBucketChange(ClosedGradingPeriodStudentGradeBucketChangeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/ClosedGradingPeriodStudentGradeBucketChange/" + ClosedGradingPeriodStudentGradeBucketChangeID, verb = "delete")

def deleteConfigDistrict(ConfigDistrictID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/ConfigDistrict/" + ConfigDistrictID, verb = "delete")

def deleteConfigDistrictYear(ConfigDistrictYearID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/ConfigDistrictYear/" + ConfigDistrictYearID, verb = "delete")

def deleteConfigEntity(ConfigEntityID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/ConfigEntity/" + ConfigEntityID, verb = "delete")

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/ConfigEntityGroupYear/" + ConfigEntityGroupYearID, verb = "delete")

def deleteCourseGradingScaleGroup(CourseGradingScaleGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/CourseGradingScaleGroup/" + CourseGradingScaleGroupID, verb = "delete")

def deleteCourseGradingScaleGroupCourse(CourseGradingScaleGroupCourseID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/CourseGradingScaleGroupCourse/" + CourseGradingScaleGroupCourseID, verb = "delete")

def deleteDropLowScoreRun(DropLowScoreRunID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/DropLowScoreRun/" + DropLowScoreRunID, verb = "delete")

def deleteDropLowScoreRunStudentAssignment(DropLowScoreRunStudentAssignmentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/DropLowScoreRunStudentAssignment/" + DropLowScoreRunStudentAssignmentID, verb = "delete")

def deleteGradesheetAssignmentSetting(GradesheetAssignmentSettingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/GradesheetAssignmentSetting/" + GradesheetAssignmentSettingID, verb = "delete")

def deleteGradingScaleGroup(GradingScaleGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/GradingScaleGroup/" + GradingScaleGroupID, verb = "delete")

def deleteGradingScaleGroupGradeMark(GradingScaleGroupGradeMarkID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/GradingScaleGroupGradeMark/" + GradingScaleGroupGradeMarkID, verb = "delete")

def deleteMonitorSummaryByClass(MonitorSummaryByClassID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/MonitorSummaryByClass/" + MonitorSummaryByClassID, verb = "delete")

def deleteMonitorSummaryByTeacher(MonitorSummaryByTeacherID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/MonitorSummaryByTeacher/" + MonitorSummaryByTeacherID, verb = "delete")

def deleteQuestion(QuestionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/Question/" + QuestionID, verb = "delete")

def deleteQuestionAnswer(QuestionAnswerID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/QuestionAnswer/" + QuestionAnswerID, verb = "delete")

def deleteQuestionAnswerMedia(QuestionAnswerMediaID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/QuestionAnswerMedia/" + QuestionAnswerMediaID, verb = "delete")

def deleteQuestionMedia(QuestionMediaID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/QuestionMedia/" + QuestionMediaID, verb = "delete")

def deleteScoreClarifier(ScoreClarifierID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/ScoreClarifier/" + ScoreClarifierID, verb = "delete")

def deleteSectionAcademicStandardWeight(SectionAcademicStandardWeightID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/SectionAcademicStandardWeight/" + SectionAcademicStandardWeightID, verb = "delete")

def deleteSectionCategory(SectionCategoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/SectionCategory/" + SectionCategoryID, verb = "delete")

def deleteSectionGradeBucket(SectionGradeBucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/SectionGradeBucket/" + SectionGradeBucketID, verb = "delete")

def deleteSectionGradeBucketSetting(SectionGradeBucketSettingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/SectionGradeBucketSetting/" + SectionGradeBucketSettingID, verb = "delete")

def deleteSectionGradeBucketWeight(SectionGradeBucketWeightID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/SectionGradeBucketWeight/" + SectionGradeBucketWeightID, verb = "delete")

def deleteSectionGradingPeriodData(SectionGradingPeriodDataID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/SectionGradingPeriodData/" + SectionGradingPeriodDataID, verb = "delete")

def deleteSectionGradingScaleGroup(SectionGradingScaleGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/SectionGradingScaleGroup/" + SectionGradingScaleGroupID, verb = "delete")

def deleteSectionSubjectWeight(SectionSubjectWeightID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/SectionSubjectWeight/" + SectionSubjectWeightID, verb = "delete")

def deleteStudentAnswer(StudentAnswerID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/StudentAnswer/" + StudentAnswerID, verb = "delete")

def deleteStudentAssignment(StudentAssignmentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/StudentAssignment/" + StudentAssignmentID, verb = "delete")

def deleteStudentAssignmentAttempt(StudentAssignmentAttemptID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/StudentAssignmentAttempt/" + StudentAssignmentAttemptID, verb = "delete")

def deleteStudentGradeBucketAcademicStandard(StudentGradeBucketAcademicStandardID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/StudentGradeBucketAcademicStandard/" + StudentGradeBucketAcademicStandardID, verb = "delete")

def deleteStudentGradeBucketSubject(StudentGradeBucketSubjectID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/StudentGradeBucketSubject/" + StudentGradeBucketSubjectID, verb = "delete")

def deleteStudentGradingScaleGroup(StudentGradingScaleGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/StudentGradingScaleGroup/" + StudentGradingScaleGroupID, verb = "delete")

def deleteStudentGradingScaleGroupStudentSection(StudentGradingScaleGroupStudentSectionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/StudentGradingScaleGroupStudentSection/" + StudentGradingScaleGroupStudentSectionID, verb = "delete")

def deleteStudentGroup(StudentGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/StudentGroup/" + StudentGroupID, verb = "delete")

def deleteStudentGroupAssignment(StudentGroupAssignmentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/StudentGroupAssignment/" + StudentGroupAssignmentID, verb = "delete")

def deleteStudentGroupStudentSection(StudentGroupStudentSectionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/StudentGroupStudentSection/" + StudentGroupStudentSectionID, verb = "delete")

def deleteStudentGroupTeacherSectionSetting(StudentGroupTeacherSectionSettingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/StudentGroupTeacherSectionSetting/" + StudentGroupTeacherSectionSettingID, verb = "delete")

def deleteStudentQuestion(StudentQuestionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/StudentQuestion/" + StudentQuestionID, verb = "delete")

def deleteStudentSectionGradingScaleGradeBucket(StudentSectionGradingScaleGradeBucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/StudentSectionGradingScaleGradeBucket/" + StudentSectionGradingScaleGradeBucketID, verb = "delete")

def deleteStudentSectionNote(StudentSectionNoteID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/StudentSectionNote/" + StudentSectionNoteID, verb = "delete")

def deleteSubjectGradingScaleGroup(SubjectGradingScaleGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/SubjectGradingScaleGroup/" + SubjectGradingScaleGroupID, verb = "delete")

def deleteSubjectGradingScaleGroupSubject(SubjectGradingScaleGroupSubjectID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/SubjectGradingScaleGroupSubject/" + SubjectGradingScaleGroupSubjectID, verb = "delete")

def deleteTeacherSectionAcademicStandardGradeBucketSetting(TeacherSectionAcademicStandardGradeBucketSettingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TeacherSectionAcademicStandardGradeBucketSetting/" + TeacherSectionAcademicStandardGradeBucketSettingID, verb = "delete")

def deleteTeacherSectionCategoryAnalyticsSetting(TeacherSectionCategoryAnalyticsSettingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TeacherSectionCategoryAnalyticsSetting/" + TeacherSectionCategoryAnalyticsSettingID, verb = "delete")

def deleteTeacherSectionGradeBucketAnalyticsSetting(TeacherSectionGradeBucketAnalyticsSettingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TeacherSectionGradeBucketAnalyticsSetting/" + TeacherSectionGradeBucketAnalyticsSettingID, verb = "delete")

def deleteTeacherSectionGradeBucketSetting(TeacherSectionGradeBucketSettingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TeacherSectionGradeBucketSetting/" + TeacherSectionGradeBucketSettingID, verb = "delete")

def deleteTeacherSectionGradingPeriodSetting(TeacherSectionGradingPeriodSettingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TeacherSectionGradingPeriodSetting/" + TeacherSectionGradingPeriodSettingID, verb = "delete")

def deleteTeacherSectionSetting(TeacherSectionSettingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TeacherSectionSetting/" + TeacherSectionSettingID, verb = "delete")

def deleteTeacherSectionStandardsDisplayAcademicStandardSetting(TeacherSectionStandardsDisplayAcademicStandardSettingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TeacherSectionStandardsDisplayAcademicStandardSetting/" + TeacherSectionStandardsDisplayAcademicStandardSettingID, verb = "delete")

def deleteTeacherSectionStandardsDisplayGradeBucketSetting(TeacherSectionStandardsDisplayGradeBucketSettingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TeacherSectionStandardsDisplayGradeBucketSetting/" + TeacherSectionStandardsDisplayGradeBucketSettingID, verb = "delete")

def deleteTeacherSectionStudentSectionSetting(TeacherSectionStudentSectionSettingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TeacherSectionStudentSectionSetting/" + TeacherSectionStudentSectionSettingID, verb = "delete")

def deleteTeacherSectionSubjectGradeBucketSetting(TeacherSectionSubjectGradeBucketSettingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TeacherSectionSubjectGradeBucketSetting/" + TeacherSectionSubjectGradeBucketSettingID, verb = "delete")

def deleteTempAdjustedCategory(TempAdjustedCategoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempAdjustedCategory/" + TempAdjustedCategoryID, verb = "delete")

def deleteTempAssignmentError(TempAssignmentErrorID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempAssignmentError/" + TempAssignmentErrorID, verb = "delete")

def deleteTempCalcGroupBucketRemoveStandardOrSubjectResult(TempCalcGroupBucketRemoveStandardOrSubjectResultID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempCalcGroupBucketRemoveStandardOrSubjectResult/" + TempCalcGroupBucketRemoveStandardOrSubjectResultID, verb = "delete")

def deleteTempCalculationGroupAcademicStandardWeighting(TempCalculationGroupAcademicStandardWeightingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempCalculationGroupAcademicStandardWeighting/" + TempCalculationGroupAcademicStandardWeightingID, verb = "delete")

def deleteTempCalculationGroupSubjectWeighting(TempCalculationGroupSubjectWeightingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempCalculationGroupSubjectWeighting/" + TempCalculationGroupSubjectWeightingID, verb = "delete")

def deleteTempCalculationGroupWeighting(TempCalculationGroupWeightingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempCalculationGroupWeighting/" + TempCalculationGroupWeightingID, verb = "delete")

def deleteTempCloneGradebookSection(TempCloneGradebookSectionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempCloneGradebookSection/" + TempCloneGradebookSectionID, verb = "delete")

def deleteTempCourseMoveCourse(TempCourseMoveCourseID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempCourseMoveCourse/" + TempCourseMoveCourseID, verb = "delete")

def deleteTempCourseMoveError(TempCourseMoveErrorID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempCourseMoveError/" + TempCourseMoveErrorID, verb = "delete")

def deleteTempCourseMoveSectionError(TempCourseMoveSectionErrorID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempCourseMoveSectionError/" + TempCourseMoveSectionErrorID, verb = "delete")

def deleteTempDropLowScoreStudentAssignment(TempDropLowScoreStudentAssignmentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempDropLowScoreStudentAssignment/" + TempDropLowScoreStudentAssignmentID, verb = "delete")

def deleteTempGradebookCloneError(TempGradebookCloneErrorID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempGradebookCloneError/" + TempGradebookCloneErrorID, verb = "delete")

def deleteTempGradebookGroupError(TempGradebookGroupErrorID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempGradebookGroupError/" + TempGradebookGroupErrorID, verb = "delete")

def deleteTempGradeMarkError(TempGradeMarkErrorID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempGradeMarkError/" + TempGradeMarkErrorID, verb = "delete")

def deleteTempGradingPeriodGradeBucket(TempGradingPeriodGradeBucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempGradingPeriodGradeBucket/" + TempGradingPeriodGradeBucketID, verb = "delete")

def deleteTempGradingPeriodGradeBucketError(TempGradingPeriodGradeBucketErrorID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempGradingPeriodGradeBucketError/" + TempGradingPeriodGradeBucketErrorID, verb = "delete")

def deleteTempSectionAssignment(TempSectionAssignmentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempSectionAssignment/" + TempSectionAssignmentID, verb = "delete")

def deleteTempSectionCategory(TempSectionCategoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempSectionCategory/" + TempSectionCategoryID, verb = "delete")

def deleteTempSectionGradeBucket(TempSectionGradeBucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempSectionGradeBucket/" + TempSectionGradeBucketID, verb = "delete")

def deleteTempSectionGradeBucketWeight(TempSectionGradeBucketWeightID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempSectionGradeBucketWeight/" + TempSectionGradeBucketWeightID, verb = "delete")

def deleteTempSectionGradingScale(TempSectionGradingScaleID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempSectionGradingScale/" + TempSectionGradingScaleID, verb = "delete")

def deleteTempSectionGradingScaleGroupToCreate(TempSectionGradingScaleGroupToCreateID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempSectionGradingScaleGroupToCreate/" + TempSectionGradingScaleGroupToCreateID, verb = "delete")

def deleteTempStudentAssignment(TempStudentAssignmentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempStudentAssignment/" + TempStudentAssignmentID, verb = "delete")

def deleteTempStudentGradingScaleGroupStudentSection(TempStudentGradingScaleGroupStudentSectionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempStudentGradingScaleGroupStudentSection/" + TempStudentGradingScaleGroupStudentSectionID, verb = "delete")

def deleteTempUnDropLowScoreStudentSection(TempUnDropLowScoreStudentSectionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/TempUnDropLowScoreStudentSection/" + TempUnDropLowScoreStudentSectionID, verb = "delete")

def deleteVendorAssignment(VendorAssignmentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/VendorAssignment/" + VendorAssignmentID, verb = "delete")

def deleteVendorCategory(VendorCategoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/VendorCategory/" + VendorCategoryID, verb = "delete")

def deleteVendorStudentAssignment(VendorStudentAssignmentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Gradebook/VendorStudentAssignment/" + VendorStudentAssignmentID, verb = "delete")