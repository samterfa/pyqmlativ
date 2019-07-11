# This module contains Guidance functions.

from .Utilities import make_request

import pandas as pd

def getEveryNotificationMethod(EntityID = 1, page = 1, pageSize = 100, returnNotificationMethodID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/NotificationMethod/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNotificationMethod(NotificationMethodID, EntityID = 1, returnreturnNotificationMethodID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/NotificationMethod/" + str(NotificationMethodID), verb = "get", params_list = params_list)

	return(response)

def deleteNotificationMethod(NotificationMethodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/NotificationMethod/" + str(NotificationMethodID), verb = "delete")

	return(response)

def getEveryOfficeVisitComment(EntityID = 1, page = 1, pageSize = 100, returnOfficeVisitCommentID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitComment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getOfficeVisitComment(OfficeVisitCommentID, EntityID = 1, returnreturnOfficeVisitCommentID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitComment/" + str(OfficeVisitCommentID), verb = "get", params_list = params_list)

	return(response)

def deleteOfficeVisitComment(OfficeVisitCommentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitComment/" + str(OfficeVisitCommentID), verb = "delete")

	return(response)

def getEveryOfficeVisitGuardianResponse(EntityID = 1, page = 1, pageSize = 100, returnOfficeVisitGuardianResponseID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getOfficeVisitGuardianResponse(OfficeVisitGuardianResponseID, EntityID = 1, returnreturnOfficeVisitGuardianResponseID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitGuardianResponse/" + str(OfficeVisitGuardianResponseID), verb = "get", params_list = params_list)

	return(response)

def deleteOfficeVisitGuardianResponse(OfficeVisitGuardianResponseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitGuardianResponse/" + str(OfficeVisitGuardianResponseID), verb = "delete")

	return(response)

def getEveryOfficeVisitReason(EntityID = 1, page = 1, pageSize = 100, returnOfficeVisitReasonID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitReason/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getOfficeVisitReason(OfficeVisitReasonID, EntityID = 1, returnreturnOfficeVisitReasonID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitReason/" + str(OfficeVisitReasonID), verb = "get", params_list = params_list)

	return(response)

def deleteOfficeVisitReason(OfficeVisitReasonID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitReason/" + str(OfficeVisitReasonID), verb = "delete")

	return(response)

def getEveryStudentOfficeVisit(EntityID = 1, page = 1, pageSize = 100, returnStudentOfficeVisitID = True, returnCreatedTime = False, returnDisplayStatus = False, returnDocumentationIsComplete = False, returnEntityID = False, returnHasBeenReleased = False, returnIsStudentOfficeVisitToday = False, returnModifiedTime = False, returnOfficeVisitCommentID = False, returnSchoolID = False, returnSchoolYearID = False, returnStudentID = False, returnStudentOfficeVisitReasonsListDisplay = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisit/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentOfficeVisit(StudentOfficeVisitID, EntityID = 1, returnreturnStudentOfficeVisitID = False, returnreturnCreatedTime = False, returnreturnDisplayStatus = False, returnreturnDocumentationIsComplete = False, returnreturnEntityID = False, returnreturnHasBeenReleased = False, returnreturnIsStudentOfficeVisitToday = False, returnreturnModifiedTime = False, returnreturnOfficeVisitCommentID = False, returnreturnSchoolID = False, returnreturnSchoolYearID = False, returnreturnStudentID = False, returnreturnStudentOfficeVisitReasonsListDisplay = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisit/" + str(StudentOfficeVisitID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentOfficeVisit(StudentOfficeVisitID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisit/" + str(StudentOfficeVisitID), verb = "delete")

	return(response)

def getEveryStudentOfficeVisitNote(EntityID = 1, page = 1, pageSize = 100, returnStudentOfficeVisitNoteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentOfficeVisitNote(StudentOfficeVisitNoteID, EntityID = 1, returnreturnStudentOfficeVisitNoteID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnStudentOfficeVisitID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNote/" + str(StudentOfficeVisitNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentOfficeVisitNote(StudentOfficeVisitNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNote/" + str(StudentOfficeVisitNoteID), verb = "delete")

	return(response)

def getEveryStudentOfficeVisitNotification(EntityID = 1, page = 1, pageSize = 100, returnStudentOfficeVisitNotificationID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnNotificationMethodID = False, returnNotificationTime = False, returnNotificationTimeDate = False, returnNotificationTimeTime = False, returnOfficeVisitGuardianResponseID = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNotification/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentOfficeVisitNotification(StudentOfficeVisitNotificationID, EntityID = 1, returnreturnStudentOfficeVisitNotificationID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnNote = False, returnreturnNotificationMethodID = False, returnreturnNotificationTime = False, returnreturnNotificationTimeDate = False, returnreturnNotificationTimeTime = False, returnreturnOfficeVisitGuardianResponseID = False, returnreturnStudentOfficeVisitID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNotification/" + str(StudentOfficeVisitNotificationID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentOfficeVisitNotification(StudentOfficeVisitNotificationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNotification/" + str(StudentOfficeVisitNotificationID), verb = "delete")

	return(response)

def getEveryStudentOfficeVisitReason(EntityID = 1, page = 1, pageSize = 100, returnStudentOfficeVisitReasonID = True, returnCreatedTime = False, returnModifiedTime = False, returnOfficeVisitReasonID = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitReason/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentOfficeVisitReason(StudentOfficeVisitReasonID, EntityID = 1, returnreturnStudentOfficeVisitReasonID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnOfficeVisitReasonID = False, returnreturnStudentOfficeVisitID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitReason/" + str(StudentOfficeVisitReasonID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentOfficeVisitReason(StudentOfficeVisitReasonID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitReason/" + str(StudentOfficeVisitReasonID), verb = "delete")

	return(response)

def getEveryStudentOfficeVisitTimeTransaction(EntityID = 1, page = 1, pageSize = 100, returnStudentOfficeVisitTimeTransactionID = True, returnCreatedTime = False, returnDisplayDuration = False, returnDisplayOrder = False, returnDuration = False, returnEndTime = False, returnEndTimeDate = False, returnEndTimeTime = False, returnModifiedTime = False, returnNote = False, returnStartTime = False, returnStartTimeDate = False, returnStartTimeTime = False, returnStatus = False, returnStatusCode = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitTimeTransaction/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentOfficeVisitTimeTransaction(StudentOfficeVisitTimeTransactionID, EntityID = 1, returnreturnStudentOfficeVisitTimeTransactionID = False, returnreturnCreatedTime = False, returnreturnDisplayDuration = False, returnreturnDisplayOrder = False, returnreturnDuration = False, returnreturnEndTime = False, returnreturnEndTimeDate = False, returnreturnEndTimeTime = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnStartTime = False, returnreturnStartTimeDate = False, returnreturnStartTimeTime = False, returnreturnStatus = False, returnreturnStatusCode = False, returnreturnStudentOfficeVisitID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitTimeTransaction/" + str(StudentOfficeVisitTimeTransactionID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentOfficeVisitTimeTransaction(StudentOfficeVisitTimeTransactionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitTimeTransaction/" + str(StudentOfficeVisitTimeTransactionID), verb = "delete")

	return(response)