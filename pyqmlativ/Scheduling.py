# This module contains Scheduling functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryAppleSchoolManagerConfig(searchConditions = [], EntityID = 1, returnAppleSchoolManagerConfigID = False, returnAsOfDateSetting = False, returnAsOfDateSettingCode = False, returnCreatedTime = False, returnDistrictID = False, returnEntityIDSelectedList = False, returnExportUncPathOverride = False, returnFTPConnectionID = False, returnMediaID = False, returnModifiedTime = False, returnSaveToFtp = False, returnSchoolYearID = False, returnSpecifiedAsOfDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipFileName = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AppleSchoolManagerConfig in the district.

	This function returns a dataframe of every AppleSchoolManagerConfig in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AppleSchoolManagerConfig/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AppleSchoolManagerConfig/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAvailabilityCourseFilter(searchConditions = [], EntityID = 1, returnAvailabilityCourseFilterID = False, returnAvailabilityCourseFilterIDClonedFrom = False, returnAvailabilityCourseFilterIDClonedTo = False, returnCode = False, returnCodeDescription = False, returnCourseTypeIDInclusionList = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnFilter = False, returnGradeLevelFilterType = False, returnGradeLevelFilterTypeCode = False, returnGradeReferenceIDInclusionList = False, returnIncludeCategoryLunch = False, returnIncludeCategoryRegular = False, returnIncludeCategoryStudyHall = False, returnIncludeCoursesWithNoCourseType = False, returnIncludeElective = False, returnIncludeInactiveCourses = False, returnIncludeOfferedCourses = False, returnIncludeRequired = False, returnIncludeSchedulingTypeManuallyScheduled = False, returnIncludeSchedulingTypeNormal = False, returnIncludeSchedulingTypeSpecialEducation = False, returnModifiedTime = False, returnSchoolYearID = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AvailabilityCourseFilter in the district.

	This function returns a dataframe of every AvailabilityCourseFilter in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityCourseFilter/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityCourseFilter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAvailabilityFilterArenaSchedulingSetting(searchConditions = [], EntityID = 1, returnAvailabilityFilterArenaSchedulingSettingID = False, returnAutoSchedulerCourseSelection = False, returnAutoSchedulerCourseSelectionCode = False, returnAvailabilityFilterCourseStudentID = False, returnAvailableEndDate = False, returnAvailableStartDate = False, returnCreatedTime = False, returnEnableAutoSchedule = False, returnHideRoom = False, returnHideStaff = False, returnLockAfterSubmission = False, returnModifiedTime = False, returnSchedulingEntryEndDate = False, returnSchedulingEntryEndDateTime = False, returnSchedulingEntryEndTime = False, returnSchedulingEntryStartDate = False, returnSchedulingEntryStartDateTime = False, returnSchedulingEntryStartTime = False, returnShowAllClasses = False, returnShowMyAlternateRequests = False, returnShowMyRequests = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AvailabilityFilterArenaSchedulingSetting in the district.

	This function returns a dataframe of every AvailabilityFilterArenaSchedulingSetting in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityFilterArenaSchedulingSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityFilterArenaSchedulingSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAvailabilityFilterCourseRequestSetting(searchConditions = [], EntityID = 1, returnAvailabilityFilterCourseRequestSettingID = False, returnAvailabilityFilterCourseStudentID = False, returnAvailableEndDate = False, returnAvailableStartDate = False, returnCreatedTime = False, returnMaximumAlternateCourseRequests = False, returnMaximumAlternateCredits = False, returnMaximumCourseRequests = False, returnMaximumCredits = False, returnModifiedTime = False, returnRequestEntryEndDate = False, returnRequestEntryEndDateTime = False, returnRequestEntryEndTime = False, returnRequestEntryStartDate = False, returnRequestEntryStartDateTime = False, returnRequestEntryStartTime = False, returnUseCourseRequestCountMaximum = False, returnUseCreditsMaximum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AvailabilityFilterCourseRequestSetting in the district.

	This function returns a dataframe of every AvailabilityFilterCourseRequestSetting in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityFilterCourseRequestSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityFilterCourseRequestSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAvailabilityFilterCourseStudent(searchConditions = [], EntityID = 1, returnAvailabilityFilterCourseStudentID = False, returnArenaSchedulingStartDate = False, returnAvailabilityCourseFilterID = False, returnAvailabilityFilterCourseStudentIDClonedFrom = False, returnAvailabilityStudentFilterID = False, returnCourseRequestStartDate = False, returnCreatedTime = False, returnDescription = False, returnExcludeAvailabilityListBoolUpdatedManually = False, returnExcludeAvailabilityListInNightlyUpdateTask = False, returnModifiedTime = False, returnUseForArenaScheduling = False, returnUseForCourseRequests = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AvailabilityFilterCourseStudent in the district.

	This function returns a dataframe of every AvailabilityFilterCourseStudent in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityFilterCourseStudent/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityFilterCourseStudent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAvailabilityFilterCourseStudentCourse(searchConditions = [], EntityID = 1, returnAvailabilityFilterCourseStudentCourseID = False, returnAvailabilityFilterCourseStudentID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AvailabilityFilterCourseStudentCourse in the district.

	This function returns a dataframe of every AvailabilityFilterCourseStudentCourse in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityFilterCourseStudentCourse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityFilterCourseStudentCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAvailabilityFilterCourseStudentStudent(searchConditions = [], EntityID = 1, returnAvailabilityFilterCourseStudentStudentID = False, returnArenaSchedulingStatus = False, returnArenaSchedulingStatusCode = False, returnAvailabilityFilterCourseStudentID = False, returnCreatedTime = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AvailabilityFilterCourseStudentStudent in the district.

	This function returns a dataframe of every AvailabilityFilterCourseStudentStudent in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityFilterCourseStudentStudent/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityFilterCourseStudentStudent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAvailabilityStudentFilter(searchConditions = [], EntityID = 1, returnAvailabilityStudentFilterID = False, returnAvailabilityStudentFilterIDClonedFrom = False, returnAvailabilityStudentFilterIDClonedTo = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnFilter = False, returnGradeReferenceIDInclusionList = False, returnModifiedTime = False, returnSchoolYearID = False, returnSkywardID = False, returnStudentTypeIDInclusionList = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AvailabilityStudentFilter in the district.

	This function returns a dataframe of every AvailabilityStudentFilter in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityStudentFilter/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityStudentFilter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBaseRunAnalysis(searchConditions = [], EntityID = 1, returnBaseRunAnalysisID = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnRunType = False, returnRunTypeCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDPerformer = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BaseRunAnalysis in the district.

	This function returns a dataframe of every BaseRunAnalysis in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/BaseRunAnalysis/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/BaseRunAnalysis/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBlockPeriod(searchConditions = [], EntityID = 1, returnBlockPeriodID = False, returnBlockPeriodIDClonedFrom = False, returnBlockPeriodIDClonedTo = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnHasDisplayPeriods = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BlockPeriod in the district.

	This function returns a dataframe of every BlockPeriod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/BlockPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/BlockPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBlockPeriodDisplayPeriod(searchConditions = [], EntityID = 1, returnBlockPeriodDisplayPeriodID = False, returnBlockPeriodDisplayPeriodIDClonedFrom = False, returnBlockPeriodID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BlockPeriodDisplayPeriod in the district.

	This function returns a dataframe of every BlockPeriodDisplayPeriod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/BlockPeriodDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/BlockPeriodDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigEntityYear(searchConditions = [], EntityID = 1, returnConfigEntityYearID = False, returnArenaSchedulingConfirmationScreenMessage = False, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEnableArenaSchedulingConfirmationScreen = False, returnEnableValidationOfRoomCapacityDuringStudentSectionEnrollment = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ConfigEntityYear in the district.

	This function returns a dataframe of every ConfigEntityYear in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/ConfigEntityYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/ConfigEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourseAlternate(searchConditions = [], EntityID = 1, returnCourseAlternateID = False, returnCourseAlternateIDClonedFrom = False, returnCourseIDAlternate = False, returnCourseIDPrimary = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CourseAlternate in the district.

	This function returns a dataframe of every CourseAlternate in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseAlternate/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseAlternate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourseCorequisiteGroup(searchConditions = [], EntityID = 1, returnCourseCorequisiteGroupID = False, returnAutomaticRequestSetting = False, returnAutomaticRequestSettingCode = False, returnCourseCorequisiteGroupIDClonedFrom = False, returnCourseCorequisiteGroupIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnDisplayPeriodMatch = False, returnDisplayPeriodMatchCode = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnOverlap = False, returnOverlapCode = False, returnScheduleAllCoursesInGroupOrNone = False, returnSchoolYearID = False, returnStaffMatch = False, returnStaffMatchCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CourseCorequisiteGroup in the district.

	This function returns a dataframe of every CourseCorequisiteGroup in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseCorequisiteGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseCorequisiteGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourseCorequisiteGroupCourse(searchConditions = [], EntityID = 1, returnCourseCorequisiteGroupCourseID = False, returnCourseCorequisiteGroupCourseIDClonedFrom = False, returnCourseCorequisiteGroupID = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CourseCorequisiteGroupCourse in the district.

	This function returns a dataframe of every CourseCorequisiteGroupCourse in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseCorequisiteGroupCourse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseCorequisiteGroupCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourseCustomRequirement(searchConditions = [], EntityID = 1, returnCourseCustomRequirementID = False, returnCourseCustomRequirementIDClonedFrom = False, returnCourseID = False, returnCreatedTime = False, returnCustomRequirementID = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CourseCustomRequirement in the district.

	This function returns a dataframe of every CourseCustomRequirement in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseCustomRequirement/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseCustomRequirement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourseEntityOfferedTo(searchConditions = [], EntityID = 1, returnCourseEntityOfferedToID = False, returnActiveSections = False, returnActiveSectionsOpen = False, returnCourseCode = False, returnCourseEntityOfferedToIDClonedFrom = False, returnCourseEntityOfferedToIDClonedTo = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityIDOfferedTo = False, returnHasStudentCourseRequestsEntity = False, returnIsActive = False, returnIsAutoOffering = False, returnIsCurrentSchoolYearEntity = False, returnIsHomeCourse = False, returnIsOfferedCourse = False, returnIsRequired = False, returnIsRequiredOverride = False, returnModifiedTime = False, returnNumberOfAlternateCourseRequestsEntity = False, returnNumberOfCourseRequestsEntity = False, returnNumberOfCourseRequestsFemalesEntity = False, returnNumberOfCourseRequestsMalesEntity = False, returnNumberOfSeatsRemainingEntity = False, returnNumberTransferStudentSectionsEntity = False, returnRequired = False, returnSchedulingPriorityCode = False, returnSchedulingPriorityOverride = False, returnSchedulingPriorityOverrideCode = False, returnSchedulingTypeCode = False, returnSchedulingTypeOverride = False, returnSchedulingTypeOverrideCode = False, returnSchoolYearID = False, returnTotalSeatsAvailable = False, returnTotalSectionCountEntity = False, returnTotalStudentCourseRequestSectionLengthSubsetCountEntity = False, returnTotalStudentSectionCountEntity = False, returnUseIsRequiredOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSchedulingPriorityOverride = False, returnUseSchedulingTypeOverride = False, returnViewingFromOfferedEntity = False, returnViewingFromOfferingEntity = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CourseEntityOfferedTo in the district.

	This function returns a dataframe of every CourseEntityOfferedTo in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedTo/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedTo/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourseEntityOfferedToSection(searchConditions = [], EntityID = 1, returnCourseEntityOfferedToSectionID = False, returnCourseEntityOfferedToID = False, returnCourseEntityOfferedToSectionIDClonedFrom = False, returnCourseEntityOfferedToSectionIDClonedTo = False, returnCourseID = False, returnCreatedTime = False, returnEntityIDOfferedTo = False, returnHasMeetDisplayPeriodOverrides = False, returnIsActive = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnRoomSeatsAvailable = False, returnSchoolYearID = False, returnSeatsAvailableEntity = False, returnSectionID = False, returnStudentEnrollmentEntity = False, returnTotalEnrollmentCountEntity = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferedEntity = False, returnViewingFromOfferingEntity = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CourseEntityOfferedToSection in the district.

	This function returns a dataframe of every CourseEntityOfferedToSection in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedToSection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedToSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourseEntityOfferedToSectionMeet(searchConditions = [], EntityID = 1, returnCourseEntityOfferedToSectionMeetID = False, returnCourseEntityOfferedToSectionID = False, returnCourseEntityOfferedToSectionMeetIDClonedFrom = False, returnCreatedTime = False, returnEntityIDOfferedTo = False, returnMeetID = False, returnModifiedTime = False, returnRoomID = False, returnSchoolYearID = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CourseEntityOfferedToSectionMeet in the district.

	This function returns a dataframe of every CourseEntityOfferedToSectionMeet in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedToSectionMeet/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedToSectionMeet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourseEntityOfferedToSectionMeetDisplayPeriod(searchConditions = [], EntityID = 1, returnCourseEntityOfferedToSectionMeetDisplayPeriodID = False, returnCourseEntityOfferedToSectionID = False, returnCourseEntityOfferedToSectionMeetDisplayPeriodIDClonedFrom = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnHideMeetDisplayPeriod = False, returnIsPrimary = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CourseEntityOfferedToSectionMeetDisplayPeriod in the district.

	This function returns a dataframe of every CourseEntityOfferedToSectionMeetDisplayPeriod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedToSectionMeetDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedToSectionMeetDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourseEntityOfferedToSectionStaffMeet(searchConditions = [], EntityID = 1, returnCourseEntityOfferedToSectionStaffMeetID = False, returnCourseEntityOfferedToSectionID = False, returnCourseEntityOfferedToSectionStaffMeetIDClonedFrom = False, returnCreatedTime = False, returnMeetID = False, returnModifiedTime = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CourseEntityOfferedToSectionStaffMeet in the district.

	This function returns a dataframe of every CourseEntityOfferedToSectionStaffMeet in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedToSectionStaffMeet/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedToSectionStaffMeet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourseGradeReference(searchConditions = [], EntityID = 1, returnCourseGradeReferenceID = False, returnCourseGradeReferenceIDClonedFrom = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNumberOfAlternateCourseRequests = False, returnNumberOfAlternateCourseRequestsEntity = False, returnNumberOfCourseRequests = False, returnNumberOfCourseRequestsEntity = False, returnNumberOfCourseRequestsFemales = False, returnNumberOfCourseRequestsFemalesEntity = False, returnNumberOfCourseRequestsMales = False, returnNumberOfCourseRequestsMalesEntity = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CourseGradeReference in the district.

	This function returns a dataframe of every CourseGradeReference in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseGradeReference/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseGradeReference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourseGradeReferenceSummary(searchConditions = [], EntityID = 1, returnCourseID = False, returnGradeLevelIDSummary = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CourseGradeReferenceSummary in the district.

	This function returns a dataframe of every CourseGradeReferenceSummary in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseGradeReferenceSummary/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseGradeReferenceSummary/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourseGroup(searchConditions = [], EntityID = 1, returnCourseGroupID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CourseGroup in the district.

	This function returns a dataframe of every CourseGroup in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourseGroupCourse(searchConditions = [], EntityID = 1, returnCourseGroupCourseID = False, returnCourseGroupCourseIDClonedFrom = False, returnCourseGroupID = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CourseGroupCourse in the district.

	This function returns a dataframe of every CourseGroupCourse in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseGroupCourse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseGroupCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourseLength(searchConditions = [], EntityID = 1, returnCourseLengthID = False, returnCode = False, returnCodeDescription = False, returnCourseLengthIDClonedFrom = False, returnCourseLengthIDClonedTo = False, returnCreatedTime = False, returnDefaultEarnedCredits = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionLengthCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CourseLength in the district.

	This function returns a dataframe of every CourseLength in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseLength/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseLength/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourseLevelMN(searchConditions = [], EntityID = 1, returnCourseLevelMNID = False, returnCode = False, returnCreatedTime = False, returnCredits = False, returnCurriculumYearID = False, returnInstitutionID = False, returnModifiedTime = False, returnStateCollegeCourseLevelMNID = False, returnTitle = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CourseLevelMN in the district.

	This function returns a dataframe of every CourseLevelMN in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseLevelMN/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseLevelMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourseMasterMassUpdate(searchConditions = [], EntityID = 1, returnCourseMasterMassUpdateID = False, returnCreatedTime = False, returnEntityID = False, returnFilterParameters = False, returnModifiedTime = False, returnRunReason = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRanBy = False, returnValueParameters = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CourseMasterMassUpdate in the district.

	This function returns a dataframe of every CourseMasterMassUpdate in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseMasterMassUpdate/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseMasterMassUpdate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourse(searchConditions = [], EntityID = 1, returnCourseID = False, returnAcademicMinutes = False, returnActiveSections = False, returnActiveSectionsOpen = False, returnActivityID = False, returnAllowTeachersToAddAssignments = False, returnCanBeOfferedToAnotherEntity = False, returnCategory = False, returnCategoryCode = False, returnCodeDescription = False, returnCourseCloned = False, returnCourseCode = False, returnCourseGradeLevelCodes = False, returnCourseGroupDescriptions = False, returnCourseIDClonedFrom = False, returnCourseIDClonedTo = False, returnCourseIDHash = False, returnCourseLengthID = False, returnCourseMNID = False, returnCourseSubjectID = False, returnCourseTypeID = False, returnCreatedTime = False, returnCurriculumID = False, returnDepartmentID = False, returnDescription = False, returnEarnedCredits = False, returnEdFiCourseLevelCharacteristicID = False, returnEdFiSubjectTypeID = False, returnEntityGroupKey = False, returnEntityID = False, returnEstimatedNumberOfSections = False, returnExcludeFromSTAR = False, returnExcludeFromStudentSectionLink = False, returnGradeCourse = False, returnGradeLevelIDSummary = False, returnGradeLevelSummary = False, returnGradingPeriodSetID = False, returnHasAttachedStandards = False, returnHasCourseRequestsInCommonWithCourse = False, returnHasNonAlternateStudentCourseRequests = False, returnHasOfferedCourseEntity = False, returnHasStudentCourseRequests = False, returnHasSubjects = False, returnHideFromArenaScheduling = False, returnHideFromRequestEntry = False, returnIsActive = False, returnIsActiveForEntity = False, returnIsAHistoricRecord = False, returnIsCoreAcademic = False, returnIsCurrentSchoolYear = False, returnIsDirectPay = False, returnIsHonors = False, returnIsOffered = False, returnIsRepeatable = False, returnIsRequired = False, returnIsRequiredOverride = False, returnIsWritingEmphasis = False, returnKeepAttendance = False, returnLengthOfPeriod = False, returnLockCourseFromSectionScheduler = False, returnMaximumPercentageOfSectionsInSingleDisplayPeriod = False, returnMaxRequestedCount = False, returnModifiedTime = False, returnNumberOfAlternateCourseRequests = False, returnNumberOfCourseRequests = False, returnNumberOfCourseRequestsFemales = False, returnNumberOfCourseRequestsInCommonWithCourse = False, returnNumberOfCourseRequestsMales = False, returnNumberOfSeatsAvailable = False, returnNumberOfSeatsRemaining = False, returnNumberOfTransferStudentSections = False, returnOfferingEntity = False, returnOverrideStudentSectionLinkByCourse = False, returnPeriodsPerWeek = False, returnPreventDrop = False, returnPreventMultipleSectionsUsingSingleDisplayPeriod = False, returnRequestLimitPerStudent = False, returnRequired = False, returnSchedulingPriority = False, returnSchedulingPriorityCode = False, returnSchedulingPriorityCodeOverride = False, returnSchedulingPriorityOverride = False, returnSchedulingTeamMode = False, returnSchedulingTeamModeCode = False, returnSchedulingType = False, returnSchedulingTypeCode = False, returnSchedulingTypeCodeOverride = False, returnSchedulingTypeOverride = False, returnSchoolYearID = False, returnSectionSchedulerManualProcessingOrder = False, returnSequenceLimit = False, returnSequenceNumber = False, returnSpecificStudentRequests = False, returnStateCarlPerkinsProgramCodeMNID = False, returnStateSTARAssignmentCodeMNID = False, returnStateSTARGradeLevelMNID = False, returnSumTotalActiveSectionsOptimalStudentCount = False, returnTotalEntitiesOfferedTo = False, returnTotalSectionCount = False, returnTotalStudentCourseRequestSectionLengthSubsetCount = False, returnTotalStudentSectionCount = False, returnUseRequiredOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSchedulingPriorityOverride = False, returnUseSchedulingTypeOverride = False, returnViewingFromOfferingEntity = False, returnWebsite = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Course in the district.

	This function returns a dataframe of every Course in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/Course/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/Course/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCoursePrerequisite(searchConditions = [], EntityID = 1, returnCoursePrerequisiteID = False, returnCourseID = False, returnCurriculumCode = False, returnCurriculumDescription = False, returnCurriculumID = False, returnEarnedCredits = False, returnEntityID = False, returnHasPrequisiteCurriculums = False, returnNumericYearCourse = False, returnNumericYearCurrent = False, returnPrerequisiteCode = False, returnPrerequisiteID = False, returnSchoolYearHigh = False, returnSchoolYearID = False, returnSchoolYearLow = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CoursePrerequisite in the district.

	This function returns a dataframe of every CoursePrerequisite in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CoursePrerequisite/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CoursePrerequisite/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCoursePrerequisiteCurriculumCourse(searchConditions = [], EntityID = 1, returnCoursePrerequisiteCurriculumCourseID = False, returnCourseIDFor = False, returnCourseIDRequired = False, returnCurriculumIDFor = False, returnCurriculumIDRequired = False, returnEntityIDFor = False, returnEntityIDRequired = False, returnNumericYearCourse = False, returnNumericYearCurrentFor = False, returnNumericYearRequired = False, returnPrerequisiteCurriculumID = False, returnPrerequisiteID = False, returnSchoolYearIDFor = False, returnSchoolYearIDRequired = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CoursePrerequisiteCurriculumCourse in the district.

	This function returns a dataframe of every CoursePrerequisiteCurriculumCourse in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CoursePrerequisiteCurriculumCourse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CoursePrerequisiteCurriculumCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCoursePrerequisiteCurriculumCourseStudentCourseRequest(searchConditions = [], EntityID = 1, returnCoursePrerequisiteCurriculumCourseStudentCourseRequestID = False, returnCourseIDFor = False, returnCourseIDRequired = False, returnCurriculumIDFor = False, returnCurriculumIDRequired = False, returnPrerequisiteID = False, returnStatus = False, returnStatusCode = False, returnStudentCourseRequestID = False, returnStudentID = False, returnStudentSectionID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CoursePrerequisiteCurriculumCourseStudentCourseRequest in the district.

	This function returns a dataframe of every CoursePrerequisiteCurriculumCourseStudentCourseRequest in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CoursePrerequisiteCurriculumCourseStudentCourseRequest/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CoursePrerequisiteCurriculumCourseStudentCourseRequest/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourseSectionLengthExclude(searchConditions = [], EntityID = 1, returnCourseSectionLengthExcludeID = False, returnCourseID = False, returnCreatedTime = False, returnDistributionPercent = False, returnEntityGroupKey = False, returnModifiedTime = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CourseSectionLengthExclude in the district.

	This function returns a dataframe of every CourseSectionLengthExclude in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseSectionLengthExclude/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseSectionLengthExclude/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourseSubject(searchConditions = [], EntityID = 1, returnCourseSubjectID = False, returnCode = False, returnCodeDescription = False, returnCourseSubjectIDClonedFrom = False, returnCourseSubjectIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CourseSubject in the district.

	This function returns a dataframe of every CourseSubject in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseSubject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseSubject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourseType(searchConditions = [], EntityID = 1, returnCourseTypeID = False, returnCode = False, returnCodeDescription = False, returnCourseTypeIDClonedFrom = False, returnCourseTypeIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CourseType in the district.

	This function returns a dataframe of every CourseType in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCustomRequirement(searchConditions = [], EntityID = 1, returnCustomRequirementID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnStudentCondition = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CustomRequirement in the district.

	This function returns a dataframe of every CustomRequirement in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CustomRequirement/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CustomRequirement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDateRangePreset(searchConditions = [], EntityID = 1, returnDateRangePresetID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDateRangePresetIDClonedFrom = False, returnDateRangePresetIDClonedTo = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnHighDate = False, returnLowDate = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DateRangePreset in the district.

	This function returns a dataframe of every DateRangePreset in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DateRangePreset/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DateRangePreset/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDayRotation(searchConditions = [], EntityID = 1, returnDayRotationID = False, returnCode = False, returnConsecutiveTeachingHourLimit = False, returnCreatedTime = False, returnDayRotationIDClonedFrom = False, returnDayRotationIDClonedTo = False, returnEntityGroupKey = False, returnEntityID = False, returnMaximumTeachingHourLimit = False, returnModifiedTime = False, returnSchoolYearID = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DayRotation in the district.

	This function returns a dataframe of every DayRotation in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DayRotation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DayRotation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDisplayPeriod(searchConditions = [], EntityID = 1, returnDisplayPeriodID = False, returnAttendancePeriodID = False, returnCode = False, returnCodeDescription = False, returnCodeDescriptionDayRotation = False, returnCreatedTime = False, returnDayRotationID = False, returnDescription = False, returnDisplayPeriodCodeDayRotationCode = False, returnDisplayPeriodEndTime = False, returnDisplayPeriodIDClonedFrom = False, returnDisplayPeriodIDClonedTo = False, returnDisplayPeriodStartTime = False, returnEntityGroupKey = False, returnIsLunchPeriod = False, returnIsOutsideRegularSchoolDay = False, returnModifiedTime = False, returnSortNumber = False, returnTeachingHourEquivalent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DisplayPeriod in the district.

	This function returns a dataframe of every DisplayPeriod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDisplayPeriodConflict(searchConditions = [], EntityID = 1, returnDisplayPeriodConflictID = False, returnCreatedTime = False, returnDisplayPeriodIDBase = False, returnDisplayPeriodIDConflicting = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DisplayPeriodConflict in the district.

	This function returns a dataframe of every DisplayPeriodConflict in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DisplayPeriodConflict/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DisplayPeriodConflict/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDisplayPeriodRotation(searchConditions = [], EntityID = 1, returnDisplayPeriodRotationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayPeriodRotationIDClonedFrom = False, returnDisplayPeriodRotationIDClonedTo = False, returnDisplayPeriodSummary = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DisplayPeriodRotation in the district.

	This function returns a dataframe of every DisplayPeriodRotation in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DisplayPeriodRotation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DisplayPeriodRotation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDisplayPeriodRotationDisplayPeriod(searchConditions = [], EntityID = 1, returnDisplayPeriodRotationDisplayPeriodID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnDisplayPeriodRotationDisplayPeriodIDClonedFrom = False, returnDisplayPeriodRotationID = False, returnHideMeetDisplayPeriod = False, returnIsPrimary = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DisplayPeriodRotationDisplayPeriod in the district.

	This function returns a dataframe of every DisplayPeriodRotationDisplayPeriod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DisplayPeriodRotationDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DisplayPeriodRotationDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEarlyExitReason(searchConditions = [], EntityID = 1, returnEarlyExitReasonID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEarlyExitReasonIDClonedFrom = False, returnEntityGroupKey = False, returnEntityID = False, returnIsConsideredDrop = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EarlyExitReason in the district.

	This function returns a dataframe of every EarlyExitReason in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/EarlyExitReason/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/EarlyExitReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMassPrintStudentScheduleRunHistory(searchConditions = [], EntityID = 1, returnMassPrintStudentScheduleRunHistoryID = False, returnCreatedTime = False, returnEntityID = False, returnMediaID = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnRequestIdentifier = False, returnRunDescription = False, returnSchoolYearID = False, returnSendMessageOnComplete = False, returnStudentSelectType = False, returnStudentSelectTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MassPrintStudentScheduleRunHistory in the district.

	This function returns a dataframe of every MassPrintStudentScheduleRunHistory in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MassPrintStudentScheduleRunHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MassPrintStudentScheduleRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMassUpdateSystemDateRunHistory(searchConditions = [], EntityID = 1, returnMassUpdateSystemDateRunHistoryID = False, returnCreatedTime = False, returnDateTemplateXML = False, returnDuration = False, returnEndTime = False, returnEntityID = False, returnErrorCount = False, returnHasErrors = False, returnLocation = False, returnLocationCode = False, returnModifiedTime = False, returnRunDescription = False, returnRunReason = False, returnSchoolYearID = False, returnSourceID = False, returnStartTime = False, returnUpdateSuccessful = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MassUpdateSystemDateRunHistory in the district.

	This function returns a dataframe of every MassUpdateSystemDateRunHistory in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MassUpdateSystemDateRunHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MassUpdateSystemDateRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMassUpdateSystemDateRunHistoryDetail(searchConditions = [], EntityID = 1, returnMassUpdateSystemDateRunHistoryDetailID = False, returnCreatedTime = False, returnEndDateFailedCount = False, returnEndDateRecordsProcessedCount = False, returnEndDateSuccessCount = False, returnMassUpdateSystemDateRunHistoryID = False, returnModifiedTime = False, returnSortNumber = False, returnStartDateFailedCount = False, returnStartDateRecordsProcessedCount = False, returnStartDateSuccessCount = False, returnTableType = False, returnTableTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MassUpdateSystemDateRunHistoryDetail in the district.

	This function returns a dataframe of every MassUpdateSystemDateRunHistoryDetail in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MassUpdateSystemDateRunHistoryDetail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MassUpdateSystemDateRunHistoryDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMassUpdateSystemDateRunHistoryError(searchConditions = [], EntityID = 1, returnMassUpdateSystemDateRunHistoryErrorID = False, returnCreatedTime = False, returnDescription = False, returnErrorDetail = False, returnMassUpdateSystemDateRunHistoryID = False, returnModifiedTime = False, returnObjectID = False, returnParentObjectID = False, returnTableType = False, returnTableTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MassUpdateSystemDateRunHistoryError in the district.

	This function returns a dataframe of every MassUpdateSystemDateRunHistoryError in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MassUpdateSystemDateRunHistoryError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MassUpdateSystemDateRunHistoryError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMaximumTeachingHourOverride(searchConditions = [], EntityID = 1, returnMaximumTeachingHourOverrideID = False, returnCreatedTime = False, returnDayRotationID = False, returnMaximumConsecutiveTeachingHours = False, returnMaximumTeachingHourOverrideIDClonedFrom = False, returnMaximumTotalTeachingHours = False, returnModifiedTime = False, returnStaffEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MaximumTeachingHourOverride in the district.

	This function returns a dataframe of every MaximumTeachingHourOverride in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MaximumTeachingHourOverride/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MaximumTeachingHourOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMCCCTermGradeBucketMN(searchConditions = [], EntityID = 1, returnMCCCTermGradeBucketMNID = False, returnCreatedTime = False, returnGradeBucketID = False, returnMCCCTermImportID = False, returnModifiedTime = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MCCCTermGradeBucketMN in the district.

	This function returns a dataframe of every MCCCTermGradeBucketMN in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MCCCTermGradeBucketMN/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MCCCTermGradeBucketMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMeet(searchConditions = [], EntityID = 1, returnMeetID = False, returnCalendarIDStaff = False, returnCreatedTime = False, returnDisplayPeriodRotationID = False, returnDurationInMinutes = False, returnEndDate = False, returnEntityID = False, returnHasDisplayPeriodRotationAssigned = False, returnIsAssignedToAHomeroomRoom = False, returnIsPrimary = False, returnLockAllMeetDayRotationsFromSectionScheduler = False, returnLockAllMeetDisplayPeriodsFromSectionScheduler = False, returnLockAllStaffMeetsFromSectionScheduler = False, returnLockRoomFromSectionScheduler = False, returnMeetIDClonedFrom = False, returnMeetIDClonedTo = False, returnModifiedTime = False, returnOverridePeriodEndTime = False, returnOverridePeriodStartTime = False, returnRoomID = False, returnRoomSeatsAvailable = False, returnSchoolYearID = False, returnSectionID = False, returnStartDate = False, returnStartDateEndDateBuildingCodeRoomNumber = False, returnTotalMeetDisplayPeriodCount = False, returnTotalStaffMeetCount = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Meet in the district.

	This function returns a dataframe of every Meet in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/Meet/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/Meet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMeetDisplayPeriod(searchConditions = [], EntityID = 1, returnMeetDisplayPeriodID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnHideMeetDisplayPeriod = False, returnIsPrimary = False, returnLockDisplayPeriod = False, returnMeetDisplayPeriodEndTime = False, returnMeetDisplayPeriodIDClonedFrom = False, returnMeetDisplayPeriodStartTime = False, returnMeetID = False, returnModifiedTime = False, returnScheduledBySectionScheduler = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MeetDisplayPeriod in the district.

	This function returns a dataframe of every MeetDisplayPeriod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMeetEntityRoomPeriod(searchConditions = [], EntityID = 1, returnMeetID = False, returnCalendarID = False, returnDisplayPeriodID = False, returnEndDate = False, returnEntityIDCourse = False, returnEntityIDFor = False, returnEntityIDViewingCalculated = False, returnEntityIDViewingMeetSummary = False, returnIsDefaultCalendar = False, returnMeetSummaryID = False, returnRoomID = False, returnSchedulingPeriodID = False, returnSchoolYearID = False, returnSectionID = False, returnStartDate = False, returnUseRoomOverride = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MeetEntityRoomPeriod in the district.

	This function returns a dataframe of every MeetEntityRoomPeriod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetEntityRoomPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetEntityRoomPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMeetEntityRoomPeriodDateSeatsAvailable(searchConditions = [], EntityID = 1, returnMeetID = False, returnCalendarID = False, returnDate = False, returnDisplayPeriodID = False, returnEndDate = False, returnEntityIDCourse = False, returnEntityIDFor = False, returnEntityIDViewingCalculated = False, returnEntityIDViewingMeetSummary = False, returnIsOfferedMeet = False, returnMaxSeats = False, returnMaxSeatsMeet = False, returnMaxSeatsMeetOverride = False, returnMeetSummaryID = False, returnRoomID = False, returnRoomIDMeet = False, returnRoomIDMeetOverride = False, returnRoomSeatsAvailable = False, returnSchedulingPeriodID = False, returnSchoolYearID = False, returnSectionID = False, returnStartDate = False, returnUseRoomOverride = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MeetEntityRoomPeriodDateSeatsAvailable in the district.

	This function returns a dataframe of every MeetEntityRoomPeriodDateSeatsAvailable in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetEntityRoomPeriodDateSeatsAvailable/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetEntityRoomPeriodDateSeatsAvailable/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMeetRequirement(searchConditions = [], EntityID = 1, returnMeetRequirementID = False, returnAllowMultiplePeriodsPerDayRotation = False, returnCourseID = False, returnCreatedTime = False, returnDaysPerRotation = False, returnForceConsecutivePeriods = False, returnMeetRequirementIDClonedFrom = False, returnMeetRequirementIDClonedTo = False, returnMinutesPerDay = False, returnModifiedTime = False, returnTimeSpanAnalysisType = False, returnTimeSpanAnalysisTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MeetRequirement in the district.

	This function returns a dataframe of every MeetRequirement in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetRequirement/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetRequirement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMeetSummary(searchConditions = [], EntityID = 1, returnMeetSummaryID = False, returnCalculatedDays = False, returnCalculatedDaysStudent = False, returnCalculatedPeriod = False, returnCalculatedPeriodStudent = False, returnCalendarID = False, returnCreatedTime = False, returnDays = False, returnEntityIDViewing = False, returnHasOnlyHiddenDetails = False, returnIsDefaultCalendar = False, returnIsPrimary = False, returnMeetID = False, returnModifiedTime = False, returnPeriod = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MeetSummary in the district.

	This function returns a dataframe of every MeetSummary in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetSummary/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetSummary/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMeetSummaryDetail(searchConditions = [], EntityID = 1, returnMeetSummaryDetailID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnIsPrimary = False, returnMeetSummaryID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MeetSummaryDetail in the district.

	This function returns a dataframe of every MeetSummaryDetail in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetSummaryDetail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetSummaryDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryOpenPeriodAnalysis(searchConditions = [], EntityID = 1, returnOpenPeriodAnalysisID = False, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDPerformer = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every OpenPeriodAnalysis in the district.

	This function returns a dataframe of every OpenPeriodAnalysis in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/OpenPeriodAnalysis/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/OpenPeriodAnalysis/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryOpenPeriodAnalysisStudent(searchConditions = [], EntityID = 1, returnOpenPeriodAnalysisStudentID = False, returnCreatedTime = False, returnFirstName = False, returnGradeLevelCode = False, returnIsActive = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnOpenPeriodAnalysisID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every OpenPeriodAnalysisStudent in the district.

	This function returns a dataframe of every OpenPeriodAnalysisStudent in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/OpenPeriodAnalysisStudent/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/OpenPeriodAnalysisStudent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPrerequisiteCurriculumCourse(searchConditions = [], EntityID = 1, returnPrerequisiteCurriculumCourseID = False, returnCourseID = False, returnCurriculumIDFor = False, returnCurriculumIDRequired = False, returnEntityID = False, returnNumericYear = False, returnPrerequisiteCurriculumID = False, returnPrerequisiteID = False, returnSchoolYearID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PrerequisiteCurriculumCourse in the district.

	This function returns a dataframe of every PrerequisiteCurriculumCourse in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/PrerequisiteCurriculumCourse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/PrerequisiteCurriculumCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryProcessRestriction(searchConditions = [], EntityID = 1, returnProcessRestrictionID = False, returnCreatedTime = False, returnEntityID = False, returnLockCourseMaster = False, returnLockCourseMasterSetByMassStudentSchedulerUtility = False, returnLockMassStudentSchedulerUtility = False, returnLockMassStudentSchedulerUtilitySetByMassStudentSchedulerUtility = False, returnLockMassUnscheduleStudentSectionsUtility = False, returnLockMassUnscheduleStudentSectionsUtilitySetByMassStudentSchedulerUtility = False, returnLockSchedulingBoard = False, returnLockSchedulingBoardSetByMassStudentSchedulerUtility = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDLockCourseMasterPerformer = False, returnUserIDLockMassStudentSchedulerUtilityPerformer = False, returnUserIDLockMassUnscheduleStudentSectionsUtilityPerformer = False, returnUserIDLockSchedulingBoardPerformer = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ProcessRestriction in the district.

	This function returns a dataframe of every ProcessRestriction in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/ProcessRestriction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/ProcessRestriction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryQueuedStudentSection(searchConditions = [], EntityID = 1, returnQueuedStudentSectionID = False, returnCreatedTime = False, returnIsComplete = False, returnModifiedTime = False, returnSourceProcess = False, returnSourceProcessCode = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every QueuedStudentSection in the district.

	This function returns a dataframe of every QueuedStudentSection in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/QueuedStudentSection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/QueuedStudentSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryScheduleRestorePoint(searchConditions = [], EntityID = 1, returnScheduleRestorePointID = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnReportQueueID = False, returnRestorePointDateTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ScheduleRestorePoint in the district.

	This function returns a dataframe of every ScheduleRestorePoint in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/ScheduleRestorePoint/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/ScheduleRestorePoint/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySchedulingBoardFilter(searchConditions = [], EntityID = 1, returnSchedulingBoardFilterID = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SchedulingBoardFilter in the district.

	This function returns a dataframe of every SchedulingBoardFilter in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingBoardFilter/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingBoardFilter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySchedulingCategory(searchConditions = [], EntityID = 1, returnSchedulingCategoryID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchedulingCategoryIDClonedFrom = False, returnSchedulingCategoryIDClonedTo = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SchedulingCategory in the district.

	This function returns a dataframe of every SchedulingCategory in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingCategory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySchedulingGroup(searchConditions = [], EntityID = 1, returnSchedulingGroupID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnGradeReferenceID = False, returnHomeroomID = False, returnModifiedTime = False, returnSchedulingGroupIDClonedFrom = False, returnSchedulingGroupIDClonedTo = False, returnSchoolYearID = False, returnTotalSchedulingGroupCoursesCount = False, returnTotalSchedulingGroupSectionsCount = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SchedulingGroup in the district.

	This function returns a dataframe of every SchedulingGroup in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySchedulingGroupCourse(searchConditions = [], EntityID = 1, returnSchedulingGroupCourseID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingGroupCourseIDClonedFrom = False, returnSchedulingGroupCourseIDClonedTo = False, returnSchedulingGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SchedulingGroupCourse in the district.

	This function returns a dataframe of every SchedulingGroupCourse in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingGroupCourse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingGroupCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySchedulingGroupSection(searchConditions = [], EntityID = 1, returnSchedulingGroupSectionID = False, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingGroupID = False, returnSchedulingGroupSectionIDClonedFrom = False, returnSchedulingGroupSectionIDClonedTo = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SchedulingGroupSection in the district.

	This function returns a dataframe of every SchedulingGroupSection in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingGroupSection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingGroupSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySchedulingPeriod(searchConditions = [], EntityID = 1, returnSchedulingPeriodID = False, returnCodeNumber = False, returnCreatedTime = False, returnDayRotationID = False, returnDynamicRelationshipID = False, returnEntityGroupKey = False, returnModifiedTime = False, returnSchedulingPeriodIDClonedFrom = False, returnSchedulingPeriodIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SchedulingPeriod in the district.

	This function returns a dataframe of every SchedulingPeriod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySchedulingPeriodDisplayPeriod(searchConditions = [], EntityID = 1, returnSchedulingPeriodDisplayPeriodID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnEntityGroupKey = False, returnLabel = False, returnModifiedTime = False, returnSchedulingPeriodDisplayPeriodIDClonedFrom = False, returnSchedulingPeriodID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SchedulingPeriodDisplayPeriod in the district.

	This function returns a dataframe of every SchedulingPeriodDisplayPeriod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingPeriodDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingPeriodDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySchedulingTeam(searchConditions = [], EntityID = 1, returnSchedulingTeamID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchedulingTeamIDClonedFrom = False, returnSchedulingTeamIDClonedTo = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SchedulingTeam in the district.

	This function returns a dataframe of every SchedulingTeam in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingTeam/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingTeam/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySchedulingTeamGradeReference(searchConditions = [], EntityID = 1, returnSchedulingTeamGradeReferenceID = False, returnCreatedTime = False, returnGradeReferenceID = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnSchedulingTeamGradeReferenceIDClonedFrom = False, returnSchedulingTeamID = False, returnStudentEntityYearsCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SchedulingTeamGradeReference in the district.

	This function returns a dataframe of every SchedulingTeamGradeReference in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingTeamGradeReference/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingTeamGradeReference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionCorequisiteGroup(searchConditions = [], EntityID = 1, returnSectionCorequisiteGroupID = False, returnAutomaticRequestSetting = False, returnAutomaticRequestSettingCode = False, returnAutomaticScheduleSetting = False, returnAutomaticScheduleSettingCode = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnScheduleAllSectionsInGroupOrNone = False, returnSectionCorequisiteGroupIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionCorequisiteGroup in the district.

	This function returns a dataframe of every SectionCorequisiteGroup in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionCorequisiteGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionCorequisiteGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionCorequisiteGroupSection(searchConditions = [], EntityID = 1, returnSectionCorequisiteGroupSectionID = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionCorequisiteGroupID = False, returnSectionCorequisiteGroupSectionIDClonedFrom = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionCorequisiteGroupSection in the district.

	This function returns a dataframe of every SectionCorequisiteGroupSection in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionCorequisiteGroupSection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionCorequisiteGroupSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionCustomRequirement(searchConditions = [], EntityID = 1, returnSectionCustomRequirementID = False, returnCreatedTime = False, returnCustomRequirementID = False, returnModifiedTime = False, returnSectionCustomRequirementIDClonedFrom = False, returnSectionCustomRequirementIDClonedTo = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionCustomRequirement in the district.

	This function returns a dataframe of every SectionCustomRequirement in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionCustomRequirement/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionCustomRequirement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionDefault(searchConditions = [], EntityID = 1, returnSectionDefaultID = False, returnCourseID = False, returnCreatedTime = False, returnMaximumStudentCount = False, returnMinimumStudentCount = False, returnModifiedTime = False, returnOptimalStudentCount = False, returnSectionDefaultIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionDefault in the district.

	This function returns a dataframe of every SectionDefault in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionEnrollmentTotalForSectionLengthSubset(searchConditions = [], EntityID = 1, returnSectionID = False, returnSectionLengthSubsetID = False, returnTotalEnrollmentCount = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionEnrollmentTotalForSectionLengthSubset in the district.

	This function returns a dataframe of every SectionEnrollmentTotalForSectionLengthSubset in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionEnrollmentTotalForSectionLengthSubset/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionEnrollmentTotalForSectionLengthSubset/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionEnrollmentTotalForSectionLengthSubsetAndEntity(searchConditions = [], EntityID = 1, returnSectionID = False, returnEntityIDCountsAs = False, returnSectionLengthSubsetID = False, returnTotalEnrollmentCount = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionEnrollmentTotalForSectionLengthSubsetAndEntity in the district.

	This function returns a dataframe of every SectionEnrollmentTotalForSectionLengthSubsetAndEntity in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionEnrollmentTotalForSectionLengthSubsetAndEntity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionEnrollmentTotalForSectionLengthSubsetAndEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionLength(searchConditions = [], EntityID = 1, returnSectionLengthID = False, returnCode = False, returnCodeDescription = False, returnCourseLengthID = False, returnCreatedTime = False, returnDescription = False, returnEdFiTermTypeID = False, returnEndDate = False, returnEntityGroupKey = False, returnIlluminateTermType = False, returnIsSectionCurrent = False, returnMCCCDropDate = False, returnModifiedTime = False, returnSectionLengthIDClonedFrom = False, returnSectionLengthIDClonedTo = False, returnSectionLengthMNID = False, returnSectionRange = False, returnStartDate = False, returnThirdPartyTermNumber = False, returnThirdPartyTermTypeCalculated = False, returnThirdPartyTermTypeOverride = False, returnThirdPartyTermTypeOverrideCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionLength in the district.

	This function returns a dataframe of every SectionLength in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionLength/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionLength/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionLengthSubset(searchConditions = [], EntityID = 1, returnSectionLengthSubsetID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiTermTypeID = False, returnEndDate = False, returnEntityGroupKey = False, returnGradeBucketIDCarlPerkins = False, returnIsFullSectionLength = False, returnMCCCDropDate = False, returnMCCCTermImportID = False, returnModifiedTime = False, returnSectionLengthID = False, returnSectionLengthSubsetIDClonedFrom = False, returnSectionLengthSubsetIDClonedTo = False, returnSectionLengthSubsetMNID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionLengthSubset in the district.

	This function returns a dataframe of every SectionLengthSubset in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionLengthSubset/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionLengthSubset/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionMeetSummary(searchConditions = [], EntityID = 1, returnSectionMeetSummaryID = False, returnCalendarID = False, returnCreatedTime = False, returnEntityIDViewing = False, returnIsDefaultCalendar = False, returnModifiedTime = False, returnPeriodDaySummary = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionMeetSummary in the district.

	This function returns a dataframe of every SectionMeetSummary in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionMeetSummary/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionMeetSummary/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySection(searchConditions = [], EntityID = 1, returnSectionID = False, returnAllowCECE = False, returnAllowStudentsWithoutCategoryToBeAssigned = False, returnAssignmentCount = False, returnAssignmentCountForTermCalculated = False, returnAssignmentCountYTDCalculated = False, returnAssignmentDataString = False, returnAssignmentsHaveBeenCreated = False, returnBellScheduleGroupID = False, returnCalculatedBellScheduleGroupID = False, returnCalculatedStudentEnrollmentCount = False, returnCalculatedStudentEnrollmentCountEntity = False, returnCalculatedStudentEnrollmentCountEntityFirstDay = False, returnCalculatedStudentEnrollmentCountEntitySpecifiedDate = False, returnCalculatedStudentEnrollmentCountEntityToday = False, returnCalculatedStudentEnrollmentCountFirstDay = False, returnCalculatedStudentEnrollmentCountSpecifiedDate = False, returnCalculatedStudentEnrollmentCountToday = False, returnCalendarIDMCCCOverride = False, returnCanAddStudentSection = False, returnCanBeOffered = False, returnCode = False, returnCourseCodeSectionCode = False, returnCourseCodeSectionCodeCourseDescription = False, returnCourseDescriptionCodeSectionCode = False, returnCourseID = False, returnCourseIDHash = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnCurrentEnrollmentEntity = False, returnCurrentEnrollmentEntityForFilter = False, returnCurrentEnrollmentForFilter = False, returnCurrentGradingPeriod = False, returnCurrentlyRecalculating = False, returnDisplayForTeachers = False, returnDisplayPeriodIDCurrentStoredPrimary = False, returnDueDateOfLastAssignmentScored = False, returnEdFiEducationalEnvironmentID = False, returnEffectiveTeacherFirstLastName = False, returnEffectiveTeacherLastFirstName = False, returnEntityCodeTeacherNumber = False, returnEntityID = False, returnExcludeFromStudentSectionLink = False, returnExcusedAbsencesForTerm = False, returnExcusedAbsencesYTD = False, returnFit = False, returnFutureAssignmentCountForTermCalculated = False, returnGradebookCanHaveSettingsCopiedFromPreviousYear = False, returnGradedAssignmentCountForTermCalculated = False, returnHasAssignments = False, returnHasAssignmentsWithAcademicStandards = False, returnHasAssignmentsWithStudentGroups = False, returnHasAssignmentsWithSubjects = False, returnHasCalculationGroupCourse = False, returnHasCategoriesInDistrict = False, returnHasClosedOrCompletedSectionGradingScaleGroup = False, returnHasCompleted = False, returnHasCompletedForFilter = False, returnHasGradeMarksInEntity = False, returnHasGradingPeriodGradeBuckets = False, returnHasGradingScales = False, returnHasIncompleteClosedGradeChangeRequests = False, returnHasNonDeletedAssignments = False, returnHasNotStarted = False, returnHasNotStartedForFilter = False, returnHasPreviousYearSettings = False, returnHasStandardsCheckSectionLengthGradingPeriodSet = False, returnHasStudentSections = False, returnHasSubjectsCheckSectionLengthGradingPeriodSet = False, returnHasValidGradebookSetup = False, returnHasValidStandardsSetup = False, returnHasValidSubjectsSetup = False, returnHomeroomID = False, returnInPastYear = False, returnIsActive = False, returnIsActiveOverride = False, returnIsAdministeredForTSA = False, returnIsAHistoricRecord = False, returnIsBilingual = False, returnIsCreditRecovery = False, returnIsInProgress = False, returnIsInProgressForFilter = False, returnIsOffered = False, returnIsOfferedToAnotherEntity = False, returnIsSelfPaced = False, returnIsSelfPacedAndActive = False, returnIsTSAProficient = False, returnLanguageID = False, returnLockSectionFromSectionScheduler = False, returnLockSectionLengthFromSectionScheduler = False, returnMaximumStudentCount = False, returnMaximumStudentCountEntity = False, returnMaximumStudentCountEntityForFilter = False, returnMaximumStudentCountForEntityOfCourse = False, returnMaximumStudentCountForViewingEntity = False, returnMaximumStudentCountOffered = False, returnMaximumStudentCountOfferedForFilter = False, returnMaximumStudentCountOfferedToSpecifiedEntity = False, returnMeetIDCurrentStoredPrimary = False, returnMeetSummaryIDCurrentStoredPrimary = False, returnMinimumStudentCount = False, returnMissingAssignmentCount = False, returnMissingAssignmentCountForTermCalculated = False, returnModifiedTime = False, returnNoCountAssignmentCountForTermCalculated = False, returnNonGradedAssignmentCountForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnNonTransferCourseEnrollmentCountFemales = False, returnNonTransferCourseEnrollmentCountFemalesEntity = False, returnNonTransferCourseEnrollmentCountFemalesEntityFirstDay = False, returnNonTransferCourseEnrollmentCountFemalesEntitySpecifiedDate = False, returnNonTransferCourseEnrollmentCountFemalesEntityToday = False, returnNonTransferCourseEnrollmentCountFemalesFirstDay = False, returnNonTransferCourseEnrollmentCountFemalesSpecifiedDate = False, returnNonTransferCourseEnrollmentCountFemalesToday = False, returnNonTransferCourseEnrollmentCountMales = False, returnNonTransferCourseEnrollmentCountMalesEntity = False, returnNonTransferCourseEnrollmentCountMalesEntityFirstDay = False, returnNonTransferCourseEnrollmentCountMalesEntitySpecifiedDate = False, returnNonTransferCourseEnrollmentCountMalesEntityToday = False, returnNonTransferCourseEnrollmentCountMalesFirstDay = False, returnNonTransferCourseEnrollmentCountMalesSpecifiedDate = False, returnNonTransferCourseEnrollmentCountMalesToday = False, returnNonTransferCourseStudentEnrollmentCount = False, returnNonTransferCourseStudentEnrollmentCountEntity = False, returnNonTransferCourseStudentEnrollmentCountEntityFirstDay = False, returnNonTransferCourseStudentEnrollmentCountEntitySpecifiedDate = False, returnNonTransferCourseStudentEnrollmentCountEntityToday = False, returnNonTransferCourseStudentEnrollmentCountFirstDay = False, returnNonTransferCourseStudentEnrollmentCountSpecifiedDate = False, returnNonTransferCourseStudentEnrollmentCountToday = False, returnNumberOfTransferStudentSections = False, returnNumberOfTransferStudentSectionsForFilter = False, returnOffenseCount = False, returnOffenseCountYTD = False, returnOptimalStudentCount = False, returnOtherAbsencesForTerm = False, returnOtherAbsencesYTD = False, returnPeriodDaySummary = False, returnPreviousVersionOfFit = False, returnProgressStatusSpecifiedDate = False, returnProgressStatusToday = False, returnRecalculateGradebook = False, returnRecalculateGradebookAdmin = False, returnReservedSeatCount = False, returnRoomSeatsAvailable = False, returnSchedulingCategories = False, returnSchedulingTeams = False, returnSchoolYearID = False, returnScoreClarifierAssignmentCountForTermCalculated = False, returnScoredAssignmentCount = False, returnScoredAssignmentRange0CurrentTerm = False, returnScoredAssignmentRange100to90CurrentTerm = False, returnScoredAssignmentRange49to1CurrentTerm = False, returnScoredAssignmentRange59to50CurrentTerm = False, returnScoredAssignmentRange69to60CurrentTerm = False, returnScoredAssignmentRange79to70CurrentTerm = False, returnScoredAssignmentRange89to80CurrentTerm = False, returnSeatsAvailable = False, returnSeatsAvailableEntity = False, returnSeatsAvailableEntityForFilter = False, returnSeatsAvailableForFilter = False, returnSectionEnrollmentTotalsForSectionLengthSubsetSummary = False, returnSectionEnrollmentTotalsForSectionLengthSubsetSummaryForEntity = False, returnSectionIDClonedFrom = False, returnSectionIDClonedTo = False, returnSectionIDHash = False, returnSectionLengthID = False, returnSectionLengthScheduledBySectionScheduler = False, returnSectionMNID = False, returnSelfPacedEndTime = False, returnSelfPacedEndTimeDate = False, returnSelfPacedEndTimeTime = False, returnSingleSex = False, returnSingleSexCode = False, returnSpecialEdPercentageLimit = False, returnSpecifiedPeriodDaySummary = False, returnStaffIDCurrentStoredPrimary = False, returnStaffMeetIDCurrentStoredPrimary = False, returnStateInstructionalMethodCodeMNID = False, returnStateSTARModeOfTeachingMNID = False, returnStudentAssignmentDataString = False, returnStudentCountForTerm = False, returnStudentEnrollment = False, returnStudentEnrollmentAsOfSpecifiedDate = False, returnStudentEnrollmentAsOfSpecifiedDateForFilter = False, returnStudentEnrollmentEntity = False, returnStudentEnrollmentEntityForFilter = False, returnStudentEnrollmentFemales = False, returnStudentEnrollmentFemalesAsOfSpecifiedDate = False, returnStudentEnrollmentFemalesAsOfSpecifiedDateForFilter = False, returnStudentEnrollmentFemalesEntity = False, returnStudentEnrollmentFemalesEntityForFilter = False, returnStudentEnrollmentFemalesForFilter = False, returnStudentEnrollmentForFilter = False, returnStudentEnrollmentMales = False, returnStudentEnrollmentMalesAsOfSpecifiedDate = False, returnStudentEnrollmentMalesAsOfSpecifiedDateForFilter = False, returnStudentEnrollmentMalesEntity = False, returnStudentEnrollmentMalesEntityForFilter = False, returnStudentEnrollmentMalesForFilter = False, returnStudentSectionSectionIDHash = False, returnTardiesForTerm = False, returnTardiesYTD = False, returnThisPeriodDaySummary = False, returnTotalEnrollmentCount = False, returnTotalEnrollmentCountEntity = False, returnTotalEnrollmentCountEntityForFilter = False, returnTotalEnrollmentCountForFilter = False, returnTotalMeetCount = False, returnTotalSeatsOfferedToOtherEntities = False, returnTransferCourseEnrollmentCountFemales = False, returnTransferCourseEnrollmentCountFemalesEntity = False, returnTransferCourseEnrollmentCountFemalesEntityFirstDay = False, returnTransferCourseEnrollmentCountFemalesEntitySpecifiedDate = False, returnTransferCourseEnrollmentCountFemalesEntityToday = False, returnTransferCourseEnrollmentCountFemalesFirstDay = False, returnTransferCourseEnrollmentCountFemalesSpecifiedDate = False, returnTransferCourseEnrollmentCountFemalesToday = False, returnTransferCourseEnrollmentCountMales = False, returnTransferCourseEnrollmentCountMalesEntity = False, returnTransferCourseEnrollmentCountMalesEntityFirstDay = False, returnTransferCourseEnrollmentCountMalesEntitySpecifiedDate = False, returnTransferCourseEnrollmentCountMalesEntityToday = False, returnTransferCourseEnrollmentCountMalesFirstDay = False, returnTransferCourseEnrollmentCountMalesSpecifiedDate = False, returnTransferCourseEnrollmentCountMalesToday = False, returnTransferCourseStudentEnrollmentCount = False, returnTransferCourseStudentEnrollmentCountEntity = False, returnTransferCourseStudentEnrollmentCountEntityFirstDay = False, returnTransferCourseStudentEnrollmentCountEntitySpecifiedDate = False, returnTransferCourseStudentEnrollmentCountEntityToday = False, returnTransferCourseStudentEnrollmentCountFirstDay = False, returnTransferCourseStudentEnrollmentCountSpecifiedDate = False, returnTransferCourseStudentEnrollmentCountToday = False, returnUnexcusedAbsencesForTerm = False, returnUnexcusedAbsencesYTD = False, returnUnscoredAssignmentCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsingCurriculumSubjectsInGradebook = False, returnViewingFromOfferingEntity = False, returnWebsite = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Section in the district.

	This function returns a dataframe of every Section in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/Section/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/Section/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionSchedulerCourseConstraint(searchConditions = [], EntityID = 1, returnSectionSchedulerCourseConstraintID = False, returnCourseID = False, returnCourseIDLinked = False, returnCreatedTime = False, returnCurrentCourseSection = False, returnCurrentCourseSectionCode = False, returnCurrentCourseTopSectionCount = False, returnIsActive = False, returnLinkedCourse = False, returnLinkedCourseSection = False, returnLinkedCourseSectionCode = False, returnLinkedCourseTopSectionCount = False, returnModifiedTime = False, returnRule = False, returnRuleCode = False, returnScheduleFirst = False, returnScheduleLinkedCourseFirst = False, returnSectionIDCurrentCourseSelected = False, returnSectionIDLinkedCourseSelected = False, returnSectionSchedulerCourseConstraintIDClonedFrom = False, returnSectionSchedulerCourseConstraintIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionSchedulerCourseConstraint in the district.

	This function returns a dataframe of every SectionSchedulerCourseConstraint in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerCourseConstraint/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerCourseConstraint/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionSchedulerDayRotationForMeet(searchConditions = [], EntityID = 1, returnSectionSchedulerDayRotationForMeetID = False, returnCreatedTime = False, returnDayRotationID = False, returnMeetID = False, returnModifiedTime = False, returnSectionSchedulerDayRotationForMeetClonedTo = False, returnSectionSchedulerDayRotationForMeetIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionSchedulerDayRotationForMeet in the district.

	This function returns a dataframe of every SectionSchedulerDayRotationForMeet in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerDayRotationForMeet/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerDayRotationForMeet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionSchedulerDisplayPeriodExcludedForCourse(searchConditions = [], EntityID = 1, returnSectionSchedulerDisplayPeriodExcludedForCourseID = False, returnCourseID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnSectionSchedulerDisplayPeriodExcludedForCourseIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionSchedulerDisplayPeriodExcludedForCourse in the district.

	This function returns a dataframe of every SectionSchedulerDisplayPeriodExcludedForCourse in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerDisplayPeriodExcludedForCourse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerDisplayPeriodExcludedForCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionSchedulerPattern(searchConditions = [], EntityID = 1, returnSectionSchedulerPatternID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDayRotationCount = False, returnDayRotationSummary = False, returnDescription = False, returnEntityID = False, returnHasDayRotations = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionSchedulerPatternIDClonedFrom = False, returnSectionSchedulerPatternIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionSchedulerPattern in the district.

	This function returns a dataframe of every SectionSchedulerPattern in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerPattern/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerPattern/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionSchedulerPatternDayRotation(searchConditions = [], EntityID = 1, returnSectionSchedulerPatternDayRotationID = False, returnCreatedTime = False, returnDayRotationID = False, returnModifiedTime = False, returnSectionSchedulerPatternDayRotationClonedTo = False, returnSectionSchedulerPatternDayRotationIDClonedFrom = False, returnSectionSchedulerPatternID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionSchedulerPatternDayRotation in the district.

	This function returns a dataframe of every SectionSchedulerPatternDayRotation in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerPatternDayRotation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerPatternDayRotation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionSchedulerPatternExcludedForMeetRequirement(searchConditions = [], EntityID = 1, returnSectionSchedulerPatternExcludedForMeetRequirementID = False, returnCreatedTime = False, returnMeetRequirementID = False, returnModifiedTime = False, returnSectionSchedulerPatternExcludedForMeetRequirementIDClonedFrom = False, returnSectionSchedulerPatternID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionSchedulerPatternExcludedForMeetRequirement in the district.

	This function returns a dataframe of every SectionSchedulerPatternExcludedForMeetRequirement in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerPatternExcludedForMeetRequirement/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerPatternExcludedForMeetRequirement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionSchedulerProposedMeet(searchConditions = [], EntityID = 1, returnSectionSchedulerProposedMeetID = False, returnCreatedTime = False, returnDisplayPeriodRotationID = False, returnEndDate = False, returnMeetDisplayPeriodSummary = False, returnModifiedTime = False, returnNumberOfActualConflicts = False, returnNumberOfEstimatedConflicts = False, returnNumberOfProposedMeetCourseConflicts = False, returnNumberOfProposedMeetRoomAndStaffConflicts = False, returnNumberOfProposedMeetRoomConflicts = False, returnNumberOfProposedMeetStaffConflicts = False, returnPrimaryStaffMeetFullNameLFM = False, returnRank = False, returnRankValue = False, returnRoomID = False, returnSectionLengthID = False, returnSectionSchedulerRunAnalysisID = False, returnStartDate = False, returnSumTotalOfMaximumStudentCountForScheduledSections = False, returnSumTotalOfOptimalStudentCountForScheduledSections = False, returnTotalActualConflictsPointsEarned = False, returnTotalDisplayPeriodPointsEarned = False, returnTotalEstimatedConflictsPointsEarned = False, returnTotalRoomPointsEarned = False, returnTotalStaffPointsEarned = False, returnTotalSumOfMaximumStudentCountForScheduledSectionsPointsEarned = False, returnTotalSumOfOptimalStudentCountForScheduledSectionsPointsEarned = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionSchedulerProposedMeet in the district.

	This function returns a dataframe of every SectionSchedulerProposedMeet in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerProposedMeet/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerProposedMeet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionSchedulerProposedMeetConflict(searchConditions = [], EntityID = 1, returnSectionSchedulerProposedMeetConflictID = False, returnConflictType = False, returnConflictTypeCode = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnName = False, returnNumberOfActualConflicts = False, returnNumberOfCommonRequests = False, returnNumberOfEstimatedConflicts = False, returnSectionSchedulerProposedMeetID = False, returnSeverity = False, returnSeverityCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionSchedulerProposedMeetConflict in the district.

	This function returns a dataframe of every SectionSchedulerProposedMeetConflict in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerProposedMeetConflict/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerProposedMeetConflict/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionSchedulerProposedMeetDisplayPeriod(searchConditions = [], EntityID = 1, returnSectionSchedulerProposedMeetDisplayPeriodID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnSectionSchedulerProposedMeetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionSchedulerProposedMeetDisplayPeriod in the district.

	This function returns a dataframe of every SectionSchedulerProposedMeetDisplayPeriod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerProposedMeetDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerProposedMeetDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionSchedulerProposedStaffMeet(searchConditions = [], EntityID = 1, returnSectionSchedulerProposedStaffMeetID = False, returnCreatedTime = False, returnEffectiveEndDate = False, returnEffectiveStartDate = False, returnIsPrimary = False, returnModifiedTime = False, returnSectionSchedulerProposedMeetID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionSchedulerProposedStaffMeet in the district.

	This function returns a dataframe of every SectionSchedulerProposedStaffMeet in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerProposedStaffMeet/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerProposedStaffMeet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionSchedulerRoomTypeForCourse(searchConditions = [], EntityID = 1, returnSectionSchedulerRoomTypeForCourseID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnRoomTypeID = False, returnSectionSchedulerRoomTypeForCourseIDClonedFrom = False, returnSectionSchedulerRoomTypeForCourseIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionSchedulerRoomTypeForCourse in the district.

	This function returns a dataframe of every SectionSchedulerRoomTypeForCourse in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerRoomTypeForCourse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerRoomTypeForCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionSchedulerRunAnalysis(searchConditions = [], EntityID = 1, returnSectionSchedulerRunAnalysisID = False, returnAcceptedMeetReverted = False, returnAnalysisDuration = False, returnAnalysisMethod = False, returnAnalysisMethodCode = False, returnAnalyzeDayRotations = False, returnAnalyzeMeetDisplayPeriods = False, returnAnalyzeRoom = False, returnAnalyzeSectionLength = False, returnAnalyzeStaffMeets = False, returnCountOfSectionSchedulerProposedMeetRecords = False, returnCreatedTime = False, returnEndTimeAnalysis = False, returnEntityID = False, returnExcludeMeetsPreviouslyScheduled = False, returnMeetID = False, returnModifiedTime = False, returnPageStateID = False, returnRunReason = False, returnSchoolYearID = False, returnSectionSchedulerProposedMeetIDAccepted = False, returnStartTimeAnalysis = False, returnTotalActualConflictsPointsPossible = False, returnTotalDisplayPeriodPointsPossible = False, returnTotalEstimatedConflictsPointsPossible = False, returnTotalRoomPointsPossible = False, returnTotalStaffPointsPossible = False, returnTotalSumOfMaximumStudentCountForScheduledSectionsPointsPossible = False, returnTotalSumOfOptimalStudentCountForScheduledSectionsPointsPossible = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDPerformer = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionSchedulerRunAnalysis in the district.

	This function returns a dataframe of every SectionSchedulerRunAnalysis in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerRunAnalysis/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerRunAnalysis/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionSchedulerStaffForCourse(searchConditions = [], EntityID = 1, returnSectionSchedulerStaffForCourseID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionSchedulerStaffForCourseIDClonedFrom = False, returnSectionSchedulerStaffForCourseIDClonedTo = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionSchedulerStaffForCourse in the district.

	This function returns a dataframe of every SectionSchedulerStaffForCourse in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerStaffForCourse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerStaffForCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionSchedulingCategory(searchConditions = [], EntityID = 1, returnSectionSchedulingCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingCategoryID = False, returnSectionID = False, returnSectionSchedulingCategoryIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionSchedulingCategory in the district.

	This function returns a dataframe of every SectionSchedulingCategory in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulingCategory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulingCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionSchedulingTeam(searchConditions = [], EntityID = 1, returnSectionSchedulingTeamID = False, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingTeamID = False, returnSectionID = False, returnSectionSchedulingTeamIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionSchedulingTeam in the district.

	This function returns a dataframe of every SectionSchedulingTeam in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulingTeam/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulingTeam/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStaffMeet(searchConditions = [], EntityID = 1, returnStaffMeetID = False, returnApplyClosedGradingPeriodGradeChangePermission = False, returnAssignmentCount = False, returnCanMakeClosedGradingPeriodGradeChange = False, returnClosedGradingPeriodGradeChangeCount = False, returnCreatedTime = False, returnEffectiveEndDate = False, returnEffectiveStartDate = False, returnGradebookLastAccessedTime = False, returnHasAttendanceAccess = False, returnHasAttendanceAccessAsOfDate = False, returnHasGradebookAccess = False, returnIsLongTermSubstitute = False, returnIsPrimary = False, returnIsStaffCertified = False, returnIsSubstitute = False, returnLockStaffFromSectionScheduler = False, returnMeetID = False, returnMeetIsCurrent = False, returnMeetsToday = False, returnModifiedTime = False, returnNameMeetDescription = False, returnScheduledBySectionScheduler = False, returnSchoolYearID = False, returnSectionID = False, returnStaffID = False, returnStaffMeetIDClonedFrom = False, returnStaffMeetIDSubstituteFor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StaffMeet in the district.

	This function returns a dataframe of every StaffMeet in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StaffMeet/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StaffMeet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStaffStudent(searchConditions = [], EntityID = 1, returnStudentID = False, returnEntityID = False, returnSchoolYearID = False, returnStaffID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StaffStudent in the district.

	This function returns a dataframe of every StaffStudent in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StaffStudent/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StaffStudent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentAutoSchedulerCourse(searchConditions = [], EntityID = 1, returnStudentAutoSchedulerCourseID = False, returnActiveSections = False, returnCategoryCode = False, returnConflictedRequestPercent = False, returnCourseCode = False, returnCourseDescription = False, returnCourseEntityCode = False, returnCourseEntityID = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseSubjectCode = False, returnCreatedTime = False, returnDepartmentCode = False, returnIsActive = False, returnIsRequired = False, returnModifiedTime = False, returnScheduledRequestPercent = False, returnSchedulingPriorityCode = False, returnSchedulingTeamModeCode = False, returnSchedulingTypeCode = False, returnStudentAutoSchedulerRunAnalysisID = False, returnTotalAlternateRequests = False, returnTotalConflicts = False, returnTotalNumberScheduledThisRun = False, returnTotalRequests = False, returnTotalScheduled = False, returnTotalSeatsAvailable = False, returnTotalSeatsScheduled = False, returnTotalSections = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentAutoSchedulerCourse in the district.

	This function returns a dataframe of every StudentAutoSchedulerCourse in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerCourse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentAutoSchedulerProposedStudentCourseRequest(searchConditions = [], EntityID = 1, returnStudentAutoSchedulerProposedStudentCourseRequestID = False, returnBaseRunAnalysisID = False, returnCachedStudentSectionID = False, returnCourseConflictReason = False, returnCourseConflictReasonCode = False, returnCourseConflictReasonText = False, returnCourseID = False, returnCourseIDOriginal = False, returnCreatedTime = False, returnDataCommittedToRealObjects = False, returnEntityIDRequestedFrom = False, returnIgnore = False, returnIsAlternate = False, returnIsNewlyScheduled = False, returnModifiedTime = False, returnRequestStatus = False, returnRequestStatusCode = False, returnRequestStatusOriginal = False, returnRequestStatusOriginalCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSchedulingMethodOriginal = False, returnSchedulingMethodOriginalCode = False, returnSectionID = False, returnSectionIDOriginal = False, returnSectionLengthSubsetsRequested = False, returnSectionLengthSubsetSummary = False, returnSequenceWithinEntireProcess = False, returnSequenceWithinGrade = False, returnSequenceWithinStudent = False, returnStudentCourseRequestID = False, returnStudentCourseRequestIDOriginal = False, returnStudentID = False, returnStudentIDOriginal = False, returnStudentSectionID = False, returnStudentSectionIDOriginal = False, returnUnscheduleStatus = False, returnUnscheduleStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentAutoSchedulerProposedStudentCourseRequest in the district.

	This function returns a dataframe of every StudentAutoSchedulerProposedStudentCourseRequest in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerProposedStudentCourseRequest/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerProposedStudentCourseRequest/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentAutoSchedulerProposedStudentSection(searchConditions = [], EntityID = 1, returnStudentAutoSchedulerProposedStudentSectionID = False, returnBaseRunAnalysisID = False, returnCachedStudentSectionID = False, returnCreatedTime = False, returnDataCommittedToRealObjects = False, returnGradeReferenceID = False, returnGradeReferenceIDOriginal = False, returnModifiedTime = False, returnSectionID = False, returnSectionIDOriginal = False, returnSequenceWithinEntireProcess = False, returnSequenceWithinGrade = False, returnSequenceWithinStudent = False, returnStudentID = False, returnStudentIDOriginal = False, returnStudentSectionID = False, returnStudentSectionIDOriginal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentAutoSchedulerProposedStudentSection in the district.

	This function returns a dataframe of every StudentAutoSchedulerProposedStudentSection in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerProposedStudentSection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerProposedStudentSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentAutoSchedulerProposedStudentSectionTransaction(searchConditions = [], EntityID = 1, returnStudentAutoSchedulerProposedStudentSectionTransactionID = False, returnBaseRunAnalysisID = False, returnCachedStudentSectionID = False, returnCreatedTime = False, returnDataCommittedToRealObjects = False, returnEndDate = False, returnEndDateOriginal = False, returnEntityIDCountsAs = False, returnModifiedTime = False, returnSectionID = False, returnSectionIDOriginal = False, returnSectionLengthSubsetID = False, returnSectionLengthSubsetIDOriginal = False, returnStartDate = False, returnStartDateOriginal = False, returnStudentID = False, returnStudentIDOriginal = False, returnStudentSectionID = False, returnStudentSectionIDOriginal = False, returnStudentSectionTransactionID = False, returnStudentSectionTransactionIDOriginal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentAutoSchedulerProposedStudentSectionTransaction in the district.

	This function returns a dataframe of every StudentAutoSchedulerProposedStudentSectionTransaction in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerProposedStudentSectionTransaction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerProposedStudentSectionTransaction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentAutoSchedulerRunAnalysis(searchConditions = [], EntityID = 1, returnStudentAutoSchedulerRunAnalysisID = False, returnAnalysisDuration = False, returnAnalysisVersion = False, returnAnalysisVersionCode = False, returnBaseRunAnalysisID = False, returnCloseSectionsWhenFilled = False, returnConflictedStudentCourseRequestPercent = False, returnCountOfStudentAutoSchedulerCourseRecords = False, returnCountOfStudentAutoSchedulerRunAnalysisExceptionRecords = False, returnCountOfStudentAutoSchedulerStudentRecords = False, returnCourseConflictPercent = False, returnCreatedCourseAndSectionAnalysisDetails = False, returnCreatedStudentAnalysisDetails = False, returnCreatedTime = False, returnDescription = False, returnEndTimeAnalysis = False, returnEndTimeFinalize = False, returnExistsAutoScheduledCourses = False, returnExistsAutoScheduledStudents = False, returnFailedScheduledStudentSectionsCount = False, returnFailedStudentCourseRequestsCount = False, returnFailedStudentSectionsCount = False, returnFailedStudentSectionTransactionsCount = False, returnFinalizeDuration = False, returnGradeReferenceIDEnd = False, returnGradeReferenceIDStart = False, returnIncludedAbilityToAcceptProposedSchedules = False, returnIsInvalidFinalizeState = False, returnModifiedTime = False, returnOverallDuration = False, returnPersistentSchedulingRunDataIsNoLongerAcceptable = False, returnProcessSpecialEdCourses = False, returnProposedSchedulesAccepted = False, returnRunDescription = False, returnRunInformation = False, returnScheduledStudentCourseRequestPercent = False, returnSendMessageOnComplete = False, returnStartTimeAnalysis = False, returnStartTimeFinalize = False, returnStudentAutoSchedulerMode = False, returnStudentAutoSchedulerModeCode = False, returnStudentConflictPercent = False, returnStudentCourseRequestOrder = False, returnStudentCourseRequestsConflictedThisRun = False, returnStudentCourseRequestsProcessedThisRun = False, returnStudentCourseRequestsScheduledThisRun = False, returnStudentDifficultyOrder = False, returnStudentInformation = False, returnSuccessfulStudentSectionsCount = False, returnTotalAlternateStudentCourseRequests = False, returnTotalConflictedStudentCourseRequests = False, returnTotalScheduledStudentCourseRequests = False, returnTotalStudentCourseRequests = False, returnTotalStudentCourseRequestsToFinalize = False, returnTotalStudents = False, returnTotalStudentSectionsToFinalize = False, returnTotalStudentSectionTransactionsToFinalize = False, returnTotalStudentsWithConflicts = False, returnTotalStudentsWithOneConflict = False, returnTotalStudentsWithThreeOrMoreConflicts = False, returnTotalStudentsWithTwoConflicts = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentAutoSchedulerRunAnalysis in the district.

	This function returns a dataframe of every StudentAutoSchedulerRunAnalysis in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerRunAnalysis/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerRunAnalysis/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentAutoSchedulerRunAnalysisException(searchConditions = [], EntityID = 1, returnStudentAutoSchedulerRunAnalysisExceptionID = False, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnMessage = False, returnModifiedTime = False, returnSectionCode = False, returnSeverityType = False, returnSeverityTypeCode = False, returnStudentAutoSchedulerRunAnalysisID = False, returnStudentAutoSchedulerStudentCourseRequestID = False, returnStudentFullName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentAutoSchedulerRunAnalysisException in the district.

	This function returns a dataframe of every StudentAutoSchedulerRunAnalysisException in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerRunAnalysisException/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerRunAnalysisException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentAutoSchedulerRunAnalysisTotal(searchConditions = [], EntityID = 1, returnStudentAutoSchedulerRunAnalysisTotalID = False, returnConflictedStudentCourseRequestPercent = False, returnConflictPercent = False, returnCreatedTime = False, returnEndTimeAnalysis = False, returnGradeReferenceID = False, returnModifiedTime = False, returnScheduledStudentCourseRequestPercent = False, returnStartTimeAnalysis = False, returnStudentAutoSchedulerRunAnalysisID = False, returnStudentCourseRequestsConflictedThisRun = False, returnStudentCourseRequestsProcessedThisRun = False, returnStudentCourseRequestsScheduledThisRun = False, returnStudentsWithConflicts = False, returnStudentsWithOneConflict = False, returnStudentsWithThreeOrMoreConflicts = False, returnStudentsWithTwoConflicts = False, returnTotalAlternateStudentCourseRequests = False, returnTotalConflictedStudentCourseRequests = False, returnTotalScheduledStudentCourseRequests = False, returnTotalStudentCourseRequests = False, returnTotalStudents = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentAutoSchedulerRunAnalysisTotal in the district.

	This function returns a dataframe of every StudentAutoSchedulerRunAnalysisTotal in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerRunAnalysisTotal/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerRunAnalysisTotal/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentAutoSchedulerSection(searchConditions = [], EntityID = 1, returnStudentAutoSchedulerSectionID = False, returnAllowStudentsWithoutCategoryToBeAssigned = False, returnCreatedTime = False, returnDayRotationCode = False, returnDisplayPeriodCode = False, returnIsActive = False, returnMaximumStudentCount = False, returnMinimumStudentCount = False, returnModifiedTime = False, returnOptimalStudentCount = False, returnPeriodDaySummary = False, returnPrimaryMeetBuildingCode = False, returnPrimaryMeetRoomNumber = False, returnPrimaryMeetStaffNameLFM = False, returnSchedulingCategories = False, returnSchedulingTeams = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnStudentAutoSchedulerCourseID = False, returnTotalNumberScheduledThisRun = False, returnTotalScheduled = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentAutoSchedulerSection in the district.

	This function returns a dataframe of every StudentAutoSchedulerSection in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerSection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentAutoSchedulerStudent(searchConditions = [], EntityID = 1, returnStudentAutoSchedulerStudentID = False, returnBirthDate = False, returnCalendarCode = False, returnCreatedTime = False, returnEndTimeAnalysis = False, returnFullName = False, returnGenderCode = False, returnGrade = False, returnGradeReferenceID = False, returnHasConflict = False, returnModifiedTime = False, returnNumberOfConflictedStudentCourseRequests = False, returnNumberOfScheduledStudentCourseRequests = False, returnProcessedDuringThisSchedulingRun = False, returnRandomSchedulingInteger = False, returnRawPermutations = False, returnSchedulesConsidered = False, returnSchedulingCategories = False, returnSchedulingTeamCode = False, returnSequenceNumber = False, returnStartTimeAnalysis = False, returnStudentAutoSchedulerRunAnalysisID = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnTotalNumberOfAlternateStudentCourseRequests = False, returnTotalNumberOfStudentCourseRequests = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentAutoSchedulerStudent in the district.

	This function returns a dataframe of every StudentAutoSchedulerStudent in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerStudent/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerStudent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentAutoSchedulerStudentCourseRequest(searchConditions = [], EntityID = 1, returnStudentAutoSchedulerStudentCourseRequestID = False, returnCourseConflictReason = False, returnCourseConflictReasonCode = False, returnCourseConflictReasonText = False, returnCreatedTime = False, returnEntityIDRequestedFrom = False, returnEntityRequestedFromEntityCode = False, returnHasRelatedStudentAutoSchedulerStudentCourseRequestSections = False, returnInitialSequenceNumber = False, returnIsAlternate = False, returnModifiedTime = False, returnSchedulingMethodCode = False, returnSectionLengthSubsetsRequested = False, returnSectionLengthSubsetSummary = False, returnSequenceNumber = False, returnStudentAutoSchedulerCourseID = False, returnStudentAutoSchedulerSectionID = False, returnStudentAutoSchedulerStudentID = False, returnStudentCourseRequestID = False, returnUpdatedDuringThisSchedulingRun = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentAutoSchedulerStudentCourseRequest in the district.

	This function returns a dataframe of every StudentAutoSchedulerStudentCourseRequest in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerStudentCourseRequest/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerStudentCourseRequest/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentAutoSchedulerStudentCourseRequestSection(searchConditions = [], EntityID = 1, returnStudentAutoSchedulerStudentCourseRequestSectionID = False, returnAssignedToThisSection = False, returnCreatedTime = False, returnEligibleToEnrollInSection = False, returnModifiedTime = False, returnPeriodDaySummary = False, returnSeatsRemaining = False, returnSequenceNumber = False, returnStudentAutoSchedulerSectionID = False, returnStudentAutoSchedulerStudentCourseRequestID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentAutoSchedulerStudentCourseRequestSection in the district.

	This function returns a dataframe of every StudentAutoSchedulerStudentCourseRequestSection in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerStudentCourseRequestSection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerStudentCourseRequestSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentAutoSchedulerStudentCourseRequestSectionDetail(searchConditions = [], EntityID = 1, returnStudentAutoSchedulerStudentCourseRequestSectionDetailID = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionConflictReason = False, returnSectionConflictReasonCode = False, returnSectionConflictReasonText = False, returnStudentAutoSchedulerStudentCourseRequestSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentAutoSchedulerStudentCourseRequestSectionDetail in the district.

	This function returns a dataframe of every StudentAutoSchedulerStudentCourseRequestSectionDetail in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerStudentCourseRequestSectionDetail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerStudentCourseRequestSectionDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentCourseRequest(searchConditions = [], EntityID = 1, returnStudentCourseRequestID = False, returnAlternateRank = False, returnCountsAgainstRequestLimit = False, returnCourseConflict = False, returnCourseEntityOfferedToID = False, returnCourseID = False, returnCourseIsNotDroppedManualOrTransfer = False, returnCourseNotScheduled = False, returnCourseNotScheduledAndIsRequestedFromViewingEntity = False, returnCourseRequested = False, returnCourseScheduled = False, returnCourseScheduledAndAllTransactionsCountTowardsViewingEntity = False, returnCourseScheduledAndAllTransactionsCountTowardsViewingEntityAndCourseIsNotDropOrTransfer = False, returnCourseScheduledAndCountsTowardsViewingEntity = False, returnCourseScheduledAndInProgress = False, returnCourseScheduledAndInProgressAndIsEffectiveToViewingEntity = False, returnCourseScheduledAndIsBeforeOrInProgress = False, returnCourseScheduledAndIsBeforeOrInProgressAndNotHasAtleastOneTransactionNotCountTowardsViewingEntity = False, returnCourseScheduledAndIsRequestedFromOfferingEntityAndAllTransactionsCountTowardsViewingEntity = False, returnCourseScheduledAndRequestedFromViewingEntityAndAllTransactionsCountTowardsViewingEntity = False, returnCreatedTime = False, returnCrsIsNotDrpOrTransferAndNotScheduledOrCrsScheduledAndRequestedFromViewingEntityAndAllTransactionsCntTowardsViewingEntity = False, returnDisplayToViewingEntity = False, returnEarnedCreditsPossibleAnticipated = False, returnEarnedCreditsRequested = False, returnEntityIDRequestedFrom = False, returnIsAlternate = False, returnModifiedTime = False, returnPrerequisiteMet = False, returnRequestedFromOfferingEntity = False, returnRequestedFromViewingEntity = False, returnRequestSource = False, returnRequestSourceCode = False, returnRequestStatus = False, returnRequestStatusCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSectionLengthSubsetSummary = False, returnStudentCourseRequestIDAlternateFor = False, returnStudentCourseRequestIDHash = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionIDHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentCourseRequest in the district.

	This function returns a dataframe of every StudentCourseRequest in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentCourseRequest/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentCourseRequest/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentCourseRequestSectionLengthSubset(searchConditions = [], EntityID = 1, returnStudentCourseRequestSectionLengthSubsetID = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionLengthSubsetID = False, returnStudentCourseRequestID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentCourseRequestSectionLengthSubset in the district.

	This function returns a dataframe of every StudentCourseRequestSectionLengthSubset in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentCourseRequestSectionLengthSubset/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentCourseRequestSectionLengthSubset/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentEntityYearSchedulingCategory(searchConditions = [], EntityID = 1, returnStudentEntityYearSchedulingCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingCategoryID = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentEntityYearSchedulingCategory in the district.

	This function returns a dataframe of every StudentEntityYearSchedulingCategory in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentEntityYearSchedulingCategory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentEntityYearSchedulingCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentSection(searchConditions = [], EntityID = 1, returnStudentSectionID = False, returnAcademicHistoryHash = False, returnActiveStudentGroups = False, returnAllTransactionsCountTowardsViewingEntity = False, returnAssignmentDueDateAttendance = False, returnConversionKey = False, returnCountsForViewingEntity = False, returnCourseOrTransferDescription = False, returnCreatedTime = False, returnDisplayLinkedStudentSection = False, returnDisplayToViewingEntity = False, returnEarnedCreditAttempted = False, returnEarnedCreditAttemptedAllEntered = False, returnEarnedCreditAttemptedCompleted = False, returnEarnedCreditOverride = False, returnEarnedCredits = False, returnEarnedCreditsAllEntered = False, returnEarnedCreditsCompleted = False, returnEarnedCreditsPossible = False, returnEarnedCreditsPossibleAllEntered = False, returnEarnedCreditsPossibleCompleted = False, returnEndDate = False, returnEntityIDCourse = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLink = False, returnExistsStudentSectionGPAMethods = False, returnFailedCredits = False, returnFailedCreditsAllEntered = False, returnFailedCreditsCompleted = False, returnFilteredGradedAssignmentCount = False, returnFilteredMissingAssignmentCount = False, returnFilteredUnGradedAssignmentCount = False, returnGradebookSortCode = False, returnGradebookStudentNameToUse = False, returnGradeReferenceID = False, returnHasAtLeastOneCrossEntityStudentSectionTransaction = False, returnHasAtleastOneTransactionNotCountTowardsViewingEntity = False, returnHasLinkingConflicts = False, returnHasStudentGradingScaleGroupForGradingPeriodGradeBucket = False, returnHasStudentSectionNoteForCurrentUser = False, returnInProgress = False, returnInProgressAndIsEffectiveForViewingEntity = False, returnIsActiveAsOfDate = False, returnIsActiveForTodayOrForSectionStartOrEnd = False, returnIsAvailableForAssignmentStudentGroup = False, returnIsBeforeOrInProgress = False, returnIsBeforeOrInProgressAndNotHasAtleastOneTransactionNotCountTowardsViewingEntity = False, returnIsCurrentStudentSection = False, returnIsEffectiveForViewingEntity = False, returnIsFlaggedAsMissingAssignmentCount = False, returnIsForCurrentSchoolYear = False, returnIsStudentSectionScheduledToMeet = False, returnIsTransferCourse = False, returnIsTSAProficient = False, returnIsWorkInProgress = False, returnLastStudentSectionTransactionConsideredDropped = False, returnLinkedStudentSectionsEarnedCredit = False, returnLinkedStudentSectionsEarnedCreditAttempted = False, returnLinkedStudentSectionsFailedCredit = False, returnMissingAssignmentCount = False, returnModifiedTime = False, returnMultipleTransactions = False, returnRenderTransferGradesRowButton = False, returnRequestedFromOfferingEntityAndAllTransactionsCountTowardsViewingEntity = False, returnRequestedFromViewingEntityAndAllTransactionsCountTowardsViewingEntity = False, returnSchoolYearIDCourse = False, returnSectionID = False, returnSectionLengthSubsetSummary = False, returnStartDate = False, returnStatus = False, returnStatusCode = False, returnStatusString = False, returnStudentID = False, returnStudentSectionCode = False, returnStudentSectionIDHash = False, returnStudentSectionLink = False, returnStudentSectionMNID = False, returnStudentSectionNoteCountForCurrentUser = False, returnTotalDaysAbsent = False, returnTotalDaysExcused = False, returnTotalDaysOther = False, returnTotalDaysTardy = False, returnTotalDaysUnexcused = False, returnTotalEarnedCreditOverride = False, returnTotalFailedCreditOverride = False, returnTransactionCountsForViewingEntity = False, returnTransferCourseName = False, returnUnscoredPastDueAssignmentCount = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditTotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentSection in the district.

	This function returns a dataframe of every StudentSection in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentSection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentSectionTransaction(searchConditions = [], EntityID = 1, returnStudentSectionTransactionID = False, returnCalendarID = False, returnCountsTowardsViewingEntity = False, returnCreatedTime = False, returnEarlyExitReasonID = False, returnEndDate = False, returnEndsAfterSectionLengthStartDate = False, returnEntityIDCountsAs = False, returnHideNewStudentButton = False, returnIsCECE = False, returnIsInProgress = False, returnIsInProgressAsOfToday = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnOverlapsSectionLength = False, returnSectionID = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionTransactionIDHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentSectionTransaction in the district.

	This function returns a dataframe of every StudentSectionTransaction in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentSectionTransaction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentSectionTransaction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentSectionTransactionRoomPeriod(searchConditions = [], EntityID = 1, returnStudentSectionTransactionID = False, returnCalendarID = False, returnDisplayPeriodID = False, returnEndDateMeet = False, returnEndDateSectionSectionTransaction = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnEntityIDFor = False, returnEntityIDViewingCalculated = False, returnEntityIDViewingMeetSummary = False, returnIsDefaultCalendar = False, returnMeetID = False, returnMeetSummaryID = False, returnRoomID = False, returnSchedulingPeriodID = False, returnSchoolYearID = False, returnSectionID = False, returnStartDateMeet = False, returnStartDateStudentSectionTransaction = False, returnStudentID = False, returnStudentSectionID = False, returnUseRoomOverride = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentSectionTransactionRoomPeriod in the district.

	This function returns a dataframe of every StudentSectionTransactionRoomPeriod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentSectionTransactionRoomPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentSectionTransactionRoomPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudyHallSchedulerRunAnalysis(searchConditions = [], EntityID = 1, returnStudyHallSchedulerRunAnalysisID = False, returnBaseRunAnalysisID = False, returnCreatedTime = False, returnEndTimeAnalysis = False, returnEndTimeFinalize = False, returnModifiedTime = False, returnRunInformation = False, returnStartTimeAnalysis = False, returnStartTimeFinalize = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudyHallSchedulerRunAnalysis in the district.

	This function returns a dataframe of every StudyHallSchedulerRunAnalysis in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudyHallSchedulerRunAnalysis/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudyHallSchedulerRunAnalysis/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempCourse(searchConditions = [], EntityID = 1, returnTempCourseID = False, returnActiveSections = False, returnAveragePerSectionMinimumSectionsRequired = False, returnCodeDescription = False, returnCourseCode = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseLengthID = False, returnCourseSubjectCode = False, returnCourseTypeCode = False, returnCreatedTime = False, returnCurriculumCode = False, returnDefaultSectionLengthID = False, returnDescription = False, returnEarnedCredits = False, returnEntityCode = False, returnEstimatedNumberOfSections = False, returnEstimatedStudentsPerSection = False, returnGradeLevelSummary = False, returnGradingPeriodSetCode = False, returnGradingPeriodSetID = False, returnIsActive = False, returnMinimumSectionsRequired = False, returnModifiedTime = False, returnNewCourseLengthCode = False, returnNewCourseLengthID = False, returnNewGradingPeriodSetCode = False, returnNewGradingPeriodSetID = False, returnNote = False, returnNumberOfAlternateCourseRequests = False, returnNumberOfCourseRequests = False, returnNumberOfSeatsAvailable = False, returnNumberOfTransferStudentSections = False, returnObjectIsDirty = False, returnObjectName = False, returnOriginalEstimatedNumberOfSections = False, returnRecordsUpdated = False, returnRowIsReadOnly = False, returnRowIsSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempCourse in the district.

	This function returns a dataframe of every TempCourse in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempCourseEntityOfferedToSection(searchConditions = [], EntityID = 1, returnTempCourseEntityOfferedToSectionID = False, returnCourseEntityOfferedToID = False, returnCourseEntityOfferedToSectionID = False, returnCourseEntityOfferedToSectionRecordExists = False, returnCourseID = False, returnCreatedTime = False, returnEntityIDOfferedTo = False, returnEntityOfferedToCode = False, returnEntityOfferedToName = False, returnIsActiveOverride = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnOriginalMaximumStudentCount = False, returnRowIsSelected = False, returnSchoolYearID = False, returnSeatsAvailable = False, returnSectionCode = False, returnSectionID = False, returnSectionIsActive = False, returnSectionMaximumStudentCount = False, returnSectionReservedSeatCount = False, returnSectionSectionLengthCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempCourseEntityOfferedToSection in the district.

	This function returns a dataframe of every TempCourseEntityOfferedToSection in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourseEntityOfferedToSection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourseEntityOfferedToSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempCourseMasterMassUpdateError(searchConditions = [], EntityID = 1, returnTempCourseMasterMassUpdateErrorID = False, returnBaseTableName = False, returnCreatedTime = False, returnModifiedTime = False, returnSourceDescription = False, returnTableName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempCourseMasterMassUpdateError in the district.

	This function returns a dataframe of every TempCourseMasterMassUpdateError in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourseMasterMassUpdateError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourseMasterMassUpdateError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempCourseMasterMassUpdateErrorDetail(searchConditions = [], EntityID = 1, returnTempCourseMasterMassUpdateErrorDetailID = False, returnCreatedTime = False, returnError = False, returnErrorName = False, returnModifiedTime = False, returnTempCourseMasterMassUpdateErrorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempCourseMasterMassUpdateErrorDetail in the district.

	This function returns a dataframe of every TempCourseMasterMassUpdateErrorDetail in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourseMasterMassUpdateErrorDetail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourseMasterMassUpdateErrorDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempCourseMasterMassUpdateField(searchConditions = [], EntityID = 1, returnTempCourseMasterMassUpdateFieldID = False, returnAffectedPrimaryKey = False, returnBaseTableName = False, returnCourseID = False, returnCreatedTime = False, returnFieldDisplayName = False, returnFieldName = False, returnFriendlyOriginalValue = False, returnFriendlyUpdatedValue = False, returnModifiedTime = False, returnOriginalValue = False, returnSourceDescription = False, returnTableName = False, returnUpdatedValue = False, returnUpdateRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempCourseMasterMassUpdateField in the district.

	This function returns a dataframe of every TempCourseMasterMassUpdateField in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourseMasterMassUpdateField/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourseMasterMassUpdateField/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempDayRotation(searchConditions = [], EntityID = 1, returnTempDayRotationID = False, returnCode = False, returnCreatedTime = False, returnDayRotationID = False, returnModifiedTime = False, returnNote = False, returnObjectIsDirty = False, returnObjectName = False, returnRecordsUpdated = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempDayRotation in the district.

	This function returns a dataframe of every TempDayRotation in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempDayRotation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempDayRotation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempException(searchConditions = [], EntityID = 1, returnTempExceptionID = False, returnCreatedTime = False, returnErrorDetail = False, returnErrorFieldName = False, returnFailedRecordPrimaryKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempException in the district.

	This function returns a dataframe of every TempException in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempException/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempFailedCourse(searchConditions = [], EntityID = 1, returnTempFailedCourseID = False, returnActiveSections = False, returnAveragePerSectionMinimumSectionsRequired = False, returnCodeDescription = False, returnCourseCode = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseLengthID = False, returnCourseSubjectCode = False, returnCourseTypeCode = False, returnCreatedTime = False, returnCurriculumCode = False, returnDefaultSectionLengthID = False, returnDescription = False, returnEarnedCredits = False, returnEntityCode = False, returnEstimatedNumberOfSections = False, returnEstimatedStudentsPerSection = False, returnGradeLevelSummary = False, returnGradingPeriodSetCode = False, returnGradingPeriodSetID = False, returnIsActive = False, returnMinimumSectionsRequired = False, returnModifiedTime = False, returnNewCourseLengthCode = False, returnNewCourseLengthID = False, returnNewGradingPeriodSetCode = False, returnNewGradingPeriodSetID = False, returnNote = False, returnNumberOfAlternateCourseRequests = False, returnNumberOfCourseRequests = False, returnNumberOfSeatsAvailable = False, returnNumberOfTransferStudentSections = False, returnObjectIsDirty = False, returnObjectName = False, returnOriginalEstimatedNumberOfSections = False, returnRecordsUpdated = False, returnRowIsReadOnly = False, returnRowIsSelected = False, returnTempCourseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempFailedCourse in the district.

	This function returns a dataframe of every TempFailedCourse in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedCourse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempFailedDayRotation(searchConditions = [], EntityID = 1, returnTempFailedDayRotationID = False, returnCode = False, returnCreatedTime = False, returnDayRotationID = False, returnModifiedTime = False, returnNote = False, returnObjectIsDirty = False, returnObjectName = False, returnRecordsUpdated = False, returnTempDayRotationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempFailedDayRotation in the district.

	This function returns a dataframe of every TempFailedDayRotation in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedDayRotation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedDayRotation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempFailedSection(searchConditions = [], EntityID = 1, returnTempFailedSectionID = False, returnCourse = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseID = False, returnCourseIsActive = False, returnCourseTypeCode = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnEntityIDCourse = False, returnEntityIDOfferedTo = False, returnErrorCount = False, returnGradeLevelSummary = False, returnHasErrors = False, returnIsActive = False, returnIsSourceSection = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNewCourseLengthCode = False, returnNewCourseLengthID = False, returnNewSectionLengthCode = False, returnNewSectionLengthID = False, returnNote = False, returnNumberOfTransferStudentSections = False, returnPeriodDaySummary = False, returnPrimaryDays = False, returnPrimaryDisplayPeriod = False, returnRowIsReadOnly = False, returnRowIsSelected = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnSectionLengthEndDate = False, returnSectionLengthID = False, returnSectionLengthStartDate = False, returnStaffFullNameFML = False, returnTargetCourse = False, returnTempSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempFailedSection in the district.

	This function returns a dataframe of every TempFailedSection in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedSection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempFailedSectionLengthSubset(searchConditions = [], EntityID = 1, returnTempFailedSectionLengthSubsetID = False, returnCode = False, returnCodeDescription = False, returnCourseLengthCode = False, returnCourseLengthCodeDescription = False, returnCourseLengthID = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnIsFullSectionLength = False, returnIsUpdated = False, returnModifiedTime = False, returnNote = False, returnObjectIsDirty = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnSectionLengthCode = False, returnSectionLengthCodeDescription = False, returnSectionLengthEndDate = False, returnSectionLengthID = False, returnSectionLengthStartDate = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnTempSectionLengthSubsetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempFailedSectionLengthSubset in the district.

	This function returns a dataframe of every TempFailedSectionLengthSubset in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedSectionLengthSubset/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedSectionLengthSubset/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempFailedStaffMeet(searchConditions = [], EntityID = 1, returnTempFailedStaffMeetID = False, returnConflicts = False, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnEffectiveEndDate = False, returnEffectiveStartDate = False, returnErrorCount = False, returnHasAttendanceAccess = False, returnHasConflicts = False, returnHasErrors = False, returnHasGradebookAccess = False, returnIsChecked = False, returnIsLongTermSubstitute = False, returnIsPrimary = False, returnIsSubstitute = False, returnMeetID = False, returnModifiedTime = False, returnNewEffectiveEndDate = False, returnNewEffectiveStartDate = False, returnNewStaffFullNameFML = False, returnNewStaffID = False, returnNote = False, returnSectionCode = False, returnSectionID = False, returnStaffFullNameFML = False, returnStaffID = False, returnStaffMeetID = False, returnTempStaffMeetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempFailedStaffMeet in the district.

	This function returns a dataframe of every TempFailedStaffMeet in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStaffMeet/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStaffMeet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempFailedStudentCourseRequest(searchConditions = [], EntityID = 1, returnTempFailedStudentCourseRequestID = False, returnCourseCode = False, returnCourseDepartmentCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseNumericSchoolYear = False, returnCourseSchoolYearDescription = False, returnCourseSubjectCodeDescription = False, returnCreatedTime = False, returnEarnedCredits = False, returnEntityIDRequestedFrom = False, returnErrorMessage = False, returnFailed = False, returnFullStudentNameLFM = False, returnModifiedTime = False, returnNote = False, returnSectionCode = False, returnSectionlengthSubsetCode = False, returnSectionLengthSubsetID = False, returnSelected = False, returnStudentCourseRequestID = False, returnStudentCourseRequestSectionLengthSubsetID = False, returnStudentID = False, returnStudentNumber = False, returnStudentSectionID = False, returnTempStudentCourseRequestID = False, returnTempStudentEnrollmentRecordID = False, returnTempStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempFailedStudentCourseRequest in the district.

	This function returns a dataframe of every TempFailedStudentCourseRequest in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentCourseRequest/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentCourseRequest/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempFailedStudentCourseRequestToReactivate(searchConditions = [], EntityID = 1, returnTempFailedStudentCourseRequestToReactivateID = False, returnAlternateRank = False, returnAuditRecordIsRequestable = False, returnAuditRecordIsSchedulable = False, returnCourseCode = False, returnCourseCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnDateFrom = False, returnDateTo = False, returnDays = False, returnEarlyExitReasonCodeDescription = False, returnEarlyExitReasonID = False, returnEarnedCreditOverride = False, returnEarnedCredits = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnEntityIDRequestedFrom = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLink = False, returnGradeReferenceID = False, returnIsAlternate = False, returnIsTransferCourse = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnNameRequestedByLFM = False, returnNote = False, returnPeriod = False, returnPreventReactivateCheckboxFromBeingRendered = False, returnRequestSource = False, returnRequestSourceCode = False, returnRequestStatus = False, returnRequestStatusCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthID = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSectionLengthSubsetID = False, returnStaffFullNameFML = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentCourseRequestIDAlternateFor = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionTransactionID = False, returnTempRecordToReactivatePrimaryKeyValue = False, returnTotalEarnedCreditOverride = False, returnTotalFailedCreditOverride = False, returnTransferCourseName = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditTotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempFailedStudentCourseRequestToReactivate in the district.

	This function returns a dataframe of every TempFailedStudentCourseRequestToReactivate in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentCourseRequestToReactivate/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentCourseRequestToReactivate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempFailedStudentCourseRequestToReactivateDetail(searchConditions = [], EntityID = 1, returnTempFailedStudentCourseRequestToReactivateDetailID = False, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnTempRecordToReactivatePrimaryKeyValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempFailedStudentCourseRequestToReactivateDetail in the district.

	This function returns a dataframe of every TempFailedStudentCourseRequestToReactivateDetail in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentCourseRequestToReactivateDetail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentCourseRequestToReactivateDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempFailedStudentSection(searchConditions = [], EntityID = 1, returnTempFailedStudentSectionID = False, returnAutomaticRequestSetting = False, returnAutomaticRequestSettingCode = False, returnAutomaticScheduleSetting = False, returnAutomaticScheduleSettingCode = False, returnCourseCode = False, returnCourseCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnEarlyExitReasonCodeDescription = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNote = False, returnRenderCheckbox = False, returnRowIsReadOnly = False, returnRowIsSelected = False, returnScheduleAllSectionsInGroupOrNone = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionCorequisiteGroupName = False, returnSectionID = False, returnSectionLengthCode = False, returnSectionLengthEndDate = False, returnSectionLengthID = False, returnSectionLengthStartDate = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentGenderCode = False, returnStudentGradeLevelCode = False, returnStudentGradYear = False, returnStudentID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionID = False, returnStudentSectionTransactionIDToUpdate = False, returnTempStudentID = False, returnTempStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempFailedStudentSection in the district.

	This function returns a dataframe of every TempFailedStudentSection in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentSection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempFailedStudentSectionTransaction(searchConditions = [], EntityID = 1, returnTempFailedStudentSectionTransactionID = False, returnCourse = False, returnCreatedTime = False, returnEarlyExitReasonID = False, returnEndDate = False, returnEntityIDCountsAs = False, returnHideNewStudentButton = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnNote = False, returnSectionCode = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionTransactionID = False, returnTempStudentCourseRequestID = False, returnTempStudentCourseRequestToReactivateID = False, returnTempStudentSectionTransactionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempFailedStudentSectionTransaction in the district.

	This function returns a dataframe of every TempFailedStudentSectionTransaction in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentSectionTransaction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentSectionTransaction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempMasterDateChangeDetail(searchConditions = [], EntityID = 1, returnTempMasterDateChangeDetailID = False, returnCreatedTime = False, returnCurrentDate = False, returnDateDescriptor = False, returnDateDescriptorCode = False, returnDisplayLowHighDates = False, returnHighDate = False, returnLowDate = False, returnModifiedTime = False, returnNewDate = False, returnUsedBy = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempMasterDateChangeDetail in the district.

	This function returns a dataframe of every TempMasterDateChangeDetail in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempMasterDateChangeDetail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempMasterDateChangeDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempMeet(searchConditions = [], EntityID = 1, returnTempMeetID = False, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnEndDate = False, returnMeetID = False, returnModifiedTime = False, returnNewEndDate = False, returnNewSectionLengthCode = False, returnNewStartDate = False, returnPrimaryDays = False, returnPrimaryDisplayPeriod = False, returnPrimaryStaffFullNameFML = False, returnRoomNumberDescription = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempMeet in the district.

	This function returns a dataframe of every TempMeet in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempMeet/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempMeet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempSchedulingTeamGradeReference(searchConditions = [], EntityID = 1, returnTempSchedulingTeamGradeReferenceID = False, returnCode = False, returnCreatedTime = False, returnCurrentStudentCount = False, returnDescription = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnOverrideTotalToBeAssignedCount = False, returnOverrideTotalToBeAssignedPercent = False, returnSchedulingTeamGradeReferenceID = False, returnSchedulingTeamID = False, returnSortOrder = False, returnTotalStudents = False, returnTotalToBeAssignedCount = False, returnTotalToBeAssignedPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempSchedulingTeamGradeReference in the district.

	This function returns a dataframe of every TempSchedulingTeamGradeReference in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSchedulingTeamGradeReference/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSchedulingTeamGradeReference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempSection(searchConditions = [], EntityID = 1, returnTempSectionID = False, returnCourse = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseID = False, returnCourseIsActive = False, returnCourseTypeCode = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnEntityIDCourse = False, returnEntityIDOfferedTo = False, returnGradeLevelSummary = False, returnIsActive = False, returnIsSourceSection = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNewCourseLengthCode = False, returnNewCourseLengthID = False, returnNewSectionLengthCode = False, returnNewSectionLengthID = False, returnNote = False, returnNumberOfTransferStudentSections = False, returnPeriodDaySummary = False, returnPrimaryDays = False, returnPrimaryDisplayPeriod = False, returnRowIsReadOnly = False, returnRowIsSelected = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnSectionLengthEndDate = False, returnSectionLengthID = False, returnSectionLengthStartDate = False, returnStaffFullNameFML = False, returnTargetCourse = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempSection in the district.

	This function returns a dataframe of every TempSection in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempSectionLength(searchConditions = [], EntityID = 1, returnTempSectionLengthID = False, returnCode = False, returnCourseLengthCode = False, returnCreatedTime = False, returnEndDate = False, returnIsUpdated = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnSectionLengthID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempSectionLength in the district.

	This function returns a dataframe of every TempSectionLength in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSectionLength/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSectionLength/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempSectionLengthSubset(searchConditions = [], EntityID = 1, returnTempSectionLengthSubsetID = False, returnCode = False, returnCodeDescription = False, returnCourseLengthCode = False, returnCourseLengthCodeDescription = False, returnCourseLengthID = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnIsFullSectionLength = False, returnIsUpdated = False, returnModifiedTime = False, returnObjectIsDirty = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnSectionLengthCode = False, returnSectionLengthCodeDescription = False, returnSectionLengthEndDate = False, returnSectionLengthID = False, returnSectionLengthStartDate = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempSectionLengthSubset in the district.

	This function returns a dataframe of every TempSectionLengthSubset in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSectionLengthSubset/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSectionLengthSubset/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStaffMeet(searchConditions = [], EntityID = 1, returnTempStaffMeetID = False, returnConflicts = False, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnEffectiveEndDate = False, returnEffectiveStartDate = False, returnHasAttendanceAccess = False, returnHasConflicts = False, returnHasGradebookAccess = False, returnIsChecked = False, returnIsLongTermSubstitute = False, returnIsPrimary = False, returnIsSubstitute = False, returnMeetID = False, returnModifiedTime = False, returnNewEffectiveEndDate = False, returnNewEffectiveStartDate = False, returnNewStaffFullNameFML = False, returnNewStaffID = False, returnNote = False, returnSectionCode = False, returnSectionID = False, returnStaffFullNameFML = False, returnStaffID = False, returnStaffMeetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStaffMeet in the district.

	This function returns a dataframe of every TempStaffMeet in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStaffMeet/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStaffMeet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudent(searchConditions = [], EntityID = 1, returnTempStudentID = False, returnCourseRequestCount = False, returnCreatedTime = False, returnCurrentActive = False, returnFullNameLFM = False, returnGenderCode = False, returnGradeLevelCode = False, returnGradeReferenceID = False, returnGradYear = False, returnHasConflictedStudentCourseRequest = False, returnHasFailedUpdate = False, returnHomeRoomCode = False, returnIsSelected = False, returnModifiedTime = False, returnSchoolName = False, returnStudentID = False, returnStudentNumber = False, returnStudentSectionCount = False, returnStudentTypeCodeDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudent in the district.

	This function returns a dataframe of every TempStudent in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudent/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentCourseRequest(searchConditions = [], EntityID = 1, returnTempStudentCourseRequestID = False, returnCourseCode = False, returnCourseDepartmentCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseNumericSchoolYear = False, returnCourseSchoolYearDescription = False, returnCourseSubjectCodeDescription = False, returnCreatedTime = False, returnEarnedCredits = False, returnEntityIDRequestedFrom = False, returnErrorMessage = False, returnFailed = False, returnFullStudentNameLFM = False, returnModifiedTime = False, returnSectionCode = False, returnSectionlengthSubsetCode = False, returnSectionLengthSubsetID = False, returnSelected = False, returnStudentCourseRequestID = False, returnStudentCourseRequestSectionLengthSubsetID = False, returnStudentID = False, returnStudentNumber = False, returnStudentSectionID = False, returnTempStudentEnrollmentRecordID = False, returnTempStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentCourseRequest in the district.

	This function returns a dataframe of every TempStudentCourseRequest in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentCourseRequest/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentCourseRequest/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentCourseRequestSectionLengthSubset(searchConditions = [], EntityID = 1, returnTempStudentCourseRequestSectionLengthSubsetID = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionLengthSubsetID = False, returnStudentCourseRequestID = False, returnStudentCourseRequestSectionLengthSubsetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentCourseRequestSectionLengthSubset in the district.

	This function returns a dataframe of every TempStudentCourseRequestSectionLengthSubset in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentCourseRequestSectionLengthSubset/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentCourseRequestSectionLengthSubset/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentCourseRequestToReactivateMN(searchConditions = [], EntityID = 1, returnTempStudentCourseRequestToReactivateMNID = False, returnAlternateRank = False, returnAuditRecordIsRequestable = False, returnAuditRecordIsSchedulable = False, returnCourseCode = False, returnCourseCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnDateFrom = False, returnDateTo = False, returnDays = False, returnEarlyExitReasonCodeDescription = False, returnEarlyExitReasonID = False, returnEarnedCreditOverride = False, returnEarnedCredits = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnEntityIDRequestedFrom = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLink = False, returnGradeReferenceID = False, returnIsAlternate = False, returnIsTransferCourse = False, returnIsTSAProficient = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnNameRequestedByLFM = False, returnPeriod = False, returnPreventReactivateCheckboxFromBeingRendered = False, returnRequestSource = False, returnRequestSourceCode = False, returnRequestStatus = False, returnRequestStatusCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthID = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSectionLengthSubsetID = False, returnStaffFullNameFML = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentCourseRequestIDAlternateFor = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionTransactionID = False, returnTotalEarnedCreditOverride = False, returnTotalFailedCreditOverride = False, returnTransferCourseName = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditTotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentCourseRequestToReactivateMN in the district.

	This function returns a dataframe of every TempStudentCourseRequestToReactivateMN in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentCourseRequestToReactivateMN/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentCourseRequestToReactivateMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentCourseRequestToReactivateNonState(searchConditions = [], EntityID = 1, returnTempStudentCourseRequestToReactivateNonStateID = False, returnAlternateRank = False, returnAuditRecordIsRequestable = False, returnAuditRecordIsSchedulable = False, returnCourseCode = False, returnCourseCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnDateFrom = False, returnDateTo = False, returnDays = False, returnEarlyExitReasonCodeDescription = False, returnEarlyExitReasonID = False, returnEarnedCreditOverride = False, returnEarnedCredits = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnEntityIDRequestedFrom = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLink = False, returnGradeReferenceID = False, returnIsAlternate = False, returnIsTransferCourse = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnNameRequestedByLFM = False, returnPeriod = False, returnPreventReactivateCheckboxFromBeingRendered = False, returnRequestSource = False, returnRequestSourceCode = False, returnRequestStatus = False, returnRequestStatusCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthID = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSectionLengthSubsetID = False, returnStaffFullNameFML = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentCourseRequestIDAlternateFor = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionTransactionID = False, returnTotalEarnedCreditOverride = False, returnTotalFailedCreditOverride = False, returnTransferCourseName = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditTotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentCourseRequestToReactivateNonState in the district.

	This function returns a dataframe of every TempStudentCourseRequestToReactivateNonState in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentCourseRequestToReactivateNonState/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentCourseRequestToReactivateNonState/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentSchedulingCategory(searchConditions = [], EntityID = 1, returnTempStudentSchedulingCategoryID = False, returnCreatedTime = False, returnMessage = False, returnModifiedTime = False, returnProposedCategoriesDisplayValue = False, returnProposedTargetCategoryIDsToDeleteCSV = False, returnProposedTargetCategoryIDsToInsertCSV = False, returnSourceCategoriesDisplayValue = False, returnSourceCategoryIDsCSV = False, returnSourceStudentEntityYearID = False, returnStudentNameLFM = False, returnTargetCategoriesDisplayValue = False, returnTargetCategoryIDsCSV = False, returnTargetStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentSchedulingCategory in the district.

	This function returns a dataframe of every TempStudentSchedulingCategory in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentSchedulingCategory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentSchedulingCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentSchedulingTeam(searchConditions = [], EntityID = 1, returnTempStudentSchedulingTeamID = False, returnCreatedTime = False, returnMessage = False, returnModifiedTime = False, returnSourceSchedulingTeamCode = False, returnSourceSchedulingTeamDescription = False, returnSourceSchedulingTeamID = False, returnSourceSchoolYearDescription = False, returnSourceStudentEntityYearID = False, returnStudentNameLFM = False, returnTargetSchedulingTeamCode = False, returnTargetSchedulingTeamDescription = False, returnTargetSchedulingTeamID = False, returnTargetSchoolYearDescription = False, returnTargetStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentSchedulingTeam in the district.

	This function returns a dataframe of every TempStudentSchedulingTeam in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentSchedulingTeam/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentSchedulingTeam/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentSection(searchConditions = [], EntityID = 1, returnTempStudentSectionID = False, returnAutomaticRequestSetting = False, returnAutomaticRequestSettingCode = False, returnAutomaticScheduleSetting = False, returnAutomaticScheduleSettingCode = False, returnCourseCode = False, returnCourseCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnEarlyExitReasonCodeDescription = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNote = False, returnRenderCheckbox = False, returnRowIsReadOnly = False, returnRowIsSelected = False, returnScheduleAllSectionsInGroupOrNone = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionCorequisiteGroupName = False, returnSectionID = False, returnSectionLengthCode = False, returnSectionLengthEndDate = False, returnSectionLengthID = False, returnSectionLengthStartDate = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentGenderCode = False, returnStudentGradeLevelCode = False, returnStudentGradYear = False, returnStudentID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionID = False, returnStudentSectionTransactionIDToUpdate = False, returnTempStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentSection in the district.

	This function returns a dataframe of every TempStudentSection in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentSection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentSectionTransaction(searchConditions = [], EntityID = 1, returnTempStudentSectionTransactionID = False, returnCreatedTime = False, returnEarlyExitReasonID = False, returnEndDate = False, returnEntityIDCountsAs = False, returnHideNewStudentButton = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentSectionTransactionID = False, returnTempStudentCourseRequestID = False, returnTempStudentCourseRequestToReactivateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentSectionTransaction in the district.

	This function returns a dataframe of every TempStudentSectionTransaction in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentSectionTransaction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentSectionTransaction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempSubstituteAssignment(searchConditions = [], EntityID = 1, returnTempSubstituteAssignmentID = False, returnConflicts = False, returnCourseCodeSectionCode = False, returnCreatedTime = False, returnDate = False, returnDisplayPeriodID = False, returnDisplayPeriodSortNumber = False, returnEntityID = False, returnHasAttendanceAccess = False, returnHasConflicts = False, returnHasGradebookAccess = False, returnIsLongTermSubstitute = False, returnMeetID = False, returnModifiedTime = False, returnPeriod = False, returnSchoolYearID = False, returnSectionAlreadyCovered = False, returnSectionID = False, returnSourceStaffID = False, returnStaffMeetID = False, returnStaffName = False, returnSubstituteStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempSubstituteAssignment in the district.

	This function returns a dataframe of every TempSubstituteAssignment in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSubstituteAssignment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSubstituteAssignment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)