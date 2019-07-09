# This module contains Reporting functions.

def deleteBurstAction(BurstActionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/BurstAction/" + BurstActionID, verb = "delete")

def deleteConfigSystem(ConfigSystemID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/ConfigSystem/" + ConfigSystemID, verb = "delete")

def deleteDataMiningReport(DataMiningReportID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/DataMiningReport/" + DataMiningReportID, verb = "delete")

def deleteDataMiningReportField(DataMiningReportFieldID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/DataMiningReportField/" + DataMiningReportFieldID, verb = "delete")

def deleteDataMiningReportFieldFilter(DataMiningReportFieldFilterID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/DataMiningReportFieldFilter/" + DataMiningReportFieldFilterID, verb = "delete")

def deleteDataMiningReportFieldSort(DataMiningReportFieldSortID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/DataMiningReportFieldSort/" + DataMiningReportFieldSortID, verb = "delete")

def deleteDataMiningReportSortBreak(DataMiningReportSortBreakID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/DataMiningReportSortBreak/" + DataMiningReportSortBreakID, verb = "delete")

def deleteDataMiningReportSubtopic(DataMiningReportSubtopicID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/DataMiningReportSubtopic/" + DataMiningReportSubtopicID, verb = "delete")

def deleteDataMiningReportSubtopicStandardFilter(DataMiningReportSubtopicStandardFilterID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/DataMiningReportSubtopicStandardFilter/" + DataMiningReportSubtopicStandardFilterID, verb = "delete")

def deletePage(PageID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/Page/" + PageID, verb = "delete")

def deletePageBurst(PageBurstID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/PageBurst/" + PageBurstID, verb = "delete")

def deletePromptTemplate(PromptTemplateID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/PromptTemplate/" + PromptTemplateID, verb = "delete")

def deleteReport(ReportID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/Report/" + ReportID, verb = "delete")

def deleteReportMenuModule(ReportMenuModuleID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/ReportMenuModule/" + ReportMenuModuleID, verb = "delete")

def deleteReportQueue(ReportQueueID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/ReportQueue/" + ReportQueueID, verb = "delete")

def deleteReportQueueBurstAction(ReportQueueBurstActionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/ReportQueueBurstAction/" + ReportQueueBurstActionID, verb = "delete")

def deleteReportQueueSQL(ReportQueueSQLID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/ReportQueueSQL/" + ReportQueueSQLID, verb = "delete")

def deleteReportRole(ReportRoleID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/ReportRole/" + ReportRoleID, verb = "delete")

def deleteReportRunInfo(ReportRunInfoID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/ReportRunInfo/" + ReportRunInfoID, verb = "delete")

def deleteReportStyle(ReportStyleID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/ReportStyle/" + ReportStyleID, verb = "delete")

def deleteScheduledReport(ScheduledReportID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/ScheduledReport/" + ScheduledReportID, verb = "delete")

def deleteSecurityLocationReportSet(SecurityLocationReportSetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/SecurityLocationReportSet/" + SecurityLocationReportSetID, verb = "delete")

def deleteSecurityLocationReportSetReportRunInfo(SecurityLocationReportSetReportRunInfoID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/SecurityLocationReportSetReportRunInfo/" + SecurityLocationReportSetReportRunInfoID, verb = "delete")

def deleteSort(SortID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/Sort/" + SortID, verb = "delete")

def deleteSortBreak(SortBreakID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/SortBreak/" + SortBreakID, verb = "delete")

def deleteSortGroup(SortGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/SortGroup/" + SortGroupID, verb = "delete")

def deleteSubject(SubjectID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/Subject/" + SubjectID, verb = "delete")

def deleteSubjectSecurityLocation(SubjectSecurityLocationID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/SubjectSecurityLocation/" + SubjectSecurityLocationID, verb = "delete")

def deleteSubtopic(SubtopicID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/Subtopic/" + SubtopicID, verb = "delete")

def deleteSubtopicField(SubtopicFieldID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/SubtopicField/" + SubtopicFieldID, verb = "delete")

def deleteSubtopicStandardFilter(SubtopicStandardFilterID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/SubtopicStandardFilter/" + SubtopicStandardFilterID, verb = "delete")

def deleteSummaryReportParameter(SummaryReportParameterID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/SummaryReportParameter/" + SummaryReportParameterID, verb = "delete")

def deleteSummaryReportPrompt(SummaryReportPromptID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/SummaryReportPrompt/" + SummaryReportPromptID, verb = "delete")

def deleteSummaryReportSection(SummaryReportSectionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/SummaryReportSection/" + SummaryReportSectionID, verb = "delete")

def deleteSummaryReportSectionColumn(SummaryReportSectionColumnID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/SummaryReportSectionColumn/" + SummaryReportSectionColumnID, verb = "delete")

def deleteTopic(TopicID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/Topic/" + TopicID, verb = "delete")

def deleteUploadReportLog(UploadReportLogID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/UploadReportLog/" + UploadReportLogID, verb = "delete")

def deleteUserReportPrompt(UserReportPromptID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/UserReportPrompt/" + UserReportPromptID, verb = "delete")

def deleteUserSetting(UserSettingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Reporting/UserSetting/" + UserSettingID, verb = "delete")