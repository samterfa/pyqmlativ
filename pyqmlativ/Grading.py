# This module contains Grading functions.

def deleteCommentBucket(CommentBucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/CommentBucket/" + CommentBucketID, verb = "delete")

def deleteCommentBucketCourse(CommentBucketCourseID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/CommentBucketCourse/" + CommentBucketCourseID, verb = "delete")

def deleteCommentCode(CommentCodeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/CommentCode/" + CommentCodeID, verb = "delete")

def deleteCommentSet(CommentSetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/CommentSet/" + CommentSetID, verb = "delete")

def deleteConfigDistrictGroup(ConfigDistrictGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/ConfigDistrictGroup/" + ConfigDistrictGroupID, verb = "delete")

def deleteConfigDistrictYear(ConfigDistrictYearID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/ConfigDistrictYear/" + ConfigDistrictYearID, verb = "delete")

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/ConfigEntityGroupYear/" + ConfigEntityGroupYearID, verb = "delete")

def deleteConfigEntityYear(ConfigEntityYearID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/ConfigEntityYear/" + ConfigEntityYearID, verb = "delete")

def deleteCourseGPAMethod(CourseGPAMethodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/CourseGPAMethod/" + CourseGPAMethodID, verb = "delete")

def deleteCourseGPAMethodGradeReferenceOverride(CourseGPAMethodGradeReferenceOverrideID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/CourseGPAMethodGradeReferenceOverride/" + CourseGPAMethodGradeReferenceOverrideID, verb = "delete")

def deleteEarnedCreditsBucketGroup(EarnedCreditsBucketGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/EarnedCreditsBucketGroup/" + EarnedCreditsBucketGroupID, verb = "delete")

def deleteEarnedCreditsBucketGroupGradeBucket(EarnedCreditsBucketGroupGradeBucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/EarnedCreditsBucketGroupGradeBucket/" + EarnedCreditsBucketGroupGradeBucketID, verb = "delete")

def deleteEarnedCreditsBucketGroupGradeBucketStudentOverride(EarnedCreditsBucketGroupGradeBucketStudentOverrideID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/EarnedCreditsBucketGroupGradeBucketStudentOverride/" + EarnedCreditsBucketGroupGradeBucketStudentOverrideID, verb = "delete")

def deleteFactorBasedAddOn(FactorBasedAddOnID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/FactorBasedAddOn/" + FactorBasedAddOnID, verb = "delete")

def deleteGPABucket(GPABucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GPABucket/" + GPABucketID, verb = "delete")

def deleteGPABucketEntity(GPABucketEntityID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GPABucketEntity/" + GPABucketEntityID, verb = "delete")

def deleteGPABucketGroup(GPABucketGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GPABucketGroup/" + GPABucketGroupID, verb = "delete")

def deleteGPABucketGroupGradeBucket(GPABucketGroupGradeBucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GPABucketGroupGradeBucket/" + GPABucketGroupGradeBucketID, verb = "delete")

def deleteGPABucketGroupGradeBucketStudentOverride(GPABucketGroupGradeBucketStudentOverrideID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GPABucketGroupGradeBucketStudentOverride/" + GPABucketGroupGradeBucketStudentOverrideID, verb = "delete")

def deleteGPABucketGroupSummary(GPABucketGroupSummaryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GPABucketGroupSummary/" + GPABucketGroupSummaryID, verb = "delete")

def deleteGPABucketSet(GPABucketSetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GPABucketSet/" + GPABucketSetID, verb = "delete")

def deleteGPABucketType(GPABucketTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GPABucketType/" + GPABucketTypeID, verb = "delete")

def deleteGPAMethod(GPAMethodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GPAMethod/" + GPAMethodID, verb = "delete")

def deleteGPAMethodCourseGroup(GPAMethodCourseGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GPAMethodCourseGroup/" + GPAMethodCourseGroupID, verb = "delete")

def deleteGPAMethodEntity(GPAMethodEntityID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GPAMethodEntity/" + GPAMethodEntityID, verb = "delete")

def deleteGPAMethodGradeBucketFlagGPAPointsOverride(GPAMethodGradeBucketFlagGPAPointsOverrideID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GPAMethodGradeBucketFlagGPAPointsOverride/" + GPAMethodGradeBucketFlagGPAPointsOverrideID, verb = "delete")

def deleteGradebookLockGradeBucket(GradebookLockGradeBucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradebookLockGradeBucket/" + GradebookLockGradeBucketID, verb = "delete")

def deleteGradebookLockGradeReference(GradebookLockGradeReferenceID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradebookLockGradeReference/" + GradebookLockGradeReferenceID, verb = "delete")

def deleteGradeBucket(GradeBucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeBucket/" + GradeBucketID, verb = "delete")

def deleteGradeBucketFlag(GradeBucketFlagID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeBucketFlag/" + GradeBucketFlagID, verb = "delete")

def deleteGradeBucketFlagDetail(GradeBucketFlagDetailID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeBucketFlagDetail/" + GradeBucketFlagDetailID, verb = "delete")

def deleteGradeBucketFlagDetailGPAMethod(GradeBucketFlagDetailGPAMethodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeBucketFlagDetailGPAMethod/" + GradeBucketFlagDetailGPAMethodID, verb = "delete")

def deleteGradeBucketType(GradeBucketTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeBucketType/" + GradeBucketTypeID, verb = "delete")

def deleteGradeMark(GradeMarkID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeMark/" + GradeMarkID, verb = "delete")

def deleteGradeMarkPointSet(GradeMarkPointSetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeMarkPointSet/" + GradeMarkPointSetID, verb = "delete")

def deleteGradeReportAcademicSession(GradeReportAcademicSessionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportAcademicSession/" + GradeReportAcademicSessionID, verb = "delete")

def deleteGradeReportAcademicSessionTemplate(GradeReportAcademicSessionTemplateID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportAcademicSessionTemplate/" + GradeReportAcademicSessionTemplateID, verb = "delete")

def deleteGradeReportAcademicSessionTemplateCourse(GradeReportAcademicSessionTemplateCourseID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportAcademicSessionTemplateCourse/" + GradeReportAcademicSessionTemplateCourseID, verb = "delete")

def deleteGradeReportAcademicSessionTemplateCourseGroup(GradeReportAcademicSessionTemplateCourseGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportAcademicSessionTemplateCourseGroup/" + GradeReportAcademicSessionTemplateCourseGroupID, verb = "delete")

def deleteGradeReportAcademicSessionTemplateGradeLevel(GradeReportAcademicSessionTemplateGradeLevelID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportAcademicSessionTemplateGradeLevel/" + GradeReportAcademicSessionTemplateGradeLevelID, verb = "delete")

def deleteGradeReportAcademicSessionTemplateGroup(GradeReportAcademicSessionTemplateGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportAcademicSessionTemplateGroup/" + GradeReportAcademicSessionTemplateGroupID, verb = "delete")

def deleteGradeReportColumnAttendanceCategory(GradeReportColumnAttendanceCategoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportColumnAttendanceCategory/" + GradeReportColumnAttendanceCategoryID, verb = "delete")

def deleteGradeReportColumnAttendanceTerm(GradeReportColumnAttendanceTermID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportColumnAttendanceTerm/" + GradeReportColumnAttendanceTermID, verb = "delete")

def deleteGradeReportColumnGradeBucket(GradeReportColumnGradeBucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportColumnGradeBucket/" + GradeReportColumnGradeBucketID, verb = "delete")

def deleteGradeReportColumnGroup(GradeReportColumnGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportColumnGroup/" + GradeReportColumnGroupID, verb = "delete")

def deleteGradeReportColumnGroupColumn(GradeReportColumnGroupColumnID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportColumnGroupColumn/" + GradeReportColumnGroupColumnID, verb = "delete")

def deleteGradeReportEndorsementRow(GradeReportEndorsementRowID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportEndorsementRow/" + GradeReportEndorsementRowID, verb = "delete")

def deleteGradeReportGPARow(GradeReportGPARowID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportGPARow/" + GradeReportGPARowID, verb = "delete")

def deleteGradeReportGradingScale(GradeReportGradingScaleID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportGradingScale/" + GradeReportGradingScaleID, verb = "delete")

def deleteGradeReportRow(GradeReportRowID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportRow/" + GradeReportRowID, verb = "delete")

def deleteGradeReportRowColumn(GradeReportRowColumnID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportRowColumn/" + GradeReportRowColumnID, verb = "delete")

def deleteGradeReportRowDetail(GradeReportRowDetailID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportRowDetail/" + GradeReportRowDetailID, verb = "delete")

def deleteGradeReportRunHistory(GradeReportRunHistoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportRunHistory/" + GradeReportRunHistoryID, verb = "delete")

def deleteGradeReportRunHistoryAttachment(GradeReportRunHistoryAttachmentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportRunHistoryAttachment/" + GradeReportRunHistoryAttachmentID, verb = "delete")

def deleteGradeReportStudent(GradeReportStudentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportStudent/" + GradeReportStudentID, verb = "delete")

def deleteGradeReportStudentAttendanceTerm(GradeReportStudentAttendanceTermID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportStudentAttendanceTerm/" + GradeReportStudentAttendanceTermID, verb = "delete")

def deleteGradeReportStudentTestRow(GradeReportStudentTestRowID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportStudentTestRow/" + GradeReportStudentTestRowID, verb = "delete")

def deleteGradeReportStudentTestType(GradeReportStudentTestTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportStudentTestType/" + GradeReportStudentTestTypeID, verb = "delete")

def deleteGradeReportTemplate(GradeReportTemplateID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportTemplate/" + GradeReportTemplateID, verb = "delete")

def deleteGradeReportTemplateCommentSet(GradeReportTemplateCommentSetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportTemplateCommentSet/" + GradeReportTemplateCommentSetID, verb = "delete")

def deleteGradeReportTemplateEndorsement(GradeReportTemplateEndorsementID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportTemplateEndorsement/" + GradeReportTemplateEndorsementID, verb = "delete")

def deleteGradeReportTemplateGPABucket(GradeReportTemplateGPABucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportTemplateGPABucket/" + GradeReportTemplateGPABucketID, verb = "delete")

def deleteGradeReportTemplateGPAMethod(GradeReportTemplateGPAMethodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportTemplateGPAMethod/" + GradeReportTemplateGPAMethodID, verb = "delete")

def deleteGradeReportTemplateGradeMark(GradeReportTemplateGradeMarkID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportTemplateGradeMark/" + GradeReportTemplateGradeMarkID, verb = "delete")

def deleteGradeReportTemplateHeaderColumn(GradeReportTemplateHeaderColumnID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportTemplateHeaderColumn/" + GradeReportTemplateHeaderColumnID, verb = "delete")

def deleteGradeReportTemplateHeaderRow(GradeReportTemplateHeaderRowID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportTemplateHeaderRow/" + GradeReportTemplateHeaderRowID, verb = "delete")

def deleteGradeReportTemplateTestType(GradeReportTemplateTestTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradeReportTemplateTestType/" + GradeReportTemplateTestTypeID, verb = "delete")

def deleteGradingPeriod(GradingPeriodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradingPeriod/" + GradingPeriodID, verb = "delete")

def deleteGradingPeriodGradeBucket(GradingPeriodGradeBucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradingPeriodGradeBucket/" + GradingPeriodGradeBucketID, verb = "delete")

def deleteGradingPeriodSet(GradingPeriodSetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradingPeriodSet/" + GradingPeriodSetID, verb = "delete")

def deleteGradReqRankGPACourseType(GradReqRankGPACourseTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradReqRankGPACourseType/" + GradReqRankGPACourseTypeID, verb = "delete")

def deleteGradReqRankGPAMethodEntity(GradReqRankGPAMethodEntityID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradReqRankGPAMethodEntity/" + GradReqRankGPAMethodEntityID, verb = "delete")

def deleteGradReqRankHighSchoolGradeLevel(GradReqRankHighSchoolGradeLevelID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradReqRankHighSchoolGradeLevel/" + GradReqRankHighSchoolGradeLevelID, verb = "delete")

def deleteGradReqRankSchoolYearIncludeLocalCredit(GradReqRankSchoolYearIncludeLocalCreditID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradReqRankSchoolYearIncludeLocalCredit/" + GradReqRankSchoolYearIncludeLocalCreditID, verb = "delete")

def deleteGradReqSubjectType(GradReqSubjectTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/GradReqSubjectType/" + GradReqSubjectTypeID, verb = "delete")

def deleteHonorRollRuleGPA(HonorRollRuleGPAID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/HonorRollRuleGPA/" + HonorRollRuleGPAID, verb = "delete")

def deleteHonorRollRuleGradeMark(HonorRollRuleGradeMarkID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/HonorRollRuleGradeMark/" + HonorRollRuleGradeMarkID, verb = "delete")

def deleteHonorRollRuleGradeMarkGradeBucket(HonorRollRuleGradeMarkGradeBucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/HonorRollRuleGradeMarkGradeBucket/" + HonorRollRuleGradeMarkGradeBucketID, verb = "delete")

def deleteHonorRollRuleGradeMarkGradeMark(HonorRollRuleGradeMarkGradeMarkID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/HonorRollRuleGradeMarkGradeMark/" + HonorRollRuleGradeMarkGradeMarkID, verb = "delete")

def deleteHonorRollRulePriorHonorRoll(HonorRollRulePriorHonorRollID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/HonorRollRulePriorHonorRoll/" + HonorRollRulePriorHonorRollID, verb = "delete")

def deleteHonorRollRulePriorHonorRollLevel(HonorRollRulePriorHonorRollLevelID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/HonorRollRulePriorHonorRollLevel/" + HonorRollRulePriorHonorRollLevelID, verb = "delete")

def deleteHonorRollRun(HonorRollRunID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/HonorRollRun/" + HonorRollRunID, verb = "delete")

def deleteHonorRollRunHistory(HonorRollRunHistoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/HonorRollRunHistory/" + HonorRollRunHistoryID, verb = "delete")

def deleteHonorRollRunLevel(HonorRollRunLevelID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/HonorRollRunLevel/" + HonorRollRunLevelID, verb = "delete")

def deleteHonorRollRunLevelHistory(HonorRollRunLevelHistoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/HonorRollRunLevelHistory/" + HonorRollRunLevelHistoryID, verb = "delete")

def deleteHonorRollRunLevelRule(HonorRollRunLevelRuleID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/HonorRollRunLevelRule/" + HonorRollRunLevelRuleID, verb = "delete")

def deletePointSet(PointSetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/PointSet/" + PointSetID, verb = "delete")

def deletePointSetEntity(PointSetEntityID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/PointSetEntity/" + PointSetEntityID, verb = "delete")

def deleteQueuedGPACalculation(QueuedGPACalculationID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/QueuedGPACalculation/" + QueuedGPACalculationID, verb = "delete")

def deleteRankMethod(RankMethodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/RankMethod/" + RankMethodID, verb = "delete")

def deleteRankMethodStudentRangeSetup(RankMethodStudentRangeSetupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/RankMethodStudentRangeSetup/" + RankMethodStudentRangeSetupID, verb = "delete")

def deleteRankRunHistory(RankRunHistoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/RankRunHistory/" + RankRunHistoryID, verb = "delete")

def deleteSectionLengthGPABucket(SectionLengthGPABucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/SectionLengthGPABucket/" + SectionLengthGPABucketID, verb = "delete")

def deleteStudentCommentBucket(StudentCommentBucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/StudentCommentBucket/" + StudentCommentBucketID, verb = "delete")

def deleteStudentFreeFormCommentBucket(StudentFreeFormCommentBucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/StudentFreeFormCommentBucket/" + StudentFreeFormCommentBucketID, verb = "delete")

def deleteStudentGPABucket(StudentGPABucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/StudentGPABucket/" + StudentGPABucketID, verb = "delete")

def deleteStudentGPABucketGroup(StudentGPABucketGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/StudentGPABucketGroup/" + StudentGPABucketGroupID, verb = "delete")

def deleteStudentGradeBucket(StudentGradeBucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/StudentGradeBucket/" + StudentGradeBucketID, verb = "delete")

def deleteStudentGradeBucketFlag(StudentGradeBucketFlagID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/StudentGradeBucketFlag/" + StudentGradeBucketFlagID, verb = "delete")

def deleteStudentHonorRollRunLevel(StudentHonorRollRunLevelID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/StudentHonorRollRunLevel/" + StudentHonorRollRunLevelID, verb = "delete")

def deleteStudentRange(StudentRangeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/StudentRange/" + StudentRangeID, verb = "delete")

def deleteStudentRank(StudentRankID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/StudentRank/" + StudentRankID, verb = "delete")

def deleteStudentSectionGPABucketGroup(StudentSectionGPABucketGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/StudentSectionGPABucketGroup/" + StudentSectionGPABucketGroupID, verb = "delete")

def deleteStudentSectionGPAMethod(StudentSectionGPAMethodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/StudentSectionGPAMethod/" + StudentSectionGPAMethodID, verb = "delete")

def deleteTempFactorBasedAddOn(TempFactorBasedAddOnID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempFactorBasedAddOn/" + TempFactorBasedAddOnID, verb = "delete")

def deleteTempFailedGradingPeriod(TempFailedGradingPeriodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempFailedGradingPeriod/" + TempFailedGradingPeriodID, verb = "delete")

def deleteTempGradeBucketFlagDetailGPAMethod(TempGradeBucketFlagDetailGPAMethodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempGradeBucketFlagDetailGPAMethod/" + TempGradeBucketFlagDetailGPAMethodID, verb = "delete")

def deleteTempGradeMarkPointSetError(TempGradeMarkPointSetErrorID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempGradeMarkPointSetError/" + TempGradeMarkPointSetErrorID, verb = "delete")

def deleteTempGradeReportAttendanceTerm(TempGradeReportAttendanceTermID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempGradeReportAttendanceTerm/" + TempGradeReportAttendanceTermID, verb = "delete")

def deleteTempGradeReportGradeBucket(TempGradeReportGradeBucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempGradeReportGradeBucket/" + TempGradeReportGradeBucketID, verb = "delete")

def deleteTempGradeReportTemplate(TempGradeReportTemplateID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempGradeReportTemplate/" + TempGradeReportTemplateID, verb = "delete")

def deleteTempGradeReportTemplateError(TempGradeReportTemplateErrorID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempGradeReportTemplateError/" + TempGradeReportTemplateErrorID, verb = "delete")

def deleteTempGradingPeriod(TempGradingPeriodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempGradingPeriod/" + TempGradingPeriodID, verb = "delete")

def deleteTempGradingPeriodError(TempGradingPeriodErrorID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempGradingPeriodError/" + TempGradingPeriodErrorID, verb = "delete")

def deleteTempGradingPeriodUpdateProcessError(TempGradingPeriodUpdateProcessErrorID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempGradingPeriodUpdateProcessError/" + TempGradingPeriodUpdateProcessErrorID, verb = "delete")

def deleteTempGradingUtilityError(TempGradingUtilityErrorID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempGradingUtilityError/" + TempGradingUtilityErrorID, verb = "delete")

def deleteTempHonorRollGradeMarkMethodRange(TempHonorRollGradeMarkMethodRangeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempHonorRollGradeMarkMethodRange/" + TempHonorRollGradeMarkMethodRangeID, verb = "delete")

def deleteTempHonorRollGradeMarkMethodRangeCourseGroup(TempHonorRollGradeMarkMethodRangeCourseGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempHonorRollGradeMarkMethodRangeCourseGroup/" + TempHonorRollGradeMarkMethodRangeCourseGroupID, verb = "delete")

def deleteTempHonorRollGradeMarkMethodRangeGradeMark(TempHonorRollGradeMarkMethodRangeGradeMarkID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempHonorRollGradeMarkMethodRangeGradeMark/" + TempHonorRollGradeMarkMethodRangeGradeMarkID, verb = "delete")

def deleteTempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucket(TempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucket/" + TempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID, verb = "delete")

def deleteTempHonorRollMethodRange(TempHonorRollMethodRangeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempHonorRollMethodRange/" + TempHonorRollMethodRangeID, verb = "delete")

def deleteTempMassChangeSystemDatesError(TempMassChangeSystemDatesErrorID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempMassChangeSystemDatesError/" + TempMassChangeSystemDatesErrorID, verb = "delete")

def deleteTempStudentCommentBucket(TempStudentCommentBucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempStudentCommentBucket/" + TempStudentCommentBucketID, verb = "delete")

def deleteTempStudentGPABucket(TempStudentGPABucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempStudentGPABucket/" + TempStudentGPABucketID, verb = "delete")

def deleteTempStudentGPABucketGroup(TempStudentGPABucketGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempStudentGPABucketGroup/" + TempStudentGPABucketGroupID, verb = "delete")

def deleteTempStudentGradeBucket(TempStudentGradeBucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempStudentGradeBucket/" + TempStudentGradeBucketID, verb = "delete")

def deleteTempStudentGradeBucketFlag(TempStudentGradeBucketFlagID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempStudentGradeBucketFlag/" + TempStudentGradeBucketFlagID, verb = "delete")

def deleteTempStudentHonorRollRunLevel(TempStudentHonorRollRunLevelID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempStudentHonorRollRunLevel/" + TempStudentHonorRollRunLevelID, verb = "delete")

def deleteTempStudentRank(TempStudentRankID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempStudentRank/" + TempStudentRankID, verb = "delete")

def deleteTempStudentSection(TempStudentSectionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempStudentSection/" + TempStudentSectionID, verb = "delete")

def deleteTempStudentSectionFailedUpdate(TempStudentSectionFailedUpdateID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempStudentSectionFailedUpdate/" + TempStudentSectionFailedUpdateID, verb = "delete")

def deleteTempStudentSectionGPABucketGroup(TempStudentSectionGPABucketGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempStudentSectionGPABucketGroup/" + TempStudentSectionGPABucketGroupID, verb = "delete")

def deleteTempTransferCourse(TempTransferCourseID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TempTransferCourse/" + TempTransferCourseID, verb = "delete")

def deleteTranscriptNote(TranscriptNoteID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TranscriptNote/" + TranscriptNoteID, verb = "delete")

def deleteTranscriptSent(TranscriptSentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Grading/TranscriptSent/" + TranscriptSentID, verb = "delete")