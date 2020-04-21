# This module contains Enrollment functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryAMTransportation(searchConditions = [], EntityID = 1, returnAMTransportationID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AMTransportation in the district.

	This function returns a dataframe of every AMTransportation in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AMTransportation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AMTransportation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCommonEducationDataStandardsGradeLevel(searchConditions = [], EntityID = 1, returnCommonEducationDataStandardsGradeLevelID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnOrderNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CommonEducationDataStandardsGradeLevel in the district.

	This function returns a dataframe of every CommonEducationDataStandardsGradeLevel in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/CommonEducationDataStandardsGradeLevel/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/CommonEducationDataStandardsGradeLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigDistrict(searchConditions = [], EntityID = 1, returnConfigDistrictID = False, returnAllowDualEnrollment = False, returnCreatedTime = False, returnDistrictID = False, returnEntryDaysBeforeCalendarStart = False, returnModifiedTime = False, returnNumberDaysBackdateEntry = False, returnNumberDaysBackdateWithdrawal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDaysAfterCalendarEnd = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigDistrictYear(searchConditions = [], EntityID = 1, returnConfigDistrictYearID = False, returnAutoAddSchoolPathOverride = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnEnableNoShow = False, returnEnrolledDifferentEntityNoShowActionType = False, returnEnrolledDifferentEntityNoShowActionTypeCode = False, returnEnrolledDifferentEntityNoShowEntryDate = False, returnEnrolledDifferentEntityNoShowWithdrawalDate = False, returnModifiedTime = False, returnNoDistrictEnrollmentNoShowActionType = False, returnNoDistrictEnrollmentNoShowActionTypeCode = False, returnNoDistrictEnrollmentNoShowEntryDate = False, returnNoDistrictEnrollmentNoShowWithdrawalDate = False, returnPermitIDAutoAdd = False, returnPreviouslyEnrolledSameEntityNoShowActionType = False, returnPreviouslyEnrolledSameEntityNoShowActionTypeCode = False, returnPreviouslyEnrolledSameEntityNoShowEntryDate = False, returnPreviouslyEnrolledSameEntityNoShowWithdrawalDate = False, returnPriorNoShowRecord = False, returnPriorNoShowRecordCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ConfigDistrictYear in the district.

	This function returns a dataframe of every ConfigDistrictYear in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigDistrictYearWithdrawalCode(searchConditions = [], EntityID = 1, returnConfigDistrictYearWithdrawalCodeID = False, returnConfigDistrictYearID = False, returnConfigDistrictYearWithdrawalCodeIDClonedFrom = False, returnCreatedTime = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ConfigDistrictYearWithdrawalCode in the district.

	This function returns a dataframe of every ConfigDistrictYearWithdrawalCode in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYearWithdrawalCode/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYearWithdrawalCode/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEntitySchool(searchConditions = [], EntityID = 1, returnEntitySchoolID = False, returnCreatedTime = False, returnEntityID = False, returnEntitySchoolIDClonedFrom = False, returnEntitySchoolIDClonedTo = False, returnIsDefaultEntityForSchool = False, returnIsDefaultSchoolForEntity = False, returnIsOnlySchoolInEntity = False, returnModifiedTime = False, returnSchoolID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EntitySchool in the district.

	This function returns a dataframe of every EntitySchool in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchool/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchool/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEntitySchoolBuilding(searchConditions = [], EntityID = 1, returnEntitySchoolBuildingID = False, returnBuildingID = False, returnCreatedTime = False, returnEntitySchoolBuildingIDClonedFrom = False, returnEntitySchoolID = False, returnIsPrimary = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EntitySchoolBuilding in the district.

	This function returns a dataframe of every EntitySchoolBuilding in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchoolBuilding/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchoolBuilding/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEntryCode(searchConditions = [], EntityID = 1, returnEntryCodeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEntryCodeIDClonedFrom = False, returnIsCrossEntityCourseEnrollment = False, returnModifiedTime = False, returnSchoolYearID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EntryCode in the district.

	This function returns a dataframe of every EntryCode in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryCode/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryCode/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEntryWithdrawal(searchConditions = [], EntityID = 1, returnEntryWithdrawalID = False, returnAttendanceDays = False, returnCalendarID = False, returnCreatedTime = False, returnEndDate = False, returnEnrolledAtLeastOneDay = False, returnEntityID = False, returnEntryCodeID = False, returnEntryComment = False, returnEntryWithdrawalIDStatusChangePrevious = False, returnEntryWithdrawalMNID = False, returnGradeReferenceID = False, returnHasMessageCenterAllowedWithdrawalCodeOverride = False, returnIsCombinedEnrollmentFullTime = False, returnIsCrossEntityCourseEnrollment = False, returnIsCurrentOrFutureEnrollment = False, returnIsDefaultEntity = False, returnIsHistoricalEnrollment = False, returnIsIndependentStudy = False, returnIsNoShow = False, returnIsPostSecondaryOption = False, returnIsPSEOConcurrentEnrollment = False, returnIsStartDateOnOrAfterFirstDayOfSchool = False, returnMembershipDays = False, returnModifiedTime = False, returnPercentEnrolled = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnPSEOHours = False, returnRenderDeleteOption = False, returnRenderNoShowOption = False, returnRenderPrintWithdrawalFormOption = False, returnRenderUndoStatusChangeOption = False, returnRenderWithdrawalAndStatusChangeOptions = False, returnSchoolID = False, returnSchoolYearID = False, returnSpecialEdServiceHours = False, returnStartDate = False, returnStateAidCategoryCodeMNID = False, returnStateDistrictMNID = False, returnStateLastAttendanceLocationCodeMNID = False, returnStatusChangeEntry = False, returnStatusChangeWithdrawal = False, returnStudentID = False, returnStudentTypeID = False, returnTotalMembershipDays = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnWithdrawalComment = False, returnWithdrawalDate = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EntryWithdrawal in the district.

	This function returns a dataframe of every EntryWithdrawal in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryWithdrawal/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryWithdrawal/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeLevel(searchConditions = [], EntityID = 1, returnGradeLevelID = False, returnCode = False, returnCodeDescription = False, returnCommonEducationDataStandardsGradeLevelID = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnFederalGradeLevel = False, returnFederalGradeLevelCode = False, returnIlluminate = False, returnIlluminateCalculated = False, returnIlluminateOverride = False, returnModifiedTime = False, returnNumericValue = False, returnStateGradeLevel = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeLevel in the district.

	This function returns a dataframe of every GradeLevel in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeLevel/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReference(searchConditions = [], EntityID = 1, returnGradeReferenceID = False, returnCreatedTime = False, returnDistrictGroupKey = False, returnGradeLevelID = False, returnGradeReferenceIDClonedFrom = False, returnGradeReferenceIDClonedTo = False, returnGradeReferenceMNID = False, returnGradYear = False, returnMinutesPresentFullDay = False, returnMinutesPresentHalfDay = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateGradeLevel = False, returnStateSTARGradeLevelMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReference in the district.

	This function returns a dataframe of every GradeReference in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeReference/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeReference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHomeroom(searchConditions = [], EntityID = 1, returnHomeroomID = False, returnCode = False, returnCreatedTime = False, returnEntityID = False, returnHomeroomDetails = False, returnHomeroomIDClonedFrom = False, returnHomeroomIDClonedTo = False, returnModifiedTime = False, returnRoomID = False, returnSchoolYearID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Homeroom in the district.

	This function returns a dataframe of every Homeroom in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Homeroom/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Homeroom/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNumberedStudentEntityYearForDistrictAndSchoolYear(searchConditions = [], EntityID = 1, returnStudentEntityYearID = False, returnDistrictID = False, returnEntityID = False, returnIsDefaultEntity = False, returnSchoolYearID = False, returnStudentDistrictRowNumber = False, returnStudentID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NumberedStudentEntityYearForDistrictAndSchoolYear in the district.

	This function returns a dataframe of every NumberedStudentEntityYearForDistrictAndSchoolYear in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/NumberedStudentEntityYearForDistrictAndSchoolYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/NumberedStudentEntityYearForDistrictAndSchoolYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPaymentPlanMA(searchConditions = [], EntityID = 1, returnPaymentPlanMAID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PaymentPlanMA in the district.

	This function returns a dataframe of every PaymentPlanMA in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PaymentPlanMA/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PaymentPlanMA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPermit(searchConditions = [], EntityID = 1, returnPermitID = False, returnAllowSchoolPathAssignment = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnPermitIDClonedFrom = False, returnPermitIDClonedTo = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Permit in the district.

	This function returns a dataframe of every Permit in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Permit/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Permit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPMTransportation(searchConditions = [], EntityID = 1, returnPMTransportationID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PMTransportation in the district.

	This function returns a dataframe of every PMTransportation in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PMTransportation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PMTransportation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySchoolDistrict(searchConditions = [], EntityID = 1, returnSchoolDistrictID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SchoolDistrict in the district.

	This function returns a dataframe of every SchoolDistrict in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolDistrict/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolDistrict/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySchool(searchConditions = [], EntityID = 1, returnSchoolID = False, returnAllowsSchoolDevices = False, returnAllowsStudentDevices = False, returnBuildingID = False, returnCampusAccountabilityRatingID = False, returnCEEBCode = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnDaysInRegularSchoolYear = False, returnDaysPriorForAlgebraICounts = False, returnDistrictID = False, returnEdFiSchoolCategoryID = False, returnEdFiSchoolID = False, returnEducationalProgramHoursPerWeek = False, returnExcludeFromCRDC = False, returnFaxNumber = False, returnFaxNumberIsInternational = False, returnFederalAlternativeSchoolDetailID = False, returnFederalJusticeFacilityTypeID = False, returnFederalNCESSchoolID = False, returnFormattedFaxNumber = False, returnFormattedPhoneNumber = False, returnGradeLevelIDHigh = False, returnGradeLevelIDLow = False, returnHasAlcoholDrugEducation = False, returnHasAntiBullying = False, returnHasAntiViolence = False, returnHasAPCourses = False, returnHasAPSelfSelection = False, returnHasCorporalPunishment = False, returnHasCreditRecovery = False, returnHasCrisisPlan = False, returnHasDualEnrollment = False, returnHasFiberOptic = False, returnHasGifted = False, returnHasHomicideOccurred = False, returnHasIBDiplomaProgramme = False, returnHasPreschoolNonIDEAAge3 = False, returnHasPreschoolNonIDEAAge4 = False, returnHasPreschoolNonIDEAAge5 = False, returnHasSafetyPlan = False, returnHasShootingOccurred = False, returnHasSingleSexAthletics = False, returnHasSingleSexClasses = False, returnHasUngraded = False, returnHasUngradedMainlyElementary = False, returnHasUngradedMainlyHighSchool = False, returnHasUngradedMainlyMiddleSchool = False, returnHasWiFi = False, returnHasZeroTolerance = False, returnIsALCSchool = False, returnIsAlternative = False, returnIsCEP = False, returnIsCharter = False, returnIsCRDCCollectedForSchoolYear = False, returnIsEntireSchoolMagnet = False, returnIsMagnet = False, returnIsNonLEA = False, returnIsSpecialEducation = False, returnIsTitleIII = False, returnIsTitleISchoolwide = False, returnModifiedTime = False, returnName = False, returnNameIDSafetySpecialist = False, returnNumberWiFiDevices = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnSchoolIDClonedFrom = False, returnSchoolIDClonedTo = False, returnSchoolMNID = False, returnSchoolNumber = False, returnSchoolYearID = False, returnStaffIDPrincipal = False, returnStateAssignedID = False, returnStateKindergartenScheduleIndicatorCodeMNID = False, returnStateSchoolMNID = False, returnStateTitleISchoolIndicatorCodeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every School in the district.

	This function returns a dataframe of every School in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/School/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/School/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySchoolPath(searchConditions = [], EntityID = 1, returnSchoolPathID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnSchoolPathIDClonedFrom = False, returnSchoolPathIDClonedTo = False, returnSchoolPathTypeID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SchoolPath in the district.

	This function returns a dataframe of every SchoolPath in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPath/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPath/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySchoolPathSchool(searchConditions = [], EntityID = 1, returnSchoolPathSchoolID = False, returnCodeDescription = False, returnCreatedTime = False, returnDistrictID = False, returnIsOverriddenForStudent = False, returnModifiedTime = False, returnOrder = False, returnOverriddenSchoolName = False, returnSchoolID = False, returnSchoolPathID = False, returnSchoolPathSchoolIDClonedFrom = False, returnSchoolPathSchoolIDClonedTo = False, returnSchoolYearID = False, returnStudentHasPermit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SchoolPathSchool in the district.

	This function returns a dataframe of every SchoolPathSchool in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathSchool/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathSchool/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySchoolPathSchoolOverride(searchConditions = [], EntityID = 1, returnSchoolPathSchoolOverrideID = False, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnSchoolID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SchoolPathSchoolOverride in the district.

	This function returns a dataframe of every SchoolPathSchoolOverride in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathSchoolOverride/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathSchoolOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySchoolPathStudent(searchConditions = [], EntityID = 1, returnSchoolPathStudentID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolPathID = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SchoolPathStudent in the district.

	This function returns a dataframe of every SchoolPathStudent in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathStudent/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathStudent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySchoolPathType(searchConditions = [], EntityID = 1, returnSchoolPathTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SchoolPathType in the district.

	This function returns a dataframe of every SchoolPathType in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentAccountsMA(searchConditions = [], EntityID = 1, returnStudentAccountsMAID = False, returnAMTransportationID = False, returnCreatedTime = False, returnEthnicityMAID = False, returnFacultyStaffChild = False, returnFinancialAid = False, returniPadLease = False, returnModifiedTime = False, returnNYDepositPaid = False, returnPaymentPlanMAID = False, returnPlaceofWorship = False, returnPMTransportationID = False, returnReligionID = False, returnSchoolDistrictID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentAccountsMA in the district.

	This function returns a dataframe of every StudentAccountsMA in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentAccountsMA/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentAccountsMA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentEntityYear(searchConditions = [], EntityID = 1, returnStudentEntityYearID = False, returnChromebookDocumentsReturned = False, returnCreatedTime = False, returnCurrentPercentEnrolled = False, returnDaysAbsentYTD = False, returnDaysEnrolledYTD = False, returnDaysExcusedYTD = False, returnDaysOtherYTD = False, returnDaysUnexcusedYTD = False, returnEntityID = False, returnEntryWithdrawalIDLatest = False, returnExcludeFromHonorRoll = False, returnExcludeFromRank = False, returnExistsConflictedStudentCourseRequests = False, returnExistsUnscheduleableStudentSections = False, returnFeeAmountDue = False, returnFeeChargeAmount = False, returnFeePaidAmount = False, returnFeePaidAndWaivedAmount = False, returnFeeUnappliedAmount = False, returnFeeWaivedAmount = False, returnFirstName = False, returnFlaggedMissingAssignmentsCount = False, returnGrade = False, returnHandbookSigned = False, returnHasActiveCareerPlanDeclarationTimePeriod = False, returnHasActiveEndorsementDeclarationTimePeriod = False, returnHasConflictedStudentCourseRequest = False, returnHasFlaggedMissingAssignments = False, returnHasMissingAssignments = False, returnHasNoAttendanceToday = False, returnHasNonCrossEntityCourseSchedulingEntryWithdrawal = False, returnHasOpenDisplayPeriodsInRegularSchoolDay = False, returnHasOverscheduledPeriod = False, returnHasValidStudentPlan = False, returnHomeroomCodeFollettDestiny = False, returnHomeroomID = False, returnHomeroomPeriodFollettDestiny = False, returnHomeroomStaffNameFollettDestiny = False, returnIncludeAsProspectiveRank = False, returnIsActive = False, returnIsCrossEntityCourseEnrollment = False, returnIsDefaultEntity = False, returnIsTransportationRequested = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNumberOfStudentCourseRequests = False, returnNumberOfStudentSections = False, returnOptOutOfMedia = False, returnSchedulingCategories = False, returnSchedulingTeamID = False, returnSchoolIDPathExpectedSchool = False, returnSchoolYearID = False, returnSectionLengthAbsent = False, returnSectionLengthEnrolled = False, returnSemester2Absent = False, returnSemester2Enrolled = False, returnSignedAcceptableUsePolicy = False, returnStaffIDAdvisor = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnTardyCountYTD = False, returnTardyKioskTotals = False, returnTotalEarnedCreditsPossibleAnticipatedNonTransferStudentSectionsNonAlternateRequestCredits = False, returnTotalMissedAssignmentCount = False, returnUILFeeReceived = False, returnUnscheduleableStudentSectionCount = False, returnUnscheduledStudentCourseRequestCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDate = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentEntityYear in the district.

	This function returns a dataframe of every StudentEntityYear in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentEntityYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentPermit(searchConditions = [], EntityID = 1, returnStudentPermitID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnPermitID = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentPermit in the district.

	This function returns a dataframe of every StudentPermit in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentPermit/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentPermit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentType(searchConditions = [], EntityID = 1, returnStudentTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentType in the district.

	This function returns a dataframe of every StudentType in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempAffectedWithdrawalRecord(searchConditions = [], EntityID = 1, returnTempAffectedWithdrawalRecordID = False, returnAction = False, returnActionCode = False, returnActionMessage = False, returnAffectedPrimaryKey = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHasAttendance = False, returnHasFutureAttendance = False, returnHasFutureGrades = False, returnHasGrades = False, returnHasPartiallyPaidFees = False, returnHasTransactionPreventingStudentSectionDelete = False, returnIsFutureEntryWithdrawal = False, returnModifiedTime = False, returnMostFutureGradeStartDate = False, returnNameIDRequestedBy = False, returnNewEndDate = False, returnParentPrimaryKey = False, returnRecordType = False, returnRecordTypeCode = False, returnSchoolYearID = False, returnSection = False, returnSectionID = False, returnStartDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempAffectedWithdrawalRecord in the district.

	This function returns a dataframe of every TempAffectedWithdrawalRecord in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempAffectedWithdrawalRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempAffectedWithdrawalRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempHomeroomError(searchConditions = [], EntityID = 1, returnTempHomeroomErrorID = False, returnCode = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnTempHomeroomRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempHomeroomError in the district.

	This function returns a dataframe of every TempHomeroomError in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempHomeroomRecord(searchConditions = [], EntityID = 1, returnTempHomeroomRecordID = False, returnBuilding = False, returnBuildingID = False, returnCode = False, returnColumnIndex = False, returnCreatedTime = False, returnHasSaveError = False, returnHomeroomID = False, returnIsOverwrite = False, returnModifiedTime = False, returnRoom = False, returnRoomID = False, returnSchoolYear = False, returnSchoolYearID = False, returnStaff = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempHomeroomRecord in the district.

	This function returns a dataframe of every TempHomeroomRecord in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempNameAddressMoveSchoolPathSchoolOverride(searchConditions = [], EntityID = 1, returnTempNameAddressMoveSchoolPathSchoolOverrideID = False, returnCreatedTime = False, returnIsCreateOverride = False, returnIsOverrideExists = False, returnIsRemoveOverride = False, returnIsRemovePermit = False, returnIsUpdateOverride = False, returnModifiedTime = False, returnOrder = False, returnPermitID = False, returnPermitSchoolYearID = False, returnSchoolID = False, returnSchoolNameOverriddingTo = False, returnSchoolNameToOverride = False, returnSchoolPathSchoolOverrideID = False, returnSchoolYearDescription = False, returnStudentFullNameLFM = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempNameAddressMoveSchoolPathSchoolOverride in the district.

	This function returns a dataframe of every TempNameAddressMoveSchoolPathSchoolOverride in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNameAddressMoveSchoolPathSchoolOverride/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNameAddressMoveSchoolPathSchoolOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempNoShowEntryWithdrawal(searchConditions = [], EntityID = 1, returnTempNoShowEntryWithdrawalID = False, returnAttemptToUpdateWithdrawalCode = False, returnCreatedTime = False, returnDisplayAction = False, returnDisplayActionCode = False, returnEndDate = False, returnEntity = False, returnEntryCode = False, returnEntryWithdrawalID = False, returnFailureReason = False, returnGradeLevel = False, returnModifiedTime = False, returnNoShowAction = False, returnNoShowActionCode = False, returnNoShowEntryWithdrawalType = False, returnNoShowEntryWithdrawalTypeCode = False, returnNoShowTypeOfNoShow = False, returnNoShowTypeOfNoShowCode = False, returnSchoolYear = False, returnSchoolYearID = False, returnStartDate = False, returnStudent = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCode = False, returnWithdrawalCodeID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempNoShowEntryWithdrawal in the district.

	This function returns a dataframe of every TempNoShowEntryWithdrawal in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNoShowEntryWithdrawal/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNoShowEntryWithdrawal/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempSchoolPathSchoolOverride(searchConditions = [], EntityID = 1, returnTempSchoolPathSchoolOverrideID = False, returnCreatedTime = False, returnDistrictID = False, returnExceptionNote = False, returnHasExceptions = False, returnModifiedTime = False, returnOrder = False, returnPermitCodeDescription = False, returnPermitID = False, returnSchoolCodeName = False, returnSchoolID = False, returnSchoolIDClonedTo = False, returnSchoolYearID = False, returnStudentID = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempSchoolPathSchoolOverride in the district.

	This function returns a dataframe of every TempSchoolPathSchoolOverride in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempSchoolPathSchoolOverride/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempSchoolPathSchoolOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentEnrollmentError(searchConditions = [], EntityID = 1, returnTempStudentEnrollmentErrorID = False, returnCreatedTime = False, returnError = False, returnErrorCount = False, returnErrorDetail = False, returnModifiedTime = False, returnTempStudentEnrollmentRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentEnrollmentError in the district.

	This function returns a dataframe of every TempStudentEnrollmentError in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentEnrollmentRecord(searchConditions = [], EntityID = 1, returnTempStudentEnrollmentRecordID = False, returnAdvisorFullName = False, returnCalendarCode = False, returnCalendarID = False, returnCompletedSchoolYearOverride = False, returnCreatedTime = False, returnCreateFeeManagementCustomer = False, returnCreateFeeManagementCustomerEntityYear = False, returnDisciplineOfficerFullName = False, returnEdFiDistrictIDResidence = False, returnEdFiDistrictIDTransfer = False, returnEdFiDistrictResidenceCodeDescription = False, returnEdFiSchoolIDTransfer = False, returnEndDate = False, returnEnrollIntoEntityCode = False, returnEnrollmentMoveable = False, returnEntityCode = False, returnEntityID = False, returnEntryCode = False, returnEntryCodeID = False, returnEntryComment = False, returnEntryWithdrawalID = False, returnError = False, returnErrorCount = False, returnExcludeFromHonorRoll = False, returnExcludeFromRank = False, returnExcludeFromThirdFridaySeptemberCount = False, returnFailureReason = False, returnFeeManagementCustomerID = False, returnGradeLevelCode = False, returnGradeReferenceID = False, returnGradYear = False, returnGSAADAClaimableOverrideCode = False, returnGSAADAClaimableOverrideCodeDisplayName = False, returnHomeroomCode = False, returnHomeroomID = False, returnIncludeAsProspectiveRank = False, returnIsCurrentActive = False, returnIsDefaultEntityForEntryWithdrawal = False, returnIsDefaultEntityForStudentEntityYear = False, returnIsPermanentExit = False, returnIsPrivateSchoolChoiceStudent = False, returnIsTuitionPaidOutOfDistrict = False, returnModifiedTime = False, returnNumericYear = False, returnOutgoingStudent = False, returnPercentEnrolled = False, returnProcessEntryWithdrawal = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnScheduledSectionCount = False, returnSchoolCode = False, returnSchoolID = False, returnSchoolYearID = False, returnServingRCDTSOverrideCode = False, returnServingRCDTSOverrideCodeDisplayName = False, returnServingRCDTSOverrideID = False, returnSourceEntryWithdrawalID = False, returnStaffIDAdvisor = False, returnStaffIDDisciplineOfficer = False, returnStartDate = False, returnStateAidCategoryMNID = False, returnStateDistrictMNCodeName = False, returnStateDistrictMNID = False, returnStateLastAttendanceLocationCodeMNID = False, returnStudentCourseRequestNotMoveableCount = False, returnStudentCourseRequestToDeleteCount = False, returnStudentFullName = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnStudentTypeID = False, returnTestingSchoolCode = False, returnTestingSchoolCodeDisplayName = False, returnTestingSchoolRCDTSOverrideCode = False, returnTestingSchoolRCDTSOverrideCodeDisplayName = False, returnTestingSchoolRCDTSOverrideID = False, returnTotalStudentCourseRequestCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCode = False, returnWithdrawalCodeID = False, returnWithdrawalComment = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentEnrollmentRecord in the district.

	This function returns a dataframe of every TempStudentEnrollmentRecord in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentEntityYear(searchConditions = [], EntityID = 1, returnTempStudentEntityYearID = False, returnAdvisorDetails = False, returnCreatedTime = False, returnCurrentAdvisorDetails = False, returnCurrentHomeroomDetails = False, returnGenderCode = False, returnGradeLevelCodeDescription = False, returnHomeroomDetails = False, returnHomeroomID = False, returnIsActive = False, returnMessage = False, returnModifiedTime = False, returnStaffIDAdvisor = False, returnStudentEntityYearID = False, returnStudentFullName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentEntityYear in the district.

	This function returns a dataframe of every TempStudentEntityYear in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEntityYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryWithdrawalCode(searchConditions = [], EntityID = 1, returnWithdrawalCodeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEdFiExitWithdrawID = False, returnIsCrossEntityCourseEnrollment = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateStatusEndCodeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeIDClonedFrom = False, returnWithdrawalCodeMNID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every WithdrawalCode in the district.

	This function returns a dataframe of every WithdrawalCode in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/WithdrawalCode/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/WithdrawalCode/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)