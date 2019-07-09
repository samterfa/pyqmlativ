# This module contains MessageCenter functions.

def deleteConfigDistrictYear(ConfigDistrictYearID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/MessageCenter/ConfigDistrictYear/" + ConfigDistrictYearID, verb = "delete")

def deleteConfigDistrictYearWithdrawalCode(ConfigDistrictYearWithdrawalCodeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/MessageCenter/ConfigDistrictYearWithdrawalCode/" + ConfigDistrictYearWithdrawalCodeID, verb = "delete")

def deleteMessage(MessageID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/MessageCenter/Message/" + MessageID, verb = "delete")

def deleteMessageMaster(MessageMasterID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/MessageCenter/MessageMaster/" + MessageMasterID, verb = "delete")

def deleteNotification(NotificationID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/MessageCenter/Notification/" + NotificationID, verb = "delete")

def deleteNotificationAction(NotificationActionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/MessageCenter/NotificationAction/" + NotificationActionID, verb = "delete")

def deleteNotificationAttendanceType(NotificationAttendanceTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/MessageCenter/NotificationAttendanceType/" + NotificationAttendanceTypeID, verb = "delete")

def deleteNotificationCarbonCopyStaff(NotificationCarbonCopyStaffID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/MessageCenter/NotificationCarbonCopyStaff/" + NotificationCarbonCopyStaffID, verb = "delete")

def deleteNotificationDisciplineThreshold(NotificationDisciplineThresholdID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/MessageCenter/NotificationDisciplineThreshold/" + NotificationDisciplineThresholdID, verb = "delete")

def deleteNotificationGradeBucket(NotificationGradeBucketID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/MessageCenter/NotificationGradeBucket/" + NotificationGradeBucketID, verb = "delete")

def deleteNotificationGradeMark(NotificationGradeMarkID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/MessageCenter/NotificationGradeMark/" + NotificationGradeMarkID, verb = "delete")

def deleteNotificationGradeReference(NotificationGradeReferenceID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/MessageCenter/NotificationGradeReference/" + NotificationGradeReferenceID, verb = "delete")

def deleteNotificationOffense(NotificationOffenseID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/MessageCenter/NotificationOffense/" + NotificationOffenseID, verb = "delete")

def deleteNotificationOnlineForm(NotificationOnlineFormID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/MessageCenter/NotificationOnlineForm/" + NotificationOnlineFormID, verb = "delete")

def deleteNotificationScheduleIsAvailableSectionLength(NotificationScheduleIsAvailableSectionLengthID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/MessageCenter/NotificationScheduleIsAvailableSectionLength/" + NotificationScheduleIsAvailableSectionLengthID, verb = "delete")

def deleteNotificationUnrecordedClassAttendance(NotificationUnrecordedClassAttendanceID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/MessageCenter/NotificationUnrecordedClassAttendance/" + NotificationUnrecordedClassAttendanceID, verb = "delete")

def deleteNotificationWithdrawalCode(NotificationWithdrawalCodeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/MessageCenter/NotificationWithdrawalCode/" + NotificationWithdrawalCodeID, verb = "delete")

def deleteQueuedCompletedCareerPlanChangeNotification(QueuedCompletedCareerPlanChangeNotificationID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/MessageCenter/QueuedCompletedCareerPlanChangeNotification/" + QueuedCompletedCareerPlanChangeNotificationID, verb = "delete")

def deleteQueuedCompletedGradeChangeNotification(QueuedCompletedGradeChangeNotificationID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/MessageCenter/QueuedCompletedGradeChangeNotification/" + QueuedCompletedGradeChangeNotificationID, verb = "delete")

def deleteTempMessage(TempMessageID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/MessageCenter/TempMessage/" + TempMessageID, verb = "delete")

def deleteUserMessageSetting(UserMessageSettingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/MessageCenter/UserMessageSetting/" + UserMessageSettingID, verb = "delete")