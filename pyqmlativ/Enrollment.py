# This module contains Enrollment functions.

from .Utilities import make_request

import pandas as pd

def getEveryAwardsListMA(EntityID = 1, page = 1, pageSize = 100, returnAwardsListMAID = True, returnAwardID = False, returnCreatedTime = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AwardsListMA/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAwardsListMA(AwardsListMAID, EntityID = 1, returnreturnAwardsListMAID = False, returnreturnAwardID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnStudentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AwardsListMA/" + str(AwardsListMAID), verb = "get", params_list = params_list)

	return(response)

def deleteAwardsListMA(AwardsListMAID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AwardsListMA/" + str(AwardsListMAID), verb = "delete")

	return(response)

def getEveryAwardsMA(EntityID = 1, page = 1, pageSize = 100, returnAwardsMAID = True, returnAward = False, returnCode = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AwardsMA/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAwardsMA(AwardsMAID, EntityID = 1, returnreturnAwardsMAID = False, returnreturnAward = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AwardsMA/" + str(AwardsMAID), verb = "get", params_list = params_list)

	return(response)

def deleteAwardsMA(AwardsMAID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AwardsMA/" + str(AwardsMAID), verb = "delete")

	return(response)

def getEveryConfigDistrict(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictID = True, returnAllowDualEnrollment = False, returnCreatedTime = False, returnDistrictID = False, returnEntryDaysBeforeCalendarStart = False, returnModifiedTime = False, returnNumberDaysBackdateEntry = False, returnNumberDaysBackdateWithdrawal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDaysAfterCalendarEnd = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigDistrict(ConfigDistrictID, EntityID = 1, returnreturnConfigDistrictID = False, returnreturnAllowDualEnrollment = False, returnreturnCreatedTime = False, returnreturnDistrictID = False, returnreturnEntryDaysBeforeCalendarStart = False, returnreturnModifiedTime = False, returnreturnNumberDaysBackdateEntry = False, returnreturnNumberDaysBackdateWithdrawal = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWithdrawalDaysAfterCalendarEnd = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrict/" + str(ConfigDistrictID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigDistrict(ConfigDistrictID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrict/" + str(ConfigDistrictID), verb = "delete")

	return(response)

def getEveryConfigDistrictYear(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictYearID = True, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnEnableNoShow = False, returnEnrolledDifferentEntityNoShowActionType = False, returnEnrolledDifferentEntityNoShowActionTypeCode = False, returnEnrolledDifferentEntityNoShowEntryDate = False, returnEnrolledDifferentEntityNoShowWithdrawalDate = False, returnModifiedTime = False, returnNoDistrictEnrollmentNoShowActionType = False, returnNoDistrictEnrollmentNoShowActionTypeCode = False, returnNoDistrictEnrollmentNoShowEntryDate = False, returnNoDistrictEnrollmentNoShowWithdrawalDate = False, returnPreviouslyEnrolledSameEntityNoShowActionType = False, returnPreviouslyEnrolledSameEntityNoShowActionTypeCode = False, returnPreviouslyEnrolledSameEntityNoShowEntryDate = False, returnPreviouslyEnrolledSameEntityNoShowWithdrawalDate = False, returnPriorNoShowRecord = False, returnPriorNoShowRecordCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, returnreturnConfigDistrictYearID = False, returnreturnConfigDistrictYearIDClonedFrom = False, returnreturnCreatedTime = False, returnreturnDistrictID = False, returnreturnEnableNoShow = False, returnreturnEnrolledDifferentEntityNoShowActionType = False, returnreturnEnrolledDifferentEntityNoShowActionTypeCode = False, returnreturnEnrolledDifferentEntityNoShowEntryDate = False, returnreturnEnrolledDifferentEntityNoShowWithdrawalDate = False, returnreturnModifiedTime = False, returnreturnNoDistrictEnrollmentNoShowActionType = False, returnreturnNoDistrictEnrollmentNoShowActionTypeCode = False, returnreturnNoDistrictEnrollmentNoShowEntryDate = False, returnreturnNoDistrictEnrollmentNoShowWithdrawalDate = False, returnreturnPreviouslyEnrolledSameEntityNoShowActionType = False, returnreturnPreviouslyEnrolledSameEntityNoShowActionTypeCode = False, returnreturnPreviouslyEnrolledSameEntityNoShowEntryDate = False, returnreturnPreviouslyEnrolledSameEntityNoShowWithdrawalDate = False, returnreturnPriorNoShowRecord = False, returnreturnPriorNoShowRecordCode = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigDistrictYear(ConfigDistrictYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "delete")

	return(response)

def getEveryConfigDistrictYearWithdrawalCode(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictYearWithdrawalCodeID = True, returnConfigDistrictYearID = False, returnConfigDistrictYearWithdrawalCodeIDClonedFrom = False, returnCreatedTime = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYearWithdrawalCode/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigDistrictYearWithdrawalCode(ConfigDistrictYearWithdrawalCodeID, EntityID = 1, returnreturnConfigDistrictYearWithdrawalCodeID = False, returnreturnConfigDistrictYearID = False, returnreturnConfigDistrictYearWithdrawalCodeIDClonedFrom = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnType = False, returnreturnTypeCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWithdrawalCodeID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYearWithdrawalCode/" + str(ConfigDistrictYearWithdrawalCodeID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigDistrictYearWithdrawalCode(ConfigDistrictYearWithdrawalCodeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYearWithdrawalCode/" + str(ConfigDistrictYearWithdrawalCodeID), verb = "delete")

	return(response)

def getEveryEntitySchool(EntityID = 1, page = 1, pageSize = 100, returnEntitySchoolID = True, returnCreatedTime = False, returnEntityID = False, returnEntitySchoolIDClonedFrom = False, returnEntitySchoolIDClonedTo = False, returnIsDefaultEntityForSchool = False, returnIsDefaultSchoolForEntity = False, returnIsOnlySchoolInEntity = False, returnModifiedTime = False, returnSchoolID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchool/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEntitySchool(EntitySchoolID, EntityID = 1, returnreturnEntitySchoolID = False, returnreturnCreatedTime = False, returnreturnEntityID = False, returnreturnEntitySchoolIDClonedFrom = False, returnreturnEntitySchoolIDClonedTo = False, returnreturnIsDefaultEntityForSchool = False, returnreturnIsDefaultSchoolForEntity = False, returnreturnIsOnlySchoolInEntity = False, returnreturnModifiedTime = False, returnreturnSchoolID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchool/" + str(EntitySchoolID), verb = "get", params_list = params_list)

	return(response)

def deleteEntitySchool(EntitySchoolID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchool/" + str(EntitySchoolID), verb = "delete")

	return(response)

def getEveryEntitySchoolBuilding(EntityID = 1, page = 1, pageSize = 100, returnEntitySchoolBuildingID = True, returnBuildingID = False, returnCreatedTime = False, returnEntitySchoolBuildingIDClonedFrom = False, returnEntitySchoolID = False, returnIsPrimary = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchoolBuilding/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEntitySchoolBuilding(EntitySchoolBuildingID, EntityID = 1, returnreturnEntitySchoolBuildingID = False, returnreturnBuildingID = False, returnreturnCreatedTime = False, returnreturnEntitySchoolBuildingIDClonedFrom = False, returnreturnEntitySchoolID = False, returnreturnIsPrimary = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchoolBuilding/" + str(EntitySchoolBuildingID), verb = "get", params_list = params_list)

	return(response)

def deleteEntitySchoolBuilding(EntitySchoolBuildingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchoolBuilding/" + str(EntitySchoolBuildingID), verb = "delete")

	return(response)

def getEveryEntryCode(EntityID = 1, page = 1, pageSize = 100, returnEntryCodeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEntryCodeIDClonedFrom = False, returnIsCrossEntityCourseEnrollment = False, returnModifiedTime = False, returnSchoolYearID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryCode/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEntryCode(EntryCodeID, EntityID = 1, returnreturnEntryCodeID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnEntryCodeIDClonedFrom = False, returnreturnIsCrossEntityCourseEnrollment = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnType = False, returnreturnTypeCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryCode/" + str(EntryCodeID), verb = "get", params_list = params_list)

	return(response)

def deleteEntryCode(EntryCodeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryCode/" + str(EntryCodeID), verb = "delete")

	return(response)

def getEveryEntryWithdrawal(EntityID = 1, page = 1, pageSize = 100, returnEntryWithdrawalID = True, returnAttendanceDays = False, returnCalendarID = False, returnCreatedTime = False, returnEndDate = False, returnEnrolledAtLeastOneDay = False, returnEntityID = False, returnEntryCodeID = False, returnEntryComment = False, returnEntryWithdrawalIDStatusChangePrevious = False, returnEntryWithdrawalMNID = False, returnGradeReferenceID = False, returnHasMessageCenterAllowedWithdrawalCodeOverride = False, returnIsCombinedEnrollmentFullTime = False, returnIsCrossEntityCourseEnrollment = False, returnIsCurrentOrFutureEnrollment = False, returnIsDefaultEntity = False, returnIsHistoricalEnrollment = False, returnIsIndependentStudy = False, returnIsNoShow = False, returnIsPostSecondaryOption = False, returnIsPSEOConcurrentEnrollment = False, returnIsStartDateOnOrAfterFirstDayOfSchool = False, returnMembershipDays = False, returnModifiedTime = False, returnPercentEnrolled = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnPSEOHours = False, returnRenderDeleteOption = False, returnRenderNoShowOption = False, returnRenderPrintWithdrawalFormOption = False, returnRenderUndoStatusChangeOption = False, returnRenderWithdrawalAndStatusChangeOptions = False, returnSchoolID = False, returnSchoolYearID = False, returnSpecialEdServiceHours = False, returnStartDate = False, returnStateAidCategoryCodeMNID = False, returnStateDistrictMNID = False, returnStateLastAttendanceLocationCodeMNID = False, returnStatusChangeEntry = False, returnStatusChangeWithdrawal = False, returnStudentID = False, returnStudentTypeID = False, returnTotalMembershipDays = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnWithdrawalComment = False, returnWithdrawalDate = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryWithdrawal/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEntryWithdrawal(EntryWithdrawalID, EntityID = 1, returnreturnEntryWithdrawalID = False, returnreturnAttendanceDays = False, returnreturnCalendarID = False, returnreturnCreatedTime = False, returnreturnEndDate = False, returnreturnEnrolledAtLeastOneDay = False, returnreturnEntityID = False, returnreturnEntryCodeID = False, returnreturnEntryComment = False, returnreturnEntryWithdrawalIDStatusChangePrevious = False, returnreturnEntryWithdrawalMNID = False, returnreturnGradeReferenceID = False, returnreturnHasMessageCenterAllowedWithdrawalCodeOverride = False, returnreturnIsCombinedEnrollmentFullTime = False, returnreturnIsCrossEntityCourseEnrollment = False, returnreturnIsCurrentOrFutureEnrollment = False, returnreturnIsDefaultEntity = False, returnreturnIsHistoricalEnrollment = False, returnreturnIsIndependentStudy = False, returnreturnIsNoShow = False, returnreturnIsPostSecondaryOption = False, returnreturnIsPSEOConcurrentEnrollment = False, returnreturnIsStartDateOnOrAfterFirstDayOfSchool = False, returnreturnMembershipDays = False, returnreturnModifiedTime = False, returnreturnPercentEnrolled = False, returnreturnPromotionStatus = False, returnreturnPromotionStatusCode = False, returnreturnPSEOHours = False, returnreturnRenderDeleteOption = False, returnreturnRenderNoShowOption = False, returnreturnRenderPrintWithdrawalFormOption = False, returnreturnRenderUndoStatusChangeOption = False, returnreturnRenderWithdrawalAndStatusChangeOptions = False, returnreturnSchoolID = False, returnreturnSchoolYearID = False, returnreturnSpecialEdServiceHours = False, returnreturnStartDate = False, returnreturnStateAidCategoryCodeMNID = False, returnreturnStateDistrictMNID = False, returnreturnStateLastAttendanceLocationCodeMNID = False, returnreturnStatusChangeEntry = False, returnreturnStatusChangeWithdrawal = False, returnreturnStudentID = False, returnreturnStudentTypeID = False, returnreturnTotalMembershipDays = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWithdrawalCodeID = False, returnreturnWithdrawalComment = False, returnreturnWithdrawalDate = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryWithdrawal/" + str(EntryWithdrawalID), verb = "get", params_list = params_list)

	return(response)

def deleteEntryWithdrawal(EntryWithdrawalID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryWithdrawal/" + str(EntryWithdrawalID), verb = "delete")

	return(response)

def getEveryGradeLevel(EntityID = 1, page = 1, pageSize = 100, returnGradeLevelID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnFederalGradeLevel = False, returnFederalGradeLevelCode = False, returnModifiedTime = False, returnNumericValue = False, returnStateGradeLevel = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeLevel/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeLevel(GradeLevelID, EntityID = 1, returnreturnGradeLevelID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnFederalGradeLevel = False, returnreturnFederalGradeLevelCode = False, returnreturnModifiedTime = False, returnreturnNumericValue = False, returnreturnStateGradeLevel = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeLevel/" + str(GradeLevelID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeLevel(GradeLevelID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeLevel/" + str(GradeLevelID), verb = "delete")

	return(response)

def getEveryGradeReference(EntityID = 1, page = 1, pageSize = 100, returnGradeReferenceID = True, returnCreatedTime = False, returnDistrictGroupKey = False, returnGradeLevelID = False, returnGradeReferenceIDClonedFrom = False, returnGradeReferenceIDClonedTo = False, returnGradeReferenceMNID = False, returnGradYear = False, returnMinutesPresentFullDay = False, returnMinutesPresentHalfDay = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateGradeLevel = False, returnStateSTARGradeLevelMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeReference/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReference(GradeReferenceID, EntityID = 1, returnreturnGradeReferenceID = False, returnreturnCreatedTime = False, returnreturnDistrictGroupKey = False, returnreturnGradeLevelID = False, returnreturnGradeReferenceIDClonedFrom = False, returnreturnGradeReferenceIDClonedTo = False, returnreturnGradeReferenceMNID = False, returnreturnGradYear = False, returnreturnMinutesPresentFullDay = False, returnreturnMinutesPresentHalfDay = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnStateGradeLevel = False, returnreturnStateSTARGradeLevelMNID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeReference/" + str(GradeReferenceID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReference(GradeReferenceID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeReference/" + str(GradeReferenceID), verb = "delete")

	return(response)

def getEveryHomeroom(EntityID = 1, page = 1, pageSize = 100, returnHomeroomID = True, returnCode = False, returnCreatedTime = False, returnEntityID = False, returnHomeroomDetails = False, returnHomeroomIDClonedFrom = False, returnHomeroomIDClonedTo = False, returnModifiedTime = False, returnRoomID = False, returnSchoolYearID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Homeroom/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHomeroom(HomeroomID, EntityID = 1, returnreturnHomeroomID = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnEntityID = False, returnreturnHomeroomDetails = False, returnreturnHomeroomIDClonedFrom = False, returnreturnHomeroomIDClonedTo = False, returnreturnModifiedTime = False, returnreturnRoomID = False, returnreturnSchoolYearID = False, returnreturnStaffID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Homeroom/" + str(HomeroomID), verb = "get", params_list = params_list)

	return(response)

def deleteHomeroom(HomeroomID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Homeroom/" + str(HomeroomID), verb = "delete")

	return(response)

def getEveryPaymentPlanMA(EntityID = 1, page = 1, pageSize = 100, returnPaymentPlanMAID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PaymentPlanMA/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getPaymentPlanMA(PaymentPlanMAID, EntityID = 1, returnreturnPaymentPlanMAID = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PaymentPlanMA/" + str(PaymentPlanMAID), verb = "get", params_list = params_list)

	return(response)

def deletePaymentPlanMA(PaymentPlanMAID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PaymentPlanMA/" + str(PaymentPlanMAID), verb = "delete")

	return(response)

def getEveryPermit(EntityID = 1, page = 1, pageSize = 100, returnPermitID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEndDate = False, returnModifiedTime = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Permit/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getPermit(PermitID, EntityID = 1, returnreturnPermitID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnEndDate = False, returnreturnModifiedTime = False, returnreturnStartDate = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Permit/" + str(PermitID), verb = "get", params_list = params_list)

	return(response)

def deletePermit(PermitID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Permit/" + str(PermitID), verb = "delete")

	return(response)

def getEverySchool(EntityID = 1, page = 1, pageSize = 100, returnSchoolID = True, returnAllowsSchoolDevices = False, returnAllowsStudentDevices = False, returnBuildingID = False, returnCampusAccountabilityRatingID = False, returnCEEBCode = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnDaysInRegularSchoolYear = False, returnDaysPriorForAlgebraICounts = False, returnDistrictID = False, returnEdFiSchoolCategoryID = False, returnEdFiSchoolID = False, returnEducationalProgramHoursPerWeek = False, returnExcludeFromCRDC = False, returnFaxNumber = False, returnFaxNumberIsInternational = False, returnFederalAlternativeSchoolDetailID = False, returnFederalJusticeFacilityTypeID = False, returnFederalNCESSchoolID = False, returnFormattedFaxNumber = False, returnFormattedPhoneNumber = False, returnGradeLevelIDHigh = False, returnGradeLevelIDLow = False, returnHasAlcoholDrugEducation = False, returnHasAntiBullying = False, returnHasAntiViolence = False, returnHasAPCourses = False, returnHasAPSelfSelection = False, returnHasCorporalPunishment = False, returnHasCreditRecovery = False, returnHasCrisisPlan = False, returnHasDualEnrollment = False, returnHasFiberOptic = False, returnHasGifted = False, returnHasHomicideOccurred = False, returnHasIBDiplomaProgramme = False, returnHasPreschoolNonIDEAAge3 = False, returnHasPreschoolNonIDEAAge4 = False, returnHasPreschoolNonIDEAAge5 = False, returnHasSafetyPlan = False, returnHasShootingOccurred = False, returnHasSingleSexAthletics = False, returnHasSingleSexClasses = False, returnHasUngraded = False, returnHasUngradedMainlyElementary = False, returnHasUngradedMainlyHighSchool = False, returnHasUngradedMainlyMiddleSchool = False, returnHasWiFi = False, returnHasZeroTolerance = False, returnIsALCSchool = False, returnIsAlternative = False, returnIsCEP = False, returnIsCharter = False, returnIsCRDCCollectedForSchoolYear = False, returnIsEntireSchoolMagnet = False, returnIsMagnet = False, returnIsNonLEA = False, returnIsSpecialEducation = False, returnIsTitleIII = False, returnModifiedTime = False, returnName = False, returnNameIDSafetySpecialist = False, returnNumberWiFiDevices = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnSchoolIDClonedFrom = False, returnSchoolIDClonedTo = False, returnSchoolMNID = False, returnSchoolNumber = False, returnSchoolYearID = False, returnStaffIDPrincipal = False, returnStateKindergartenScheduleIndicatorCodeMNID = False, returnStateSchoolMNID = False, returnStateTitleISchoolIndicatorCodeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/School/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getSchool(SchoolID, EntityID = 1, returnreturnSchoolID = False, returnreturnAllowsSchoolDevices = False, returnreturnAllowsStudentDevices = False, returnreturnBuildingID = False, returnreturnCampusAccountabilityRatingID = False, returnreturnCEEBCode = False, returnreturnCode = False, returnreturnCodeName = False, returnreturnCreatedTime = False, returnreturnDaysInRegularSchoolYear = False, returnreturnDaysPriorForAlgebraICounts = False, returnreturnDistrictID = False, returnreturnEdFiSchoolCategoryID = False, returnreturnEdFiSchoolID = False, returnreturnEducationalProgramHoursPerWeek = False, returnreturnExcludeFromCRDC = False, returnreturnFaxNumber = False, returnreturnFaxNumberIsInternational = False, returnreturnFederalAlternativeSchoolDetailID = False, returnreturnFederalJusticeFacilityTypeID = False, returnreturnFederalNCESSchoolID = False, returnreturnFormattedFaxNumber = False, returnreturnFormattedPhoneNumber = False, returnreturnGradeLevelIDHigh = False, returnreturnGradeLevelIDLow = False, returnreturnHasAlcoholDrugEducation = False, returnreturnHasAntiBullying = False, returnreturnHasAntiViolence = False, returnreturnHasAPCourses = False, returnreturnHasAPSelfSelection = False, returnreturnHasCorporalPunishment = False, returnreturnHasCreditRecovery = False, returnreturnHasCrisisPlan = False, returnreturnHasDualEnrollment = False, returnreturnHasFiberOptic = False, returnreturnHasGifted = False, returnreturnHasHomicideOccurred = False, returnreturnHasIBDiplomaProgramme = False, returnreturnHasPreschoolNonIDEAAge3 = False, returnreturnHasPreschoolNonIDEAAge4 = False, returnreturnHasPreschoolNonIDEAAge5 = False, returnreturnHasSafetyPlan = False, returnreturnHasShootingOccurred = False, returnreturnHasSingleSexAthletics = False, returnreturnHasSingleSexClasses = False, returnreturnHasUngraded = False, returnreturnHasUngradedMainlyElementary = False, returnreturnHasUngradedMainlyHighSchool = False, returnreturnHasUngradedMainlyMiddleSchool = False, returnreturnHasWiFi = False, returnreturnHasZeroTolerance = False, returnreturnIsALCSchool = False, returnreturnIsAlternative = False, returnreturnIsCEP = False, returnreturnIsCharter = False, returnreturnIsCRDCCollectedForSchoolYear = False, returnreturnIsEntireSchoolMagnet = False, returnreturnIsMagnet = False, returnreturnIsNonLEA = False, returnreturnIsSpecialEducation = False, returnreturnIsTitleIII = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnNameIDSafetySpecialist = False, returnreturnNumberWiFiDevices = False, returnreturnPhoneNumber = False, returnreturnPhoneNumberIsInternational = False, returnreturnSchoolIDClonedFrom = False, returnreturnSchoolIDClonedTo = False, returnreturnSchoolMNID = False, returnreturnSchoolNumber = False, returnreturnSchoolYearID = False, returnreturnStaffIDPrincipal = False, returnreturnStateKindergartenScheduleIndicatorCodeMNID = False, returnreturnStateSchoolMNID = False, returnreturnStateTitleISchoolIndicatorCodeMNID = False, returnreturnType = False, returnreturnTypeCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/School/" + str(SchoolID), verb = "get", params_list = params_list)

	return(response)

def deleteSchool(SchoolID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/School/" + str(SchoolID), verb = "delete")

	return(response)

def getEveryStudentAccountsMA(EntityID = 1, page = 1, pageSize = 100, returnStudentAccountsMAID = True, returnCreatedTime = False, returnFinancialAid = False, returniPadLease = False, returnModifiedTime = False, returnPaymentPlanMAID = False, returnPlaceofWorship = False, returnReligionID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentAccountsMA/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentAccountsMA(StudentAccountsMAID, EntityID = 1, returnreturnStudentAccountsMAID = False, returnreturnCreatedTime = False, returnreturnFinancialAid = False, returnreturniPadLease = False, returnreturnModifiedTime = False, returnreturnPaymentPlanMAID = False, returnreturnPlaceofWorship = False, returnreturnReligionID = False, returnreturnStudentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentAccountsMA/" + str(StudentAccountsMAID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentAccountsMA(StudentAccountsMAID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentAccountsMA/" + str(StudentAccountsMAID), verb = "delete")

	return(response)

def getEveryStudentEntityYear(EntityID = 1, page = 1, pageSize = 100, returnStudentEntityYearID = True, returnChromebookDocumentsReturned = False, returnCreatedTime = False, returnDaysAbsentYTD = False, returnDaysEnrolledYTD = False, returnDaysExcusedYTD = False, returnDaysOtherYTD = False, returnDaysUnexcusedYTD = False, returnEntityID = False, returnEntryWithdrawalIDLatest = False, returnExcludeFromHonorRoll = False, returnExcludeFromRank = False, returnExistsConflictedStudentCourseRequests = False, returnExistsUnscheduleableStudentSections = False, returnFeeAmountDue = False, returnFeeChargeAmount = False, returnFeePaidAmount = False, returnFeePaidAndWaivedAmount = False, returnFeeUnappliedAmount = False, returnFeeWaivedAmount = False, returnFirstName = False, returnFlaggedMissingAssignmentsCount = False, returnGrade = False, returnHandbookSigned = False, returnHasActiveCareerPlanDeclarationTimePeriod = False, returnHasActiveEndorsementDeclarationTimePeriod = False, returnHasConflictedStudentCourseRequest = False, returnHasFlaggedMissingAssignments = False, returnHasMissingAssignments = False, returnHasNoAttendanceToday = False, returnHasOpenDisplayPeriodsInRegularSchoolDay = False, returnHasOverscheduledPeriod = False, returnHasValidStudentPlan = False, returnHomeroomCodeFollettDestiny = False, returnHomeroomID = False, returnHomeroomPeriodFollettDestiny = False, returnHomeroomStaffNameFollettDestiny = False, returnIncludeAsProspectiveRank = False, returnIsActive = False, returnIsCrossEntityCourseEnrollment = False, returnIsDefaultEntity = False, returnIsTransportationRequested = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNumberOfStudentCourseRequests = False, returnNumberOfStudentSections = False, returnOptOutOfMedia = False, returnSchedulingCategories = False, returnSchedulingTeamID = False, returnSchoolYearID = False, returnSectionLengthAbsent = False, returnSectionLengthEnrolled = False, returnSemester2Absent = False, returnSemester2Enrolled = False, returnSignedAcceptableUsePolicy = False, returnStaffIDAdvisor = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnTardyCountYTD = False, returnTardyKioskTotals = False, returnTotalEarnedCreditsPossibleAnticipatedNonTransferStudentSectionsNonAlternateRequestCredits = False, returnTotalMissedAssignmentCount = False, returnUILFeeReceived = False, returnUnscheduleableStudentSectionCount = False, returnUnscheduledStudentCourseRequestCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDate = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentEntityYear(StudentEntityYearID, EntityID = 1, returnreturnStudentEntityYearID = False, returnreturnChromebookDocumentsReturned = False, returnreturnCreatedTime = False, returnreturnDaysAbsentYTD = False, returnreturnDaysEnrolledYTD = False, returnreturnDaysExcusedYTD = False, returnreturnDaysOtherYTD = False, returnreturnDaysUnexcusedYTD = False, returnreturnEntityID = False, returnreturnEntryWithdrawalIDLatest = False, returnreturnExcludeFromHonorRoll = False, returnreturnExcludeFromRank = False, returnreturnExistsConflictedStudentCourseRequests = False, returnreturnExistsUnscheduleableStudentSections = False, returnreturnFeeAmountDue = False, returnreturnFeeChargeAmount = False, returnreturnFeePaidAmount = False, returnreturnFeePaidAndWaivedAmount = False, returnreturnFeeUnappliedAmount = False, returnreturnFeeWaivedAmount = False, returnreturnFirstName = False, returnreturnFlaggedMissingAssignmentsCount = False, returnreturnGrade = False, returnreturnHandbookSigned = False, returnreturnHasActiveCareerPlanDeclarationTimePeriod = False, returnreturnHasActiveEndorsementDeclarationTimePeriod = False, returnreturnHasConflictedStudentCourseRequest = False, returnreturnHasFlaggedMissingAssignments = False, returnreturnHasMissingAssignments = False, returnreturnHasNoAttendanceToday = False, returnreturnHasOpenDisplayPeriodsInRegularSchoolDay = False, returnreturnHasOverscheduledPeriod = False, returnreturnHasValidStudentPlan = False, returnreturnHomeroomCodeFollettDestiny = False, returnreturnHomeroomID = False, returnreturnHomeroomPeriodFollettDestiny = False, returnreturnHomeroomStaffNameFollettDestiny = False, returnreturnIncludeAsProspectiveRank = False, returnreturnIsActive = False, returnreturnIsCrossEntityCourseEnrollment = False, returnreturnIsDefaultEntity = False, returnreturnIsTransportationRequested = False, returnreturnLastName = False, returnreturnMiddleName = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnNumberOfStudentCourseRequests = False, returnreturnNumberOfStudentSections = False, returnreturnOptOutOfMedia = False, returnreturnSchedulingCategories = False, returnreturnSchedulingTeamID = False, returnreturnSchoolYearID = False, returnreturnSectionLengthAbsent = False, returnreturnSectionLengthEnrolled = False, returnreturnSemester2Absent = False, returnreturnSemester2Enrolled = False, returnreturnSignedAcceptableUsePolicy = False, returnreturnStaffIDAdvisor = False, returnreturnStaffIDDisciplineOfficer = False, returnreturnStudentID = False, returnreturnStudentNumber = False, returnreturnTardyCountYTD = False, returnreturnTardyKioskTotals = False, returnreturnTotalEarnedCreditsPossibleAnticipatedNonTransferStudentSectionsNonAlternateRequestCredits = False, returnreturnTotalMissedAssignmentCount = False, returnreturnUILFeeReceived = False, returnreturnUnscheduleableStudentSectionCount = False, returnreturnUnscheduledStudentCourseRequestCount = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWithdrawalDate = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentEntityYear/" + str(StudentEntityYearID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentEntityYear(StudentEntityYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentEntityYear/" + str(StudentEntityYearID), verb = "delete")

	return(response)

def getEveryStudentType(EntityID = 1, page = 1, pageSize = 100, returnStudentTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentType/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentType(StudentTypeID, EntityID = 1, returnreturnStudentTypeID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentType/" + str(StudentTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentType(StudentTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentType/" + str(StudentTypeID), verb = "delete")

	return(response)

def getEveryTempAffectedWithdrawalRecord(EntityID = 1, page = 1, pageSize = 100, returnTempAffectedWithdrawalRecordID = True, returnAction = False, returnActionCode = False, returnActionMessage = False, returnAffectedPrimaryKey = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHasAttendance = False, returnHasFutureAttendance = False, returnHasFutureGrades = False, returnHasGrades = False, returnHasPartiallyPaidFees = False, returnIsFutureEntryWithdrawal = False, returnModifiedTime = False, returnMostFutureGradeStartDate = False, returnNameIDRequestedBy = False, returnNewEndDate = False, returnRecordType = False, returnRecordTypeCode = False, returnSchoolYearID = False, returnSection = False, returnSectionID = False, returnStartDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempAffectedWithdrawalRecord/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempAffectedWithdrawalRecord(TempAffectedWithdrawalRecordID, EntityID = 1, returnreturnTempAffectedWithdrawalRecordID = False, returnreturnAction = False, returnreturnActionCode = False, returnreturnActionMessage = False, returnreturnAffectedPrimaryKey = False, returnreturnCourseID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnEndDate = False, returnreturnEntityID = False, returnreturnHasAttendance = False, returnreturnHasFutureAttendance = False, returnreturnHasFutureGrades = False, returnreturnHasGrades = False, returnreturnHasPartiallyPaidFees = False, returnreturnIsFutureEntryWithdrawal = False, returnreturnModifiedTime = False, returnreturnMostFutureGradeStartDate = False, returnreturnNameIDRequestedBy = False, returnreturnNewEndDate = False, returnreturnRecordType = False, returnreturnRecordTypeCode = False, returnreturnSchoolYearID = False, returnreturnSection = False, returnreturnSectionID = False, returnreturnStartDate = False, returnreturnStudentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempAffectedWithdrawalRecord/" + str(TempAffectedWithdrawalRecordID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAffectedWithdrawalRecord(TempAffectedWithdrawalRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempAffectedWithdrawalRecord/" + str(TempAffectedWithdrawalRecordID), verb = "delete")

	return(response)

def getEveryTempHomeroomError(EntityID = 1, page = 1, pageSize = 100, returnTempHomeroomErrorID = True, returnCode = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnTempHomeroomRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomError/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempHomeroomError(TempHomeroomErrorID, EntityID = 1, returnreturnTempHomeroomErrorID = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnFailureReason = False, returnreturnModifiedTime = False, returnreturnTempHomeroomRecordID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomError/" + str(TempHomeroomErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempHomeroomError(TempHomeroomErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomError/" + str(TempHomeroomErrorID), verb = "delete")

	return(response)

def getEveryTempHomeroomRecord(EntityID = 1, page = 1, pageSize = 100, returnTempHomeroomRecordID = True, returnBuilding = False, returnBuildingID = False, returnCode = False, returnColumnIndex = False, returnCreatedTime = False, returnHasSaveError = False, returnHomeroomID = False, returnIsOverwrite = False, returnModifiedTime = False, returnRoom = False, returnRoomID = False, returnSchoolYear = False, returnSchoolYearID = False, returnStaff = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomRecord/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempHomeroomRecord(TempHomeroomRecordID, EntityID = 1, returnreturnTempHomeroomRecordID = False, returnreturnBuilding = False, returnreturnBuildingID = False, returnreturnCode = False, returnreturnColumnIndex = False, returnreturnCreatedTime = False, returnreturnHasSaveError = False, returnreturnHomeroomID = False, returnreturnIsOverwrite = False, returnreturnModifiedTime = False, returnreturnRoom = False, returnreturnRoomID = False, returnreturnSchoolYear = False, returnreturnSchoolYearID = False, returnreturnStaff = False, returnreturnStaffID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomRecord/" + str(TempHomeroomRecordID), verb = "get", params_list = params_list)

	return(response)

def deleteTempHomeroomRecord(TempHomeroomRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomRecord/" + str(TempHomeroomRecordID), verb = "delete")

	return(response)

def getEveryTempNoShowEntryWithdrawal(EntityID = 1, page = 1, pageSize = 100, returnTempNoShowEntryWithdrawalID = True, returnCreatedTime = False, returnDisplayAction = False, returnDisplayActionCode = False, returnEndDate = False, returnEntity = False, returnEntryCode = False, returnEntryWithdrawalID = False, returnFailureReason = False, returnGradeLevel = False, returnModifiedTime = False, returnNoShowAction = False, returnNoShowActionCode = False, returnNoShowEntryWithdrawalType = False, returnNoShowEntryWithdrawalTypeCode = False, returnNoShowTypeOfNoShow = False, returnNoShowTypeOfNoShowCode = False, returnSchoolYear = False, returnSchoolYearID = False, returnStartDate = False, returnStudent = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCode = False, returnWithdrawalCodeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNoShowEntryWithdrawal/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempNoShowEntryWithdrawal(TempNoShowEntryWithdrawalID, EntityID = 1, returnreturnTempNoShowEntryWithdrawalID = False, returnreturnCreatedTime = False, returnreturnDisplayAction = False, returnreturnDisplayActionCode = False, returnreturnEndDate = False, returnreturnEntity = False, returnreturnEntryCode = False, returnreturnEntryWithdrawalID = False, returnreturnFailureReason = False, returnreturnGradeLevel = False, returnreturnModifiedTime = False, returnreturnNoShowAction = False, returnreturnNoShowActionCode = False, returnreturnNoShowEntryWithdrawalType = False, returnreturnNoShowEntryWithdrawalTypeCode = False, returnreturnNoShowTypeOfNoShow = False, returnreturnNoShowTypeOfNoShowCode = False, returnreturnSchoolYear = False, returnreturnSchoolYearID = False, returnreturnStartDate = False, returnreturnStudent = False, returnreturnStudentID = False, returnreturnStudentNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWithdrawalCode = False, returnreturnWithdrawalCodeID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNoShowEntryWithdrawal/" + str(TempNoShowEntryWithdrawalID), verb = "get", params_list = params_list)

	return(response)

def deleteTempNoShowEntryWithdrawal(TempNoShowEntryWithdrawalID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNoShowEntryWithdrawal/" + str(TempNoShowEntryWithdrawalID), verb = "delete")

	return(response)

def getEveryTempStudentEnrollmentRecord(EntityID = 1, page = 1, pageSize = 100, returnTempStudentEnrollmentRecordID = True, returnAdvisorFullName = False, returnCalendarCode = False, returnCalendarID = False, returnCompletedSchoolYearOverride = False, returnCreatedTime = False, returnCreateFeeManagementCustomer = False, returnCreateFeeManagementCustomerEntityYear = False, returnDisciplineOfficerFullName = False, returnEdFiDistrictIDResidence = False, returnEdFiDistrictIDTransfer = False, returnEdFiDistrictResidenceCodeDescription = False, returnEdFiSchoolIDTransfer = False, returnEndDate = False, returnEnrollIntoEntityCode = False, returnEnrollmentMoveable = False, returnEntityCode = False, returnEntityID = False, returnEntryCode = False, returnEntryCodeID = False, returnEntryComment = False, returnEntryWithdrawalID = False, returnExcludeFromHonorRoll = False, returnExcludeFromRank = False, returnExcludeFromThirdFridaySeptemberCount = False, returnFailureReason = False, returnFeeManagementCustomerID = False, returnGradeLevelCode = False, returnGradeReferenceID = False, returnGradYear = False, returnGSAADAClaimableOverrideCode = False, returnGSAADAClaimableOverrideCodeDisplayName = False, returnHomeroomCode = False, returnHomeroomID = False, returnIncludeAsProspectiveRank = False, returnIsCurrentActive = False, returnIsDefaultEntityForEntryWithdrawal = False, returnIsDefaultEntityForStudentEntityYear = False, returnIsPermanentExit = False, returnIsPrivateSchoolChoiceStudent = False, returnIsTuitionPaidOutOfDistrict = False, returnModifiedTime = False, returnNumericYear = False, returnOutgoingStudent = False, returnPercentEnrolled = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnScheduledSectionCount = False, returnSchoolCode = False, returnSchoolID = False, returnSchoolYearID = False, returnServingRCDTSOverrideCode = False, returnServingRCDTSOverrideCodeDisplayName = False, returnServingRCDTSOverrideID = False, returnSourceEntryWithdrawalID = False, returnStaffIDAdvisor = False, returnStaffIDDisciplineOfficer = False, returnStartDate = False, returnStateAidCategoryMNID = False, returnStateDistrictMNCodeName = False, returnStateDistrictMNID = False, returnStateLastAttendanceLocationCodeMNID = False, returnStudentCourseRequestNotMoveableCount = False, returnStudentCourseRequestToDeleteCount = False, returnStudentFullName = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnStudentTypeID = False, returnTestingSchoolCode = False, returnTestingSchoolCodeDisplayName = False, returnTestingSchoolRCDTSOverrideCode = False, returnTestingSchoolRCDTSOverrideCodeDisplayName = False, returnTestingSchoolRCDTSOverrideID = False, returnTotalStudentCourseRequestCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCode = False, returnWithdrawalCodeID = False, returnWithdrawalComment = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentRecord/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempStudentEnrollmentRecord(TempStudentEnrollmentRecordID, EntityID = 1, returnreturnTempStudentEnrollmentRecordID = False, returnreturnAdvisorFullName = False, returnreturnCalendarCode = False, returnreturnCalendarID = False, returnreturnCompletedSchoolYearOverride = False, returnreturnCreatedTime = False, returnreturnCreateFeeManagementCustomer = False, returnreturnCreateFeeManagementCustomerEntityYear = False, returnreturnDisciplineOfficerFullName = False, returnreturnEdFiDistrictIDResidence = False, returnreturnEdFiDistrictIDTransfer = False, returnreturnEdFiDistrictResidenceCodeDescription = False, returnreturnEdFiSchoolIDTransfer = False, returnreturnEndDate = False, returnreturnEnrollIntoEntityCode = False, returnreturnEnrollmentMoveable = False, returnreturnEntityCode = False, returnreturnEntityID = False, returnreturnEntryCode = False, returnreturnEntryCodeID = False, returnreturnEntryComment = False, returnreturnEntryWithdrawalID = False, returnreturnExcludeFromHonorRoll = False, returnreturnExcludeFromRank = False, returnreturnExcludeFromThirdFridaySeptemberCount = False, returnreturnFailureReason = False, returnreturnFeeManagementCustomerID = False, returnreturnGradeLevelCode = False, returnreturnGradeReferenceID = False, returnreturnGradYear = False, returnreturnGSAADAClaimableOverrideCode = False, returnreturnGSAADAClaimableOverrideCodeDisplayName = False, returnreturnHomeroomCode = False, returnreturnHomeroomID = False, returnreturnIncludeAsProspectiveRank = False, returnreturnIsCurrentActive = False, returnreturnIsDefaultEntityForEntryWithdrawal = False, returnreturnIsDefaultEntityForStudentEntityYear = False, returnreturnIsPermanentExit = False, returnreturnIsPrivateSchoolChoiceStudent = False, returnreturnIsTuitionPaidOutOfDistrict = False, returnreturnModifiedTime = False, returnreturnNumericYear = False, returnreturnOutgoingStudent = False, returnreturnPercentEnrolled = False, returnreturnPromotionStatus = False, returnreturnPromotionStatusCode = False, returnreturnScheduledSectionCount = False, returnreturnSchoolCode = False, returnreturnSchoolID = False, returnreturnSchoolYearID = False, returnreturnServingRCDTSOverrideCode = False, returnreturnServingRCDTSOverrideCodeDisplayName = False, returnreturnServingRCDTSOverrideID = False, returnreturnSourceEntryWithdrawalID = False, returnreturnStaffIDAdvisor = False, returnreturnStaffIDDisciplineOfficer = False, returnreturnStartDate = False, returnreturnStateAidCategoryMNID = False, returnreturnStateDistrictMNCodeName = False, returnreturnStateDistrictMNID = False, returnreturnStateLastAttendanceLocationCodeMNID = False, returnreturnStudentCourseRequestNotMoveableCount = False, returnreturnStudentCourseRequestToDeleteCount = False, returnreturnStudentFullName = False, returnreturnStudentID = False, returnreturnStudentNumber = False, returnreturnStudentTypeCode = False, returnreturnStudentTypeID = False, returnreturnTestingSchoolCode = False, returnreturnTestingSchoolCodeDisplayName = False, returnreturnTestingSchoolRCDTSOverrideCode = False, returnreturnTestingSchoolRCDTSOverrideCodeDisplayName = False, returnreturnTestingSchoolRCDTSOverrideID = False, returnreturnTotalStudentCourseRequestCount = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWithdrawalCode = False, returnreturnWithdrawalCodeID = False, returnreturnWithdrawalComment = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentRecord/" + str(TempStudentEnrollmentRecordID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStudentEnrollmentRecord(TempStudentEnrollmentRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentRecord/" + str(TempStudentEnrollmentRecordID), verb = "delete")

	return(response)

def getEveryTempStudentEntityYear(EntityID = 1, page = 1, pageSize = 100, returnTempStudentEntityYearID = True, returnAdvisorDetails = False, returnCreatedTime = False, returnCurrentAdvisorDetails = False, returnCurrentHomeroomDetails = False, returnGenderCode = False, returnGradeLevelCodeDescription = False, returnHomeroomDetails = False, returnHomeroomID = False, returnIsActive = False, returnMessage = False, returnModifiedTime = False, returnStaffIDAdvisor = False, returnStudentEntityYearID = False, returnStudentFullName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempStudentEntityYear(TempStudentEntityYearID, EntityID = 1, returnreturnTempStudentEntityYearID = False, returnreturnAdvisorDetails = False, returnreturnCreatedTime = False, returnreturnCurrentAdvisorDetails = False, returnreturnCurrentHomeroomDetails = False, returnreturnGenderCode = False, returnreturnGradeLevelCodeDescription = False, returnreturnHomeroomDetails = False, returnreturnHomeroomID = False, returnreturnIsActive = False, returnreturnMessage = False, returnreturnModifiedTime = False, returnreturnStaffIDAdvisor = False, returnreturnStudentEntityYearID = False, returnreturnStudentFullName = False, returnreturnStudentNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEntityYear/" + str(TempStudentEntityYearID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStudentEntityYear(TempStudentEntityYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEntityYear/" + str(TempStudentEntityYearID), verb = "delete")

	return(response)

def getEveryWithdrawalCode(EntityID = 1, page = 1, pageSize = 100, returnWithdrawalCodeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEdFiExitWithdrawID = False, returnIsCrossEntityCourseEnrollment = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateStatusEndCodeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeIDClonedFrom = False, returnWithdrawalCodeMNID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/WithdrawalCode/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getWithdrawalCode(WithdrawalCodeID, EntityID = 1, returnreturnWithdrawalCodeID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnEdFiExitWithdrawID = False, returnreturnIsCrossEntityCourseEnrollment = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnStateStatusEndCodeMNID = False, returnreturnType = False, returnreturnTypeCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWithdrawalCodeIDClonedFrom = False, returnreturnWithdrawalCodeMNID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/WithdrawalCode/" + str(WithdrawalCodeID), verb = "get", params_list = params_list)

	return(response)

def deleteWithdrawalCode(WithdrawalCodeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/WithdrawalCode/" + str(WithdrawalCodeID), verb = "delete")

	return(response)