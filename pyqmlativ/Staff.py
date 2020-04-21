# This module contains Staff functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryConfigEntityGroupYear(searchConditions = [], EntityID = 1, returnConfigEntityGroupYearID = False, returnAllowFoodServiceOnlinePaymentsAccessByDefault = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigSystem(searchConditions = [], EntityID = 1, returnConfigSystemID = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnModifiedTime = False, returnNewTeacherAccessUserMessageContent = False, returnNewTeacherAccessUserMessageSubject = False, returnStaffNumberMask = False, returnStaffNumberStartValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDepartment(searchConditions = [], EntityID = 1, returnDepartmentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDepartmentIDClonedFrom = False, returnDepartmentIDClonedTo = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStaffIDDepartmentHead = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Department in the district.

	This function returns a dataframe of every Department in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/Department/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/Department/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryJobTitleMA(searchConditions = [], EntityID = 1, returnJobTitleMAID = False, returnCreatedTime = False, returnModifiedTime = False, returnStaffID = False, returnTitle = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every JobTitleMA in the district.

	This function returns a dataframe of every JobTitleMA in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/JobTitleMA/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/JobTitleMA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMassPrintStaffScheduleRunHistory(searchConditions = [], EntityID = 1, returnMassPrintStaffScheduleRunHistoryID = False, returnCreatedTime = False, returnEntityID = False, returnMediaID = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnRequestIdentifier = False, returnRunDescription = False, returnSchoolYearID = False, returnSendMessageOnComplete = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MassPrintStaffScheduleRunHistory in the district.

	This function returns a dataframe of every MassPrintStaffScheduleRunHistory in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/MassPrintStaffScheduleRunHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/MassPrintStaffScheduleRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNextStaffNumber(searchConditions = [], EntityID = 1, returnNextStaffNumberID = False, returnCreatedTime = False, returnMaskPrefix = False, returnModifiedTime = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NextStaffNumber in the district.

	This function returns a dataframe of every NextStaffNumber in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/NextStaffNumber/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/NextStaffNumber/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNumberedStaffEntityYearForDistrictAndSchoolYear(searchConditions = [], EntityID = 1, returnStaffEntityYearID = False, returnDistrictID = False, returnEntityID = False, returnSchoolYearID = False, returnStaffDistrictRowNumber = False, returnStaffID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NumberedStaffEntityYearForDistrictAndSchoolYear in the district.

	This function returns a dataframe of every NumberedStaffEntityYearForDistrictAndSchoolYear in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/NumberedStaffEntityYearForDistrictAndSchoolYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/NumberedStaffEntityYearForDistrictAndSchoolYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryScheduleBlocker(searchConditions = [], EntityID = 1, returnScheduleBlockerID = False, returnCreatedTime = False, returnEndDate = False, returnEntityID = False, returnModifiedTime = False, returnReason = False, returnSchoolYearID = False, returnStaffID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ScheduleBlocker in the district.

	This function returns a dataframe of every ScheduleBlocker in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ScheduleBlocker/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ScheduleBlocker/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryScheduleBlockerDisplayPeriod(searchConditions = [], EntityID = 1, returnScheduleBlockerDisplayPeriodID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnScheduleBlockerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ScheduleBlockerDisplayPeriod in the district.

	This function returns a dataframe of every ScheduleBlockerDisplayPeriod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ScheduleBlockerDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ScheduleBlockerDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStaffDepartment(searchConditions = [], EntityID = 1, returnStaffDepartmentID = False, returnCreatedTime = False, returnDepartmentID = False, returnIsDefaultDepartment = False, returnModifiedTime = False, returnStaffDepartmentIDClonedFrom = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StaffDepartment in the district.

	This function returns a dataframe of every StaffDepartment in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffDepartment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffDepartment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStaffEntityYear(searchConditions = [], EntityID = 1, returnStaffEntityYearID = False, returnCreatedTime = False, returnEntityID = False, returnIsActive = False, returnIsAdditionalStaffOnNotification = False, returnIsCareerCenterCounselor = False, returnIsDisciplineOfficer = False, returnIsSubstituteTeacher = False, returnIsTeacher = False, returnModifiedTime = False, returnRoomIDDefault = False, returnSchoolYearID = False, returnStaffDepartmentSummary = False, returnStaffEntityYearClonedTo = False, returnStaffEntityYearIDClonedFrom = False, returnStaffID = False, returnTeacherNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StaffEntityYear in the district.

	This function returns a dataframe of every StaffEntityYear in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffEntityYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStaff(searchConditions = [], EntityID = 1, returnStaffID = False, returnActiveStudentCount = False, returnAssignmentCount = False, returnAssignmentCountForTermCalculated = False, returnAssignmentCountYTDCalculated = False, returnAssignmentDataString = False, returnCreatedTime = False, returnDateTimeofLastScoredAssignment = False, returnDistrictID = False, returnDueDateOfLastAssignmentScored = False, returnFamilyStudentAccessStaffNameToUse = False, returnFileFolderNumber = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnFutureAssignmentCountForTermCalculated = False, returnGradebookLastAccessedTime = False, returnGradedAssignmentCountForTermCalculated = False, returnGradeLevelLowerBound = False, returnGradeLevelUpperBound = False, returnIsActiveForDistrict = False, returnIsCurrentStaffEntityYear = False, returnMissingAssignmentCountForTermCalculated = False, returnModifiedTime = False, returnNameID = False, returnNoCountAssignmentCountForTermCalculated = False, returnNonGradedAssignmentCountForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsYTD = False, returnPercentageOfAssignmentsScoredYTD = False, returnScoreClarifierAssignmentCountForTermCalculated = False, returnStaffMeetCount = False, returnStaffMNID = False, returnStaffNumber = False, returnStaffWebsite = False, returnStudentAssignmentDataString = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Staff in the district.

	This function returns a dataframe of every Staff in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/Staff/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/Staff/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStaffStaffType(searchConditions = [], EntityID = 1, returnStaffStaffTypeID = False, returnCreatedTime = False, returnEndDate = False, returnIsPrimary = False, returnModifiedTime = False, returnStaffID = False, returnStaffStaffTypeIDClonedFrom = False, returnStaffTypeID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StaffStaffType in the district.

	This function returns a dataframe of every StaffStaffType in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffStaffType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffStaffType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStaffType(searchConditions = [], EntityID = 1, returnStaffTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStaffTypeIDClonedFrom = False, returnStaffTypeIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StaffType in the district.

	This function returns a dataframe of every StaffType in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)