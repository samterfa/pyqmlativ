# This module contains Student functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryActivity(searchConditions = [], EntityID = 1, returnActivityID = False, returnActivityIDClonedFrom = False, returnActivityIDClonedTo = False, returnActivityLeaderNames = False, returnActivityTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHideInFamilyAccess = False, returnModifiedTime = False, returnSchoolYearID = False, returnSingleSex = False, returnSingleSexCode = False, returnStartDate = False, returnStudentAwardID = False, returnUseForAthleticEligibilityReporting = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Activity in the district.

	This function returns a dataframe of every Activity in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Activity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Activity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryActivityEvent(searchConditions = [], EntityID = 1, returnActivityEventID = False, returnActivityID = False, returnCodeSummary = False, returnContactType = False, returnContactTypeCode = False, returnCost = False, returnCreatedTime = False, returnDate = False, returnDescription = False, returnDescriptionSummary = False, returnDisplayOnDistrictCalendar = False, returnEndTime = False, returnEventTypeID = False, returnLocationID = False, returnModifiedTime = False, returnNameIDContact = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnSummary = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVisibleTo = False, returnVisibleToCode = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ActivityEvent in the district.

	This function returns a dataframe of every ActivityEvent in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityEvent/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityEvent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryActivityPersonnel(searchConditions = [], EntityID = 1, returnActivityPersonnelID = False, returnActivityID = False, returnActivityPersonnelIDClonedFrom = False, returnCreatedTime = False, returnIsLeader = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ActivityPersonnel in the district.

	This function returns a dataframe of every ActivityPersonnel in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityPersonnel/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityPersonnel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryActivityType(searchConditions = [], EntityID = 1, returnActivityTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ActivityType in the district.

	This function returns a dataframe of every ActivityType in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAlert(searchConditions = [], EntityID = 1, returnAlertID = False, returnCreatedTime = False, returnEndDate = False, returnInformation = False, returnIsActive = False, returnIsCritical = False, returnModifiedTime = False, returnStartDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Alert in the district.

	This function returns a dataframe of every Alert in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Alert/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Alert/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAwardCategory(searchConditions = [], EntityID = 1, returnAwardCategoryID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AwardCategory in the district.

	This function returns a dataframe of every AwardCategory in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/AwardCategory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/AwardCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAwardHardware(searchConditions = [], EntityID = 1, returnAwardHardwareID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AwardHardware in the district.

	This function returns a dataframe of every AwardHardware in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/AwardHardware/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/AwardHardware/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAwardType(searchConditions = [], EntityID = 1, returnAwardTypeID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AwardType in the district.

	This function returns a dataframe of every AwardType in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/AwardType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/AwardType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigDistrict(searchConditions = [], EntityID = 1, returnConfigDistrictID = False, returnCreatedTime = False, returnDistrictID = False, returnEnableIEPWriterDocumentFunctions = False, returnIEPWriterDocumentSecurityToken = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ConfigDistrict in the district.

	This function returns a dataframe of every ConfigDistrict in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigEntityGroupYear(searchConditions = [], EntityID = 1, returnConfigEntityGroupYearID = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCourseSubjectIDFollettDestinyRoomTeacher = False, returnCreatedTime = False, returnDefaultAllowFeeManagementOnlinePaymentAccess = False, returnDefaultAllowFoodServiceOnlinePaymentAccess = False, returnEntityGroupKey = False, returnEntityID = False, returnFollettDestinyCustomEntityCode = False, returnFollettDestinyRoomTeacherPeriod = False, returnFollettDestinyRoomTeacherType = False, returnFollettDestinyRoomTeacherTypeCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentAccessAccountInfoEmailBody = False, returnStudentAccessAccountInfoEmailIncludeResetPasswordText = False, returnStudentAccessAccountInfoEmailSubject = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ConfigEntityGroupYear in the district.

	This function returns a dataframe of every ConfigEntityGroupYear in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigSystem(searchConditions = [], EntityID = 1, returnConfigSystemID = False, returnAllowStudentAccessDefault = False, returnAutoGenerateEmail = False, returnAutoGenerateEmailCode = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnEasyIEPSection504ImportFilePath = False, returnEasyIEPSpecEdImportFilePath = False, returnEmailDomain = False, returnEmailTypeIDDefault = False, returnModifiedTime = False, returnStudentAttachmentVisibility = False, returnStudentAttachmentVisibilityCode = False, returnStudentNumberMask = False, returnStudentNumberStartValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ConfigSystem in the district.

	This function returns a dataframe of every ConfigSystem in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCurrentSportsSelections(searchConditions = [], EntityID = 1, returnCurrentSportsSelectionsID = False, returnCreatedTime = False, returnFallSportID = False, returnModifiedTime = False, returnSpringSportID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSportID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CurrentSportsSelections in the district.

	This function returns a dataframe of every CurrentSportsSelections in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CurrentSportsSelections/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CurrentSportsSelections/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCustomCode(searchConditions = [], EntityID = 1, returnCustomCodeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCustomCodeTypeID = False, returnDescription = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CustomCode in the district.

	This function returns a dataframe of every CustomCode in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CustomCode/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CustomCode/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCustomCodeType(searchConditions = [], EntityID = 1, returnCustomCodeTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CustomCodeType in the district.

	This function returns a dataframe of every CustomCodeType in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CustomCodeType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CustomCodeType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEthnicityMA(searchConditions = [], EntityID = 1, returnEthnicityMAID = False, returnCode = False, returnCreatedTime = False, returnEthnicity = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EthnicityMA in the district.

	This function returns a dataframe of every EthnicityMA in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/EthnicityMA/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/EthnicityMA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEventType(searchConditions = [], EntityID = 1, returnEventTypeID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EventType in the district.

	This function returns a dataframe of every EventType in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/EventType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/EventType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryFallSport(searchConditions = [], EntityID = 1, returnFallSportID = False, returnCode = False, returnCreatedTime = False, returnFallSport = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every FallSport in the district.

	This function returns a dataframe of every FallSport in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FallSport/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FallSport/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryFallSportsTeam(searchConditions = [], EntityID = 1, returnFallSportsTeamID = False, returnCaptain = False, returnCreatedTime = False, returnFallSportID = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every FallSportsTeam in the district.

	This function returns a dataframe of every FallSportsTeam in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FallSportsTeam/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FallSportsTeam/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryFeederSchool(searchConditions = [], EntityID = 1, returnFeederSchoolID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every FeederSchool in the district.

	This function returns a dataframe of every FeederSchool in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FeederSchool/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FeederSchool/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryIndicator(searchConditions = [], EntityID = 1, returnIndicatorID = False, returnCreatedTime = False, returnImage = False, returnImageCode = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnRank = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Indicator in the district.

	This function returns a dataframe of every Indicator in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Indicator/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Indicator/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryLock(searchConditions = [], EntityID = 1, returnLockID = False, returnBuildingID = False, returnCreatedTime = False, returnIsAssigned = False, returnIsAttached = False, returnIsAvailable = False, returnIsBuiltInLock = False, returnLockerID = False, returnLockMakeID = False, returnModifiedTime = False, returnOwnedBySchool = False, returnRenderRemoveLock = False, returnSerialNumber = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Lock in the district.

	This function returns a dataframe of every Lock in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Lock/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Lock/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryLockCombination(searchConditions = [], EntityID = 1, returnLockCombinationID = False, returnCombination = False, returnCombinationNumber = False, returnCreatedTime = False, returnIsCurrentCombination = False, returnLockID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every LockCombination in the district.

	This function returns a dataframe of every LockCombination in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockCombination/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockCombination/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryLocker(searchConditions = [], EntityID = 1, returnLockerID = False, returnComment = False, returnCreatedTime = False, returnCurrentCombination = False, returnGender = False, returnGenderCode = False, returnGenderCount = False, returnHasBuiltInLock = False, returnIsActive = False, returnIsAvailable = False, returnIsDamaged = False, returnLockerAreaID = False, returnLockerNumber = False, returnModifiedTime = False, returnNeedsLock = False, returnStudentsPerLocker = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Locker in the district.

	This function returns a dataframe of every Locker in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Locker/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Locker/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryLockerArea(searchConditions = [], EntityID = 1, returnLockerAreaID = False, returnAllowCoedLocker = False, returnBuildingID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnHasBuiltInLockDefault = False, returnMaximumStudentsPerLocker = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every LockerArea in the district.

	This function returns a dataframe of every LockerArea in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockerArea/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockerArea/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryLockMake(searchConditions = [], EntityID = 1, returnLockMakeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every LockMake in the district.

	This function returns a dataframe of every LockMake in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockMake/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockMake/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNextStudentNumber(searchConditions = [], EntityID = 1, returnNextStudentNumberID = False, returnCreatedTime = False, returnIsForStateID = False, returnMaskPrefix = False, returnModifiedTime = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NextStudentNumber in the district.

	This function returns a dataframe of every NextStudentNumber in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/NextStudentNumber/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/NextStudentNumber/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNoteType(searchConditions = [], EntityID = 1, returnNoteTypeID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnIndicatorID = False, returnIsActive = False, returnIsParentalConsent = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NoteType in the district.

	This function returns a dataframe of every NoteType in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/NoteType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/NoteType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryReligion(searchConditions = [], EntityID = 1, returnReligionID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Religion in the district.

	This function returns a dataframe of every Religion in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Religion/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Religion/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySkylertAttendanceExportAttendanceType(searchConditions = [], EntityID = 1, returnSkylertAttendanceExportAttendanceTypeID = False, returnAttendanceTypeCodeOverride = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnSkylertAttendanceExportSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SkylertAttendanceExportAttendanceType in the district.

	This function returns a dataframe of every SkylertAttendanceExportAttendanceType in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportAttendanceType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportAttendanceType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySkylertAttendanceExportSetting(searchConditions = [], EntityID = 1, returnSkylertAttendanceExportSettingID = False, returnAttendancePeriodIDHigh = False, returnAttendancePeriodIDLow = False, returnCreatedTime = False, returnEntityID = False, returnFileSequence = False, returnMinimumPeriodsAbsent = False, returnModifiedTime = False, returnParentNotifiedOption = False, returnParentNotifiedOptionCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SkylertAttendanceExportSetting in the district.

	This function returns a dataframe of every SkylertAttendanceExportSetting in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySkylertAttendanceExportSettingScheduledTask(searchConditions = [], EntityID = 1, returnSkylertAttendanceExportSettingScheduledTaskID = False, returnCreatedTime = False, returnModifiedTime = False, returnScheduledTaskID = False, returnSkylertAttendanceExportSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SkylertAttendanceExportSettingScheduledTask in the district.

	This function returns a dataframe of every SkylertAttendanceExportSettingScheduledTask in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportSettingScheduledTask/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportSettingScheduledTask/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySpringSport(searchConditions = [], EntityID = 1, returnSpringSportID = False, returnCode = False, returnCreatedTime = False, returnModifiedTime = False, returnSpringSport = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SpringSport in the district.

	This function returns a dataframe of every SpringSport in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SpringSport/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SpringSport/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySpringSportsTeam(searchConditions = [], EntityID = 1, returnSpringSportsTeamID = False, returnCaptain = False, returnCreatedTime = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnSpringSportID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SpringSportsTeam in the district.

	This function returns a dataframe of every SpringSportsTeam in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SpringSportsTeam/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SpringSportsTeam/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentActivity(searchConditions = [], EntityID = 1, returnStudentActivityID = False, returnActivityID = False, returnCourseID = False, returnCreatedTime = False, returnHasParticipation = False, returnIsActive = False, returnModifiedTime = False, returnStudentActivityIDClonedFrom = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentActivity in the district.

	This function returns a dataframe of every StudentActivity in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentActivity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentActivity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentActivityTransaction(searchConditions = [], EntityID = 1, returnStudentActivityTransactionID = False, returnCreatedTime = False, returnModifiedTime = False, returnParticipationEndDate = False, returnParticipationStartDate = False, returnStudentActivityID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentActivityTransaction in the district.

	This function returns a dataframe of every StudentActivityTransaction in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentActivityTransaction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentActivityTransaction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentAward(searchConditions = [], EntityID = 1, returnStudentAwardID = False, returnActivityID = False, returnAwardCategoryID = False, returnAwardHardwareID = False, returnAwardTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentAward in the district.

	This function returns a dataframe of every StudentAward in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentAward/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentAward/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentCustomCode(searchConditions = [], EntityID = 1, returnStudentCustomCodeID = False, returnCreatedTime = False, returnCustomCodeID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentCustomCode in the district.

	This function returns a dataframe of every StudentCustomCode in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentCustomCode/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentCustomCode/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentDistrict(searchConditions = [], EntityID = 1, returnStudentDistrictID = False, returnCreatedTime = False, returnDistrictID = False, returnFeederSchoolID = False, returnFirstName = False, returnGrade = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentDistrict in the district.

	This function returns a dataframe of every StudentDistrict in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentDistrict/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentDistrict/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentEthnicityMA(searchConditions = [], EntityID = 1, returnStudentEthnicityMAID = False, returnCreatedTime = False, returnEthnicityMAID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentEthnicityMA in the district.

	This function returns a dataframe of every StudentEthnicityMA in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentEthnicityMA/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentEthnicityMA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentLocker(searchConditions = [], EntityID = 1, returnStudentLockerID = False, returnCreatedTime = False, returnIsPrimaryLocker = False, returnLockerID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentLocker in the district.

	This function returns a dataframe of every StudentLocker in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentLocker/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentLocker/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentMassUpdate(searchConditions = [], EntityID = 1, returnStudentMassUpdateID = False, returnAsOfDate = False, returnCreatedTime = False, returnDistrictID = False, returnFilterParameters = False, returnModifiedTime = False, returnRunReason = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRanBy = False, returnValueParameters = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentMassUpdate in the district.

	This function returns a dataframe of every StudentMassUpdate in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentMassUpdate/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentMassUpdate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentMedia(searchConditions = [], EntityID = 1, returnStudentMediaID = False, returnAttachmentTypeID = False, returnCreatedTime = False, returnDisplayInTeacherAccess = False, returnDisplayName = False, returnDisplayNameOrMediaName = False, returnDisplayOnFamilyAccessPortfolio = False, returnDisplayOnStudentAccessPortfolio = False, returnMediaID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentMedia in the district.

	This function returns a dataframe of every StudentMedia in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentMedia/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentMedia/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudent(searchConditions = [], EntityID = 1, returnStudentID = False, returnAllowCustomerCategoryAdd = False, returnAllowDistrictDistribution = False, returnAllowHigherEdDistribution = False, returnAllowLocalDistribution = False, returnAllowMediaDistribution = False, returnAllowMilitaryDistribution = False, returnAllowPublicDistribution = False, returnAllowStudentAccess = False, returnAllowTripsDistribution = False, returnAllowVendorsDistribution = False, returnArrestCount = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCalculatedEntityYearIsActive = False, returnCalculatedGrade = False, returnCalculatedGradYear = False, returnCalculatedLocation = False, returnCalculatedPrimaryFormattedPhoneNumber = False, returnCalculatedStudentStateID = False, returnConversionKey = False, returnCorporalPunishmentIncidents = False, returnCreatedTime = False, returnCurrentDefaultEntityIsActive = False, returnCurrentEconomicIndicator = False, returnDateOfFirstEntryWithdrawalInEntity = False, returnDentalPolicyNumber = False, returnDisciplinedBullyingDisability = False, returnDisciplinedBullyingRace = False, returnDisciplinedBullyingSex = False, returnEarliestDistrictEnrollmentDate = False, returnEarnedCredits = False, returnEarnedCreditsPossible = False, returnEdFiCountryIDBirth = False, returnEffectiveDateForDirectCertificationImport = False, returnEligibilityCategoryForDirectCertificationImport = False, returnEntityConfigEarnedCredits = False, returnEntityConfigFailedCredits = False, returnEntryWithdrawalIDDefaultEntityToday = False, returnExpulsionWithoutServicesCount = False, returnExpulsionWithServicesCount = False, returnFailedCredits = False, returnFeeOnlinePaymentOverrideType = False, returnFeeOnlinePaymentOverrideTypeCode = False, returnFirstName = False, returnFoodServiceOnlinePaymentOverrideType = False, returnFoodServiceOnlinePaymentOverrideTypeCode = False, returnFormattedVaccinationDates = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnGrade = False, returnGradeNumeric = False, returnGraduationDate = False, returnGraduationRequirementYear = False, returnGradYear = False, returnHasActiveAlert = False, returnHasActiveCriticalAlert = False, returnHasActiveGeneralNote = False, returnHasActiveHealthCondition = False, returnHasActiveIHP = False, returnHasActiveInterventionPlan = False, returnHasActiveParentalConsentNote = False, returnHasActiveSection504 = False, returnHasActiveSpecialEducation = False, returnHasActiveStudentGuardianRestrictedAccess = False, returnHasAdvancedMathGrade0912 = False, returnHasAlertIndicator = False, returnHasAlgebraIGrade07 = False, returnHasAlgebraIGrade08 = False, returnHasAlgebraIGrade0910 = False, returnHasAlgebraIGrade1112 = False, returnHasAlgebraIIGrade0912 = False, returnHasAllowStudentAccessButNoSecurity = False, returnHasAPComputerScienceGrade0912 = False, returnHasAPCourseGrade0912 = False, returnHasAPMathGrade0912 = False, returnHasAPOtherGrade0912 = False, returnHasAPScienceGrade0912 = False, returnHasBiologyGrade0912 = False, returnHasCalculusGrade0912 = False, returnHasChemistryGrade0912 = False, returnHasComputerScienceGrade0912 = False, returnHasCreditRecovery = False, returnHasCriticalAlertIndicator = False, returnHasDuplicateStudentNumber = False, returnHasGeneralNoteIndicator = False, returnHasGeometryGrade08 = False, returnHasGeometryGrade0912 = False, returnHasHealthIndicator = False, returnHasIHPIndicator = False, returnHasInterventionPlanIndicator = False, returnHasOneNormalEnrollmentInEntityDuringSchoolYear = False, returnHasParentalConsentNoteIndicator = False, returnHasPassedAlgebraIGrade07 = False, returnHasPassedAlgebraIGrade08 = False, returnHasPassedAlgebraIGrade0910 = False, returnHasPassedAlgebraIGrade1112 = False, returnHasPhysicsGrade0912 = False, returnHasSection504Indicator = False, returnHasSpecialEducationIndicator = False, returnHasStudentEntityYearForCurrentSchoolYear = False, returnHasStudentGuardianWithAllowFamilyAccessButNoSecurity = False, returnHasTakenACT0912 = False, returnHasTakenAPExam0912 = False, returnHasTakenSAT0912 = False, returnHealthPolicyNumber = False, returnHealthProfessionalIDDentist = False, returnHealthProfessionalIDPrimaryPhysician = False, returnIndicatorsXML = False, returnInSchoolSuspensionCount = False, returnInSpecifiedDirectCertificationImport = False, returnIsActiveAsOfDate = False, returnIsChronicallyAbsent = False, returnIsCurrentActive = False, returnIsCurrentActiveDefaultEnrollment = False, returnIsCurrentlyTransported = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnIsGiftedTalentedSnapshot = False, returnIsGraduated = False, returnIsHealthProfessionalDentist = False, returnIsHealthProfessionalPrimaryPhysician = False, returnIsIBDiplomaProgramme = False, returnIsIDEA = False, returnIsIDEASnapshot = False, returnIsLEP = False, returnIsLEPSnapshot = False, returnIsSection504 = False, returnIsSection504Snapshot = False, returnIsStateReportingUnknownGender = False, returnLanguageIDNative = False, returnLanguageIDPrimary = False, returnLastName = False, returnLawEnforcementReferralCount = False, returnLocation = False, returnLocationDateToUse = False, returnLocationEntityID = False, returnLocationSchoolYearID = False, returnMaskedStudentNumber = False, returnMechanicalRestraintCount = False, returnMedicaidNumber = False, returnMiddleName = False, returnMMRStatus = False, returnModifiedTime = False, returnNameID = False, returnNameIDDentalInsuranceCompany = False, returnNameIDDentalPractice = False, returnNameIDHealthInsuranceCompany = False, returnNameIDHospital = False, returnOutOfSchoolSuspensionCount = False, returnOutOfSchoolSuspensionMissedDays = False, returnOverrideFeeOnlinePaymentAccess = False, returnOverrideFoodServiceOnlinePaymentAccess = False, returnPhysicalRestraintCount = False, returnReportedBulliedDisability = False, returnReportedBulliedRace = False, returnReportedBulliedSex = False, returnSchoolPathExpectedSchoolCode = False, returnSchoolPathExpectedSchoolName = False, returnSchoolYearIDSpecifiedCohort = False, returnSeclusionCount = False, returnSingleSexAthleticCount = False, returnSpecifiedCohortNumericSchoolYear = False, returnSpecifiedEntityYearNoShow = False, returnStateEthnicityRaceCodeMNID = False, returnStudentIDHash = False, returnStudentIndicatorColumn = False, returnStudentMNID = False, returnStudentNumber = False, returnStudentNumberForGradebook = False, returnStudentRankSort = False, returnStudentStateID = False, returnTotalCommunityServiceHours = False, returnTransferToAlternativeSchool = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLIndicators = False, returnZeroToleranceWithoutServicesCount = False, returnZeroToleranceWithServicesCount = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Student in the district.

	This function returns a dataframe of every Student in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Student/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Student/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentNote(searchConditions = [], EntityID = 1, returnStudentNoteID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnNoteTypeID = False, returnStartDate = False, returnStudentID = False, returnStudentTransportationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentNote in the district.

	This function returns a dataframe of every StudentNote in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempActivityRecord(searchConditions = [], EntityID = 1, returnTempActivityRecordID = False, returnActivityID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempActivityRecord in the district.

	This function returns a dataframe of every TempActivityRecord in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempActivityRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempActivityRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempFitnessGram(searchConditions = [], EntityID = 1, returnTempFitnessGramID = False, returnClassDescription = False, returnClassEndDate = False, returnClassID = False, returnClassName = False, returnClassStartDate = False, returnCourseCodeDescription = False, returnCreatedTime = False, returnHasMissingData = False, returnMessage = False, returnModifiedTime = False, returnParentReportEmail1 = False, returnParentReportEmail2 = False, returnSchoolID = False, returnSectionCode = False, returnStudentBirthdate = False, returnStudentFirstName = False, returnStudentGender = False, returnStudentGrade = False, returnStudentID = False, returnStudentLastName = False, returnStudentMiddleInitial = False, returnStudentPassword = False, returnStudentReportEmail = False, returnStudentSSOID = False, returnTeacherBirthDate = False, returnTeacherEmail = False, returnTeacherFirstName = False, returnTeacherID = False, returnTeacherLastName = False, returnTeacherMiddleInitial = False, returnTeacherPassword = False, returnTeacherSSOID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempFitnessGram in the district.

	This function returns a dataframe of every TempFitnessGram in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempFitnessGram/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempFitnessGram/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempLockCombination(searchConditions = [], EntityID = 1, returnTempLockCombinationID = False, returnCombination = False, returnCombinationNumber = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnTempLockerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempLockCombination in the district.

	This function returns a dataframe of every TempLockCombination in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempLockCombination/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempLockCombination/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempLocker(searchConditions = [], EntityID = 1, returnTempLockerID = False, returnBuilding = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnFailureReason = False, returnLockerArea = False, returnLockerAreaID = False, returnLockerID = False, returnLockerNumber = False, returnLockerNumberDigitLength = False, returnModifiedTime = False, returnNewLockerNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempLocker in the district.

	This function returns a dataframe of every TempLocker in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempLocker/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempLocker/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentActivity(searchConditions = [], EntityID = 1, returnTempStudentActivityID = False, returnActivityID = False, returnAge = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityCode = False, returnErrorNumber = False, returnFullNameLFM = False, returnGenderCodeAndGender = False, returnGradeLevel = False, returnGradYear = False, returnIsActive = False, returnModifiedTime = False, returnParticipationEndDate = False, returnParticipationStartDate = False, returnStartDate = False, returnStudentID = False, returnStudentName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentActivity in the district.

	This function returns a dataframe of every TempStudentActivity in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentActivityError(searchConditions = [], EntityID = 1, returnTempStudentActivityErrorID = False, returnCreatedTime = False, returnErrorNumber = False, returnErrorText = False, returnModifiedTime = False, returnTempStudentActivityID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentActivityError in the district.

	This function returns a dataframe of every TempStudentActivityError in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivityError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivityError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentActivityTransactionRecord(searchConditions = [], EntityID = 1, returnTempStudentActivityTransactionRecordID = False, returnActivityID = False, returnCreatedTime = False, returnIsValidTransaction = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnStudentActivityTransactionID = False, returnStudentFullNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentActivityTransactionRecord in the district.

	This function returns a dataframe of every TempStudentActivityTransactionRecord in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivityTransactionRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivityTransactionRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentAssignedLockCombinationRecord(searchConditions = [], EntityID = 1, returnTempStudentAssignedLockCombinationRecordID = False, returnAge = False, returnBirthDate = False, returnBuilding = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGrade = False, returnGradYear = False, returnLockerArea = False, returnLockerID = False, returnLockerNumber = False, returnLockID = False, returnModifiedTime = False, returnNewCombination = False, returnNewCombinationNumber = False, returnNewLockCombinationID = False, returnOldCombination = False, returnOldCombinationNumber = False, returnOldLockCombinationID = False, returnStudentID = False, returnStudentNumber = False, returnUnoccupiedLockersOnly = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentAssignedLockCombinationRecord in the district.

	This function returns a dataframe of every TempStudentAssignedLockCombinationRecord in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentAssignedLockCombinationRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentAssignedLockCombinationRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentAssignedLockerRecord(searchConditions = [], EntityID = 1, returnTempStudentAssignedLockerRecordID = False, returnAge = False, returnBirthDate = False, returnBuilding = False, returnCombination = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGrade = False, returnGradYear = False, returnIsStudentAccessUser = False, returnLockerArea = False, returnLockerID = False, returnLockerNumber = False, returnModifiedTime = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentAssignedLockerRecord in the district.

	This function returns a dataframe of every TempStudentAssignedLockerRecord in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentAssignedLockerRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentAssignedLockerRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentError(searchConditions = [], EntityID = 1, returnTempStudentErrorID = False, returnCreatedTime = False, returnErrorCount = False, returnFullStudentNameLFM = False, returnGender = False, returnGradeLevelCode = False, returnGraduationRequirementYear = False, returnGradYear = False, returnIsCurrentActive = False, returnLockerNumber = False, returnModifiedTime = False, returnNote = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnStudentTypeDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentError in the district.

	This function returns a dataframe of every TempStudentError in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentErrorMessage(searchConditions = [], EntityID = 1, returnTempStudentErrorMessageID = False, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnModifiedTime = False, returnTempStudentErrorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentErrorMessage in the district.

	This function returns a dataframe of every TempStudentErrorMessage in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentErrorMessage/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentErrorMessage/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentMassUpdateError(searchConditions = [], EntityID = 1, returnTempStudentMassUpdateErrorID = False, returnCreatedTime = False, returnFailureReason = False, returnFullNameLFM = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentMassUpdateError in the district.

	This function returns a dataframe of every TempStudentMassUpdateError in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMassUpdateError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMassUpdateError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentMassUpdateField(searchConditions = [], EntityID = 1, returnTempStudentMassUpdateFieldID = False, returnAffectedPrimaryKey = False, returnCreatedTime = False, returnFieldName = False, returnFriendlyOriginalValue = False, returnFriendlyUpdatedValue = False, returnFullNameLFM = False, returnModifiedTime = False, returnOriginalValue = False, returnRelatedType = False, returnRelatedTypeCode = False, returnStudentID = False, returnUpdatedValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentMassUpdateField in the district.

	This function returns a dataframe of every TempStudentMassUpdateField in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMassUpdateField/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMassUpdateField/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentMergeObject(searchConditions = [], EntityID = 1, returnTempStudentMergeObjectID = False, returnCreatedTime = False, returnFieldToShow = False, returnHandlingType = False, returnHandlingTypeCode = False, returnModifiedTime = False, returnRecordType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentMergeObject in the district.

	This function returns a dataframe of every TempStudentMergeObject in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMergeObject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMergeObject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentPermit(searchConditions = [], EntityID = 1, returnTempStudentPermitID = False, returnAddressID = False, returnAge = False, returnCreatedTime = False, returnDistrictID = False, returnEntityName = False, returnExceptionNote = False, returnFullNameLFM = False, returnGenderCode = False, returnGradYear = False, returnHasExceptions = False, returnModifiedTime = False, returnPermitID = False, returnSchoolYearID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentPermit in the district.

	This function returns a dataframe of every TempStudentPermit in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentPermit/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentPermit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentWithoutLockerRecord(searchConditions = [], EntityID = 1, returnTempStudentWithoutLockerRecordID = False, returnAge = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGradYear = False, returnModifiedTime = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentWithoutLockerRecord in the district.

	This function returns a dataframe of every TempStudentWithoutLockerRecord in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentWithoutLockerRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentWithoutLockerRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryWinterSport(searchConditions = [], EntityID = 1, returnWinterSportID = False, returnCode = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSport = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every WinterSport in the district.

	This function returns a dataframe of every WinterSport in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/WinterSport/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/WinterSport/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryWinterSportsTeam(searchConditions = [], EntityID = 1, returnWinterSportsTeamID = False, returnCaptain = False, returnCreatedTime = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSportID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every WinterSportsTeam in the district.

	This function returns a dataframe of every WinterSportsTeam in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/WinterSportsTeam/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/WinterSportsTeam/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)