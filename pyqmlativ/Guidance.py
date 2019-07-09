# This module contains Guidance functions.

from . import make_request

def deleteNotificationMethod(NotificationMethodID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Guidance/NotificationMethod/" + NotificationMethodID, verb = "delete")

def deleteOfficeVisitComment(OfficeVisitCommentID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Guidance/OfficeVisitComment/" + OfficeVisitCommentID, verb = "delete")

def deleteOfficeVisitGuardianResponse(OfficeVisitGuardianResponseID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Guidance/OfficeVisitGuardianResponse/" + OfficeVisitGuardianResponseID, verb = "delete")

def deleteOfficeVisitReason(OfficeVisitReasonID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Guidance/OfficeVisitReason/" + OfficeVisitReasonID, verb = "delete")

def deleteStudentOfficeVisit(StudentOfficeVisitID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Guidance/StudentOfficeVisit/" + StudentOfficeVisitID, verb = "delete")

def deleteStudentOfficeVisitNote(StudentOfficeVisitNoteID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Guidance/StudentOfficeVisitNote/" + StudentOfficeVisitNoteID, verb = "delete")

def deleteStudentOfficeVisitNotification(StudentOfficeVisitNotificationID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Guidance/StudentOfficeVisitNotification/" + StudentOfficeVisitNotificationID, verb = "delete")

def deleteStudentOfficeVisitReason(StudentOfficeVisitReasonID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Guidance/StudentOfficeVisitReason/" + StudentOfficeVisitReasonID, verb = "delete")

def deleteStudentOfficeVisitTimeTransaction(StudentOfficeVisitTimeTransactionID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Guidance/StudentOfficeVisitTimeTransaction/" + StudentOfficeVisitTimeTransactionID, verb = "delete")