# This module contains Scheduling functions.

from .Utilities import make_request

import pandas as pd

import json

import re

def getEveryAvailabilityCourseFilter(EntityID = 1, page = 1, pageSize = 100, returnAvailabilityCourseFilterID = True, returnAvailabilityCourseFilterIDClonedFrom = False, returnAvailabilityCourseFilterIDClonedTo = False, returnCode = False, returnCodeDescription = False, returnCourseTypeIDInclusionList = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnFilter = False, returnIncludeCategoryLunch = False, returnIncludeCategoryRegular = False, returnIncludeCategoryStudyHall = False, returnIncludeCoursesHiddenFromRequestEntry = False, returnIncludeCoursesWithNoCourseType = False, returnIncludeElective = False, returnIncludeInactiveCourses = False, returnIncludeOfferedCourses = False, returnIncludeRequired = False, returnIncludeSchedulingTypeManuallyScheduled = False, returnIncludeSchedulingTypeNormal = False, returnIncludeSchedulingTypeSpecialEducation = False, returnModifiedTime = False, returnSchoolYearID = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityCourseFilter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAvailabilityCourseFilter(AvailabilityCourseFilterID, EntityID = 1, returnAvailabilityCourseFilterID = True, returnAvailabilityCourseFilterIDClonedFrom = False, returnAvailabilityCourseFilterIDClonedTo = False, returnCode = False, returnCodeDescription = False, returnCourseTypeIDInclusionList = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnFilter = False, returnIncludeCategoryLunch = False, returnIncludeCategoryRegular = False, returnIncludeCategoryStudyHall = False, returnIncludeCoursesHiddenFromRequestEntry = False, returnIncludeCoursesWithNoCourseType = False, returnIncludeElective = False, returnIncludeInactiveCourses = False, returnIncludeOfferedCourses = False, returnIncludeRequired = False, returnIncludeSchedulingTypeManuallyScheduled = False, returnIncludeSchedulingTypeNormal = False, returnIncludeSchedulingTypeSpecialEducation = False, returnModifiedTime = False, returnSchoolYearID = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityCourseFilter/" + str(AvailabilityCourseFilterID), verb = "get", return_params_list = return_params_list)

def modifyAvailabilityCourseFilter(AvailabilityCourseFilterID, EntityID = 1, setAvailabilityCourseFilterIDClonedFrom = None, setCode = None, setCourseTypeIDInclusionList = None, setDescription = None, setEntityID = None, setFilter = None, setIncludeCategoryLunch = None, setIncludeCategoryRegular = None, setIncludeCategoryStudyHall = None, setIncludeCoursesHiddenFromRequestEntry = None, setIncludeCoursesWithNoCourseType = None, setIncludeElective = None, setIncludeInactiveCourses = None, setIncludeOfferedCourses = None, setIncludeRequired = None, setIncludeSchedulingTypeManuallyScheduled = None, setIncludeSchedulingTypeNormal = None, setIncludeSchedulingTypeSpecialEducation = None, setSchoolYearID = None, setSkywardID = None, setRelationships = None, returnAvailabilityCourseFilterID = True, returnAvailabilityCourseFilterIDClonedFrom = False, returnAvailabilityCourseFilterIDClonedTo = False, returnCode = False, returnCodeDescription = False, returnCourseTypeIDInclusionList = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnFilter = False, returnIncludeCategoryLunch = False, returnIncludeCategoryRegular = False, returnIncludeCategoryStudyHall = False, returnIncludeCoursesHiddenFromRequestEntry = False, returnIncludeCoursesWithNoCourseType = False, returnIncludeElective = False, returnIncludeInactiveCourses = False, returnIncludeOfferedCourses = False, returnIncludeRequired = False, returnIncludeSchedulingTypeManuallyScheduled = False, returnIncludeSchedulingTypeNormal = False, returnIncludeSchedulingTypeSpecialEducation = False, returnModifiedTime = False, returnSchoolYearID = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityCourseFilter/" + str(AvailabilityCourseFilterID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAvailabilityCourseFilter(EntityID = 1, setAvailabilityCourseFilterIDClonedFrom = None, setCode = None, setCourseTypeIDInclusionList = None, setDescription = None, setEntityID = None, setFilter = None, setIncludeCategoryLunch = None, setIncludeCategoryRegular = None, setIncludeCategoryStudyHall = None, setIncludeCoursesHiddenFromRequestEntry = None, setIncludeCoursesWithNoCourseType = None, setIncludeElective = None, setIncludeInactiveCourses = None, setIncludeOfferedCourses = None, setIncludeRequired = None, setIncludeSchedulingTypeManuallyScheduled = None, setIncludeSchedulingTypeNormal = None, setIncludeSchedulingTypeSpecialEducation = None, setSchoolYearID = None, setSkywardID = None, setRelationships = None, returnAvailabilityCourseFilterID = True, returnAvailabilityCourseFilterIDClonedFrom = False, returnAvailabilityCourseFilterIDClonedTo = False, returnCode = False, returnCodeDescription = False, returnCourseTypeIDInclusionList = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnFilter = False, returnIncludeCategoryLunch = False, returnIncludeCategoryRegular = False, returnIncludeCategoryStudyHall = False, returnIncludeCoursesHiddenFromRequestEntry = False, returnIncludeCoursesWithNoCourseType = False, returnIncludeElective = False, returnIncludeInactiveCourses = False, returnIncludeOfferedCourses = False, returnIncludeRequired = False, returnIncludeSchedulingTypeManuallyScheduled = False, returnIncludeSchedulingTypeNormal = False, returnIncludeSchedulingTypeSpecialEducation = False, returnModifiedTime = False, returnSchoolYearID = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityCourseFilter/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAvailabilityCourseFilter(AvailabilityCourseFilterID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAvailabilityFilterCourseStudent(EntityID = 1, page = 1, pageSize = 100, returnAvailabilityFilterCourseStudentID = True, returnAvailabilityCourseFilterID = False, returnAvailabilityFilterCourseStudentIDClonedFrom = False, returnAvailabilityStudentFilterID = False, returnAvailableEndDate = False, returnAvailableStartDate = False, returnCreatedTime = False, returnDescription = False, returnExcludeAvailabilityListBoolUpdatedManually = False, returnExcludeAvailabilityListInNightlyUpdateTask = False, returnMaximumAlternateCourseRequests = False, returnMaximumAlternateCredits = False, returnMaximumCourseRequests = False, returnMaximumCredits = False, returnModifiedTime = False, returnRequestEntryEndDate = False, returnRequestEntryEndDateTime = False, returnRequestEntryEndTime = False, returnRequestEntryStartDate = False, returnRequestEntryStartDateTime = False, returnRequestEntryStartTime = False, returnUseCourseRequestCountMaximum = False, returnUseCreditsMaximum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityFilterCourseStudent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAvailabilityFilterCourseStudent(AvailabilityFilterCourseStudentID, EntityID = 1, returnAvailabilityFilterCourseStudentID = True, returnAvailabilityCourseFilterID = False, returnAvailabilityFilterCourseStudentIDClonedFrom = False, returnAvailabilityStudentFilterID = False, returnAvailableEndDate = False, returnAvailableStartDate = False, returnCreatedTime = False, returnDescription = False, returnExcludeAvailabilityListBoolUpdatedManually = False, returnExcludeAvailabilityListInNightlyUpdateTask = False, returnMaximumAlternateCourseRequests = False, returnMaximumAlternateCredits = False, returnMaximumCourseRequests = False, returnMaximumCredits = False, returnModifiedTime = False, returnRequestEntryEndDate = False, returnRequestEntryEndDateTime = False, returnRequestEntryEndTime = False, returnRequestEntryStartDate = False, returnRequestEntryStartDateTime = False, returnRequestEntryStartTime = False, returnUseCourseRequestCountMaximum = False, returnUseCreditsMaximum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityFilterCourseStudent/" + str(AvailabilityFilterCourseStudentID), verb = "get", return_params_list = return_params_list)

def modifyAvailabilityFilterCourseStudent(AvailabilityFilterCourseStudentID, EntityID = 1, setAvailabilityCourseFilterID = None, setAvailabilityFilterCourseStudentIDClonedFrom = None, setAvailabilityStudentFilterID = None, setAvailableEndDate = None, setAvailableStartDate = None, setDescription = None, setExcludeAvailabilityListBoolUpdatedManually = None, setExcludeAvailabilityListInNightlyUpdateTask = None, setMaximumAlternateCourseRequests = None, setMaximumAlternateCredits = None, setMaximumCourseRequests = None, setMaximumCredits = None, setRequestEntryEndDate = None, setRequestEntryEndDateTime = None, setRequestEntryEndTime = None, setRequestEntryStartDate = None, setRequestEntryStartDateTime = None, setRequestEntryStartTime = None, setUseCourseRequestCountMaximum = None, setUseCreditsMaximum = None, setRelationships = None, returnAvailabilityFilterCourseStudentID = True, returnAvailabilityCourseFilterID = False, returnAvailabilityFilterCourseStudentIDClonedFrom = False, returnAvailabilityStudentFilterID = False, returnAvailableEndDate = False, returnAvailableStartDate = False, returnCreatedTime = False, returnDescription = False, returnExcludeAvailabilityListBoolUpdatedManually = False, returnExcludeAvailabilityListInNightlyUpdateTask = False, returnMaximumAlternateCourseRequests = False, returnMaximumAlternateCredits = False, returnMaximumCourseRequests = False, returnMaximumCredits = False, returnModifiedTime = False, returnRequestEntryEndDate = False, returnRequestEntryEndDateTime = False, returnRequestEntryEndTime = False, returnRequestEntryStartDate = False, returnRequestEntryStartDateTime = False, returnRequestEntryStartTime = False, returnUseCourseRequestCountMaximum = False, returnUseCreditsMaximum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityFilterCourseStudent/" + str(AvailabilityFilterCourseStudentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAvailabilityFilterCourseStudent(EntityID = 1, setAvailabilityCourseFilterID = None, setAvailabilityFilterCourseStudentIDClonedFrom = None, setAvailabilityStudentFilterID = None, setAvailableEndDate = None, setAvailableStartDate = None, setDescription = None, setExcludeAvailabilityListBoolUpdatedManually = None, setExcludeAvailabilityListInNightlyUpdateTask = None, setMaximumAlternateCourseRequests = None, setMaximumAlternateCredits = None, setMaximumCourseRequests = None, setMaximumCredits = None, setRequestEntryEndDate = None, setRequestEntryEndDateTime = None, setRequestEntryEndTime = None, setRequestEntryStartDate = None, setRequestEntryStartDateTime = None, setRequestEntryStartTime = None, setUseCourseRequestCountMaximum = None, setUseCreditsMaximum = None, setRelationships = None, returnAvailabilityFilterCourseStudentID = True, returnAvailabilityCourseFilterID = False, returnAvailabilityFilterCourseStudentIDClonedFrom = False, returnAvailabilityStudentFilterID = False, returnAvailableEndDate = False, returnAvailableStartDate = False, returnCreatedTime = False, returnDescription = False, returnExcludeAvailabilityListBoolUpdatedManually = False, returnExcludeAvailabilityListInNightlyUpdateTask = False, returnMaximumAlternateCourseRequests = False, returnMaximumAlternateCredits = False, returnMaximumCourseRequests = False, returnMaximumCredits = False, returnModifiedTime = False, returnRequestEntryEndDate = False, returnRequestEntryEndDateTime = False, returnRequestEntryEndTime = False, returnRequestEntryStartDate = False, returnRequestEntryStartDateTime = False, returnRequestEntryStartTime = False, returnUseCourseRequestCountMaximum = False, returnUseCreditsMaximum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityFilterCourseStudent/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAvailabilityFilterCourseStudent(AvailabilityFilterCourseStudentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAvailabilityFilterCourseStudentCourse(EntityID = 1, page = 1, pageSize = 100, returnAvailabilityFilterCourseStudentCourseID = True, returnAvailabilityFilterCourseStudentID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityFilterCourseStudentCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAvailabilityFilterCourseStudentCourse(AvailabilityFilterCourseStudentCourseID, EntityID = 1, returnAvailabilityFilterCourseStudentCourseID = True, returnAvailabilityFilterCourseStudentID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityFilterCourseStudentCourse/" + str(AvailabilityFilterCourseStudentCourseID), verb = "get", return_params_list = return_params_list)

def modifyAvailabilityFilterCourseStudentCourse(AvailabilityFilterCourseStudentCourseID, EntityID = 1, setAvailabilityFilterCourseStudentID = None, setCourseID = None, setRelationships = None, returnAvailabilityFilterCourseStudentCourseID = True, returnAvailabilityFilterCourseStudentID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityFilterCourseStudentCourse/" + str(AvailabilityFilterCourseStudentCourseID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAvailabilityFilterCourseStudentCourse(EntityID = 1, setAvailabilityFilterCourseStudentID = None, setCourseID = None, setRelationships = None, returnAvailabilityFilterCourseStudentCourseID = True, returnAvailabilityFilterCourseStudentID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityFilterCourseStudentCourse/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAvailabilityFilterCourseStudentCourse(AvailabilityFilterCourseStudentCourseID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAvailabilityFilterCourseStudentStudent(EntityID = 1, page = 1, pageSize = 100, returnAvailabilityFilterCourseStudentStudentID = True, returnAvailabilityFilterCourseStudentID = False, returnCreatedTime = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityFilterCourseStudentStudent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAvailabilityFilterCourseStudentStudent(AvailabilityFilterCourseStudentStudentID, EntityID = 1, returnAvailabilityFilterCourseStudentStudentID = True, returnAvailabilityFilterCourseStudentID = False, returnCreatedTime = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityFilterCourseStudentStudent/" + str(AvailabilityFilterCourseStudentStudentID), verb = "get", return_params_list = return_params_list)

def modifyAvailabilityFilterCourseStudentStudent(AvailabilityFilterCourseStudentStudentID, EntityID = 1, setAvailabilityFilterCourseStudentID = None, setStudentID = None, setRelationships = None, returnAvailabilityFilterCourseStudentStudentID = True, returnAvailabilityFilterCourseStudentID = False, returnCreatedTime = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityFilterCourseStudentStudent/" + str(AvailabilityFilterCourseStudentStudentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAvailabilityFilterCourseStudentStudent(EntityID = 1, setAvailabilityFilterCourseStudentID = None, setStudentID = None, setRelationships = None, returnAvailabilityFilterCourseStudentStudentID = True, returnAvailabilityFilterCourseStudentID = False, returnCreatedTime = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityFilterCourseStudentStudent/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAvailabilityFilterCourseStudentStudent(AvailabilityFilterCourseStudentStudentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAvailabilityStudentFilter(EntityID = 1, page = 1, pageSize = 100, returnAvailabilityStudentFilterID = True, returnAvailabilityStudentFilterIDClonedFrom = False, returnAvailabilityStudentFilterIDClonedTo = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnFilter = False, returnGradeReferenceIDInclusionList = False, returnModifiedTime = False, returnSchoolYearID = False, returnSkywardID = False, returnStudentTypeIDInclusionList = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityStudentFilter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAvailabilityStudentFilter(AvailabilityStudentFilterID, EntityID = 1, returnAvailabilityStudentFilterID = True, returnAvailabilityStudentFilterIDClonedFrom = False, returnAvailabilityStudentFilterIDClonedTo = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnFilter = False, returnGradeReferenceIDInclusionList = False, returnModifiedTime = False, returnSchoolYearID = False, returnSkywardID = False, returnStudentTypeIDInclusionList = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityStudentFilter/" + str(AvailabilityStudentFilterID), verb = "get", return_params_list = return_params_list)

def modifyAvailabilityStudentFilter(AvailabilityStudentFilterID, EntityID = 1, setAvailabilityStudentFilterIDClonedFrom = None, setCode = None, setDescription = None, setEntityID = None, setFilter = None, setGradeReferenceIDInclusionList = None, setSchoolYearID = None, setSkywardID = None, setStudentTypeIDInclusionList = None, setRelationships = None, returnAvailabilityStudentFilterID = True, returnAvailabilityStudentFilterIDClonedFrom = False, returnAvailabilityStudentFilterIDClonedTo = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnFilter = False, returnGradeReferenceIDInclusionList = False, returnModifiedTime = False, returnSchoolYearID = False, returnSkywardID = False, returnStudentTypeIDInclusionList = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityStudentFilter/" + str(AvailabilityStudentFilterID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAvailabilityStudentFilter(EntityID = 1, setAvailabilityStudentFilterIDClonedFrom = None, setCode = None, setDescription = None, setEntityID = None, setFilter = None, setGradeReferenceIDInclusionList = None, setSchoolYearID = None, setSkywardID = None, setStudentTypeIDInclusionList = None, setRelationships = None, returnAvailabilityStudentFilterID = True, returnAvailabilityStudentFilterIDClonedFrom = False, returnAvailabilityStudentFilterIDClonedTo = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnFilter = False, returnGradeReferenceIDInclusionList = False, returnModifiedTime = False, returnSchoolYearID = False, returnSkywardID = False, returnStudentTypeIDInclusionList = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/AvailabilityStudentFilter/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAvailabilityStudentFilter(AvailabilityStudentFilterID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryBaseRunAnalysis(EntityID = 1, page = 1, pageSize = 100, returnBaseRunAnalysisID = True, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnRunType = False, returnRunTypeCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDPerformer = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/BaseRunAnalysis/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getBaseRunAnalysis(BaseRunAnalysisID, EntityID = 1, returnBaseRunAnalysisID = True, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnRunType = False, returnRunTypeCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDPerformer = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/BaseRunAnalysis/" + str(BaseRunAnalysisID), verb = "get", return_params_list = return_params_list)

def modifyBaseRunAnalysis(BaseRunAnalysisID, EntityID = 1, setEntityID = None, setRunType = None, setRunTypeCode = None, setSchoolYearID = None, setUserIDPerformer = None, setRelationships = None, returnBaseRunAnalysisID = True, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnRunType = False, returnRunTypeCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDPerformer = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/BaseRunAnalysis/" + str(BaseRunAnalysisID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createBaseRunAnalysis(EntityID = 1, setEntityID = None, setRunType = None, setRunTypeCode = None, setSchoolYearID = None, setUserIDPerformer = None, setRelationships = None, returnBaseRunAnalysisID = True, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnRunType = False, returnRunTypeCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDPerformer = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/BaseRunAnalysis/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteBaseRunAnalysis(BaseRunAnalysisID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryBlockPeriod(EntityID = 1, page = 1, pageSize = 100, returnBlockPeriodID = True, returnBlockPeriodIDClonedFrom = False, returnBlockPeriodIDClonedTo = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnHasDisplayPeriods = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/BlockPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getBlockPeriod(BlockPeriodID, EntityID = 1, returnBlockPeriodID = True, returnBlockPeriodIDClonedFrom = False, returnBlockPeriodIDClonedTo = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnHasDisplayPeriods = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/BlockPeriod/" + str(BlockPeriodID), verb = "get", return_params_list = return_params_list)

def modifyBlockPeriod(BlockPeriodID, EntityID = 1, setBlockPeriodIDClonedFrom = None, setCode = None, setDescription = None, setEntityID = None, setSchoolYearID = None, setRelationships = None, returnBlockPeriodID = True, returnBlockPeriodIDClonedFrom = False, returnBlockPeriodIDClonedTo = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnHasDisplayPeriods = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/BlockPeriod/" + str(BlockPeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createBlockPeriod(EntityID = 1, setBlockPeriodIDClonedFrom = None, setCode = None, setDescription = None, setEntityID = None, setSchoolYearID = None, setRelationships = None, returnBlockPeriodID = True, returnBlockPeriodIDClonedFrom = False, returnBlockPeriodIDClonedTo = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnHasDisplayPeriods = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/BlockPeriod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteBlockPeriod(BlockPeriodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryBlockPeriodDisplayPeriod(EntityID = 1, page = 1, pageSize = 100, returnBlockPeriodDisplayPeriodID = True, returnBlockPeriodDisplayPeriodIDClonedFrom = False, returnBlockPeriodID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/BlockPeriodDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getBlockPeriodDisplayPeriod(BlockPeriodDisplayPeriodID, EntityID = 1, returnBlockPeriodDisplayPeriodID = True, returnBlockPeriodDisplayPeriodIDClonedFrom = False, returnBlockPeriodID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/BlockPeriodDisplayPeriod/" + str(BlockPeriodDisplayPeriodID), verb = "get", return_params_list = return_params_list)

def modifyBlockPeriodDisplayPeriod(BlockPeriodDisplayPeriodID, EntityID = 1, setBlockPeriodDisplayPeriodIDClonedFrom = None, setBlockPeriodID = None, setDisplayPeriodID = None, setRelationships = None, returnBlockPeriodDisplayPeriodID = True, returnBlockPeriodDisplayPeriodIDClonedFrom = False, returnBlockPeriodID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/BlockPeriodDisplayPeriod/" + str(BlockPeriodDisplayPeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createBlockPeriodDisplayPeriod(EntityID = 1, setBlockPeriodDisplayPeriodIDClonedFrom = None, setBlockPeriodID = None, setDisplayPeriodID = None, setRelationships = None, returnBlockPeriodDisplayPeriodID = True, returnBlockPeriodDisplayPeriodIDClonedFrom = False, returnBlockPeriodID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/BlockPeriodDisplayPeriod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteBlockPeriodDisplayPeriod(BlockPeriodDisplayPeriodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigEntityYear(EntityID = 1, page = 1, pageSize = 100, returnConfigEntityYearID = True, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/ConfigEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigEntityYear(ConfigEntityYearID, EntityID = 1, returnConfigEntityYearID = True, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/ConfigEntityYear/" + str(ConfigEntityYearID), verb = "get", return_params_list = return_params_list)

def modifyConfigEntityYear(ConfigEntityYearID, EntityID = 1, setConfigEntityYearIDClonedFrom = None, setEntityID = None, setSchoolYearID = None, setRelationships = None, returnConfigEntityYearID = True, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/ConfigEntityYear/" + str(ConfigEntityYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigEntityYear(EntityID = 1, setConfigEntityYearIDClonedFrom = None, setEntityID = None, setSchoolYearID = None, setRelationships = None, returnConfigEntityYearID = True, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/ConfigEntityYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigEntityYear(ConfigEntityYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCourseAlternate(EntityID = 1, page = 1, pageSize = 100, returnCourseAlternateID = True, returnCourseAlternateIDClonedFrom = False, returnCourseIDAlternate = False, returnCourseIDPrimary = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseAlternate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCourseAlternate(CourseAlternateID, EntityID = 1, returnCourseAlternateID = True, returnCourseAlternateIDClonedFrom = False, returnCourseIDAlternate = False, returnCourseIDPrimary = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseAlternate/" + str(CourseAlternateID), verb = "get", return_params_list = return_params_list)

def modifyCourseAlternate(CourseAlternateID, EntityID = 1, setCourseAlternateIDClonedFrom = None, setCourseIDAlternate = None, setCourseIDPrimary = None, setRelationships = None, returnCourseAlternateID = True, returnCourseAlternateIDClonedFrom = False, returnCourseIDAlternate = False, returnCourseIDPrimary = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseAlternate/" + str(CourseAlternateID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCourseAlternate(EntityID = 1, setCourseAlternateIDClonedFrom = None, setCourseIDAlternate = None, setCourseIDPrimary = None, setRelationships = None, returnCourseAlternateID = True, returnCourseAlternateIDClonedFrom = False, returnCourseIDAlternate = False, returnCourseIDPrimary = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseAlternate/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCourseAlternate(CourseAlternateID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCourseCorequisiteGroup(EntityID = 1, page = 1, pageSize = 100, returnCourseCorequisiteGroupID = True, returnAutomaticRequestSetting = False, returnAutomaticRequestSettingCode = False, returnCourseCorequisiteGroupIDClonedFrom = False, returnCourseCorequisiteGroupIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnDisplayPeriodMatch = False, returnDisplayPeriodMatchCode = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnOverlap = False, returnOverlapCode = False, returnScheduleAllCoursesInGroupOrNone = False, returnSchoolYearID = False, returnStaffMatch = False, returnStaffMatchCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseCorequisiteGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCourseCorequisiteGroup(CourseCorequisiteGroupID, EntityID = 1, returnCourseCorequisiteGroupID = True, returnAutomaticRequestSetting = False, returnAutomaticRequestSettingCode = False, returnCourseCorequisiteGroupIDClonedFrom = False, returnCourseCorequisiteGroupIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnDisplayPeriodMatch = False, returnDisplayPeriodMatchCode = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnOverlap = False, returnOverlapCode = False, returnScheduleAllCoursesInGroupOrNone = False, returnSchoolYearID = False, returnStaffMatch = False, returnStaffMatchCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseCorequisiteGroup/" + str(CourseCorequisiteGroupID), verb = "get", return_params_list = return_params_list)

def modifyCourseCorequisiteGroup(CourseCorequisiteGroupID, EntityID = 1, setAutomaticRequestSetting = None, setAutomaticRequestSettingCode = None, setCourseCorequisiteGroupIDClonedFrom = None, setDescription = None, setDisplayPeriodMatch = None, setDisplayPeriodMatchCode = None, setEntityGroupKey = None, setEntityID = None, setName = None, setOverlap = None, setOverlapCode = None, setScheduleAllCoursesInGroupOrNone = None, setSchoolYearID = None, setStaffMatch = None, setStaffMatchCode = None, setRelationships = None, returnCourseCorequisiteGroupID = True, returnAutomaticRequestSetting = False, returnAutomaticRequestSettingCode = False, returnCourseCorequisiteGroupIDClonedFrom = False, returnCourseCorequisiteGroupIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnDisplayPeriodMatch = False, returnDisplayPeriodMatchCode = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnOverlap = False, returnOverlapCode = False, returnScheduleAllCoursesInGroupOrNone = False, returnSchoolYearID = False, returnStaffMatch = False, returnStaffMatchCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseCorequisiteGroup/" + str(CourseCorequisiteGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCourseCorequisiteGroup(EntityID = 1, setAutomaticRequestSetting = None, setAutomaticRequestSettingCode = None, setCourseCorequisiteGroupIDClonedFrom = None, setDescription = None, setDisplayPeriodMatch = None, setDisplayPeriodMatchCode = None, setEntityGroupKey = None, setEntityID = None, setName = None, setOverlap = None, setOverlapCode = None, setScheduleAllCoursesInGroupOrNone = None, setSchoolYearID = None, setStaffMatch = None, setStaffMatchCode = None, setRelationships = None, returnCourseCorequisiteGroupID = True, returnAutomaticRequestSetting = False, returnAutomaticRequestSettingCode = False, returnCourseCorequisiteGroupIDClonedFrom = False, returnCourseCorequisiteGroupIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnDisplayPeriodMatch = False, returnDisplayPeriodMatchCode = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnOverlap = False, returnOverlapCode = False, returnScheduleAllCoursesInGroupOrNone = False, returnSchoolYearID = False, returnStaffMatch = False, returnStaffMatchCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseCorequisiteGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCourseCorequisiteGroup(CourseCorequisiteGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCourseCorequisiteGroupCourse(EntityID = 1, page = 1, pageSize = 100, returnCourseCorequisiteGroupCourseID = True, returnCourseCorequisiteGroupCourseIDClonedFrom = False, returnCourseCorequisiteGroupID = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseCorequisiteGroupCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCourseCorequisiteGroupCourse(CourseCorequisiteGroupCourseID, EntityID = 1, returnCourseCorequisiteGroupCourseID = True, returnCourseCorequisiteGroupCourseIDClonedFrom = False, returnCourseCorequisiteGroupID = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseCorequisiteGroupCourse/" + str(CourseCorequisiteGroupCourseID), verb = "get", return_params_list = return_params_list)

def modifyCourseCorequisiteGroupCourse(CourseCorequisiteGroupCourseID, EntityID = 1, setCourseCorequisiteGroupCourseIDClonedFrom = None, setCourseCorequisiteGroupID = None, setCourseID = None, setEntityGroupKey = None, setRelationships = None, returnCourseCorequisiteGroupCourseID = True, returnCourseCorequisiteGroupCourseIDClonedFrom = False, returnCourseCorequisiteGroupID = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseCorequisiteGroupCourse/" + str(CourseCorequisiteGroupCourseID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCourseCorequisiteGroupCourse(EntityID = 1, setCourseCorequisiteGroupCourseIDClonedFrom = None, setCourseCorequisiteGroupID = None, setCourseID = None, setEntityGroupKey = None, setRelationships = None, returnCourseCorequisiteGroupCourseID = True, returnCourseCorequisiteGroupCourseIDClonedFrom = False, returnCourseCorequisiteGroupID = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseCorequisiteGroupCourse/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCourseCorequisiteGroupCourse(CourseCorequisiteGroupCourseID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCourseCustomRequirement(EntityID = 1, page = 1, pageSize = 100, returnCourseCustomRequirementID = True, returnCourseCustomRequirementIDClonedFrom = False, returnCourseID = False, returnCreatedTime = False, returnCustomRequirementID = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseCustomRequirement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCourseCustomRequirement(CourseCustomRequirementID, EntityID = 1, returnCourseCustomRequirementID = True, returnCourseCustomRequirementIDClonedFrom = False, returnCourseID = False, returnCreatedTime = False, returnCustomRequirementID = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseCustomRequirement/" + str(CourseCustomRequirementID), verb = "get", return_params_list = return_params_list)

def modifyCourseCustomRequirement(CourseCustomRequirementID, EntityID = 1, setCourseCustomRequirementIDClonedFrom = None, setCourseID = None, setCustomRequirementID = None, setEntityGroupKey = None, setRelationships = None, returnCourseCustomRequirementID = True, returnCourseCustomRequirementIDClonedFrom = False, returnCourseID = False, returnCreatedTime = False, returnCustomRequirementID = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseCustomRequirement/" + str(CourseCustomRequirementID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCourseCustomRequirement(EntityID = 1, setCourseCustomRequirementIDClonedFrom = None, setCourseID = None, setCustomRequirementID = None, setEntityGroupKey = None, setRelationships = None, returnCourseCustomRequirementID = True, returnCourseCustomRequirementIDClonedFrom = False, returnCourseID = False, returnCreatedTime = False, returnCustomRequirementID = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseCustomRequirement/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCourseCustomRequirement(CourseCustomRequirementID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCourseEntityOfferedTo(EntityID = 1, page = 1, pageSize = 100, returnCourseEntityOfferedToID = True, returnActiveSections = False, returnActiveSectionsOpen = False, returnCourseCode = False, returnCourseEntityOfferedToIDClonedFrom = False, returnCourseEntityOfferedToIDClonedTo = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityIDOfferedTo = False, returnHasStudentCourseRequestsEntity = False, returnIsActive = False, returnIsAutoOffering = False, returnIsCurrentSchoolYearEntity = False, returnIsHomeCourse = False, returnIsOfferedCourse = False, returnIsRequired = False, returnIsRequiredOverride = False, returnModifiedTime = False, returnNumberOfAlternateCourseRequestsEntity = False, returnNumberOfCourseRequestsEntity = False, returnNumberOfCourseRequestsFemalesEntity = False, returnNumberOfCourseRequestsMalesEntity = False, returnNumberOfSeatsRemainingEntity = False, returnNumberTransferStudentSectionsEntity = False, returnRequired = False, returnSchedulingPriorityCode = False, returnSchedulingPriorityOverride = False, returnSchedulingPriorityOverrideCode = False, returnSchedulingTypeCode = False, returnSchedulingTypeOverride = False, returnSchedulingTypeOverrideCode = False, returnSchoolYearID = False, returnTotalSeatsAvailable = False, returnTotalSectionCountEntity = False, returnTotalStudentCourseRequestSectionLengthSubsetCountEntity = False, returnTotalStudentSectionCountEntity = False, returnUseIsRequiredOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSchedulingPriorityOverride = False, returnUseSchedulingTypeOverride = False, returnViewingFromOfferedEntity = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedTo/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCourseEntityOfferedTo(CourseEntityOfferedToID, EntityID = 1, returnCourseEntityOfferedToID = True, returnActiveSections = False, returnActiveSectionsOpen = False, returnCourseCode = False, returnCourseEntityOfferedToIDClonedFrom = False, returnCourseEntityOfferedToIDClonedTo = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityIDOfferedTo = False, returnHasStudentCourseRequestsEntity = False, returnIsActive = False, returnIsAutoOffering = False, returnIsCurrentSchoolYearEntity = False, returnIsHomeCourse = False, returnIsOfferedCourse = False, returnIsRequired = False, returnIsRequiredOverride = False, returnModifiedTime = False, returnNumberOfAlternateCourseRequestsEntity = False, returnNumberOfCourseRequestsEntity = False, returnNumberOfCourseRequestsFemalesEntity = False, returnNumberOfCourseRequestsMalesEntity = False, returnNumberOfSeatsRemainingEntity = False, returnNumberTransferStudentSectionsEntity = False, returnRequired = False, returnSchedulingPriorityCode = False, returnSchedulingPriorityOverride = False, returnSchedulingPriorityOverrideCode = False, returnSchedulingTypeCode = False, returnSchedulingTypeOverride = False, returnSchedulingTypeOverrideCode = False, returnSchoolYearID = False, returnTotalSeatsAvailable = False, returnTotalSectionCountEntity = False, returnTotalStudentCourseRequestSectionLengthSubsetCountEntity = False, returnTotalStudentSectionCountEntity = False, returnUseIsRequiredOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSchedulingPriorityOverride = False, returnUseSchedulingTypeOverride = False, returnViewingFromOfferedEntity = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedTo/" + str(CourseEntityOfferedToID), verb = "get", return_params_list = return_params_list)

def modifyCourseEntityOfferedTo(CourseEntityOfferedToID, EntityID = 1, setCourseCode = None, setCourseEntityOfferedToIDClonedFrom = None, setCourseID = None, setEntityGroupKey = None, setEntityIDOfferedTo = None, setIsActive = None, setIsRequiredOverride = None, setSchedulingPriorityOverride = None, setSchedulingPriorityOverrideCode = None, setSchedulingTypeOverride = None, setSchedulingTypeOverrideCode = None, setSchoolYearID = None, setUseIsRequiredOverride = None, setUseSchedulingPriorityOverride = None, setUseSchedulingTypeOverride = None, setRelationships = None, returnCourseEntityOfferedToID = True, returnActiveSections = False, returnActiveSectionsOpen = False, returnCourseCode = False, returnCourseEntityOfferedToIDClonedFrom = False, returnCourseEntityOfferedToIDClonedTo = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityIDOfferedTo = False, returnHasStudentCourseRequestsEntity = False, returnIsActive = False, returnIsAutoOffering = False, returnIsCurrentSchoolYearEntity = False, returnIsHomeCourse = False, returnIsOfferedCourse = False, returnIsRequired = False, returnIsRequiredOverride = False, returnModifiedTime = False, returnNumberOfAlternateCourseRequestsEntity = False, returnNumberOfCourseRequestsEntity = False, returnNumberOfCourseRequestsFemalesEntity = False, returnNumberOfCourseRequestsMalesEntity = False, returnNumberOfSeatsRemainingEntity = False, returnNumberTransferStudentSectionsEntity = False, returnRequired = False, returnSchedulingPriorityCode = False, returnSchedulingPriorityOverride = False, returnSchedulingPriorityOverrideCode = False, returnSchedulingTypeCode = False, returnSchedulingTypeOverride = False, returnSchedulingTypeOverrideCode = False, returnSchoolYearID = False, returnTotalSeatsAvailable = False, returnTotalSectionCountEntity = False, returnTotalStudentCourseRequestSectionLengthSubsetCountEntity = False, returnTotalStudentSectionCountEntity = False, returnUseIsRequiredOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSchedulingPriorityOverride = False, returnUseSchedulingTypeOverride = False, returnViewingFromOfferedEntity = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedTo/" + str(CourseEntityOfferedToID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCourseEntityOfferedTo(EntityID = 1, setCourseCode = None, setCourseEntityOfferedToIDClonedFrom = None, setCourseID = None, setEntityGroupKey = None, setEntityIDOfferedTo = None, setIsActive = None, setIsRequiredOverride = None, setSchedulingPriorityOverride = None, setSchedulingPriorityOverrideCode = None, setSchedulingTypeOverride = None, setSchedulingTypeOverrideCode = None, setSchoolYearID = None, setUseIsRequiredOverride = None, setUseSchedulingPriorityOverride = None, setUseSchedulingTypeOverride = None, setRelationships = None, returnCourseEntityOfferedToID = True, returnActiveSections = False, returnActiveSectionsOpen = False, returnCourseCode = False, returnCourseEntityOfferedToIDClonedFrom = False, returnCourseEntityOfferedToIDClonedTo = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityIDOfferedTo = False, returnHasStudentCourseRequestsEntity = False, returnIsActive = False, returnIsAutoOffering = False, returnIsCurrentSchoolYearEntity = False, returnIsHomeCourse = False, returnIsOfferedCourse = False, returnIsRequired = False, returnIsRequiredOverride = False, returnModifiedTime = False, returnNumberOfAlternateCourseRequestsEntity = False, returnNumberOfCourseRequestsEntity = False, returnNumberOfCourseRequestsFemalesEntity = False, returnNumberOfCourseRequestsMalesEntity = False, returnNumberOfSeatsRemainingEntity = False, returnNumberTransferStudentSectionsEntity = False, returnRequired = False, returnSchedulingPriorityCode = False, returnSchedulingPriorityOverride = False, returnSchedulingPriorityOverrideCode = False, returnSchedulingTypeCode = False, returnSchedulingTypeOverride = False, returnSchedulingTypeOverrideCode = False, returnSchoolYearID = False, returnTotalSeatsAvailable = False, returnTotalSectionCountEntity = False, returnTotalStudentCourseRequestSectionLengthSubsetCountEntity = False, returnTotalStudentSectionCountEntity = False, returnUseIsRequiredOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSchedulingPriorityOverride = False, returnUseSchedulingTypeOverride = False, returnViewingFromOfferedEntity = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedTo/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCourseEntityOfferedTo(CourseEntityOfferedToID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCourseEntityOfferedToSection(EntityID = 1, page = 1, pageSize = 100, returnCourseEntityOfferedToSectionID = True, returnCourseEntityOfferedToID = False, returnCourseEntityOfferedToSectionIDClonedFrom = False, returnCourseEntityOfferedToSectionIDClonedTo = False, returnCourseID = False, returnCreatedTime = False, returnEntityIDOfferedTo = False, returnHasMeetDisplayPeriodOverrides = False, returnIsActive = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnSchoolYearID = False, returnSeatsAvailableEntity = False, returnSectionID = False, returnStudentEnrollmentEntity = False, returnTotalEnrollmentCountEntity = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferedEntity = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedToSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCourseEntityOfferedToSection(CourseEntityOfferedToSectionID, EntityID = 1, returnCourseEntityOfferedToSectionID = True, returnCourseEntityOfferedToID = False, returnCourseEntityOfferedToSectionIDClonedFrom = False, returnCourseEntityOfferedToSectionIDClonedTo = False, returnCourseID = False, returnCreatedTime = False, returnEntityIDOfferedTo = False, returnHasMeetDisplayPeriodOverrides = False, returnIsActive = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnSchoolYearID = False, returnSeatsAvailableEntity = False, returnSectionID = False, returnStudentEnrollmentEntity = False, returnTotalEnrollmentCountEntity = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferedEntity = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedToSection/" + str(CourseEntityOfferedToSectionID), verb = "get", return_params_list = return_params_list)

def modifyCourseEntityOfferedToSection(CourseEntityOfferedToSectionID, EntityID = 1, setCourseEntityOfferedToID = None, setCourseEntityOfferedToSectionIDClonedFrom = None, setCourseID = None, setEntityIDOfferedTo = None, setIsActive = None, setMaximumStudentCount = None, setSchoolYearID = None, setSectionID = None, setRelationships = None, returnCourseEntityOfferedToSectionID = True, returnCourseEntityOfferedToID = False, returnCourseEntityOfferedToSectionIDClonedFrom = False, returnCourseEntityOfferedToSectionIDClonedTo = False, returnCourseID = False, returnCreatedTime = False, returnEntityIDOfferedTo = False, returnHasMeetDisplayPeriodOverrides = False, returnIsActive = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnSchoolYearID = False, returnSeatsAvailableEntity = False, returnSectionID = False, returnStudentEnrollmentEntity = False, returnTotalEnrollmentCountEntity = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferedEntity = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedToSection/" + str(CourseEntityOfferedToSectionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCourseEntityOfferedToSection(EntityID = 1, setCourseEntityOfferedToID = None, setCourseEntityOfferedToSectionIDClonedFrom = None, setCourseID = None, setEntityIDOfferedTo = None, setIsActive = None, setMaximumStudentCount = None, setSchoolYearID = None, setSectionID = None, setRelationships = None, returnCourseEntityOfferedToSectionID = True, returnCourseEntityOfferedToID = False, returnCourseEntityOfferedToSectionIDClonedFrom = False, returnCourseEntityOfferedToSectionIDClonedTo = False, returnCourseID = False, returnCreatedTime = False, returnEntityIDOfferedTo = False, returnHasMeetDisplayPeriodOverrides = False, returnIsActive = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnSchoolYearID = False, returnSeatsAvailableEntity = False, returnSectionID = False, returnStudentEnrollmentEntity = False, returnTotalEnrollmentCountEntity = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferedEntity = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedToSection/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCourseEntityOfferedToSection(CourseEntityOfferedToSectionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCourseEntityOfferedToSectionMeet(EntityID = 1, page = 1, pageSize = 100, returnCourseEntityOfferedToSectionMeetID = True, returnCourseEntityOfferedToSectionID = False, returnCourseEntityOfferedToSectionMeetIDClonedFrom = False, returnCreatedTime = False, returnEntityIDOfferedTo = False, returnMeetID = False, returnModifiedTime = False, returnRoomID = False, returnSchoolYearID = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedToSectionMeet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCourseEntityOfferedToSectionMeet(CourseEntityOfferedToSectionMeetID, EntityID = 1, returnCourseEntityOfferedToSectionMeetID = True, returnCourseEntityOfferedToSectionID = False, returnCourseEntityOfferedToSectionMeetIDClonedFrom = False, returnCreatedTime = False, returnEntityIDOfferedTo = False, returnMeetID = False, returnModifiedTime = False, returnRoomID = False, returnSchoolYearID = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedToSectionMeet/" + str(CourseEntityOfferedToSectionMeetID), verb = "get", return_params_list = return_params_list)

def modifyCourseEntityOfferedToSectionMeet(CourseEntityOfferedToSectionMeetID, EntityID = 1, setCourseEntityOfferedToSectionID = None, setCourseEntityOfferedToSectionMeetIDClonedFrom = None, setEntityIDOfferedTo = None, setMeetID = None, setRoomID = None, setSchoolYearID = None, setSectionID = None, setRelationships = None, returnCourseEntityOfferedToSectionMeetID = True, returnCourseEntityOfferedToSectionID = False, returnCourseEntityOfferedToSectionMeetIDClonedFrom = False, returnCreatedTime = False, returnEntityIDOfferedTo = False, returnMeetID = False, returnModifiedTime = False, returnRoomID = False, returnSchoolYearID = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedToSectionMeet/" + str(CourseEntityOfferedToSectionMeetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCourseEntityOfferedToSectionMeet(EntityID = 1, setCourseEntityOfferedToSectionID = None, setCourseEntityOfferedToSectionMeetIDClonedFrom = None, setEntityIDOfferedTo = None, setMeetID = None, setRoomID = None, setSchoolYearID = None, setSectionID = None, setRelationships = None, returnCourseEntityOfferedToSectionMeetID = True, returnCourseEntityOfferedToSectionID = False, returnCourseEntityOfferedToSectionMeetIDClonedFrom = False, returnCreatedTime = False, returnEntityIDOfferedTo = False, returnMeetID = False, returnModifiedTime = False, returnRoomID = False, returnSchoolYearID = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedToSectionMeet/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCourseEntityOfferedToSectionMeet(CourseEntityOfferedToSectionMeetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCourseEntityOfferedToSectionMeetDisplayPeriod(EntityID = 1, page = 1, pageSize = 100, returnCourseEntityOfferedToSectionMeetDisplayPeriodID = True, returnCourseEntityOfferedToSectionID = False, returnCourseEntityOfferedToSectionMeetDisplayPeriodIDClonedFrom = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnHideMeetDisplayPeriod = False, returnIsPrimary = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedToSectionMeetDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCourseEntityOfferedToSectionMeetDisplayPeriod(CourseEntityOfferedToSectionMeetDisplayPeriodID, EntityID = 1, returnCourseEntityOfferedToSectionMeetDisplayPeriodID = True, returnCourseEntityOfferedToSectionID = False, returnCourseEntityOfferedToSectionMeetDisplayPeriodIDClonedFrom = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnHideMeetDisplayPeriod = False, returnIsPrimary = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedToSectionMeetDisplayPeriod/" + str(CourseEntityOfferedToSectionMeetDisplayPeriodID), verb = "get", return_params_list = return_params_list)

def modifyCourseEntityOfferedToSectionMeetDisplayPeriod(CourseEntityOfferedToSectionMeetDisplayPeriodID, EntityID = 1, setCourseEntityOfferedToSectionID = None, setCourseEntityOfferedToSectionMeetDisplayPeriodIDClonedFrom = None, setDisplayPeriodID = None, setHideMeetDisplayPeriod = None, setIsPrimary = None, setMeetID = None, setRelationships = None, returnCourseEntityOfferedToSectionMeetDisplayPeriodID = True, returnCourseEntityOfferedToSectionID = False, returnCourseEntityOfferedToSectionMeetDisplayPeriodIDClonedFrom = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnHideMeetDisplayPeriod = False, returnIsPrimary = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedToSectionMeetDisplayPeriod/" + str(CourseEntityOfferedToSectionMeetDisplayPeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCourseEntityOfferedToSectionMeetDisplayPeriod(EntityID = 1, setCourseEntityOfferedToSectionID = None, setCourseEntityOfferedToSectionMeetDisplayPeriodIDClonedFrom = None, setDisplayPeriodID = None, setHideMeetDisplayPeriod = None, setIsPrimary = None, setMeetID = None, setRelationships = None, returnCourseEntityOfferedToSectionMeetDisplayPeriodID = True, returnCourseEntityOfferedToSectionID = False, returnCourseEntityOfferedToSectionMeetDisplayPeriodIDClonedFrom = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnHideMeetDisplayPeriod = False, returnIsPrimary = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedToSectionMeetDisplayPeriod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCourseEntityOfferedToSectionMeetDisplayPeriod(CourseEntityOfferedToSectionMeetDisplayPeriodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCourseEntityOfferedToSectionStaffMeet(EntityID = 1, page = 1, pageSize = 100, returnCourseEntityOfferedToSectionStaffMeetID = True, returnCourseEntityOfferedToSectionID = False, returnCourseEntityOfferedToSectionStaffMeetIDClonedFrom = False, returnCreatedTime = False, returnMeetID = False, returnModifiedTime = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedToSectionStaffMeet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCourseEntityOfferedToSectionStaffMeet(CourseEntityOfferedToSectionStaffMeetID, EntityID = 1, returnCourseEntityOfferedToSectionStaffMeetID = True, returnCourseEntityOfferedToSectionID = False, returnCourseEntityOfferedToSectionStaffMeetIDClonedFrom = False, returnCreatedTime = False, returnMeetID = False, returnModifiedTime = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedToSectionStaffMeet/" + str(CourseEntityOfferedToSectionStaffMeetID), verb = "get", return_params_list = return_params_list)

def modifyCourseEntityOfferedToSectionStaffMeet(CourseEntityOfferedToSectionStaffMeetID, EntityID = 1, setCourseEntityOfferedToSectionID = None, setCourseEntityOfferedToSectionStaffMeetIDClonedFrom = None, setMeetID = None, setStaffID = None, setRelationships = None, returnCourseEntityOfferedToSectionStaffMeetID = True, returnCourseEntityOfferedToSectionID = False, returnCourseEntityOfferedToSectionStaffMeetIDClonedFrom = False, returnCreatedTime = False, returnMeetID = False, returnModifiedTime = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedToSectionStaffMeet/" + str(CourseEntityOfferedToSectionStaffMeetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCourseEntityOfferedToSectionStaffMeet(EntityID = 1, setCourseEntityOfferedToSectionID = None, setCourseEntityOfferedToSectionStaffMeetIDClonedFrom = None, setMeetID = None, setStaffID = None, setRelationships = None, returnCourseEntityOfferedToSectionStaffMeetID = True, returnCourseEntityOfferedToSectionID = False, returnCourseEntityOfferedToSectionStaffMeetIDClonedFrom = False, returnCreatedTime = False, returnMeetID = False, returnModifiedTime = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseEntityOfferedToSectionStaffMeet/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCourseEntityOfferedToSectionStaffMeet(CourseEntityOfferedToSectionStaffMeetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCourseGradeReference(EntityID = 1, page = 1, pageSize = 100, returnCourseGradeReferenceID = True, returnCourseGradeReferenceIDClonedFrom = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNumberOfAlternateCourseRequests = False, returnNumberOfAlternateCourseRequestsEntity = False, returnNumberOfCourseRequests = False, returnNumberOfCourseRequestsEntity = False, returnNumberOfCourseRequestsFemales = False, returnNumberOfCourseRequestsFemalesEntity = False, returnNumberOfCourseRequestsMales = False, returnNumberOfCourseRequestsMalesEntity = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseGradeReference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCourseGradeReference(CourseGradeReferenceID, EntityID = 1, returnCourseGradeReferenceID = True, returnCourseGradeReferenceIDClonedFrom = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNumberOfAlternateCourseRequests = False, returnNumberOfAlternateCourseRequestsEntity = False, returnNumberOfCourseRequests = False, returnNumberOfCourseRequestsEntity = False, returnNumberOfCourseRequestsFemales = False, returnNumberOfCourseRequestsFemalesEntity = False, returnNumberOfCourseRequestsMales = False, returnNumberOfCourseRequestsMalesEntity = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseGradeReference/" + str(CourseGradeReferenceID), verb = "get", return_params_list = return_params_list)

def modifyCourseGradeReference(CourseGradeReferenceID, EntityID = 1, setCourseGradeReferenceIDClonedFrom = None, setCourseID = None, setEntityGroupKey = None, setGradeReferenceID = None, setRelationships = None, returnCourseGradeReferenceID = True, returnCourseGradeReferenceIDClonedFrom = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNumberOfAlternateCourseRequests = False, returnNumberOfAlternateCourseRequestsEntity = False, returnNumberOfCourseRequests = False, returnNumberOfCourseRequestsEntity = False, returnNumberOfCourseRequestsFemales = False, returnNumberOfCourseRequestsFemalesEntity = False, returnNumberOfCourseRequestsMales = False, returnNumberOfCourseRequestsMalesEntity = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseGradeReference/" + str(CourseGradeReferenceID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCourseGradeReference(EntityID = 1, setCourseGradeReferenceIDClonedFrom = None, setCourseID = None, setEntityGroupKey = None, setGradeReferenceID = None, setRelationships = None, returnCourseGradeReferenceID = True, returnCourseGradeReferenceIDClonedFrom = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNumberOfAlternateCourseRequests = False, returnNumberOfAlternateCourseRequestsEntity = False, returnNumberOfCourseRequests = False, returnNumberOfCourseRequestsEntity = False, returnNumberOfCourseRequestsFemales = False, returnNumberOfCourseRequestsFemalesEntity = False, returnNumberOfCourseRequestsMales = False, returnNumberOfCourseRequestsMalesEntity = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseGradeReference/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCourseGradeReference(CourseGradeReferenceID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCourseGroup(EntityID = 1, page = 1, pageSize = 100, returnCourseGroupID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCourseGroup(CourseGroupID, EntityID = 1, returnCourseGroupID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseGroup/" + str(CourseGroupID), verb = "get", return_params_list = return_params_list)

def modifyCourseGroup(CourseGroupID, EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setRelationships = None, returnCourseGroupID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseGroup/" + str(CourseGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCourseGroup(EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setRelationships = None, returnCourseGroupID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCourseGroup(CourseGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCourseGroupCourse(EntityID = 1, page = 1, pageSize = 100, returnCourseGroupCourseID = True, returnCourseGroupCourseIDClonedFrom = False, returnCourseGroupID = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseGroupCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCourseGroupCourse(CourseGroupCourseID, EntityID = 1, returnCourseGroupCourseID = True, returnCourseGroupCourseIDClonedFrom = False, returnCourseGroupID = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseGroupCourse/" + str(CourseGroupCourseID), verb = "get", return_params_list = return_params_list)

def modifyCourseGroupCourse(CourseGroupCourseID, EntityID = 1, setCourseGroupCourseIDClonedFrom = None, setCourseGroupID = None, setCourseID = None, setEntityGroupKey = None, setRelationships = None, returnCourseGroupCourseID = True, returnCourseGroupCourseIDClonedFrom = False, returnCourseGroupID = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseGroupCourse/" + str(CourseGroupCourseID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCourseGroupCourse(EntityID = 1, setCourseGroupCourseIDClonedFrom = None, setCourseGroupID = None, setCourseID = None, setEntityGroupKey = None, setRelationships = None, returnCourseGroupCourseID = True, returnCourseGroupCourseIDClonedFrom = False, returnCourseGroupID = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseGroupCourse/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCourseGroupCourse(CourseGroupCourseID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCourseLength(EntityID = 1, page = 1, pageSize = 100, returnCourseLengthID = True, returnCode = False, returnCodeDescription = False, returnCourseLengthIDClonedFrom = False, returnCourseLengthIDClonedTo = False, returnCreatedTime = False, returnDefaultEarnedCredits = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseLength/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCourseLength(CourseLengthID, EntityID = 1, returnCourseLengthID = True, returnCode = False, returnCodeDescription = False, returnCourseLengthIDClonedFrom = False, returnCourseLengthIDClonedTo = False, returnCreatedTime = False, returnDefaultEarnedCredits = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseLength/" + str(CourseLengthID), verb = "get", return_params_list = return_params_list)

def modifyCourseLength(CourseLengthID, EntityID = 1, setCode = None, setCourseLengthIDClonedFrom = None, setDefaultEarnedCredits = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setSchoolYearID = None, setRelationships = None, returnCourseLengthID = True, returnCode = False, returnCodeDescription = False, returnCourseLengthIDClonedFrom = False, returnCourseLengthIDClonedTo = False, returnCreatedTime = False, returnDefaultEarnedCredits = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseLength/" + str(CourseLengthID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCourseLength(EntityID = 1, setCode = None, setCourseLengthIDClonedFrom = None, setDefaultEarnedCredits = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setSchoolYearID = None, setRelationships = None, returnCourseLengthID = True, returnCode = False, returnCodeDescription = False, returnCourseLengthIDClonedFrom = False, returnCourseLengthIDClonedTo = False, returnCreatedTime = False, returnDefaultEarnedCredits = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseLength/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCourseLength(CourseLengthID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCourseLevelMN(EntityID = 1, page = 1, pageSize = 100, returnCourseLevelMNID = True, returnCode = False, returnCreatedTime = False, returnCredits = False, returnCurriculumYearID = False, returnInstitutionID = False, returnModifiedTime = False, returnStateCollegeCourseLevelMNID = False, returnTitle = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseLevelMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCourseLevelMN(CourseLevelMNID, EntityID = 1, returnCourseLevelMNID = True, returnCode = False, returnCreatedTime = False, returnCredits = False, returnCurriculumYearID = False, returnInstitutionID = False, returnModifiedTime = False, returnStateCollegeCourseLevelMNID = False, returnTitle = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseLevelMN/" + str(CourseLevelMNID), verb = "get", return_params_list = return_params_list)

def modifyCourseLevelMN(CourseLevelMNID, EntityID = 1, setCode = None, setCredits = None, setCurriculumYearID = None, setInstitutionID = None, setStateCollegeCourseLevelMNID = None, setTitle = None, setRelationships = None, returnCourseLevelMNID = True, returnCode = False, returnCreatedTime = False, returnCredits = False, returnCurriculumYearID = False, returnInstitutionID = False, returnModifiedTime = False, returnStateCollegeCourseLevelMNID = False, returnTitle = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseLevelMN/" + str(CourseLevelMNID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCourseLevelMN(EntityID = 1, setCode = None, setCredits = None, setCurriculumYearID = None, setInstitutionID = None, setStateCollegeCourseLevelMNID = None, setTitle = None, setRelationships = None, returnCourseLevelMNID = True, returnCode = False, returnCreatedTime = False, returnCredits = False, returnCurriculumYearID = False, returnInstitutionID = False, returnModifiedTime = False, returnStateCollegeCourseLevelMNID = False, returnTitle = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseLevelMN/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCourseLevelMN(CourseLevelMNID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCourseMasterMassUpdate(EntityID = 1, page = 1, pageSize = 100, returnCourseMasterMassUpdateID = True, returnCreatedTime = False, returnEntityID = False, returnFilterParameters = False, returnModifiedTime = False, returnRunReason = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRanBy = False, returnValueParameters = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseMasterMassUpdate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCourseMasterMassUpdate(CourseMasterMassUpdateID, EntityID = 1, returnCourseMasterMassUpdateID = True, returnCreatedTime = False, returnEntityID = False, returnFilterParameters = False, returnModifiedTime = False, returnRunReason = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRanBy = False, returnValueParameters = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseMasterMassUpdate/" + str(CourseMasterMassUpdateID), verb = "get", return_params_list = return_params_list)

def modifyCourseMasterMassUpdate(CourseMasterMassUpdateID, EntityID = 1, setEntityID = None, setFilterParameters = None, setRunReason = None, setSchoolYearID = None, setUserIDRanBy = None, setValueParameters = None, setRelationships = None, returnCourseMasterMassUpdateID = True, returnCreatedTime = False, returnEntityID = False, returnFilterParameters = False, returnModifiedTime = False, returnRunReason = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRanBy = False, returnValueParameters = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseMasterMassUpdate/" + str(CourseMasterMassUpdateID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCourseMasterMassUpdate(EntityID = 1, setEntityID = None, setFilterParameters = None, setRunReason = None, setSchoolYearID = None, setUserIDRanBy = None, setValueParameters = None, setRelationships = None, returnCourseMasterMassUpdateID = True, returnCreatedTime = False, returnEntityID = False, returnFilterParameters = False, returnModifiedTime = False, returnRunReason = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRanBy = False, returnValueParameters = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseMasterMassUpdate/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCourseMasterMassUpdate(CourseMasterMassUpdateID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCourse(EntityID = 1, page = 1, pageSize = 100, returnCourseID = True, returnAcademicMinutes = False, returnActiveSections = False, returnActiveSectionsOpen = False, returnActivityID = False, returnAllowTeachersToAddAssignments = False, returnCanBeOfferedToAnotherEntity = False, returnCategory = False, returnCategoryCode = False, returnCodeDescription = False, returnCourseCloned = False, returnCourseCode = False, returnCourseGradeLevelCodes = False, returnCourseGroupDescriptions = False, returnCourseIDClonedFrom = False, returnCourseIDClonedTo = False, returnCourseIDHash = False, returnCourseLengthID = False, returnCourseMNID = False, returnCourseSubjectID = False, returnCourseTypeID = False, returnCreatedTime = False, returnCurriculumID = False, returnDepartmentID = False, returnDescription = False, returnEarnedCredits = False, returnEdFiCourseLevelCharacteristicID = False, returnEdFiSubjectTypeID = False, returnEntityGroupKey = False, returnEntityID = False, returnEstimatedNumberOfSections = False, returnExcludeFromSTAR = False, returnExcludeFromStudentSectionLink = False, returnGradeCourse = False, returnGradeLevelIDSummary = False, returnGradeLevelSummary = False, returnGradingPeriodSetID = False, returnHasAttachedStandards = False, returnHasCourseRequestsInCommonWithCourse = False, returnHasNonAlternateStudentCourseRequests = False, returnHasOfferedCourseEntity = False, returnHasStudentCourseRequests = False, returnHasSubjects = False, returnHideFromArenaScheduling = False, returnHideFromRequestEntry = False, returnIsActive = False, returnIsActiveForEntity = False, returnIsAHistoricRecord = False, returnIsCoreAcademic = False, returnIsCurrentSchoolYear = False, returnIsDirectPay = False, returnIsHonors = False, returnIsOffered = False, returnIsRepeatable = False, returnIsRequired = False, returnIsRequiredOverride = False, returnIsWritingEmphasis = False, returnKeepAttendance = False, returnLengthOfPeriod = False, returnLockCourseFromSectionScheduler = False, returnMaximumPercentageOfSectionsInSingleDisplayPeriod = False, returnMaxRequestedCount = False, returnModifiedTime = False, returnNumberOfAlternateCourseRequests = False, returnNumberOfCourseRequests = False, returnNumberOfCourseRequestsFemales = False, returnNumberOfCourseRequestsInCommonWithCourse = False, returnNumberOfCourseRequestsMales = False, returnNumberOfSeatsAvailable = False, returnNumberOfSeatsRemaining = False, returnNumberOfTransferStudentSections = False, returnOfferingEntity = False, returnOverrideStudentSectionLinkByCourse = False, returnPeriodsPerWeek = False, returnPreventDrop = False, returnPreventMultipleSectionsUsingSingleDisplayPeriod = False, returnRequestLimitPerStudent = False, returnRequired = False, returnSchedulingPriority = False, returnSchedulingPriorityCode = False, returnSchedulingPriorityCodeOverride = False, returnSchedulingPriorityOverride = False, returnSchedulingTeamMode = False, returnSchedulingTeamModeCode = False, returnSchedulingType = False, returnSchedulingTypeCode = False, returnSchedulingTypeCodeOverride = False, returnSchedulingTypeOverride = False, returnSchoolYearID = False, returnSectionSchedulerManualProcessingOrder = False, returnSequenceLimit = False, returnSequenceNumber = False, returnSpecificStudentRequests = False, returnStateCarlPerkinsProgramCodeMNID = False, returnStateSTARAssignmentCodeMNID = False, returnStateSTARGradeLevelMNID = False, returnSumTotalActiveSectionsOptimalStudentCount = False, returnTotalEntitiesOfferedTo = False, returnTotalSectionCount = False, returnTotalStudentCourseRequestSectionLengthSubsetCount = False, returnTotalStudentSectionCount = False, returnUseRequiredOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSchedulingPriorityOverride = False, returnUseSchedulingTypeOverride = False, returnViewingFromOfferingEntity = False, returnWebsite = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/Course/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCourse(CourseID, EntityID = 1, returnCourseID = True, returnAcademicMinutes = False, returnActiveSections = False, returnActiveSectionsOpen = False, returnActivityID = False, returnAllowTeachersToAddAssignments = False, returnCanBeOfferedToAnotherEntity = False, returnCategory = False, returnCategoryCode = False, returnCodeDescription = False, returnCourseCloned = False, returnCourseCode = False, returnCourseGradeLevelCodes = False, returnCourseGroupDescriptions = False, returnCourseIDClonedFrom = False, returnCourseIDClonedTo = False, returnCourseIDHash = False, returnCourseLengthID = False, returnCourseMNID = False, returnCourseSubjectID = False, returnCourseTypeID = False, returnCreatedTime = False, returnCurriculumID = False, returnDepartmentID = False, returnDescription = False, returnEarnedCredits = False, returnEdFiCourseLevelCharacteristicID = False, returnEdFiSubjectTypeID = False, returnEntityGroupKey = False, returnEntityID = False, returnEstimatedNumberOfSections = False, returnExcludeFromSTAR = False, returnExcludeFromStudentSectionLink = False, returnGradeCourse = False, returnGradeLevelIDSummary = False, returnGradeLevelSummary = False, returnGradingPeriodSetID = False, returnHasAttachedStandards = False, returnHasCourseRequestsInCommonWithCourse = False, returnHasNonAlternateStudentCourseRequests = False, returnHasOfferedCourseEntity = False, returnHasStudentCourseRequests = False, returnHasSubjects = False, returnHideFromArenaScheduling = False, returnHideFromRequestEntry = False, returnIsActive = False, returnIsActiveForEntity = False, returnIsAHistoricRecord = False, returnIsCoreAcademic = False, returnIsCurrentSchoolYear = False, returnIsDirectPay = False, returnIsHonors = False, returnIsOffered = False, returnIsRepeatable = False, returnIsRequired = False, returnIsRequiredOverride = False, returnIsWritingEmphasis = False, returnKeepAttendance = False, returnLengthOfPeriod = False, returnLockCourseFromSectionScheduler = False, returnMaximumPercentageOfSectionsInSingleDisplayPeriod = False, returnMaxRequestedCount = False, returnModifiedTime = False, returnNumberOfAlternateCourseRequests = False, returnNumberOfCourseRequests = False, returnNumberOfCourseRequestsFemales = False, returnNumberOfCourseRequestsInCommonWithCourse = False, returnNumberOfCourseRequestsMales = False, returnNumberOfSeatsAvailable = False, returnNumberOfSeatsRemaining = False, returnNumberOfTransferStudentSections = False, returnOfferingEntity = False, returnOverrideStudentSectionLinkByCourse = False, returnPeriodsPerWeek = False, returnPreventDrop = False, returnPreventMultipleSectionsUsingSingleDisplayPeriod = False, returnRequestLimitPerStudent = False, returnRequired = False, returnSchedulingPriority = False, returnSchedulingPriorityCode = False, returnSchedulingPriorityCodeOverride = False, returnSchedulingPriorityOverride = False, returnSchedulingTeamMode = False, returnSchedulingTeamModeCode = False, returnSchedulingType = False, returnSchedulingTypeCode = False, returnSchedulingTypeCodeOverride = False, returnSchedulingTypeOverride = False, returnSchoolYearID = False, returnSectionSchedulerManualProcessingOrder = False, returnSequenceLimit = False, returnSequenceNumber = False, returnSpecificStudentRequests = False, returnStateCarlPerkinsProgramCodeMNID = False, returnStateSTARAssignmentCodeMNID = False, returnStateSTARGradeLevelMNID = False, returnSumTotalActiveSectionsOptimalStudentCount = False, returnTotalEntitiesOfferedTo = False, returnTotalSectionCount = False, returnTotalStudentCourseRequestSectionLengthSubsetCount = False, returnTotalStudentSectionCount = False, returnUseRequiredOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSchedulingPriorityOverride = False, returnUseSchedulingTypeOverride = False, returnViewingFromOfferingEntity = False, returnWebsite = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/Course/" + str(CourseID), verb = "get", return_params_list = return_params_list)

def modifyCourse(CourseID, EntityID = 1, setAcademicMinutes = None, setActivityID = None, setAllowTeachersToAddAssignments = None, setCategory = None, setCategoryCode = None, setCourseCode = None, setCourseIDClonedFrom = None, setCourseLengthID = None, setCourseSubjectID = None, setCourseTypeID = None, setCurriculumID = None, setDepartmentID = None, setDescription = None, setEarnedCredits = None, setEdFiCourseLevelCharacteristicID = None, setEdFiSubjectTypeID = None, setEntityGroupKey = None, setEntityID = None, setEstimatedNumberOfSections = None, setExcludeFromSTAR = None, setExcludeFromStudentSectionLink = None, setGradeCourse = None, setGradingPeriodSetID = None, setHideFromArenaScheduling = None, setHideFromRequestEntry = None, setIsCoreAcademic = None, setIsDirectPay = None, setIsHonors = None, setIsRepeatable = None, setIsRequired = None, setIsWritingEmphasis = None, setKeepAttendance = None, setLengthOfPeriod = None, setLockCourseFromSectionScheduler = None, setMaximumPercentageOfSectionsInSingleDisplayPeriod = None, setOverrideStudentSectionLinkByCourse = None, setPeriodsPerWeek = None, setPreventDrop = None, setPreventMultipleSectionsUsingSingleDisplayPeriod = None, setRequestLimitPerStudent = None, setSchedulingPriority = None, setSchedulingPriorityCode = None, setSchedulingTeamMode = None, setSchedulingTeamModeCode = None, setSchedulingType = None, setSchedulingTypeCode = None, setSchoolYearID = None, setSectionSchedulerManualProcessingOrder = None, setSequenceLimit = None, setSequenceNumber = None, setStateCarlPerkinsProgramCodeMNID = None, setStateSTARAssignmentCodeMNID = None, setStateSTARGradeLevelMNID = None, setWebsite = None, setRelationships = None, returnCourseID = True, returnAcademicMinutes = False, returnActiveSections = False, returnActiveSectionsOpen = False, returnActivityID = False, returnAllowTeachersToAddAssignments = False, returnCanBeOfferedToAnotherEntity = False, returnCategory = False, returnCategoryCode = False, returnCodeDescription = False, returnCourseCloned = False, returnCourseCode = False, returnCourseGradeLevelCodes = False, returnCourseGroupDescriptions = False, returnCourseIDClonedFrom = False, returnCourseIDClonedTo = False, returnCourseIDHash = False, returnCourseLengthID = False, returnCourseMNID = False, returnCourseSubjectID = False, returnCourseTypeID = False, returnCreatedTime = False, returnCurriculumID = False, returnDepartmentID = False, returnDescription = False, returnEarnedCredits = False, returnEdFiCourseLevelCharacteristicID = False, returnEdFiSubjectTypeID = False, returnEntityGroupKey = False, returnEntityID = False, returnEstimatedNumberOfSections = False, returnExcludeFromSTAR = False, returnExcludeFromStudentSectionLink = False, returnGradeCourse = False, returnGradeLevelIDSummary = False, returnGradeLevelSummary = False, returnGradingPeriodSetID = False, returnHasAttachedStandards = False, returnHasCourseRequestsInCommonWithCourse = False, returnHasNonAlternateStudentCourseRequests = False, returnHasOfferedCourseEntity = False, returnHasStudentCourseRequests = False, returnHasSubjects = False, returnHideFromArenaScheduling = False, returnHideFromRequestEntry = False, returnIsActive = False, returnIsActiveForEntity = False, returnIsAHistoricRecord = False, returnIsCoreAcademic = False, returnIsCurrentSchoolYear = False, returnIsDirectPay = False, returnIsHonors = False, returnIsOffered = False, returnIsRepeatable = False, returnIsRequired = False, returnIsRequiredOverride = False, returnIsWritingEmphasis = False, returnKeepAttendance = False, returnLengthOfPeriod = False, returnLockCourseFromSectionScheduler = False, returnMaximumPercentageOfSectionsInSingleDisplayPeriod = False, returnMaxRequestedCount = False, returnModifiedTime = False, returnNumberOfAlternateCourseRequests = False, returnNumberOfCourseRequests = False, returnNumberOfCourseRequestsFemales = False, returnNumberOfCourseRequestsInCommonWithCourse = False, returnNumberOfCourseRequestsMales = False, returnNumberOfSeatsAvailable = False, returnNumberOfSeatsRemaining = False, returnNumberOfTransferStudentSections = False, returnOfferingEntity = False, returnOverrideStudentSectionLinkByCourse = False, returnPeriodsPerWeek = False, returnPreventDrop = False, returnPreventMultipleSectionsUsingSingleDisplayPeriod = False, returnRequestLimitPerStudent = False, returnRequired = False, returnSchedulingPriority = False, returnSchedulingPriorityCode = False, returnSchedulingPriorityCodeOverride = False, returnSchedulingPriorityOverride = False, returnSchedulingTeamMode = False, returnSchedulingTeamModeCode = False, returnSchedulingType = False, returnSchedulingTypeCode = False, returnSchedulingTypeCodeOverride = False, returnSchedulingTypeOverride = False, returnSchoolYearID = False, returnSectionSchedulerManualProcessingOrder = False, returnSequenceLimit = False, returnSequenceNumber = False, returnSpecificStudentRequests = False, returnStateCarlPerkinsProgramCodeMNID = False, returnStateSTARAssignmentCodeMNID = False, returnStateSTARGradeLevelMNID = False, returnSumTotalActiveSectionsOptimalStudentCount = False, returnTotalEntitiesOfferedTo = False, returnTotalSectionCount = False, returnTotalStudentCourseRequestSectionLengthSubsetCount = False, returnTotalStudentSectionCount = False, returnUseRequiredOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSchedulingPriorityOverride = False, returnUseSchedulingTypeOverride = False, returnViewingFromOfferingEntity = False, returnWebsite = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/Course/" + str(CourseID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCourse(EntityID = 1, setAcademicMinutes = None, setActivityID = None, setAllowTeachersToAddAssignments = None, setCategory = None, setCategoryCode = None, setCourseCode = None, setCourseIDClonedFrom = None, setCourseLengthID = None, setCourseSubjectID = None, setCourseTypeID = None, setCurriculumID = None, setDepartmentID = None, setDescription = None, setEarnedCredits = None, setEdFiCourseLevelCharacteristicID = None, setEdFiSubjectTypeID = None, setEntityGroupKey = None, setEntityID = None, setEstimatedNumberOfSections = None, setExcludeFromSTAR = None, setExcludeFromStudentSectionLink = None, setGradeCourse = None, setGradingPeriodSetID = None, setHideFromArenaScheduling = None, setHideFromRequestEntry = None, setIsCoreAcademic = None, setIsDirectPay = None, setIsHonors = None, setIsRepeatable = None, setIsRequired = None, setIsWritingEmphasis = None, setKeepAttendance = None, setLengthOfPeriod = None, setLockCourseFromSectionScheduler = None, setMaximumPercentageOfSectionsInSingleDisplayPeriod = None, setOverrideStudentSectionLinkByCourse = None, setPeriodsPerWeek = None, setPreventDrop = None, setPreventMultipleSectionsUsingSingleDisplayPeriod = None, setRequestLimitPerStudent = None, setSchedulingPriority = None, setSchedulingPriorityCode = None, setSchedulingTeamMode = None, setSchedulingTeamModeCode = None, setSchedulingType = None, setSchedulingTypeCode = None, setSchoolYearID = None, setSectionSchedulerManualProcessingOrder = None, setSequenceLimit = None, setSequenceNumber = None, setStateCarlPerkinsProgramCodeMNID = None, setStateSTARAssignmentCodeMNID = None, setStateSTARGradeLevelMNID = None, setWebsite = None, setRelationships = None, returnCourseID = True, returnAcademicMinutes = False, returnActiveSections = False, returnActiveSectionsOpen = False, returnActivityID = False, returnAllowTeachersToAddAssignments = False, returnCanBeOfferedToAnotherEntity = False, returnCategory = False, returnCategoryCode = False, returnCodeDescription = False, returnCourseCloned = False, returnCourseCode = False, returnCourseGradeLevelCodes = False, returnCourseGroupDescriptions = False, returnCourseIDClonedFrom = False, returnCourseIDClonedTo = False, returnCourseIDHash = False, returnCourseLengthID = False, returnCourseMNID = False, returnCourseSubjectID = False, returnCourseTypeID = False, returnCreatedTime = False, returnCurriculumID = False, returnDepartmentID = False, returnDescription = False, returnEarnedCredits = False, returnEdFiCourseLevelCharacteristicID = False, returnEdFiSubjectTypeID = False, returnEntityGroupKey = False, returnEntityID = False, returnEstimatedNumberOfSections = False, returnExcludeFromSTAR = False, returnExcludeFromStudentSectionLink = False, returnGradeCourse = False, returnGradeLevelIDSummary = False, returnGradeLevelSummary = False, returnGradingPeriodSetID = False, returnHasAttachedStandards = False, returnHasCourseRequestsInCommonWithCourse = False, returnHasNonAlternateStudentCourseRequests = False, returnHasOfferedCourseEntity = False, returnHasStudentCourseRequests = False, returnHasSubjects = False, returnHideFromArenaScheduling = False, returnHideFromRequestEntry = False, returnIsActive = False, returnIsActiveForEntity = False, returnIsAHistoricRecord = False, returnIsCoreAcademic = False, returnIsCurrentSchoolYear = False, returnIsDirectPay = False, returnIsHonors = False, returnIsOffered = False, returnIsRepeatable = False, returnIsRequired = False, returnIsRequiredOverride = False, returnIsWritingEmphasis = False, returnKeepAttendance = False, returnLengthOfPeriod = False, returnLockCourseFromSectionScheduler = False, returnMaximumPercentageOfSectionsInSingleDisplayPeriod = False, returnMaxRequestedCount = False, returnModifiedTime = False, returnNumberOfAlternateCourseRequests = False, returnNumberOfCourseRequests = False, returnNumberOfCourseRequestsFemales = False, returnNumberOfCourseRequestsInCommonWithCourse = False, returnNumberOfCourseRequestsMales = False, returnNumberOfSeatsAvailable = False, returnNumberOfSeatsRemaining = False, returnNumberOfTransferStudentSections = False, returnOfferingEntity = False, returnOverrideStudentSectionLinkByCourse = False, returnPeriodsPerWeek = False, returnPreventDrop = False, returnPreventMultipleSectionsUsingSingleDisplayPeriod = False, returnRequestLimitPerStudent = False, returnRequired = False, returnSchedulingPriority = False, returnSchedulingPriorityCode = False, returnSchedulingPriorityCodeOverride = False, returnSchedulingPriorityOverride = False, returnSchedulingTeamMode = False, returnSchedulingTeamModeCode = False, returnSchedulingType = False, returnSchedulingTypeCode = False, returnSchedulingTypeCodeOverride = False, returnSchedulingTypeOverride = False, returnSchoolYearID = False, returnSectionSchedulerManualProcessingOrder = False, returnSequenceLimit = False, returnSequenceNumber = False, returnSpecificStudentRequests = False, returnStateCarlPerkinsProgramCodeMNID = False, returnStateSTARAssignmentCodeMNID = False, returnStateSTARGradeLevelMNID = False, returnSumTotalActiveSectionsOptimalStudentCount = False, returnTotalEntitiesOfferedTo = False, returnTotalSectionCount = False, returnTotalStudentCourseRequestSectionLengthSubsetCount = False, returnTotalStudentSectionCount = False, returnUseRequiredOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSchedulingPriorityOverride = False, returnUseSchedulingTypeOverride = False, returnViewingFromOfferingEntity = False, returnWebsite = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/Course/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCourse(CourseID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCourseSectionLengthExclude(EntityID = 1, page = 1, pageSize = 100, returnCourseSectionLengthExcludeID = True, returnCourseID = False, returnCreatedTime = False, returnDistributionPercent = False, returnEntityGroupKey = False, returnModifiedTime = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseSectionLengthExclude/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCourseSectionLengthExclude(CourseSectionLengthExcludeID, EntityID = 1, returnCourseSectionLengthExcludeID = True, returnCourseID = False, returnCreatedTime = False, returnDistributionPercent = False, returnEntityGroupKey = False, returnModifiedTime = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseSectionLengthExclude/" + str(CourseSectionLengthExcludeID), verb = "get", return_params_list = return_params_list)

def modifyCourseSectionLengthExclude(CourseSectionLengthExcludeID, EntityID = 1, setCourseID = None, setDistributionPercent = None, setEntityGroupKey = None, setSectionLengthID = None, setRelationships = None, returnCourseSectionLengthExcludeID = True, returnCourseID = False, returnCreatedTime = False, returnDistributionPercent = False, returnEntityGroupKey = False, returnModifiedTime = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseSectionLengthExclude/" + str(CourseSectionLengthExcludeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCourseSectionLengthExclude(EntityID = 1, setCourseID = None, setDistributionPercent = None, setEntityGroupKey = None, setSectionLengthID = None, setRelationships = None, returnCourseSectionLengthExcludeID = True, returnCourseID = False, returnCreatedTime = False, returnDistributionPercent = False, returnEntityGroupKey = False, returnModifiedTime = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseSectionLengthExclude/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCourseSectionLengthExclude(CourseSectionLengthExcludeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCourseSubject(EntityID = 1, page = 1, pageSize = 100, returnCourseSubjectID = True, returnCode = False, returnCodeDescription = False, returnCourseSubjectIDClonedFrom = False, returnCourseSubjectIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseSubject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCourseSubject(CourseSubjectID, EntityID = 1, returnCourseSubjectID = True, returnCode = False, returnCodeDescription = False, returnCourseSubjectIDClonedFrom = False, returnCourseSubjectIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseSubject/" + str(CourseSubjectID), verb = "get", return_params_list = return_params_list)

def modifyCourseSubject(CourseSubjectID, EntityID = 1, setCode = None, setCourseSubjectIDClonedFrom = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setSchoolYearID = None, setRelationships = None, returnCourseSubjectID = True, returnCode = False, returnCodeDescription = False, returnCourseSubjectIDClonedFrom = False, returnCourseSubjectIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseSubject/" + str(CourseSubjectID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCourseSubject(EntityID = 1, setCode = None, setCourseSubjectIDClonedFrom = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setSchoolYearID = None, setRelationships = None, returnCourseSubjectID = True, returnCode = False, returnCodeDescription = False, returnCourseSubjectIDClonedFrom = False, returnCourseSubjectIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseSubject/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCourseSubject(CourseSubjectID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCourseType(EntityID = 1, page = 1, pageSize = 100, returnCourseTypeID = True, returnCode = False, returnCodeDescription = False, returnCourseTypeIDClonedFrom = False, returnCourseTypeIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCourseType(CourseTypeID, EntityID = 1, returnCourseTypeID = True, returnCode = False, returnCodeDescription = False, returnCourseTypeIDClonedFrom = False, returnCourseTypeIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseType/" + str(CourseTypeID), verb = "get", return_params_list = return_params_list)

def modifyCourseType(CourseTypeID, EntityID = 1, setCode = None, setCourseTypeIDClonedFrom = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setSchoolYearID = None, setRelationships = None, returnCourseTypeID = True, returnCode = False, returnCodeDescription = False, returnCourseTypeIDClonedFrom = False, returnCourseTypeIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseType/" + str(CourseTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCourseType(EntityID = 1, setCode = None, setCourseTypeIDClonedFrom = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setSchoolYearID = None, setRelationships = None, returnCourseTypeID = True, returnCode = False, returnCodeDescription = False, returnCourseTypeIDClonedFrom = False, returnCourseTypeIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CourseType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCourseType(CourseTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCustomRequirement(EntityID = 1, page = 1, pageSize = 100, returnCustomRequirementID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnStudentCondition = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CustomRequirement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCustomRequirement(CustomRequirementID, EntityID = 1, returnCustomRequirementID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnStudentCondition = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CustomRequirement/" + str(CustomRequirementID), verb = "get", return_params_list = return_params_list)

def modifyCustomRequirement(CustomRequirementID, EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setStudentCondition = None, setRelationships = None, returnCustomRequirementID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnStudentCondition = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CustomRequirement/" + str(CustomRequirementID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCustomRequirement(EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setStudentCondition = None, setRelationships = None, returnCustomRequirementID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnStudentCondition = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/CustomRequirement/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCustomRequirement(CustomRequirementID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDateRangePreset(EntityID = 1, page = 1, pageSize = 100, returnDateRangePresetID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDateRangePresetIDClonedFrom = False, returnDateRangePresetIDClonedTo = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnHighDate = False, returnLowDate = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DateRangePreset/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDateRangePreset(DateRangePresetID, EntityID = 1, returnDateRangePresetID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDateRangePresetIDClonedFrom = False, returnDateRangePresetIDClonedTo = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnHighDate = False, returnLowDate = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DateRangePreset/" + str(DateRangePresetID), verb = "get", return_params_list = return_params_list)

def modifyDateRangePreset(DateRangePresetID, EntityID = 1, setCode = None, setDateRangePresetIDClonedFrom = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setHighDate = None, setLowDate = None, setSchoolYearID = None, setRelationships = None, returnDateRangePresetID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDateRangePresetIDClonedFrom = False, returnDateRangePresetIDClonedTo = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnHighDate = False, returnLowDate = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DateRangePreset/" + str(DateRangePresetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDateRangePreset(EntityID = 1, setCode = None, setDateRangePresetIDClonedFrom = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setHighDate = None, setLowDate = None, setSchoolYearID = None, setRelationships = None, returnDateRangePresetID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDateRangePresetIDClonedFrom = False, returnDateRangePresetIDClonedTo = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnHighDate = False, returnLowDate = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DateRangePreset/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDateRangePreset(DateRangePresetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDayRotation(EntityID = 1, page = 1, pageSize = 100, returnDayRotationID = True, returnCode = False, returnConsecutiveTeachingHourLimit = False, returnCreatedTime = False, returnDayRotationIDClonedFrom = False, returnDayRotationIDClonedTo = False, returnEntityGroupKey = False, returnEntityID = False, returnMaximumTeachingHourLimit = False, returnModifiedTime = False, returnSchoolYearID = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DayRotation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDayRotation(DayRotationID, EntityID = 1, returnDayRotationID = True, returnCode = False, returnConsecutiveTeachingHourLimit = False, returnCreatedTime = False, returnDayRotationIDClonedFrom = False, returnDayRotationIDClonedTo = False, returnEntityGroupKey = False, returnEntityID = False, returnMaximumTeachingHourLimit = False, returnModifiedTime = False, returnSchoolYearID = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DayRotation/" + str(DayRotationID), verb = "get", return_params_list = return_params_list)

def modifyDayRotation(DayRotationID, EntityID = 1, setCode = None, setConsecutiveTeachingHourLimit = None, setDayRotationIDClonedFrom = None, setEntityGroupKey = None, setEntityID = None, setMaximumTeachingHourLimit = None, setSchoolYearID = None, setSortNumber = None, setRelationships = None, returnDayRotationID = True, returnCode = False, returnConsecutiveTeachingHourLimit = False, returnCreatedTime = False, returnDayRotationIDClonedFrom = False, returnDayRotationIDClonedTo = False, returnEntityGroupKey = False, returnEntityID = False, returnMaximumTeachingHourLimit = False, returnModifiedTime = False, returnSchoolYearID = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DayRotation/" + str(DayRotationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDayRotation(EntityID = 1, setCode = None, setConsecutiveTeachingHourLimit = None, setDayRotationIDClonedFrom = None, setEntityGroupKey = None, setEntityID = None, setMaximumTeachingHourLimit = None, setSchoolYearID = None, setSortNumber = None, setRelationships = None, returnDayRotationID = True, returnCode = False, returnConsecutiveTeachingHourLimit = False, returnCreatedTime = False, returnDayRotationIDClonedFrom = False, returnDayRotationIDClonedTo = False, returnEntityGroupKey = False, returnEntityID = False, returnMaximumTeachingHourLimit = False, returnModifiedTime = False, returnSchoolYearID = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DayRotation/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDayRotation(DayRotationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDisplayPeriod(EntityID = 1, page = 1, pageSize = 100, returnDisplayPeriodID = True, returnAttendancePeriodID = False, returnCode = False, returnCodeDescription = False, returnCodeDescriptionDayRotation = False, returnCreatedTime = False, returnDayRotationID = False, returnDescription = False, returnDisplayPeriodCodeDayRotationCode = False, returnDisplayPeriodEndTime = False, returnDisplayPeriodIDClonedFrom = False, returnDisplayPeriodIDClonedTo = False, returnDisplayPeriodStartTime = False, returnEntityGroupKey = False, returnIsLunchPeriod = False, returnIsOutsideRegularSchoolDay = False, returnModifiedTime = False, returnSortNumber = False, returnTeachingHourEquivalent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDisplayPeriod(DisplayPeriodID, EntityID = 1, returnDisplayPeriodID = True, returnAttendancePeriodID = False, returnCode = False, returnCodeDescription = False, returnCodeDescriptionDayRotation = False, returnCreatedTime = False, returnDayRotationID = False, returnDescription = False, returnDisplayPeriodCodeDayRotationCode = False, returnDisplayPeriodEndTime = False, returnDisplayPeriodIDClonedFrom = False, returnDisplayPeriodIDClonedTo = False, returnDisplayPeriodStartTime = False, returnEntityGroupKey = False, returnIsLunchPeriod = False, returnIsOutsideRegularSchoolDay = False, returnModifiedTime = False, returnSortNumber = False, returnTeachingHourEquivalent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DisplayPeriod/" + str(DisplayPeriodID), verb = "get", return_params_list = return_params_list)

def modifyDisplayPeriod(DisplayPeriodID, EntityID = 1, setAttendancePeriodID = None, setCode = None, setDayRotationID = None, setDescription = None, setDisplayPeriodIDClonedFrom = None, setEntityGroupKey = None, setIsLunchPeriod = None, setIsOutsideRegularSchoolDay = None, setSortNumber = None, setTeachingHourEquivalent = None, setRelationships = None, returnDisplayPeriodID = True, returnAttendancePeriodID = False, returnCode = False, returnCodeDescription = False, returnCodeDescriptionDayRotation = False, returnCreatedTime = False, returnDayRotationID = False, returnDescription = False, returnDisplayPeriodCodeDayRotationCode = False, returnDisplayPeriodEndTime = False, returnDisplayPeriodIDClonedFrom = False, returnDisplayPeriodIDClonedTo = False, returnDisplayPeriodStartTime = False, returnEntityGroupKey = False, returnIsLunchPeriod = False, returnIsOutsideRegularSchoolDay = False, returnModifiedTime = False, returnSortNumber = False, returnTeachingHourEquivalent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DisplayPeriod/" + str(DisplayPeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDisplayPeriod(EntityID = 1, setAttendancePeriodID = None, setCode = None, setDayRotationID = None, setDescription = None, setDisplayPeriodIDClonedFrom = None, setEntityGroupKey = None, setIsLunchPeriod = None, setIsOutsideRegularSchoolDay = None, setSortNumber = None, setTeachingHourEquivalent = None, setRelationships = None, returnDisplayPeriodID = True, returnAttendancePeriodID = False, returnCode = False, returnCodeDescription = False, returnCodeDescriptionDayRotation = False, returnCreatedTime = False, returnDayRotationID = False, returnDescription = False, returnDisplayPeriodCodeDayRotationCode = False, returnDisplayPeriodEndTime = False, returnDisplayPeriodIDClonedFrom = False, returnDisplayPeriodIDClonedTo = False, returnDisplayPeriodStartTime = False, returnEntityGroupKey = False, returnIsLunchPeriod = False, returnIsOutsideRegularSchoolDay = False, returnModifiedTime = False, returnSortNumber = False, returnTeachingHourEquivalent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DisplayPeriod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDisplayPeriod(DisplayPeriodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDisplayPeriodConflict(EntityID = 1, page = 1, pageSize = 100, returnDisplayPeriodConflictID = True, returnCreatedTime = False, returnDisplayPeriodIDBase = False, returnDisplayPeriodIDConflicting = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DisplayPeriodConflict/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDisplayPeriodConflict(DisplayPeriodConflictID, EntityID = 1, returnDisplayPeriodConflictID = True, returnCreatedTime = False, returnDisplayPeriodIDBase = False, returnDisplayPeriodIDConflicting = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DisplayPeriodConflict/" + str(DisplayPeriodConflictID), verb = "get", return_params_list = return_params_list)

def modifyDisplayPeriodConflict(DisplayPeriodConflictID, EntityID = 1, setDisplayPeriodIDBase = None, setDisplayPeriodIDConflicting = None, setEntityGroupKey = None, setRelationships = None, returnDisplayPeriodConflictID = True, returnCreatedTime = False, returnDisplayPeriodIDBase = False, returnDisplayPeriodIDConflicting = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DisplayPeriodConflict/" + str(DisplayPeriodConflictID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDisplayPeriodConflict(EntityID = 1, setDisplayPeriodIDBase = None, setDisplayPeriodIDConflicting = None, setEntityGroupKey = None, setRelationships = None, returnDisplayPeriodConflictID = True, returnCreatedTime = False, returnDisplayPeriodIDBase = False, returnDisplayPeriodIDConflicting = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DisplayPeriodConflict/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDisplayPeriodConflict(DisplayPeriodConflictID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDisplayPeriodRotation(EntityID = 1, page = 1, pageSize = 100, returnDisplayPeriodRotationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayPeriodRotationIDClonedFrom = False, returnDisplayPeriodRotationIDClonedTo = False, returnDisplayPeriodSummary = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DisplayPeriodRotation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDisplayPeriodRotation(DisplayPeriodRotationID, EntityID = 1, returnDisplayPeriodRotationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayPeriodRotationIDClonedFrom = False, returnDisplayPeriodRotationIDClonedTo = False, returnDisplayPeriodSummary = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DisplayPeriodRotation/" + str(DisplayPeriodRotationID), verb = "get", return_params_list = return_params_list)

def modifyDisplayPeriodRotation(DisplayPeriodRotationID, EntityID = 1, setCode = None, setDescription = None, setDisplayPeriodRotationIDClonedFrom = None, setDisplayPeriodSummary = None, setEntityID = None, setSchoolYearID = None, setRelationships = None, returnDisplayPeriodRotationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayPeriodRotationIDClonedFrom = False, returnDisplayPeriodRotationIDClonedTo = False, returnDisplayPeriodSummary = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DisplayPeriodRotation/" + str(DisplayPeriodRotationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDisplayPeriodRotation(EntityID = 1, setCode = None, setDescription = None, setDisplayPeriodRotationIDClonedFrom = None, setDisplayPeriodSummary = None, setEntityID = None, setSchoolYearID = None, setRelationships = None, returnDisplayPeriodRotationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayPeriodRotationIDClonedFrom = False, returnDisplayPeriodRotationIDClonedTo = False, returnDisplayPeriodSummary = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DisplayPeriodRotation/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDisplayPeriodRotation(DisplayPeriodRotationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDisplayPeriodRotationDisplayPeriod(EntityID = 1, page = 1, pageSize = 100, returnDisplayPeriodRotationDisplayPeriodID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnDisplayPeriodRotationDisplayPeriodIDClonedFrom = False, returnDisplayPeriodRotationID = False, returnHideMeetDisplayPeriod = False, returnIsPrimary = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DisplayPeriodRotationDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDisplayPeriodRotationDisplayPeriod(DisplayPeriodRotationDisplayPeriodID, EntityID = 1, returnDisplayPeriodRotationDisplayPeriodID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnDisplayPeriodRotationDisplayPeriodIDClonedFrom = False, returnDisplayPeriodRotationID = False, returnHideMeetDisplayPeriod = False, returnIsPrimary = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DisplayPeriodRotationDisplayPeriod/" + str(DisplayPeriodRotationDisplayPeriodID), verb = "get", return_params_list = return_params_list)

def modifyDisplayPeriodRotationDisplayPeriod(DisplayPeriodRotationDisplayPeriodID, EntityID = 1, setDisplayPeriodID = None, setDisplayPeriodRotationDisplayPeriodIDClonedFrom = None, setDisplayPeriodRotationID = None, setHideMeetDisplayPeriod = None, setIsPrimary = None, setRelationships = None, returnDisplayPeriodRotationDisplayPeriodID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnDisplayPeriodRotationDisplayPeriodIDClonedFrom = False, returnDisplayPeriodRotationID = False, returnHideMeetDisplayPeriod = False, returnIsPrimary = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DisplayPeriodRotationDisplayPeriod/" + str(DisplayPeriodRotationDisplayPeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDisplayPeriodRotationDisplayPeriod(EntityID = 1, setDisplayPeriodID = None, setDisplayPeriodRotationDisplayPeriodIDClonedFrom = None, setDisplayPeriodRotationID = None, setHideMeetDisplayPeriod = None, setIsPrimary = None, setRelationships = None, returnDisplayPeriodRotationDisplayPeriodID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnDisplayPeriodRotationDisplayPeriodIDClonedFrom = False, returnDisplayPeriodRotationID = False, returnHideMeetDisplayPeriod = False, returnIsPrimary = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/DisplayPeriodRotationDisplayPeriod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDisplayPeriodRotationDisplayPeriod(DisplayPeriodRotationDisplayPeriodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEarlyExitReason(EntityID = 1, page = 1, pageSize = 100, returnEarlyExitReasonID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEarlyExitReasonIDClonedFrom = False, returnEntityGroupKey = False, returnEntityID = False, returnIsConsideredDrop = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/EarlyExitReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEarlyExitReason(EarlyExitReasonID, EntityID = 1, returnEarlyExitReasonID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEarlyExitReasonIDClonedFrom = False, returnEntityGroupKey = False, returnEntityID = False, returnIsConsideredDrop = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/EarlyExitReason/" + str(EarlyExitReasonID), verb = "get", return_params_list = return_params_list)

def modifyEarlyExitReason(EarlyExitReasonID, EntityID = 1, setCode = None, setDescription = None, setEarlyExitReasonIDClonedFrom = None, setEntityGroupKey = None, setEntityID = None, setIsConsideredDrop = None, setSchoolYearID = None, setRelationships = None, returnEarlyExitReasonID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEarlyExitReasonIDClonedFrom = False, returnEntityGroupKey = False, returnEntityID = False, returnIsConsideredDrop = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/EarlyExitReason/" + str(EarlyExitReasonID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEarlyExitReason(EntityID = 1, setCode = None, setDescription = None, setEarlyExitReasonIDClonedFrom = None, setEntityGroupKey = None, setEntityID = None, setIsConsideredDrop = None, setSchoolYearID = None, setRelationships = None, returnEarlyExitReasonID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEarlyExitReasonIDClonedFrom = False, returnEntityGroupKey = False, returnEntityID = False, returnIsConsideredDrop = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/EarlyExitReason/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEarlyExitReason(EarlyExitReasonID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryMassPrintStudentScheduleRunHistory(EntityID = 1, page = 1, pageSize = 100, returnMassPrintStudentScheduleRunHistoryID = True, returnCreatedTime = False, returnEntityID = False, returnMediaID = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnRequestIdentifier = False, returnRunDescription = False, returnSchoolYearID = False, returnSendMessageOnComplete = False, returnStudentSelectType = False, returnStudentSelectTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MassPrintStudentScheduleRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getMassPrintStudentScheduleRunHistory(MassPrintStudentScheduleRunHistoryID, EntityID = 1, returnMassPrintStudentScheduleRunHistoryID = True, returnCreatedTime = False, returnEntityID = False, returnMediaID = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnRequestIdentifier = False, returnRunDescription = False, returnSchoolYearID = False, returnSendMessageOnComplete = False, returnStudentSelectType = False, returnStudentSelectTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MassPrintStudentScheduleRunHistory/" + str(MassPrintStudentScheduleRunHistoryID), verb = "get", return_params_list = return_params_list)

def modifyMassPrintStudentScheduleRunHistory(MassPrintStudentScheduleRunHistoryID, EntityID = 1, setEntityID = None, setMediaID = None, setRequestIdentifier = None, setRunDescription = None, setSchoolYearID = None, setSendMessageOnComplete = None, setStudentSelectType = None, setStudentSelectTypeCode = None, setWorkflowInstanceID = None, setRelationships = None, returnMassPrintStudentScheduleRunHistoryID = True, returnCreatedTime = False, returnEntityID = False, returnMediaID = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnRequestIdentifier = False, returnRunDescription = False, returnSchoolYearID = False, returnSendMessageOnComplete = False, returnStudentSelectType = False, returnStudentSelectTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MassPrintStudentScheduleRunHistory/" + str(MassPrintStudentScheduleRunHistoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createMassPrintStudentScheduleRunHistory(EntityID = 1, setEntityID = None, setMediaID = None, setRequestIdentifier = None, setRunDescription = None, setSchoolYearID = None, setSendMessageOnComplete = None, setStudentSelectType = None, setStudentSelectTypeCode = None, setWorkflowInstanceID = None, setRelationships = None, returnMassPrintStudentScheduleRunHistoryID = True, returnCreatedTime = False, returnEntityID = False, returnMediaID = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnRequestIdentifier = False, returnRunDescription = False, returnSchoolYearID = False, returnSendMessageOnComplete = False, returnStudentSelectType = False, returnStudentSelectTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MassPrintStudentScheduleRunHistory/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteMassPrintStudentScheduleRunHistory(MassPrintStudentScheduleRunHistoryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryMaximumTeachingHourOverride(EntityID = 1, page = 1, pageSize = 100, returnMaximumTeachingHourOverrideID = True, returnCreatedTime = False, returnDayRotationID = False, returnMaximumConsecutiveTeachingHours = False, returnMaximumTeachingHourOverrideIDClonedFrom = False, returnMaximumTotalTeachingHours = False, returnModifiedTime = False, returnStaffEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MaximumTeachingHourOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getMaximumTeachingHourOverride(MaximumTeachingHourOverrideID, EntityID = 1, returnMaximumTeachingHourOverrideID = True, returnCreatedTime = False, returnDayRotationID = False, returnMaximumConsecutiveTeachingHours = False, returnMaximumTeachingHourOverrideIDClonedFrom = False, returnMaximumTotalTeachingHours = False, returnModifiedTime = False, returnStaffEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MaximumTeachingHourOverride/" + str(MaximumTeachingHourOverrideID), verb = "get", return_params_list = return_params_list)

def modifyMaximumTeachingHourOverride(MaximumTeachingHourOverrideID, EntityID = 1, setDayRotationID = None, setMaximumConsecutiveTeachingHours = None, setMaximumTeachingHourOverrideIDClonedFrom = None, setMaximumTotalTeachingHours = None, setStaffEntityYearID = None, setRelationships = None, returnMaximumTeachingHourOverrideID = True, returnCreatedTime = False, returnDayRotationID = False, returnMaximumConsecutiveTeachingHours = False, returnMaximumTeachingHourOverrideIDClonedFrom = False, returnMaximumTotalTeachingHours = False, returnModifiedTime = False, returnStaffEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MaximumTeachingHourOverride/" + str(MaximumTeachingHourOverrideID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createMaximumTeachingHourOverride(EntityID = 1, setDayRotationID = None, setMaximumConsecutiveTeachingHours = None, setMaximumTeachingHourOverrideIDClonedFrom = None, setMaximumTotalTeachingHours = None, setStaffEntityYearID = None, setRelationships = None, returnMaximumTeachingHourOverrideID = True, returnCreatedTime = False, returnDayRotationID = False, returnMaximumConsecutiveTeachingHours = False, returnMaximumTeachingHourOverrideIDClonedFrom = False, returnMaximumTotalTeachingHours = False, returnModifiedTime = False, returnStaffEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MaximumTeachingHourOverride/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteMaximumTeachingHourOverride(MaximumTeachingHourOverrideID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryMCCCTermGradeBucketMN(EntityID = 1, page = 1, pageSize = 100, returnMCCCTermGradeBucketMNID = True, returnCreatedTime = False, returnGradeBucketID = False, returnMCCCTermImportID = False, returnModifiedTime = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MCCCTermGradeBucketMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getMCCCTermGradeBucketMN(MCCCTermGradeBucketMNID, EntityID = 1, returnMCCCTermGradeBucketMNID = True, returnCreatedTime = False, returnGradeBucketID = False, returnMCCCTermImportID = False, returnModifiedTime = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MCCCTermGradeBucketMN/" + str(MCCCTermGradeBucketMNID), verb = "get", return_params_list = return_params_list)

def modifyMCCCTermGradeBucketMN(MCCCTermGradeBucketMNID, EntityID = 1, setGradeBucketID = None, setMCCCTermImportID = None, setSectionLengthID = None, setRelationships = None, returnMCCCTermGradeBucketMNID = True, returnCreatedTime = False, returnGradeBucketID = False, returnMCCCTermImportID = False, returnModifiedTime = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MCCCTermGradeBucketMN/" + str(MCCCTermGradeBucketMNID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createMCCCTermGradeBucketMN(EntityID = 1, setGradeBucketID = None, setMCCCTermImportID = None, setSectionLengthID = None, setRelationships = None, returnMCCCTermGradeBucketMNID = True, returnCreatedTime = False, returnGradeBucketID = False, returnMCCCTermImportID = False, returnModifiedTime = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MCCCTermGradeBucketMN/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteMCCCTermGradeBucketMN(MCCCTermGradeBucketMNID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryMeet(EntityID = 1, page = 1, pageSize = 100, returnMeetID = True, returnCalendarIDStaff = False, returnCreatedTime = False, returnDisplayPeriodRotationID = False, returnDurationInMinutes = False, returnEndDate = False, returnEntityID = False, returnHasDisplayPeriodRotationAssigned = False, returnIsAssignedToAHomeroomRoom = False, returnIsPrimary = False, returnLockAllMeetDayRotationsFromSectionScheduler = False, returnLockAllMeetDisplayPeriodsFromSectionScheduler = False, returnLockAllStaffMeetsFromSectionScheduler = False, returnLockRoomFromSectionScheduler = False, returnMeetIDClonedFrom = False, returnMeetIDClonedTo = False, returnModifiedTime = False, returnOverridePeriodEndTime = False, returnOverridePeriodStartTime = False, returnRoomID = False, returnSchoolYearID = False, returnSectionID = False, returnStartDate = False, returnStartDateEndDateBuildingCodeRoomNumber = False, returnTotalMeetDisplayPeriodCount = False, returnTotalStaffMeetCount = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/Meet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getMeet(MeetID, EntityID = 1, returnMeetID = True, returnCalendarIDStaff = False, returnCreatedTime = False, returnDisplayPeriodRotationID = False, returnDurationInMinutes = False, returnEndDate = False, returnEntityID = False, returnHasDisplayPeriodRotationAssigned = False, returnIsAssignedToAHomeroomRoom = False, returnIsPrimary = False, returnLockAllMeetDayRotationsFromSectionScheduler = False, returnLockAllMeetDisplayPeriodsFromSectionScheduler = False, returnLockAllStaffMeetsFromSectionScheduler = False, returnLockRoomFromSectionScheduler = False, returnMeetIDClonedFrom = False, returnMeetIDClonedTo = False, returnModifiedTime = False, returnOverridePeriodEndTime = False, returnOverridePeriodStartTime = False, returnRoomID = False, returnSchoolYearID = False, returnSectionID = False, returnStartDate = False, returnStartDateEndDateBuildingCodeRoomNumber = False, returnTotalMeetDisplayPeriodCount = False, returnTotalStaffMeetCount = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/Meet/" + str(MeetID), verb = "get", return_params_list = return_params_list)

def modifyMeet(MeetID, EntityID = 1, setCalendarIDStaff = None, setDisplayPeriodRotationID = None, setEndDate = None, setEntityID = None, setIsPrimary = None, setLockAllMeetDayRotationsFromSectionScheduler = None, setLockAllMeetDisplayPeriodsFromSectionScheduler = None, setLockAllStaffMeetsFromSectionScheduler = None, setLockRoomFromSectionScheduler = None, setMeetIDClonedFrom = None, setOverridePeriodEndTime = None, setOverridePeriodStartTime = None, setRoomID = None, setSchoolYearID = None, setSectionID = None, setStartDate = None, setType = None, setTypeCode = None, setRelationships = None, returnMeetID = True, returnCalendarIDStaff = False, returnCreatedTime = False, returnDisplayPeriodRotationID = False, returnDurationInMinutes = False, returnEndDate = False, returnEntityID = False, returnHasDisplayPeriodRotationAssigned = False, returnIsAssignedToAHomeroomRoom = False, returnIsPrimary = False, returnLockAllMeetDayRotationsFromSectionScheduler = False, returnLockAllMeetDisplayPeriodsFromSectionScheduler = False, returnLockAllStaffMeetsFromSectionScheduler = False, returnLockRoomFromSectionScheduler = False, returnMeetIDClonedFrom = False, returnMeetIDClonedTo = False, returnModifiedTime = False, returnOverridePeriodEndTime = False, returnOverridePeriodStartTime = False, returnRoomID = False, returnSchoolYearID = False, returnSectionID = False, returnStartDate = False, returnStartDateEndDateBuildingCodeRoomNumber = False, returnTotalMeetDisplayPeriodCount = False, returnTotalStaffMeetCount = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/Meet/" + str(MeetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createMeet(EntityID = 1, setCalendarIDStaff = None, setDisplayPeriodRotationID = None, setEndDate = None, setEntityID = None, setIsPrimary = None, setLockAllMeetDayRotationsFromSectionScheduler = None, setLockAllMeetDisplayPeriodsFromSectionScheduler = None, setLockAllStaffMeetsFromSectionScheduler = None, setLockRoomFromSectionScheduler = None, setMeetIDClonedFrom = None, setOverridePeriodEndTime = None, setOverridePeriodStartTime = None, setRoomID = None, setSchoolYearID = None, setSectionID = None, setStartDate = None, setType = None, setTypeCode = None, setRelationships = None, returnMeetID = True, returnCalendarIDStaff = False, returnCreatedTime = False, returnDisplayPeriodRotationID = False, returnDurationInMinutes = False, returnEndDate = False, returnEntityID = False, returnHasDisplayPeriodRotationAssigned = False, returnIsAssignedToAHomeroomRoom = False, returnIsPrimary = False, returnLockAllMeetDayRotationsFromSectionScheduler = False, returnLockAllMeetDisplayPeriodsFromSectionScheduler = False, returnLockAllStaffMeetsFromSectionScheduler = False, returnLockRoomFromSectionScheduler = False, returnMeetIDClonedFrom = False, returnMeetIDClonedTo = False, returnModifiedTime = False, returnOverridePeriodEndTime = False, returnOverridePeriodStartTime = False, returnRoomID = False, returnSchoolYearID = False, returnSectionID = False, returnStartDate = False, returnStartDateEndDateBuildingCodeRoomNumber = False, returnTotalMeetDisplayPeriodCount = False, returnTotalStaffMeetCount = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/Meet/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteMeet(MeetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryMeetDisplayPeriod(EntityID = 1, page = 1, pageSize = 100, returnMeetDisplayPeriodID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnHideMeetDisplayPeriod = False, returnIsPrimary = False, returnLockDisplayPeriod = False, returnMeetDisplayPeriodIDClonedFrom = False, returnMeetID = False, returnModifiedTime = False, returnScheduledBySectionScheduler = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getMeetDisplayPeriod(MeetDisplayPeriodID, EntityID = 1, returnMeetDisplayPeriodID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnHideMeetDisplayPeriod = False, returnIsPrimary = False, returnLockDisplayPeriod = False, returnMeetDisplayPeriodIDClonedFrom = False, returnMeetID = False, returnModifiedTime = False, returnScheduledBySectionScheduler = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetDisplayPeriod/" + str(MeetDisplayPeriodID), verb = "get", return_params_list = return_params_list)

def modifyMeetDisplayPeriod(MeetDisplayPeriodID, EntityID = 1, setDisplayPeriodID = None, setHideMeetDisplayPeriod = None, setIsPrimary = None, setLockDisplayPeriod = None, setMeetDisplayPeriodIDClonedFrom = None, setMeetID = None, setScheduledBySectionScheduler = None, setRelationships = None, returnMeetDisplayPeriodID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnHideMeetDisplayPeriod = False, returnIsPrimary = False, returnLockDisplayPeriod = False, returnMeetDisplayPeriodIDClonedFrom = False, returnMeetID = False, returnModifiedTime = False, returnScheduledBySectionScheduler = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetDisplayPeriod/" + str(MeetDisplayPeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createMeetDisplayPeriod(EntityID = 1, setDisplayPeriodID = None, setHideMeetDisplayPeriod = None, setIsPrimary = None, setLockDisplayPeriod = None, setMeetDisplayPeriodIDClonedFrom = None, setMeetID = None, setScheduledBySectionScheduler = None, setRelationships = None, returnMeetDisplayPeriodID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnHideMeetDisplayPeriod = False, returnIsPrimary = False, returnLockDisplayPeriod = False, returnMeetDisplayPeriodIDClonedFrom = False, returnMeetID = False, returnModifiedTime = False, returnScheduledBySectionScheduler = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetDisplayPeriod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteMeetDisplayPeriod(MeetDisplayPeriodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryMeetRequirement(EntityID = 1, page = 1, pageSize = 100, returnMeetRequirementID = True, returnAllowMultiplePeriodsPerDayRotation = False, returnCourseID = False, returnCreatedTime = False, returnDaysPerRotation = False, returnForceConsecutivePeriods = False, returnMeetRequirementIDClonedFrom = False, returnMeetRequirementIDClonedTo = False, returnMinutesPerDay = False, returnModifiedTime = False, returnTimeSpanAnalysisType = False, returnTimeSpanAnalysisTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetRequirement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getMeetRequirement(MeetRequirementID, EntityID = 1, returnMeetRequirementID = True, returnAllowMultiplePeriodsPerDayRotation = False, returnCourseID = False, returnCreatedTime = False, returnDaysPerRotation = False, returnForceConsecutivePeriods = False, returnMeetRequirementIDClonedFrom = False, returnMeetRequirementIDClonedTo = False, returnMinutesPerDay = False, returnModifiedTime = False, returnTimeSpanAnalysisType = False, returnTimeSpanAnalysisTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetRequirement/" + str(MeetRequirementID), verb = "get", return_params_list = return_params_list)

def modifyMeetRequirement(MeetRequirementID, EntityID = 1, setAllowMultiplePeriodsPerDayRotation = None, setCourseID = None, setDaysPerRotation = None, setForceConsecutivePeriods = None, setMeetRequirementIDClonedFrom = None, setMinutesPerDay = None, setTimeSpanAnalysisType = None, setTimeSpanAnalysisTypeCode = None, setRelationships = None, returnMeetRequirementID = True, returnAllowMultiplePeriodsPerDayRotation = False, returnCourseID = False, returnCreatedTime = False, returnDaysPerRotation = False, returnForceConsecutivePeriods = False, returnMeetRequirementIDClonedFrom = False, returnMeetRequirementIDClonedTo = False, returnMinutesPerDay = False, returnModifiedTime = False, returnTimeSpanAnalysisType = False, returnTimeSpanAnalysisTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetRequirement/" + str(MeetRequirementID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createMeetRequirement(EntityID = 1, setAllowMultiplePeriodsPerDayRotation = None, setCourseID = None, setDaysPerRotation = None, setForceConsecutivePeriods = None, setMeetRequirementIDClonedFrom = None, setMinutesPerDay = None, setTimeSpanAnalysisType = None, setTimeSpanAnalysisTypeCode = None, setRelationships = None, returnMeetRequirementID = True, returnAllowMultiplePeriodsPerDayRotation = False, returnCourseID = False, returnCreatedTime = False, returnDaysPerRotation = False, returnForceConsecutivePeriods = False, returnMeetRequirementIDClonedFrom = False, returnMeetRequirementIDClonedTo = False, returnMinutesPerDay = False, returnModifiedTime = False, returnTimeSpanAnalysisType = False, returnTimeSpanAnalysisTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetRequirement/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteMeetRequirement(MeetRequirementID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryMeetSummary(EntityID = 1, page = 1, pageSize = 100, returnMeetSummaryID = True, returnCalculatedDays = False, returnCalculatedDaysStudent = False, returnCalculatedPeriod = False, returnCalculatedPeriodStudent = False, returnCalendarID = False, returnCreatedTime = False, returnDays = False, returnEntityIDViewing = False, returnHasOnlyHiddenDetails = False, returnIsDefaultCalendar = False, returnIsPrimary = False, returnMeetID = False, returnModifiedTime = False, returnPeriod = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetSummary/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getMeetSummary(MeetSummaryID, EntityID = 1, returnMeetSummaryID = True, returnCalculatedDays = False, returnCalculatedDaysStudent = False, returnCalculatedPeriod = False, returnCalculatedPeriodStudent = False, returnCalendarID = False, returnCreatedTime = False, returnDays = False, returnEntityIDViewing = False, returnHasOnlyHiddenDetails = False, returnIsDefaultCalendar = False, returnIsPrimary = False, returnMeetID = False, returnModifiedTime = False, returnPeriod = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetSummary/" + str(MeetSummaryID), verb = "get", return_params_list = return_params_list)

def modifyMeetSummary(MeetSummaryID, EntityID = 1, setCalendarID = None, setDays = None, setEntityIDViewing = None, setHasOnlyHiddenDetails = None, setIsDefaultCalendar = None, setIsPrimary = None, setMeetID = None, setPeriod = None, setRelationships = None, returnMeetSummaryID = True, returnCalculatedDays = False, returnCalculatedDaysStudent = False, returnCalculatedPeriod = False, returnCalculatedPeriodStudent = False, returnCalendarID = False, returnCreatedTime = False, returnDays = False, returnEntityIDViewing = False, returnHasOnlyHiddenDetails = False, returnIsDefaultCalendar = False, returnIsPrimary = False, returnMeetID = False, returnModifiedTime = False, returnPeriod = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetSummary/" + str(MeetSummaryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createMeetSummary(EntityID = 1, setCalendarID = None, setDays = None, setEntityIDViewing = None, setHasOnlyHiddenDetails = None, setIsDefaultCalendar = None, setIsPrimary = None, setMeetID = None, setPeriod = None, setRelationships = None, returnMeetSummaryID = True, returnCalculatedDays = False, returnCalculatedDaysStudent = False, returnCalculatedPeriod = False, returnCalculatedPeriodStudent = False, returnCalendarID = False, returnCreatedTime = False, returnDays = False, returnEntityIDViewing = False, returnHasOnlyHiddenDetails = False, returnIsDefaultCalendar = False, returnIsPrimary = False, returnMeetID = False, returnModifiedTime = False, returnPeriod = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetSummary/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteMeetSummary(MeetSummaryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryMeetSummaryDetail(EntityID = 1, page = 1, pageSize = 100, returnMeetSummaryDetailID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnIsPrimary = False, returnMeetSummaryID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetSummaryDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getMeetSummaryDetail(MeetSummaryDetailID, EntityID = 1, returnMeetSummaryDetailID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnIsPrimary = False, returnMeetSummaryID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetSummaryDetail/" + str(MeetSummaryDetailID), verb = "get", return_params_list = return_params_list)

def modifyMeetSummaryDetail(MeetSummaryDetailID, EntityID = 1, setDisplayPeriodID = None, setIsPrimary = None, setMeetSummaryID = None, setRelationships = None, returnMeetSummaryDetailID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnIsPrimary = False, returnMeetSummaryID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetSummaryDetail/" + str(MeetSummaryDetailID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createMeetSummaryDetail(EntityID = 1, setDisplayPeriodID = None, setIsPrimary = None, setMeetSummaryID = None, setRelationships = None, returnMeetSummaryDetailID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnIsPrimary = False, returnMeetSummaryID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/MeetSummaryDetail/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteMeetSummaryDetail(MeetSummaryDetailID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryOpenPeriodAnalysis(EntityID = 1, page = 1, pageSize = 100, returnOpenPeriodAnalysisID = True, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDPerformer = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/OpenPeriodAnalysis/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getOpenPeriodAnalysis(OpenPeriodAnalysisID, EntityID = 1, returnOpenPeriodAnalysisID = True, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDPerformer = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/OpenPeriodAnalysis/" + str(OpenPeriodAnalysisID), verb = "get", return_params_list = return_params_list)

def modifyOpenPeriodAnalysis(OpenPeriodAnalysisID, EntityID = 1, setEndTime = None, setEntityID = None, setSchoolYearID = None, setStartTime = None, setStatus = None, setStatusCode = None, setUserIDPerformer = None, setRelationships = None, returnOpenPeriodAnalysisID = True, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDPerformer = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/OpenPeriodAnalysis/" + str(OpenPeriodAnalysisID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createOpenPeriodAnalysis(EntityID = 1, setEndTime = None, setEntityID = None, setSchoolYearID = None, setStartTime = None, setStatus = None, setStatusCode = None, setUserIDPerformer = None, setRelationships = None, returnOpenPeriodAnalysisID = True, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDPerformer = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/OpenPeriodAnalysis/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteOpenPeriodAnalysis(OpenPeriodAnalysisID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryOpenPeriodAnalysisStudent(EntityID = 1, page = 1, pageSize = 100, returnOpenPeriodAnalysisStudentID = True, returnCreatedTime = False, returnFirstName = False, returnGradeLevelCode = False, returnIsActive = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnOpenPeriodAnalysisID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/OpenPeriodAnalysisStudent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getOpenPeriodAnalysisStudent(OpenPeriodAnalysisStudentID, EntityID = 1, returnOpenPeriodAnalysisStudentID = True, returnCreatedTime = False, returnFirstName = False, returnGradeLevelCode = False, returnIsActive = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnOpenPeriodAnalysisID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/OpenPeriodAnalysisStudent/" + str(OpenPeriodAnalysisStudentID), verb = "get", return_params_list = return_params_list)

def modifyOpenPeriodAnalysisStudent(OpenPeriodAnalysisStudentID, EntityID = 1, setFirstName = None, setGradeLevelCode = None, setIsActive = None, setLastName = None, setMiddleName = None, setOpenPeriodAnalysisID = None, setStudentID = None, setStudentNumber = None, setRelationships = None, returnOpenPeriodAnalysisStudentID = True, returnCreatedTime = False, returnFirstName = False, returnGradeLevelCode = False, returnIsActive = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnOpenPeriodAnalysisID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/OpenPeriodAnalysisStudent/" + str(OpenPeriodAnalysisStudentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createOpenPeriodAnalysisStudent(EntityID = 1, setFirstName = None, setGradeLevelCode = None, setIsActive = None, setLastName = None, setMiddleName = None, setOpenPeriodAnalysisID = None, setStudentID = None, setStudentNumber = None, setRelationships = None, returnOpenPeriodAnalysisStudentID = True, returnCreatedTime = False, returnFirstName = False, returnGradeLevelCode = False, returnIsActive = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnOpenPeriodAnalysisID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/OpenPeriodAnalysisStudent/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteOpenPeriodAnalysisStudent(OpenPeriodAnalysisStudentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryProcessRestriction(EntityID = 1, page = 1, pageSize = 100, returnProcessRestrictionID = True, returnCreatedTime = False, returnEntityID = False, returnLockCourseMaster = False, returnLockCourseMasterSetByMassStudentSchedulerUtility = False, returnLockMassStudentSchedulerUtility = False, returnLockMassStudentSchedulerUtilitySetByMassStudentSchedulerUtility = False, returnLockMassUnscheduleStudentSectionsUtility = False, returnLockMassUnscheduleStudentSectionsUtilitySetByMassStudentSchedulerUtility = False, returnLockSchedulingBoard = False, returnLockSchedulingBoardSetByMassStudentSchedulerUtility = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDLockCourseMasterPerformer = False, returnUserIDLockMassStudentSchedulerUtilityPerformer = False, returnUserIDLockMassUnscheduleStudentSectionsUtilityPerformer = False, returnUserIDLockSchedulingBoardPerformer = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/ProcessRestriction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getProcessRestriction(ProcessRestrictionID, EntityID = 1, returnProcessRestrictionID = True, returnCreatedTime = False, returnEntityID = False, returnLockCourseMaster = False, returnLockCourseMasterSetByMassStudentSchedulerUtility = False, returnLockMassStudentSchedulerUtility = False, returnLockMassStudentSchedulerUtilitySetByMassStudentSchedulerUtility = False, returnLockMassUnscheduleStudentSectionsUtility = False, returnLockMassUnscheduleStudentSectionsUtilitySetByMassStudentSchedulerUtility = False, returnLockSchedulingBoard = False, returnLockSchedulingBoardSetByMassStudentSchedulerUtility = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDLockCourseMasterPerformer = False, returnUserIDLockMassStudentSchedulerUtilityPerformer = False, returnUserIDLockMassUnscheduleStudentSectionsUtilityPerformer = False, returnUserIDLockSchedulingBoardPerformer = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/ProcessRestriction/" + str(ProcessRestrictionID), verb = "get", return_params_list = return_params_list)

def modifyProcessRestriction(ProcessRestrictionID, EntityID = 1, setEntityID = None, setLockCourseMaster = None, setLockCourseMasterSetByMassStudentSchedulerUtility = None, setLockMassStudentSchedulerUtility = None, setLockMassStudentSchedulerUtilitySetByMassStudentSchedulerUtility = None, setLockMassUnscheduleStudentSectionsUtility = None, setLockMassUnscheduleStudentSectionsUtilitySetByMassStudentSchedulerUtility = None, setLockSchedulingBoard = None, setLockSchedulingBoardSetByMassStudentSchedulerUtility = None, setSchoolYearID = None, setUserIDLockCourseMasterPerformer = None, setUserIDLockMassStudentSchedulerUtilityPerformer = None, setUserIDLockMassUnscheduleStudentSectionsUtilityPerformer = None, setUserIDLockSchedulingBoardPerformer = None, setRelationships = None, returnProcessRestrictionID = True, returnCreatedTime = False, returnEntityID = False, returnLockCourseMaster = False, returnLockCourseMasterSetByMassStudentSchedulerUtility = False, returnLockMassStudentSchedulerUtility = False, returnLockMassStudentSchedulerUtilitySetByMassStudentSchedulerUtility = False, returnLockMassUnscheduleStudentSectionsUtility = False, returnLockMassUnscheduleStudentSectionsUtilitySetByMassStudentSchedulerUtility = False, returnLockSchedulingBoard = False, returnLockSchedulingBoardSetByMassStudentSchedulerUtility = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDLockCourseMasterPerformer = False, returnUserIDLockMassStudentSchedulerUtilityPerformer = False, returnUserIDLockMassUnscheduleStudentSectionsUtilityPerformer = False, returnUserIDLockSchedulingBoardPerformer = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/ProcessRestriction/" + str(ProcessRestrictionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createProcessRestriction(EntityID = 1, setEntityID = None, setLockCourseMaster = None, setLockCourseMasterSetByMassStudentSchedulerUtility = None, setLockMassStudentSchedulerUtility = None, setLockMassStudentSchedulerUtilitySetByMassStudentSchedulerUtility = None, setLockMassUnscheduleStudentSectionsUtility = None, setLockMassUnscheduleStudentSectionsUtilitySetByMassStudentSchedulerUtility = None, setLockSchedulingBoard = None, setLockSchedulingBoardSetByMassStudentSchedulerUtility = None, setSchoolYearID = None, setUserIDLockCourseMasterPerformer = None, setUserIDLockMassStudentSchedulerUtilityPerformer = None, setUserIDLockMassUnscheduleStudentSectionsUtilityPerformer = None, setUserIDLockSchedulingBoardPerformer = None, setRelationships = None, returnProcessRestrictionID = True, returnCreatedTime = False, returnEntityID = False, returnLockCourseMaster = False, returnLockCourseMasterSetByMassStudentSchedulerUtility = False, returnLockMassStudentSchedulerUtility = False, returnLockMassStudentSchedulerUtilitySetByMassStudentSchedulerUtility = False, returnLockMassUnscheduleStudentSectionsUtility = False, returnLockMassUnscheduleStudentSectionsUtilitySetByMassStudentSchedulerUtility = False, returnLockSchedulingBoard = False, returnLockSchedulingBoardSetByMassStudentSchedulerUtility = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDLockCourseMasterPerformer = False, returnUserIDLockMassStudentSchedulerUtilityPerformer = False, returnUserIDLockMassUnscheduleStudentSectionsUtilityPerformer = False, returnUserIDLockSchedulingBoardPerformer = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/ProcessRestriction/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteProcessRestriction(ProcessRestrictionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryScheduleRestorePoint(EntityID = 1, page = 1, pageSize = 100, returnScheduleRestorePointID = True, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnReportQueueID = False, returnRestorePointDateTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/ScheduleRestorePoint/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getScheduleRestorePoint(ScheduleRestorePointID, EntityID = 1, returnScheduleRestorePointID = True, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnReportQueueID = False, returnRestorePointDateTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/ScheduleRestorePoint/" + str(ScheduleRestorePointID), verb = "get", return_params_list = return_params_list)

def modifyScheduleRestorePoint(ScheduleRestorePointID, EntityID = 1, setDescription = None, setEntityID = None, setName = None, setReportQueueID = None, setRestorePointDateTime = None, setSchoolYearID = None, setRelationships = None, returnScheduleRestorePointID = True, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnReportQueueID = False, returnRestorePointDateTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/ScheduleRestorePoint/" + str(ScheduleRestorePointID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createScheduleRestorePoint(EntityID = 1, setDescription = None, setEntityID = None, setName = None, setReportQueueID = None, setRestorePointDateTime = None, setSchoolYearID = None, setRelationships = None, returnScheduleRestorePointID = True, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnReportQueueID = False, returnRestorePointDateTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/ScheduleRestorePoint/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteScheduleRestorePoint(ScheduleRestorePointID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySchedulingBoardFilter(EntityID = 1, page = 1, pageSize = 100, returnSchedulingBoardFilterID = True, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingBoardFilter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSchedulingBoardFilter(SchedulingBoardFilterID, EntityID = 1, returnSchedulingBoardFilterID = True, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingBoardFilter/" + str(SchedulingBoardFilterID), verb = "get", return_params_list = return_params_list)

def modifySchedulingBoardFilter(SchedulingBoardFilterID, EntityID = 1, setDescription = None, setDisplayOrder = None, setSkywardHash = None, setSkywardID = None, setType = None, setTypeCode = None, setRelationships = None, returnSchedulingBoardFilterID = True, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingBoardFilter/" + str(SchedulingBoardFilterID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSchedulingBoardFilter(EntityID = 1, setDescription = None, setDisplayOrder = None, setSkywardHash = None, setSkywardID = None, setType = None, setTypeCode = None, setRelationships = None, returnSchedulingBoardFilterID = True, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingBoardFilter/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSchedulingBoardFilter(SchedulingBoardFilterID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySchedulingCategory(EntityID = 1, page = 1, pageSize = 100, returnSchedulingCategoryID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchedulingCategoryIDClonedFrom = False, returnSchedulingCategoryIDClonedTo = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSchedulingCategory(SchedulingCategoryID, EntityID = 1, returnSchedulingCategoryID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchedulingCategoryIDClonedFrom = False, returnSchedulingCategoryIDClonedTo = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingCategory/" + str(SchedulingCategoryID), verb = "get", return_params_list = return_params_list)

def modifySchedulingCategory(SchedulingCategoryID, EntityID = 1, setCode = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setSchedulingCategoryIDClonedFrom = None, setSchoolYearID = None, setRelationships = None, returnSchedulingCategoryID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchedulingCategoryIDClonedFrom = False, returnSchedulingCategoryIDClonedTo = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingCategory/" + str(SchedulingCategoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSchedulingCategory(EntityID = 1, setCode = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setSchedulingCategoryIDClonedFrom = None, setSchoolYearID = None, setRelationships = None, returnSchedulingCategoryID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchedulingCategoryIDClonedFrom = False, returnSchedulingCategoryIDClonedTo = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingCategory/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSchedulingCategory(SchedulingCategoryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySchedulingGroup(EntityID = 1, page = 1, pageSize = 100, returnSchedulingGroupID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnGradeReferenceID = False, returnHomeroomID = False, returnModifiedTime = False, returnSchedulingGroupIDClonedFrom = False, returnSchedulingGroupIDClonedTo = False, returnSchoolYearID = False, returnTotalSchedulingGroupCoursesCount = False, returnTotalSchedulingGroupSectionsCount = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSchedulingGroup(SchedulingGroupID, EntityID = 1, returnSchedulingGroupID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnGradeReferenceID = False, returnHomeroomID = False, returnModifiedTime = False, returnSchedulingGroupIDClonedFrom = False, returnSchedulingGroupIDClonedTo = False, returnSchoolYearID = False, returnTotalSchedulingGroupCoursesCount = False, returnTotalSchedulingGroupSectionsCount = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingGroup/" + str(SchedulingGroupID), verb = "get", return_params_list = return_params_list)

def modifySchedulingGroup(SchedulingGroupID, EntityID = 1, setCode = None, setDescription = None, setEntityID = None, setGradeReferenceID = None, setHomeroomID = None, setSchedulingGroupIDClonedFrom = None, setSchoolYearID = None, setType = None, setTypeCode = None, setRelationships = None, returnSchedulingGroupID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnGradeReferenceID = False, returnHomeroomID = False, returnModifiedTime = False, returnSchedulingGroupIDClonedFrom = False, returnSchedulingGroupIDClonedTo = False, returnSchoolYearID = False, returnTotalSchedulingGroupCoursesCount = False, returnTotalSchedulingGroupSectionsCount = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingGroup/" + str(SchedulingGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSchedulingGroup(EntityID = 1, setCode = None, setDescription = None, setEntityID = None, setGradeReferenceID = None, setHomeroomID = None, setSchedulingGroupIDClonedFrom = None, setSchoolYearID = None, setType = None, setTypeCode = None, setRelationships = None, returnSchedulingGroupID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnGradeReferenceID = False, returnHomeroomID = False, returnModifiedTime = False, returnSchedulingGroupIDClonedFrom = False, returnSchedulingGroupIDClonedTo = False, returnSchoolYearID = False, returnTotalSchedulingGroupCoursesCount = False, returnTotalSchedulingGroupSectionsCount = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSchedulingGroup(SchedulingGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySchedulingGroupCourse(EntityID = 1, page = 1, pageSize = 100, returnSchedulingGroupCourseID = True, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingGroupCourseIDClonedFrom = False, returnSchedulingGroupCourseIDClonedTo = False, returnSchedulingGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingGroupCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSchedulingGroupCourse(SchedulingGroupCourseID, EntityID = 1, returnSchedulingGroupCourseID = True, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingGroupCourseIDClonedFrom = False, returnSchedulingGroupCourseIDClonedTo = False, returnSchedulingGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingGroupCourse/" + str(SchedulingGroupCourseID), verb = "get", return_params_list = return_params_list)

def modifySchedulingGroupCourse(SchedulingGroupCourseID, EntityID = 1, setCourseID = None, setSchedulingGroupCourseIDClonedFrom = None, setSchedulingGroupID = None, setRelationships = None, returnSchedulingGroupCourseID = True, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingGroupCourseIDClonedFrom = False, returnSchedulingGroupCourseIDClonedTo = False, returnSchedulingGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingGroupCourse/" + str(SchedulingGroupCourseID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSchedulingGroupCourse(EntityID = 1, setCourseID = None, setSchedulingGroupCourseIDClonedFrom = None, setSchedulingGroupID = None, setRelationships = None, returnSchedulingGroupCourseID = True, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingGroupCourseIDClonedFrom = False, returnSchedulingGroupCourseIDClonedTo = False, returnSchedulingGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingGroupCourse/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSchedulingGroupCourse(SchedulingGroupCourseID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySchedulingGroupSection(EntityID = 1, page = 1, pageSize = 100, returnSchedulingGroupSectionID = True, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingGroupID = False, returnSchedulingGroupSectionIDClonedFrom = False, returnSchedulingGroupSectionIDClonedTo = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingGroupSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSchedulingGroupSection(SchedulingGroupSectionID, EntityID = 1, returnSchedulingGroupSectionID = True, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingGroupID = False, returnSchedulingGroupSectionIDClonedFrom = False, returnSchedulingGroupSectionIDClonedTo = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingGroupSection/" + str(SchedulingGroupSectionID), verb = "get", return_params_list = return_params_list)

def modifySchedulingGroupSection(SchedulingGroupSectionID, EntityID = 1, setSchedulingGroupID = None, setSchedulingGroupSectionIDClonedFrom = None, setSectionID = None, setRelationships = None, returnSchedulingGroupSectionID = True, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingGroupID = False, returnSchedulingGroupSectionIDClonedFrom = False, returnSchedulingGroupSectionIDClonedTo = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingGroupSection/" + str(SchedulingGroupSectionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSchedulingGroupSection(EntityID = 1, setSchedulingGroupID = None, setSchedulingGroupSectionIDClonedFrom = None, setSectionID = None, setRelationships = None, returnSchedulingGroupSectionID = True, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingGroupID = False, returnSchedulingGroupSectionIDClonedFrom = False, returnSchedulingGroupSectionIDClonedTo = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingGroupSection/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSchedulingGroupSection(SchedulingGroupSectionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySchedulingPeriod(EntityID = 1, page = 1, pageSize = 100, returnSchedulingPeriodID = True, returnCodeNumber = False, returnCreatedTime = False, returnDayRotationID = False, returnEntityGroupKey = False, returnModifiedTime = False, returnSchedulingPeriodIDClonedFrom = False, returnSchedulingPeriodIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSchedulingPeriod(SchedulingPeriodID, EntityID = 1, returnSchedulingPeriodID = True, returnCodeNumber = False, returnCreatedTime = False, returnDayRotationID = False, returnEntityGroupKey = False, returnModifiedTime = False, returnSchedulingPeriodIDClonedFrom = False, returnSchedulingPeriodIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingPeriod/" + str(SchedulingPeriodID), verb = "get", return_params_list = return_params_list)

def modifySchedulingPeriod(SchedulingPeriodID, EntityID = 1, setCodeNumber = None, setDayRotationID = None, setEntityGroupKey = None, setSchedulingPeriodIDClonedFrom = None, setRelationships = None, returnSchedulingPeriodID = True, returnCodeNumber = False, returnCreatedTime = False, returnDayRotationID = False, returnEntityGroupKey = False, returnModifiedTime = False, returnSchedulingPeriodIDClonedFrom = False, returnSchedulingPeriodIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingPeriod/" + str(SchedulingPeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSchedulingPeriod(EntityID = 1, setCodeNumber = None, setDayRotationID = None, setEntityGroupKey = None, setSchedulingPeriodIDClonedFrom = None, setRelationships = None, returnSchedulingPeriodID = True, returnCodeNumber = False, returnCreatedTime = False, returnDayRotationID = False, returnEntityGroupKey = False, returnModifiedTime = False, returnSchedulingPeriodIDClonedFrom = False, returnSchedulingPeriodIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingPeriod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSchedulingPeriod(SchedulingPeriodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySchedulingPeriodDisplayPeriod(EntityID = 1, page = 1, pageSize = 100, returnSchedulingPeriodDisplayPeriodID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnEntityGroupKey = False, returnLabel = False, returnModifiedTime = False, returnSchedulingPeriodDisplayPeriodIDClonedFrom = False, returnSchedulingPeriodID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingPeriodDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSchedulingPeriodDisplayPeriod(SchedulingPeriodDisplayPeriodID, EntityID = 1, returnSchedulingPeriodDisplayPeriodID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnEntityGroupKey = False, returnLabel = False, returnModifiedTime = False, returnSchedulingPeriodDisplayPeriodIDClonedFrom = False, returnSchedulingPeriodID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingPeriodDisplayPeriod/" + str(SchedulingPeriodDisplayPeriodID), verb = "get", return_params_list = return_params_list)

def modifySchedulingPeriodDisplayPeriod(SchedulingPeriodDisplayPeriodID, EntityID = 1, setDisplayPeriodID = None, setEntityGroupKey = None, setSchedulingPeriodDisplayPeriodIDClonedFrom = None, setSchedulingPeriodID = None, setRelationships = None, returnSchedulingPeriodDisplayPeriodID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnEntityGroupKey = False, returnLabel = False, returnModifiedTime = False, returnSchedulingPeriodDisplayPeriodIDClonedFrom = False, returnSchedulingPeriodID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingPeriodDisplayPeriod/" + str(SchedulingPeriodDisplayPeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSchedulingPeriodDisplayPeriod(EntityID = 1, setDisplayPeriodID = None, setEntityGroupKey = None, setSchedulingPeriodDisplayPeriodIDClonedFrom = None, setSchedulingPeriodID = None, setRelationships = None, returnSchedulingPeriodDisplayPeriodID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnEntityGroupKey = False, returnLabel = False, returnModifiedTime = False, returnSchedulingPeriodDisplayPeriodIDClonedFrom = False, returnSchedulingPeriodID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingPeriodDisplayPeriod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSchedulingPeriodDisplayPeriod(SchedulingPeriodDisplayPeriodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySchedulingTeam(EntityID = 1, page = 1, pageSize = 100, returnSchedulingTeamID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchedulingTeamIDClonedFrom = False, returnSchedulingTeamIDClonedTo = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingTeam/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSchedulingTeam(SchedulingTeamID, EntityID = 1, returnSchedulingTeamID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchedulingTeamIDClonedFrom = False, returnSchedulingTeamIDClonedTo = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingTeam/" + str(SchedulingTeamID), verb = "get", return_params_list = return_params_list)

def modifySchedulingTeam(SchedulingTeamID, EntityID = 1, setCode = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setSchedulingTeamIDClonedFrom = None, setSchoolYearID = None, setRelationships = None, returnSchedulingTeamID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchedulingTeamIDClonedFrom = False, returnSchedulingTeamIDClonedTo = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingTeam/" + str(SchedulingTeamID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSchedulingTeam(EntityID = 1, setCode = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setSchedulingTeamIDClonedFrom = None, setSchoolYearID = None, setRelationships = None, returnSchedulingTeamID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchedulingTeamIDClonedFrom = False, returnSchedulingTeamIDClonedTo = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingTeam/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSchedulingTeam(SchedulingTeamID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySchedulingTeamGradeReference(EntityID = 1, page = 1, pageSize = 100, returnSchedulingTeamGradeReferenceID = True, returnCreatedTime = False, returnGradeReferenceID = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnSchedulingTeamGradeReferenceIDClonedFrom = False, returnSchedulingTeamID = False, returnStudentEntityYearsCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingTeamGradeReference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSchedulingTeamGradeReference(SchedulingTeamGradeReferenceID, EntityID = 1, returnSchedulingTeamGradeReferenceID = True, returnCreatedTime = False, returnGradeReferenceID = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnSchedulingTeamGradeReferenceIDClonedFrom = False, returnSchedulingTeamID = False, returnStudentEntityYearsCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingTeamGradeReference/" + str(SchedulingTeamGradeReferenceID), verb = "get", return_params_list = return_params_list)

def modifySchedulingTeamGradeReference(SchedulingTeamGradeReferenceID, EntityID = 1, setGradeReferenceID = None, setMaximumStudentCount = None, setSchedulingTeamGradeReferenceIDClonedFrom = None, setSchedulingTeamID = None, setRelationships = None, returnSchedulingTeamGradeReferenceID = True, returnCreatedTime = False, returnGradeReferenceID = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnSchedulingTeamGradeReferenceIDClonedFrom = False, returnSchedulingTeamID = False, returnStudentEntityYearsCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingTeamGradeReference/" + str(SchedulingTeamGradeReferenceID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSchedulingTeamGradeReference(EntityID = 1, setGradeReferenceID = None, setMaximumStudentCount = None, setSchedulingTeamGradeReferenceIDClonedFrom = None, setSchedulingTeamID = None, setRelationships = None, returnSchedulingTeamGradeReferenceID = True, returnCreatedTime = False, returnGradeReferenceID = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnSchedulingTeamGradeReferenceIDClonedFrom = False, returnSchedulingTeamID = False, returnStudentEntityYearsCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SchedulingTeamGradeReference/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSchedulingTeamGradeReference(SchedulingTeamGradeReferenceID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionCorequisiteGroup(EntityID = 1, page = 1, pageSize = 100, returnSectionCorequisiteGroupID = True, returnAutomaticRequestSetting = False, returnAutomaticRequestSettingCode = False, returnAutomaticScheduleSetting = False, returnAutomaticScheduleSettingCode = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnScheduleAllSectionsInGroupOrNone = False, returnSectionCorequisiteGroupIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionCorequisiteGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionCorequisiteGroup(SectionCorequisiteGroupID, EntityID = 1, returnSectionCorequisiteGroupID = True, returnAutomaticRequestSetting = False, returnAutomaticRequestSettingCode = False, returnAutomaticScheduleSetting = False, returnAutomaticScheduleSettingCode = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnScheduleAllSectionsInGroupOrNone = False, returnSectionCorequisiteGroupIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionCorequisiteGroup/" + str(SectionCorequisiteGroupID), verb = "get", return_params_list = return_params_list)

def modifySectionCorequisiteGroup(SectionCorequisiteGroupID, EntityID = 1, setAutomaticRequestSetting = None, setAutomaticRequestSettingCode = None, setAutomaticScheduleSetting = None, setAutomaticScheduleSettingCode = None, setDescription = None, setEntityID = None, setName = None, setScheduleAllSectionsInGroupOrNone = None, setRelationships = None, returnSectionCorequisiteGroupID = True, returnAutomaticRequestSetting = False, returnAutomaticRequestSettingCode = False, returnAutomaticScheduleSetting = False, returnAutomaticScheduleSettingCode = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnScheduleAllSectionsInGroupOrNone = False, returnSectionCorequisiteGroupIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionCorequisiteGroup/" + str(SectionCorequisiteGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionCorequisiteGroup(EntityID = 1, setAutomaticRequestSetting = None, setAutomaticRequestSettingCode = None, setAutomaticScheduleSetting = None, setAutomaticScheduleSettingCode = None, setDescription = None, setEntityID = None, setName = None, setScheduleAllSectionsInGroupOrNone = None, setRelationships = None, returnSectionCorequisiteGroupID = True, returnAutomaticRequestSetting = False, returnAutomaticRequestSettingCode = False, returnAutomaticScheduleSetting = False, returnAutomaticScheduleSettingCode = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnScheduleAllSectionsInGroupOrNone = False, returnSectionCorequisiteGroupIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionCorequisiteGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionCorequisiteGroup(SectionCorequisiteGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionCorequisiteGroupSection(EntityID = 1, page = 1, pageSize = 100, returnSectionCorequisiteGroupSectionID = True, returnCreatedTime = False, returnModifiedTime = False, returnSectionCorequisiteGroupID = False, returnSectionCorequisiteGroupSectionIDClonedFrom = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionCorequisiteGroupSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionCorequisiteGroupSection(SectionCorequisiteGroupSectionID, EntityID = 1, returnSectionCorequisiteGroupSectionID = True, returnCreatedTime = False, returnModifiedTime = False, returnSectionCorequisiteGroupID = False, returnSectionCorequisiteGroupSectionIDClonedFrom = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionCorequisiteGroupSection/" + str(SectionCorequisiteGroupSectionID), verb = "get", return_params_list = return_params_list)

def modifySectionCorequisiteGroupSection(SectionCorequisiteGroupSectionID, EntityID = 1, setSectionCorequisiteGroupID = None, setSectionCorequisiteGroupSectionIDClonedFrom = None, setSectionID = None, setRelationships = None, returnSectionCorequisiteGroupSectionID = True, returnCreatedTime = False, returnModifiedTime = False, returnSectionCorequisiteGroupID = False, returnSectionCorequisiteGroupSectionIDClonedFrom = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionCorequisiteGroupSection/" + str(SectionCorequisiteGroupSectionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionCorequisiteGroupSection(EntityID = 1, setSectionCorequisiteGroupID = None, setSectionCorequisiteGroupSectionIDClonedFrom = None, setSectionID = None, setRelationships = None, returnSectionCorequisiteGroupSectionID = True, returnCreatedTime = False, returnModifiedTime = False, returnSectionCorequisiteGroupID = False, returnSectionCorequisiteGroupSectionIDClonedFrom = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionCorequisiteGroupSection/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionCorequisiteGroupSection(SectionCorequisiteGroupSectionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionCustomRequirement(EntityID = 1, page = 1, pageSize = 100, returnSectionCustomRequirementID = True, returnCreatedTime = False, returnCustomRequirementID = False, returnModifiedTime = False, returnSectionCustomRequirementIDClonedFrom = False, returnSectionCustomRequirementIDClonedTo = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionCustomRequirement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionCustomRequirement(SectionCustomRequirementID, EntityID = 1, returnSectionCustomRequirementID = True, returnCreatedTime = False, returnCustomRequirementID = False, returnModifiedTime = False, returnSectionCustomRequirementIDClonedFrom = False, returnSectionCustomRequirementIDClonedTo = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionCustomRequirement/" + str(SectionCustomRequirementID), verb = "get", return_params_list = return_params_list)

def modifySectionCustomRequirement(SectionCustomRequirementID, EntityID = 1, setCustomRequirementID = None, setSectionCustomRequirementIDClonedFrom = None, setSectionID = None, setRelationships = None, returnSectionCustomRequirementID = True, returnCreatedTime = False, returnCustomRequirementID = False, returnModifiedTime = False, returnSectionCustomRequirementIDClonedFrom = False, returnSectionCustomRequirementIDClonedTo = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionCustomRequirement/" + str(SectionCustomRequirementID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionCustomRequirement(EntityID = 1, setCustomRequirementID = None, setSectionCustomRequirementIDClonedFrom = None, setSectionID = None, setRelationships = None, returnSectionCustomRequirementID = True, returnCreatedTime = False, returnCustomRequirementID = False, returnModifiedTime = False, returnSectionCustomRequirementIDClonedFrom = False, returnSectionCustomRequirementIDClonedTo = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionCustomRequirement/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionCustomRequirement(SectionCustomRequirementID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionDefault(EntityID = 1, page = 1, pageSize = 100, returnSectionDefaultID = True, returnCourseID = False, returnCreatedTime = False, returnMaximumStudentCount = False, returnMinimumStudentCount = False, returnModifiedTime = False, returnOptimalStudentCount = False, returnSectionDefaultIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionDefault(SectionDefaultID, EntityID = 1, returnSectionDefaultID = True, returnCourseID = False, returnCreatedTime = False, returnMaximumStudentCount = False, returnMinimumStudentCount = False, returnModifiedTime = False, returnOptimalStudentCount = False, returnSectionDefaultIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionDefault/" + str(SectionDefaultID), verb = "get", return_params_list = return_params_list)

def modifySectionDefault(SectionDefaultID, EntityID = 1, setCourseID = None, setMaximumStudentCount = None, setMinimumStudentCount = None, setOptimalStudentCount = None, setSectionDefaultIDClonedFrom = None, setRelationships = None, returnSectionDefaultID = True, returnCourseID = False, returnCreatedTime = False, returnMaximumStudentCount = False, returnMinimumStudentCount = False, returnModifiedTime = False, returnOptimalStudentCount = False, returnSectionDefaultIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionDefault/" + str(SectionDefaultID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionDefault(EntityID = 1, setCourseID = None, setMaximumStudentCount = None, setMinimumStudentCount = None, setOptimalStudentCount = None, setSectionDefaultIDClonedFrom = None, setRelationships = None, returnSectionDefaultID = True, returnCourseID = False, returnCreatedTime = False, returnMaximumStudentCount = False, returnMinimumStudentCount = False, returnModifiedTime = False, returnOptimalStudentCount = False, returnSectionDefaultIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionDefault/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionDefault(SectionDefaultID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionEnrollmentTotalForSectionLengthSubset(EntityID = 1, page = 1, pageSize = 100, returnSectionID = True, returnSectionLengthSubsetID = False, returnTotalEnrollmentCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionEnrollmentTotalForSectionLengthSubset/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionEnrollmentTotalForSectionLengthSubset(SectionID, EntityID = 1, returnSectionID = True, returnSectionLengthSubsetID = False, returnTotalEnrollmentCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionEnrollmentTotalForSectionLengthSubset/" + str(SectionID), verb = "get", return_params_list = return_params_list)

def modifySectionEnrollmentTotalForSectionLengthSubset(SectionID, EntityID = 1, setRelationships = None, returnSectionID = True, returnSectionLengthSubsetID = False, returnTotalEnrollmentCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionEnrollmentTotalForSectionLengthSubset/" + str(SectionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionEnrollmentTotalForSectionLengthSubset(EntityID = 1, setRelationships = None, returnSectionID = True, returnSectionLengthSubsetID = False, returnTotalEnrollmentCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionEnrollmentTotalForSectionLengthSubset/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionEnrollmentTotalForSectionLengthSubset(SectionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionEnrollmentTotalForSectionLengthSubsetAndEntity(EntityID = 1, page = 1, pageSize = 100, returnSectionID = True, returnEntityIDCountsAs = False, returnSectionLengthSubsetID = False, returnTotalEnrollmentCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionEnrollmentTotalForSectionLengthSubsetAndEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionEnrollmentTotalForSectionLengthSubsetAndEntity(SectionID, EntityID = 1, returnSectionID = True, returnEntityIDCountsAs = False, returnSectionLengthSubsetID = False, returnTotalEnrollmentCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionEnrollmentTotalForSectionLengthSubsetAndEntity/" + str(SectionID), verb = "get", return_params_list = return_params_list)

def modifySectionEnrollmentTotalForSectionLengthSubsetAndEntity(SectionID, EntityID = 1, setRelationships = None, returnSectionID = True, returnEntityIDCountsAs = False, returnSectionLengthSubsetID = False, returnTotalEnrollmentCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionEnrollmentTotalForSectionLengthSubsetAndEntity/" + str(SectionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionEnrollmentTotalForSectionLengthSubsetAndEntity(EntityID = 1, setRelationships = None, returnSectionID = True, returnEntityIDCountsAs = False, returnSectionLengthSubsetID = False, returnTotalEnrollmentCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionEnrollmentTotalForSectionLengthSubsetAndEntity/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionEnrollmentTotalForSectionLengthSubsetAndEntity(SectionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionLength(EntityID = 1, page = 1, pageSize = 100, returnSectionLengthID = True, returnCode = False, returnCodeDescription = False, returnCourseLengthID = False, returnCreatedTime = False, returnDescription = False, returnEdFiTermTypeID = False, returnEndDate = False, returnEntityGroupKey = False, returnIsSectionCurrent = False, returnMCCCDropDate = False, returnModifiedTime = False, returnSectionLengthIDClonedFrom = False, returnSectionLengthIDClonedTo = False, returnSectionLengthMNID = False, returnSectionRange = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionLength/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionLength(SectionLengthID, EntityID = 1, returnSectionLengthID = True, returnCode = False, returnCodeDescription = False, returnCourseLengthID = False, returnCreatedTime = False, returnDescription = False, returnEdFiTermTypeID = False, returnEndDate = False, returnEntityGroupKey = False, returnIsSectionCurrent = False, returnMCCCDropDate = False, returnModifiedTime = False, returnSectionLengthIDClonedFrom = False, returnSectionLengthIDClonedTo = False, returnSectionLengthMNID = False, returnSectionRange = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionLength/" + str(SectionLengthID), verb = "get", return_params_list = return_params_list)

def modifySectionLength(SectionLengthID, EntityID = 1, setCode = None, setCourseLengthID = None, setDescription = None, setEdFiTermTypeID = None, setEndDate = None, setEntityGroupKey = None, setMCCCDropDate = None, setSectionLengthIDClonedFrom = None, setStartDate = None, setRelationships = None, returnSectionLengthID = True, returnCode = False, returnCodeDescription = False, returnCourseLengthID = False, returnCreatedTime = False, returnDescription = False, returnEdFiTermTypeID = False, returnEndDate = False, returnEntityGroupKey = False, returnIsSectionCurrent = False, returnMCCCDropDate = False, returnModifiedTime = False, returnSectionLengthIDClonedFrom = False, returnSectionLengthIDClonedTo = False, returnSectionLengthMNID = False, returnSectionRange = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionLength/" + str(SectionLengthID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionLength(EntityID = 1, setCode = None, setCourseLengthID = None, setDescription = None, setEdFiTermTypeID = None, setEndDate = None, setEntityGroupKey = None, setMCCCDropDate = None, setSectionLengthIDClonedFrom = None, setStartDate = None, setRelationships = None, returnSectionLengthID = True, returnCode = False, returnCodeDescription = False, returnCourseLengthID = False, returnCreatedTime = False, returnDescription = False, returnEdFiTermTypeID = False, returnEndDate = False, returnEntityGroupKey = False, returnIsSectionCurrent = False, returnMCCCDropDate = False, returnModifiedTime = False, returnSectionLengthIDClonedFrom = False, returnSectionLengthIDClonedTo = False, returnSectionLengthMNID = False, returnSectionRange = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionLength/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionLength(SectionLengthID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionLengthSubset(EntityID = 1, page = 1, pageSize = 100, returnSectionLengthSubsetID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiTermTypeID = False, returnEndDate = False, returnEntityGroupKey = False, returnGradeBucketIDCarlPerkins = False, returnIsFullSectionLength = False, returnMCCCDropDate = False, returnMCCCTermImportID = False, returnModifiedTime = False, returnSectionLengthID = False, returnSectionLengthSubsetIDClonedFrom = False, returnSectionLengthSubsetIDClonedTo = False, returnSectionLengthSubsetMNID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionLengthSubset/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionLengthSubset(SectionLengthSubsetID, EntityID = 1, returnSectionLengthSubsetID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiTermTypeID = False, returnEndDate = False, returnEntityGroupKey = False, returnGradeBucketIDCarlPerkins = False, returnIsFullSectionLength = False, returnMCCCDropDate = False, returnMCCCTermImportID = False, returnModifiedTime = False, returnSectionLengthID = False, returnSectionLengthSubsetIDClonedFrom = False, returnSectionLengthSubsetIDClonedTo = False, returnSectionLengthSubsetMNID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionLengthSubset/" + str(SectionLengthSubsetID), verb = "get", return_params_list = return_params_list)

def modifySectionLengthSubset(SectionLengthSubsetID, EntityID = 1, setCode = None, setDescription = None, setEdFiTermTypeID = None, setEndDate = None, setEntityGroupKey = None, setGradeBucketIDCarlPerkins = None, setIsFullSectionLength = None, setMCCCDropDate = None, setMCCCTermImportID = None, setSectionLengthID = None, setSectionLengthSubsetIDClonedFrom = None, setStartDate = None, setRelationships = None, returnSectionLengthSubsetID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiTermTypeID = False, returnEndDate = False, returnEntityGroupKey = False, returnGradeBucketIDCarlPerkins = False, returnIsFullSectionLength = False, returnMCCCDropDate = False, returnMCCCTermImportID = False, returnModifiedTime = False, returnSectionLengthID = False, returnSectionLengthSubsetIDClonedFrom = False, returnSectionLengthSubsetIDClonedTo = False, returnSectionLengthSubsetMNID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionLengthSubset/" + str(SectionLengthSubsetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionLengthSubset(EntityID = 1, setCode = None, setDescription = None, setEdFiTermTypeID = None, setEndDate = None, setEntityGroupKey = None, setGradeBucketIDCarlPerkins = None, setIsFullSectionLength = None, setMCCCDropDate = None, setMCCCTermImportID = None, setSectionLengthID = None, setSectionLengthSubsetIDClonedFrom = None, setStartDate = None, setRelationships = None, returnSectionLengthSubsetID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiTermTypeID = False, returnEndDate = False, returnEntityGroupKey = False, returnGradeBucketIDCarlPerkins = False, returnIsFullSectionLength = False, returnMCCCDropDate = False, returnMCCCTermImportID = False, returnModifiedTime = False, returnSectionLengthID = False, returnSectionLengthSubsetIDClonedFrom = False, returnSectionLengthSubsetIDClonedTo = False, returnSectionLengthSubsetMNID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionLengthSubset/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionLengthSubset(SectionLengthSubsetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionMeetSummary(EntityID = 1, page = 1, pageSize = 100, returnSectionMeetSummaryID = True, returnCalendarID = False, returnCreatedTime = False, returnEntityIDViewing = False, returnIsDefaultCalendar = False, returnModifiedTime = False, returnPeriodDaySummary = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionMeetSummary/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionMeetSummary(SectionMeetSummaryID, EntityID = 1, returnSectionMeetSummaryID = True, returnCalendarID = False, returnCreatedTime = False, returnEntityIDViewing = False, returnIsDefaultCalendar = False, returnModifiedTime = False, returnPeriodDaySummary = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionMeetSummary/" + str(SectionMeetSummaryID), verb = "get", return_params_list = return_params_list)

def modifySectionMeetSummary(SectionMeetSummaryID, EntityID = 1, setCalendarID = None, setEntityIDViewing = None, setIsDefaultCalendar = None, setPeriodDaySummary = None, setSectionID = None, setRelationships = None, returnSectionMeetSummaryID = True, returnCalendarID = False, returnCreatedTime = False, returnEntityIDViewing = False, returnIsDefaultCalendar = False, returnModifiedTime = False, returnPeriodDaySummary = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionMeetSummary/" + str(SectionMeetSummaryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionMeetSummary(EntityID = 1, setCalendarID = None, setEntityIDViewing = None, setIsDefaultCalendar = None, setPeriodDaySummary = None, setSectionID = None, setRelationships = None, returnSectionMeetSummaryID = True, returnCalendarID = False, returnCreatedTime = False, returnEntityIDViewing = False, returnIsDefaultCalendar = False, returnModifiedTime = False, returnPeriodDaySummary = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionMeetSummary/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionMeetSummary(SectionMeetSummaryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySection(EntityID = 1, page = 1, pageSize = 100, returnSectionID = True, returnAllowCECE = False, returnAllowStudentsWithoutCategoryToBeAssigned = False, returnAssignmentCount = False, returnAssignmentCountForTerm = False, returnAssignmentCountForTermCalculated = False, returnAssignmentCountYTD = False, returnAssignmentCountYTDCalculated = False, returnAssignmentDataString = False, returnAssignmentsHaveBeenCreated = False, returnBellScheduleGroupID = False, returnCalculatedBellScheduleGroupID = False, returnCalculatedStudentEnrollmentCount = False, returnCalculatedStudentEnrollmentCountEntity = False, returnCalculatedStudentEnrollmentCountEntityFirstDay = False, returnCalculatedStudentEnrollmentCountEntitySpecifiedDate = False, returnCalculatedStudentEnrollmentCountEntityToday = False, returnCalculatedStudentEnrollmentCountFirstDay = False, returnCalculatedStudentEnrollmentCountSpecifiedDate = False, returnCalculatedStudentEnrollmentCountToday = False, returnCalendarIDMCCCOverride = False, returnCanAddStudentSection = False, returnCanBeOffered = False, returnCode = False, returnCourseCodeSectionCode = False, returnCourseCodeSectionCodeCourseDescription = False, returnCourseDescriptionCodeSectionCode = False, returnCourseID = False, returnCourseIDHash = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnCurrentEnrollmentEntity = False, returnCurrentEnrollmentEntityForFilter = False, returnCurrentEnrollmentForFilter = False, returnCurrentGradingPeriod = False, returnCurrentlyRecalculating = False, returnDisplayForTeachers = False, returnDisplayPeriodIDCurrentStoredPrimary = False, returnDueDateOfLastAssignmentScored = False, returnEdFiEducationalEnvironmentID = False, returnEffectiveTeacherFirstLastName = False, returnEffectiveTeacherLastFirstName = False, returnEntityCodeTeacherNumber = False, returnEntityID = False, returnExcludeFromStudentSectionLink = False, returnExcusedAbsencesForTerm = False, returnExcusedAbsencesYTD = False, returnFit = False, returnFutureAssignmentCountForTerm = False, returnFutureAssignmentCountForTermCalculated = False, returnGradebookCanHaveSettingsCopiedFromPreviousYear = False, returnGradedAssignmentCountForTerm = False, returnGradedAssignmentCountForTermCalculated = False, returnHasAssignments = False, returnHasAssignmentsWithAcademicStandards = False, returnHasAssignmentsWithStudentGroups = False, returnHasAssignmentsWithSubjects = False, returnHasCalculationGroupCourse = False, returnHasCategoriesInDistrict = False, returnHasClosedOrCompletedSectionGradingScaleGroup = False, returnHasCompleted = False, returnHasCompletedForFilter = False, returnHasGradeMarksInEntity = False, returnHasGradingPeriodGradeBuckets = False, returnHasGradingScales = False, returnHasIncompleteClosedGradeChangeRequests = False, returnHasNotStarted = False, returnHasNotStartedForFilter = False, returnHasPreviousYearSettings = False, returnHasStandardsCheckSectionLengthGradingPeriodSet = False, returnHasStudentSections = False, returnHasSubjectsCheckSectionLengthGradingPeriodSet = False, returnHasValidGradebookSetup = False, returnHasValidStandardsSetup = False, returnHasValidSubjectsSetup = False, returnHomeroomID = False, returnInPastYear = False, returnIsActive = False, returnIsActiveOverride = False, returnIsAdministeredForTSA = False, returnIsAHistoricRecord = False, returnIsBilingual = False, returnIsCreditRecovery = False, returnIsInProgress = False, returnIsInProgressForFilter = False, returnIsOffered = False, returnIsOfferedToAnotherEntity = False, returnIsSelfPaced = False, returnIsSelfPacedAndActive = False, returnIsTSAProficient = False, returnLanguageID = False, returnLockSectionFromSectionScheduler = False, returnLockSectionLengthFromSectionScheduler = False, returnMaximumStudentCount = False, returnMaximumStudentCountEntity = False, returnMaximumStudentCountEntityForFilter = False, returnMaximumStudentCountForEntityOfCourse = False, returnMaximumStudentCountForViewingEntity = False, returnMaximumStudentCountOffered = False, returnMaximumStudentCountOfferedForFilter = False, returnMaximumStudentCountOfferedToSpecifiedEntity = False, returnMeetIDCurrentStoredPrimary = False, returnMeetSummaryIDCurrentStoredPrimary = False, returnMinimumStudentCount = False, returnMissingAssignmentCount = False, returnMissingAssignmentCountForTerm = False, returnMissingAssignmentCountForTermCalculated = False, returnModifiedTime = False, returnNoCountAssignmentCountForTerm = False, returnNoCountAssignmentCountForTermCalculated = False, returnNonGradedAssignmentCountForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnNonTransferCourseEnrollmentCountFemales = False, returnNonTransferCourseEnrollmentCountFemalesEntity = False, returnNonTransferCourseEnrollmentCountFemalesEntityFirstDay = False, returnNonTransferCourseEnrollmentCountFemalesEntitySpecifiedDate = False, returnNonTransferCourseEnrollmentCountFemalesEntityToday = False, returnNonTransferCourseEnrollmentCountFemalesFirstDay = False, returnNonTransferCourseEnrollmentCountFemalesSpecifiedDate = False, returnNonTransferCourseEnrollmentCountFemalesToday = False, returnNonTransferCourseEnrollmentCountMales = False, returnNonTransferCourseEnrollmentCountMalesEntity = False, returnNonTransferCourseEnrollmentCountMalesEntityFirstDay = False, returnNonTransferCourseEnrollmentCountMalesEntitySpecifiedDate = False, returnNonTransferCourseEnrollmentCountMalesEntityToday = False, returnNonTransferCourseEnrollmentCountMalesFirstDay = False, returnNonTransferCourseEnrollmentCountMalesSpecifiedDate = False, returnNonTransferCourseEnrollmentCountMalesToday = False, returnNonTransferCourseStudentEnrollmentCount = False, returnNonTransferCourseStudentEnrollmentCountEntity = False, returnNonTransferCourseStudentEnrollmentCountEntityFirstDay = False, returnNonTransferCourseStudentEnrollmentCountEntitySpecifiedDate = False, returnNonTransferCourseStudentEnrollmentCountEntityToday = False, returnNonTransferCourseStudentEnrollmentCountFirstDay = False, returnNonTransferCourseStudentEnrollmentCountSpecifiedDate = False, returnNonTransferCourseStudentEnrollmentCountToday = False, returnNumberOfTransferStudentSections = False, returnNumberOfTransferStudentSectionsForFilter = False, returnOffenseCount = False, returnOffenseCountYTD = False, returnOptimalStudentCount = False, returnOtherAbsencesForTerm = False, returnOtherAbsencesYTD = False, returnPeriodDaySummary = False, returnPreviousVersionOfFit = False, returnProgressStatusSpecifiedDate = False, returnProgressStatusToday = False, returnRecalculateGradebook = False, returnRecalculateGradebookAdmin = False, returnReservedSeatCount = False, returnSchedulingCategories = False, returnSchedulingTeams = False, returnSchoolYearID = False, returnScoreClarifierAssignmentCountForTerm = False, returnScoreClarifierAssignmentCountForTermCalculated = False, returnScoredAssignmentCount = False, returnScoredAssignmentRange0CurrentTerm = False, returnScoredAssignmentRange100to90CurrentTerm = False, returnScoredAssignmentRange49to1CurrentTerm = False, returnScoredAssignmentRange59to50CurrentTerm = False, returnScoredAssignmentRange69to60CurrentTerm = False, returnScoredAssignmentRange79to70CurrentTerm = False, returnScoredAssignmentRange89to80CurrentTerm = False, returnSeatsAvailable = False, returnSeatsAvailableEntity = False, returnSeatsAvailableEntityForFilter = False, returnSeatsAvailableForFilter = False, returnSectionEnrollmentTotalsForSectionLengthSubsetSummary = False, returnSectionEnrollmentTotalsForSectionLengthSubsetSummaryForEntity = False, returnSectionIDClonedFrom = False, returnSectionIDClonedTo = False, returnSectionIDHash = False, returnSectionLengthID = False, returnSectionLengthScheduledBySectionScheduler = False, returnSectionMNID = False, returnSelfPacedEndTime = False, returnSelfPacedEndTimeDate = False, returnSelfPacedEndTimeTime = False, returnSingleSex = False, returnSingleSexCode = False, returnSpecialEdPercentageLimit = False, returnSpecifiedPeriodDaySummary = False, returnStaffIDCurrentStoredPrimary = False, returnStaffMeetIDCurrentStoredPrimary = False, returnStateInstructionalMethodCodeMNID = False, returnStateSTARModeOfTeachingMNID = False, returnStudentAssignmentDataString = False, returnStudentCountForTerm = False, returnStudentEnrollment = False, returnStudentEnrollmentAsOfSpecifiedDate = False, returnStudentEnrollmentAsOfSpecifiedDateForFilter = False, returnStudentEnrollmentEntity = False, returnStudentEnrollmentEntityForFilter = False, returnStudentEnrollmentFemales = False, returnStudentEnrollmentFemalesAsOfSpecifiedDate = False, returnStudentEnrollmentFemalesAsOfSpecifiedDateForFilter = False, returnStudentEnrollmentFemalesEntity = False, returnStudentEnrollmentFemalesEntityForFilter = False, returnStudentEnrollmentFemalesForFilter = False, returnStudentEnrollmentForFilter = False, returnStudentEnrollmentMales = False, returnStudentEnrollmentMalesAsOfSpecifiedDate = False, returnStudentEnrollmentMalesAsOfSpecifiedDateForFilter = False, returnStudentEnrollmentMalesEntity = False, returnStudentEnrollmentMalesEntityForFilter = False, returnStudentEnrollmentMalesForFilter = False, returnStudentSectionSectionIDHash = False, returnTardiesForTerm = False, returnTardiesYTD = False, returnThisPeriodDaySummary = False, returnTotalEnrollmentCount = False, returnTotalEnrollmentCountEntity = False, returnTotalEnrollmentCountEntityForFilter = False, returnTotalEnrollmentCountForFilter = False, returnTotalMeetCount = False, returnTotalSeatsOfferedToOtherEntities = False, returnTransferCourseEnrollmentCountFemales = False, returnTransferCourseEnrollmentCountFemalesEntity = False, returnTransferCourseEnrollmentCountFemalesEntityFirstDay = False, returnTransferCourseEnrollmentCountFemalesEntitySpecifiedDate = False, returnTransferCourseEnrollmentCountFemalesEntityToday = False, returnTransferCourseEnrollmentCountFemalesFirstDay = False, returnTransferCourseEnrollmentCountFemalesSpecifiedDate = False, returnTransferCourseEnrollmentCountFemalesToday = False, returnTransferCourseEnrollmentCountMales = False, returnTransferCourseEnrollmentCountMalesEntity = False, returnTransferCourseEnrollmentCountMalesEntityFirstDay = False, returnTransferCourseEnrollmentCountMalesEntitySpecifiedDate = False, returnTransferCourseEnrollmentCountMalesEntityToday = False, returnTransferCourseEnrollmentCountMalesFirstDay = False, returnTransferCourseEnrollmentCountMalesSpecifiedDate = False, returnTransferCourseEnrollmentCountMalesToday = False, returnTransferCourseStudentEnrollmentCount = False, returnTransferCourseStudentEnrollmentCountEntity = False, returnTransferCourseStudentEnrollmentCountEntityFirstDay = False, returnTransferCourseStudentEnrollmentCountEntitySpecifiedDate = False, returnTransferCourseStudentEnrollmentCountEntityToday = False, returnTransferCourseStudentEnrollmentCountFirstDay = False, returnTransferCourseStudentEnrollmentCountSpecifiedDate = False, returnTransferCourseStudentEnrollmentCountToday = False, returnUnexcusedAbsencesForTerm = False, returnUnexcusedAbsencesYTD = False, returnUnscoredAssignmentCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, returnWebsite = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/Section/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSection(SectionID, EntityID = 1, returnSectionID = True, returnAllowCECE = False, returnAllowStudentsWithoutCategoryToBeAssigned = False, returnAssignmentCount = False, returnAssignmentCountForTerm = False, returnAssignmentCountForTermCalculated = False, returnAssignmentCountYTD = False, returnAssignmentCountYTDCalculated = False, returnAssignmentDataString = False, returnAssignmentsHaveBeenCreated = False, returnBellScheduleGroupID = False, returnCalculatedBellScheduleGroupID = False, returnCalculatedStudentEnrollmentCount = False, returnCalculatedStudentEnrollmentCountEntity = False, returnCalculatedStudentEnrollmentCountEntityFirstDay = False, returnCalculatedStudentEnrollmentCountEntitySpecifiedDate = False, returnCalculatedStudentEnrollmentCountEntityToday = False, returnCalculatedStudentEnrollmentCountFirstDay = False, returnCalculatedStudentEnrollmentCountSpecifiedDate = False, returnCalculatedStudentEnrollmentCountToday = False, returnCalendarIDMCCCOverride = False, returnCanAddStudentSection = False, returnCanBeOffered = False, returnCode = False, returnCourseCodeSectionCode = False, returnCourseCodeSectionCodeCourseDescription = False, returnCourseDescriptionCodeSectionCode = False, returnCourseID = False, returnCourseIDHash = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnCurrentEnrollmentEntity = False, returnCurrentEnrollmentEntityForFilter = False, returnCurrentEnrollmentForFilter = False, returnCurrentGradingPeriod = False, returnCurrentlyRecalculating = False, returnDisplayForTeachers = False, returnDisplayPeriodIDCurrentStoredPrimary = False, returnDueDateOfLastAssignmentScored = False, returnEdFiEducationalEnvironmentID = False, returnEffectiveTeacherFirstLastName = False, returnEffectiveTeacherLastFirstName = False, returnEntityCodeTeacherNumber = False, returnEntityID = False, returnExcludeFromStudentSectionLink = False, returnExcusedAbsencesForTerm = False, returnExcusedAbsencesYTD = False, returnFit = False, returnFutureAssignmentCountForTerm = False, returnFutureAssignmentCountForTermCalculated = False, returnGradebookCanHaveSettingsCopiedFromPreviousYear = False, returnGradedAssignmentCountForTerm = False, returnGradedAssignmentCountForTermCalculated = False, returnHasAssignments = False, returnHasAssignmentsWithAcademicStandards = False, returnHasAssignmentsWithStudentGroups = False, returnHasAssignmentsWithSubjects = False, returnHasCalculationGroupCourse = False, returnHasCategoriesInDistrict = False, returnHasClosedOrCompletedSectionGradingScaleGroup = False, returnHasCompleted = False, returnHasCompletedForFilter = False, returnHasGradeMarksInEntity = False, returnHasGradingPeriodGradeBuckets = False, returnHasGradingScales = False, returnHasIncompleteClosedGradeChangeRequests = False, returnHasNotStarted = False, returnHasNotStartedForFilter = False, returnHasPreviousYearSettings = False, returnHasStandardsCheckSectionLengthGradingPeriodSet = False, returnHasStudentSections = False, returnHasSubjectsCheckSectionLengthGradingPeriodSet = False, returnHasValidGradebookSetup = False, returnHasValidStandardsSetup = False, returnHasValidSubjectsSetup = False, returnHomeroomID = False, returnInPastYear = False, returnIsActive = False, returnIsActiveOverride = False, returnIsAdministeredForTSA = False, returnIsAHistoricRecord = False, returnIsBilingual = False, returnIsCreditRecovery = False, returnIsInProgress = False, returnIsInProgressForFilter = False, returnIsOffered = False, returnIsOfferedToAnotherEntity = False, returnIsSelfPaced = False, returnIsSelfPacedAndActive = False, returnIsTSAProficient = False, returnLanguageID = False, returnLockSectionFromSectionScheduler = False, returnLockSectionLengthFromSectionScheduler = False, returnMaximumStudentCount = False, returnMaximumStudentCountEntity = False, returnMaximumStudentCountEntityForFilter = False, returnMaximumStudentCountForEntityOfCourse = False, returnMaximumStudentCountForViewingEntity = False, returnMaximumStudentCountOffered = False, returnMaximumStudentCountOfferedForFilter = False, returnMaximumStudentCountOfferedToSpecifiedEntity = False, returnMeetIDCurrentStoredPrimary = False, returnMeetSummaryIDCurrentStoredPrimary = False, returnMinimumStudentCount = False, returnMissingAssignmentCount = False, returnMissingAssignmentCountForTerm = False, returnMissingAssignmentCountForTermCalculated = False, returnModifiedTime = False, returnNoCountAssignmentCountForTerm = False, returnNoCountAssignmentCountForTermCalculated = False, returnNonGradedAssignmentCountForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnNonTransferCourseEnrollmentCountFemales = False, returnNonTransferCourseEnrollmentCountFemalesEntity = False, returnNonTransferCourseEnrollmentCountFemalesEntityFirstDay = False, returnNonTransferCourseEnrollmentCountFemalesEntitySpecifiedDate = False, returnNonTransferCourseEnrollmentCountFemalesEntityToday = False, returnNonTransferCourseEnrollmentCountFemalesFirstDay = False, returnNonTransferCourseEnrollmentCountFemalesSpecifiedDate = False, returnNonTransferCourseEnrollmentCountFemalesToday = False, returnNonTransferCourseEnrollmentCountMales = False, returnNonTransferCourseEnrollmentCountMalesEntity = False, returnNonTransferCourseEnrollmentCountMalesEntityFirstDay = False, returnNonTransferCourseEnrollmentCountMalesEntitySpecifiedDate = False, returnNonTransferCourseEnrollmentCountMalesEntityToday = False, returnNonTransferCourseEnrollmentCountMalesFirstDay = False, returnNonTransferCourseEnrollmentCountMalesSpecifiedDate = False, returnNonTransferCourseEnrollmentCountMalesToday = False, returnNonTransferCourseStudentEnrollmentCount = False, returnNonTransferCourseStudentEnrollmentCountEntity = False, returnNonTransferCourseStudentEnrollmentCountEntityFirstDay = False, returnNonTransferCourseStudentEnrollmentCountEntitySpecifiedDate = False, returnNonTransferCourseStudentEnrollmentCountEntityToday = False, returnNonTransferCourseStudentEnrollmentCountFirstDay = False, returnNonTransferCourseStudentEnrollmentCountSpecifiedDate = False, returnNonTransferCourseStudentEnrollmentCountToday = False, returnNumberOfTransferStudentSections = False, returnNumberOfTransferStudentSectionsForFilter = False, returnOffenseCount = False, returnOffenseCountYTD = False, returnOptimalStudentCount = False, returnOtherAbsencesForTerm = False, returnOtherAbsencesYTD = False, returnPeriodDaySummary = False, returnPreviousVersionOfFit = False, returnProgressStatusSpecifiedDate = False, returnProgressStatusToday = False, returnRecalculateGradebook = False, returnRecalculateGradebookAdmin = False, returnReservedSeatCount = False, returnSchedulingCategories = False, returnSchedulingTeams = False, returnSchoolYearID = False, returnScoreClarifierAssignmentCountForTerm = False, returnScoreClarifierAssignmentCountForTermCalculated = False, returnScoredAssignmentCount = False, returnScoredAssignmentRange0CurrentTerm = False, returnScoredAssignmentRange100to90CurrentTerm = False, returnScoredAssignmentRange49to1CurrentTerm = False, returnScoredAssignmentRange59to50CurrentTerm = False, returnScoredAssignmentRange69to60CurrentTerm = False, returnScoredAssignmentRange79to70CurrentTerm = False, returnScoredAssignmentRange89to80CurrentTerm = False, returnSeatsAvailable = False, returnSeatsAvailableEntity = False, returnSeatsAvailableEntityForFilter = False, returnSeatsAvailableForFilter = False, returnSectionEnrollmentTotalsForSectionLengthSubsetSummary = False, returnSectionEnrollmentTotalsForSectionLengthSubsetSummaryForEntity = False, returnSectionIDClonedFrom = False, returnSectionIDClonedTo = False, returnSectionIDHash = False, returnSectionLengthID = False, returnSectionLengthScheduledBySectionScheduler = False, returnSectionMNID = False, returnSelfPacedEndTime = False, returnSelfPacedEndTimeDate = False, returnSelfPacedEndTimeTime = False, returnSingleSex = False, returnSingleSexCode = False, returnSpecialEdPercentageLimit = False, returnSpecifiedPeriodDaySummary = False, returnStaffIDCurrentStoredPrimary = False, returnStaffMeetIDCurrentStoredPrimary = False, returnStateInstructionalMethodCodeMNID = False, returnStateSTARModeOfTeachingMNID = False, returnStudentAssignmentDataString = False, returnStudentCountForTerm = False, returnStudentEnrollment = False, returnStudentEnrollmentAsOfSpecifiedDate = False, returnStudentEnrollmentAsOfSpecifiedDateForFilter = False, returnStudentEnrollmentEntity = False, returnStudentEnrollmentEntityForFilter = False, returnStudentEnrollmentFemales = False, returnStudentEnrollmentFemalesAsOfSpecifiedDate = False, returnStudentEnrollmentFemalesAsOfSpecifiedDateForFilter = False, returnStudentEnrollmentFemalesEntity = False, returnStudentEnrollmentFemalesEntityForFilter = False, returnStudentEnrollmentFemalesForFilter = False, returnStudentEnrollmentForFilter = False, returnStudentEnrollmentMales = False, returnStudentEnrollmentMalesAsOfSpecifiedDate = False, returnStudentEnrollmentMalesAsOfSpecifiedDateForFilter = False, returnStudentEnrollmentMalesEntity = False, returnStudentEnrollmentMalesEntityForFilter = False, returnStudentEnrollmentMalesForFilter = False, returnStudentSectionSectionIDHash = False, returnTardiesForTerm = False, returnTardiesYTD = False, returnThisPeriodDaySummary = False, returnTotalEnrollmentCount = False, returnTotalEnrollmentCountEntity = False, returnTotalEnrollmentCountEntityForFilter = False, returnTotalEnrollmentCountForFilter = False, returnTotalMeetCount = False, returnTotalSeatsOfferedToOtherEntities = False, returnTransferCourseEnrollmentCountFemales = False, returnTransferCourseEnrollmentCountFemalesEntity = False, returnTransferCourseEnrollmentCountFemalesEntityFirstDay = False, returnTransferCourseEnrollmentCountFemalesEntitySpecifiedDate = False, returnTransferCourseEnrollmentCountFemalesEntityToday = False, returnTransferCourseEnrollmentCountFemalesFirstDay = False, returnTransferCourseEnrollmentCountFemalesSpecifiedDate = False, returnTransferCourseEnrollmentCountFemalesToday = False, returnTransferCourseEnrollmentCountMales = False, returnTransferCourseEnrollmentCountMalesEntity = False, returnTransferCourseEnrollmentCountMalesEntityFirstDay = False, returnTransferCourseEnrollmentCountMalesEntitySpecifiedDate = False, returnTransferCourseEnrollmentCountMalesEntityToday = False, returnTransferCourseEnrollmentCountMalesFirstDay = False, returnTransferCourseEnrollmentCountMalesSpecifiedDate = False, returnTransferCourseEnrollmentCountMalesToday = False, returnTransferCourseStudentEnrollmentCount = False, returnTransferCourseStudentEnrollmentCountEntity = False, returnTransferCourseStudentEnrollmentCountEntityFirstDay = False, returnTransferCourseStudentEnrollmentCountEntitySpecifiedDate = False, returnTransferCourseStudentEnrollmentCountEntityToday = False, returnTransferCourseStudentEnrollmentCountFirstDay = False, returnTransferCourseStudentEnrollmentCountSpecifiedDate = False, returnTransferCourseStudentEnrollmentCountToday = False, returnUnexcusedAbsencesForTerm = False, returnUnexcusedAbsencesYTD = False, returnUnscoredAssignmentCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, returnWebsite = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/Section/" + str(SectionID), verb = "get", return_params_list = return_params_list)

def modifySection(SectionID, EntityID = 1, setAllowCECE = None, setAllowStudentsWithoutCategoryToBeAssigned = None, setBellScheduleGroupID = None, setCalendarIDMCCCOverride = None, setCode = None, setCourseID = None, setCurrentlyRecalculating = None, setDisplayPeriodIDCurrentStoredPrimary = None, setDueDateOfLastAssignmentScored = None, setEdFiEducationalEnvironmentID = None, setEntityID = None, setExcludeFromStudentSectionLink = None, setFit = None, setHomeroomID = None, setIsActive = None, setIsAdministeredForTSA = None, setIsBilingual = None, setIsCreditRecovery = None, setIsSelfPaced = None, setIsTSAProficient = None, setLanguageID = None, setLockSectionFromSectionScheduler = None, setLockSectionLengthFromSectionScheduler = None, setMaximumStudentCount = None, setMeetIDCurrentStoredPrimary = None, setMeetSummaryIDCurrentStoredPrimary = None, setMinimumStudentCount = None, setNonGradedAssignmentCountNoStudentAssignmentsForTerm = None, setOptimalStudentCount = None, setPreviousVersionOfFit = None, setProgressStatusSpecifiedDate = None, setProgressStatusToday = None, setRecalculateGradebook = None, setRecalculateGradebookAdmin = None, setReservedSeatCount = None, setSchedulingCategories = None, setSchedulingTeams = None, setSchoolYearID = None, setSectionIDClonedFrom = None, setSectionLengthID = None, setSectionLengthScheduledBySectionScheduler = None, setSelfPacedEndTime = None, setSelfPacedEndTimeDate = None, setSelfPacedEndTimeTime = None, setSingleSex = None, setSingleSexCode = None, setSpecialEdPercentageLimit = None, setStaffIDCurrentStoredPrimary = None, setStaffMeetIDCurrentStoredPrimary = None, setStateInstructionalMethodCodeMNID = None, setStateSTARModeOfTeachingMNID = None, setWebsite = None, setRelationships = None, returnSectionID = True, returnAllowCECE = False, returnAllowStudentsWithoutCategoryToBeAssigned = False, returnAssignmentCount = False, returnAssignmentCountForTerm = False, returnAssignmentCountForTermCalculated = False, returnAssignmentCountYTD = False, returnAssignmentCountYTDCalculated = False, returnAssignmentDataString = False, returnAssignmentsHaveBeenCreated = False, returnBellScheduleGroupID = False, returnCalculatedBellScheduleGroupID = False, returnCalculatedStudentEnrollmentCount = False, returnCalculatedStudentEnrollmentCountEntity = False, returnCalculatedStudentEnrollmentCountEntityFirstDay = False, returnCalculatedStudentEnrollmentCountEntitySpecifiedDate = False, returnCalculatedStudentEnrollmentCountEntityToday = False, returnCalculatedStudentEnrollmentCountFirstDay = False, returnCalculatedStudentEnrollmentCountSpecifiedDate = False, returnCalculatedStudentEnrollmentCountToday = False, returnCalendarIDMCCCOverride = False, returnCanAddStudentSection = False, returnCanBeOffered = False, returnCode = False, returnCourseCodeSectionCode = False, returnCourseCodeSectionCodeCourseDescription = False, returnCourseDescriptionCodeSectionCode = False, returnCourseID = False, returnCourseIDHash = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnCurrentEnrollmentEntity = False, returnCurrentEnrollmentEntityForFilter = False, returnCurrentEnrollmentForFilter = False, returnCurrentGradingPeriod = False, returnCurrentlyRecalculating = False, returnDisplayForTeachers = False, returnDisplayPeriodIDCurrentStoredPrimary = False, returnDueDateOfLastAssignmentScored = False, returnEdFiEducationalEnvironmentID = False, returnEffectiveTeacherFirstLastName = False, returnEffectiveTeacherLastFirstName = False, returnEntityCodeTeacherNumber = False, returnEntityID = False, returnExcludeFromStudentSectionLink = False, returnExcusedAbsencesForTerm = False, returnExcusedAbsencesYTD = False, returnFit = False, returnFutureAssignmentCountForTerm = False, returnFutureAssignmentCountForTermCalculated = False, returnGradebookCanHaveSettingsCopiedFromPreviousYear = False, returnGradedAssignmentCountForTerm = False, returnGradedAssignmentCountForTermCalculated = False, returnHasAssignments = False, returnHasAssignmentsWithAcademicStandards = False, returnHasAssignmentsWithStudentGroups = False, returnHasAssignmentsWithSubjects = False, returnHasCalculationGroupCourse = False, returnHasCategoriesInDistrict = False, returnHasClosedOrCompletedSectionGradingScaleGroup = False, returnHasCompleted = False, returnHasCompletedForFilter = False, returnHasGradeMarksInEntity = False, returnHasGradingPeriodGradeBuckets = False, returnHasGradingScales = False, returnHasIncompleteClosedGradeChangeRequests = False, returnHasNotStarted = False, returnHasNotStartedForFilter = False, returnHasPreviousYearSettings = False, returnHasStandardsCheckSectionLengthGradingPeriodSet = False, returnHasStudentSections = False, returnHasSubjectsCheckSectionLengthGradingPeriodSet = False, returnHasValidGradebookSetup = False, returnHasValidStandardsSetup = False, returnHasValidSubjectsSetup = False, returnHomeroomID = False, returnInPastYear = False, returnIsActive = False, returnIsActiveOverride = False, returnIsAdministeredForTSA = False, returnIsAHistoricRecord = False, returnIsBilingual = False, returnIsCreditRecovery = False, returnIsInProgress = False, returnIsInProgressForFilter = False, returnIsOffered = False, returnIsOfferedToAnotherEntity = False, returnIsSelfPaced = False, returnIsSelfPacedAndActive = False, returnIsTSAProficient = False, returnLanguageID = False, returnLockSectionFromSectionScheduler = False, returnLockSectionLengthFromSectionScheduler = False, returnMaximumStudentCount = False, returnMaximumStudentCountEntity = False, returnMaximumStudentCountEntityForFilter = False, returnMaximumStudentCountForEntityOfCourse = False, returnMaximumStudentCountForViewingEntity = False, returnMaximumStudentCountOffered = False, returnMaximumStudentCountOfferedForFilter = False, returnMaximumStudentCountOfferedToSpecifiedEntity = False, returnMeetIDCurrentStoredPrimary = False, returnMeetSummaryIDCurrentStoredPrimary = False, returnMinimumStudentCount = False, returnMissingAssignmentCount = False, returnMissingAssignmentCountForTerm = False, returnMissingAssignmentCountForTermCalculated = False, returnModifiedTime = False, returnNoCountAssignmentCountForTerm = False, returnNoCountAssignmentCountForTermCalculated = False, returnNonGradedAssignmentCountForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnNonTransferCourseEnrollmentCountFemales = False, returnNonTransferCourseEnrollmentCountFemalesEntity = False, returnNonTransferCourseEnrollmentCountFemalesEntityFirstDay = False, returnNonTransferCourseEnrollmentCountFemalesEntitySpecifiedDate = False, returnNonTransferCourseEnrollmentCountFemalesEntityToday = False, returnNonTransferCourseEnrollmentCountFemalesFirstDay = False, returnNonTransferCourseEnrollmentCountFemalesSpecifiedDate = False, returnNonTransferCourseEnrollmentCountFemalesToday = False, returnNonTransferCourseEnrollmentCountMales = False, returnNonTransferCourseEnrollmentCountMalesEntity = False, returnNonTransferCourseEnrollmentCountMalesEntityFirstDay = False, returnNonTransferCourseEnrollmentCountMalesEntitySpecifiedDate = False, returnNonTransferCourseEnrollmentCountMalesEntityToday = False, returnNonTransferCourseEnrollmentCountMalesFirstDay = False, returnNonTransferCourseEnrollmentCountMalesSpecifiedDate = False, returnNonTransferCourseEnrollmentCountMalesToday = False, returnNonTransferCourseStudentEnrollmentCount = False, returnNonTransferCourseStudentEnrollmentCountEntity = False, returnNonTransferCourseStudentEnrollmentCountEntityFirstDay = False, returnNonTransferCourseStudentEnrollmentCountEntitySpecifiedDate = False, returnNonTransferCourseStudentEnrollmentCountEntityToday = False, returnNonTransferCourseStudentEnrollmentCountFirstDay = False, returnNonTransferCourseStudentEnrollmentCountSpecifiedDate = False, returnNonTransferCourseStudentEnrollmentCountToday = False, returnNumberOfTransferStudentSections = False, returnNumberOfTransferStudentSectionsForFilter = False, returnOffenseCount = False, returnOffenseCountYTD = False, returnOptimalStudentCount = False, returnOtherAbsencesForTerm = False, returnOtherAbsencesYTD = False, returnPeriodDaySummary = False, returnPreviousVersionOfFit = False, returnProgressStatusSpecifiedDate = False, returnProgressStatusToday = False, returnRecalculateGradebook = False, returnRecalculateGradebookAdmin = False, returnReservedSeatCount = False, returnSchedulingCategories = False, returnSchedulingTeams = False, returnSchoolYearID = False, returnScoreClarifierAssignmentCountForTerm = False, returnScoreClarifierAssignmentCountForTermCalculated = False, returnScoredAssignmentCount = False, returnScoredAssignmentRange0CurrentTerm = False, returnScoredAssignmentRange100to90CurrentTerm = False, returnScoredAssignmentRange49to1CurrentTerm = False, returnScoredAssignmentRange59to50CurrentTerm = False, returnScoredAssignmentRange69to60CurrentTerm = False, returnScoredAssignmentRange79to70CurrentTerm = False, returnScoredAssignmentRange89to80CurrentTerm = False, returnSeatsAvailable = False, returnSeatsAvailableEntity = False, returnSeatsAvailableEntityForFilter = False, returnSeatsAvailableForFilter = False, returnSectionEnrollmentTotalsForSectionLengthSubsetSummary = False, returnSectionEnrollmentTotalsForSectionLengthSubsetSummaryForEntity = False, returnSectionIDClonedFrom = False, returnSectionIDClonedTo = False, returnSectionIDHash = False, returnSectionLengthID = False, returnSectionLengthScheduledBySectionScheduler = False, returnSectionMNID = False, returnSelfPacedEndTime = False, returnSelfPacedEndTimeDate = False, returnSelfPacedEndTimeTime = False, returnSingleSex = False, returnSingleSexCode = False, returnSpecialEdPercentageLimit = False, returnSpecifiedPeriodDaySummary = False, returnStaffIDCurrentStoredPrimary = False, returnStaffMeetIDCurrentStoredPrimary = False, returnStateInstructionalMethodCodeMNID = False, returnStateSTARModeOfTeachingMNID = False, returnStudentAssignmentDataString = False, returnStudentCountForTerm = False, returnStudentEnrollment = False, returnStudentEnrollmentAsOfSpecifiedDate = False, returnStudentEnrollmentAsOfSpecifiedDateForFilter = False, returnStudentEnrollmentEntity = False, returnStudentEnrollmentEntityForFilter = False, returnStudentEnrollmentFemales = False, returnStudentEnrollmentFemalesAsOfSpecifiedDate = False, returnStudentEnrollmentFemalesAsOfSpecifiedDateForFilter = False, returnStudentEnrollmentFemalesEntity = False, returnStudentEnrollmentFemalesEntityForFilter = False, returnStudentEnrollmentFemalesForFilter = False, returnStudentEnrollmentForFilter = False, returnStudentEnrollmentMales = False, returnStudentEnrollmentMalesAsOfSpecifiedDate = False, returnStudentEnrollmentMalesAsOfSpecifiedDateForFilter = False, returnStudentEnrollmentMalesEntity = False, returnStudentEnrollmentMalesEntityForFilter = False, returnStudentEnrollmentMalesForFilter = False, returnStudentSectionSectionIDHash = False, returnTardiesForTerm = False, returnTardiesYTD = False, returnThisPeriodDaySummary = False, returnTotalEnrollmentCount = False, returnTotalEnrollmentCountEntity = False, returnTotalEnrollmentCountEntityForFilter = False, returnTotalEnrollmentCountForFilter = False, returnTotalMeetCount = False, returnTotalSeatsOfferedToOtherEntities = False, returnTransferCourseEnrollmentCountFemales = False, returnTransferCourseEnrollmentCountFemalesEntity = False, returnTransferCourseEnrollmentCountFemalesEntityFirstDay = False, returnTransferCourseEnrollmentCountFemalesEntitySpecifiedDate = False, returnTransferCourseEnrollmentCountFemalesEntityToday = False, returnTransferCourseEnrollmentCountFemalesFirstDay = False, returnTransferCourseEnrollmentCountFemalesSpecifiedDate = False, returnTransferCourseEnrollmentCountFemalesToday = False, returnTransferCourseEnrollmentCountMales = False, returnTransferCourseEnrollmentCountMalesEntity = False, returnTransferCourseEnrollmentCountMalesEntityFirstDay = False, returnTransferCourseEnrollmentCountMalesEntitySpecifiedDate = False, returnTransferCourseEnrollmentCountMalesEntityToday = False, returnTransferCourseEnrollmentCountMalesFirstDay = False, returnTransferCourseEnrollmentCountMalesSpecifiedDate = False, returnTransferCourseEnrollmentCountMalesToday = False, returnTransferCourseStudentEnrollmentCount = False, returnTransferCourseStudentEnrollmentCountEntity = False, returnTransferCourseStudentEnrollmentCountEntityFirstDay = False, returnTransferCourseStudentEnrollmentCountEntitySpecifiedDate = False, returnTransferCourseStudentEnrollmentCountEntityToday = False, returnTransferCourseStudentEnrollmentCountFirstDay = False, returnTransferCourseStudentEnrollmentCountSpecifiedDate = False, returnTransferCourseStudentEnrollmentCountToday = False, returnUnexcusedAbsencesForTerm = False, returnUnexcusedAbsencesYTD = False, returnUnscoredAssignmentCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, returnWebsite = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/Section/" + str(SectionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSection(EntityID = 1, setAllowCECE = None, setAllowStudentsWithoutCategoryToBeAssigned = None, setBellScheduleGroupID = None, setCalendarIDMCCCOverride = None, setCode = None, setCourseID = None, setCurrentlyRecalculating = None, setDisplayPeriodIDCurrentStoredPrimary = None, setDueDateOfLastAssignmentScored = None, setEdFiEducationalEnvironmentID = None, setEntityID = None, setExcludeFromStudentSectionLink = None, setFit = None, setHomeroomID = None, setIsActive = None, setIsAdministeredForTSA = None, setIsBilingual = None, setIsCreditRecovery = None, setIsSelfPaced = None, setIsTSAProficient = None, setLanguageID = None, setLockSectionFromSectionScheduler = None, setLockSectionLengthFromSectionScheduler = None, setMaximumStudentCount = None, setMeetIDCurrentStoredPrimary = None, setMeetSummaryIDCurrentStoredPrimary = None, setMinimumStudentCount = None, setNonGradedAssignmentCountNoStudentAssignmentsForTerm = None, setOptimalStudentCount = None, setPreviousVersionOfFit = None, setProgressStatusSpecifiedDate = None, setProgressStatusToday = None, setRecalculateGradebook = None, setRecalculateGradebookAdmin = None, setReservedSeatCount = None, setSchedulingCategories = None, setSchedulingTeams = None, setSchoolYearID = None, setSectionIDClonedFrom = None, setSectionLengthID = None, setSectionLengthScheduledBySectionScheduler = None, setSelfPacedEndTime = None, setSelfPacedEndTimeDate = None, setSelfPacedEndTimeTime = None, setSingleSex = None, setSingleSexCode = None, setSpecialEdPercentageLimit = None, setStaffIDCurrentStoredPrimary = None, setStaffMeetIDCurrentStoredPrimary = None, setStateInstructionalMethodCodeMNID = None, setStateSTARModeOfTeachingMNID = None, setWebsite = None, setRelationships = None, returnSectionID = True, returnAllowCECE = False, returnAllowStudentsWithoutCategoryToBeAssigned = False, returnAssignmentCount = False, returnAssignmentCountForTerm = False, returnAssignmentCountForTermCalculated = False, returnAssignmentCountYTD = False, returnAssignmentCountYTDCalculated = False, returnAssignmentDataString = False, returnAssignmentsHaveBeenCreated = False, returnBellScheduleGroupID = False, returnCalculatedBellScheduleGroupID = False, returnCalculatedStudentEnrollmentCount = False, returnCalculatedStudentEnrollmentCountEntity = False, returnCalculatedStudentEnrollmentCountEntityFirstDay = False, returnCalculatedStudentEnrollmentCountEntitySpecifiedDate = False, returnCalculatedStudentEnrollmentCountEntityToday = False, returnCalculatedStudentEnrollmentCountFirstDay = False, returnCalculatedStudentEnrollmentCountSpecifiedDate = False, returnCalculatedStudentEnrollmentCountToday = False, returnCalendarIDMCCCOverride = False, returnCanAddStudentSection = False, returnCanBeOffered = False, returnCode = False, returnCourseCodeSectionCode = False, returnCourseCodeSectionCodeCourseDescription = False, returnCourseDescriptionCodeSectionCode = False, returnCourseID = False, returnCourseIDHash = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnCurrentEnrollmentEntity = False, returnCurrentEnrollmentEntityForFilter = False, returnCurrentEnrollmentForFilter = False, returnCurrentGradingPeriod = False, returnCurrentlyRecalculating = False, returnDisplayForTeachers = False, returnDisplayPeriodIDCurrentStoredPrimary = False, returnDueDateOfLastAssignmentScored = False, returnEdFiEducationalEnvironmentID = False, returnEffectiveTeacherFirstLastName = False, returnEffectiveTeacherLastFirstName = False, returnEntityCodeTeacherNumber = False, returnEntityID = False, returnExcludeFromStudentSectionLink = False, returnExcusedAbsencesForTerm = False, returnExcusedAbsencesYTD = False, returnFit = False, returnFutureAssignmentCountForTerm = False, returnFutureAssignmentCountForTermCalculated = False, returnGradebookCanHaveSettingsCopiedFromPreviousYear = False, returnGradedAssignmentCountForTerm = False, returnGradedAssignmentCountForTermCalculated = False, returnHasAssignments = False, returnHasAssignmentsWithAcademicStandards = False, returnHasAssignmentsWithStudentGroups = False, returnHasAssignmentsWithSubjects = False, returnHasCalculationGroupCourse = False, returnHasCategoriesInDistrict = False, returnHasClosedOrCompletedSectionGradingScaleGroup = False, returnHasCompleted = False, returnHasCompletedForFilter = False, returnHasGradeMarksInEntity = False, returnHasGradingPeriodGradeBuckets = False, returnHasGradingScales = False, returnHasIncompleteClosedGradeChangeRequests = False, returnHasNotStarted = False, returnHasNotStartedForFilter = False, returnHasPreviousYearSettings = False, returnHasStandardsCheckSectionLengthGradingPeriodSet = False, returnHasStudentSections = False, returnHasSubjectsCheckSectionLengthGradingPeriodSet = False, returnHasValidGradebookSetup = False, returnHasValidStandardsSetup = False, returnHasValidSubjectsSetup = False, returnHomeroomID = False, returnInPastYear = False, returnIsActive = False, returnIsActiveOverride = False, returnIsAdministeredForTSA = False, returnIsAHistoricRecord = False, returnIsBilingual = False, returnIsCreditRecovery = False, returnIsInProgress = False, returnIsInProgressForFilter = False, returnIsOffered = False, returnIsOfferedToAnotherEntity = False, returnIsSelfPaced = False, returnIsSelfPacedAndActive = False, returnIsTSAProficient = False, returnLanguageID = False, returnLockSectionFromSectionScheduler = False, returnLockSectionLengthFromSectionScheduler = False, returnMaximumStudentCount = False, returnMaximumStudentCountEntity = False, returnMaximumStudentCountEntityForFilter = False, returnMaximumStudentCountForEntityOfCourse = False, returnMaximumStudentCountForViewingEntity = False, returnMaximumStudentCountOffered = False, returnMaximumStudentCountOfferedForFilter = False, returnMaximumStudentCountOfferedToSpecifiedEntity = False, returnMeetIDCurrentStoredPrimary = False, returnMeetSummaryIDCurrentStoredPrimary = False, returnMinimumStudentCount = False, returnMissingAssignmentCount = False, returnMissingAssignmentCountForTerm = False, returnMissingAssignmentCountForTermCalculated = False, returnModifiedTime = False, returnNoCountAssignmentCountForTerm = False, returnNoCountAssignmentCountForTermCalculated = False, returnNonGradedAssignmentCountForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnNonTransferCourseEnrollmentCountFemales = False, returnNonTransferCourseEnrollmentCountFemalesEntity = False, returnNonTransferCourseEnrollmentCountFemalesEntityFirstDay = False, returnNonTransferCourseEnrollmentCountFemalesEntitySpecifiedDate = False, returnNonTransferCourseEnrollmentCountFemalesEntityToday = False, returnNonTransferCourseEnrollmentCountFemalesFirstDay = False, returnNonTransferCourseEnrollmentCountFemalesSpecifiedDate = False, returnNonTransferCourseEnrollmentCountFemalesToday = False, returnNonTransferCourseEnrollmentCountMales = False, returnNonTransferCourseEnrollmentCountMalesEntity = False, returnNonTransferCourseEnrollmentCountMalesEntityFirstDay = False, returnNonTransferCourseEnrollmentCountMalesEntitySpecifiedDate = False, returnNonTransferCourseEnrollmentCountMalesEntityToday = False, returnNonTransferCourseEnrollmentCountMalesFirstDay = False, returnNonTransferCourseEnrollmentCountMalesSpecifiedDate = False, returnNonTransferCourseEnrollmentCountMalesToday = False, returnNonTransferCourseStudentEnrollmentCount = False, returnNonTransferCourseStudentEnrollmentCountEntity = False, returnNonTransferCourseStudentEnrollmentCountEntityFirstDay = False, returnNonTransferCourseStudentEnrollmentCountEntitySpecifiedDate = False, returnNonTransferCourseStudentEnrollmentCountEntityToday = False, returnNonTransferCourseStudentEnrollmentCountFirstDay = False, returnNonTransferCourseStudentEnrollmentCountSpecifiedDate = False, returnNonTransferCourseStudentEnrollmentCountToday = False, returnNumberOfTransferStudentSections = False, returnNumberOfTransferStudentSectionsForFilter = False, returnOffenseCount = False, returnOffenseCountYTD = False, returnOptimalStudentCount = False, returnOtherAbsencesForTerm = False, returnOtherAbsencesYTD = False, returnPeriodDaySummary = False, returnPreviousVersionOfFit = False, returnProgressStatusSpecifiedDate = False, returnProgressStatusToday = False, returnRecalculateGradebook = False, returnRecalculateGradebookAdmin = False, returnReservedSeatCount = False, returnSchedulingCategories = False, returnSchedulingTeams = False, returnSchoolYearID = False, returnScoreClarifierAssignmentCountForTerm = False, returnScoreClarifierAssignmentCountForTermCalculated = False, returnScoredAssignmentCount = False, returnScoredAssignmentRange0CurrentTerm = False, returnScoredAssignmentRange100to90CurrentTerm = False, returnScoredAssignmentRange49to1CurrentTerm = False, returnScoredAssignmentRange59to50CurrentTerm = False, returnScoredAssignmentRange69to60CurrentTerm = False, returnScoredAssignmentRange79to70CurrentTerm = False, returnScoredAssignmentRange89to80CurrentTerm = False, returnSeatsAvailable = False, returnSeatsAvailableEntity = False, returnSeatsAvailableEntityForFilter = False, returnSeatsAvailableForFilter = False, returnSectionEnrollmentTotalsForSectionLengthSubsetSummary = False, returnSectionEnrollmentTotalsForSectionLengthSubsetSummaryForEntity = False, returnSectionIDClonedFrom = False, returnSectionIDClonedTo = False, returnSectionIDHash = False, returnSectionLengthID = False, returnSectionLengthScheduledBySectionScheduler = False, returnSectionMNID = False, returnSelfPacedEndTime = False, returnSelfPacedEndTimeDate = False, returnSelfPacedEndTimeTime = False, returnSingleSex = False, returnSingleSexCode = False, returnSpecialEdPercentageLimit = False, returnSpecifiedPeriodDaySummary = False, returnStaffIDCurrentStoredPrimary = False, returnStaffMeetIDCurrentStoredPrimary = False, returnStateInstructionalMethodCodeMNID = False, returnStateSTARModeOfTeachingMNID = False, returnStudentAssignmentDataString = False, returnStudentCountForTerm = False, returnStudentEnrollment = False, returnStudentEnrollmentAsOfSpecifiedDate = False, returnStudentEnrollmentAsOfSpecifiedDateForFilter = False, returnStudentEnrollmentEntity = False, returnStudentEnrollmentEntityForFilter = False, returnStudentEnrollmentFemales = False, returnStudentEnrollmentFemalesAsOfSpecifiedDate = False, returnStudentEnrollmentFemalesAsOfSpecifiedDateForFilter = False, returnStudentEnrollmentFemalesEntity = False, returnStudentEnrollmentFemalesEntityForFilter = False, returnStudentEnrollmentFemalesForFilter = False, returnStudentEnrollmentForFilter = False, returnStudentEnrollmentMales = False, returnStudentEnrollmentMalesAsOfSpecifiedDate = False, returnStudentEnrollmentMalesAsOfSpecifiedDateForFilter = False, returnStudentEnrollmentMalesEntity = False, returnStudentEnrollmentMalesEntityForFilter = False, returnStudentEnrollmentMalesForFilter = False, returnStudentSectionSectionIDHash = False, returnTardiesForTerm = False, returnTardiesYTD = False, returnThisPeriodDaySummary = False, returnTotalEnrollmentCount = False, returnTotalEnrollmentCountEntity = False, returnTotalEnrollmentCountEntityForFilter = False, returnTotalEnrollmentCountForFilter = False, returnTotalMeetCount = False, returnTotalSeatsOfferedToOtherEntities = False, returnTransferCourseEnrollmentCountFemales = False, returnTransferCourseEnrollmentCountFemalesEntity = False, returnTransferCourseEnrollmentCountFemalesEntityFirstDay = False, returnTransferCourseEnrollmentCountFemalesEntitySpecifiedDate = False, returnTransferCourseEnrollmentCountFemalesEntityToday = False, returnTransferCourseEnrollmentCountFemalesFirstDay = False, returnTransferCourseEnrollmentCountFemalesSpecifiedDate = False, returnTransferCourseEnrollmentCountFemalesToday = False, returnTransferCourseEnrollmentCountMales = False, returnTransferCourseEnrollmentCountMalesEntity = False, returnTransferCourseEnrollmentCountMalesEntityFirstDay = False, returnTransferCourseEnrollmentCountMalesEntitySpecifiedDate = False, returnTransferCourseEnrollmentCountMalesEntityToday = False, returnTransferCourseEnrollmentCountMalesFirstDay = False, returnTransferCourseEnrollmentCountMalesSpecifiedDate = False, returnTransferCourseEnrollmentCountMalesToday = False, returnTransferCourseStudentEnrollmentCount = False, returnTransferCourseStudentEnrollmentCountEntity = False, returnTransferCourseStudentEnrollmentCountEntityFirstDay = False, returnTransferCourseStudentEnrollmentCountEntitySpecifiedDate = False, returnTransferCourseStudentEnrollmentCountEntityToday = False, returnTransferCourseStudentEnrollmentCountFirstDay = False, returnTransferCourseStudentEnrollmentCountSpecifiedDate = False, returnTransferCourseStudentEnrollmentCountToday = False, returnUnexcusedAbsencesForTerm = False, returnUnexcusedAbsencesYTD = False, returnUnscoredAssignmentCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, returnWebsite = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/Section/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSection(SectionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionSchedulerCourseConstraint(EntityID = 1, page = 1, pageSize = 100, returnSectionSchedulerCourseConstraintID = True, returnCourseID = False, returnCourseIDLinked = False, returnCreatedTime = False, returnCurrentCourseSection = False, returnCurrentCourseSectionCode = False, returnCurrentCourseTopSectionCount = False, returnIsActive = False, returnLinkedCourse = False, returnLinkedCourseSection = False, returnLinkedCourseSectionCode = False, returnLinkedCourseTopSectionCount = False, returnModifiedTime = False, returnRule = False, returnRuleCode = False, returnScheduleFirst = False, returnScheduleLinkedCourseFirst = False, returnSectionIDCurrentCourseSelected = False, returnSectionIDLinkedCourseSelected = False, returnSectionSchedulerCourseConstraintIDClonedFrom = False, returnSectionSchedulerCourseConstraintIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerCourseConstraint/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionSchedulerCourseConstraint(SectionSchedulerCourseConstraintID, EntityID = 1, returnSectionSchedulerCourseConstraintID = True, returnCourseID = False, returnCourseIDLinked = False, returnCreatedTime = False, returnCurrentCourseSection = False, returnCurrentCourseSectionCode = False, returnCurrentCourseTopSectionCount = False, returnIsActive = False, returnLinkedCourse = False, returnLinkedCourseSection = False, returnLinkedCourseSectionCode = False, returnLinkedCourseTopSectionCount = False, returnModifiedTime = False, returnRule = False, returnRuleCode = False, returnScheduleFirst = False, returnScheduleLinkedCourseFirst = False, returnSectionIDCurrentCourseSelected = False, returnSectionIDLinkedCourseSelected = False, returnSectionSchedulerCourseConstraintIDClonedFrom = False, returnSectionSchedulerCourseConstraintIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerCourseConstraint/" + str(SectionSchedulerCourseConstraintID), verb = "get", return_params_list = return_params_list)

def modifySectionSchedulerCourseConstraint(SectionSchedulerCourseConstraintID, EntityID = 1, setCourseID = None, setCourseIDLinked = None, setCurrentCourseSection = None, setCurrentCourseSectionCode = None, setCurrentCourseTopSectionCount = None, setIsActive = None, setLinkedCourse = None, setLinkedCourseSection = None, setLinkedCourseSectionCode = None, setLinkedCourseTopSectionCount = None, setRule = None, setRuleCode = None, setScheduleLinkedCourseFirst = None, setSectionIDCurrentCourseSelected = None, setSectionIDLinkedCourseSelected = None, setSectionSchedulerCourseConstraintIDClonedFrom = None, setRelationships = None, returnSectionSchedulerCourseConstraintID = True, returnCourseID = False, returnCourseIDLinked = False, returnCreatedTime = False, returnCurrentCourseSection = False, returnCurrentCourseSectionCode = False, returnCurrentCourseTopSectionCount = False, returnIsActive = False, returnLinkedCourse = False, returnLinkedCourseSection = False, returnLinkedCourseSectionCode = False, returnLinkedCourseTopSectionCount = False, returnModifiedTime = False, returnRule = False, returnRuleCode = False, returnScheduleFirst = False, returnScheduleLinkedCourseFirst = False, returnSectionIDCurrentCourseSelected = False, returnSectionIDLinkedCourseSelected = False, returnSectionSchedulerCourseConstraintIDClonedFrom = False, returnSectionSchedulerCourseConstraintIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerCourseConstraint/" + str(SectionSchedulerCourseConstraintID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionSchedulerCourseConstraint(EntityID = 1, setCourseID = None, setCourseIDLinked = None, setCurrentCourseSection = None, setCurrentCourseSectionCode = None, setCurrentCourseTopSectionCount = None, setIsActive = None, setLinkedCourse = None, setLinkedCourseSection = None, setLinkedCourseSectionCode = None, setLinkedCourseTopSectionCount = None, setRule = None, setRuleCode = None, setScheduleLinkedCourseFirst = None, setSectionIDCurrentCourseSelected = None, setSectionIDLinkedCourseSelected = None, setSectionSchedulerCourseConstraintIDClonedFrom = None, setRelationships = None, returnSectionSchedulerCourseConstraintID = True, returnCourseID = False, returnCourseIDLinked = False, returnCreatedTime = False, returnCurrentCourseSection = False, returnCurrentCourseSectionCode = False, returnCurrentCourseTopSectionCount = False, returnIsActive = False, returnLinkedCourse = False, returnLinkedCourseSection = False, returnLinkedCourseSectionCode = False, returnLinkedCourseTopSectionCount = False, returnModifiedTime = False, returnRule = False, returnRuleCode = False, returnScheduleFirst = False, returnScheduleLinkedCourseFirst = False, returnSectionIDCurrentCourseSelected = False, returnSectionIDLinkedCourseSelected = False, returnSectionSchedulerCourseConstraintIDClonedFrom = False, returnSectionSchedulerCourseConstraintIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerCourseConstraint/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionSchedulerCourseConstraint(SectionSchedulerCourseConstraintID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionSchedulerDayRotationForMeet(EntityID = 1, page = 1, pageSize = 100, returnSectionSchedulerDayRotationForMeetID = True, returnCreatedTime = False, returnDayRotationID = False, returnMeetID = False, returnModifiedTime = False, returnSectionSchedulerDayRotationForMeetClonedTo = False, returnSectionSchedulerDayRotationForMeetIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerDayRotationForMeet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionSchedulerDayRotationForMeet(SectionSchedulerDayRotationForMeetID, EntityID = 1, returnSectionSchedulerDayRotationForMeetID = True, returnCreatedTime = False, returnDayRotationID = False, returnMeetID = False, returnModifiedTime = False, returnSectionSchedulerDayRotationForMeetClonedTo = False, returnSectionSchedulerDayRotationForMeetIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerDayRotationForMeet/" + str(SectionSchedulerDayRotationForMeetID), verb = "get", return_params_list = return_params_list)

def modifySectionSchedulerDayRotationForMeet(SectionSchedulerDayRotationForMeetID, EntityID = 1, setDayRotationID = None, setMeetID = None, setSectionSchedulerDayRotationForMeetIDClonedFrom = None, setRelationships = None, returnSectionSchedulerDayRotationForMeetID = True, returnCreatedTime = False, returnDayRotationID = False, returnMeetID = False, returnModifiedTime = False, returnSectionSchedulerDayRotationForMeetClonedTo = False, returnSectionSchedulerDayRotationForMeetIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerDayRotationForMeet/" + str(SectionSchedulerDayRotationForMeetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionSchedulerDayRotationForMeet(EntityID = 1, setDayRotationID = None, setMeetID = None, setSectionSchedulerDayRotationForMeetIDClonedFrom = None, setRelationships = None, returnSectionSchedulerDayRotationForMeetID = True, returnCreatedTime = False, returnDayRotationID = False, returnMeetID = False, returnModifiedTime = False, returnSectionSchedulerDayRotationForMeetClonedTo = False, returnSectionSchedulerDayRotationForMeetIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerDayRotationForMeet/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionSchedulerDayRotationForMeet(SectionSchedulerDayRotationForMeetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionSchedulerDisplayPeriodExcludedForCourse(EntityID = 1, page = 1, pageSize = 100, returnSectionSchedulerDisplayPeriodExcludedForCourseID = True, returnCourseID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnSectionSchedulerDisplayPeriodExcludedForCourseIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerDisplayPeriodExcludedForCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionSchedulerDisplayPeriodExcludedForCourse(SectionSchedulerDisplayPeriodExcludedForCourseID, EntityID = 1, returnSectionSchedulerDisplayPeriodExcludedForCourseID = True, returnCourseID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnSectionSchedulerDisplayPeriodExcludedForCourseIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerDisplayPeriodExcludedForCourse/" + str(SectionSchedulerDisplayPeriodExcludedForCourseID), verb = "get", return_params_list = return_params_list)

def modifySectionSchedulerDisplayPeriodExcludedForCourse(SectionSchedulerDisplayPeriodExcludedForCourseID, EntityID = 1, setCourseID = None, setDisplayPeriodID = None, setSectionSchedulerDisplayPeriodExcludedForCourseIDClonedFrom = None, setRelationships = None, returnSectionSchedulerDisplayPeriodExcludedForCourseID = True, returnCourseID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnSectionSchedulerDisplayPeriodExcludedForCourseIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerDisplayPeriodExcludedForCourse/" + str(SectionSchedulerDisplayPeriodExcludedForCourseID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionSchedulerDisplayPeriodExcludedForCourse(EntityID = 1, setCourseID = None, setDisplayPeriodID = None, setSectionSchedulerDisplayPeriodExcludedForCourseIDClonedFrom = None, setRelationships = None, returnSectionSchedulerDisplayPeriodExcludedForCourseID = True, returnCourseID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnSectionSchedulerDisplayPeriodExcludedForCourseIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerDisplayPeriodExcludedForCourse/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionSchedulerDisplayPeriodExcludedForCourse(SectionSchedulerDisplayPeriodExcludedForCourseID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionSchedulerPattern(EntityID = 1, page = 1, pageSize = 100, returnSectionSchedulerPatternID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDayRotationCount = False, returnDayRotationSummary = False, returnDescription = False, returnEntityID = False, returnHasDayRotations = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionSchedulerPatternIDClonedFrom = False, returnSectionSchedulerPatternIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerPattern/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionSchedulerPattern(SectionSchedulerPatternID, EntityID = 1, returnSectionSchedulerPatternID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDayRotationCount = False, returnDayRotationSummary = False, returnDescription = False, returnEntityID = False, returnHasDayRotations = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionSchedulerPatternIDClonedFrom = False, returnSectionSchedulerPatternIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerPattern/" + str(SectionSchedulerPatternID), verb = "get", return_params_list = return_params_list)

def modifySectionSchedulerPattern(SectionSchedulerPatternID, EntityID = 1, setCode = None, setDayRotationSummary = None, setDescription = None, setEntityID = None, setSchoolYearID = None, setSectionSchedulerPatternIDClonedFrom = None, setRelationships = None, returnSectionSchedulerPatternID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDayRotationCount = False, returnDayRotationSummary = False, returnDescription = False, returnEntityID = False, returnHasDayRotations = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionSchedulerPatternIDClonedFrom = False, returnSectionSchedulerPatternIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerPattern/" + str(SectionSchedulerPatternID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionSchedulerPattern(EntityID = 1, setCode = None, setDayRotationSummary = None, setDescription = None, setEntityID = None, setSchoolYearID = None, setSectionSchedulerPatternIDClonedFrom = None, setRelationships = None, returnSectionSchedulerPatternID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDayRotationCount = False, returnDayRotationSummary = False, returnDescription = False, returnEntityID = False, returnHasDayRotations = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionSchedulerPatternIDClonedFrom = False, returnSectionSchedulerPatternIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerPattern/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionSchedulerPattern(SectionSchedulerPatternID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionSchedulerPatternDayRotation(EntityID = 1, page = 1, pageSize = 100, returnSectionSchedulerPatternDayRotationID = True, returnCreatedTime = False, returnDayRotationID = False, returnModifiedTime = False, returnSectionSchedulerPatternDayRotationClonedTo = False, returnSectionSchedulerPatternDayRotationIDClonedFrom = False, returnSectionSchedulerPatternID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerPatternDayRotation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionSchedulerPatternDayRotation(SectionSchedulerPatternDayRotationID, EntityID = 1, returnSectionSchedulerPatternDayRotationID = True, returnCreatedTime = False, returnDayRotationID = False, returnModifiedTime = False, returnSectionSchedulerPatternDayRotationClonedTo = False, returnSectionSchedulerPatternDayRotationIDClonedFrom = False, returnSectionSchedulerPatternID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerPatternDayRotation/" + str(SectionSchedulerPatternDayRotationID), verb = "get", return_params_list = return_params_list)

def modifySectionSchedulerPatternDayRotation(SectionSchedulerPatternDayRotationID, EntityID = 1, setDayRotationID = None, setSectionSchedulerPatternDayRotationIDClonedFrom = None, setSectionSchedulerPatternID = None, setRelationships = None, returnSectionSchedulerPatternDayRotationID = True, returnCreatedTime = False, returnDayRotationID = False, returnModifiedTime = False, returnSectionSchedulerPatternDayRotationClonedTo = False, returnSectionSchedulerPatternDayRotationIDClonedFrom = False, returnSectionSchedulerPatternID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerPatternDayRotation/" + str(SectionSchedulerPatternDayRotationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionSchedulerPatternDayRotation(EntityID = 1, setDayRotationID = None, setSectionSchedulerPatternDayRotationIDClonedFrom = None, setSectionSchedulerPatternID = None, setRelationships = None, returnSectionSchedulerPatternDayRotationID = True, returnCreatedTime = False, returnDayRotationID = False, returnModifiedTime = False, returnSectionSchedulerPatternDayRotationClonedTo = False, returnSectionSchedulerPatternDayRotationIDClonedFrom = False, returnSectionSchedulerPatternID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerPatternDayRotation/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionSchedulerPatternDayRotation(SectionSchedulerPatternDayRotationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionSchedulerPatternExcludedForMeetRequirement(EntityID = 1, page = 1, pageSize = 100, returnSectionSchedulerPatternExcludedForMeetRequirementID = True, returnCreatedTime = False, returnMeetRequirementID = False, returnModifiedTime = False, returnSectionSchedulerPatternExcludedForMeetRequirementIDClonedFrom = False, returnSectionSchedulerPatternID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerPatternExcludedForMeetRequirement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionSchedulerPatternExcludedForMeetRequirement(SectionSchedulerPatternExcludedForMeetRequirementID, EntityID = 1, returnSectionSchedulerPatternExcludedForMeetRequirementID = True, returnCreatedTime = False, returnMeetRequirementID = False, returnModifiedTime = False, returnSectionSchedulerPatternExcludedForMeetRequirementIDClonedFrom = False, returnSectionSchedulerPatternID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerPatternExcludedForMeetRequirement/" + str(SectionSchedulerPatternExcludedForMeetRequirementID), verb = "get", return_params_list = return_params_list)

def modifySectionSchedulerPatternExcludedForMeetRequirement(SectionSchedulerPatternExcludedForMeetRequirementID, EntityID = 1, setMeetRequirementID = None, setSectionSchedulerPatternExcludedForMeetRequirementIDClonedFrom = None, setSectionSchedulerPatternID = None, setRelationships = None, returnSectionSchedulerPatternExcludedForMeetRequirementID = True, returnCreatedTime = False, returnMeetRequirementID = False, returnModifiedTime = False, returnSectionSchedulerPatternExcludedForMeetRequirementIDClonedFrom = False, returnSectionSchedulerPatternID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerPatternExcludedForMeetRequirement/" + str(SectionSchedulerPatternExcludedForMeetRequirementID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionSchedulerPatternExcludedForMeetRequirement(EntityID = 1, setMeetRequirementID = None, setSectionSchedulerPatternExcludedForMeetRequirementIDClonedFrom = None, setSectionSchedulerPatternID = None, setRelationships = None, returnSectionSchedulerPatternExcludedForMeetRequirementID = True, returnCreatedTime = False, returnMeetRequirementID = False, returnModifiedTime = False, returnSectionSchedulerPatternExcludedForMeetRequirementIDClonedFrom = False, returnSectionSchedulerPatternID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerPatternExcludedForMeetRequirement/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionSchedulerPatternExcludedForMeetRequirement(SectionSchedulerPatternExcludedForMeetRequirementID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionSchedulerProposedMeet(EntityID = 1, page = 1, pageSize = 100, returnSectionSchedulerProposedMeetID = True, returnCreatedTime = False, returnDisplayPeriodRotationID = False, returnEndDate = False, returnMeetDisplayPeriodSummary = False, returnModifiedTime = False, returnNumberOfActualConflicts = False, returnNumberOfEstimatedConflicts = False, returnNumberOfProposedMeetCourseConflicts = False, returnNumberOfProposedMeetRoomAndStaffConflicts = False, returnNumberOfProposedMeetRoomConflicts = False, returnNumberOfProposedMeetStaffConflicts = False, returnPrimaryStaffMeetFullNameLFM = False, returnRank = False, returnRankValue = False, returnRoomID = False, returnSectionLengthID = False, returnSectionSchedulerRunAnalysisID = False, returnStartDate = False, returnSumTotalOfMaximumStudentCountForScheduledSections = False, returnSumTotalOfOptimalStudentCountForScheduledSections = False, returnTotalActualConflictsPointsEarned = False, returnTotalDisplayPeriodPointsEarned = False, returnTotalEstimatedConflictsPointsEarned = False, returnTotalRoomPointsEarned = False, returnTotalStaffPointsEarned = False, returnTotalSumOfMaximumStudentCountForScheduledSectionsPointsEarned = False, returnTotalSumOfOptimalStudentCountForScheduledSectionsPointsEarned = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerProposedMeet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionSchedulerProposedMeet(SectionSchedulerProposedMeetID, EntityID = 1, returnSectionSchedulerProposedMeetID = True, returnCreatedTime = False, returnDisplayPeriodRotationID = False, returnEndDate = False, returnMeetDisplayPeriodSummary = False, returnModifiedTime = False, returnNumberOfActualConflicts = False, returnNumberOfEstimatedConflicts = False, returnNumberOfProposedMeetCourseConflicts = False, returnNumberOfProposedMeetRoomAndStaffConflicts = False, returnNumberOfProposedMeetRoomConflicts = False, returnNumberOfProposedMeetStaffConflicts = False, returnPrimaryStaffMeetFullNameLFM = False, returnRank = False, returnRankValue = False, returnRoomID = False, returnSectionLengthID = False, returnSectionSchedulerRunAnalysisID = False, returnStartDate = False, returnSumTotalOfMaximumStudentCountForScheduledSections = False, returnSumTotalOfOptimalStudentCountForScheduledSections = False, returnTotalActualConflictsPointsEarned = False, returnTotalDisplayPeriodPointsEarned = False, returnTotalEstimatedConflictsPointsEarned = False, returnTotalRoomPointsEarned = False, returnTotalStaffPointsEarned = False, returnTotalSumOfMaximumStudentCountForScheduledSectionsPointsEarned = False, returnTotalSumOfOptimalStudentCountForScheduledSectionsPointsEarned = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerProposedMeet/" + str(SectionSchedulerProposedMeetID), verb = "get", return_params_list = return_params_list)

def modifySectionSchedulerProposedMeet(SectionSchedulerProposedMeetID, EntityID = 1, setDisplayPeriodRotationID = None, setEndDate = None, setMeetDisplayPeriodSummary = None, setNumberOfActualConflicts = None, setNumberOfEstimatedConflicts = None, setPrimaryStaffMeetFullNameLFM = None, setRank = None, setRankValue = None, setRoomID = None, setSectionLengthID = None, setSectionSchedulerRunAnalysisID = None, setStartDate = None, setSumTotalOfMaximumStudentCountForScheduledSections = None, setSumTotalOfOptimalStudentCountForScheduledSections = None, setTotalActualConflictsPointsEarned = None, setTotalDisplayPeriodPointsEarned = None, setTotalEstimatedConflictsPointsEarned = None, setTotalRoomPointsEarned = None, setTotalStaffPointsEarned = None, setTotalSumOfMaximumStudentCountForScheduledSectionsPointsEarned = None, setTotalSumOfOptimalStudentCountForScheduledSectionsPointsEarned = None, setRelationships = None, returnSectionSchedulerProposedMeetID = True, returnCreatedTime = False, returnDisplayPeriodRotationID = False, returnEndDate = False, returnMeetDisplayPeriodSummary = False, returnModifiedTime = False, returnNumberOfActualConflicts = False, returnNumberOfEstimatedConflicts = False, returnNumberOfProposedMeetCourseConflicts = False, returnNumberOfProposedMeetRoomAndStaffConflicts = False, returnNumberOfProposedMeetRoomConflicts = False, returnNumberOfProposedMeetStaffConflicts = False, returnPrimaryStaffMeetFullNameLFM = False, returnRank = False, returnRankValue = False, returnRoomID = False, returnSectionLengthID = False, returnSectionSchedulerRunAnalysisID = False, returnStartDate = False, returnSumTotalOfMaximumStudentCountForScheduledSections = False, returnSumTotalOfOptimalStudentCountForScheduledSections = False, returnTotalActualConflictsPointsEarned = False, returnTotalDisplayPeriodPointsEarned = False, returnTotalEstimatedConflictsPointsEarned = False, returnTotalRoomPointsEarned = False, returnTotalStaffPointsEarned = False, returnTotalSumOfMaximumStudentCountForScheduledSectionsPointsEarned = False, returnTotalSumOfOptimalStudentCountForScheduledSectionsPointsEarned = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerProposedMeet/" + str(SectionSchedulerProposedMeetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionSchedulerProposedMeet(EntityID = 1, setDisplayPeriodRotationID = None, setEndDate = None, setMeetDisplayPeriodSummary = None, setNumberOfActualConflicts = None, setNumberOfEstimatedConflicts = None, setPrimaryStaffMeetFullNameLFM = None, setRank = None, setRankValue = None, setRoomID = None, setSectionLengthID = None, setSectionSchedulerRunAnalysisID = None, setStartDate = None, setSumTotalOfMaximumStudentCountForScheduledSections = None, setSumTotalOfOptimalStudentCountForScheduledSections = None, setTotalActualConflictsPointsEarned = None, setTotalDisplayPeriodPointsEarned = None, setTotalEstimatedConflictsPointsEarned = None, setTotalRoomPointsEarned = None, setTotalStaffPointsEarned = None, setTotalSumOfMaximumStudentCountForScheduledSectionsPointsEarned = None, setTotalSumOfOptimalStudentCountForScheduledSectionsPointsEarned = None, setRelationships = None, returnSectionSchedulerProposedMeetID = True, returnCreatedTime = False, returnDisplayPeriodRotationID = False, returnEndDate = False, returnMeetDisplayPeriodSummary = False, returnModifiedTime = False, returnNumberOfActualConflicts = False, returnNumberOfEstimatedConflicts = False, returnNumberOfProposedMeetCourseConflicts = False, returnNumberOfProposedMeetRoomAndStaffConflicts = False, returnNumberOfProposedMeetRoomConflicts = False, returnNumberOfProposedMeetStaffConflicts = False, returnPrimaryStaffMeetFullNameLFM = False, returnRank = False, returnRankValue = False, returnRoomID = False, returnSectionLengthID = False, returnSectionSchedulerRunAnalysisID = False, returnStartDate = False, returnSumTotalOfMaximumStudentCountForScheduledSections = False, returnSumTotalOfOptimalStudentCountForScheduledSections = False, returnTotalActualConflictsPointsEarned = False, returnTotalDisplayPeriodPointsEarned = False, returnTotalEstimatedConflictsPointsEarned = False, returnTotalRoomPointsEarned = False, returnTotalStaffPointsEarned = False, returnTotalSumOfMaximumStudentCountForScheduledSectionsPointsEarned = False, returnTotalSumOfOptimalStudentCountForScheduledSectionsPointsEarned = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerProposedMeet/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionSchedulerProposedMeet(SectionSchedulerProposedMeetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionSchedulerProposedMeetConflict(EntityID = 1, page = 1, pageSize = 100, returnSectionSchedulerProposedMeetConflictID = True, returnConflictType = False, returnConflictTypeCode = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnName = False, returnNumberOfActualConflicts = False, returnNumberOfCommonRequests = False, returnNumberOfEstimatedConflicts = False, returnSectionSchedulerProposedMeetID = False, returnSeverity = False, returnSeverityCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerProposedMeetConflict/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionSchedulerProposedMeetConflict(SectionSchedulerProposedMeetConflictID, EntityID = 1, returnSectionSchedulerProposedMeetConflictID = True, returnConflictType = False, returnConflictTypeCode = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnName = False, returnNumberOfActualConflicts = False, returnNumberOfCommonRequests = False, returnNumberOfEstimatedConflicts = False, returnSectionSchedulerProposedMeetID = False, returnSeverity = False, returnSeverityCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerProposedMeetConflict/" + str(SectionSchedulerProposedMeetConflictID), verb = "get", return_params_list = return_params_list)

def modifySectionSchedulerProposedMeetConflict(SectionSchedulerProposedMeetConflictID, EntityID = 1, setConflictType = None, setConflictTypeCode = None, setCourseID = None, setDescription = None, setName = None, setNumberOfActualConflicts = None, setNumberOfCommonRequests = None, setNumberOfEstimatedConflicts = None, setSectionSchedulerProposedMeetID = None, setSeverity = None, setSeverityCode = None, setRelationships = None, returnSectionSchedulerProposedMeetConflictID = True, returnConflictType = False, returnConflictTypeCode = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnName = False, returnNumberOfActualConflicts = False, returnNumberOfCommonRequests = False, returnNumberOfEstimatedConflicts = False, returnSectionSchedulerProposedMeetID = False, returnSeverity = False, returnSeverityCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerProposedMeetConflict/" + str(SectionSchedulerProposedMeetConflictID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionSchedulerProposedMeetConflict(EntityID = 1, setConflictType = None, setConflictTypeCode = None, setCourseID = None, setDescription = None, setName = None, setNumberOfActualConflicts = None, setNumberOfCommonRequests = None, setNumberOfEstimatedConflicts = None, setSectionSchedulerProposedMeetID = None, setSeverity = None, setSeverityCode = None, setRelationships = None, returnSectionSchedulerProposedMeetConflictID = True, returnConflictType = False, returnConflictTypeCode = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnName = False, returnNumberOfActualConflicts = False, returnNumberOfCommonRequests = False, returnNumberOfEstimatedConflicts = False, returnSectionSchedulerProposedMeetID = False, returnSeverity = False, returnSeverityCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerProposedMeetConflict/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionSchedulerProposedMeetConflict(SectionSchedulerProposedMeetConflictID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionSchedulerProposedMeetDisplayPeriod(EntityID = 1, page = 1, pageSize = 100, returnSectionSchedulerProposedMeetDisplayPeriodID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnSectionSchedulerProposedMeetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerProposedMeetDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionSchedulerProposedMeetDisplayPeriod(SectionSchedulerProposedMeetDisplayPeriodID, EntityID = 1, returnSectionSchedulerProposedMeetDisplayPeriodID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnSectionSchedulerProposedMeetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerProposedMeetDisplayPeriod/" + str(SectionSchedulerProposedMeetDisplayPeriodID), verb = "get", return_params_list = return_params_list)

def modifySectionSchedulerProposedMeetDisplayPeriod(SectionSchedulerProposedMeetDisplayPeriodID, EntityID = 1, setDisplayPeriodID = None, setSectionSchedulerProposedMeetID = None, setRelationships = None, returnSectionSchedulerProposedMeetDisplayPeriodID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnSectionSchedulerProposedMeetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerProposedMeetDisplayPeriod/" + str(SectionSchedulerProposedMeetDisplayPeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionSchedulerProposedMeetDisplayPeriod(EntityID = 1, setDisplayPeriodID = None, setSectionSchedulerProposedMeetID = None, setRelationships = None, returnSectionSchedulerProposedMeetDisplayPeriodID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnSectionSchedulerProposedMeetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerProposedMeetDisplayPeriod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionSchedulerProposedMeetDisplayPeriod(SectionSchedulerProposedMeetDisplayPeriodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionSchedulerProposedStaffMeet(EntityID = 1, page = 1, pageSize = 100, returnSectionSchedulerProposedStaffMeetID = True, returnCreatedTime = False, returnEffectiveEndDate = False, returnEffectiveStartDate = False, returnIsPrimary = False, returnModifiedTime = False, returnSectionSchedulerProposedMeetID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerProposedStaffMeet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionSchedulerProposedStaffMeet(SectionSchedulerProposedStaffMeetID, EntityID = 1, returnSectionSchedulerProposedStaffMeetID = True, returnCreatedTime = False, returnEffectiveEndDate = False, returnEffectiveStartDate = False, returnIsPrimary = False, returnModifiedTime = False, returnSectionSchedulerProposedMeetID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerProposedStaffMeet/" + str(SectionSchedulerProposedStaffMeetID), verb = "get", return_params_list = return_params_list)

def modifySectionSchedulerProposedStaffMeet(SectionSchedulerProposedStaffMeetID, EntityID = 1, setEffectiveEndDate = None, setEffectiveStartDate = None, setIsPrimary = None, setSectionSchedulerProposedMeetID = None, setStaffID = None, setRelationships = None, returnSectionSchedulerProposedStaffMeetID = True, returnCreatedTime = False, returnEffectiveEndDate = False, returnEffectiveStartDate = False, returnIsPrimary = False, returnModifiedTime = False, returnSectionSchedulerProposedMeetID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerProposedStaffMeet/" + str(SectionSchedulerProposedStaffMeetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionSchedulerProposedStaffMeet(EntityID = 1, setEffectiveEndDate = None, setEffectiveStartDate = None, setIsPrimary = None, setSectionSchedulerProposedMeetID = None, setStaffID = None, setRelationships = None, returnSectionSchedulerProposedStaffMeetID = True, returnCreatedTime = False, returnEffectiveEndDate = False, returnEffectiveStartDate = False, returnIsPrimary = False, returnModifiedTime = False, returnSectionSchedulerProposedMeetID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerProposedStaffMeet/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionSchedulerProposedStaffMeet(SectionSchedulerProposedStaffMeetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionSchedulerRoomTypeForCourse(EntityID = 1, page = 1, pageSize = 100, returnSectionSchedulerRoomTypeForCourseID = True, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnRoomTypeID = False, returnSectionSchedulerRoomTypeForCourseIDClonedFrom = False, returnSectionSchedulerRoomTypeForCourseIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerRoomTypeForCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionSchedulerRoomTypeForCourse(SectionSchedulerRoomTypeForCourseID, EntityID = 1, returnSectionSchedulerRoomTypeForCourseID = True, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnRoomTypeID = False, returnSectionSchedulerRoomTypeForCourseIDClonedFrom = False, returnSectionSchedulerRoomTypeForCourseIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerRoomTypeForCourse/" + str(SectionSchedulerRoomTypeForCourseID), verb = "get", return_params_list = return_params_list)

def modifySectionSchedulerRoomTypeForCourse(SectionSchedulerRoomTypeForCourseID, EntityID = 1, setCourseID = None, setRoomTypeID = None, setSectionSchedulerRoomTypeForCourseIDClonedFrom = None, setRelationships = None, returnSectionSchedulerRoomTypeForCourseID = True, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnRoomTypeID = False, returnSectionSchedulerRoomTypeForCourseIDClonedFrom = False, returnSectionSchedulerRoomTypeForCourseIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerRoomTypeForCourse/" + str(SectionSchedulerRoomTypeForCourseID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionSchedulerRoomTypeForCourse(EntityID = 1, setCourseID = None, setRoomTypeID = None, setSectionSchedulerRoomTypeForCourseIDClonedFrom = None, setRelationships = None, returnSectionSchedulerRoomTypeForCourseID = True, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnRoomTypeID = False, returnSectionSchedulerRoomTypeForCourseIDClonedFrom = False, returnSectionSchedulerRoomTypeForCourseIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerRoomTypeForCourse/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionSchedulerRoomTypeForCourse(SectionSchedulerRoomTypeForCourseID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionSchedulerRunAnalysis(EntityID = 1, page = 1, pageSize = 100, returnSectionSchedulerRunAnalysisID = True, returnAcceptedMeetReverted = False, returnAnalysisDuration = False, returnAnalysisMethod = False, returnAnalysisMethodCode = False, returnAnalyzeDayRotations = False, returnAnalyzeMeetDisplayPeriods = False, returnAnalyzeRoom = False, returnAnalyzeSectionLength = False, returnAnalyzeStaffMeets = False, returnCountOfSectionSchedulerProposedMeetRecords = False, returnCreatedTime = False, returnEndTimeAnalysis = False, returnEntityID = False, returnExcludeMeetsPreviouslyScheduled = False, returnMeetID = False, returnModifiedTime = False, returnPageStateID = False, returnRunReason = False, returnSchoolYearID = False, returnSectionSchedulerProposedMeetIDAccepted = False, returnStartTimeAnalysis = False, returnTotalActualConflictsPointsPossible = False, returnTotalDisplayPeriodPointsPossible = False, returnTotalEstimatedConflictsPointsPossible = False, returnTotalRoomPointsPossible = False, returnTotalStaffPointsPossible = False, returnTotalSumOfMaximumStudentCountForScheduledSectionsPointsPossible = False, returnTotalSumOfOptimalStudentCountForScheduledSectionsPointsPossible = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDPerformer = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerRunAnalysis/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionSchedulerRunAnalysis(SectionSchedulerRunAnalysisID, EntityID = 1, returnSectionSchedulerRunAnalysisID = True, returnAcceptedMeetReverted = False, returnAnalysisDuration = False, returnAnalysisMethod = False, returnAnalysisMethodCode = False, returnAnalyzeDayRotations = False, returnAnalyzeMeetDisplayPeriods = False, returnAnalyzeRoom = False, returnAnalyzeSectionLength = False, returnAnalyzeStaffMeets = False, returnCountOfSectionSchedulerProposedMeetRecords = False, returnCreatedTime = False, returnEndTimeAnalysis = False, returnEntityID = False, returnExcludeMeetsPreviouslyScheduled = False, returnMeetID = False, returnModifiedTime = False, returnPageStateID = False, returnRunReason = False, returnSchoolYearID = False, returnSectionSchedulerProposedMeetIDAccepted = False, returnStartTimeAnalysis = False, returnTotalActualConflictsPointsPossible = False, returnTotalDisplayPeriodPointsPossible = False, returnTotalEstimatedConflictsPointsPossible = False, returnTotalRoomPointsPossible = False, returnTotalStaffPointsPossible = False, returnTotalSumOfMaximumStudentCountForScheduledSectionsPointsPossible = False, returnTotalSumOfOptimalStudentCountForScheduledSectionsPointsPossible = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDPerformer = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerRunAnalysis/" + str(SectionSchedulerRunAnalysisID), verb = "get", return_params_list = return_params_list)

def modifySectionSchedulerRunAnalysis(SectionSchedulerRunAnalysisID, EntityID = 1, setAcceptedMeetReverted = None, setAnalysisMethod = None, setAnalysisMethodCode = None, setAnalyzeDayRotations = None, setAnalyzeMeetDisplayPeriods = None, setAnalyzeRoom = None, setAnalyzeSectionLength = None, setAnalyzeStaffMeets = None, setEndTimeAnalysis = None, setEntityID = None, setExcludeMeetsPreviouslyScheduled = None, setMeetID = None, setPageStateID = None, setRunReason = None, setSchoolYearID = None, setSectionSchedulerProposedMeetIDAccepted = None, setStartTimeAnalysis = None, setTotalActualConflictsPointsPossible = None, setTotalDisplayPeriodPointsPossible = None, setTotalEstimatedConflictsPointsPossible = None, setTotalRoomPointsPossible = None, setTotalStaffPointsPossible = None, setTotalSumOfMaximumStudentCountForScheduledSectionsPointsPossible = None, setTotalSumOfOptimalStudentCountForScheduledSectionsPointsPossible = None, setUserIDPerformer = None, setRelationships = None, returnSectionSchedulerRunAnalysisID = True, returnAcceptedMeetReverted = False, returnAnalysisDuration = False, returnAnalysisMethod = False, returnAnalysisMethodCode = False, returnAnalyzeDayRotations = False, returnAnalyzeMeetDisplayPeriods = False, returnAnalyzeRoom = False, returnAnalyzeSectionLength = False, returnAnalyzeStaffMeets = False, returnCountOfSectionSchedulerProposedMeetRecords = False, returnCreatedTime = False, returnEndTimeAnalysis = False, returnEntityID = False, returnExcludeMeetsPreviouslyScheduled = False, returnMeetID = False, returnModifiedTime = False, returnPageStateID = False, returnRunReason = False, returnSchoolYearID = False, returnSectionSchedulerProposedMeetIDAccepted = False, returnStartTimeAnalysis = False, returnTotalActualConflictsPointsPossible = False, returnTotalDisplayPeriodPointsPossible = False, returnTotalEstimatedConflictsPointsPossible = False, returnTotalRoomPointsPossible = False, returnTotalStaffPointsPossible = False, returnTotalSumOfMaximumStudentCountForScheduledSectionsPointsPossible = False, returnTotalSumOfOptimalStudentCountForScheduledSectionsPointsPossible = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDPerformer = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerRunAnalysis/" + str(SectionSchedulerRunAnalysisID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionSchedulerRunAnalysis(EntityID = 1, setAcceptedMeetReverted = None, setAnalysisMethod = None, setAnalysisMethodCode = None, setAnalyzeDayRotations = None, setAnalyzeMeetDisplayPeriods = None, setAnalyzeRoom = None, setAnalyzeSectionLength = None, setAnalyzeStaffMeets = None, setEndTimeAnalysis = None, setEntityID = None, setExcludeMeetsPreviouslyScheduled = None, setMeetID = None, setPageStateID = None, setRunReason = None, setSchoolYearID = None, setSectionSchedulerProposedMeetIDAccepted = None, setStartTimeAnalysis = None, setTotalActualConflictsPointsPossible = None, setTotalDisplayPeriodPointsPossible = None, setTotalEstimatedConflictsPointsPossible = None, setTotalRoomPointsPossible = None, setTotalStaffPointsPossible = None, setTotalSumOfMaximumStudentCountForScheduledSectionsPointsPossible = None, setTotalSumOfOptimalStudentCountForScheduledSectionsPointsPossible = None, setUserIDPerformer = None, setRelationships = None, returnSectionSchedulerRunAnalysisID = True, returnAcceptedMeetReverted = False, returnAnalysisDuration = False, returnAnalysisMethod = False, returnAnalysisMethodCode = False, returnAnalyzeDayRotations = False, returnAnalyzeMeetDisplayPeriods = False, returnAnalyzeRoom = False, returnAnalyzeSectionLength = False, returnAnalyzeStaffMeets = False, returnCountOfSectionSchedulerProposedMeetRecords = False, returnCreatedTime = False, returnEndTimeAnalysis = False, returnEntityID = False, returnExcludeMeetsPreviouslyScheduled = False, returnMeetID = False, returnModifiedTime = False, returnPageStateID = False, returnRunReason = False, returnSchoolYearID = False, returnSectionSchedulerProposedMeetIDAccepted = False, returnStartTimeAnalysis = False, returnTotalActualConflictsPointsPossible = False, returnTotalDisplayPeriodPointsPossible = False, returnTotalEstimatedConflictsPointsPossible = False, returnTotalRoomPointsPossible = False, returnTotalStaffPointsPossible = False, returnTotalSumOfMaximumStudentCountForScheduledSectionsPointsPossible = False, returnTotalSumOfOptimalStudentCountForScheduledSectionsPointsPossible = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDPerformer = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerRunAnalysis/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionSchedulerRunAnalysis(SectionSchedulerRunAnalysisID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionSchedulerStaffForCourse(EntityID = 1, page = 1, pageSize = 100, returnSectionSchedulerStaffForCourseID = True, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionSchedulerStaffForCourseIDClonedFrom = False, returnSectionSchedulerStaffForCourseIDClonedTo = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerStaffForCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionSchedulerStaffForCourse(SectionSchedulerStaffForCourseID, EntityID = 1, returnSectionSchedulerStaffForCourseID = True, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionSchedulerStaffForCourseIDClonedFrom = False, returnSectionSchedulerStaffForCourseIDClonedTo = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerStaffForCourse/" + str(SectionSchedulerStaffForCourseID), verb = "get", return_params_list = return_params_list)

def modifySectionSchedulerStaffForCourse(SectionSchedulerStaffForCourseID, EntityID = 1, setCourseID = None, setSectionSchedulerStaffForCourseIDClonedFrom = None, setStaffID = None, setRelationships = None, returnSectionSchedulerStaffForCourseID = True, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionSchedulerStaffForCourseIDClonedFrom = False, returnSectionSchedulerStaffForCourseIDClonedTo = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerStaffForCourse/" + str(SectionSchedulerStaffForCourseID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionSchedulerStaffForCourse(EntityID = 1, setCourseID = None, setSectionSchedulerStaffForCourseIDClonedFrom = None, setStaffID = None, setRelationships = None, returnSectionSchedulerStaffForCourseID = True, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionSchedulerStaffForCourseIDClonedFrom = False, returnSectionSchedulerStaffForCourseIDClonedTo = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulerStaffForCourse/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionSchedulerStaffForCourse(SectionSchedulerStaffForCourseID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionSchedulingCategory(EntityID = 1, page = 1, pageSize = 100, returnSectionSchedulingCategoryID = True, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingCategoryID = False, returnSectionID = False, returnSectionSchedulingCategoryIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulingCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionSchedulingCategory(SectionSchedulingCategoryID, EntityID = 1, returnSectionSchedulingCategoryID = True, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingCategoryID = False, returnSectionID = False, returnSectionSchedulingCategoryIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulingCategory/" + str(SectionSchedulingCategoryID), verb = "get", return_params_list = return_params_list)

def modifySectionSchedulingCategory(SectionSchedulingCategoryID, EntityID = 1, setSchedulingCategoryID = None, setSectionID = None, setSectionSchedulingCategoryIDClonedFrom = None, setRelationships = None, returnSectionSchedulingCategoryID = True, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingCategoryID = False, returnSectionID = False, returnSectionSchedulingCategoryIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulingCategory/" + str(SectionSchedulingCategoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionSchedulingCategory(EntityID = 1, setSchedulingCategoryID = None, setSectionID = None, setSectionSchedulingCategoryIDClonedFrom = None, setRelationships = None, returnSectionSchedulingCategoryID = True, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingCategoryID = False, returnSectionID = False, returnSectionSchedulingCategoryIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulingCategory/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionSchedulingCategory(SectionSchedulingCategoryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionSchedulingTeam(EntityID = 1, page = 1, pageSize = 100, returnSectionSchedulingTeamID = True, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingTeamID = False, returnSectionID = False, returnSectionSchedulingTeamIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulingTeam/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionSchedulingTeam(SectionSchedulingTeamID, EntityID = 1, returnSectionSchedulingTeamID = True, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingTeamID = False, returnSectionID = False, returnSectionSchedulingTeamIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulingTeam/" + str(SectionSchedulingTeamID), verb = "get", return_params_list = return_params_list)

def modifySectionSchedulingTeam(SectionSchedulingTeamID, EntityID = 1, setSchedulingTeamID = None, setSectionID = None, setSectionSchedulingTeamIDClonedFrom = None, setRelationships = None, returnSectionSchedulingTeamID = True, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingTeamID = False, returnSectionID = False, returnSectionSchedulingTeamIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulingTeam/" + str(SectionSchedulingTeamID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionSchedulingTeam(EntityID = 1, setSchedulingTeamID = None, setSectionID = None, setSectionSchedulingTeamIDClonedFrom = None, setRelationships = None, returnSectionSchedulingTeamID = True, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingTeamID = False, returnSectionID = False, returnSectionSchedulingTeamIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/SectionSchedulingTeam/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionSchedulingTeam(SectionSchedulingTeamID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStaffMeet(EntityID = 1, page = 1, pageSize = 100, returnStaffMeetID = True, returnApplyClosedGradingPeriodGradeChangePermission = False, returnAssignmentCount = False, returnCanMakeClosedGradingPeriodGradeChange = False, returnClosedGradingPeriodGradeChangeCount = False, returnCreatedTime = False, returnEffectiveEndDate = False, returnEffectiveStartDate = False, returnGradebookLastAccessedTime = False, returnGradebookLastScoredTime = False, returnHasAttendanceAccess = False, returnHasAttendanceAccessAsOfDate = False, returnHasGradebookAccess = False, returnIsLongTermSubstitute = False, returnIsPrimary = False, returnIsStaffCertified = False, returnIsSubstitute = False, returnLockStaffFromSectionScheduler = False, returnMeetID = False, returnMeetIsCurrent = False, returnMeetsToday = False, returnModifiedTime = False, returnNameMeetDescription = False, returnScheduledBySectionScheduler = False, returnSchoolYearID = False, returnSectionID = False, returnStaffID = False, returnStaffMeetIDClonedFrom = False, returnStaffMeetIDSubstituteFor = False, returnStudentAssignmentIDLastScored = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StaffMeet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStaffMeet(StaffMeetID, EntityID = 1, returnStaffMeetID = True, returnApplyClosedGradingPeriodGradeChangePermission = False, returnAssignmentCount = False, returnCanMakeClosedGradingPeriodGradeChange = False, returnClosedGradingPeriodGradeChangeCount = False, returnCreatedTime = False, returnEffectiveEndDate = False, returnEffectiveStartDate = False, returnGradebookLastAccessedTime = False, returnGradebookLastScoredTime = False, returnHasAttendanceAccess = False, returnHasAttendanceAccessAsOfDate = False, returnHasGradebookAccess = False, returnIsLongTermSubstitute = False, returnIsPrimary = False, returnIsStaffCertified = False, returnIsSubstitute = False, returnLockStaffFromSectionScheduler = False, returnMeetID = False, returnMeetIsCurrent = False, returnMeetsToday = False, returnModifiedTime = False, returnNameMeetDescription = False, returnScheduledBySectionScheduler = False, returnSchoolYearID = False, returnSectionID = False, returnStaffID = False, returnStaffMeetIDClonedFrom = False, returnStaffMeetIDSubstituteFor = False, returnStudentAssignmentIDLastScored = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StaffMeet/" + str(StaffMeetID), verb = "get", return_params_list = return_params_list)

def modifyStaffMeet(StaffMeetID, EntityID = 1, setApplyClosedGradingPeriodGradeChangePermission = None, setCanMakeClosedGradingPeriodGradeChange = None, setEffectiveEndDate = None, setEffectiveStartDate = None, setGradebookLastAccessedTime = None, setGradebookLastScoredTime = None, setHasAttendanceAccess = None, setHasGradebookAccess = None, setIsLongTermSubstitute = None, setIsPrimary = None, setIsStaffCertified = None, setIsSubstitute = None, setLockStaffFromSectionScheduler = None, setMeetID = None, setScheduledBySectionScheduler = None, setSchoolYearID = None, setSectionID = None, setStaffID = None, setStaffMeetIDClonedFrom = None, setStaffMeetIDSubstituteFor = None, setStudentAssignmentIDLastScored = None, setRelationships = None, returnStaffMeetID = True, returnApplyClosedGradingPeriodGradeChangePermission = False, returnAssignmentCount = False, returnCanMakeClosedGradingPeriodGradeChange = False, returnClosedGradingPeriodGradeChangeCount = False, returnCreatedTime = False, returnEffectiveEndDate = False, returnEffectiveStartDate = False, returnGradebookLastAccessedTime = False, returnGradebookLastScoredTime = False, returnHasAttendanceAccess = False, returnHasAttendanceAccessAsOfDate = False, returnHasGradebookAccess = False, returnIsLongTermSubstitute = False, returnIsPrimary = False, returnIsStaffCertified = False, returnIsSubstitute = False, returnLockStaffFromSectionScheduler = False, returnMeetID = False, returnMeetIsCurrent = False, returnMeetsToday = False, returnModifiedTime = False, returnNameMeetDescription = False, returnScheduledBySectionScheduler = False, returnSchoolYearID = False, returnSectionID = False, returnStaffID = False, returnStaffMeetIDClonedFrom = False, returnStaffMeetIDSubstituteFor = False, returnStudentAssignmentIDLastScored = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StaffMeet/" + str(StaffMeetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStaffMeet(EntityID = 1, setApplyClosedGradingPeriodGradeChangePermission = None, setCanMakeClosedGradingPeriodGradeChange = None, setEffectiveEndDate = None, setEffectiveStartDate = None, setGradebookLastAccessedTime = None, setGradebookLastScoredTime = None, setHasAttendanceAccess = None, setHasGradebookAccess = None, setIsLongTermSubstitute = None, setIsPrimary = None, setIsStaffCertified = None, setIsSubstitute = None, setLockStaffFromSectionScheduler = None, setMeetID = None, setScheduledBySectionScheduler = None, setSchoolYearID = None, setSectionID = None, setStaffID = None, setStaffMeetIDClonedFrom = None, setStaffMeetIDSubstituteFor = None, setStudentAssignmentIDLastScored = None, setRelationships = None, returnStaffMeetID = True, returnApplyClosedGradingPeriodGradeChangePermission = False, returnAssignmentCount = False, returnCanMakeClosedGradingPeriodGradeChange = False, returnClosedGradingPeriodGradeChangeCount = False, returnCreatedTime = False, returnEffectiveEndDate = False, returnEffectiveStartDate = False, returnGradebookLastAccessedTime = False, returnGradebookLastScoredTime = False, returnHasAttendanceAccess = False, returnHasAttendanceAccessAsOfDate = False, returnHasGradebookAccess = False, returnIsLongTermSubstitute = False, returnIsPrimary = False, returnIsStaffCertified = False, returnIsSubstitute = False, returnLockStaffFromSectionScheduler = False, returnMeetID = False, returnMeetIsCurrent = False, returnMeetsToday = False, returnModifiedTime = False, returnNameMeetDescription = False, returnScheduledBySectionScheduler = False, returnSchoolYearID = False, returnSectionID = False, returnStaffID = False, returnStaffMeetIDClonedFrom = False, returnStaffMeetIDSubstituteFor = False, returnStudentAssignmentIDLastScored = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StaffMeet/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStaffMeet(StaffMeetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStaffStudent(EntityID = 1, page = 1, pageSize = 100, returnStudentID = True, returnEntityID = False, returnSchoolYearID = False, returnStaffID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StaffStudent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStaffStudent(StudentID, EntityID = 1, returnStudentID = True, returnEntityID = False, returnSchoolYearID = False, returnStaffID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StaffStudent/" + str(StudentID), verb = "get", return_params_list = return_params_list)

def modifyStaffStudent(StudentID, EntityID = 1, setRelationships = None, returnStudentID = True, returnEntityID = False, returnSchoolYearID = False, returnStaffID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StaffStudent/" + str(StudentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStaffStudent(EntityID = 1, setRelationships = None, returnStudentID = True, returnEntityID = False, returnSchoolYearID = False, returnStaffID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StaffStudent/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStaffStudent(StudentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentAutoSchedulerCourse(EntityID = 1, page = 1, pageSize = 100, returnStudentAutoSchedulerCourseID = True, returnActiveSections = False, returnCategoryCode = False, returnConflictedRequestPercent = False, returnCourseCode = False, returnCourseDescription = False, returnCourseEntityCode = False, returnCourseEntityID = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseSubjectCode = False, returnCreatedTime = False, returnDepartmentCode = False, returnIsActive = False, returnIsRequired = False, returnModifiedTime = False, returnScheduledRequestPercent = False, returnSchedulingPriorityCode = False, returnSchedulingTeamModeCode = False, returnSchedulingTypeCode = False, returnStudentAutoSchedulerRunAnalysisID = False, returnTotalAlternateRequests = False, returnTotalConflicts = False, returnTotalNumberScheduledThisRun = False, returnTotalRequests = False, returnTotalScheduled = False, returnTotalSeatsAvailable = False, returnTotalSeatsScheduled = False, returnTotalSections = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentAutoSchedulerCourse(StudentAutoSchedulerCourseID, EntityID = 1, returnStudentAutoSchedulerCourseID = True, returnActiveSections = False, returnCategoryCode = False, returnConflictedRequestPercent = False, returnCourseCode = False, returnCourseDescription = False, returnCourseEntityCode = False, returnCourseEntityID = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseSubjectCode = False, returnCreatedTime = False, returnDepartmentCode = False, returnIsActive = False, returnIsRequired = False, returnModifiedTime = False, returnScheduledRequestPercent = False, returnSchedulingPriorityCode = False, returnSchedulingTeamModeCode = False, returnSchedulingTypeCode = False, returnStudentAutoSchedulerRunAnalysisID = False, returnTotalAlternateRequests = False, returnTotalConflicts = False, returnTotalNumberScheduledThisRun = False, returnTotalRequests = False, returnTotalScheduled = False, returnTotalSeatsAvailable = False, returnTotalSeatsScheduled = False, returnTotalSections = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerCourse/" + str(StudentAutoSchedulerCourseID), verb = "get", return_params_list = return_params_list)

def modifyStudentAutoSchedulerCourse(StudentAutoSchedulerCourseID, EntityID = 1, setCategoryCode = None, setCourseCode = None, setCourseDescription = None, setCourseEntityCode = None, setCourseEntityID = None, setCourseID = None, setCourseLengthCode = None, setCourseSubjectCode = None, setDepartmentCode = None, setIsActive = None, setIsRequired = None, setSchedulingPriorityCode = None, setSchedulingTeamModeCode = None, setSchedulingTypeCode = None, setStudentAutoSchedulerRunAnalysisID = None, setTotalAlternateRequests = None, setTotalConflicts = None, setTotalNumberScheduledThisRun = None, setTotalRequests = None, setTotalScheduled = None, setRelationships = None, returnStudentAutoSchedulerCourseID = True, returnActiveSections = False, returnCategoryCode = False, returnConflictedRequestPercent = False, returnCourseCode = False, returnCourseDescription = False, returnCourseEntityCode = False, returnCourseEntityID = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseSubjectCode = False, returnCreatedTime = False, returnDepartmentCode = False, returnIsActive = False, returnIsRequired = False, returnModifiedTime = False, returnScheduledRequestPercent = False, returnSchedulingPriorityCode = False, returnSchedulingTeamModeCode = False, returnSchedulingTypeCode = False, returnStudentAutoSchedulerRunAnalysisID = False, returnTotalAlternateRequests = False, returnTotalConflicts = False, returnTotalNumberScheduledThisRun = False, returnTotalRequests = False, returnTotalScheduled = False, returnTotalSeatsAvailable = False, returnTotalSeatsScheduled = False, returnTotalSections = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerCourse/" + str(StudentAutoSchedulerCourseID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentAutoSchedulerCourse(EntityID = 1, setCategoryCode = None, setCourseCode = None, setCourseDescription = None, setCourseEntityCode = None, setCourseEntityID = None, setCourseID = None, setCourseLengthCode = None, setCourseSubjectCode = None, setDepartmentCode = None, setIsActive = None, setIsRequired = None, setSchedulingPriorityCode = None, setSchedulingTeamModeCode = None, setSchedulingTypeCode = None, setStudentAutoSchedulerRunAnalysisID = None, setTotalAlternateRequests = None, setTotalConflicts = None, setTotalNumberScheduledThisRun = None, setTotalRequests = None, setTotalScheduled = None, setRelationships = None, returnStudentAutoSchedulerCourseID = True, returnActiveSections = False, returnCategoryCode = False, returnConflictedRequestPercent = False, returnCourseCode = False, returnCourseDescription = False, returnCourseEntityCode = False, returnCourseEntityID = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseSubjectCode = False, returnCreatedTime = False, returnDepartmentCode = False, returnIsActive = False, returnIsRequired = False, returnModifiedTime = False, returnScheduledRequestPercent = False, returnSchedulingPriorityCode = False, returnSchedulingTeamModeCode = False, returnSchedulingTypeCode = False, returnStudentAutoSchedulerRunAnalysisID = False, returnTotalAlternateRequests = False, returnTotalConflicts = False, returnTotalNumberScheduledThisRun = False, returnTotalRequests = False, returnTotalScheduled = False, returnTotalSeatsAvailable = False, returnTotalSeatsScheduled = False, returnTotalSections = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerCourse/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentAutoSchedulerCourse(StudentAutoSchedulerCourseID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentAutoSchedulerProposedStudentCourseRequest(EntityID = 1, page = 1, pageSize = 100, returnStudentAutoSchedulerProposedStudentCourseRequestID = True, returnBaseRunAnalysisID = False, returnCachedStudentSectionID = False, returnCourseConflictReason = False, returnCourseConflictReasonCode = False, returnCourseConflictReasonText = False, returnCourseID = False, returnCourseIDOriginal = False, returnCreatedTime = False, returnDataCommittedToRealObjects = False, returnEntityIDRequestedFrom = False, returnIgnore = False, returnIsAlternate = False, returnIsNewlyScheduled = False, returnModifiedTime = False, returnRequestStatus = False, returnRequestStatusCode = False, returnRequestStatusOriginal = False, returnRequestStatusOriginalCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSchedulingMethodOriginal = False, returnSchedulingMethodOriginalCode = False, returnSectionID = False, returnSectionIDOriginal = False, returnSectionLengthSubsetsRequested = False, returnSectionLengthSubsetSummary = False, returnSequenceWithinEntireProcess = False, returnSequenceWithinGrade = False, returnSequenceWithinStudent = False, returnStudentCourseRequestID = False, returnStudentCourseRequestIDOriginal = False, returnStudentID = False, returnStudentIDOriginal = False, returnStudentSectionID = False, returnStudentSectionIDOriginal = False, returnUnscheduleStatus = False, returnUnscheduleStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerProposedStudentCourseRequest/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentAutoSchedulerProposedStudentCourseRequest(StudentAutoSchedulerProposedStudentCourseRequestID, EntityID = 1, returnStudentAutoSchedulerProposedStudentCourseRequestID = True, returnBaseRunAnalysisID = False, returnCachedStudentSectionID = False, returnCourseConflictReason = False, returnCourseConflictReasonCode = False, returnCourseConflictReasonText = False, returnCourseID = False, returnCourseIDOriginal = False, returnCreatedTime = False, returnDataCommittedToRealObjects = False, returnEntityIDRequestedFrom = False, returnIgnore = False, returnIsAlternate = False, returnIsNewlyScheduled = False, returnModifiedTime = False, returnRequestStatus = False, returnRequestStatusCode = False, returnRequestStatusOriginal = False, returnRequestStatusOriginalCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSchedulingMethodOriginal = False, returnSchedulingMethodOriginalCode = False, returnSectionID = False, returnSectionIDOriginal = False, returnSectionLengthSubsetsRequested = False, returnSectionLengthSubsetSummary = False, returnSequenceWithinEntireProcess = False, returnSequenceWithinGrade = False, returnSequenceWithinStudent = False, returnStudentCourseRequestID = False, returnStudentCourseRequestIDOriginal = False, returnStudentID = False, returnStudentIDOriginal = False, returnStudentSectionID = False, returnStudentSectionIDOriginal = False, returnUnscheduleStatus = False, returnUnscheduleStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerProposedStudentCourseRequest/" + str(StudentAutoSchedulerProposedStudentCourseRequestID), verb = "get", return_params_list = return_params_list)

def modifyStudentAutoSchedulerProposedStudentCourseRequest(StudentAutoSchedulerProposedStudentCourseRequestID, EntityID = 1, setBaseRunAnalysisID = None, setCachedStudentSectionID = None, setCourseConflictReason = None, setCourseConflictReasonCode = None, setCourseConflictReasonText = None, setCourseID = None, setCourseIDOriginal = None, setDataCommittedToRealObjects = None, setEntityIDRequestedFrom = None, setIgnore = None, setIsAlternate = None, setRequestStatus = None, setRequestStatusCode = None, setRequestStatusOriginal = None, setRequestStatusOriginalCode = None, setSchedulingMethod = None, setSchedulingMethodCode = None, setSchedulingMethodOriginal = None, setSchedulingMethodOriginalCode = None, setSectionID = None, setSectionIDOriginal = None, setSectionLengthSubsetsRequested = None, setSectionLengthSubsetSummary = None, setSequenceWithinEntireProcess = None, setSequenceWithinGrade = None, setSequenceWithinStudent = None, setStudentCourseRequestID = None, setStudentCourseRequestIDOriginal = None, setStudentID = None, setStudentIDOriginal = None, setStudentSectionID = None, setStudentSectionIDOriginal = None, setUnscheduleStatus = None, setUnscheduleStatusCode = None, setRelationships = None, returnStudentAutoSchedulerProposedStudentCourseRequestID = True, returnBaseRunAnalysisID = False, returnCachedStudentSectionID = False, returnCourseConflictReason = False, returnCourseConflictReasonCode = False, returnCourseConflictReasonText = False, returnCourseID = False, returnCourseIDOriginal = False, returnCreatedTime = False, returnDataCommittedToRealObjects = False, returnEntityIDRequestedFrom = False, returnIgnore = False, returnIsAlternate = False, returnIsNewlyScheduled = False, returnModifiedTime = False, returnRequestStatus = False, returnRequestStatusCode = False, returnRequestStatusOriginal = False, returnRequestStatusOriginalCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSchedulingMethodOriginal = False, returnSchedulingMethodOriginalCode = False, returnSectionID = False, returnSectionIDOriginal = False, returnSectionLengthSubsetsRequested = False, returnSectionLengthSubsetSummary = False, returnSequenceWithinEntireProcess = False, returnSequenceWithinGrade = False, returnSequenceWithinStudent = False, returnStudentCourseRequestID = False, returnStudentCourseRequestIDOriginal = False, returnStudentID = False, returnStudentIDOriginal = False, returnStudentSectionID = False, returnStudentSectionIDOriginal = False, returnUnscheduleStatus = False, returnUnscheduleStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerProposedStudentCourseRequest/" + str(StudentAutoSchedulerProposedStudentCourseRequestID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentAutoSchedulerProposedStudentCourseRequest(EntityID = 1, setBaseRunAnalysisID = None, setCachedStudentSectionID = None, setCourseConflictReason = None, setCourseConflictReasonCode = None, setCourseConflictReasonText = None, setCourseID = None, setCourseIDOriginal = None, setDataCommittedToRealObjects = None, setEntityIDRequestedFrom = None, setIgnore = None, setIsAlternate = None, setRequestStatus = None, setRequestStatusCode = None, setRequestStatusOriginal = None, setRequestStatusOriginalCode = None, setSchedulingMethod = None, setSchedulingMethodCode = None, setSchedulingMethodOriginal = None, setSchedulingMethodOriginalCode = None, setSectionID = None, setSectionIDOriginal = None, setSectionLengthSubsetsRequested = None, setSectionLengthSubsetSummary = None, setSequenceWithinEntireProcess = None, setSequenceWithinGrade = None, setSequenceWithinStudent = None, setStudentCourseRequestID = None, setStudentCourseRequestIDOriginal = None, setStudentID = None, setStudentIDOriginal = None, setStudentSectionID = None, setStudentSectionIDOriginal = None, setUnscheduleStatus = None, setUnscheduleStatusCode = None, setRelationships = None, returnStudentAutoSchedulerProposedStudentCourseRequestID = True, returnBaseRunAnalysisID = False, returnCachedStudentSectionID = False, returnCourseConflictReason = False, returnCourseConflictReasonCode = False, returnCourseConflictReasonText = False, returnCourseID = False, returnCourseIDOriginal = False, returnCreatedTime = False, returnDataCommittedToRealObjects = False, returnEntityIDRequestedFrom = False, returnIgnore = False, returnIsAlternate = False, returnIsNewlyScheduled = False, returnModifiedTime = False, returnRequestStatus = False, returnRequestStatusCode = False, returnRequestStatusOriginal = False, returnRequestStatusOriginalCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSchedulingMethodOriginal = False, returnSchedulingMethodOriginalCode = False, returnSectionID = False, returnSectionIDOriginal = False, returnSectionLengthSubsetsRequested = False, returnSectionLengthSubsetSummary = False, returnSequenceWithinEntireProcess = False, returnSequenceWithinGrade = False, returnSequenceWithinStudent = False, returnStudentCourseRequestID = False, returnStudentCourseRequestIDOriginal = False, returnStudentID = False, returnStudentIDOriginal = False, returnStudentSectionID = False, returnStudentSectionIDOriginal = False, returnUnscheduleStatus = False, returnUnscheduleStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerProposedStudentCourseRequest/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentAutoSchedulerProposedStudentCourseRequest(StudentAutoSchedulerProposedStudentCourseRequestID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentAutoSchedulerProposedStudentSection(EntityID = 1, page = 1, pageSize = 100, returnStudentAutoSchedulerProposedStudentSectionID = True, returnBaseRunAnalysisID = False, returnCachedStudentSectionID = False, returnCreatedTime = False, returnDataCommittedToRealObjects = False, returnGradeReferenceID = False, returnGradeReferenceIDOriginal = False, returnModifiedTime = False, returnSectionID = False, returnSectionIDOriginal = False, returnSequenceWithinEntireProcess = False, returnSequenceWithinGrade = False, returnSequenceWithinStudent = False, returnStudentID = False, returnStudentIDOriginal = False, returnStudentSectionID = False, returnStudentSectionIDOriginal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerProposedStudentSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentAutoSchedulerProposedStudentSection(StudentAutoSchedulerProposedStudentSectionID, EntityID = 1, returnStudentAutoSchedulerProposedStudentSectionID = True, returnBaseRunAnalysisID = False, returnCachedStudentSectionID = False, returnCreatedTime = False, returnDataCommittedToRealObjects = False, returnGradeReferenceID = False, returnGradeReferenceIDOriginal = False, returnModifiedTime = False, returnSectionID = False, returnSectionIDOriginal = False, returnSequenceWithinEntireProcess = False, returnSequenceWithinGrade = False, returnSequenceWithinStudent = False, returnStudentID = False, returnStudentIDOriginal = False, returnStudentSectionID = False, returnStudentSectionIDOriginal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerProposedStudentSection/" + str(StudentAutoSchedulerProposedStudentSectionID), verb = "get", return_params_list = return_params_list)

def modifyStudentAutoSchedulerProposedStudentSection(StudentAutoSchedulerProposedStudentSectionID, EntityID = 1, setBaseRunAnalysisID = None, setCachedStudentSectionID = None, setDataCommittedToRealObjects = None, setGradeReferenceID = None, setGradeReferenceIDOriginal = None, setSectionID = None, setSectionIDOriginal = None, setSequenceWithinEntireProcess = None, setSequenceWithinGrade = None, setSequenceWithinStudent = None, setStudentID = None, setStudentIDOriginal = None, setStudentSectionID = None, setStudentSectionIDOriginal = None, setRelationships = None, returnStudentAutoSchedulerProposedStudentSectionID = True, returnBaseRunAnalysisID = False, returnCachedStudentSectionID = False, returnCreatedTime = False, returnDataCommittedToRealObjects = False, returnGradeReferenceID = False, returnGradeReferenceIDOriginal = False, returnModifiedTime = False, returnSectionID = False, returnSectionIDOriginal = False, returnSequenceWithinEntireProcess = False, returnSequenceWithinGrade = False, returnSequenceWithinStudent = False, returnStudentID = False, returnStudentIDOriginal = False, returnStudentSectionID = False, returnStudentSectionIDOriginal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerProposedStudentSection/" + str(StudentAutoSchedulerProposedStudentSectionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentAutoSchedulerProposedStudentSection(EntityID = 1, setBaseRunAnalysisID = None, setCachedStudentSectionID = None, setDataCommittedToRealObjects = None, setGradeReferenceID = None, setGradeReferenceIDOriginal = None, setSectionID = None, setSectionIDOriginal = None, setSequenceWithinEntireProcess = None, setSequenceWithinGrade = None, setSequenceWithinStudent = None, setStudentID = None, setStudentIDOriginal = None, setStudentSectionID = None, setStudentSectionIDOriginal = None, setRelationships = None, returnStudentAutoSchedulerProposedStudentSectionID = True, returnBaseRunAnalysisID = False, returnCachedStudentSectionID = False, returnCreatedTime = False, returnDataCommittedToRealObjects = False, returnGradeReferenceID = False, returnGradeReferenceIDOriginal = False, returnModifiedTime = False, returnSectionID = False, returnSectionIDOriginal = False, returnSequenceWithinEntireProcess = False, returnSequenceWithinGrade = False, returnSequenceWithinStudent = False, returnStudentID = False, returnStudentIDOriginal = False, returnStudentSectionID = False, returnStudentSectionIDOriginal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerProposedStudentSection/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentAutoSchedulerProposedStudentSection(StudentAutoSchedulerProposedStudentSectionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentAutoSchedulerProposedStudentSectionTransaction(EntityID = 1, page = 1, pageSize = 100, returnStudentAutoSchedulerProposedStudentSectionTransactionID = True, returnBaseRunAnalysisID = False, returnCachedStudentSectionID = False, returnCreatedTime = False, returnDataCommittedToRealObjects = False, returnEndDate = False, returnEndDateOriginal = False, returnEntityIDCountsAs = False, returnModifiedTime = False, returnSectionID = False, returnSectionIDOriginal = False, returnSectionLengthSubsetID = False, returnSectionLengthSubsetIDOriginal = False, returnStartDate = False, returnStartDateOriginal = False, returnStudentSectionID = False, returnStudentSectionIDOriginal = False, returnStudentSectionTransactionID = False, returnStudentSectionTransactionIDOriginal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerProposedStudentSectionTransaction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentAutoSchedulerProposedStudentSectionTransaction(StudentAutoSchedulerProposedStudentSectionTransactionID, EntityID = 1, returnStudentAutoSchedulerProposedStudentSectionTransactionID = True, returnBaseRunAnalysisID = False, returnCachedStudentSectionID = False, returnCreatedTime = False, returnDataCommittedToRealObjects = False, returnEndDate = False, returnEndDateOriginal = False, returnEntityIDCountsAs = False, returnModifiedTime = False, returnSectionID = False, returnSectionIDOriginal = False, returnSectionLengthSubsetID = False, returnSectionLengthSubsetIDOriginal = False, returnStartDate = False, returnStartDateOriginal = False, returnStudentSectionID = False, returnStudentSectionIDOriginal = False, returnStudentSectionTransactionID = False, returnStudentSectionTransactionIDOriginal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerProposedStudentSectionTransaction/" + str(StudentAutoSchedulerProposedStudentSectionTransactionID), verb = "get", return_params_list = return_params_list)

def modifyStudentAutoSchedulerProposedStudentSectionTransaction(StudentAutoSchedulerProposedStudentSectionTransactionID, EntityID = 1, setBaseRunAnalysisID = None, setCachedStudentSectionID = None, setDataCommittedToRealObjects = None, setEndDate = None, setEndDateOriginal = None, setEntityIDCountsAs = None, setSectionID = None, setSectionIDOriginal = None, setSectionLengthSubsetID = None, setSectionLengthSubsetIDOriginal = None, setStartDate = None, setStartDateOriginal = None, setStudentSectionID = None, setStudentSectionIDOriginal = None, setStudentSectionTransactionID = None, setStudentSectionTransactionIDOriginal = None, setRelationships = None, returnStudentAutoSchedulerProposedStudentSectionTransactionID = True, returnBaseRunAnalysisID = False, returnCachedStudentSectionID = False, returnCreatedTime = False, returnDataCommittedToRealObjects = False, returnEndDate = False, returnEndDateOriginal = False, returnEntityIDCountsAs = False, returnModifiedTime = False, returnSectionID = False, returnSectionIDOriginal = False, returnSectionLengthSubsetID = False, returnSectionLengthSubsetIDOriginal = False, returnStartDate = False, returnStartDateOriginal = False, returnStudentSectionID = False, returnStudentSectionIDOriginal = False, returnStudentSectionTransactionID = False, returnStudentSectionTransactionIDOriginal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerProposedStudentSectionTransaction/" + str(StudentAutoSchedulerProposedStudentSectionTransactionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentAutoSchedulerProposedStudentSectionTransaction(EntityID = 1, setBaseRunAnalysisID = None, setCachedStudentSectionID = None, setDataCommittedToRealObjects = None, setEndDate = None, setEndDateOriginal = None, setEntityIDCountsAs = None, setSectionID = None, setSectionIDOriginal = None, setSectionLengthSubsetID = None, setSectionLengthSubsetIDOriginal = None, setStartDate = None, setStartDateOriginal = None, setStudentSectionID = None, setStudentSectionIDOriginal = None, setStudentSectionTransactionID = None, setStudentSectionTransactionIDOriginal = None, setRelationships = None, returnStudentAutoSchedulerProposedStudentSectionTransactionID = True, returnBaseRunAnalysisID = False, returnCachedStudentSectionID = False, returnCreatedTime = False, returnDataCommittedToRealObjects = False, returnEndDate = False, returnEndDateOriginal = False, returnEntityIDCountsAs = False, returnModifiedTime = False, returnSectionID = False, returnSectionIDOriginal = False, returnSectionLengthSubsetID = False, returnSectionLengthSubsetIDOriginal = False, returnStartDate = False, returnStartDateOriginal = False, returnStudentSectionID = False, returnStudentSectionIDOriginal = False, returnStudentSectionTransactionID = False, returnStudentSectionTransactionIDOriginal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerProposedStudentSectionTransaction/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentAutoSchedulerProposedStudentSectionTransaction(StudentAutoSchedulerProposedStudentSectionTransactionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentAutoSchedulerRunAnalysis(EntityID = 1, page = 1, pageSize = 100, returnStudentAutoSchedulerRunAnalysisID = True, returnAnalysisDuration = False, returnAnalysisVersion = False, returnAnalysisVersionCode = False, returnBaseRunAnalysisID = False, returnCloseSectionsWhenFilled = False, returnConflictedStudentCourseRequestPercent = False, returnCountOfStudentAutoSchedulerCourseRecords = False, returnCountOfStudentAutoSchedulerRunAnalysisExceptionRecords = False, returnCountOfStudentAutoSchedulerStudentRecords = False, returnCourseConflictPercent = False, returnCreatedCourseAndSectionAnalysisDetails = False, returnCreatedStudentAnalysisDetails = False, returnCreatedTime = False, returnDescription = False, returnEndTimeAnalysis = False, returnEndTimeFinalize = False, returnExistsAutoScheduledCourses = False, returnExistsAutoScheduledStudents = False, returnFailedScheduledStudentSectionsCount = False, returnFailedStudentCourseRequestsCount = False, returnFailedStudentSectionsCount = False, returnFailedStudentSectionTransactionsCount = False, returnFinalizeDuration = False, returnGradeReferenceIDEnd = False, returnGradeReferenceIDStart = False, returnIncludedAbilityToAcceptProposedSchedules = False, returnIsInvalidFinalizeState = False, returnModifiedTime = False, returnOverallDuration = False, returnPersistentSchedulingRunDataIsNoLongerAcceptable = False, returnProcessSpecialEdCourses = False, returnProposedSchedulesAccepted = False, returnRunInformation = False, returnScheduledStudentCourseRequestPercent = False, returnSendMessageOnComplete = False, returnStartTimeAnalysis = False, returnStartTimeFinalize = False, returnStudentAutoSchedulerMode = False, returnStudentAutoSchedulerModeCode = False, returnStudentConflictPercent = False, returnStudentCourseRequestOrder = False, returnStudentCourseRequestsConflictedThisRun = False, returnStudentCourseRequestsProcessedThisRun = False, returnStudentCourseRequestsScheduledThisRun = False, returnStudentDifficultyOrder = False, returnStudentInformation = False, returnSuccessfulStudentSectionsCount = False, returnTotalAlternateStudentCourseRequests = False, returnTotalConflictedStudentCourseRequests = False, returnTotalScheduledStudentCourseRequests = False, returnTotalStudentCourseRequests = False, returnTotalStudentCourseRequestsToFinalize = False, returnTotalStudents = False, returnTotalStudentSectionsToFinalize = False, returnTotalStudentSectionTransactionsToFinalize = False, returnTotalStudentsWithConflicts = False, returnTotalStudentsWithOneConflict = False, returnTotalStudentsWithThreeOrMoreConflicts = False, returnTotalStudentsWithTwoConflicts = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerRunAnalysis/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentAutoSchedulerRunAnalysis(StudentAutoSchedulerRunAnalysisID, EntityID = 1, returnStudentAutoSchedulerRunAnalysisID = True, returnAnalysisDuration = False, returnAnalysisVersion = False, returnAnalysisVersionCode = False, returnBaseRunAnalysisID = False, returnCloseSectionsWhenFilled = False, returnConflictedStudentCourseRequestPercent = False, returnCountOfStudentAutoSchedulerCourseRecords = False, returnCountOfStudentAutoSchedulerRunAnalysisExceptionRecords = False, returnCountOfStudentAutoSchedulerStudentRecords = False, returnCourseConflictPercent = False, returnCreatedCourseAndSectionAnalysisDetails = False, returnCreatedStudentAnalysisDetails = False, returnCreatedTime = False, returnDescription = False, returnEndTimeAnalysis = False, returnEndTimeFinalize = False, returnExistsAutoScheduledCourses = False, returnExistsAutoScheduledStudents = False, returnFailedScheduledStudentSectionsCount = False, returnFailedStudentCourseRequestsCount = False, returnFailedStudentSectionsCount = False, returnFailedStudentSectionTransactionsCount = False, returnFinalizeDuration = False, returnGradeReferenceIDEnd = False, returnGradeReferenceIDStart = False, returnIncludedAbilityToAcceptProposedSchedules = False, returnIsInvalidFinalizeState = False, returnModifiedTime = False, returnOverallDuration = False, returnPersistentSchedulingRunDataIsNoLongerAcceptable = False, returnProcessSpecialEdCourses = False, returnProposedSchedulesAccepted = False, returnRunInformation = False, returnScheduledStudentCourseRequestPercent = False, returnSendMessageOnComplete = False, returnStartTimeAnalysis = False, returnStartTimeFinalize = False, returnStudentAutoSchedulerMode = False, returnStudentAutoSchedulerModeCode = False, returnStudentConflictPercent = False, returnStudentCourseRequestOrder = False, returnStudentCourseRequestsConflictedThisRun = False, returnStudentCourseRequestsProcessedThisRun = False, returnStudentCourseRequestsScheduledThisRun = False, returnStudentDifficultyOrder = False, returnStudentInformation = False, returnSuccessfulStudentSectionsCount = False, returnTotalAlternateStudentCourseRequests = False, returnTotalConflictedStudentCourseRequests = False, returnTotalScheduledStudentCourseRequests = False, returnTotalStudentCourseRequests = False, returnTotalStudentCourseRequestsToFinalize = False, returnTotalStudents = False, returnTotalStudentSectionsToFinalize = False, returnTotalStudentSectionTransactionsToFinalize = False, returnTotalStudentsWithConflicts = False, returnTotalStudentsWithOneConflict = False, returnTotalStudentsWithThreeOrMoreConflicts = False, returnTotalStudentsWithTwoConflicts = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerRunAnalysis/" + str(StudentAutoSchedulerRunAnalysisID), verb = "get", return_params_list = return_params_list)

def modifyStudentAutoSchedulerRunAnalysis(StudentAutoSchedulerRunAnalysisID, EntityID = 1, setAnalysisVersion = None, setAnalysisVersionCode = None, setBaseRunAnalysisID = None, setCloseSectionsWhenFilled = None, setCreatedCourseAndSectionAnalysisDetails = None, setCreatedStudentAnalysisDetails = None, setDescription = None, setEndTimeAnalysis = None, setEndTimeFinalize = None, setFailedScheduledStudentSectionsCount = None, setFailedStudentCourseRequestsCount = None, setFailedStudentSectionsCount = None, setFailedStudentSectionTransactionsCount = None, setGradeReferenceIDEnd = None, setGradeReferenceIDStart = None, setIncludedAbilityToAcceptProposedSchedules = None, setPersistentSchedulingRunDataIsNoLongerAcceptable = None, setProcessSpecialEdCourses = None, setRunInformation = None, setSendMessageOnComplete = None, setStartTimeAnalysis = None, setStartTimeFinalize = None, setStudentAutoSchedulerMode = None, setStudentAutoSchedulerModeCode = None, setStudentCourseRequestOrder = None, setStudentDifficultyOrder = None, setStudentInformation = None, setSuccessfulStudentSectionsCount = None, setTotalAlternateStudentCourseRequests = None, setTotalConflictedStudentCourseRequests = None, setTotalScheduledStudentCourseRequests = None, setTotalStudentCourseRequests = None, setTotalStudentCourseRequestsToFinalize = None, setTotalStudents = None, setTotalStudentSectionsToFinalize = None, setTotalStudentSectionTransactionsToFinalize = None, setTotalStudentsWithConflicts = None, setTotalStudentsWithOneConflict = None, setTotalStudentsWithThreeOrMoreConflicts = None, setTotalStudentsWithTwoConflicts = None, setRelationships = None, returnStudentAutoSchedulerRunAnalysisID = True, returnAnalysisDuration = False, returnAnalysisVersion = False, returnAnalysisVersionCode = False, returnBaseRunAnalysisID = False, returnCloseSectionsWhenFilled = False, returnConflictedStudentCourseRequestPercent = False, returnCountOfStudentAutoSchedulerCourseRecords = False, returnCountOfStudentAutoSchedulerRunAnalysisExceptionRecords = False, returnCountOfStudentAutoSchedulerStudentRecords = False, returnCourseConflictPercent = False, returnCreatedCourseAndSectionAnalysisDetails = False, returnCreatedStudentAnalysisDetails = False, returnCreatedTime = False, returnDescription = False, returnEndTimeAnalysis = False, returnEndTimeFinalize = False, returnExistsAutoScheduledCourses = False, returnExistsAutoScheduledStudents = False, returnFailedScheduledStudentSectionsCount = False, returnFailedStudentCourseRequestsCount = False, returnFailedStudentSectionsCount = False, returnFailedStudentSectionTransactionsCount = False, returnFinalizeDuration = False, returnGradeReferenceIDEnd = False, returnGradeReferenceIDStart = False, returnIncludedAbilityToAcceptProposedSchedules = False, returnIsInvalidFinalizeState = False, returnModifiedTime = False, returnOverallDuration = False, returnPersistentSchedulingRunDataIsNoLongerAcceptable = False, returnProcessSpecialEdCourses = False, returnProposedSchedulesAccepted = False, returnRunInformation = False, returnScheduledStudentCourseRequestPercent = False, returnSendMessageOnComplete = False, returnStartTimeAnalysis = False, returnStartTimeFinalize = False, returnStudentAutoSchedulerMode = False, returnStudentAutoSchedulerModeCode = False, returnStudentConflictPercent = False, returnStudentCourseRequestOrder = False, returnStudentCourseRequestsConflictedThisRun = False, returnStudentCourseRequestsProcessedThisRun = False, returnStudentCourseRequestsScheduledThisRun = False, returnStudentDifficultyOrder = False, returnStudentInformation = False, returnSuccessfulStudentSectionsCount = False, returnTotalAlternateStudentCourseRequests = False, returnTotalConflictedStudentCourseRequests = False, returnTotalScheduledStudentCourseRequests = False, returnTotalStudentCourseRequests = False, returnTotalStudentCourseRequestsToFinalize = False, returnTotalStudents = False, returnTotalStudentSectionsToFinalize = False, returnTotalStudentSectionTransactionsToFinalize = False, returnTotalStudentsWithConflicts = False, returnTotalStudentsWithOneConflict = False, returnTotalStudentsWithThreeOrMoreConflicts = False, returnTotalStudentsWithTwoConflicts = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerRunAnalysis/" + str(StudentAutoSchedulerRunAnalysisID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentAutoSchedulerRunAnalysis(EntityID = 1, setAnalysisVersion = None, setAnalysisVersionCode = None, setBaseRunAnalysisID = None, setCloseSectionsWhenFilled = None, setCreatedCourseAndSectionAnalysisDetails = None, setCreatedStudentAnalysisDetails = None, setDescription = None, setEndTimeAnalysis = None, setEndTimeFinalize = None, setFailedScheduledStudentSectionsCount = None, setFailedStudentCourseRequestsCount = None, setFailedStudentSectionsCount = None, setFailedStudentSectionTransactionsCount = None, setGradeReferenceIDEnd = None, setGradeReferenceIDStart = None, setIncludedAbilityToAcceptProposedSchedules = None, setPersistentSchedulingRunDataIsNoLongerAcceptable = None, setProcessSpecialEdCourses = None, setRunInformation = None, setSendMessageOnComplete = None, setStartTimeAnalysis = None, setStartTimeFinalize = None, setStudentAutoSchedulerMode = None, setStudentAutoSchedulerModeCode = None, setStudentCourseRequestOrder = None, setStudentDifficultyOrder = None, setStudentInformation = None, setSuccessfulStudentSectionsCount = None, setTotalAlternateStudentCourseRequests = None, setTotalConflictedStudentCourseRequests = None, setTotalScheduledStudentCourseRequests = None, setTotalStudentCourseRequests = None, setTotalStudentCourseRequestsToFinalize = None, setTotalStudents = None, setTotalStudentSectionsToFinalize = None, setTotalStudentSectionTransactionsToFinalize = None, setTotalStudentsWithConflicts = None, setTotalStudentsWithOneConflict = None, setTotalStudentsWithThreeOrMoreConflicts = None, setTotalStudentsWithTwoConflicts = None, setRelationships = None, returnStudentAutoSchedulerRunAnalysisID = True, returnAnalysisDuration = False, returnAnalysisVersion = False, returnAnalysisVersionCode = False, returnBaseRunAnalysisID = False, returnCloseSectionsWhenFilled = False, returnConflictedStudentCourseRequestPercent = False, returnCountOfStudentAutoSchedulerCourseRecords = False, returnCountOfStudentAutoSchedulerRunAnalysisExceptionRecords = False, returnCountOfStudentAutoSchedulerStudentRecords = False, returnCourseConflictPercent = False, returnCreatedCourseAndSectionAnalysisDetails = False, returnCreatedStudentAnalysisDetails = False, returnCreatedTime = False, returnDescription = False, returnEndTimeAnalysis = False, returnEndTimeFinalize = False, returnExistsAutoScheduledCourses = False, returnExistsAutoScheduledStudents = False, returnFailedScheduledStudentSectionsCount = False, returnFailedStudentCourseRequestsCount = False, returnFailedStudentSectionsCount = False, returnFailedStudentSectionTransactionsCount = False, returnFinalizeDuration = False, returnGradeReferenceIDEnd = False, returnGradeReferenceIDStart = False, returnIncludedAbilityToAcceptProposedSchedules = False, returnIsInvalidFinalizeState = False, returnModifiedTime = False, returnOverallDuration = False, returnPersistentSchedulingRunDataIsNoLongerAcceptable = False, returnProcessSpecialEdCourses = False, returnProposedSchedulesAccepted = False, returnRunInformation = False, returnScheduledStudentCourseRequestPercent = False, returnSendMessageOnComplete = False, returnStartTimeAnalysis = False, returnStartTimeFinalize = False, returnStudentAutoSchedulerMode = False, returnStudentAutoSchedulerModeCode = False, returnStudentConflictPercent = False, returnStudentCourseRequestOrder = False, returnStudentCourseRequestsConflictedThisRun = False, returnStudentCourseRequestsProcessedThisRun = False, returnStudentCourseRequestsScheduledThisRun = False, returnStudentDifficultyOrder = False, returnStudentInformation = False, returnSuccessfulStudentSectionsCount = False, returnTotalAlternateStudentCourseRequests = False, returnTotalConflictedStudentCourseRequests = False, returnTotalScheduledStudentCourseRequests = False, returnTotalStudentCourseRequests = False, returnTotalStudentCourseRequestsToFinalize = False, returnTotalStudents = False, returnTotalStudentSectionsToFinalize = False, returnTotalStudentSectionTransactionsToFinalize = False, returnTotalStudentsWithConflicts = False, returnTotalStudentsWithOneConflict = False, returnTotalStudentsWithThreeOrMoreConflicts = False, returnTotalStudentsWithTwoConflicts = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerRunAnalysis/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentAutoSchedulerRunAnalysis(StudentAutoSchedulerRunAnalysisID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentAutoSchedulerRunAnalysisException(EntityID = 1, page = 1, pageSize = 100, returnStudentAutoSchedulerRunAnalysisExceptionID = True, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnMessage = False, returnModifiedTime = False, returnSectionCode = False, returnSeverityType = False, returnSeverityTypeCode = False, returnStudentAutoSchedulerRunAnalysisID = False, returnStudentAutoSchedulerStudentCourseRequestID = False, returnStudentFullName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerRunAnalysisException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentAutoSchedulerRunAnalysisException(StudentAutoSchedulerRunAnalysisExceptionID, EntityID = 1, returnStudentAutoSchedulerRunAnalysisExceptionID = True, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnMessage = False, returnModifiedTime = False, returnSectionCode = False, returnSeverityType = False, returnSeverityTypeCode = False, returnStudentAutoSchedulerRunAnalysisID = False, returnStudentAutoSchedulerStudentCourseRequestID = False, returnStudentFullName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerRunAnalysisException/" + str(StudentAutoSchedulerRunAnalysisExceptionID), verb = "get", return_params_list = return_params_list)

def modifyStudentAutoSchedulerRunAnalysisException(StudentAutoSchedulerRunAnalysisExceptionID, EntityID = 1, setCourseCode = None, setCourseDescription = None, setMessage = None, setSectionCode = None, setSeverityType = None, setSeverityTypeCode = None, setStudentAutoSchedulerRunAnalysisID = None, setStudentAutoSchedulerStudentCourseRequestID = None, setStudentFullName = None, setStudentNumber = None, setRelationships = None, returnStudentAutoSchedulerRunAnalysisExceptionID = True, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnMessage = False, returnModifiedTime = False, returnSectionCode = False, returnSeverityType = False, returnSeverityTypeCode = False, returnStudentAutoSchedulerRunAnalysisID = False, returnStudentAutoSchedulerStudentCourseRequestID = False, returnStudentFullName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerRunAnalysisException/" + str(StudentAutoSchedulerRunAnalysisExceptionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentAutoSchedulerRunAnalysisException(EntityID = 1, setCourseCode = None, setCourseDescription = None, setMessage = None, setSectionCode = None, setSeverityType = None, setSeverityTypeCode = None, setStudentAutoSchedulerRunAnalysisID = None, setStudentAutoSchedulerStudentCourseRequestID = None, setStudentFullName = None, setStudentNumber = None, setRelationships = None, returnStudentAutoSchedulerRunAnalysisExceptionID = True, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnMessage = False, returnModifiedTime = False, returnSectionCode = False, returnSeverityType = False, returnSeverityTypeCode = False, returnStudentAutoSchedulerRunAnalysisID = False, returnStudentAutoSchedulerStudentCourseRequestID = False, returnStudentFullName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerRunAnalysisException/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentAutoSchedulerRunAnalysisException(StudentAutoSchedulerRunAnalysisExceptionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentAutoSchedulerRunAnalysisTotal(EntityID = 1, page = 1, pageSize = 100, returnStudentAutoSchedulerRunAnalysisTotalID = True, returnConflictedStudentCourseRequestPercent = False, returnConflictPercent = False, returnCreatedTime = False, returnEndTimeAnalysis = False, returnGradeReferenceID = False, returnModifiedTime = False, returnScheduledStudentCourseRequestPercent = False, returnStartTimeAnalysis = False, returnStudentAutoSchedulerRunAnalysisID = False, returnStudentCourseRequestsConflictedThisRun = False, returnStudentCourseRequestsProcessedThisRun = False, returnStudentCourseRequestsScheduledThisRun = False, returnStudentsWithConflicts = False, returnStudentsWithOneConflict = False, returnStudentsWithThreeOrMoreConflicts = False, returnStudentsWithTwoConflicts = False, returnTotalAlternateStudentCourseRequests = False, returnTotalConflictedStudentCourseRequests = False, returnTotalScheduledStudentCourseRequests = False, returnTotalStudentCourseRequests = False, returnTotalStudents = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerRunAnalysisTotal/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentAutoSchedulerRunAnalysisTotal(StudentAutoSchedulerRunAnalysisTotalID, EntityID = 1, returnStudentAutoSchedulerRunAnalysisTotalID = True, returnConflictedStudentCourseRequestPercent = False, returnConflictPercent = False, returnCreatedTime = False, returnEndTimeAnalysis = False, returnGradeReferenceID = False, returnModifiedTime = False, returnScheduledStudentCourseRequestPercent = False, returnStartTimeAnalysis = False, returnStudentAutoSchedulerRunAnalysisID = False, returnStudentCourseRequestsConflictedThisRun = False, returnStudentCourseRequestsProcessedThisRun = False, returnStudentCourseRequestsScheduledThisRun = False, returnStudentsWithConflicts = False, returnStudentsWithOneConflict = False, returnStudentsWithThreeOrMoreConflicts = False, returnStudentsWithTwoConflicts = False, returnTotalAlternateStudentCourseRequests = False, returnTotalConflictedStudentCourseRequests = False, returnTotalScheduledStudentCourseRequests = False, returnTotalStudentCourseRequests = False, returnTotalStudents = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerRunAnalysisTotal/" + str(StudentAutoSchedulerRunAnalysisTotalID), verb = "get", return_params_list = return_params_list)

def modifyStudentAutoSchedulerRunAnalysisTotal(StudentAutoSchedulerRunAnalysisTotalID, EntityID = 1, setConflictPercent = None, setEndTimeAnalysis = None, setGradeReferenceID = None, setStartTimeAnalysis = None, setStudentAutoSchedulerRunAnalysisID = None, setStudentCourseRequestsConflictedThisRun = None, setStudentCourseRequestsProcessedThisRun = None, setStudentCourseRequestsScheduledThisRun = None, setStudentsWithConflicts = None, setStudentsWithOneConflict = None, setStudentsWithThreeOrMoreConflicts = None, setStudentsWithTwoConflicts = None, setTotalAlternateStudentCourseRequests = None, setTotalConflictedStudentCourseRequests = None, setTotalScheduledStudentCourseRequests = None, setTotalStudentCourseRequests = None, setTotalStudents = None, setRelationships = None, returnStudentAutoSchedulerRunAnalysisTotalID = True, returnConflictedStudentCourseRequestPercent = False, returnConflictPercent = False, returnCreatedTime = False, returnEndTimeAnalysis = False, returnGradeReferenceID = False, returnModifiedTime = False, returnScheduledStudentCourseRequestPercent = False, returnStartTimeAnalysis = False, returnStudentAutoSchedulerRunAnalysisID = False, returnStudentCourseRequestsConflictedThisRun = False, returnStudentCourseRequestsProcessedThisRun = False, returnStudentCourseRequestsScheduledThisRun = False, returnStudentsWithConflicts = False, returnStudentsWithOneConflict = False, returnStudentsWithThreeOrMoreConflicts = False, returnStudentsWithTwoConflicts = False, returnTotalAlternateStudentCourseRequests = False, returnTotalConflictedStudentCourseRequests = False, returnTotalScheduledStudentCourseRequests = False, returnTotalStudentCourseRequests = False, returnTotalStudents = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerRunAnalysisTotal/" + str(StudentAutoSchedulerRunAnalysisTotalID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentAutoSchedulerRunAnalysisTotal(EntityID = 1, setConflictPercent = None, setEndTimeAnalysis = None, setGradeReferenceID = None, setStartTimeAnalysis = None, setStudentAutoSchedulerRunAnalysisID = None, setStudentCourseRequestsConflictedThisRun = None, setStudentCourseRequestsProcessedThisRun = None, setStudentCourseRequestsScheduledThisRun = None, setStudentsWithConflicts = None, setStudentsWithOneConflict = None, setStudentsWithThreeOrMoreConflicts = None, setStudentsWithTwoConflicts = None, setTotalAlternateStudentCourseRequests = None, setTotalConflictedStudentCourseRequests = None, setTotalScheduledStudentCourseRequests = None, setTotalStudentCourseRequests = None, setTotalStudents = None, setRelationships = None, returnStudentAutoSchedulerRunAnalysisTotalID = True, returnConflictedStudentCourseRequestPercent = False, returnConflictPercent = False, returnCreatedTime = False, returnEndTimeAnalysis = False, returnGradeReferenceID = False, returnModifiedTime = False, returnScheduledStudentCourseRequestPercent = False, returnStartTimeAnalysis = False, returnStudentAutoSchedulerRunAnalysisID = False, returnStudentCourseRequestsConflictedThisRun = False, returnStudentCourseRequestsProcessedThisRun = False, returnStudentCourseRequestsScheduledThisRun = False, returnStudentsWithConflicts = False, returnStudentsWithOneConflict = False, returnStudentsWithThreeOrMoreConflicts = False, returnStudentsWithTwoConflicts = False, returnTotalAlternateStudentCourseRequests = False, returnTotalConflictedStudentCourseRequests = False, returnTotalScheduledStudentCourseRequests = False, returnTotalStudentCourseRequests = False, returnTotalStudents = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerRunAnalysisTotal/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentAutoSchedulerRunAnalysisTotal(StudentAutoSchedulerRunAnalysisTotalID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentAutoSchedulerSection(EntityID = 1, page = 1, pageSize = 100, returnStudentAutoSchedulerSectionID = True, returnAllowStudentsWithoutCategoryToBeAssigned = False, returnCreatedTime = False, returnDayRotationCode = False, returnDisplayPeriodCode = False, returnIsActive = False, returnMaximumStudentCount = False, returnMinimumStudentCount = False, returnModifiedTime = False, returnOptimalStudentCount = False, returnPeriodDaySummary = False, returnPrimaryMeetBuildingCode = False, returnPrimaryMeetRoomNumber = False, returnPrimaryMeetStaffNameLFM = False, returnSchedulingCategories = False, returnSchedulingTeams = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnStudentAutoSchedulerCourseID = False, returnTotalNumberScheduledThisRun = False, returnTotalScheduled = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentAutoSchedulerSection(StudentAutoSchedulerSectionID, EntityID = 1, returnStudentAutoSchedulerSectionID = True, returnAllowStudentsWithoutCategoryToBeAssigned = False, returnCreatedTime = False, returnDayRotationCode = False, returnDisplayPeriodCode = False, returnIsActive = False, returnMaximumStudentCount = False, returnMinimumStudentCount = False, returnModifiedTime = False, returnOptimalStudentCount = False, returnPeriodDaySummary = False, returnPrimaryMeetBuildingCode = False, returnPrimaryMeetRoomNumber = False, returnPrimaryMeetStaffNameLFM = False, returnSchedulingCategories = False, returnSchedulingTeams = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnStudentAutoSchedulerCourseID = False, returnTotalNumberScheduledThisRun = False, returnTotalScheduled = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerSection/" + str(StudentAutoSchedulerSectionID), verb = "get", return_params_list = return_params_list)

def modifyStudentAutoSchedulerSection(StudentAutoSchedulerSectionID, EntityID = 1, setAllowStudentsWithoutCategoryToBeAssigned = None, setDayRotationCode = None, setDisplayPeriodCode = None, setIsActive = None, setMaximumStudentCount = None, setMinimumStudentCount = None, setOptimalStudentCount = None, setPeriodDaySummary = None, setPrimaryMeetBuildingCode = None, setPrimaryMeetRoomNumber = None, setPrimaryMeetStaffNameLFM = None, setSchedulingCategories = None, setSchedulingTeams = None, setSectionCode = None, setSectionID = None, setSectionLengthCode = None, setStudentAutoSchedulerCourseID = None, setTotalNumberScheduledThisRun = None, setTotalScheduled = None, setRelationships = None, returnStudentAutoSchedulerSectionID = True, returnAllowStudentsWithoutCategoryToBeAssigned = False, returnCreatedTime = False, returnDayRotationCode = False, returnDisplayPeriodCode = False, returnIsActive = False, returnMaximumStudentCount = False, returnMinimumStudentCount = False, returnModifiedTime = False, returnOptimalStudentCount = False, returnPeriodDaySummary = False, returnPrimaryMeetBuildingCode = False, returnPrimaryMeetRoomNumber = False, returnPrimaryMeetStaffNameLFM = False, returnSchedulingCategories = False, returnSchedulingTeams = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnStudentAutoSchedulerCourseID = False, returnTotalNumberScheduledThisRun = False, returnTotalScheduled = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerSection/" + str(StudentAutoSchedulerSectionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentAutoSchedulerSection(EntityID = 1, setAllowStudentsWithoutCategoryToBeAssigned = None, setDayRotationCode = None, setDisplayPeriodCode = None, setIsActive = None, setMaximumStudentCount = None, setMinimumStudentCount = None, setOptimalStudentCount = None, setPeriodDaySummary = None, setPrimaryMeetBuildingCode = None, setPrimaryMeetRoomNumber = None, setPrimaryMeetStaffNameLFM = None, setSchedulingCategories = None, setSchedulingTeams = None, setSectionCode = None, setSectionID = None, setSectionLengthCode = None, setStudentAutoSchedulerCourseID = None, setTotalNumberScheduledThisRun = None, setTotalScheduled = None, setRelationships = None, returnStudentAutoSchedulerSectionID = True, returnAllowStudentsWithoutCategoryToBeAssigned = False, returnCreatedTime = False, returnDayRotationCode = False, returnDisplayPeriodCode = False, returnIsActive = False, returnMaximumStudentCount = False, returnMinimumStudentCount = False, returnModifiedTime = False, returnOptimalStudentCount = False, returnPeriodDaySummary = False, returnPrimaryMeetBuildingCode = False, returnPrimaryMeetRoomNumber = False, returnPrimaryMeetStaffNameLFM = False, returnSchedulingCategories = False, returnSchedulingTeams = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnStudentAutoSchedulerCourseID = False, returnTotalNumberScheduledThisRun = False, returnTotalScheduled = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerSection/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentAutoSchedulerSection(StudentAutoSchedulerSectionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentAutoSchedulerStudent(EntityID = 1, page = 1, pageSize = 100, returnStudentAutoSchedulerStudentID = True, returnBirthDate = False, returnCalendarCode = False, returnCreatedTime = False, returnEndTimeAnalysis = False, returnFullName = False, returnGenderCode = False, returnGrade = False, returnGradeReferenceID = False, returnHasConflict = False, returnModifiedTime = False, returnNumberOfConflictedStudentCourseRequests = False, returnNumberOfScheduledStudentCourseRequests = False, returnProcessedDuringThisSchedulingRun = False, returnRandomSchedulingInteger = False, returnRawPermutations = False, returnSchedulesConsidered = False, returnSchedulingCategories = False, returnSchedulingTeamCode = False, returnSequenceNumber = False, returnStartTimeAnalysis = False, returnStudentAutoSchedulerRunAnalysisID = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnTotalNumberOfAlternateStudentCourseRequests = False, returnTotalNumberOfStudentCourseRequests = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerStudent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentAutoSchedulerStudent(StudentAutoSchedulerStudentID, EntityID = 1, returnStudentAutoSchedulerStudentID = True, returnBirthDate = False, returnCalendarCode = False, returnCreatedTime = False, returnEndTimeAnalysis = False, returnFullName = False, returnGenderCode = False, returnGrade = False, returnGradeReferenceID = False, returnHasConflict = False, returnModifiedTime = False, returnNumberOfConflictedStudentCourseRequests = False, returnNumberOfScheduledStudentCourseRequests = False, returnProcessedDuringThisSchedulingRun = False, returnRandomSchedulingInteger = False, returnRawPermutations = False, returnSchedulesConsidered = False, returnSchedulingCategories = False, returnSchedulingTeamCode = False, returnSequenceNumber = False, returnStartTimeAnalysis = False, returnStudentAutoSchedulerRunAnalysisID = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnTotalNumberOfAlternateStudentCourseRequests = False, returnTotalNumberOfStudentCourseRequests = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerStudent/" + str(StudentAutoSchedulerStudentID), verb = "get", return_params_list = return_params_list)

def modifyStudentAutoSchedulerStudent(StudentAutoSchedulerStudentID, EntityID = 1, setBirthDate = None, setCalendarCode = None, setEndTimeAnalysis = None, setFullName = None, setGenderCode = None, setGrade = None, setGradeReferenceID = None, setHasConflict = None, setNumberOfConflictedStudentCourseRequests = None, setNumberOfScheduledStudentCourseRequests = None, setRandomSchedulingInteger = None, setRawPermutations = None, setSchedulesConsidered = None, setSchedulingCategories = None, setSchedulingTeamCode = None, setSequenceNumber = None, setStartTimeAnalysis = None, setStudentAutoSchedulerRunAnalysisID = None, setStudentID = None, setStudentNumber = None, setStudentTypeCode = None, setTotalNumberOfAlternateStudentCourseRequests = None, setTotalNumberOfStudentCourseRequests = None, setRelationships = None, returnStudentAutoSchedulerStudentID = True, returnBirthDate = False, returnCalendarCode = False, returnCreatedTime = False, returnEndTimeAnalysis = False, returnFullName = False, returnGenderCode = False, returnGrade = False, returnGradeReferenceID = False, returnHasConflict = False, returnModifiedTime = False, returnNumberOfConflictedStudentCourseRequests = False, returnNumberOfScheduledStudentCourseRequests = False, returnProcessedDuringThisSchedulingRun = False, returnRandomSchedulingInteger = False, returnRawPermutations = False, returnSchedulesConsidered = False, returnSchedulingCategories = False, returnSchedulingTeamCode = False, returnSequenceNumber = False, returnStartTimeAnalysis = False, returnStudentAutoSchedulerRunAnalysisID = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnTotalNumberOfAlternateStudentCourseRequests = False, returnTotalNumberOfStudentCourseRequests = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerStudent/" + str(StudentAutoSchedulerStudentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentAutoSchedulerStudent(EntityID = 1, setBirthDate = None, setCalendarCode = None, setEndTimeAnalysis = None, setFullName = None, setGenderCode = None, setGrade = None, setGradeReferenceID = None, setHasConflict = None, setNumberOfConflictedStudentCourseRequests = None, setNumberOfScheduledStudentCourseRequests = None, setRandomSchedulingInteger = None, setRawPermutations = None, setSchedulesConsidered = None, setSchedulingCategories = None, setSchedulingTeamCode = None, setSequenceNumber = None, setStartTimeAnalysis = None, setStudentAutoSchedulerRunAnalysisID = None, setStudentID = None, setStudentNumber = None, setStudentTypeCode = None, setTotalNumberOfAlternateStudentCourseRequests = None, setTotalNumberOfStudentCourseRequests = None, setRelationships = None, returnStudentAutoSchedulerStudentID = True, returnBirthDate = False, returnCalendarCode = False, returnCreatedTime = False, returnEndTimeAnalysis = False, returnFullName = False, returnGenderCode = False, returnGrade = False, returnGradeReferenceID = False, returnHasConflict = False, returnModifiedTime = False, returnNumberOfConflictedStudentCourseRequests = False, returnNumberOfScheduledStudentCourseRequests = False, returnProcessedDuringThisSchedulingRun = False, returnRandomSchedulingInteger = False, returnRawPermutations = False, returnSchedulesConsidered = False, returnSchedulingCategories = False, returnSchedulingTeamCode = False, returnSequenceNumber = False, returnStartTimeAnalysis = False, returnStudentAutoSchedulerRunAnalysisID = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnTotalNumberOfAlternateStudentCourseRequests = False, returnTotalNumberOfStudentCourseRequests = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerStudent/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentAutoSchedulerStudent(StudentAutoSchedulerStudentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentAutoSchedulerStudentCourseRequest(EntityID = 1, page = 1, pageSize = 100, returnStudentAutoSchedulerStudentCourseRequestID = True, returnCourseConflictReason = False, returnCourseConflictReasonCode = False, returnCourseConflictReasonText = False, returnCreatedTime = False, returnEntityIDRequestedFrom = False, returnEntityRequestedFromEntityCode = False, returnHasRelatedStudentAutoSchedulerStudentCourseRequestSections = False, returnInitialSequenceNumber = False, returnIsAlternate = False, returnModifiedTime = False, returnSchedulingMethodCode = False, returnSectionLengthSubsetsRequested = False, returnSectionLengthSubsetSummary = False, returnSequenceNumber = False, returnStudentAutoSchedulerCourseID = False, returnStudentAutoSchedulerSectionID = False, returnStudentAutoSchedulerStudentID = False, returnStudentCourseRequestID = False, returnUpdatedDuringThisSchedulingRun = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerStudentCourseRequest/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentAutoSchedulerStudentCourseRequest(StudentAutoSchedulerStudentCourseRequestID, EntityID = 1, returnStudentAutoSchedulerStudentCourseRequestID = True, returnCourseConflictReason = False, returnCourseConflictReasonCode = False, returnCourseConflictReasonText = False, returnCreatedTime = False, returnEntityIDRequestedFrom = False, returnEntityRequestedFromEntityCode = False, returnHasRelatedStudentAutoSchedulerStudentCourseRequestSections = False, returnInitialSequenceNumber = False, returnIsAlternate = False, returnModifiedTime = False, returnSchedulingMethodCode = False, returnSectionLengthSubsetsRequested = False, returnSectionLengthSubsetSummary = False, returnSequenceNumber = False, returnStudentAutoSchedulerCourseID = False, returnStudentAutoSchedulerSectionID = False, returnStudentAutoSchedulerStudentID = False, returnStudentCourseRequestID = False, returnUpdatedDuringThisSchedulingRun = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerStudentCourseRequest/" + str(StudentAutoSchedulerStudentCourseRequestID), verb = "get", return_params_list = return_params_list)

def modifyStudentAutoSchedulerStudentCourseRequest(StudentAutoSchedulerStudentCourseRequestID, EntityID = 1, setCourseConflictReason = None, setCourseConflictReasonCode = None, setCourseConflictReasonText = None, setEntityIDRequestedFrom = None, setEntityRequestedFromEntityCode = None, setInitialSequenceNumber = None, setIsAlternate = None, setSchedulingMethodCode = None, setSectionLengthSubsetsRequested = None, setSectionLengthSubsetSummary = None, setSequenceNumber = None, setStudentAutoSchedulerCourseID = None, setStudentAutoSchedulerSectionID = None, setStudentAutoSchedulerStudentID = None, setStudentCourseRequestID = None, setRelationships = None, returnStudentAutoSchedulerStudentCourseRequestID = True, returnCourseConflictReason = False, returnCourseConflictReasonCode = False, returnCourseConflictReasonText = False, returnCreatedTime = False, returnEntityIDRequestedFrom = False, returnEntityRequestedFromEntityCode = False, returnHasRelatedStudentAutoSchedulerStudentCourseRequestSections = False, returnInitialSequenceNumber = False, returnIsAlternate = False, returnModifiedTime = False, returnSchedulingMethodCode = False, returnSectionLengthSubsetsRequested = False, returnSectionLengthSubsetSummary = False, returnSequenceNumber = False, returnStudentAutoSchedulerCourseID = False, returnStudentAutoSchedulerSectionID = False, returnStudentAutoSchedulerStudentID = False, returnStudentCourseRequestID = False, returnUpdatedDuringThisSchedulingRun = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerStudentCourseRequest/" + str(StudentAutoSchedulerStudentCourseRequestID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentAutoSchedulerStudentCourseRequest(EntityID = 1, setCourseConflictReason = None, setCourseConflictReasonCode = None, setCourseConflictReasonText = None, setEntityIDRequestedFrom = None, setEntityRequestedFromEntityCode = None, setInitialSequenceNumber = None, setIsAlternate = None, setSchedulingMethodCode = None, setSectionLengthSubsetsRequested = None, setSectionLengthSubsetSummary = None, setSequenceNumber = None, setStudentAutoSchedulerCourseID = None, setStudentAutoSchedulerSectionID = None, setStudentAutoSchedulerStudentID = None, setStudentCourseRequestID = None, setRelationships = None, returnStudentAutoSchedulerStudentCourseRequestID = True, returnCourseConflictReason = False, returnCourseConflictReasonCode = False, returnCourseConflictReasonText = False, returnCreatedTime = False, returnEntityIDRequestedFrom = False, returnEntityRequestedFromEntityCode = False, returnHasRelatedStudentAutoSchedulerStudentCourseRequestSections = False, returnInitialSequenceNumber = False, returnIsAlternate = False, returnModifiedTime = False, returnSchedulingMethodCode = False, returnSectionLengthSubsetsRequested = False, returnSectionLengthSubsetSummary = False, returnSequenceNumber = False, returnStudentAutoSchedulerCourseID = False, returnStudentAutoSchedulerSectionID = False, returnStudentAutoSchedulerStudentID = False, returnStudentCourseRequestID = False, returnUpdatedDuringThisSchedulingRun = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerStudentCourseRequest/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentAutoSchedulerStudentCourseRequest(StudentAutoSchedulerStudentCourseRequestID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentAutoSchedulerStudentCourseRequestSection(EntityID = 1, page = 1, pageSize = 100, returnStudentAutoSchedulerStudentCourseRequestSectionID = True, returnAssignedToThisSection = False, returnCreatedTime = False, returnEligibleToEnrollInSection = False, returnModifiedTime = False, returnPeriodDaySummary = False, returnSeatsRemaining = False, returnSequenceNumber = False, returnStudentAutoSchedulerSectionID = False, returnStudentAutoSchedulerStudentCourseRequestID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerStudentCourseRequestSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentAutoSchedulerStudentCourseRequestSection(StudentAutoSchedulerStudentCourseRequestSectionID, EntityID = 1, returnStudentAutoSchedulerStudentCourseRequestSectionID = True, returnAssignedToThisSection = False, returnCreatedTime = False, returnEligibleToEnrollInSection = False, returnModifiedTime = False, returnPeriodDaySummary = False, returnSeatsRemaining = False, returnSequenceNumber = False, returnStudentAutoSchedulerSectionID = False, returnStudentAutoSchedulerStudentCourseRequestID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerStudentCourseRequestSection/" + str(StudentAutoSchedulerStudentCourseRequestSectionID), verb = "get", return_params_list = return_params_list)

def modifyStudentAutoSchedulerStudentCourseRequestSection(StudentAutoSchedulerStudentCourseRequestSectionID, EntityID = 1, setPeriodDaySummary = None, setSeatsRemaining = None, setSequenceNumber = None, setStudentAutoSchedulerSectionID = None, setStudentAutoSchedulerStudentCourseRequestID = None, setRelationships = None, returnStudentAutoSchedulerStudentCourseRequestSectionID = True, returnAssignedToThisSection = False, returnCreatedTime = False, returnEligibleToEnrollInSection = False, returnModifiedTime = False, returnPeriodDaySummary = False, returnSeatsRemaining = False, returnSequenceNumber = False, returnStudentAutoSchedulerSectionID = False, returnStudentAutoSchedulerStudentCourseRequestID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerStudentCourseRequestSection/" + str(StudentAutoSchedulerStudentCourseRequestSectionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentAutoSchedulerStudentCourseRequestSection(EntityID = 1, setPeriodDaySummary = None, setSeatsRemaining = None, setSequenceNumber = None, setStudentAutoSchedulerSectionID = None, setStudentAutoSchedulerStudentCourseRequestID = None, setRelationships = None, returnStudentAutoSchedulerStudentCourseRequestSectionID = True, returnAssignedToThisSection = False, returnCreatedTime = False, returnEligibleToEnrollInSection = False, returnModifiedTime = False, returnPeriodDaySummary = False, returnSeatsRemaining = False, returnSequenceNumber = False, returnStudentAutoSchedulerSectionID = False, returnStudentAutoSchedulerStudentCourseRequestID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerStudentCourseRequestSection/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentAutoSchedulerStudentCourseRequestSection(StudentAutoSchedulerStudentCourseRequestSectionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentAutoSchedulerStudentCourseRequestSectionDetail(EntityID = 1, page = 1, pageSize = 100, returnStudentAutoSchedulerStudentCourseRequestSectionDetailID = True, returnCreatedTime = False, returnModifiedTime = False, returnSectionConflictReason = False, returnSectionConflictReasonCode = False, returnSectionConflictReasonText = False, returnStudentAutoSchedulerStudentCourseRequestSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerStudentCourseRequestSectionDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentAutoSchedulerStudentCourseRequestSectionDetail(StudentAutoSchedulerStudentCourseRequestSectionDetailID, EntityID = 1, returnStudentAutoSchedulerStudentCourseRequestSectionDetailID = True, returnCreatedTime = False, returnModifiedTime = False, returnSectionConflictReason = False, returnSectionConflictReasonCode = False, returnSectionConflictReasonText = False, returnStudentAutoSchedulerStudentCourseRequestSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerStudentCourseRequestSectionDetail/" + str(StudentAutoSchedulerStudentCourseRequestSectionDetailID), verb = "get", return_params_list = return_params_list)

def modifyStudentAutoSchedulerStudentCourseRequestSectionDetail(StudentAutoSchedulerStudentCourseRequestSectionDetailID, EntityID = 1, setSectionConflictReason = None, setSectionConflictReasonCode = None, setSectionConflictReasonText = None, setStudentAutoSchedulerStudentCourseRequestSectionID = None, setRelationships = None, returnStudentAutoSchedulerStudentCourseRequestSectionDetailID = True, returnCreatedTime = False, returnModifiedTime = False, returnSectionConflictReason = False, returnSectionConflictReasonCode = False, returnSectionConflictReasonText = False, returnStudentAutoSchedulerStudentCourseRequestSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerStudentCourseRequestSectionDetail/" + str(StudentAutoSchedulerStudentCourseRequestSectionDetailID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentAutoSchedulerStudentCourseRequestSectionDetail(EntityID = 1, setSectionConflictReason = None, setSectionConflictReasonCode = None, setSectionConflictReasonText = None, setStudentAutoSchedulerStudentCourseRequestSectionID = None, setRelationships = None, returnStudentAutoSchedulerStudentCourseRequestSectionDetailID = True, returnCreatedTime = False, returnModifiedTime = False, returnSectionConflictReason = False, returnSectionConflictReasonCode = False, returnSectionConflictReasonText = False, returnStudentAutoSchedulerStudentCourseRequestSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentAutoSchedulerStudentCourseRequestSectionDetail/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentAutoSchedulerStudentCourseRequestSectionDetail(StudentAutoSchedulerStudentCourseRequestSectionDetailID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentCourseRequest(EntityID = 1, page = 1, pageSize = 100, returnStudentCourseRequestID = True, returnAlternateRank = False, returnCountsAgainstRequestLimit = False, returnCourseConflict = False, returnCourseEntityOfferedToID = False, returnCourseID = False, returnCourseNotScheduled = False, returnCourseNotScheduledAndIsRequestedFromViewingEntity = False, returnCourseRequested = False, returnCourseScheduled = False, returnCourseScheduledAndAllTransactionsCountTowardsViewingEntity = False, returnCourseScheduledAndAllTransactionsCountTowardsViewingEntityAndCourseIsNotDropOrTransfer = False, returnCourseScheduledAndCountsTowardsViewingEntity = False, returnCourseScheduledAndInProgress = False, returnCourseScheduledAndInProgressAndIsEffectiveToViewingEntity = False, returnCourseScheduledAndIsBeforeOrInProgress = False, returnCourseScheduledAndIsBeforeOrInProgressAndNotHasAtleastOneTransactionNotCountTowardsViewingEntity = False, returnCourseScheduledAndIsRequestedFromOfferingEntityAndAllTransactionsCountTowardsViewingEntity = False, returnCreatedTime = False, returnDisplayToViewingEntity = False, returnEarnedCreditsPossibleAnticipated = False, returnEarnedCreditsRequested = False, returnEntityIDRequestedFrom = False, returnIsAlternate = False, returnModifiedTime = False, returnPrerequisiteMet = False, returnRequestedFromOfferingEntity = False, returnRequestedFromViewingEntity = False, returnRequestSource = False, returnRequestSourceCode = False, returnRequestStatus = False, returnRequestStatusCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSectionLengthSubsetSummary = False, returnStudentCourseRequestIDAlternateFor = False, returnStudentCourseRequestIDHash = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionIDHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentCourseRequest/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentCourseRequest(StudentCourseRequestID, EntityID = 1, returnStudentCourseRequestID = True, returnAlternateRank = False, returnCountsAgainstRequestLimit = False, returnCourseConflict = False, returnCourseEntityOfferedToID = False, returnCourseID = False, returnCourseNotScheduled = False, returnCourseNotScheduledAndIsRequestedFromViewingEntity = False, returnCourseRequested = False, returnCourseScheduled = False, returnCourseScheduledAndAllTransactionsCountTowardsViewingEntity = False, returnCourseScheduledAndAllTransactionsCountTowardsViewingEntityAndCourseIsNotDropOrTransfer = False, returnCourseScheduledAndCountsTowardsViewingEntity = False, returnCourseScheduledAndInProgress = False, returnCourseScheduledAndInProgressAndIsEffectiveToViewingEntity = False, returnCourseScheduledAndIsBeforeOrInProgress = False, returnCourseScheduledAndIsBeforeOrInProgressAndNotHasAtleastOneTransactionNotCountTowardsViewingEntity = False, returnCourseScheduledAndIsRequestedFromOfferingEntityAndAllTransactionsCountTowardsViewingEntity = False, returnCreatedTime = False, returnDisplayToViewingEntity = False, returnEarnedCreditsPossibleAnticipated = False, returnEarnedCreditsRequested = False, returnEntityIDRequestedFrom = False, returnIsAlternate = False, returnModifiedTime = False, returnPrerequisiteMet = False, returnRequestedFromOfferingEntity = False, returnRequestedFromViewingEntity = False, returnRequestSource = False, returnRequestSourceCode = False, returnRequestStatus = False, returnRequestStatusCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSectionLengthSubsetSummary = False, returnStudentCourseRequestIDAlternateFor = False, returnStudentCourseRequestIDHash = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionIDHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentCourseRequest/" + str(StudentCourseRequestID), verb = "get", return_params_list = return_params_list)

def modifyStudentCourseRequest(StudentCourseRequestID, EntityID = 1, setAlternateRank = None, setCourseEntityOfferedToID = None, setCourseID = None, setEntityIDRequestedFrom = None, setIsAlternate = None, setRequestSource = None, setRequestSourceCode = None, setRequestStatus = None, setRequestStatusCode = None, setSchedulingMethod = None, setSchedulingMethodCode = None, setSectionLengthSubsetSummary = None, setStudentCourseRequestIDAlternateFor = None, setStudentID = None, setStudentSectionID = None, setRelationships = None, returnStudentCourseRequestID = True, returnAlternateRank = False, returnCountsAgainstRequestLimit = False, returnCourseConflict = False, returnCourseEntityOfferedToID = False, returnCourseID = False, returnCourseNotScheduled = False, returnCourseNotScheduledAndIsRequestedFromViewingEntity = False, returnCourseRequested = False, returnCourseScheduled = False, returnCourseScheduledAndAllTransactionsCountTowardsViewingEntity = False, returnCourseScheduledAndAllTransactionsCountTowardsViewingEntityAndCourseIsNotDropOrTransfer = False, returnCourseScheduledAndCountsTowardsViewingEntity = False, returnCourseScheduledAndInProgress = False, returnCourseScheduledAndInProgressAndIsEffectiveToViewingEntity = False, returnCourseScheduledAndIsBeforeOrInProgress = False, returnCourseScheduledAndIsBeforeOrInProgressAndNotHasAtleastOneTransactionNotCountTowardsViewingEntity = False, returnCourseScheduledAndIsRequestedFromOfferingEntityAndAllTransactionsCountTowardsViewingEntity = False, returnCreatedTime = False, returnDisplayToViewingEntity = False, returnEarnedCreditsPossibleAnticipated = False, returnEarnedCreditsRequested = False, returnEntityIDRequestedFrom = False, returnIsAlternate = False, returnModifiedTime = False, returnPrerequisiteMet = False, returnRequestedFromOfferingEntity = False, returnRequestedFromViewingEntity = False, returnRequestSource = False, returnRequestSourceCode = False, returnRequestStatus = False, returnRequestStatusCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSectionLengthSubsetSummary = False, returnStudentCourseRequestIDAlternateFor = False, returnStudentCourseRequestIDHash = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionIDHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentCourseRequest/" + str(StudentCourseRequestID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentCourseRequest(EntityID = 1, setAlternateRank = None, setCourseEntityOfferedToID = None, setCourseID = None, setEntityIDRequestedFrom = None, setIsAlternate = None, setRequestSource = None, setRequestSourceCode = None, setRequestStatus = None, setRequestStatusCode = None, setSchedulingMethod = None, setSchedulingMethodCode = None, setSectionLengthSubsetSummary = None, setStudentCourseRequestIDAlternateFor = None, setStudentID = None, setStudentSectionID = None, setRelationships = None, returnStudentCourseRequestID = True, returnAlternateRank = False, returnCountsAgainstRequestLimit = False, returnCourseConflict = False, returnCourseEntityOfferedToID = False, returnCourseID = False, returnCourseNotScheduled = False, returnCourseNotScheduledAndIsRequestedFromViewingEntity = False, returnCourseRequested = False, returnCourseScheduled = False, returnCourseScheduledAndAllTransactionsCountTowardsViewingEntity = False, returnCourseScheduledAndAllTransactionsCountTowardsViewingEntityAndCourseIsNotDropOrTransfer = False, returnCourseScheduledAndCountsTowardsViewingEntity = False, returnCourseScheduledAndInProgress = False, returnCourseScheduledAndInProgressAndIsEffectiveToViewingEntity = False, returnCourseScheduledAndIsBeforeOrInProgress = False, returnCourseScheduledAndIsBeforeOrInProgressAndNotHasAtleastOneTransactionNotCountTowardsViewingEntity = False, returnCourseScheduledAndIsRequestedFromOfferingEntityAndAllTransactionsCountTowardsViewingEntity = False, returnCreatedTime = False, returnDisplayToViewingEntity = False, returnEarnedCreditsPossibleAnticipated = False, returnEarnedCreditsRequested = False, returnEntityIDRequestedFrom = False, returnIsAlternate = False, returnModifiedTime = False, returnPrerequisiteMet = False, returnRequestedFromOfferingEntity = False, returnRequestedFromViewingEntity = False, returnRequestSource = False, returnRequestSourceCode = False, returnRequestStatus = False, returnRequestStatusCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSectionLengthSubsetSummary = False, returnStudentCourseRequestIDAlternateFor = False, returnStudentCourseRequestIDHash = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionIDHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentCourseRequest/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentCourseRequest(StudentCourseRequestID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentCourseRequestSectionLengthSubset(EntityID = 1, page = 1, pageSize = 100, returnStudentCourseRequestSectionLengthSubsetID = True, returnCreatedTime = False, returnModifiedTime = False, returnSectionLengthSubsetID = False, returnStudentCourseRequestID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentCourseRequestSectionLengthSubset/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentCourseRequestSectionLengthSubset(StudentCourseRequestSectionLengthSubsetID, EntityID = 1, returnStudentCourseRequestSectionLengthSubsetID = True, returnCreatedTime = False, returnModifiedTime = False, returnSectionLengthSubsetID = False, returnStudentCourseRequestID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentCourseRequestSectionLengthSubset/" + str(StudentCourseRequestSectionLengthSubsetID), verb = "get", return_params_list = return_params_list)

def modifyStudentCourseRequestSectionLengthSubset(StudentCourseRequestSectionLengthSubsetID, EntityID = 1, setSectionLengthSubsetID = None, setStudentCourseRequestID = None, setRelationships = None, returnStudentCourseRequestSectionLengthSubsetID = True, returnCreatedTime = False, returnModifiedTime = False, returnSectionLengthSubsetID = False, returnStudentCourseRequestID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentCourseRequestSectionLengthSubset/" + str(StudentCourseRequestSectionLengthSubsetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentCourseRequestSectionLengthSubset(EntityID = 1, setSectionLengthSubsetID = None, setStudentCourseRequestID = None, setRelationships = None, returnStudentCourseRequestSectionLengthSubsetID = True, returnCreatedTime = False, returnModifiedTime = False, returnSectionLengthSubsetID = False, returnStudentCourseRequestID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentCourseRequestSectionLengthSubset/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentCourseRequestSectionLengthSubset(StudentCourseRequestSectionLengthSubsetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentEntityYearSchedulingCategory(EntityID = 1, page = 1, pageSize = 100, returnStudentEntityYearSchedulingCategoryID = True, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingCategoryID = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentEntityYearSchedulingCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentEntityYearSchedulingCategory(StudentEntityYearSchedulingCategoryID, EntityID = 1, returnStudentEntityYearSchedulingCategoryID = True, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingCategoryID = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentEntityYearSchedulingCategory/" + str(StudentEntityYearSchedulingCategoryID), verb = "get", return_params_list = return_params_list)

def modifyStudentEntityYearSchedulingCategory(StudentEntityYearSchedulingCategoryID, EntityID = 1, setSchedulingCategoryID = None, setStudentEntityYearID = None, setRelationships = None, returnStudentEntityYearSchedulingCategoryID = True, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingCategoryID = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentEntityYearSchedulingCategory/" + str(StudentEntityYearSchedulingCategoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentEntityYearSchedulingCategory(EntityID = 1, setSchedulingCategoryID = None, setStudentEntityYearID = None, setRelationships = None, returnStudentEntityYearSchedulingCategoryID = True, returnCreatedTime = False, returnModifiedTime = False, returnSchedulingCategoryID = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentEntityYearSchedulingCategory/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentEntityYearSchedulingCategory(StudentEntityYearSchedulingCategoryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentSection(EntityID = 1, page = 1, pageSize = 100, returnStudentSectionID = True, returnAcademicHistoryHash = False, returnActiveStudentGroups = False, returnAllTransactionsCountTowardsViewingEntity = False, returnAssignmentDueDateAttendance = False, returnCountsForViewingEntity = False, returnCourseOrTransferDescription = False, returnCreatedTime = False, returnDisplayLinkedStudentSection = False, returnDisplayToViewingEntity = False, returnEarnedCreditAttempted = False, returnEarnedCreditOverride = False, returnEarnedCredits = False, returnEarnedCreditsPossible = False, returnEndDate = False, returnEntityIDCourse = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLink = False, returnExistsStudentSectionGPAMethods = False, returnFailedCredits = False, returnFilteredGradedAssignmentCount = False, returnFilteredMissingAssignmentCount = False, returnFilteredUnGradedAssignmentCount = False, returnGradebookSortCode = False, returnGradebookStudentNameToUse = False, returnGradeReferenceID = False, returnHasAtLeastOneCrossEntityStudentSectionTransaction = False, returnHasAtleastOneTransactionNotCountTowardsViewingEntity = False, returnHasLinkingConflicts = False, returnHasStudentGradingScaleGroupForGradingPeriodGradeBucket = False, returnHasStudentSectionNoteForCurrentUser = False, returnInProgress = False, returnInProgressAndIsEffectiveForViewingEntity = False, returnIsActiveAsOfDate = False, returnIsActiveForTodayOrForSectionStartOrEnd = False, returnIsAvailableForAssignmentStudentGroup = False, returnIsBeforeOrInProgress = False, returnIsBeforeOrInProgressAndNotHasAtleastOneTransactionNotCountTowardsViewingEntity = False, returnIsCurrentStudentSection = False, returnIsEffectiveForViewingEntity = False, returnIsFlaggedAsMissingAssignmentCount = False, returnIsForCurrentSchoolYear = False, returnIsStudentSectionScheduledToMeet = False, returnIsTransferCourse = False, returnIsTSAProficient = False, returnIsWorkInProgress = False, returnLastStudentSectionTransactionConsideredDropped = False, returnLinkedStudentSectionsEarnedCredit = False, returnLinkedStudentSectionsEarnedCreditAttempted = False, returnLinkedStudentSectionsFailedCredit = False, returnMissingAssignmentCount = False, returnModifiedTime = False, returnMultipleTransactions = False, returnRenderTransferGradesRowButton = False, returnRequestedFromOfferingEntityAndAllTransactionsCountTowardsViewingEntity = False, returnSchoolYearIDCourse = False, returnSectionID = False, returnSectionLengthSubsetSummary = False, returnStartDate = False, returnStatus = False, returnStatusCode = False, returnStatusString = False, returnStudentID = False, returnStudentSectionCode = False, returnStudentSectionIDHash = False, returnStudentSectionLink = False, returnStudentSectionMNID = False, returnStudentSectionNoteCountForCurrentUser = False, returnTotalDaysAbsent = False, returnTotalDaysExcused = False, returnTotalDaysOther = False, returnTotalDaysTardy = False, returnTotalDaysUnexcused = False, returnTotalEarnedCreditOverride = False, returnTotalFailedCreditOverride = False, returnTransactionCountsForViewingEntity = False, returnTransferCourseName = False, returnUnscoredPastDueAssignmentCount = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditTotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentSection(StudentSectionID, EntityID = 1, returnStudentSectionID = True, returnAcademicHistoryHash = False, returnActiveStudentGroups = False, returnAllTransactionsCountTowardsViewingEntity = False, returnAssignmentDueDateAttendance = False, returnCountsForViewingEntity = False, returnCourseOrTransferDescription = False, returnCreatedTime = False, returnDisplayLinkedStudentSection = False, returnDisplayToViewingEntity = False, returnEarnedCreditAttempted = False, returnEarnedCreditOverride = False, returnEarnedCredits = False, returnEarnedCreditsPossible = False, returnEndDate = False, returnEntityIDCourse = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLink = False, returnExistsStudentSectionGPAMethods = False, returnFailedCredits = False, returnFilteredGradedAssignmentCount = False, returnFilteredMissingAssignmentCount = False, returnFilteredUnGradedAssignmentCount = False, returnGradebookSortCode = False, returnGradebookStudentNameToUse = False, returnGradeReferenceID = False, returnHasAtLeastOneCrossEntityStudentSectionTransaction = False, returnHasAtleastOneTransactionNotCountTowardsViewingEntity = False, returnHasLinkingConflicts = False, returnHasStudentGradingScaleGroupForGradingPeriodGradeBucket = False, returnHasStudentSectionNoteForCurrentUser = False, returnInProgress = False, returnInProgressAndIsEffectiveForViewingEntity = False, returnIsActiveAsOfDate = False, returnIsActiveForTodayOrForSectionStartOrEnd = False, returnIsAvailableForAssignmentStudentGroup = False, returnIsBeforeOrInProgress = False, returnIsBeforeOrInProgressAndNotHasAtleastOneTransactionNotCountTowardsViewingEntity = False, returnIsCurrentStudentSection = False, returnIsEffectiveForViewingEntity = False, returnIsFlaggedAsMissingAssignmentCount = False, returnIsForCurrentSchoolYear = False, returnIsStudentSectionScheduledToMeet = False, returnIsTransferCourse = False, returnIsTSAProficient = False, returnIsWorkInProgress = False, returnLastStudentSectionTransactionConsideredDropped = False, returnLinkedStudentSectionsEarnedCredit = False, returnLinkedStudentSectionsEarnedCreditAttempted = False, returnLinkedStudentSectionsFailedCredit = False, returnMissingAssignmentCount = False, returnModifiedTime = False, returnMultipleTransactions = False, returnRenderTransferGradesRowButton = False, returnRequestedFromOfferingEntityAndAllTransactionsCountTowardsViewingEntity = False, returnSchoolYearIDCourse = False, returnSectionID = False, returnSectionLengthSubsetSummary = False, returnStartDate = False, returnStatus = False, returnStatusCode = False, returnStatusString = False, returnStudentID = False, returnStudentSectionCode = False, returnStudentSectionIDHash = False, returnStudentSectionLink = False, returnStudentSectionMNID = False, returnStudentSectionNoteCountForCurrentUser = False, returnTotalDaysAbsent = False, returnTotalDaysExcused = False, returnTotalDaysOther = False, returnTotalDaysTardy = False, returnTotalDaysUnexcused = False, returnTotalEarnedCreditOverride = False, returnTotalFailedCreditOverride = False, returnTransactionCountsForViewingEntity = False, returnTransferCourseName = False, returnUnscoredPastDueAssignmentCount = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditTotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentSection/" + str(StudentSectionID), verb = "get", return_params_list = return_params_list)

def modifyStudentSection(StudentSectionID, EntityID = 1, setEarnedCreditOverride = None, setEntityIDCourse = None, setExcludeFromReportCardsAndTranscripts = None, setExcludeFromStudentSectionLink = None, setGradeReferenceID = None, setIsTransferCourse = None, setIsTSAProficient = None, setIsWorkInProgress = None, setSchoolYearIDCourse = None, setSectionID = None, setSectionLengthSubsetSummary = None, setStudentID = None, setStudentSectionLink = None, setTotalEarnedCreditOverride = None, setTotalFailedCreditOverride = None, setTransferCourseName = None, setUseEarnedCreditOverride = None, setUseEarnedCreditTotalOverride = None, setRelationships = None, returnStudentSectionID = True, returnAcademicHistoryHash = False, returnActiveStudentGroups = False, returnAllTransactionsCountTowardsViewingEntity = False, returnAssignmentDueDateAttendance = False, returnCountsForViewingEntity = False, returnCourseOrTransferDescription = False, returnCreatedTime = False, returnDisplayLinkedStudentSection = False, returnDisplayToViewingEntity = False, returnEarnedCreditAttempted = False, returnEarnedCreditOverride = False, returnEarnedCredits = False, returnEarnedCreditsPossible = False, returnEndDate = False, returnEntityIDCourse = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLink = False, returnExistsStudentSectionGPAMethods = False, returnFailedCredits = False, returnFilteredGradedAssignmentCount = False, returnFilteredMissingAssignmentCount = False, returnFilteredUnGradedAssignmentCount = False, returnGradebookSortCode = False, returnGradebookStudentNameToUse = False, returnGradeReferenceID = False, returnHasAtLeastOneCrossEntityStudentSectionTransaction = False, returnHasAtleastOneTransactionNotCountTowardsViewingEntity = False, returnHasLinkingConflicts = False, returnHasStudentGradingScaleGroupForGradingPeriodGradeBucket = False, returnHasStudentSectionNoteForCurrentUser = False, returnInProgress = False, returnInProgressAndIsEffectiveForViewingEntity = False, returnIsActiveAsOfDate = False, returnIsActiveForTodayOrForSectionStartOrEnd = False, returnIsAvailableForAssignmentStudentGroup = False, returnIsBeforeOrInProgress = False, returnIsBeforeOrInProgressAndNotHasAtleastOneTransactionNotCountTowardsViewingEntity = False, returnIsCurrentStudentSection = False, returnIsEffectiveForViewingEntity = False, returnIsFlaggedAsMissingAssignmentCount = False, returnIsForCurrentSchoolYear = False, returnIsStudentSectionScheduledToMeet = False, returnIsTransferCourse = False, returnIsTSAProficient = False, returnIsWorkInProgress = False, returnLastStudentSectionTransactionConsideredDropped = False, returnLinkedStudentSectionsEarnedCredit = False, returnLinkedStudentSectionsEarnedCreditAttempted = False, returnLinkedStudentSectionsFailedCredit = False, returnMissingAssignmentCount = False, returnModifiedTime = False, returnMultipleTransactions = False, returnRenderTransferGradesRowButton = False, returnRequestedFromOfferingEntityAndAllTransactionsCountTowardsViewingEntity = False, returnSchoolYearIDCourse = False, returnSectionID = False, returnSectionLengthSubsetSummary = False, returnStartDate = False, returnStatus = False, returnStatusCode = False, returnStatusString = False, returnStudentID = False, returnStudentSectionCode = False, returnStudentSectionIDHash = False, returnStudentSectionLink = False, returnStudentSectionMNID = False, returnStudentSectionNoteCountForCurrentUser = False, returnTotalDaysAbsent = False, returnTotalDaysExcused = False, returnTotalDaysOther = False, returnTotalDaysTardy = False, returnTotalDaysUnexcused = False, returnTotalEarnedCreditOverride = False, returnTotalFailedCreditOverride = False, returnTransactionCountsForViewingEntity = False, returnTransferCourseName = False, returnUnscoredPastDueAssignmentCount = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditTotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentSection/" + str(StudentSectionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentSection(EntityID = 1, setEarnedCreditOverride = None, setEntityIDCourse = None, setExcludeFromReportCardsAndTranscripts = None, setExcludeFromStudentSectionLink = None, setGradeReferenceID = None, setIsTransferCourse = None, setIsTSAProficient = None, setIsWorkInProgress = None, setSchoolYearIDCourse = None, setSectionID = None, setSectionLengthSubsetSummary = None, setStudentID = None, setStudentSectionLink = None, setTotalEarnedCreditOverride = None, setTotalFailedCreditOverride = None, setTransferCourseName = None, setUseEarnedCreditOverride = None, setUseEarnedCreditTotalOverride = None, setRelationships = None, returnStudentSectionID = True, returnAcademicHistoryHash = False, returnActiveStudentGroups = False, returnAllTransactionsCountTowardsViewingEntity = False, returnAssignmentDueDateAttendance = False, returnCountsForViewingEntity = False, returnCourseOrTransferDescription = False, returnCreatedTime = False, returnDisplayLinkedStudentSection = False, returnDisplayToViewingEntity = False, returnEarnedCreditAttempted = False, returnEarnedCreditOverride = False, returnEarnedCredits = False, returnEarnedCreditsPossible = False, returnEndDate = False, returnEntityIDCourse = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLink = False, returnExistsStudentSectionGPAMethods = False, returnFailedCredits = False, returnFilteredGradedAssignmentCount = False, returnFilteredMissingAssignmentCount = False, returnFilteredUnGradedAssignmentCount = False, returnGradebookSortCode = False, returnGradebookStudentNameToUse = False, returnGradeReferenceID = False, returnHasAtLeastOneCrossEntityStudentSectionTransaction = False, returnHasAtleastOneTransactionNotCountTowardsViewingEntity = False, returnHasLinkingConflicts = False, returnHasStudentGradingScaleGroupForGradingPeriodGradeBucket = False, returnHasStudentSectionNoteForCurrentUser = False, returnInProgress = False, returnInProgressAndIsEffectiveForViewingEntity = False, returnIsActiveAsOfDate = False, returnIsActiveForTodayOrForSectionStartOrEnd = False, returnIsAvailableForAssignmentStudentGroup = False, returnIsBeforeOrInProgress = False, returnIsBeforeOrInProgressAndNotHasAtleastOneTransactionNotCountTowardsViewingEntity = False, returnIsCurrentStudentSection = False, returnIsEffectiveForViewingEntity = False, returnIsFlaggedAsMissingAssignmentCount = False, returnIsForCurrentSchoolYear = False, returnIsStudentSectionScheduledToMeet = False, returnIsTransferCourse = False, returnIsTSAProficient = False, returnIsWorkInProgress = False, returnLastStudentSectionTransactionConsideredDropped = False, returnLinkedStudentSectionsEarnedCredit = False, returnLinkedStudentSectionsEarnedCreditAttempted = False, returnLinkedStudentSectionsFailedCredit = False, returnMissingAssignmentCount = False, returnModifiedTime = False, returnMultipleTransactions = False, returnRenderTransferGradesRowButton = False, returnRequestedFromOfferingEntityAndAllTransactionsCountTowardsViewingEntity = False, returnSchoolYearIDCourse = False, returnSectionID = False, returnSectionLengthSubsetSummary = False, returnStartDate = False, returnStatus = False, returnStatusCode = False, returnStatusString = False, returnStudentID = False, returnStudentSectionCode = False, returnStudentSectionIDHash = False, returnStudentSectionLink = False, returnStudentSectionMNID = False, returnStudentSectionNoteCountForCurrentUser = False, returnTotalDaysAbsent = False, returnTotalDaysExcused = False, returnTotalDaysOther = False, returnTotalDaysTardy = False, returnTotalDaysUnexcused = False, returnTotalEarnedCreditOverride = False, returnTotalFailedCreditOverride = False, returnTransactionCountsForViewingEntity = False, returnTransferCourseName = False, returnUnscoredPastDueAssignmentCount = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditTotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromOfferingEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentSection/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentSection(StudentSectionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentSectionTransaction(EntityID = 1, page = 1, pageSize = 100, returnStudentSectionTransactionID = True, returnCalendarID = False, returnCountsTowardsViewingEntity = False, returnCreatedTime = False, returnEarlyExitReasonID = False, returnEndDate = False, returnEndsAfterSectionLengthStartDate = False, returnEntityIDCountsAs = False, returnHideNewStudentButton = False, returnIsCECE = False, returnIsInProgress = False, returnIsInProgressAsOfToday = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnOverlapsSectionLength = False, returnSectionID = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnStudentSectionID = False, returnStudentSectionTransactionIDHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentSectionTransaction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentSectionTransaction(StudentSectionTransactionID, EntityID = 1, returnStudentSectionTransactionID = True, returnCalendarID = False, returnCountsTowardsViewingEntity = False, returnCreatedTime = False, returnEarlyExitReasonID = False, returnEndDate = False, returnEndsAfterSectionLengthStartDate = False, returnEntityIDCountsAs = False, returnHideNewStudentButton = False, returnIsCECE = False, returnIsInProgress = False, returnIsInProgressAsOfToday = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnOverlapsSectionLength = False, returnSectionID = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnStudentSectionID = False, returnStudentSectionTransactionIDHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentSectionTransaction/" + str(StudentSectionTransactionID), verb = "get", return_params_list = return_params_list)

def modifyStudentSectionTransaction(StudentSectionTransactionID, EntityID = 1, setEarlyExitReasonID = None, setEndDate = None, setEntityIDCountsAs = None, setHideNewStudentButton = None, setNameIDRequestedBy = None, setSectionID = None, setSectionLengthSubsetID = None, setStartDate = None, setStudentSectionID = None, setRelationships = None, returnStudentSectionTransactionID = True, returnCalendarID = False, returnCountsTowardsViewingEntity = False, returnCreatedTime = False, returnEarlyExitReasonID = False, returnEndDate = False, returnEndsAfterSectionLengthStartDate = False, returnEntityIDCountsAs = False, returnHideNewStudentButton = False, returnIsCECE = False, returnIsInProgress = False, returnIsInProgressAsOfToday = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnOverlapsSectionLength = False, returnSectionID = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnStudentSectionID = False, returnStudentSectionTransactionIDHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentSectionTransaction/" + str(StudentSectionTransactionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentSectionTransaction(EntityID = 1, setEarlyExitReasonID = None, setEndDate = None, setEntityIDCountsAs = None, setHideNewStudentButton = None, setNameIDRequestedBy = None, setSectionID = None, setSectionLengthSubsetID = None, setStartDate = None, setStudentSectionID = None, setRelationships = None, returnStudentSectionTransactionID = True, returnCalendarID = False, returnCountsTowardsViewingEntity = False, returnCreatedTime = False, returnEarlyExitReasonID = False, returnEndDate = False, returnEndsAfterSectionLengthStartDate = False, returnEntityIDCountsAs = False, returnHideNewStudentButton = False, returnIsCECE = False, returnIsInProgress = False, returnIsInProgressAsOfToday = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnOverlapsSectionLength = False, returnSectionID = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnStudentSectionID = False, returnStudentSectionTransactionIDHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudentSectionTransaction/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentSectionTransaction(StudentSectionTransactionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudyHallSchedulerRunAnalysis(EntityID = 1, page = 1, pageSize = 100, returnStudyHallSchedulerRunAnalysisID = True, returnBaseRunAnalysisID = False, returnCreatedTime = False, returnEndTimeAnalysis = False, returnEndTimeFinalize = False, returnModifiedTime = False, returnRunInformation = False, returnStartTimeAnalysis = False, returnStartTimeFinalize = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudyHallSchedulerRunAnalysis/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudyHallSchedulerRunAnalysis(StudyHallSchedulerRunAnalysisID, EntityID = 1, returnStudyHallSchedulerRunAnalysisID = True, returnBaseRunAnalysisID = False, returnCreatedTime = False, returnEndTimeAnalysis = False, returnEndTimeFinalize = False, returnModifiedTime = False, returnRunInformation = False, returnStartTimeAnalysis = False, returnStartTimeFinalize = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudyHallSchedulerRunAnalysis/" + str(StudyHallSchedulerRunAnalysisID), verb = "get", return_params_list = return_params_list)

def modifyStudyHallSchedulerRunAnalysis(StudyHallSchedulerRunAnalysisID, EntityID = 1, setBaseRunAnalysisID = None, setEndTimeAnalysis = None, setEndTimeFinalize = None, setRunInformation = None, setStartTimeAnalysis = None, setStartTimeFinalize = None, setRelationships = None, returnStudyHallSchedulerRunAnalysisID = True, returnBaseRunAnalysisID = False, returnCreatedTime = False, returnEndTimeAnalysis = False, returnEndTimeFinalize = False, returnModifiedTime = False, returnRunInformation = False, returnStartTimeAnalysis = False, returnStartTimeFinalize = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudyHallSchedulerRunAnalysis/" + str(StudyHallSchedulerRunAnalysisID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudyHallSchedulerRunAnalysis(EntityID = 1, setBaseRunAnalysisID = None, setEndTimeAnalysis = None, setEndTimeFinalize = None, setRunInformation = None, setStartTimeAnalysis = None, setStartTimeFinalize = None, setRelationships = None, returnStudyHallSchedulerRunAnalysisID = True, returnBaseRunAnalysisID = False, returnCreatedTime = False, returnEndTimeAnalysis = False, returnEndTimeFinalize = False, returnModifiedTime = False, returnRunInformation = False, returnStartTimeAnalysis = False, returnStartTimeFinalize = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/StudyHallSchedulerRunAnalysis/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudyHallSchedulerRunAnalysis(StudyHallSchedulerRunAnalysisID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempCourse(EntityID = 1, page = 1, pageSize = 100, returnTempCourseID = True, returnActiveSections = False, returnAveragePerSectionMinimumSectionsRequired = False, returnCodeDescription = False, returnCourseCode = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseLengthID = False, returnCourseSubjectCode = False, returnCourseTypeCode = False, returnCreatedTime = False, returnCurriculumCode = False, returnDefaultSectionLengthID = False, returnDescription = False, returnEarnedCredits = False, returnEntityCode = False, returnEstimatedNumberOfSections = False, returnEstimatedStudentsPerSection = False, returnGradeLevelSummary = False, returnGradingPeriodSetCode = False, returnGradingPeriodSetID = False, returnIsActive = False, returnMinimumSectionsRequired = False, returnModifiedTime = False, returnNewCourseLengthCode = False, returnNewCourseLengthID = False, returnNewGradingPeriodSetCode = False, returnNewGradingPeriodSetID = False, returnNote = False, returnNumberOfAlternateCourseRequests = False, returnNumberOfCourseRequests = False, returnNumberOfSeatsAvailable = False, returnNumberOfTransferStudentSections = False, returnObjectIsDirty = False, returnOriginalEstimatedNumberOfSections = False, returnRowIsReadOnly = False, returnRowIsSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempCourse(TempCourseID, EntityID = 1, returnTempCourseID = True, returnActiveSections = False, returnAveragePerSectionMinimumSectionsRequired = False, returnCodeDescription = False, returnCourseCode = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseLengthID = False, returnCourseSubjectCode = False, returnCourseTypeCode = False, returnCreatedTime = False, returnCurriculumCode = False, returnDefaultSectionLengthID = False, returnDescription = False, returnEarnedCredits = False, returnEntityCode = False, returnEstimatedNumberOfSections = False, returnEstimatedStudentsPerSection = False, returnGradeLevelSummary = False, returnGradingPeriodSetCode = False, returnGradingPeriodSetID = False, returnIsActive = False, returnMinimumSectionsRequired = False, returnModifiedTime = False, returnNewCourseLengthCode = False, returnNewCourseLengthID = False, returnNewGradingPeriodSetCode = False, returnNewGradingPeriodSetID = False, returnNote = False, returnNumberOfAlternateCourseRequests = False, returnNumberOfCourseRequests = False, returnNumberOfSeatsAvailable = False, returnNumberOfTransferStudentSections = False, returnObjectIsDirty = False, returnOriginalEstimatedNumberOfSections = False, returnRowIsReadOnly = False, returnRowIsSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourse/" + str(TempCourseID), verb = "get", return_params_list = return_params_list)

def modifyTempCourse(TempCourseID, EntityID = 1, setActiveSections = None, setAveragePerSectionMinimumSectionsRequired = None, setCodeDescription = None, setCourseCode = None, setCourseID = None, setCourseLengthCode = None, setCourseLengthID = None, setCourseSubjectCode = None, setCourseTypeCode = None, setCurriculumCode = None, setDefaultSectionLengthID = None, setDescription = None, setEarnedCredits = None, setEntityCode = None, setEstimatedNumberOfSections = None, setEstimatedStudentsPerSection = None, setGradeLevelSummary = None, setGradingPeriodSetCode = None, setGradingPeriodSetID = None, setIsActive = None, setMinimumSectionsRequired = None, setNewCourseLengthCode = None, setNewCourseLengthID = None, setNewGradingPeriodSetCode = None, setNewGradingPeriodSetID = None, setNote = None, setNumberOfAlternateCourseRequests = None, setNumberOfCourseRequests = None, setNumberOfSeatsAvailable = None, setNumberOfTransferStudentSections = None, setObjectIsDirty = None, setOriginalEstimatedNumberOfSections = None, setRowIsReadOnly = None, setRowIsSelected = None, setRelationships = None, returnTempCourseID = True, returnActiveSections = False, returnAveragePerSectionMinimumSectionsRequired = False, returnCodeDescription = False, returnCourseCode = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseLengthID = False, returnCourseSubjectCode = False, returnCourseTypeCode = False, returnCreatedTime = False, returnCurriculumCode = False, returnDefaultSectionLengthID = False, returnDescription = False, returnEarnedCredits = False, returnEntityCode = False, returnEstimatedNumberOfSections = False, returnEstimatedStudentsPerSection = False, returnGradeLevelSummary = False, returnGradingPeriodSetCode = False, returnGradingPeriodSetID = False, returnIsActive = False, returnMinimumSectionsRequired = False, returnModifiedTime = False, returnNewCourseLengthCode = False, returnNewCourseLengthID = False, returnNewGradingPeriodSetCode = False, returnNewGradingPeriodSetID = False, returnNote = False, returnNumberOfAlternateCourseRequests = False, returnNumberOfCourseRequests = False, returnNumberOfSeatsAvailable = False, returnNumberOfTransferStudentSections = False, returnObjectIsDirty = False, returnOriginalEstimatedNumberOfSections = False, returnRowIsReadOnly = False, returnRowIsSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourse/" + str(TempCourseID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempCourse(EntityID = 1, setActiveSections = None, setAveragePerSectionMinimumSectionsRequired = None, setCodeDescription = None, setCourseCode = None, setCourseID = None, setCourseLengthCode = None, setCourseLengthID = None, setCourseSubjectCode = None, setCourseTypeCode = None, setCurriculumCode = None, setDefaultSectionLengthID = None, setDescription = None, setEarnedCredits = None, setEntityCode = None, setEstimatedNumberOfSections = None, setEstimatedStudentsPerSection = None, setGradeLevelSummary = None, setGradingPeriodSetCode = None, setGradingPeriodSetID = None, setIsActive = None, setMinimumSectionsRequired = None, setNewCourseLengthCode = None, setNewCourseLengthID = None, setNewGradingPeriodSetCode = None, setNewGradingPeriodSetID = None, setNote = None, setNumberOfAlternateCourseRequests = None, setNumberOfCourseRequests = None, setNumberOfSeatsAvailable = None, setNumberOfTransferStudentSections = None, setObjectIsDirty = None, setOriginalEstimatedNumberOfSections = None, setRowIsReadOnly = None, setRowIsSelected = None, setRelationships = None, returnTempCourseID = True, returnActiveSections = False, returnAveragePerSectionMinimumSectionsRequired = False, returnCodeDescription = False, returnCourseCode = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseLengthID = False, returnCourseSubjectCode = False, returnCourseTypeCode = False, returnCreatedTime = False, returnCurriculumCode = False, returnDefaultSectionLengthID = False, returnDescription = False, returnEarnedCredits = False, returnEntityCode = False, returnEstimatedNumberOfSections = False, returnEstimatedStudentsPerSection = False, returnGradeLevelSummary = False, returnGradingPeriodSetCode = False, returnGradingPeriodSetID = False, returnIsActive = False, returnMinimumSectionsRequired = False, returnModifiedTime = False, returnNewCourseLengthCode = False, returnNewCourseLengthID = False, returnNewGradingPeriodSetCode = False, returnNewGradingPeriodSetID = False, returnNote = False, returnNumberOfAlternateCourseRequests = False, returnNumberOfCourseRequests = False, returnNumberOfSeatsAvailable = False, returnNumberOfTransferStudentSections = False, returnObjectIsDirty = False, returnOriginalEstimatedNumberOfSections = False, returnRowIsReadOnly = False, returnRowIsSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourse/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempCourse(TempCourseID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempCourseEntityOfferedToSection(EntityID = 1, page = 1, pageSize = 100, returnTempCourseEntityOfferedToSectionID = True, returnCourseEntityOfferedToID = False, returnCourseEntityOfferedToSectionID = False, returnCourseEntityOfferedToSectionRecordExists = False, returnCourseID = False, returnCreatedTime = False, returnEntityIDOfferedTo = False, returnEntityOfferedToCode = False, returnEntityOfferedToName = False, returnIsActiveOverride = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnOriginalMaximumStudentCount = False, returnRowIsSelected = False, returnSchoolYearID = False, returnSeatsAvailable = False, returnSectionCode = False, returnSectionID = False, returnSectionIsActive = False, returnSectionMaximumStudentCount = False, returnSectionReservedSeatCount = False, returnSectionSectionLengthCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourseEntityOfferedToSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempCourseEntityOfferedToSection(TempCourseEntityOfferedToSectionID, EntityID = 1, returnTempCourseEntityOfferedToSectionID = True, returnCourseEntityOfferedToID = False, returnCourseEntityOfferedToSectionID = False, returnCourseEntityOfferedToSectionRecordExists = False, returnCourseID = False, returnCreatedTime = False, returnEntityIDOfferedTo = False, returnEntityOfferedToCode = False, returnEntityOfferedToName = False, returnIsActiveOverride = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnOriginalMaximumStudentCount = False, returnRowIsSelected = False, returnSchoolYearID = False, returnSeatsAvailable = False, returnSectionCode = False, returnSectionID = False, returnSectionIsActive = False, returnSectionMaximumStudentCount = False, returnSectionReservedSeatCount = False, returnSectionSectionLengthCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourseEntityOfferedToSection/" + str(TempCourseEntityOfferedToSectionID), verb = "get", return_params_list = return_params_list)

def modifyTempCourseEntityOfferedToSection(TempCourseEntityOfferedToSectionID, EntityID = 1, setCourseEntityOfferedToID = None, setCourseEntityOfferedToSectionID = None, setCourseEntityOfferedToSectionRecordExists = None, setCourseID = None, setEntityIDOfferedTo = None, setEntityOfferedToCode = None, setEntityOfferedToName = None, setIsActiveOverride = None, setMaximumStudentCount = None, setOriginalMaximumStudentCount = None, setRowIsSelected = None, setSchoolYearID = None, setSeatsAvailable = None, setSectionCode = None, setSectionID = None, setSectionIsActive = None, setSectionMaximumStudentCount = None, setSectionReservedSeatCount = None, setSectionSectionLengthCode = None, setRelationships = None, returnTempCourseEntityOfferedToSectionID = True, returnCourseEntityOfferedToID = False, returnCourseEntityOfferedToSectionID = False, returnCourseEntityOfferedToSectionRecordExists = False, returnCourseID = False, returnCreatedTime = False, returnEntityIDOfferedTo = False, returnEntityOfferedToCode = False, returnEntityOfferedToName = False, returnIsActiveOverride = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnOriginalMaximumStudentCount = False, returnRowIsSelected = False, returnSchoolYearID = False, returnSeatsAvailable = False, returnSectionCode = False, returnSectionID = False, returnSectionIsActive = False, returnSectionMaximumStudentCount = False, returnSectionReservedSeatCount = False, returnSectionSectionLengthCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourseEntityOfferedToSection/" + str(TempCourseEntityOfferedToSectionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempCourseEntityOfferedToSection(EntityID = 1, setCourseEntityOfferedToID = None, setCourseEntityOfferedToSectionID = None, setCourseEntityOfferedToSectionRecordExists = None, setCourseID = None, setEntityIDOfferedTo = None, setEntityOfferedToCode = None, setEntityOfferedToName = None, setIsActiveOverride = None, setMaximumStudentCount = None, setOriginalMaximumStudentCount = None, setRowIsSelected = None, setSchoolYearID = None, setSeatsAvailable = None, setSectionCode = None, setSectionID = None, setSectionIsActive = None, setSectionMaximumStudentCount = None, setSectionReservedSeatCount = None, setSectionSectionLengthCode = None, setRelationships = None, returnTempCourseEntityOfferedToSectionID = True, returnCourseEntityOfferedToID = False, returnCourseEntityOfferedToSectionID = False, returnCourseEntityOfferedToSectionRecordExists = False, returnCourseID = False, returnCreatedTime = False, returnEntityIDOfferedTo = False, returnEntityOfferedToCode = False, returnEntityOfferedToName = False, returnIsActiveOverride = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnOriginalMaximumStudentCount = False, returnRowIsSelected = False, returnSchoolYearID = False, returnSeatsAvailable = False, returnSectionCode = False, returnSectionID = False, returnSectionIsActive = False, returnSectionMaximumStudentCount = False, returnSectionReservedSeatCount = False, returnSectionSectionLengthCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourseEntityOfferedToSection/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempCourseEntityOfferedToSection(TempCourseEntityOfferedToSectionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempCourseMasterMassUpdateError(EntityID = 1, page = 1, pageSize = 100, returnTempCourseMasterMassUpdateErrorID = True, returnBaseTableName = False, returnCreatedTime = False, returnModifiedTime = False, returnSourceDescription = False, returnTableName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourseMasterMassUpdateError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempCourseMasterMassUpdateError(TempCourseMasterMassUpdateErrorID, EntityID = 1, returnTempCourseMasterMassUpdateErrorID = True, returnBaseTableName = False, returnCreatedTime = False, returnModifiedTime = False, returnSourceDescription = False, returnTableName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourseMasterMassUpdateError/" + str(TempCourseMasterMassUpdateErrorID), verb = "get", return_params_list = return_params_list)

def modifyTempCourseMasterMassUpdateError(TempCourseMasterMassUpdateErrorID, EntityID = 1, setBaseTableName = None, setSourceDescription = None, setTableName = None, setRelationships = None, returnTempCourseMasterMassUpdateErrorID = True, returnBaseTableName = False, returnCreatedTime = False, returnModifiedTime = False, returnSourceDescription = False, returnTableName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourseMasterMassUpdateError/" + str(TempCourseMasterMassUpdateErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempCourseMasterMassUpdateError(EntityID = 1, setBaseTableName = None, setSourceDescription = None, setTableName = None, setRelationships = None, returnTempCourseMasterMassUpdateErrorID = True, returnBaseTableName = False, returnCreatedTime = False, returnModifiedTime = False, returnSourceDescription = False, returnTableName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourseMasterMassUpdateError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempCourseMasterMassUpdateError(TempCourseMasterMassUpdateErrorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempCourseMasterMassUpdateErrorDetail(EntityID = 1, page = 1, pageSize = 100, returnTempCourseMasterMassUpdateErrorDetailID = True, returnCreatedTime = False, returnError = False, returnErrorName = False, returnModifiedTime = False, returnTempCourseMasterMassUpdateErrorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourseMasterMassUpdateErrorDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempCourseMasterMassUpdateErrorDetail(TempCourseMasterMassUpdateErrorDetailID, EntityID = 1, returnTempCourseMasterMassUpdateErrorDetailID = True, returnCreatedTime = False, returnError = False, returnErrorName = False, returnModifiedTime = False, returnTempCourseMasterMassUpdateErrorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourseMasterMassUpdateErrorDetail/" + str(TempCourseMasterMassUpdateErrorDetailID), verb = "get", return_params_list = return_params_list)

def modifyTempCourseMasterMassUpdateErrorDetail(TempCourseMasterMassUpdateErrorDetailID, EntityID = 1, setError = None, setErrorName = None, setTempCourseMasterMassUpdateErrorID = None, setRelationships = None, returnTempCourseMasterMassUpdateErrorDetailID = True, returnCreatedTime = False, returnError = False, returnErrorName = False, returnModifiedTime = False, returnTempCourseMasterMassUpdateErrorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourseMasterMassUpdateErrorDetail/" + str(TempCourseMasterMassUpdateErrorDetailID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempCourseMasterMassUpdateErrorDetail(EntityID = 1, setError = None, setErrorName = None, setTempCourseMasterMassUpdateErrorID = None, setRelationships = None, returnTempCourseMasterMassUpdateErrorDetailID = True, returnCreatedTime = False, returnError = False, returnErrorName = False, returnModifiedTime = False, returnTempCourseMasterMassUpdateErrorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourseMasterMassUpdateErrorDetail/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempCourseMasterMassUpdateErrorDetail(TempCourseMasterMassUpdateErrorDetailID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempCourseMasterMassUpdateField(EntityID = 1, page = 1, pageSize = 100, returnTempCourseMasterMassUpdateFieldID = True, returnAffectedPrimaryKey = False, returnBaseTableName = False, returnCourseID = False, returnCreatedTime = False, returnFieldDisplayName = False, returnFieldName = False, returnFriendlyOriginalValue = False, returnFriendlyUpdatedValue = False, returnModifiedTime = False, returnOriginalValue = False, returnSourceDescription = False, returnTableName = False, returnUpdatedValue = False, returnUpdateRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourseMasterMassUpdateField/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempCourseMasterMassUpdateField(TempCourseMasterMassUpdateFieldID, EntityID = 1, returnTempCourseMasterMassUpdateFieldID = True, returnAffectedPrimaryKey = False, returnBaseTableName = False, returnCourseID = False, returnCreatedTime = False, returnFieldDisplayName = False, returnFieldName = False, returnFriendlyOriginalValue = False, returnFriendlyUpdatedValue = False, returnModifiedTime = False, returnOriginalValue = False, returnSourceDescription = False, returnTableName = False, returnUpdatedValue = False, returnUpdateRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourseMasterMassUpdateField/" + str(TempCourseMasterMassUpdateFieldID), verb = "get", return_params_list = return_params_list)

def modifyTempCourseMasterMassUpdateField(TempCourseMasterMassUpdateFieldID, EntityID = 1, setAffectedPrimaryKey = None, setBaseTableName = None, setCourseID = None, setFieldDisplayName = None, setFieldName = None, setFriendlyOriginalValue = None, setFriendlyUpdatedValue = None, setOriginalValue = None, setSourceDescription = None, setTableName = None, setUpdatedValue = None, setUpdateRank = None, setRelationships = None, returnTempCourseMasterMassUpdateFieldID = True, returnAffectedPrimaryKey = False, returnBaseTableName = False, returnCourseID = False, returnCreatedTime = False, returnFieldDisplayName = False, returnFieldName = False, returnFriendlyOriginalValue = False, returnFriendlyUpdatedValue = False, returnModifiedTime = False, returnOriginalValue = False, returnSourceDescription = False, returnTableName = False, returnUpdatedValue = False, returnUpdateRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourseMasterMassUpdateField/" + str(TempCourseMasterMassUpdateFieldID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempCourseMasterMassUpdateField(EntityID = 1, setAffectedPrimaryKey = None, setBaseTableName = None, setCourseID = None, setFieldDisplayName = None, setFieldName = None, setFriendlyOriginalValue = None, setFriendlyUpdatedValue = None, setOriginalValue = None, setSourceDescription = None, setTableName = None, setUpdatedValue = None, setUpdateRank = None, setRelationships = None, returnTempCourseMasterMassUpdateFieldID = True, returnAffectedPrimaryKey = False, returnBaseTableName = False, returnCourseID = False, returnCreatedTime = False, returnFieldDisplayName = False, returnFieldName = False, returnFriendlyOriginalValue = False, returnFriendlyUpdatedValue = False, returnModifiedTime = False, returnOriginalValue = False, returnSourceDescription = False, returnTableName = False, returnUpdatedValue = False, returnUpdateRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempCourseMasterMassUpdateField/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempCourseMasterMassUpdateField(TempCourseMasterMassUpdateFieldID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempDayRotation(EntityID = 1, page = 1, pageSize = 100, returnTempDayRotationID = True, returnCode = False, returnCreatedTime = False, returnDayRotationID = False, returnModifiedTime = False, returnNote = False, returnObjectIsDirty = False, returnObjectName = False, returnRecordsUpdated = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempDayRotation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempDayRotation(TempDayRotationID, EntityID = 1, returnTempDayRotationID = True, returnCode = False, returnCreatedTime = False, returnDayRotationID = False, returnModifiedTime = False, returnNote = False, returnObjectIsDirty = False, returnObjectName = False, returnRecordsUpdated = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempDayRotation/" + str(TempDayRotationID), verb = "get", return_params_list = return_params_list)

def modifyTempDayRotation(TempDayRotationID, EntityID = 1, setCode = None, setDayRotationID = None, setNote = None, setObjectIsDirty = None, setObjectName = None, setRecordsUpdated = None, setRelationships = None, returnTempDayRotationID = True, returnCode = False, returnCreatedTime = False, returnDayRotationID = False, returnModifiedTime = False, returnNote = False, returnObjectIsDirty = False, returnObjectName = False, returnRecordsUpdated = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempDayRotation/" + str(TempDayRotationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempDayRotation(EntityID = 1, setCode = None, setDayRotationID = None, setNote = None, setObjectIsDirty = None, setObjectName = None, setRecordsUpdated = None, setRelationships = None, returnTempDayRotationID = True, returnCode = False, returnCreatedTime = False, returnDayRotationID = False, returnModifiedTime = False, returnNote = False, returnObjectIsDirty = False, returnObjectName = False, returnRecordsUpdated = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempDayRotation/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempDayRotation(TempDayRotationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempException(EntityID = 1, page = 1, pageSize = 100, returnTempExceptionID = True, returnCreatedTime = False, returnErrorDetail = False, returnErrorFieldName = False, returnFailedRecordPrimaryKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempException(TempExceptionID, EntityID = 1, returnTempExceptionID = True, returnCreatedTime = False, returnErrorDetail = False, returnErrorFieldName = False, returnFailedRecordPrimaryKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempException/" + str(TempExceptionID), verb = "get", return_params_list = return_params_list)

def modifyTempException(TempExceptionID, EntityID = 1, setErrorDetail = None, setErrorFieldName = None, setFailedRecordPrimaryKey = None, setRelationships = None, returnTempExceptionID = True, returnCreatedTime = False, returnErrorDetail = False, returnErrorFieldName = False, returnFailedRecordPrimaryKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempException/" + str(TempExceptionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempException(EntityID = 1, setErrorDetail = None, setErrorFieldName = None, setFailedRecordPrimaryKey = None, setRelationships = None, returnTempExceptionID = True, returnCreatedTime = False, returnErrorDetail = False, returnErrorFieldName = False, returnFailedRecordPrimaryKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempException/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempException(TempExceptionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempFailedCourse(EntityID = 1, page = 1, pageSize = 100, returnTempFailedCourseID = True, returnActiveSections = False, returnAveragePerSectionMinimumSectionsRequired = False, returnCodeDescription = False, returnCourseCode = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseLengthID = False, returnCourseSubjectCode = False, returnCourseTypeCode = False, returnCreatedTime = False, returnCurriculumCode = False, returnDefaultSectionLengthID = False, returnDescription = False, returnEarnedCredits = False, returnEntityCode = False, returnEstimatedNumberOfSections = False, returnEstimatedStudentsPerSection = False, returnGradeLevelSummary = False, returnGradingPeriodSetCode = False, returnGradingPeriodSetID = False, returnIsActive = False, returnMinimumSectionsRequired = False, returnModifiedTime = False, returnNewCourseLengthCode = False, returnNewCourseLengthID = False, returnNewGradingPeriodSetCode = False, returnNewGradingPeriodSetID = False, returnNote = False, returnNumberOfAlternateCourseRequests = False, returnNumberOfCourseRequests = False, returnNumberOfSeatsAvailable = False, returnNumberOfTransferStudentSections = False, returnObjectIsDirty = False, returnOriginalEstimatedNumberOfSections = False, returnRowIsReadOnly = False, returnRowIsSelected = False, returnTempCourseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempFailedCourse(TempFailedCourseID, EntityID = 1, returnTempFailedCourseID = True, returnActiveSections = False, returnAveragePerSectionMinimumSectionsRequired = False, returnCodeDescription = False, returnCourseCode = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseLengthID = False, returnCourseSubjectCode = False, returnCourseTypeCode = False, returnCreatedTime = False, returnCurriculumCode = False, returnDefaultSectionLengthID = False, returnDescription = False, returnEarnedCredits = False, returnEntityCode = False, returnEstimatedNumberOfSections = False, returnEstimatedStudentsPerSection = False, returnGradeLevelSummary = False, returnGradingPeriodSetCode = False, returnGradingPeriodSetID = False, returnIsActive = False, returnMinimumSectionsRequired = False, returnModifiedTime = False, returnNewCourseLengthCode = False, returnNewCourseLengthID = False, returnNewGradingPeriodSetCode = False, returnNewGradingPeriodSetID = False, returnNote = False, returnNumberOfAlternateCourseRequests = False, returnNumberOfCourseRequests = False, returnNumberOfSeatsAvailable = False, returnNumberOfTransferStudentSections = False, returnObjectIsDirty = False, returnOriginalEstimatedNumberOfSections = False, returnRowIsReadOnly = False, returnRowIsSelected = False, returnTempCourseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedCourse/" + str(TempFailedCourseID), verb = "get", return_params_list = return_params_list)

def modifyTempFailedCourse(TempFailedCourseID, EntityID = 1, setActiveSections = None, setAveragePerSectionMinimumSectionsRequired = None, setCodeDescription = None, setCourseCode = None, setCourseID = None, setCourseLengthCode = None, setCourseLengthID = None, setCourseSubjectCode = None, setCourseTypeCode = None, setCurriculumCode = None, setDefaultSectionLengthID = None, setDescription = None, setEarnedCredits = None, setEntityCode = None, setEstimatedNumberOfSections = None, setEstimatedStudentsPerSection = None, setGradeLevelSummary = None, setGradingPeriodSetCode = None, setGradingPeriodSetID = None, setIsActive = None, setMinimumSectionsRequired = None, setNewCourseLengthCode = None, setNewCourseLengthID = None, setNewGradingPeriodSetCode = None, setNewGradingPeriodSetID = None, setNote = None, setNumberOfAlternateCourseRequests = None, setNumberOfCourseRequests = None, setNumberOfSeatsAvailable = None, setNumberOfTransferStudentSections = None, setObjectIsDirty = None, setOriginalEstimatedNumberOfSections = None, setRowIsReadOnly = None, setRowIsSelected = None, setTempCourseID = None, setRelationships = None, returnTempFailedCourseID = True, returnActiveSections = False, returnAveragePerSectionMinimumSectionsRequired = False, returnCodeDescription = False, returnCourseCode = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseLengthID = False, returnCourseSubjectCode = False, returnCourseTypeCode = False, returnCreatedTime = False, returnCurriculumCode = False, returnDefaultSectionLengthID = False, returnDescription = False, returnEarnedCredits = False, returnEntityCode = False, returnEstimatedNumberOfSections = False, returnEstimatedStudentsPerSection = False, returnGradeLevelSummary = False, returnGradingPeriodSetCode = False, returnGradingPeriodSetID = False, returnIsActive = False, returnMinimumSectionsRequired = False, returnModifiedTime = False, returnNewCourseLengthCode = False, returnNewCourseLengthID = False, returnNewGradingPeriodSetCode = False, returnNewGradingPeriodSetID = False, returnNote = False, returnNumberOfAlternateCourseRequests = False, returnNumberOfCourseRequests = False, returnNumberOfSeatsAvailable = False, returnNumberOfTransferStudentSections = False, returnObjectIsDirty = False, returnOriginalEstimatedNumberOfSections = False, returnRowIsReadOnly = False, returnRowIsSelected = False, returnTempCourseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedCourse/" + str(TempFailedCourseID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempFailedCourse(EntityID = 1, setActiveSections = None, setAveragePerSectionMinimumSectionsRequired = None, setCodeDescription = None, setCourseCode = None, setCourseID = None, setCourseLengthCode = None, setCourseLengthID = None, setCourseSubjectCode = None, setCourseTypeCode = None, setCurriculumCode = None, setDefaultSectionLengthID = None, setDescription = None, setEarnedCredits = None, setEntityCode = None, setEstimatedNumberOfSections = None, setEstimatedStudentsPerSection = None, setGradeLevelSummary = None, setGradingPeriodSetCode = None, setGradingPeriodSetID = None, setIsActive = None, setMinimumSectionsRequired = None, setNewCourseLengthCode = None, setNewCourseLengthID = None, setNewGradingPeriodSetCode = None, setNewGradingPeriodSetID = None, setNote = None, setNumberOfAlternateCourseRequests = None, setNumberOfCourseRequests = None, setNumberOfSeatsAvailable = None, setNumberOfTransferStudentSections = None, setObjectIsDirty = None, setOriginalEstimatedNumberOfSections = None, setRowIsReadOnly = None, setRowIsSelected = None, setTempCourseID = None, setRelationships = None, returnTempFailedCourseID = True, returnActiveSections = False, returnAveragePerSectionMinimumSectionsRequired = False, returnCodeDescription = False, returnCourseCode = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseLengthID = False, returnCourseSubjectCode = False, returnCourseTypeCode = False, returnCreatedTime = False, returnCurriculumCode = False, returnDefaultSectionLengthID = False, returnDescription = False, returnEarnedCredits = False, returnEntityCode = False, returnEstimatedNumberOfSections = False, returnEstimatedStudentsPerSection = False, returnGradeLevelSummary = False, returnGradingPeriodSetCode = False, returnGradingPeriodSetID = False, returnIsActive = False, returnMinimumSectionsRequired = False, returnModifiedTime = False, returnNewCourseLengthCode = False, returnNewCourseLengthID = False, returnNewGradingPeriodSetCode = False, returnNewGradingPeriodSetID = False, returnNote = False, returnNumberOfAlternateCourseRequests = False, returnNumberOfCourseRequests = False, returnNumberOfSeatsAvailable = False, returnNumberOfTransferStudentSections = False, returnObjectIsDirty = False, returnOriginalEstimatedNumberOfSections = False, returnRowIsReadOnly = False, returnRowIsSelected = False, returnTempCourseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedCourse/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempFailedCourse(TempFailedCourseID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempFailedDayRotation(EntityID = 1, page = 1, pageSize = 100, returnTempFailedDayRotationID = True, returnCode = False, returnCreatedTime = False, returnDayRotationID = False, returnModifiedTime = False, returnNote = False, returnObjectIsDirty = False, returnObjectName = False, returnRecordsUpdated = False, returnTempDayRotationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedDayRotation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempFailedDayRotation(TempFailedDayRotationID, EntityID = 1, returnTempFailedDayRotationID = True, returnCode = False, returnCreatedTime = False, returnDayRotationID = False, returnModifiedTime = False, returnNote = False, returnObjectIsDirty = False, returnObjectName = False, returnRecordsUpdated = False, returnTempDayRotationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedDayRotation/" + str(TempFailedDayRotationID), verb = "get", return_params_list = return_params_list)

def modifyTempFailedDayRotation(TempFailedDayRotationID, EntityID = 1, setCode = None, setDayRotationID = None, setNote = None, setObjectIsDirty = None, setObjectName = None, setRecordsUpdated = None, setTempDayRotationID = None, setRelationships = None, returnTempFailedDayRotationID = True, returnCode = False, returnCreatedTime = False, returnDayRotationID = False, returnModifiedTime = False, returnNote = False, returnObjectIsDirty = False, returnObjectName = False, returnRecordsUpdated = False, returnTempDayRotationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedDayRotation/" + str(TempFailedDayRotationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempFailedDayRotation(EntityID = 1, setCode = None, setDayRotationID = None, setNote = None, setObjectIsDirty = None, setObjectName = None, setRecordsUpdated = None, setTempDayRotationID = None, setRelationships = None, returnTempFailedDayRotationID = True, returnCode = False, returnCreatedTime = False, returnDayRotationID = False, returnModifiedTime = False, returnNote = False, returnObjectIsDirty = False, returnObjectName = False, returnRecordsUpdated = False, returnTempDayRotationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedDayRotation/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempFailedDayRotation(TempFailedDayRotationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempFailedSection(EntityID = 1, page = 1, pageSize = 100, returnTempFailedSectionID = True, returnCourse = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseID = False, returnCourseIsActive = False, returnCourseTypeCode = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnEntityIDCourse = False, returnEntityIDOfferedTo = False, returnErrorCount = False, returnGradeLevelSummary = False, returnHasErrors = False, returnIsActive = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNewCourseLengthCode = False, returnNewCourseLengthID = False, returnNewSectionLengthCode = False, returnNewSectionLengthID = False, returnNote = False, returnNumberOfTransferStudentSections = False, returnPeriodDaySummary = False, returnPrimaryDays = False, returnPrimaryDisplayPeriod = False, returnRowIsReadOnly = False, returnRowIsSelected = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnSectionLengthEndDate = False, returnSectionLengthID = False, returnSectionLengthStartDate = False, returnStaffFullNameFML = False, returnTargetCourse = False, returnTempSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempFailedSection(TempFailedSectionID, EntityID = 1, returnTempFailedSectionID = True, returnCourse = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseID = False, returnCourseIsActive = False, returnCourseTypeCode = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnEntityIDCourse = False, returnEntityIDOfferedTo = False, returnErrorCount = False, returnGradeLevelSummary = False, returnHasErrors = False, returnIsActive = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNewCourseLengthCode = False, returnNewCourseLengthID = False, returnNewSectionLengthCode = False, returnNewSectionLengthID = False, returnNote = False, returnNumberOfTransferStudentSections = False, returnPeriodDaySummary = False, returnPrimaryDays = False, returnPrimaryDisplayPeriod = False, returnRowIsReadOnly = False, returnRowIsSelected = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnSectionLengthEndDate = False, returnSectionLengthID = False, returnSectionLengthStartDate = False, returnStaffFullNameFML = False, returnTargetCourse = False, returnTempSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedSection/" + str(TempFailedSectionID), verb = "get", return_params_list = return_params_list)

def modifyTempFailedSection(TempFailedSectionID, EntityID = 1, setCourse = None, setCourseDescription = None, setCourseEntityOfferedToID = None, setCourseID = None, setCourseIsActive = None, setCourseTypeCode = None, setCurrentEnrollment = None, setEntityIDCourse = None, setEntityIDOfferedTo = None, setErrorCount = None, setGradeLevelSummary = None, setHasErrors = None, setIsActive = None, setMaximumStudentCount = None, setNewCourseLengthCode = None, setNewCourseLengthID = None, setNewSectionLengthCode = None, setNewSectionLengthID = None, setNote = None, setNumberOfTransferStudentSections = None, setPeriodDaySummary = None, setPrimaryDays = None, setPrimaryDisplayPeriod = None, setRowIsReadOnly = None, setRowIsSelected = None, setSchoolYearIDCourse = None, setSectionCode = None, setSectionID = None, setSectionLengthCode = None, setSectionLengthEndDate = None, setSectionLengthID = None, setSectionLengthStartDate = None, setStaffFullNameFML = None, setTargetCourse = None, setTempSectionID = None, setRelationships = None, returnTempFailedSectionID = True, returnCourse = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseID = False, returnCourseIsActive = False, returnCourseTypeCode = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnEntityIDCourse = False, returnEntityIDOfferedTo = False, returnErrorCount = False, returnGradeLevelSummary = False, returnHasErrors = False, returnIsActive = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNewCourseLengthCode = False, returnNewCourseLengthID = False, returnNewSectionLengthCode = False, returnNewSectionLengthID = False, returnNote = False, returnNumberOfTransferStudentSections = False, returnPeriodDaySummary = False, returnPrimaryDays = False, returnPrimaryDisplayPeriod = False, returnRowIsReadOnly = False, returnRowIsSelected = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnSectionLengthEndDate = False, returnSectionLengthID = False, returnSectionLengthStartDate = False, returnStaffFullNameFML = False, returnTargetCourse = False, returnTempSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedSection/" + str(TempFailedSectionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempFailedSection(EntityID = 1, setCourse = None, setCourseDescription = None, setCourseEntityOfferedToID = None, setCourseID = None, setCourseIsActive = None, setCourseTypeCode = None, setCurrentEnrollment = None, setEntityIDCourse = None, setEntityIDOfferedTo = None, setErrorCount = None, setGradeLevelSummary = None, setHasErrors = None, setIsActive = None, setMaximumStudentCount = None, setNewCourseLengthCode = None, setNewCourseLengthID = None, setNewSectionLengthCode = None, setNewSectionLengthID = None, setNote = None, setNumberOfTransferStudentSections = None, setPeriodDaySummary = None, setPrimaryDays = None, setPrimaryDisplayPeriod = None, setRowIsReadOnly = None, setRowIsSelected = None, setSchoolYearIDCourse = None, setSectionCode = None, setSectionID = None, setSectionLengthCode = None, setSectionLengthEndDate = None, setSectionLengthID = None, setSectionLengthStartDate = None, setStaffFullNameFML = None, setTargetCourse = None, setTempSectionID = None, setRelationships = None, returnTempFailedSectionID = True, returnCourse = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseID = False, returnCourseIsActive = False, returnCourseTypeCode = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnEntityIDCourse = False, returnEntityIDOfferedTo = False, returnErrorCount = False, returnGradeLevelSummary = False, returnHasErrors = False, returnIsActive = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNewCourseLengthCode = False, returnNewCourseLengthID = False, returnNewSectionLengthCode = False, returnNewSectionLengthID = False, returnNote = False, returnNumberOfTransferStudentSections = False, returnPeriodDaySummary = False, returnPrimaryDays = False, returnPrimaryDisplayPeriod = False, returnRowIsReadOnly = False, returnRowIsSelected = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnSectionLengthEndDate = False, returnSectionLengthID = False, returnSectionLengthStartDate = False, returnStaffFullNameFML = False, returnTargetCourse = False, returnTempSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedSection/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempFailedSection(TempFailedSectionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempFailedSectionLengthSubset(EntityID = 1, page = 1, pageSize = 100, returnTempFailedSectionLengthSubsetID = True, returnCode = False, returnCodeDescription = False, returnCourseLengthCode = False, returnCourseLengthCodeDescription = False, returnCourseLengthID = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnIsFullSectionLength = False, returnModifiedTime = False, returnNote = False, returnObjectIsDirty = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnSectionLengthCode = False, returnSectionLengthCodeDescription = False, returnSectionLengthID = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnTempSectionLengthSubsetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedSectionLengthSubset/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempFailedSectionLengthSubset(TempFailedSectionLengthSubsetID, EntityID = 1, returnTempFailedSectionLengthSubsetID = True, returnCode = False, returnCodeDescription = False, returnCourseLengthCode = False, returnCourseLengthCodeDescription = False, returnCourseLengthID = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnIsFullSectionLength = False, returnModifiedTime = False, returnNote = False, returnObjectIsDirty = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnSectionLengthCode = False, returnSectionLengthCodeDescription = False, returnSectionLengthID = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnTempSectionLengthSubsetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedSectionLengthSubset/" + str(TempFailedSectionLengthSubsetID), verb = "get", return_params_list = return_params_list)

def modifyTempFailedSectionLengthSubset(TempFailedSectionLengthSubsetID, EntityID = 1, setCode = None, setCodeDescription = None, setCourseLengthCode = None, setCourseLengthCodeDescription = None, setCourseLengthID = None, setDescription = None, setEndDate = None, setIsFullSectionLength = None, setNote = None, setObjectIsDirty = None, setOriginalEndDate = None, setOriginalStartDate = None, setSectionLengthCode = None, setSectionLengthCodeDescription = None, setSectionLengthID = None, setSectionLengthSubsetID = None, setStartDate = None, setTempSectionLengthSubsetID = None, setRelationships = None, returnTempFailedSectionLengthSubsetID = True, returnCode = False, returnCodeDescription = False, returnCourseLengthCode = False, returnCourseLengthCodeDescription = False, returnCourseLengthID = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnIsFullSectionLength = False, returnModifiedTime = False, returnNote = False, returnObjectIsDirty = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnSectionLengthCode = False, returnSectionLengthCodeDescription = False, returnSectionLengthID = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnTempSectionLengthSubsetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedSectionLengthSubset/" + str(TempFailedSectionLengthSubsetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempFailedSectionLengthSubset(EntityID = 1, setCode = None, setCodeDescription = None, setCourseLengthCode = None, setCourseLengthCodeDescription = None, setCourseLengthID = None, setDescription = None, setEndDate = None, setIsFullSectionLength = None, setNote = None, setObjectIsDirty = None, setOriginalEndDate = None, setOriginalStartDate = None, setSectionLengthCode = None, setSectionLengthCodeDescription = None, setSectionLengthID = None, setSectionLengthSubsetID = None, setStartDate = None, setTempSectionLengthSubsetID = None, setRelationships = None, returnTempFailedSectionLengthSubsetID = True, returnCode = False, returnCodeDescription = False, returnCourseLengthCode = False, returnCourseLengthCodeDescription = False, returnCourseLengthID = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnIsFullSectionLength = False, returnModifiedTime = False, returnNote = False, returnObjectIsDirty = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnSectionLengthCode = False, returnSectionLengthCodeDescription = False, returnSectionLengthID = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnTempSectionLengthSubsetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedSectionLengthSubset/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempFailedSectionLengthSubset(TempFailedSectionLengthSubsetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempFailedStudentCourseRequest(EntityID = 1, page = 1, pageSize = 100, returnTempFailedStudentCourseRequestID = True, returnCourseCode = False, returnCourseDepartmentCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseNumericSchoolYear = False, returnCourseSchoolYearDescription = False, returnCourseSubjectCodeDescription = False, returnCreatedTime = False, returnEarnedCredits = False, returnEntityIDRequestedFrom = False, returnErrorMessage = False, returnFailed = False, returnFullStudentNameLFM = False, returnModifiedTime = False, returnNote = False, returnSectionCode = False, returnSectionlengthSubsetCode = False, returnSectionLengthSubsetID = False, returnSelected = False, returnStudentCourseRequestID = False, returnStudentCourseRequestSectionLengthSubsetID = False, returnStudentID = False, returnStudentNumber = False, returnStudentSectionID = False, returnTempStudentCourseRequestID = False, returnTempStudentEnrollmentRecordID = False, returnTempStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentCourseRequest/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempFailedStudentCourseRequest(TempFailedStudentCourseRequestID, EntityID = 1, returnTempFailedStudentCourseRequestID = True, returnCourseCode = False, returnCourseDepartmentCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseNumericSchoolYear = False, returnCourseSchoolYearDescription = False, returnCourseSubjectCodeDescription = False, returnCreatedTime = False, returnEarnedCredits = False, returnEntityIDRequestedFrom = False, returnErrorMessage = False, returnFailed = False, returnFullStudentNameLFM = False, returnModifiedTime = False, returnNote = False, returnSectionCode = False, returnSectionlengthSubsetCode = False, returnSectionLengthSubsetID = False, returnSelected = False, returnStudentCourseRequestID = False, returnStudentCourseRequestSectionLengthSubsetID = False, returnStudentID = False, returnStudentNumber = False, returnStudentSectionID = False, returnTempStudentCourseRequestID = False, returnTempStudentEnrollmentRecordID = False, returnTempStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentCourseRequest/" + str(TempFailedStudentCourseRequestID), verb = "get", return_params_list = return_params_list)

def modifyTempFailedStudentCourseRequest(TempFailedStudentCourseRequestID, EntityID = 1, setCourseCode = None, setCourseDepartmentCodeDescription = None, setCourseDescription = None, setCourseEntityOfferedToID = None, setCourseGradeLevelSummary = None, setCourseID = None, setCourseLengthCode = None, setCourseNumericSchoolYear = None, setCourseSchoolYearDescription = None, setCourseSubjectCodeDescription = None, setEarnedCredits = None, setEntityIDRequestedFrom = None, setErrorMessage = None, setFailed = None, setFullStudentNameLFM = None, setNote = None, setSectionCode = None, setSectionlengthSubsetCode = None, setSectionLengthSubsetID = None, setSelected = None, setStudentCourseRequestID = None, setStudentCourseRequestSectionLengthSubsetID = None, setStudentID = None, setStudentNumber = None, setStudentSectionID = None, setTempStudentCourseRequestID = None, setTempStudentEnrollmentRecordID = None, setTempStudentID = None, setWorkflowAction = None, setWorkflowActionCode = None, setRelationships = None, returnTempFailedStudentCourseRequestID = True, returnCourseCode = False, returnCourseDepartmentCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseNumericSchoolYear = False, returnCourseSchoolYearDescription = False, returnCourseSubjectCodeDescription = False, returnCreatedTime = False, returnEarnedCredits = False, returnEntityIDRequestedFrom = False, returnErrorMessage = False, returnFailed = False, returnFullStudentNameLFM = False, returnModifiedTime = False, returnNote = False, returnSectionCode = False, returnSectionlengthSubsetCode = False, returnSectionLengthSubsetID = False, returnSelected = False, returnStudentCourseRequestID = False, returnStudentCourseRequestSectionLengthSubsetID = False, returnStudentID = False, returnStudentNumber = False, returnStudentSectionID = False, returnTempStudentCourseRequestID = False, returnTempStudentEnrollmentRecordID = False, returnTempStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentCourseRequest/" + str(TempFailedStudentCourseRequestID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempFailedStudentCourseRequest(EntityID = 1, setCourseCode = None, setCourseDepartmentCodeDescription = None, setCourseDescription = None, setCourseEntityOfferedToID = None, setCourseGradeLevelSummary = None, setCourseID = None, setCourseLengthCode = None, setCourseNumericSchoolYear = None, setCourseSchoolYearDescription = None, setCourseSubjectCodeDescription = None, setEarnedCredits = None, setEntityIDRequestedFrom = None, setErrorMessage = None, setFailed = None, setFullStudentNameLFM = None, setNote = None, setSectionCode = None, setSectionlengthSubsetCode = None, setSectionLengthSubsetID = None, setSelected = None, setStudentCourseRequestID = None, setStudentCourseRequestSectionLengthSubsetID = None, setStudentID = None, setStudentNumber = None, setStudentSectionID = None, setTempStudentCourseRequestID = None, setTempStudentEnrollmentRecordID = None, setTempStudentID = None, setWorkflowAction = None, setWorkflowActionCode = None, setRelationships = None, returnTempFailedStudentCourseRequestID = True, returnCourseCode = False, returnCourseDepartmentCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseNumericSchoolYear = False, returnCourseSchoolYearDescription = False, returnCourseSubjectCodeDescription = False, returnCreatedTime = False, returnEarnedCredits = False, returnEntityIDRequestedFrom = False, returnErrorMessage = False, returnFailed = False, returnFullStudentNameLFM = False, returnModifiedTime = False, returnNote = False, returnSectionCode = False, returnSectionlengthSubsetCode = False, returnSectionLengthSubsetID = False, returnSelected = False, returnStudentCourseRequestID = False, returnStudentCourseRequestSectionLengthSubsetID = False, returnStudentID = False, returnStudentNumber = False, returnStudentSectionID = False, returnTempStudentCourseRequestID = False, returnTempStudentEnrollmentRecordID = False, returnTempStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentCourseRequest/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempFailedStudentCourseRequest(TempFailedStudentCourseRequestID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempFailedStudentCourseRequestToReactivate(EntityID = 1, page = 1, pageSize = 100, returnTempFailedStudentCourseRequestToReactivateID = True, returnAlternateRank = False, returnAuditRecordIsRequestable = False, returnAuditRecordIsSchedulable = False, returnCourseCode = False, returnCourseCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnDateFrom = False, returnDateTo = False, returnDays = False, returnEarlyExitReasonCodeDescription = False, returnEarlyExitReasonID = False, returnEarnedCreditOverride = False, returnEarnedCredits = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnEntityIDRequestedFrom = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLink = False, returnGradeReferenceID = False, returnIsAlternate = False, returnIsTransferCourse = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnNameRequestedByLFM = False, returnNote = False, returnPeriod = False, returnPreventReactivateCheckboxFromBeingRendered = False, returnRequestSource = False, returnRequestSourceCode = False, returnRequestStatus = False, returnRequestStatusCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthID = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSectionLengthSubsetID = False, returnStaffFullNameFML = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentCourseRequestIDAlternateFor = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionTransactionID = False, returnTempRecordToReactivatePrimaryKeyValue = False, returnTotalEarnedCreditOverride = False, returnTotalFailedCreditOverride = False, returnTransferCourseName = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditTotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentCourseRequestToReactivate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempFailedStudentCourseRequestToReactivate(TempFailedStudentCourseRequestToReactivateID, EntityID = 1, returnTempFailedStudentCourseRequestToReactivateID = True, returnAlternateRank = False, returnAuditRecordIsRequestable = False, returnAuditRecordIsSchedulable = False, returnCourseCode = False, returnCourseCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnDateFrom = False, returnDateTo = False, returnDays = False, returnEarlyExitReasonCodeDescription = False, returnEarlyExitReasonID = False, returnEarnedCreditOverride = False, returnEarnedCredits = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnEntityIDRequestedFrom = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLink = False, returnGradeReferenceID = False, returnIsAlternate = False, returnIsTransferCourse = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnNameRequestedByLFM = False, returnNote = False, returnPeriod = False, returnPreventReactivateCheckboxFromBeingRendered = False, returnRequestSource = False, returnRequestSourceCode = False, returnRequestStatus = False, returnRequestStatusCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthID = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSectionLengthSubsetID = False, returnStaffFullNameFML = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentCourseRequestIDAlternateFor = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionTransactionID = False, returnTempRecordToReactivatePrimaryKeyValue = False, returnTotalEarnedCreditOverride = False, returnTotalFailedCreditOverride = False, returnTransferCourseName = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditTotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentCourseRequestToReactivate/" + str(TempFailedStudentCourseRequestToReactivateID), verb = "get", return_params_list = return_params_list)

def modifyTempFailedStudentCourseRequestToReactivate(TempFailedStudentCourseRequestToReactivateID, EntityID = 1, setAlternateRank = None, setCourseCode = None, setCourseCodeDescription = None, setCourseDescription = None, setCourseEntityOfferedToID = None, setCourseGradeLevelSummary = None, setCourseID = None, setCurrentEnrollment = None, setDateFrom = None, setDateTo = None, setDays = None, setEarlyExitReasonCodeDescription = None, setEarlyExitReasonID = None, setEarnedCreditOverride = None, setEarnedCredits = None, setEndDate = None, setEntityIDCountsAs = None, setEntityIDCourse = None, setEntityIDRequestedFrom = None, setExcludeFromReportCardsAndTranscripts = None, setExcludeFromStudentSectionLink = None, setGradeReferenceID = None, setIsAlternate = None, setIsTransferCourse = None, setMaximumStudentCount = None, setNameIDRequestedBy = None, setNameRequestedByLFM = None, setNote = None, setPeriod = None, setPreventReactivateCheckboxFromBeingRendered = None, setRequestSource = None, setRequestSourceCode = None, setRequestStatus = None, setRequestStatusCode = None, setSchedulingMethod = None, setSchedulingMethodCode = None, setSchoolYearIDCourse = None, setSectionCode = None, setSectionID = None, setSectionLengthID = None, setSectionLengthSubsetCode = None, setSectionLengthSubsetDescription = None, setSectionLengthSubsetID = None, setStaffFullNameFML = None, setStartDate = None, setStudentCourseRequestID = None, setStudentCourseRequestIDAlternateFor = None, setStudentID = None, setStudentSectionID = None, setStudentSectionTransactionID = None, setTempRecordToReactivatePrimaryKeyValue = None, setTotalEarnedCreditOverride = None, setTotalFailedCreditOverride = None, setTransferCourseName = None, setUseEarnedCreditOverride = None, setUseEarnedCreditTotalOverride = None, setRelationships = None, returnTempFailedStudentCourseRequestToReactivateID = True, returnAlternateRank = False, returnAuditRecordIsRequestable = False, returnAuditRecordIsSchedulable = False, returnCourseCode = False, returnCourseCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnDateFrom = False, returnDateTo = False, returnDays = False, returnEarlyExitReasonCodeDescription = False, returnEarlyExitReasonID = False, returnEarnedCreditOverride = False, returnEarnedCredits = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnEntityIDRequestedFrom = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLink = False, returnGradeReferenceID = False, returnIsAlternate = False, returnIsTransferCourse = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnNameRequestedByLFM = False, returnNote = False, returnPeriod = False, returnPreventReactivateCheckboxFromBeingRendered = False, returnRequestSource = False, returnRequestSourceCode = False, returnRequestStatus = False, returnRequestStatusCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthID = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSectionLengthSubsetID = False, returnStaffFullNameFML = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentCourseRequestIDAlternateFor = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionTransactionID = False, returnTempRecordToReactivatePrimaryKeyValue = False, returnTotalEarnedCreditOverride = False, returnTotalFailedCreditOverride = False, returnTransferCourseName = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditTotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentCourseRequestToReactivate/" + str(TempFailedStudentCourseRequestToReactivateID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempFailedStudentCourseRequestToReactivate(EntityID = 1, setAlternateRank = None, setCourseCode = None, setCourseCodeDescription = None, setCourseDescription = None, setCourseEntityOfferedToID = None, setCourseGradeLevelSummary = None, setCourseID = None, setCurrentEnrollment = None, setDateFrom = None, setDateTo = None, setDays = None, setEarlyExitReasonCodeDescription = None, setEarlyExitReasonID = None, setEarnedCreditOverride = None, setEarnedCredits = None, setEndDate = None, setEntityIDCountsAs = None, setEntityIDCourse = None, setEntityIDRequestedFrom = None, setExcludeFromReportCardsAndTranscripts = None, setExcludeFromStudentSectionLink = None, setGradeReferenceID = None, setIsAlternate = None, setIsTransferCourse = None, setMaximumStudentCount = None, setNameIDRequestedBy = None, setNameRequestedByLFM = None, setNote = None, setPeriod = None, setPreventReactivateCheckboxFromBeingRendered = None, setRequestSource = None, setRequestSourceCode = None, setRequestStatus = None, setRequestStatusCode = None, setSchedulingMethod = None, setSchedulingMethodCode = None, setSchoolYearIDCourse = None, setSectionCode = None, setSectionID = None, setSectionLengthID = None, setSectionLengthSubsetCode = None, setSectionLengthSubsetDescription = None, setSectionLengthSubsetID = None, setStaffFullNameFML = None, setStartDate = None, setStudentCourseRequestID = None, setStudentCourseRequestIDAlternateFor = None, setStudentID = None, setStudentSectionID = None, setStudentSectionTransactionID = None, setTempRecordToReactivatePrimaryKeyValue = None, setTotalEarnedCreditOverride = None, setTotalFailedCreditOverride = None, setTransferCourseName = None, setUseEarnedCreditOverride = None, setUseEarnedCreditTotalOverride = None, setRelationships = None, returnTempFailedStudentCourseRequestToReactivateID = True, returnAlternateRank = False, returnAuditRecordIsRequestable = False, returnAuditRecordIsSchedulable = False, returnCourseCode = False, returnCourseCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnDateFrom = False, returnDateTo = False, returnDays = False, returnEarlyExitReasonCodeDescription = False, returnEarlyExitReasonID = False, returnEarnedCreditOverride = False, returnEarnedCredits = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnEntityIDRequestedFrom = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLink = False, returnGradeReferenceID = False, returnIsAlternate = False, returnIsTransferCourse = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnNameRequestedByLFM = False, returnNote = False, returnPeriod = False, returnPreventReactivateCheckboxFromBeingRendered = False, returnRequestSource = False, returnRequestSourceCode = False, returnRequestStatus = False, returnRequestStatusCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthID = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSectionLengthSubsetID = False, returnStaffFullNameFML = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentCourseRequestIDAlternateFor = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionTransactionID = False, returnTempRecordToReactivatePrimaryKeyValue = False, returnTotalEarnedCreditOverride = False, returnTotalFailedCreditOverride = False, returnTransferCourseName = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditTotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentCourseRequestToReactivate/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempFailedStudentCourseRequestToReactivate(TempFailedStudentCourseRequestToReactivateID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempFailedStudentCourseRequestToReactivateDetail(EntityID = 1, page = 1, pageSize = 100, returnTempFailedStudentCourseRequestToReactivateDetailID = True, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnTempRecordToReactivatePrimaryKeyValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentCourseRequestToReactivateDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempFailedStudentCourseRequestToReactivateDetail(TempFailedStudentCourseRequestToReactivateDetailID, EntityID = 1, returnTempFailedStudentCourseRequestToReactivateDetailID = True, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnTempRecordToReactivatePrimaryKeyValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentCourseRequestToReactivateDetail/" + str(TempFailedStudentCourseRequestToReactivateDetailID), verb = "get", return_params_list = return_params_list)

def modifyTempFailedStudentCourseRequestToReactivateDetail(TempFailedStudentCourseRequestToReactivateDetailID, EntityID = 1, setNote = None, setTempRecordToReactivatePrimaryKeyValue = None, setRelationships = None, returnTempFailedStudentCourseRequestToReactivateDetailID = True, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnTempRecordToReactivatePrimaryKeyValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentCourseRequestToReactivateDetail/" + str(TempFailedStudentCourseRequestToReactivateDetailID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempFailedStudentCourseRequestToReactivateDetail(EntityID = 1, setNote = None, setTempRecordToReactivatePrimaryKeyValue = None, setRelationships = None, returnTempFailedStudentCourseRequestToReactivateDetailID = True, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnTempRecordToReactivatePrimaryKeyValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentCourseRequestToReactivateDetail/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempFailedStudentCourseRequestToReactivateDetail(TempFailedStudentCourseRequestToReactivateDetailID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempFailedStudentSection(EntityID = 1, page = 1, pageSize = 100, returnTempFailedStudentSectionID = True, returnCourseCodeDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnEarlyExitReasonCodeDescription = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNote = False, returnRenderCheckbox = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentGenderCode = False, returnStudentGradeLevelCode = False, returnStudentGradYear = False, returnStudentID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionID = False, returnStudentSectionTransactionIDToUpdate = False, returnTempStudentID = False, returnTempStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempFailedStudentSection(TempFailedStudentSectionID, EntityID = 1, returnTempFailedStudentSectionID = True, returnCourseCodeDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnEarlyExitReasonCodeDescription = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNote = False, returnRenderCheckbox = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentGenderCode = False, returnStudentGradeLevelCode = False, returnStudentGradYear = False, returnStudentID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionID = False, returnStudentSectionTransactionIDToUpdate = False, returnTempStudentID = False, returnTempStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentSection/" + str(TempFailedStudentSectionID), verb = "get", return_params_list = return_params_list)

def modifyTempFailedStudentSection(TempFailedStudentSectionID, EntityID = 1, setCourseCodeDescription = None, setCourseEntityOfferedToID = None, setCourseGradeLevelSummary = None, setCourseID = None, setEarlyExitReasonCodeDescription = None, setEndDate = None, setEntityIDCountsAs = None, setEntityIDCourse = None, setGradeReferenceID = None, setNote = None, setRenderCheckbox = None, setSchoolYearIDCourse = None, setSectionCode = None, setSectionID = None, setStartDate = None, setStudentCourseRequestID = None, setStudentGenderCode = None, setStudentGradeLevelCode = None, setStudentGradYear = None, setStudentID = None, setStudentNameLFM = None, setStudentNumber = None, setStudentSectionID = None, setStudentSectionTransactionIDToUpdate = None, setTempStudentID = None, setTempStudentSectionID = None, setWorkflowAction = None, setWorkflowActionCode = None, setRelationships = None, returnTempFailedStudentSectionID = True, returnCourseCodeDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnEarlyExitReasonCodeDescription = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNote = False, returnRenderCheckbox = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentGenderCode = False, returnStudentGradeLevelCode = False, returnStudentGradYear = False, returnStudentID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionID = False, returnStudentSectionTransactionIDToUpdate = False, returnTempStudentID = False, returnTempStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentSection/" + str(TempFailedStudentSectionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempFailedStudentSection(EntityID = 1, setCourseCodeDescription = None, setCourseEntityOfferedToID = None, setCourseGradeLevelSummary = None, setCourseID = None, setEarlyExitReasonCodeDescription = None, setEndDate = None, setEntityIDCountsAs = None, setEntityIDCourse = None, setGradeReferenceID = None, setNote = None, setRenderCheckbox = None, setSchoolYearIDCourse = None, setSectionCode = None, setSectionID = None, setStartDate = None, setStudentCourseRequestID = None, setStudentGenderCode = None, setStudentGradeLevelCode = None, setStudentGradYear = None, setStudentID = None, setStudentNameLFM = None, setStudentNumber = None, setStudentSectionID = None, setStudentSectionTransactionIDToUpdate = None, setTempStudentID = None, setTempStudentSectionID = None, setWorkflowAction = None, setWorkflowActionCode = None, setRelationships = None, returnTempFailedStudentSectionID = True, returnCourseCodeDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnEarlyExitReasonCodeDescription = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNote = False, returnRenderCheckbox = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentGenderCode = False, returnStudentGradeLevelCode = False, returnStudentGradYear = False, returnStudentID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionID = False, returnStudentSectionTransactionIDToUpdate = False, returnTempStudentID = False, returnTempStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentSection/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempFailedStudentSection(TempFailedStudentSectionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempFailedStudentSectionTransaction(EntityID = 1, page = 1, pageSize = 100, returnTempFailedStudentSectionTransactionID = True, returnCourse = False, returnCreatedTime = False, returnEarlyExitReasonID = False, returnEndDate = False, returnEntityIDCountsAs = False, returnHideNewStudentButton = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnNote = False, returnSectionCode = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionTransactionID = False, returnTempStudentCourseRequestID = False, returnTempStudentCourseRequestToReactivateID = False, returnTempStudentSectionTransactionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentSectionTransaction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempFailedStudentSectionTransaction(TempFailedStudentSectionTransactionID, EntityID = 1, returnTempFailedStudentSectionTransactionID = True, returnCourse = False, returnCreatedTime = False, returnEarlyExitReasonID = False, returnEndDate = False, returnEntityIDCountsAs = False, returnHideNewStudentButton = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnNote = False, returnSectionCode = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionTransactionID = False, returnTempStudentCourseRequestID = False, returnTempStudentCourseRequestToReactivateID = False, returnTempStudentSectionTransactionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentSectionTransaction/" + str(TempFailedStudentSectionTransactionID), verb = "get", return_params_list = return_params_list)

def modifyTempFailedStudentSectionTransaction(TempFailedStudentSectionTransactionID, EntityID = 1, setCourse = None, setEarlyExitReasonID = None, setEndDate = None, setEntityIDCountsAs = None, setHideNewStudentButton = None, setNameIDRequestedBy = None, setNote = None, setSectionCode = None, setSectionLengthSubsetID = None, setStartDate = None, setStudentCourseRequestID = None, setStudentNameLFM = None, setStudentNumber = None, setStudentSectionTransactionID = None, setTempStudentCourseRequestID = None, setTempStudentCourseRequestToReactivateID = None, setTempStudentSectionTransactionID = None, setRelationships = None, returnTempFailedStudentSectionTransactionID = True, returnCourse = False, returnCreatedTime = False, returnEarlyExitReasonID = False, returnEndDate = False, returnEntityIDCountsAs = False, returnHideNewStudentButton = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnNote = False, returnSectionCode = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionTransactionID = False, returnTempStudentCourseRequestID = False, returnTempStudentCourseRequestToReactivateID = False, returnTempStudentSectionTransactionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentSectionTransaction/" + str(TempFailedStudentSectionTransactionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempFailedStudentSectionTransaction(EntityID = 1, setCourse = None, setEarlyExitReasonID = None, setEndDate = None, setEntityIDCountsAs = None, setHideNewStudentButton = None, setNameIDRequestedBy = None, setNote = None, setSectionCode = None, setSectionLengthSubsetID = None, setStartDate = None, setStudentCourseRequestID = None, setStudentNameLFM = None, setStudentNumber = None, setStudentSectionTransactionID = None, setTempStudentCourseRequestID = None, setTempStudentCourseRequestToReactivateID = None, setTempStudentSectionTransactionID = None, setRelationships = None, returnTempFailedStudentSectionTransactionID = True, returnCourse = False, returnCreatedTime = False, returnEarlyExitReasonID = False, returnEndDate = False, returnEntityIDCountsAs = False, returnHideNewStudentButton = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnNote = False, returnSectionCode = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionTransactionID = False, returnTempStudentCourseRequestID = False, returnTempStudentCourseRequestToReactivateID = False, returnTempStudentSectionTransactionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempFailedStudentSectionTransaction/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempFailedStudentSectionTransaction(TempFailedStudentSectionTransactionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempMeet(EntityID = 1, page = 1, pageSize = 100, returnTempMeetID = True, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnEndDate = False, returnMeetID = False, returnModifiedTime = False, returnNewEndDate = False, returnNewSectionLengthCode = False, returnNewStartDate = False, returnPrimaryDays = False, returnPrimaryDisplayPeriod = False, returnPrimaryStaffFullNameFML = False, returnRoomNumberDescription = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempMeet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempMeet(TempMeetID, EntityID = 1, returnTempMeetID = True, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnEndDate = False, returnMeetID = False, returnModifiedTime = False, returnNewEndDate = False, returnNewSectionLengthCode = False, returnNewStartDate = False, returnPrimaryDays = False, returnPrimaryDisplayPeriod = False, returnPrimaryStaffFullNameFML = False, returnRoomNumberDescription = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempMeet/" + str(TempMeetID), verb = "get", return_params_list = return_params_list)

def modifyTempMeet(TempMeetID, EntityID = 1, setCourseCode = None, setCourseDescription = None, setEndDate = None, setMeetID = None, setNewEndDate = None, setNewSectionLengthCode = None, setNewStartDate = None, setPrimaryDays = None, setPrimaryDisplayPeriod = None, setPrimaryStaffFullNameFML = None, setRoomNumberDescription = None, setSectionCode = None, setSectionID = None, setSectionLengthCode = None, setStartDate = None, setRelationships = None, returnTempMeetID = True, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnEndDate = False, returnMeetID = False, returnModifiedTime = False, returnNewEndDate = False, returnNewSectionLengthCode = False, returnNewStartDate = False, returnPrimaryDays = False, returnPrimaryDisplayPeriod = False, returnPrimaryStaffFullNameFML = False, returnRoomNumberDescription = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempMeet/" + str(TempMeetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempMeet(EntityID = 1, setCourseCode = None, setCourseDescription = None, setEndDate = None, setMeetID = None, setNewEndDate = None, setNewSectionLengthCode = None, setNewStartDate = None, setPrimaryDays = None, setPrimaryDisplayPeriod = None, setPrimaryStaffFullNameFML = None, setRoomNumberDescription = None, setSectionCode = None, setSectionID = None, setSectionLengthCode = None, setStartDate = None, setRelationships = None, returnTempMeetID = True, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnEndDate = False, returnMeetID = False, returnModifiedTime = False, returnNewEndDate = False, returnNewSectionLengthCode = False, returnNewStartDate = False, returnPrimaryDays = False, returnPrimaryDisplayPeriod = False, returnPrimaryStaffFullNameFML = False, returnRoomNumberDescription = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempMeet/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempMeet(TempMeetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempSchedulingTeamGradeReference(EntityID = 1, page = 1, pageSize = 100, returnTempSchedulingTeamGradeReferenceID = True, returnCode = False, returnCreatedTime = False, returnCurrentStudentCount = False, returnDescription = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnOverrideTotalToBeAssignedCount = False, returnOverrideTotalToBeAssignedPercent = False, returnSchedulingTeamGradeReferenceID = False, returnSchedulingTeamID = False, returnSortOrder = False, returnTotalStudents = False, returnTotalToBeAssignedCount = False, returnTotalToBeAssignedPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSchedulingTeamGradeReference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempSchedulingTeamGradeReference(TempSchedulingTeamGradeReferenceID, EntityID = 1, returnTempSchedulingTeamGradeReferenceID = True, returnCode = False, returnCreatedTime = False, returnCurrentStudentCount = False, returnDescription = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnOverrideTotalToBeAssignedCount = False, returnOverrideTotalToBeAssignedPercent = False, returnSchedulingTeamGradeReferenceID = False, returnSchedulingTeamID = False, returnSortOrder = False, returnTotalStudents = False, returnTotalToBeAssignedCount = False, returnTotalToBeAssignedPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSchedulingTeamGradeReference/" + str(TempSchedulingTeamGradeReferenceID), verb = "get", return_params_list = return_params_list)

def modifyTempSchedulingTeamGradeReference(TempSchedulingTeamGradeReferenceID, EntityID = 1, setCode = None, setCurrentStudentCount = None, setDescription = None, setMaximumStudentCount = None, setOverrideTotalToBeAssignedCount = None, setOverrideTotalToBeAssignedPercent = None, setSchedulingTeamGradeReferenceID = None, setSchedulingTeamID = None, setSortOrder = None, setTotalStudents = None, setTotalToBeAssignedCount = None, setTotalToBeAssignedPercent = None, setRelationships = None, returnTempSchedulingTeamGradeReferenceID = True, returnCode = False, returnCreatedTime = False, returnCurrentStudentCount = False, returnDescription = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnOverrideTotalToBeAssignedCount = False, returnOverrideTotalToBeAssignedPercent = False, returnSchedulingTeamGradeReferenceID = False, returnSchedulingTeamID = False, returnSortOrder = False, returnTotalStudents = False, returnTotalToBeAssignedCount = False, returnTotalToBeAssignedPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSchedulingTeamGradeReference/" + str(TempSchedulingTeamGradeReferenceID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempSchedulingTeamGradeReference(EntityID = 1, setCode = None, setCurrentStudentCount = None, setDescription = None, setMaximumStudentCount = None, setOverrideTotalToBeAssignedCount = None, setOverrideTotalToBeAssignedPercent = None, setSchedulingTeamGradeReferenceID = None, setSchedulingTeamID = None, setSortOrder = None, setTotalStudents = None, setTotalToBeAssignedCount = None, setTotalToBeAssignedPercent = None, setRelationships = None, returnTempSchedulingTeamGradeReferenceID = True, returnCode = False, returnCreatedTime = False, returnCurrentStudentCount = False, returnDescription = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnOverrideTotalToBeAssignedCount = False, returnOverrideTotalToBeAssignedPercent = False, returnSchedulingTeamGradeReferenceID = False, returnSchedulingTeamID = False, returnSortOrder = False, returnTotalStudents = False, returnTotalToBeAssignedCount = False, returnTotalToBeAssignedPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSchedulingTeamGradeReference/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempSchedulingTeamGradeReference(TempSchedulingTeamGradeReferenceID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempSection(EntityID = 1, page = 1, pageSize = 100, returnTempSectionID = True, returnCourse = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseID = False, returnCourseIsActive = False, returnCourseTypeCode = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnEntityIDCourse = False, returnEntityIDOfferedTo = False, returnGradeLevelSummary = False, returnIsActive = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNewCourseLengthCode = False, returnNewCourseLengthID = False, returnNewSectionLengthCode = False, returnNewSectionLengthID = False, returnNote = False, returnNumberOfTransferStudentSections = False, returnPeriodDaySummary = False, returnPrimaryDays = False, returnPrimaryDisplayPeriod = False, returnRowIsReadOnly = False, returnRowIsSelected = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnSectionLengthEndDate = False, returnSectionLengthID = False, returnSectionLengthStartDate = False, returnStaffFullNameFML = False, returnTargetCourse = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempSection(TempSectionID, EntityID = 1, returnTempSectionID = True, returnCourse = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseID = False, returnCourseIsActive = False, returnCourseTypeCode = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnEntityIDCourse = False, returnEntityIDOfferedTo = False, returnGradeLevelSummary = False, returnIsActive = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNewCourseLengthCode = False, returnNewCourseLengthID = False, returnNewSectionLengthCode = False, returnNewSectionLengthID = False, returnNote = False, returnNumberOfTransferStudentSections = False, returnPeriodDaySummary = False, returnPrimaryDays = False, returnPrimaryDisplayPeriod = False, returnRowIsReadOnly = False, returnRowIsSelected = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnSectionLengthEndDate = False, returnSectionLengthID = False, returnSectionLengthStartDate = False, returnStaffFullNameFML = False, returnTargetCourse = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSection/" + str(TempSectionID), verb = "get", return_params_list = return_params_list)

def modifyTempSection(TempSectionID, EntityID = 1, setCourse = None, setCourseDescription = None, setCourseEntityOfferedToID = None, setCourseID = None, setCourseIsActive = None, setCourseTypeCode = None, setCurrentEnrollment = None, setEntityIDCourse = None, setEntityIDOfferedTo = None, setGradeLevelSummary = None, setIsActive = None, setMaximumStudentCount = None, setNewCourseLengthCode = None, setNewCourseLengthID = None, setNewSectionLengthCode = None, setNewSectionLengthID = None, setNote = None, setNumberOfTransferStudentSections = None, setPeriodDaySummary = None, setPrimaryDays = None, setPrimaryDisplayPeriod = None, setRowIsReadOnly = None, setRowIsSelected = None, setSchoolYearIDCourse = None, setSectionCode = None, setSectionID = None, setSectionLengthCode = None, setSectionLengthEndDate = None, setSectionLengthID = None, setSectionLengthStartDate = None, setStaffFullNameFML = None, setTargetCourse = None, setRelationships = None, returnTempSectionID = True, returnCourse = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseID = False, returnCourseIsActive = False, returnCourseTypeCode = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnEntityIDCourse = False, returnEntityIDOfferedTo = False, returnGradeLevelSummary = False, returnIsActive = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNewCourseLengthCode = False, returnNewCourseLengthID = False, returnNewSectionLengthCode = False, returnNewSectionLengthID = False, returnNote = False, returnNumberOfTransferStudentSections = False, returnPeriodDaySummary = False, returnPrimaryDays = False, returnPrimaryDisplayPeriod = False, returnRowIsReadOnly = False, returnRowIsSelected = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnSectionLengthEndDate = False, returnSectionLengthID = False, returnSectionLengthStartDate = False, returnStaffFullNameFML = False, returnTargetCourse = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSection/" + str(TempSectionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempSection(EntityID = 1, setCourse = None, setCourseDescription = None, setCourseEntityOfferedToID = None, setCourseID = None, setCourseIsActive = None, setCourseTypeCode = None, setCurrentEnrollment = None, setEntityIDCourse = None, setEntityIDOfferedTo = None, setGradeLevelSummary = None, setIsActive = None, setMaximumStudentCount = None, setNewCourseLengthCode = None, setNewCourseLengthID = None, setNewSectionLengthCode = None, setNewSectionLengthID = None, setNote = None, setNumberOfTransferStudentSections = None, setPeriodDaySummary = None, setPrimaryDays = None, setPrimaryDisplayPeriod = None, setRowIsReadOnly = None, setRowIsSelected = None, setSchoolYearIDCourse = None, setSectionCode = None, setSectionID = None, setSectionLengthCode = None, setSectionLengthEndDate = None, setSectionLengthID = None, setSectionLengthStartDate = None, setStaffFullNameFML = None, setTargetCourse = None, setRelationships = None, returnTempSectionID = True, returnCourse = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseID = False, returnCourseIsActive = False, returnCourseTypeCode = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnEntityIDCourse = False, returnEntityIDOfferedTo = False, returnGradeLevelSummary = False, returnIsActive = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNewCourseLengthCode = False, returnNewCourseLengthID = False, returnNewSectionLengthCode = False, returnNewSectionLengthID = False, returnNote = False, returnNumberOfTransferStudentSections = False, returnPeriodDaySummary = False, returnPrimaryDays = False, returnPrimaryDisplayPeriod = False, returnRowIsReadOnly = False, returnRowIsSelected = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnSectionLengthEndDate = False, returnSectionLengthID = False, returnSectionLengthStartDate = False, returnStaffFullNameFML = False, returnTargetCourse = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSection/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempSection(TempSectionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempSectionLength(EntityID = 1, page = 1, pageSize = 100, returnTempSectionLengthID = True, returnCode = False, returnCourseLengthCode = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnSectionLengthID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSectionLength/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempSectionLength(TempSectionLengthID, EntityID = 1, returnTempSectionLengthID = True, returnCode = False, returnCourseLengthCode = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnSectionLengthID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSectionLength/" + str(TempSectionLengthID), verb = "get", return_params_list = return_params_list)

def modifyTempSectionLength(TempSectionLengthID, EntityID = 1, setCode = None, setCourseLengthCode = None, setEndDate = None, setOriginalEndDate = None, setOriginalStartDate = None, setSectionLengthID = None, setStartDate = None, setRelationships = None, returnTempSectionLengthID = True, returnCode = False, returnCourseLengthCode = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnSectionLengthID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSectionLength/" + str(TempSectionLengthID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempSectionLength(EntityID = 1, setCode = None, setCourseLengthCode = None, setEndDate = None, setOriginalEndDate = None, setOriginalStartDate = None, setSectionLengthID = None, setStartDate = None, setRelationships = None, returnTempSectionLengthID = True, returnCode = False, returnCourseLengthCode = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnSectionLengthID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSectionLength/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempSectionLength(TempSectionLengthID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempSectionLengthSubset(EntityID = 1, page = 1, pageSize = 100, returnTempSectionLengthSubsetID = True, returnCode = False, returnCodeDescription = False, returnCourseLengthCode = False, returnCourseLengthCodeDescription = False, returnCourseLengthID = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnIsFullSectionLength = False, returnModifiedTime = False, returnObjectIsDirty = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnSectionLengthCode = False, returnSectionLengthCodeDescription = False, returnSectionLengthID = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSectionLengthSubset/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempSectionLengthSubset(TempSectionLengthSubsetID, EntityID = 1, returnTempSectionLengthSubsetID = True, returnCode = False, returnCodeDescription = False, returnCourseLengthCode = False, returnCourseLengthCodeDescription = False, returnCourseLengthID = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnIsFullSectionLength = False, returnModifiedTime = False, returnObjectIsDirty = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnSectionLengthCode = False, returnSectionLengthCodeDescription = False, returnSectionLengthID = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSectionLengthSubset/" + str(TempSectionLengthSubsetID), verb = "get", return_params_list = return_params_list)

def modifyTempSectionLengthSubset(TempSectionLengthSubsetID, EntityID = 1, setCode = None, setCodeDescription = None, setCourseLengthCode = None, setCourseLengthCodeDescription = None, setCourseLengthID = None, setDescription = None, setEndDate = None, setIsFullSectionLength = None, setObjectIsDirty = None, setOriginalEndDate = None, setOriginalStartDate = None, setSectionLengthCode = None, setSectionLengthCodeDescription = None, setSectionLengthID = None, setSectionLengthSubsetID = None, setStartDate = None, setRelationships = None, returnTempSectionLengthSubsetID = True, returnCode = False, returnCodeDescription = False, returnCourseLengthCode = False, returnCourseLengthCodeDescription = False, returnCourseLengthID = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnIsFullSectionLength = False, returnModifiedTime = False, returnObjectIsDirty = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnSectionLengthCode = False, returnSectionLengthCodeDescription = False, returnSectionLengthID = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSectionLengthSubset/" + str(TempSectionLengthSubsetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempSectionLengthSubset(EntityID = 1, setCode = None, setCodeDescription = None, setCourseLengthCode = None, setCourseLengthCodeDescription = None, setCourseLengthID = None, setDescription = None, setEndDate = None, setIsFullSectionLength = None, setObjectIsDirty = None, setOriginalEndDate = None, setOriginalStartDate = None, setSectionLengthCode = None, setSectionLengthCodeDescription = None, setSectionLengthID = None, setSectionLengthSubsetID = None, setStartDate = None, setRelationships = None, returnTempSectionLengthSubsetID = True, returnCode = False, returnCodeDescription = False, returnCourseLengthCode = False, returnCourseLengthCodeDescription = False, returnCourseLengthID = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnIsFullSectionLength = False, returnModifiedTime = False, returnObjectIsDirty = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnSectionLengthCode = False, returnSectionLengthCodeDescription = False, returnSectionLengthID = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSectionLengthSubset/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempSectionLengthSubset(TempSectionLengthSubsetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStaffMeet(EntityID = 1, page = 1, pageSize = 100, returnTempStaffMeetID = True, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnEffectiveEndDate = False, returnEffectiveStartDate = False, returnIsLongTermSubstitute = False, returnIsPrimary = False, returnIsSubstitute = False, returnMeetID = False, returnModifiedTime = False, returnNewEffectiveEndDate = False, returnNewEffectiveStartDate = False, returnSectionCode = False, returnSectionID = False, returnStaffFullNameFML = False, returnStaffID = False, returnStaffMeetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStaffMeet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStaffMeet(TempStaffMeetID, EntityID = 1, returnTempStaffMeetID = True, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnEffectiveEndDate = False, returnEffectiveStartDate = False, returnIsLongTermSubstitute = False, returnIsPrimary = False, returnIsSubstitute = False, returnMeetID = False, returnModifiedTime = False, returnNewEffectiveEndDate = False, returnNewEffectiveStartDate = False, returnSectionCode = False, returnSectionID = False, returnStaffFullNameFML = False, returnStaffID = False, returnStaffMeetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStaffMeet/" + str(TempStaffMeetID), verb = "get", return_params_list = return_params_list)

def modifyTempStaffMeet(TempStaffMeetID, EntityID = 1, setCourseCode = None, setCourseDescription = None, setEffectiveEndDate = None, setEffectiveStartDate = None, setIsLongTermSubstitute = None, setIsPrimary = None, setIsSubstitute = None, setMeetID = None, setNewEffectiveEndDate = None, setNewEffectiveStartDate = None, setSectionCode = None, setSectionID = None, setStaffFullNameFML = None, setStaffID = None, setStaffMeetID = None, setRelationships = None, returnTempStaffMeetID = True, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnEffectiveEndDate = False, returnEffectiveStartDate = False, returnIsLongTermSubstitute = False, returnIsPrimary = False, returnIsSubstitute = False, returnMeetID = False, returnModifiedTime = False, returnNewEffectiveEndDate = False, returnNewEffectiveStartDate = False, returnSectionCode = False, returnSectionID = False, returnStaffFullNameFML = False, returnStaffID = False, returnStaffMeetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStaffMeet/" + str(TempStaffMeetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStaffMeet(EntityID = 1, setCourseCode = None, setCourseDescription = None, setEffectiveEndDate = None, setEffectiveStartDate = None, setIsLongTermSubstitute = None, setIsPrimary = None, setIsSubstitute = None, setMeetID = None, setNewEffectiveEndDate = None, setNewEffectiveStartDate = None, setSectionCode = None, setSectionID = None, setStaffFullNameFML = None, setStaffID = None, setStaffMeetID = None, setRelationships = None, returnTempStaffMeetID = True, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnEffectiveEndDate = False, returnEffectiveStartDate = False, returnIsLongTermSubstitute = False, returnIsPrimary = False, returnIsSubstitute = False, returnMeetID = False, returnModifiedTime = False, returnNewEffectiveEndDate = False, returnNewEffectiveStartDate = False, returnSectionCode = False, returnSectionID = False, returnStaffFullNameFML = False, returnStaffID = False, returnStaffMeetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStaffMeet/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStaffMeet(TempStaffMeetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudent(EntityID = 1, page = 1, pageSize = 100, returnTempStudentID = True, returnCourseRequestCount = False, returnCreatedTime = False, returnCurrentActive = False, returnFullNameLFM = False, returnGenderCode = False, returnGradeLevelCode = False, returnGradeReferenceID = False, returnGradYear = False, returnHasConflictedStudentCourseRequest = False, returnHasFailedUpdate = False, returnHomeRoomCode = False, returnIsSelected = False, returnModifiedTime = False, returnSchoolName = False, returnStudentID = False, returnStudentNumber = False, returnStudentSectionCount = False, returnStudentTypeCodeDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudent(TempStudentID, EntityID = 1, returnTempStudentID = True, returnCourseRequestCount = False, returnCreatedTime = False, returnCurrentActive = False, returnFullNameLFM = False, returnGenderCode = False, returnGradeLevelCode = False, returnGradeReferenceID = False, returnGradYear = False, returnHasConflictedStudentCourseRequest = False, returnHasFailedUpdate = False, returnHomeRoomCode = False, returnIsSelected = False, returnModifiedTime = False, returnSchoolName = False, returnStudentID = False, returnStudentNumber = False, returnStudentSectionCount = False, returnStudentTypeCodeDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudent/" + str(TempStudentID), verb = "get", return_params_list = return_params_list)

def modifyTempStudent(TempStudentID, EntityID = 1, setCourseRequestCount = None, setCurrentActive = None, setFullNameLFM = None, setGenderCode = None, setGradeLevelCode = None, setGradeReferenceID = None, setGradYear = None, setHasConflictedStudentCourseRequest = None, setHasFailedUpdate = None, setHomeRoomCode = None, setIsSelected = None, setSchoolName = None, setStudentID = None, setStudentNumber = None, setStudentSectionCount = None, setStudentTypeCodeDescription = None, setRelationships = None, returnTempStudentID = True, returnCourseRequestCount = False, returnCreatedTime = False, returnCurrentActive = False, returnFullNameLFM = False, returnGenderCode = False, returnGradeLevelCode = False, returnGradeReferenceID = False, returnGradYear = False, returnHasConflictedStudentCourseRequest = False, returnHasFailedUpdate = False, returnHomeRoomCode = False, returnIsSelected = False, returnModifiedTime = False, returnSchoolName = False, returnStudentID = False, returnStudentNumber = False, returnStudentSectionCount = False, returnStudentTypeCodeDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudent/" + str(TempStudentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudent(EntityID = 1, setCourseRequestCount = None, setCurrentActive = None, setFullNameLFM = None, setGenderCode = None, setGradeLevelCode = None, setGradeReferenceID = None, setGradYear = None, setHasConflictedStudentCourseRequest = None, setHasFailedUpdate = None, setHomeRoomCode = None, setIsSelected = None, setSchoolName = None, setStudentID = None, setStudentNumber = None, setStudentSectionCount = None, setStudentTypeCodeDescription = None, setRelationships = None, returnTempStudentID = True, returnCourseRequestCount = False, returnCreatedTime = False, returnCurrentActive = False, returnFullNameLFM = False, returnGenderCode = False, returnGradeLevelCode = False, returnGradeReferenceID = False, returnGradYear = False, returnHasConflictedStudentCourseRequest = False, returnHasFailedUpdate = False, returnHomeRoomCode = False, returnIsSelected = False, returnModifiedTime = False, returnSchoolName = False, returnStudentID = False, returnStudentNumber = False, returnStudentSectionCount = False, returnStudentTypeCodeDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudent/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudent(TempStudentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentCourseRequest(EntityID = 1, page = 1, pageSize = 100, returnTempStudentCourseRequestID = True, returnCourseCode = False, returnCourseDepartmentCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseNumericSchoolYear = False, returnCourseSchoolYearDescription = False, returnCourseSubjectCodeDescription = False, returnCreatedTime = False, returnEarnedCredits = False, returnEntityIDRequestedFrom = False, returnErrorMessage = False, returnFailed = False, returnFullStudentNameLFM = False, returnModifiedTime = False, returnSectionCode = False, returnSectionlengthSubsetCode = False, returnSectionLengthSubsetID = False, returnSelected = False, returnStudentCourseRequestID = False, returnStudentCourseRequestSectionLengthSubsetID = False, returnStudentID = False, returnStudentNumber = False, returnStudentSectionID = False, returnTempStudentEnrollmentRecordID = False, returnTempStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentCourseRequest/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentCourseRequest(TempStudentCourseRequestID, EntityID = 1, returnTempStudentCourseRequestID = True, returnCourseCode = False, returnCourseDepartmentCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseNumericSchoolYear = False, returnCourseSchoolYearDescription = False, returnCourseSubjectCodeDescription = False, returnCreatedTime = False, returnEarnedCredits = False, returnEntityIDRequestedFrom = False, returnErrorMessage = False, returnFailed = False, returnFullStudentNameLFM = False, returnModifiedTime = False, returnSectionCode = False, returnSectionlengthSubsetCode = False, returnSectionLengthSubsetID = False, returnSelected = False, returnStudentCourseRequestID = False, returnStudentCourseRequestSectionLengthSubsetID = False, returnStudentID = False, returnStudentNumber = False, returnStudentSectionID = False, returnTempStudentEnrollmentRecordID = False, returnTempStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentCourseRequest/" + str(TempStudentCourseRequestID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentCourseRequest(TempStudentCourseRequestID, EntityID = 1, setCourseCode = None, setCourseDepartmentCodeDescription = None, setCourseDescription = None, setCourseEntityOfferedToID = None, setCourseGradeLevelSummary = None, setCourseID = None, setCourseLengthCode = None, setCourseNumericSchoolYear = None, setCourseSchoolYearDescription = None, setCourseSubjectCodeDescription = None, setEarnedCredits = None, setEntityIDRequestedFrom = None, setErrorMessage = None, setFailed = None, setFullStudentNameLFM = None, setSectionCode = None, setSectionlengthSubsetCode = None, setSectionLengthSubsetID = None, setSelected = None, setStudentCourseRequestID = None, setStudentCourseRequestSectionLengthSubsetID = None, setStudentID = None, setStudentNumber = None, setStudentSectionID = None, setTempStudentEnrollmentRecordID = None, setTempStudentID = None, setWorkflowAction = None, setWorkflowActionCode = None, setRelationships = None, returnTempStudentCourseRequestID = True, returnCourseCode = False, returnCourseDepartmentCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseNumericSchoolYear = False, returnCourseSchoolYearDescription = False, returnCourseSubjectCodeDescription = False, returnCreatedTime = False, returnEarnedCredits = False, returnEntityIDRequestedFrom = False, returnErrorMessage = False, returnFailed = False, returnFullStudentNameLFM = False, returnModifiedTime = False, returnSectionCode = False, returnSectionlengthSubsetCode = False, returnSectionLengthSubsetID = False, returnSelected = False, returnStudentCourseRequestID = False, returnStudentCourseRequestSectionLengthSubsetID = False, returnStudentID = False, returnStudentNumber = False, returnStudentSectionID = False, returnTempStudentEnrollmentRecordID = False, returnTempStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentCourseRequest/" + str(TempStudentCourseRequestID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentCourseRequest(EntityID = 1, setCourseCode = None, setCourseDepartmentCodeDescription = None, setCourseDescription = None, setCourseEntityOfferedToID = None, setCourseGradeLevelSummary = None, setCourseID = None, setCourseLengthCode = None, setCourseNumericSchoolYear = None, setCourseSchoolYearDescription = None, setCourseSubjectCodeDescription = None, setEarnedCredits = None, setEntityIDRequestedFrom = None, setErrorMessage = None, setFailed = None, setFullStudentNameLFM = None, setSectionCode = None, setSectionlengthSubsetCode = None, setSectionLengthSubsetID = None, setSelected = None, setStudentCourseRequestID = None, setStudentCourseRequestSectionLengthSubsetID = None, setStudentID = None, setStudentNumber = None, setStudentSectionID = None, setTempStudentEnrollmentRecordID = None, setTempStudentID = None, setWorkflowAction = None, setWorkflowActionCode = None, setRelationships = None, returnTempStudentCourseRequestID = True, returnCourseCode = False, returnCourseDepartmentCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCourseLengthCode = False, returnCourseNumericSchoolYear = False, returnCourseSchoolYearDescription = False, returnCourseSubjectCodeDescription = False, returnCreatedTime = False, returnEarnedCredits = False, returnEntityIDRequestedFrom = False, returnErrorMessage = False, returnFailed = False, returnFullStudentNameLFM = False, returnModifiedTime = False, returnSectionCode = False, returnSectionlengthSubsetCode = False, returnSectionLengthSubsetID = False, returnSelected = False, returnStudentCourseRequestID = False, returnStudentCourseRequestSectionLengthSubsetID = False, returnStudentID = False, returnStudentNumber = False, returnStudentSectionID = False, returnTempStudentEnrollmentRecordID = False, returnTempStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentCourseRequest/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentCourseRequest(TempStudentCourseRequestID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentCourseRequestSectionLengthSubset(EntityID = 1, page = 1, pageSize = 100, returnTempStudentCourseRequestSectionLengthSubsetID = True, returnCreatedTime = False, returnModifiedTime = False, returnSectionLengthSubsetID = False, returnStudentCourseRequestID = False, returnStudentCourseRequestSectionLengthSubsetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentCourseRequestSectionLengthSubset/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentCourseRequestSectionLengthSubset(TempStudentCourseRequestSectionLengthSubsetID, EntityID = 1, returnTempStudentCourseRequestSectionLengthSubsetID = True, returnCreatedTime = False, returnModifiedTime = False, returnSectionLengthSubsetID = False, returnStudentCourseRequestID = False, returnStudentCourseRequestSectionLengthSubsetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentCourseRequestSectionLengthSubset/" + str(TempStudentCourseRequestSectionLengthSubsetID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentCourseRequestSectionLengthSubset(TempStudentCourseRequestSectionLengthSubsetID, EntityID = 1, setSectionLengthSubsetID = None, setStudentCourseRequestID = None, setStudentCourseRequestSectionLengthSubsetID = None, setRelationships = None, returnTempStudentCourseRequestSectionLengthSubsetID = True, returnCreatedTime = False, returnModifiedTime = False, returnSectionLengthSubsetID = False, returnStudentCourseRequestID = False, returnStudentCourseRequestSectionLengthSubsetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentCourseRequestSectionLengthSubset/" + str(TempStudentCourseRequestSectionLengthSubsetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentCourseRequestSectionLengthSubset(EntityID = 1, setSectionLengthSubsetID = None, setStudentCourseRequestID = None, setStudentCourseRequestSectionLengthSubsetID = None, setRelationships = None, returnTempStudentCourseRequestSectionLengthSubsetID = True, returnCreatedTime = False, returnModifiedTime = False, returnSectionLengthSubsetID = False, returnStudentCourseRequestID = False, returnStudentCourseRequestSectionLengthSubsetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentCourseRequestSectionLengthSubset/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentCourseRequestSectionLengthSubset(TempStudentCourseRequestSectionLengthSubsetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentCourseRequestToReactivateMN(EntityID = 1, page = 1, pageSize = 100, returnTempStudentCourseRequestToReactivateMNID = True, returnAlternateRank = False, returnAuditRecordIsRequestable = False, returnAuditRecordIsSchedulable = False, returnCourseCode = False, returnCourseCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnDateFrom = False, returnDateTo = False, returnDays = False, returnEarlyExitReasonCodeDescription = False, returnEarlyExitReasonID = False, returnEarnedCreditOverride = False, returnEarnedCredits = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnEntityIDRequestedFrom = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLink = False, returnGradeReferenceID = False, returnIsAlternate = False, returnIsTransferCourse = False, returnIsTSAProficient = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnNameRequestedByLFM = False, returnPeriod = False, returnPreventReactivateCheckboxFromBeingRendered = False, returnRequestSource = False, returnRequestSourceCode = False, returnRequestStatus = False, returnRequestStatusCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthID = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSectionLengthSubsetID = False, returnStaffFullNameFML = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentCourseRequestIDAlternateFor = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionTransactionID = False, returnTotalEarnedCreditOverride = False, returnTotalFailedCreditOverride = False, returnTransferCourseName = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditTotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentCourseRequestToReactivateMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentCourseRequestToReactivateMN(TempStudentCourseRequestToReactivateMNID, EntityID = 1, returnTempStudentCourseRequestToReactivateMNID = True, returnAlternateRank = False, returnAuditRecordIsRequestable = False, returnAuditRecordIsSchedulable = False, returnCourseCode = False, returnCourseCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnDateFrom = False, returnDateTo = False, returnDays = False, returnEarlyExitReasonCodeDescription = False, returnEarlyExitReasonID = False, returnEarnedCreditOverride = False, returnEarnedCredits = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnEntityIDRequestedFrom = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLink = False, returnGradeReferenceID = False, returnIsAlternate = False, returnIsTransferCourse = False, returnIsTSAProficient = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnNameRequestedByLFM = False, returnPeriod = False, returnPreventReactivateCheckboxFromBeingRendered = False, returnRequestSource = False, returnRequestSourceCode = False, returnRequestStatus = False, returnRequestStatusCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthID = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSectionLengthSubsetID = False, returnStaffFullNameFML = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentCourseRequestIDAlternateFor = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionTransactionID = False, returnTotalEarnedCreditOverride = False, returnTotalFailedCreditOverride = False, returnTransferCourseName = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditTotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentCourseRequestToReactivateMN/" + str(TempStudentCourseRequestToReactivateMNID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentCourseRequestToReactivateMN(TempStudentCourseRequestToReactivateMNID, EntityID = 1, setAlternateRank = None, setCourseCode = None, setCourseCodeDescription = None, setCourseDescription = None, setCourseEntityOfferedToID = None, setCourseGradeLevelSummary = None, setCourseID = None, setCurrentEnrollment = None, setDateFrom = None, setDateTo = None, setDays = None, setEarlyExitReasonCodeDescription = None, setEarlyExitReasonID = None, setEarnedCreditOverride = None, setEarnedCredits = None, setEndDate = None, setEntityIDCountsAs = None, setEntityIDCourse = None, setEntityIDRequestedFrom = None, setExcludeFromReportCardsAndTranscripts = None, setExcludeFromStudentSectionLink = None, setGradeReferenceID = None, setIsAlternate = None, setIsTransferCourse = None, setIsTSAProficient = None, setMaximumStudentCount = None, setNameIDRequestedBy = None, setNameRequestedByLFM = None, setPeriod = None, setPreventReactivateCheckboxFromBeingRendered = None, setRequestSource = None, setRequestSourceCode = None, setRequestStatus = None, setRequestStatusCode = None, setSchedulingMethod = None, setSchedulingMethodCode = None, setSchoolYearIDCourse = None, setSectionCode = None, setSectionID = None, setSectionLengthID = None, setSectionLengthSubsetCode = None, setSectionLengthSubsetDescription = None, setSectionLengthSubsetID = None, setStaffFullNameFML = None, setStartDate = None, setStudentCourseRequestID = None, setStudentCourseRequestIDAlternateFor = None, setStudentID = None, setStudentSectionID = None, setStudentSectionTransactionID = None, setTotalEarnedCreditOverride = None, setTotalFailedCreditOverride = None, setTransferCourseName = None, setUseEarnedCreditOverride = None, setUseEarnedCreditTotalOverride = None, setRelationships = None, returnTempStudentCourseRequestToReactivateMNID = True, returnAlternateRank = False, returnAuditRecordIsRequestable = False, returnAuditRecordIsSchedulable = False, returnCourseCode = False, returnCourseCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnDateFrom = False, returnDateTo = False, returnDays = False, returnEarlyExitReasonCodeDescription = False, returnEarlyExitReasonID = False, returnEarnedCreditOverride = False, returnEarnedCredits = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnEntityIDRequestedFrom = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLink = False, returnGradeReferenceID = False, returnIsAlternate = False, returnIsTransferCourse = False, returnIsTSAProficient = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnNameRequestedByLFM = False, returnPeriod = False, returnPreventReactivateCheckboxFromBeingRendered = False, returnRequestSource = False, returnRequestSourceCode = False, returnRequestStatus = False, returnRequestStatusCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthID = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSectionLengthSubsetID = False, returnStaffFullNameFML = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentCourseRequestIDAlternateFor = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionTransactionID = False, returnTotalEarnedCreditOverride = False, returnTotalFailedCreditOverride = False, returnTransferCourseName = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditTotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentCourseRequestToReactivateMN/" + str(TempStudentCourseRequestToReactivateMNID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentCourseRequestToReactivateMN(EntityID = 1, setAlternateRank = None, setCourseCode = None, setCourseCodeDescription = None, setCourseDescription = None, setCourseEntityOfferedToID = None, setCourseGradeLevelSummary = None, setCourseID = None, setCurrentEnrollment = None, setDateFrom = None, setDateTo = None, setDays = None, setEarlyExitReasonCodeDescription = None, setEarlyExitReasonID = None, setEarnedCreditOverride = None, setEarnedCredits = None, setEndDate = None, setEntityIDCountsAs = None, setEntityIDCourse = None, setEntityIDRequestedFrom = None, setExcludeFromReportCardsAndTranscripts = None, setExcludeFromStudentSectionLink = None, setGradeReferenceID = None, setIsAlternate = None, setIsTransferCourse = None, setIsTSAProficient = None, setMaximumStudentCount = None, setNameIDRequestedBy = None, setNameRequestedByLFM = None, setPeriod = None, setPreventReactivateCheckboxFromBeingRendered = None, setRequestSource = None, setRequestSourceCode = None, setRequestStatus = None, setRequestStatusCode = None, setSchedulingMethod = None, setSchedulingMethodCode = None, setSchoolYearIDCourse = None, setSectionCode = None, setSectionID = None, setSectionLengthID = None, setSectionLengthSubsetCode = None, setSectionLengthSubsetDescription = None, setSectionLengthSubsetID = None, setStaffFullNameFML = None, setStartDate = None, setStudentCourseRequestID = None, setStudentCourseRequestIDAlternateFor = None, setStudentID = None, setStudentSectionID = None, setStudentSectionTransactionID = None, setTotalEarnedCreditOverride = None, setTotalFailedCreditOverride = None, setTransferCourseName = None, setUseEarnedCreditOverride = None, setUseEarnedCreditTotalOverride = None, setRelationships = None, returnTempStudentCourseRequestToReactivateMNID = True, returnAlternateRank = False, returnAuditRecordIsRequestable = False, returnAuditRecordIsSchedulable = False, returnCourseCode = False, returnCourseCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnDateFrom = False, returnDateTo = False, returnDays = False, returnEarlyExitReasonCodeDescription = False, returnEarlyExitReasonID = False, returnEarnedCreditOverride = False, returnEarnedCredits = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnEntityIDRequestedFrom = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLink = False, returnGradeReferenceID = False, returnIsAlternate = False, returnIsTransferCourse = False, returnIsTSAProficient = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnNameRequestedByLFM = False, returnPeriod = False, returnPreventReactivateCheckboxFromBeingRendered = False, returnRequestSource = False, returnRequestSourceCode = False, returnRequestStatus = False, returnRequestStatusCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthID = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSectionLengthSubsetID = False, returnStaffFullNameFML = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentCourseRequestIDAlternateFor = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionTransactionID = False, returnTotalEarnedCreditOverride = False, returnTotalFailedCreditOverride = False, returnTransferCourseName = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditTotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentCourseRequestToReactivateMN/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentCourseRequestToReactivateMN(TempStudentCourseRequestToReactivateMNID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentCourseRequestToReactivateNonState(EntityID = 1, page = 1, pageSize = 100, returnTempStudentCourseRequestToReactivateNonStateID = True, returnAlternateRank = False, returnAuditRecordIsRequestable = False, returnAuditRecordIsSchedulable = False, returnCourseCode = False, returnCourseCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnDateFrom = False, returnDateTo = False, returnDays = False, returnEarlyExitReasonCodeDescription = False, returnEarlyExitReasonID = False, returnEarnedCreditOverride = False, returnEarnedCredits = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnEntityIDRequestedFrom = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLink = False, returnGradeReferenceID = False, returnIsAlternate = False, returnIsTransferCourse = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnNameRequestedByLFM = False, returnPeriod = False, returnPreventReactivateCheckboxFromBeingRendered = False, returnRequestSource = False, returnRequestSourceCode = False, returnRequestStatus = False, returnRequestStatusCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthID = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSectionLengthSubsetID = False, returnStaffFullNameFML = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentCourseRequestIDAlternateFor = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionTransactionID = False, returnTotalEarnedCreditOverride = False, returnTotalFailedCreditOverride = False, returnTransferCourseName = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditTotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentCourseRequestToReactivateNonState/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentCourseRequestToReactivateNonState(TempStudentCourseRequestToReactivateNonStateID, EntityID = 1, returnTempStudentCourseRequestToReactivateNonStateID = True, returnAlternateRank = False, returnAuditRecordIsRequestable = False, returnAuditRecordIsSchedulable = False, returnCourseCode = False, returnCourseCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnDateFrom = False, returnDateTo = False, returnDays = False, returnEarlyExitReasonCodeDescription = False, returnEarlyExitReasonID = False, returnEarnedCreditOverride = False, returnEarnedCredits = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnEntityIDRequestedFrom = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLink = False, returnGradeReferenceID = False, returnIsAlternate = False, returnIsTransferCourse = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnNameRequestedByLFM = False, returnPeriod = False, returnPreventReactivateCheckboxFromBeingRendered = False, returnRequestSource = False, returnRequestSourceCode = False, returnRequestStatus = False, returnRequestStatusCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthID = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSectionLengthSubsetID = False, returnStaffFullNameFML = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentCourseRequestIDAlternateFor = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionTransactionID = False, returnTotalEarnedCreditOverride = False, returnTotalFailedCreditOverride = False, returnTransferCourseName = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditTotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentCourseRequestToReactivateNonState/" + str(TempStudentCourseRequestToReactivateNonStateID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentCourseRequestToReactivateNonState(TempStudentCourseRequestToReactivateNonStateID, EntityID = 1, setAlternateRank = None, setCourseCode = None, setCourseCodeDescription = None, setCourseDescription = None, setCourseEntityOfferedToID = None, setCourseGradeLevelSummary = None, setCourseID = None, setCurrentEnrollment = None, setDateFrom = None, setDateTo = None, setDays = None, setEarlyExitReasonCodeDescription = None, setEarlyExitReasonID = None, setEarnedCreditOverride = None, setEarnedCredits = None, setEndDate = None, setEntityIDCountsAs = None, setEntityIDCourse = None, setEntityIDRequestedFrom = None, setExcludeFromReportCardsAndTranscripts = None, setExcludeFromStudentSectionLink = None, setGradeReferenceID = None, setIsAlternate = None, setIsTransferCourse = None, setMaximumStudentCount = None, setNameIDRequestedBy = None, setNameRequestedByLFM = None, setPeriod = None, setPreventReactivateCheckboxFromBeingRendered = None, setRequestSource = None, setRequestSourceCode = None, setRequestStatus = None, setRequestStatusCode = None, setSchedulingMethod = None, setSchedulingMethodCode = None, setSchoolYearIDCourse = None, setSectionCode = None, setSectionID = None, setSectionLengthID = None, setSectionLengthSubsetCode = None, setSectionLengthSubsetDescription = None, setSectionLengthSubsetID = None, setStaffFullNameFML = None, setStartDate = None, setStudentCourseRequestID = None, setStudentCourseRequestIDAlternateFor = None, setStudentID = None, setStudentSectionID = None, setStudentSectionTransactionID = None, setTotalEarnedCreditOverride = None, setTotalFailedCreditOverride = None, setTransferCourseName = None, setUseEarnedCreditOverride = None, setUseEarnedCreditTotalOverride = None, setRelationships = None, returnTempStudentCourseRequestToReactivateNonStateID = True, returnAlternateRank = False, returnAuditRecordIsRequestable = False, returnAuditRecordIsSchedulable = False, returnCourseCode = False, returnCourseCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnDateFrom = False, returnDateTo = False, returnDays = False, returnEarlyExitReasonCodeDescription = False, returnEarlyExitReasonID = False, returnEarnedCreditOverride = False, returnEarnedCredits = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnEntityIDRequestedFrom = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLink = False, returnGradeReferenceID = False, returnIsAlternate = False, returnIsTransferCourse = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnNameRequestedByLFM = False, returnPeriod = False, returnPreventReactivateCheckboxFromBeingRendered = False, returnRequestSource = False, returnRequestSourceCode = False, returnRequestStatus = False, returnRequestStatusCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthID = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSectionLengthSubsetID = False, returnStaffFullNameFML = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentCourseRequestIDAlternateFor = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionTransactionID = False, returnTotalEarnedCreditOverride = False, returnTotalFailedCreditOverride = False, returnTransferCourseName = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditTotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentCourseRequestToReactivateNonState/" + str(TempStudentCourseRequestToReactivateNonStateID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentCourseRequestToReactivateNonState(EntityID = 1, setAlternateRank = None, setCourseCode = None, setCourseCodeDescription = None, setCourseDescription = None, setCourseEntityOfferedToID = None, setCourseGradeLevelSummary = None, setCourseID = None, setCurrentEnrollment = None, setDateFrom = None, setDateTo = None, setDays = None, setEarlyExitReasonCodeDescription = None, setEarlyExitReasonID = None, setEarnedCreditOverride = None, setEarnedCredits = None, setEndDate = None, setEntityIDCountsAs = None, setEntityIDCourse = None, setEntityIDRequestedFrom = None, setExcludeFromReportCardsAndTranscripts = None, setExcludeFromStudentSectionLink = None, setGradeReferenceID = None, setIsAlternate = None, setIsTransferCourse = None, setMaximumStudentCount = None, setNameIDRequestedBy = None, setNameRequestedByLFM = None, setPeriod = None, setPreventReactivateCheckboxFromBeingRendered = None, setRequestSource = None, setRequestSourceCode = None, setRequestStatus = None, setRequestStatusCode = None, setSchedulingMethod = None, setSchedulingMethodCode = None, setSchoolYearIDCourse = None, setSectionCode = None, setSectionID = None, setSectionLengthID = None, setSectionLengthSubsetCode = None, setSectionLengthSubsetDescription = None, setSectionLengthSubsetID = None, setStaffFullNameFML = None, setStartDate = None, setStudentCourseRequestID = None, setStudentCourseRequestIDAlternateFor = None, setStudentID = None, setStudentSectionID = None, setStudentSectionTransactionID = None, setTotalEarnedCreditOverride = None, setTotalFailedCreditOverride = None, setTransferCourseName = None, setUseEarnedCreditOverride = None, setUseEarnedCreditTotalOverride = None, setRelationships = None, returnTempStudentCourseRequestToReactivateNonStateID = True, returnAlternateRank = False, returnAuditRecordIsRequestable = False, returnAuditRecordIsSchedulable = False, returnCourseCode = False, returnCourseCodeDescription = False, returnCourseDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnCurrentEnrollment = False, returnDateFrom = False, returnDateTo = False, returnDays = False, returnEarlyExitReasonCodeDescription = False, returnEarlyExitReasonID = False, returnEarnedCreditOverride = False, returnEarnedCredits = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnEntityIDRequestedFrom = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLink = False, returnGradeReferenceID = False, returnIsAlternate = False, returnIsTransferCourse = False, returnMaximumStudentCount = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnNameRequestedByLFM = False, returnPeriod = False, returnPreventReactivateCheckboxFromBeingRendered = False, returnRequestSource = False, returnRequestSourceCode = False, returnRequestStatus = False, returnRequestStatusCode = False, returnSchedulingMethod = False, returnSchedulingMethodCode = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthID = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSectionLengthSubsetID = False, returnStaffFullNameFML = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentCourseRequestIDAlternateFor = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionTransactionID = False, returnTotalEarnedCreditOverride = False, returnTotalFailedCreditOverride = False, returnTransferCourseName = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditTotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentCourseRequestToReactivateNonState/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentCourseRequestToReactivateNonState(TempStudentCourseRequestToReactivateNonStateID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentSchedulingCategory(EntityID = 1, page = 1, pageSize = 100, returnTempStudentSchedulingCategoryID = True, returnCreatedTime = False, returnMessage = False, returnModifiedTime = False, returnProposedCategoriesDisplayValue = False, returnProposedTargetCategoryIDsToDeleteCSV = False, returnProposedTargetCategoryIDsToInsertCSV = False, returnSourceCategoriesDisplayValue = False, returnSourceCategoryIDsCSV = False, returnSourceStudentEntityYearID = False, returnStudentNameLFM = False, returnTargetCategoriesDisplayValue = False, returnTargetCategoryIDsCSV = False, returnTargetStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentSchedulingCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentSchedulingCategory(TempStudentSchedulingCategoryID, EntityID = 1, returnTempStudentSchedulingCategoryID = True, returnCreatedTime = False, returnMessage = False, returnModifiedTime = False, returnProposedCategoriesDisplayValue = False, returnProposedTargetCategoryIDsToDeleteCSV = False, returnProposedTargetCategoryIDsToInsertCSV = False, returnSourceCategoriesDisplayValue = False, returnSourceCategoryIDsCSV = False, returnSourceStudentEntityYearID = False, returnStudentNameLFM = False, returnTargetCategoriesDisplayValue = False, returnTargetCategoryIDsCSV = False, returnTargetStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentSchedulingCategory/" + str(TempStudentSchedulingCategoryID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentSchedulingCategory(TempStudentSchedulingCategoryID, EntityID = 1, setMessage = None, setProposedCategoriesDisplayValue = None, setProposedTargetCategoryIDsToDeleteCSV = None, setProposedTargetCategoryIDsToInsertCSV = None, setSourceCategoriesDisplayValue = None, setSourceCategoryIDsCSV = None, setSourceStudentEntityYearID = None, setStudentNameLFM = None, setTargetCategoriesDisplayValue = None, setTargetCategoryIDsCSV = None, setTargetStudentEntityYearID = None, setRelationships = None, returnTempStudentSchedulingCategoryID = True, returnCreatedTime = False, returnMessage = False, returnModifiedTime = False, returnProposedCategoriesDisplayValue = False, returnProposedTargetCategoryIDsToDeleteCSV = False, returnProposedTargetCategoryIDsToInsertCSV = False, returnSourceCategoriesDisplayValue = False, returnSourceCategoryIDsCSV = False, returnSourceStudentEntityYearID = False, returnStudentNameLFM = False, returnTargetCategoriesDisplayValue = False, returnTargetCategoryIDsCSV = False, returnTargetStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentSchedulingCategory/" + str(TempStudentSchedulingCategoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentSchedulingCategory(EntityID = 1, setMessage = None, setProposedCategoriesDisplayValue = None, setProposedTargetCategoryIDsToDeleteCSV = None, setProposedTargetCategoryIDsToInsertCSV = None, setSourceCategoriesDisplayValue = None, setSourceCategoryIDsCSV = None, setSourceStudentEntityYearID = None, setStudentNameLFM = None, setTargetCategoriesDisplayValue = None, setTargetCategoryIDsCSV = None, setTargetStudentEntityYearID = None, setRelationships = None, returnTempStudentSchedulingCategoryID = True, returnCreatedTime = False, returnMessage = False, returnModifiedTime = False, returnProposedCategoriesDisplayValue = False, returnProposedTargetCategoryIDsToDeleteCSV = False, returnProposedTargetCategoryIDsToInsertCSV = False, returnSourceCategoriesDisplayValue = False, returnSourceCategoryIDsCSV = False, returnSourceStudentEntityYearID = False, returnStudentNameLFM = False, returnTargetCategoriesDisplayValue = False, returnTargetCategoryIDsCSV = False, returnTargetStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentSchedulingCategory/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentSchedulingCategory(TempStudentSchedulingCategoryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentSchedulingTeam(EntityID = 1, page = 1, pageSize = 100, returnTempStudentSchedulingTeamID = True, returnCreatedTime = False, returnMessage = False, returnModifiedTime = False, returnSourceSchedulingTeamCode = False, returnSourceSchedulingTeamDescription = False, returnSourceSchedulingTeamID = False, returnSourceSchoolYearDescription = False, returnSourceStudentEntityYearID = False, returnStudentNameLFM = False, returnTargetSchedulingTeamCode = False, returnTargetSchedulingTeamDescription = False, returnTargetSchedulingTeamID = False, returnTargetSchoolYearDescription = False, returnTargetStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentSchedulingTeam/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentSchedulingTeam(TempStudentSchedulingTeamID, EntityID = 1, returnTempStudentSchedulingTeamID = True, returnCreatedTime = False, returnMessage = False, returnModifiedTime = False, returnSourceSchedulingTeamCode = False, returnSourceSchedulingTeamDescription = False, returnSourceSchedulingTeamID = False, returnSourceSchoolYearDescription = False, returnSourceStudentEntityYearID = False, returnStudentNameLFM = False, returnTargetSchedulingTeamCode = False, returnTargetSchedulingTeamDescription = False, returnTargetSchedulingTeamID = False, returnTargetSchoolYearDescription = False, returnTargetStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentSchedulingTeam/" + str(TempStudentSchedulingTeamID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentSchedulingTeam(TempStudentSchedulingTeamID, EntityID = 1, setMessage = None, setSourceSchedulingTeamCode = None, setSourceSchedulingTeamDescription = None, setSourceSchedulingTeamID = None, setSourceSchoolYearDescription = None, setSourceStudentEntityYearID = None, setStudentNameLFM = None, setTargetSchedulingTeamCode = None, setTargetSchedulingTeamDescription = None, setTargetSchedulingTeamID = None, setTargetSchoolYearDescription = None, setTargetStudentEntityYearID = None, setRelationships = None, returnTempStudentSchedulingTeamID = True, returnCreatedTime = False, returnMessage = False, returnModifiedTime = False, returnSourceSchedulingTeamCode = False, returnSourceSchedulingTeamDescription = False, returnSourceSchedulingTeamID = False, returnSourceSchoolYearDescription = False, returnSourceStudentEntityYearID = False, returnStudentNameLFM = False, returnTargetSchedulingTeamCode = False, returnTargetSchedulingTeamDescription = False, returnTargetSchedulingTeamID = False, returnTargetSchoolYearDescription = False, returnTargetStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentSchedulingTeam/" + str(TempStudentSchedulingTeamID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentSchedulingTeam(EntityID = 1, setMessage = None, setSourceSchedulingTeamCode = None, setSourceSchedulingTeamDescription = None, setSourceSchedulingTeamID = None, setSourceSchoolYearDescription = None, setSourceStudentEntityYearID = None, setStudentNameLFM = None, setTargetSchedulingTeamCode = None, setTargetSchedulingTeamDescription = None, setTargetSchedulingTeamID = None, setTargetSchoolYearDescription = None, setTargetStudentEntityYearID = None, setRelationships = None, returnTempStudentSchedulingTeamID = True, returnCreatedTime = False, returnMessage = False, returnModifiedTime = False, returnSourceSchedulingTeamCode = False, returnSourceSchedulingTeamDescription = False, returnSourceSchedulingTeamID = False, returnSourceSchoolYearDescription = False, returnSourceStudentEntityYearID = False, returnStudentNameLFM = False, returnTargetSchedulingTeamCode = False, returnTargetSchedulingTeamDescription = False, returnTargetSchedulingTeamID = False, returnTargetSchoolYearDescription = False, returnTargetStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentSchedulingTeam/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentSchedulingTeam(TempStudentSchedulingTeamID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentSection(EntityID = 1, page = 1, pageSize = 100, returnTempStudentSectionID = True, returnCourseCodeDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnEarlyExitReasonCodeDescription = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNote = False, returnRenderCheckbox = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentGenderCode = False, returnStudentGradeLevelCode = False, returnStudentGradYear = False, returnStudentID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionID = False, returnStudentSectionTransactionIDToUpdate = False, returnTempStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentSection(TempStudentSectionID, EntityID = 1, returnTempStudentSectionID = True, returnCourseCodeDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnEarlyExitReasonCodeDescription = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNote = False, returnRenderCheckbox = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentGenderCode = False, returnStudentGradeLevelCode = False, returnStudentGradYear = False, returnStudentID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionID = False, returnStudentSectionTransactionIDToUpdate = False, returnTempStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentSection/" + str(TempStudentSectionID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentSection(TempStudentSectionID, EntityID = 1, setCourseCodeDescription = None, setCourseEntityOfferedToID = None, setCourseGradeLevelSummary = None, setCourseID = None, setEarlyExitReasonCodeDescription = None, setEndDate = None, setEntityIDCountsAs = None, setEntityIDCourse = None, setGradeReferenceID = None, setNote = None, setRenderCheckbox = None, setSchoolYearIDCourse = None, setSectionCode = None, setSectionID = None, setStartDate = None, setStudentCourseRequestID = None, setStudentGenderCode = None, setStudentGradeLevelCode = None, setStudentGradYear = None, setStudentID = None, setStudentNameLFM = None, setStudentNumber = None, setStudentSectionID = None, setStudentSectionTransactionIDToUpdate = None, setTempStudentID = None, setWorkflowAction = None, setWorkflowActionCode = None, setRelationships = None, returnTempStudentSectionID = True, returnCourseCodeDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnEarlyExitReasonCodeDescription = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNote = False, returnRenderCheckbox = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentGenderCode = False, returnStudentGradeLevelCode = False, returnStudentGradYear = False, returnStudentID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionID = False, returnStudentSectionTransactionIDToUpdate = False, returnTempStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentSection/" + str(TempStudentSectionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentSection(EntityID = 1, setCourseCodeDescription = None, setCourseEntityOfferedToID = None, setCourseGradeLevelSummary = None, setCourseID = None, setEarlyExitReasonCodeDescription = None, setEndDate = None, setEntityIDCountsAs = None, setEntityIDCourse = None, setGradeReferenceID = None, setNote = None, setRenderCheckbox = None, setSchoolYearIDCourse = None, setSectionCode = None, setSectionID = None, setStartDate = None, setStudentCourseRequestID = None, setStudentGenderCode = None, setStudentGradeLevelCode = None, setStudentGradYear = None, setStudentID = None, setStudentNameLFM = None, setStudentNumber = None, setStudentSectionID = None, setStudentSectionTransactionIDToUpdate = None, setTempStudentID = None, setWorkflowAction = None, setWorkflowActionCode = None, setRelationships = None, returnTempStudentSectionID = True, returnCourseCodeDescription = False, returnCourseEntityOfferedToID = False, returnCourseGradeLevelSummary = False, returnCourseID = False, returnCreatedTime = False, returnEarlyExitReasonCodeDescription = False, returnEndDate = False, returnEntityIDCountsAs = False, returnEntityIDCourse = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNote = False, returnRenderCheckbox = False, returnSchoolYearIDCourse = False, returnSectionCode = False, returnSectionID = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentGenderCode = False, returnStudentGradeLevelCode = False, returnStudentGradYear = False, returnStudentID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionID = False, returnStudentSectionTransactionIDToUpdate = False, returnTempStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentSection/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentSection(TempStudentSectionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentSectionTransaction(EntityID = 1, page = 1, pageSize = 100, returnTempStudentSectionTransactionID = True, returnCreatedTime = False, returnEarlyExitReasonID = False, returnEndDate = False, returnEntityIDCountsAs = False, returnHideNewStudentButton = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentSectionTransactionID = False, returnTempStudentCourseRequestID = False, returnTempStudentCourseRequestToReactivateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentSectionTransaction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentSectionTransaction(TempStudentSectionTransactionID, EntityID = 1, returnTempStudentSectionTransactionID = True, returnCreatedTime = False, returnEarlyExitReasonID = False, returnEndDate = False, returnEntityIDCountsAs = False, returnHideNewStudentButton = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentSectionTransactionID = False, returnTempStudentCourseRequestID = False, returnTempStudentCourseRequestToReactivateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentSectionTransaction/" + str(TempStudentSectionTransactionID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentSectionTransaction(TempStudentSectionTransactionID, EntityID = 1, setEarlyExitReasonID = None, setEndDate = None, setEntityIDCountsAs = None, setHideNewStudentButton = None, setNameIDRequestedBy = None, setSectionLengthSubsetID = None, setStartDate = None, setStudentCourseRequestID = None, setStudentSectionTransactionID = None, setTempStudentCourseRequestID = None, setTempStudentCourseRequestToReactivateID = None, setRelationships = None, returnTempStudentSectionTransactionID = True, returnCreatedTime = False, returnEarlyExitReasonID = False, returnEndDate = False, returnEntityIDCountsAs = False, returnHideNewStudentButton = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentSectionTransactionID = False, returnTempStudentCourseRequestID = False, returnTempStudentCourseRequestToReactivateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentSectionTransaction/" + str(TempStudentSectionTransactionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentSectionTransaction(EntityID = 1, setEarlyExitReasonID = None, setEndDate = None, setEntityIDCountsAs = None, setHideNewStudentButton = None, setNameIDRequestedBy = None, setSectionLengthSubsetID = None, setStartDate = None, setStudentCourseRequestID = None, setStudentSectionTransactionID = None, setTempStudentCourseRequestID = None, setTempStudentCourseRequestToReactivateID = None, setRelationships = None, returnTempStudentSectionTransactionID = True, returnCreatedTime = False, returnEarlyExitReasonID = False, returnEndDate = False, returnEntityIDCountsAs = False, returnHideNewStudentButton = False, returnModifiedTime = False, returnNameIDRequestedBy = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnStudentCourseRequestID = False, returnStudentSectionTransactionID = False, returnTempStudentCourseRequestID = False, returnTempStudentCourseRequestToReactivateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempStudentSectionTransaction/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentSectionTransaction(TempStudentSectionTransactionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempSubstituteAssignment(EntityID = 1, page = 1, pageSize = 100, returnTempSubstituteAssignmentID = True, returnConflicts = False, returnCourseCodeSectionCode = False, returnCreatedTime = False, returnDate = False, returnDisplayPeriodID = False, returnDisplayPeriodSortNumber = False, returnEntityID = False, returnHasAttendanceAccess = False, returnHasConflicts = False, returnHasGradebookAccess = False, returnIsLongTermSubstitute = False, returnMeetID = False, returnModifiedTime = False, returnPeriod = False, returnSchoolYearID = False, returnSectionAlreadyCovered = False, returnSectionID = False, returnSourceStaffID = False, returnStaffMeetID = False, returnStaffName = False, returnSubstituteStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSubstituteAssignment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempSubstituteAssignment(TempSubstituteAssignmentID, EntityID = 1, returnTempSubstituteAssignmentID = True, returnConflicts = False, returnCourseCodeSectionCode = False, returnCreatedTime = False, returnDate = False, returnDisplayPeriodID = False, returnDisplayPeriodSortNumber = False, returnEntityID = False, returnHasAttendanceAccess = False, returnHasConflicts = False, returnHasGradebookAccess = False, returnIsLongTermSubstitute = False, returnMeetID = False, returnModifiedTime = False, returnPeriod = False, returnSchoolYearID = False, returnSectionAlreadyCovered = False, returnSectionID = False, returnSourceStaffID = False, returnStaffMeetID = False, returnStaffName = False, returnSubstituteStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSubstituteAssignment/" + str(TempSubstituteAssignmentID), verb = "get", return_params_list = return_params_list)

def modifyTempSubstituteAssignment(TempSubstituteAssignmentID, EntityID = 1, setConflicts = None, setCourseCodeSectionCode = None, setDate = None, setDisplayPeriodID = None, setDisplayPeriodSortNumber = None, setEntityID = None, setHasAttendanceAccess = None, setHasGradebookAccess = None, setIsLongTermSubstitute = None, setMeetID = None, setPeriod = None, setSchoolYearID = None, setSectionAlreadyCovered = None, setSectionID = None, setSourceStaffID = None, setStaffMeetID = None, setStaffName = None, setSubstituteStaffID = None, setRelationships = None, returnTempSubstituteAssignmentID = True, returnConflicts = False, returnCourseCodeSectionCode = False, returnCreatedTime = False, returnDate = False, returnDisplayPeriodID = False, returnDisplayPeriodSortNumber = False, returnEntityID = False, returnHasAttendanceAccess = False, returnHasConflicts = False, returnHasGradebookAccess = False, returnIsLongTermSubstitute = False, returnMeetID = False, returnModifiedTime = False, returnPeriod = False, returnSchoolYearID = False, returnSectionAlreadyCovered = False, returnSectionID = False, returnSourceStaffID = False, returnStaffMeetID = False, returnStaffName = False, returnSubstituteStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSubstituteAssignment/" + str(TempSubstituteAssignmentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempSubstituteAssignment(EntityID = 1, setConflicts = None, setCourseCodeSectionCode = None, setDate = None, setDisplayPeriodID = None, setDisplayPeriodSortNumber = None, setEntityID = None, setHasAttendanceAccess = None, setHasGradebookAccess = None, setIsLongTermSubstitute = None, setMeetID = None, setPeriod = None, setSchoolYearID = None, setSectionAlreadyCovered = None, setSectionID = None, setSourceStaffID = None, setStaffMeetID = None, setStaffName = None, setSubstituteStaffID = None, setRelationships = None, returnTempSubstituteAssignmentID = True, returnConflicts = False, returnCourseCodeSectionCode = False, returnCreatedTime = False, returnDate = False, returnDisplayPeriodID = False, returnDisplayPeriodSortNumber = False, returnEntityID = False, returnHasAttendanceAccess = False, returnHasConflicts = False, returnHasGradebookAccess = False, returnIsLongTermSubstitute = False, returnMeetID = False, returnModifiedTime = False, returnPeriod = False, returnSchoolYearID = False, returnSectionAlreadyCovered = False, returnSectionID = False, returnSourceStaffID = False, returnStaffMeetID = False, returnStaffName = False, returnSubstituteStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Scheduling/TempSubstituteAssignment/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempSubstituteAssignment(TempSubstituteAssignmentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")