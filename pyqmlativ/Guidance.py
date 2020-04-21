# This module contains Guidance functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryNotificationMethod(searchConditions = [], EntityID = 1, returnNotificationMethodID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NotificationMethod in the district.

	This function returns a dataframe of every NotificationMethod in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/NotificationMethod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/NotificationMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryOfficeVisitComment(searchConditions = [], EntityID = 1, returnOfficeVisitCommentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every OfficeVisitComment in the district.

	This function returns a dataframe of every OfficeVisitComment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitComment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitComment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryOfficeVisitGuardianResponse(searchConditions = [], EntityID = 1, returnOfficeVisitGuardianResponseID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every OfficeVisitGuardianResponse in the district.

	This function returns a dataframe of every OfficeVisitGuardianResponse in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryOfficeVisitReason(searchConditions = [], EntityID = 1, returnOfficeVisitReasonID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every OfficeVisitReason in the district.

	This function returns a dataframe of every OfficeVisitReason in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitReason/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentOfficeVisit(searchConditions = [], EntityID = 1, returnStudentOfficeVisitID = False, returnCreatedTime = False, returnDisplayStatus = False, returnDocumentationIsComplete = False, returnEntityID = False, returnHasBeenReleased = False, returnIsStudentOfficeVisitToday = False, returnModifiedTime = False, returnOfficeVisitCommentID = False, returnSchoolID = False, returnSchoolYearID = False, returnStudentID = False, returnStudentOfficeVisitReasonsListDisplay = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentOfficeVisit in the district.

	This function returns a dataframe of every StudentOfficeVisit in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisit/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentOfficeVisitNote(searchConditions = [], EntityID = 1, returnStudentOfficeVisitNoteID = False, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentOfficeVisitNote in the district.

	This function returns a dataframe of every StudentOfficeVisitNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentOfficeVisitNotification(searchConditions = [], EntityID = 1, returnStudentOfficeVisitNotificationID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnNotificationMethodID = False, returnNotificationTime = False, returnNotificationTimeDate = False, returnNotificationTimeTime = False, returnOfficeVisitGuardianResponseID = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentOfficeVisitNotification in the district.

	This function returns a dataframe of every StudentOfficeVisitNotification in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNotification/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNotification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentOfficeVisitReason(searchConditions = [], EntityID = 1, returnStudentOfficeVisitReasonID = False, returnCreatedTime = False, returnModifiedTime = False, returnOfficeVisitReasonID = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentOfficeVisitReason in the district.

	This function returns a dataframe of every StudentOfficeVisitReason in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitReason/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentOfficeVisitTimeTransaction(searchConditions = [], EntityID = 1, returnStudentOfficeVisitTimeTransactionID = False, returnCreatedTime = False, returnDisplayDuration = False, returnDisplayOrder = False, returnDuration = False, returnEndTime = False, returnEndTimeDate = False, returnEndTimeTime = False, returnModifiedTime = False, returnNote = False, returnStartTime = False, returnStartTimeDate = False, returnStartTimeTime = False, returnStatus = False, returnStatusCode = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentOfficeVisitTimeTransaction in the district.

	This function returns a dataframe of every StudentOfficeVisitTimeTransaction in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitTimeTransaction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitTimeTransaction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)