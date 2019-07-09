# This module contains Guidance functions.

def deleteNotificationMethod(NotificationMethodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Guidance/NotificationMethod/" + NotificationMethodID, verb = "delete")

def deleteOfficeVisitComment(OfficeVisitCommentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Guidance/OfficeVisitComment/" + OfficeVisitCommentID, verb = "delete")

def deleteOfficeVisitGuardianResponse(OfficeVisitGuardianResponseID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Guidance/OfficeVisitGuardianResponse/" + OfficeVisitGuardianResponseID, verb = "delete")

def deleteOfficeVisitReason(OfficeVisitReasonID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Guidance/OfficeVisitReason/" + OfficeVisitReasonID, verb = "delete")

def deleteStudentOfficeVisit(StudentOfficeVisitID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Guidance/StudentOfficeVisit/" + StudentOfficeVisitID, verb = "delete")

def deleteStudentOfficeVisitNote(StudentOfficeVisitNoteID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Guidance/StudentOfficeVisitNote/" + StudentOfficeVisitNoteID, verb = "delete")

def deleteStudentOfficeVisitNotification(StudentOfficeVisitNotificationID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Guidance/StudentOfficeVisitNotification/" + StudentOfficeVisitNotificationID, verb = "delete")

def deleteStudentOfficeVisitReason(StudentOfficeVisitReasonID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Guidance/StudentOfficeVisitReason/" + StudentOfficeVisitReasonID, verb = "delete")

def deleteStudentOfficeVisitTimeTransaction(StudentOfficeVisitTimeTransactionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Guidance/StudentOfficeVisitTimeTransaction/" + StudentOfficeVisitTimeTransactionID, verb = "delete")