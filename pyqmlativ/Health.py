# This module contains Health functions.

from .Utilities import make_request

import pandas as pd

def getEveryAdministerNameMedication(EntityID = 1, page = 1, pageSize = 100, returnAdministerNameMedicationID = True, returnAdministerDate = False, returnAdministerDateOnly = False, returnAdministrationTime = False, returnCreatedTime = False, returnDosesAdministered = False, returnIsVoid = False, returnLocationID = False, returnModifiedTime = False, returnNameMedicationID = False, returnNameMedicationScheduleID = False, returnNameOfficeVisitID = False, returnNote = False, returnNotPerformedReasonID = False, returnStaffIDAdministeredBy = False, returnTotalDosesToday = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/AdministerNameMedication/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAdministerNameMedication(AdministerNameMedicationID, EntityID = 1, returnreturnAdministerNameMedicationID = False, returnreturnAdministerDate = False, returnreturnAdministerDateOnly = False, returnreturnAdministrationTime = False, returnreturnCreatedTime = False, returnreturnDosesAdministered = False, returnreturnIsVoid = False, returnreturnLocationID = False, returnreturnModifiedTime = False, returnreturnNameMedicationID = False, returnreturnNameMedicationScheduleID = False, returnreturnNameOfficeVisitID = False, returnreturnNote = False, returnreturnNotPerformedReasonID = False, returnreturnStaffIDAdministeredBy = False, returnreturnTotalDosesToday = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserIDVoidedBy = False, returnreturnVoidedTime = False, returnreturnVoidNote = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/AdministerNameMedication/" + str(AdministerNameMedicationID), verb = "get", params_list = params_list)

	return(response)

def deleteAdministerNameMedication(AdministerNameMedicationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/AdministerNameMedication/" + str(AdministerNameMedicationID), verb = "delete")

	return(response)

def getEveryBodyMassIndexPercentile(EntityID = 1, page = 1, pageSize = 100, returnBodyMassIndexPercentileID = True, returnAgeInMonths = False, returnCoefficientOfVariation = False, returnCreatedTime = False, returnEightyFifthPercentile = False, returnFifthPercentile = False, returnFiftiethPercentile = False, returnGender = False, returnGenderCode = False, returnMedian = False, returnModifiedTime = False, returnNinetyFifthPercentile = False, returnNinetySeventhPercentile = False, returnPower = False, returnSeventyFifthPercentile = False, returnSkywardHash = False, returnSkywardID = False, returnTenthPercentile = False, returnThirdPercentile = False, returnTwentyFifthPercentile = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/BodyMassIndexPercentile/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getBodyMassIndexPercentile(BodyMassIndexPercentileID, EntityID = 1, returnreturnBodyMassIndexPercentileID = False, returnreturnAgeInMonths = False, returnreturnCoefficientOfVariation = False, returnreturnCreatedTime = False, returnreturnEightyFifthPercentile = False, returnreturnFifthPercentile = False, returnreturnFiftiethPercentile = False, returnreturnGender = False, returnreturnGenderCode = False, returnreturnMedian = False, returnreturnModifiedTime = False, returnreturnNinetyFifthPercentile = False, returnreturnNinetySeventhPercentile = False, returnreturnPower = False, returnreturnSeventyFifthPercentile = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnTenthPercentile = False, returnreturnThirdPercentile = False, returnreturnTwentyFifthPercentile = False, returnreturnType = False, returnreturnTypeCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/BodyMassIndexPercentile/" + str(BodyMassIndexPercentileID), verb = "get", params_list = params_list)

	return(response)

def deleteBodyMassIndexPercentile(BodyMassIndexPercentileID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/BodyMassIndexPercentile/" + str(BodyMassIndexPercentileID), verb = "delete")

	return(response)

def getEveryBodyPart(EntityID = 1, page = 1, pageSize = 100, returnBodyPartID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/BodyPart/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getBodyPart(BodyPartID, EntityID = 1, returnreturnBodyPartID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/BodyPart/" + str(BodyPartID), verb = "get", params_list = params_list)

	return(response)

def deleteBodyPart(BodyPartID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/BodyPart/" + str(BodyPartID), verb = "delete")

	return(response)

def getEveryChildhoodIllness(EntityID = 1, page = 1, pageSize = 100, returnChildhoodIllnessID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllness/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getChildhoodIllness(ChildhoodIllnessID, EntityID = 1, returnreturnChildhoodIllnessID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllness/" + str(ChildhoodIllnessID), verb = "get", params_list = params_list)

	return(response)

def deleteChildhoodIllness(ChildhoodIllnessID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllness/" + str(ChildhoodIllnessID), verb = "delete")

	return(response)

def getEveryChildhoodIllnessComment(EntityID = 1, page = 1, pageSize = 100, returnChildhoodIllnessCommentID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessComment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getChildhoodIllnessComment(ChildhoodIllnessCommentID, EntityID = 1, returnreturnChildhoodIllnessCommentID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessComment/" + str(ChildhoodIllnessCommentID), verb = "get", params_list = params_list)

	return(response)

def deleteChildhoodIllnessComment(ChildhoodIllnessCommentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessComment/" + str(ChildhoodIllnessCommentID), verb = "delete")

	return(response)

def getEveryChildhoodIllnessGuardianNotification(EntityID = 1, page = 1, pageSize = 100, returnChildhoodIllnessGuardianNotificationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessGuardianNotification/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getChildhoodIllnessGuardianNotification(ChildhoodIllnessGuardianNotificationID, EntityID = 1, returnreturnChildhoodIllnessGuardianNotificationID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessGuardianNotification/" + str(ChildhoodIllnessGuardianNotificationID), verb = "get", params_list = params_list)

	return(response)

def deleteChildhoodIllnessGuardianNotification(ChildhoodIllnessGuardianNotificationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessGuardianNotification/" + str(ChildhoodIllnessGuardianNotificationID), verb = "delete")

	return(response)

def getEveryChildhoodIllnessGuardianResponse(EntityID = 1, page = 1, pageSize = 100, returnChildhoodIllnessGuardianResponseID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getChildhoodIllnessGuardianResponse(ChildhoodIllnessGuardianResponseID, EntityID = 1, returnreturnChildhoodIllnessGuardianResponseID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessGuardianResponse/" + str(ChildhoodIllnessGuardianResponseID), verb = "get", params_list = params_list)

	return(response)

def deleteChildhoodIllnessGuardianResponse(ChildhoodIllnessGuardianResponseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessGuardianResponse/" + str(ChildhoodIllnessGuardianResponseID), verb = "delete")

	return(response)

def getEveryChildhoodIllnessObservation(EntityID = 1, page = 1, pageSize = 100, returnChildhoodIllnessObservationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessObservation/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getChildhoodIllnessObservation(ChildhoodIllnessObservationID, EntityID = 1, returnreturnChildhoodIllnessObservationID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessObservation/" + str(ChildhoodIllnessObservationID), verb = "get", params_list = params_list)

	return(response)

def deleteChildhoodIllnessObservation(ChildhoodIllnessObservationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessObservation/" + str(ChildhoodIllnessObservationID), verb = "delete")

	return(response)

def getEveryChildhoodIllnessReferralReason(EntityID = 1, page = 1, pageSize = 100, returnChildhoodIllnessReferralReasonID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessReferralReason/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getChildhoodIllnessReferralReason(ChildhoodIllnessReferralReasonID, EntityID = 1, returnreturnChildhoodIllnessReferralReasonID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessReferralReason/" + str(ChildhoodIllnessReferralReasonID), verb = "get", params_list = params_list)

	return(response)

def deleteChildhoodIllnessReferralReason(ChildhoodIllnessReferralReasonID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessReferralReason/" + str(ChildhoodIllnessReferralReasonID), verb = "delete")

	return(response)

def getEveryChildhoodIllnessReferralResult(EntityID = 1, page = 1, pageSize = 100, returnChildhoodIllnessReferralResultID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessReferralResult/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getChildhoodIllnessReferralResult(ChildhoodIllnessReferralResultID, EntityID = 1, returnreturnChildhoodIllnessReferralResultID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessReferralResult/" + str(ChildhoodIllnessReferralResultID), verb = "get", params_list = params_list)

	return(response)

def deleteChildhoodIllnessReferralResult(ChildhoodIllnessReferralResultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessReferralResult/" + str(ChildhoodIllnessReferralResultID), verb = "delete")

	return(response)

def getEveryComplianceSchedule(EntityID = 1, page = 1, pageSize = 100, returnComplianceScheduleID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnIsDistrictDefined = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ComplianceSchedule/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getComplianceSchedule(ComplianceScheduleID, EntityID = 1, returnreturnComplianceScheduleID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnIsDistrictDefined = False, returnreturnModifiedTime = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ComplianceSchedule/" + str(ComplianceScheduleID), verb = "get", params_list = params_list)

	return(response)

def deleteComplianceSchedule(ComplianceScheduleID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ComplianceSchedule/" + str(ComplianceScheduleID), verb = "delete")

	return(response)

def getEveryComplianceScheduleDetail(EntityID = 1, page = 1, pageSize = 100, returnComplianceScheduleDetailID = True, returnAgeGradeType = False, returnAgeGradeTypeCode = False, returnAgeGradeValue = False, returnAgeUnit = False, returnAgeUnitCode = False, returnComplianceScheduleDetailIDClonedFrom = False, returnCreatedTime = False, returnDoseCount = False, returnIsDistrictDefined = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationYearComplianceScheduleID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ComplianceScheduleDetail/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getComplianceScheduleDetail(ComplianceScheduleDetailID, EntityID = 1, returnreturnComplianceScheduleDetailID = False, returnreturnAgeGradeType = False, returnreturnAgeGradeTypeCode = False, returnreturnAgeGradeValue = False, returnreturnAgeUnit = False, returnreturnAgeUnitCode = False, returnreturnComplianceScheduleDetailIDClonedFrom = False, returnreturnCreatedTime = False, returnreturnDoseCount = False, returnreturnIsDistrictDefined = False, returnreturnModifiedTime = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVaccinationYearComplianceScheduleID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ComplianceScheduleDetail/" + str(ComplianceScheduleDetailID), verb = "get", params_list = params_list)

	return(response)

def deleteComplianceScheduleDetail(ComplianceScheduleDetailID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ComplianceScheduleDetail/" + str(ComplianceScheduleDetailID), verb = "delete")

	return(response)

def getEveryComplianceScheduleDetailBooster(EntityID = 1, page = 1, pageSize = 100, returnComplianceScheduleDetailBoosterID = True, returnComplianceScheduleDetailBoosterIDClonedFrom = False, returnComplianceScheduleDetailID = False, returnCreatedTime = False, returnIntervalTime = False, returnIntervalTimeUnit = False, returnIntervalTimeUnitCode = False, returnIsDistrictDefined = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccineID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ComplianceScheduleDetailBooster/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getComplianceScheduleDetailBooster(ComplianceScheduleDetailBoosterID, EntityID = 1, returnreturnComplianceScheduleDetailBoosterID = False, returnreturnComplianceScheduleDetailBoosterIDClonedFrom = False, returnreturnComplianceScheduleDetailID = False, returnreturnCreatedTime = False, returnreturnIntervalTime = False, returnreturnIntervalTimeUnit = False, returnreturnIntervalTimeUnitCode = False, returnreturnIsDistrictDefined = False, returnreturnModifiedTime = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVaccineID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ComplianceScheduleDetailBooster/" + str(ComplianceScheduleDetailBoosterID), verb = "get", params_list = params_list)

	return(response)

def deleteComplianceScheduleDetailBooster(ComplianceScheduleDetailBoosterID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ComplianceScheduleDetailBooster/" + str(ComplianceScheduleDetailBoosterID), verb = "delete")

	return(response)

def getEveryComplianceScheduleRule(EntityID = 1, page = 1, pageSize = 100, returnComplianceScheduleRuleID = True, returnCode = False, returnCodeDescription = False, returnComplianceScheduleID = False, returnCreatedTime = False, returnDescription = False, returnGracePeriodDays = False, returnModifiedTime = False, returnRule = False, returnRuleDescription = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ComplianceScheduleRule/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getComplianceScheduleRule(ComplianceScheduleRuleID, EntityID = 1, returnreturnComplianceScheduleRuleID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnComplianceScheduleID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnGracePeriodDays = False, returnreturnModifiedTime = False, returnreturnRule = False, returnreturnRuleDescription = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ComplianceScheduleRule/" + str(ComplianceScheduleRuleID), verb = "get", params_list = params_list)

	return(response)

def deleteComplianceScheduleRule(ComplianceScheduleRuleID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ComplianceScheduleRule/" + str(ComplianceScheduleRuleID), verb = "delete")

	return(response)

def getEveryConfigDistrictGroup(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictGroupID = True, returnCreatedTime = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUseNationalChartForBodyMassIndexPercentile = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ConfigDistrictGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigDistrictGroup(ConfigDistrictGroupID, EntityID = 1, returnreturnConfigDistrictGroupID = False, returnreturnCreatedTime = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnModifiedTime = False, returnreturnUseNationalChartForBodyMassIndexPercentile = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ConfigDistrictGroup/" + str(ConfigDistrictGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigDistrictGroup(ConfigDistrictGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ConfigDistrictGroup/" + str(ConfigDistrictGroupID), verb = "delete")

	return(response)

def getEveryConfigDistrictYear(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictYearID = True, returnAgeEffectiveDate = False, returnComplianceYearStart = False, returnComplianceYearStartCode = False, returnCreatedTime = False, returnDisplayLotNumber = False, returnDistrictID = False, returnModifiedTime = False, returnProvisionalCalculationType = False, returnProvisionalCalculationTypeCode = False, returnProvisionalDays = False, returnSchoolYearID = False, returnShowVaccinationComplianceConditionalIndicator = False, returnUseComplianceDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationComplianceConditionalIndicator = False, returnVaccinationComplianceIsProcessing = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, returnreturnConfigDistrictYearID = False, returnreturnAgeEffectiveDate = False, returnreturnComplianceYearStart = False, returnreturnComplianceYearStartCode = False, returnreturnCreatedTime = False, returnreturnDisplayLotNumber = False, returnreturnDistrictID = False, returnreturnModifiedTime = False, returnreturnProvisionalCalculationType = False, returnreturnProvisionalCalculationTypeCode = False, returnreturnProvisionalDays = False, returnreturnSchoolYearID = False, returnreturnShowVaccinationComplianceConditionalIndicator = False, returnreturnUseComplianceDate = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVaccinationComplianceConditionalIndicator = False, returnreturnVaccinationComplianceIsProcessing = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigDistrictYear(ConfigDistrictYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "delete")

	return(response)

def getEveryConfigEntity(EntityID = 1, page = 1, pageSize = 100, returnConfigEntityID = True, returnCreatedTime = False, returnEntityID = False, returnLocationIDMedicationQuickEntryDefault = False, returnModifiedTime = False, returnStaffIDMedicationQuickEntryDefault = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ConfigEntity/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigEntity(ConfigEntityID, EntityID = 1, returnreturnConfigEntityID = False, returnreturnCreatedTime = False, returnreturnEntityID = False, returnreturnLocationIDMedicationQuickEntryDefault = False, returnreturnModifiedTime = False, returnreturnStaffIDMedicationQuickEntryDefault = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ConfigEntity/" + str(ConfigEntityID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigEntity(ConfigEntityID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ConfigEntity/" + str(ConfigEntityID), verb = "delete")

	return(response)

def getEveryDentalComment(EntityID = 1, page = 1, pageSize = 100, returnDentalCommentID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalComment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDentalComment(DentalCommentID, EntityID = 1, returnreturnDentalCommentID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalComment/" + str(DentalCommentID), verb = "get", params_list = params_list)

	return(response)

def deleteDentalComment(DentalCommentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalComment/" + str(DentalCommentID), verb = "delete")

	return(response)

def getEveryDentalGuardianNotification(EntityID = 1, page = 1, pageSize = 100, returnDentalGuardianNotificationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalGuardianNotification/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDentalGuardianNotification(DentalGuardianNotificationID, EntityID = 1, returnreturnDentalGuardianNotificationID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalGuardianNotification/" + str(DentalGuardianNotificationID), verb = "get", params_list = params_list)

	return(response)

def deleteDentalGuardianNotification(DentalGuardianNotificationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalGuardianNotification/" + str(DentalGuardianNotificationID), verb = "delete")

	return(response)

def getEveryDentalGuardianResponse(EntityID = 1, page = 1, pageSize = 100, returnDentalGuardianResponseID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDentalGuardianResponse(DentalGuardianResponseID, EntityID = 1, returnreturnDentalGuardianResponseID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalGuardianResponse/" + str(DentalGuardianResponseID), verb = "get", params_list = params_list)

	return(response)

def deleteDentalGuardianResponse(DentalGuardianResponseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalGuardianResponse/" + str(DentalGuardianResponseID), verb = "delete")

	return(response)

def getEveryDentalReferralReason(EntityID = 1, page = 1, pageSize = 100, returnDentalReferralReasonID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalReferralReason/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDentalReferralReason(DentalReferralReasonID, EntityID = 1, returnreturnDentalReferralReasonID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalReferralReason/" + str(DentalReferralReasonID), verb = "get", params_list = params_list)

	return(response)

def deleteDentalReferralReason(DentalReferralReasonID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalReferralReason/" + str(DentalReferralReasonID), verb = "delete")

	return(response)

def getEveryDentalReferralResult(EntityID = 1, page = 1, pageSize = 100, returnDentalReferralResultID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalReferralResult/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDentalReferralResult(DentalReferralResultID, EntityID = 1, returnreturnDentalReferralResultID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalReferralResult/" + str(DentalReferralResultID), verb = "get", params_list = params_list)

	return(response)

def deleteDentalReferralResult(DentalReferralResultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalReferralResult/" + str(DentalReferralResultID), verb = "delete")

	return(response)

def getEveryDentalScreening(EntityID = 1, page = 1, pageSize = 100, returnDentalScreeningID = True, returnCreatedTime = False, returnDentalScreeningResultID = False, returnDentalTreatmentID = False, returnDistrictID = False, returnHealthProfessionalIDExaminedBy = False, returnIsVoid = False, returnModifiedTime = False, returnNameID = False, returnSchoolYearID = False, returnScreeningDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreening/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDentalScreening(DentalScreeningID, EntityID = 1, returnreturnDentalScreeningID = False, returnreturnCreatedTime = False, returnreturnDentalScreeningResultID = False, returnreturnDentalTreatmentID = False, returnreturnDistrictID = False, returnreturnHealthProfessionalIDExaminedBy = False, returnreturnIsVoid = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnSchoolYearID = False, returnreturnScreeningDate = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserIDVoidedBy = False, returnreturnVoidedTime = False, returnreturnVoidNote = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreening/" + str(DentalScreeningID), verb = "get", params_list = params_list)

	return(response)

def deleteDentalScreening(DentalScreeningID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreening/" + str(DentalScreeningID), verb = "delete")

	return(response)

def getEveryDentalScreeningComment(EntityID = 1, page = 1, pageSize = 100, returnDentalScreeningCommentID = True, returnCreatedTime = False, returnDentalCommentID = False, returnDentalScreeningID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningComment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDentalScreeningComment(DentalScreeningCommentID, EntityID = 1, returnreturnDentalScreeningCommentID = False, returnreturnCreatedTime = False, returnreturnDentalCommentID = False, returnreturnDentalScreeningID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningComment/" + str(DentalScreeningCommentID), verb = "get", params_list = params_list)

	return(response)

def deleteDentalScreeningComment(DentalScreeningCommentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningComment/" + str(DentalScreeningCommentID), verb = "delete")

	return(response)

def getEveryDentalScreeningNote(EntityID = 1, page = 1, pageSize = 100, returnDentalScreeningNoteID = True, returnCreatedTime = False, returnDentalScreeningID = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDentalScreeningNote(DentalScreeningNoteID, EntityID = 1, returnreturnDentalScreeningNoteID = False, returnreturnCreatedTime = False, returnreturnDentalScreeningID = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningNote/" + str(DentalScreeningNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteDentalScreeningNote(DentalScreeningNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningNote/" + str(DentalScreeningNoteID), verb = "delete")

	return(response)

def getEveryDentalScreeningReferral(EntityID = 1, page = 1, pageSize = 100, returnDentalScreeningReferralID = True, returnCompletionDate = False, returnCreatedTime = False, returnDentalGuardianNotificationID = False, returnDentalGuardianResponseID = False, returnDentalReferralReasonID = False, returnDentalReferralResultID = False, returnDentalScreeningID = False, returnHealthProfessionalIDReferredBy = False, returnHealthProfessionalIDReferredTo = False, returnModifiedTime = False, returnReferralCompleted = False, returnReferralDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningReferral/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDentalScreeningReferral(DentalScreeningReferralID, EntityID = 1, returnreturnDentalScreeningReferralID = False, returnreturnCompletionDate = False, returnreturnCreatedTime = False, returnreturnDentalGuardianNotificationID = False, returnreturnDentalGuardianResponseID = False, returnreturnDentalReferralReasonID = False, returnreturnDentalReferralResultID = False, returnreturnDentalScreeningID = False, returnreturnHealthProfessionalIDReferredBy = False, returnreturnHealthProfessionalIDReferredTo = False, returnreturnModifiedTime = False, returnreturnReferralCompleted = False, returnreturnReferralDate = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningReferral/" + str(DentalScreeningReferralID), verb = "get", params_list = params_list)

	return(response)

def deleteDentalScreeningReferral(DentalScreeningReferralID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningReferral/" + str(DentalScreeningReferralID), verb = "delete")

	return(response)

def getEveryDentalScreeningResult(EntityID = 1, page = 1, pageSize = 100, returnDentalScreeningResultID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningResult/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDentalScreeningResult(DentalScreeningResultID, EntityID = 1, returnreturnDentalScreeningResultID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningResult/" + str(DentalScreeningResultID), verb = "get", params_list = params_list)

	return(response)

def deleteDentalScreeningResult(DentalScreeningResultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningResult/" + str(DentalScreeningResultID), verb = "delete")

	return(response)

def getEveryDentalScreeningSecuredNote(EntityID = 1, page = 1, pageSize = 100, returnDentalScreeningSecuredNoteID = True, returnCreatedTime = False, returnDentalScreeningID = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningSecuredNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDentalScreeningSecuredNote(DentalScreeningSecuredNoteID, EntityID = 1, returnreturnDentalScreeningSecuredNoteID = False, returnreturnCreatedTime = False, returnreturnDentalScreeningID = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningSecuredNote/" + str(DentalScreeningSecuredNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteDentalScreeningSecuredNote(DentalScreeningSecuredNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningSecuredNote/" + str(DentalScreeningSecuredNoteID), verb = "delete")

	return(response)

def getEveryDentalTreatment(EntityID = 1, page = 1, pageSize = 100, returnDentalTreatmentID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalTreatment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDentalTreatment(DentalTreatmentID, EntityID = 1, returnreturnDentalTreatmentID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalTreatment/" + str(DentalTreatmentID), verb = "get", params_list = params_list)

	return(response)

def deleteDentalTreatment(DentalTreatmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalTreatment/" + str(DentalTreatmentID), verb = "delete")

	return(response)

def getEveryDiabetesCareLog(EntityID = 1, page = 1, pageSize = 100, returnDiabetesCareLogID = True, returnBloodGlucose = False, returnBloodGlucoseInsulin = False, returnBloodGlucoseNotChecked = False, returnBodyPartID = False, returnCarbIntake = False, returnCreatedTime = False, returnDiabetesKetoneResultID = False, returnDistrictID = False, returnFoodInsulin = False, returnInsulinDeliveryType = False, returnInsulinDeliveryTypeCode = False, returnInsulinDose = False, returnInsulinOnBoard = False, returnIsVoid = False, returnMedicationDosageUnitID = False, returnModifiedTime = False, returnNameID = False, returnNameOfficeVisitID = False, returnNotificationMethodID = False, returnParentNotified = False, returnRecheckBloodGlucose = False, returnRecheckTime = False, returnSchoolYearID = False, returnScreeningTime = False, returnScreeningTimeDate = False, returnScreeningTimeTime = False, returnTreatmentDescriptionsListDisplay = False, returnTreatments = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLog/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDiabetesCareLog(DiabetesCareLogID, EntityID = 1, returnreturnDiabetesCareLogID = False, returnreturnBloodGlucose = False, returnreturnBloodGlucoseInsulin = False, returnreturnBloodGlucoseNotChecked = False, returnreturnBodyPartID = False, returnreturnCarbIntake = False, returnreturnCreatedTime = False, returnreturnDiabetesKetoneResultID = False, returnreturnDistrictID = False, returnreturnFoodInsulin = False, returnreturnInsulinDeliveryType = False, returnreturnInsulinDeliveryTypeCode = False, returnreturnInsulinDose = False, returnreturnInsulinOnBoard = False, returnreturnIsVoid = False, returnreturnMedicationDosageUnitID = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnNameOfficeVisitID = False, returnreturnNotificationMethodID = False, returnreturnParentNotified = False, returnreturnRecheckBloodGlucose = False, returnreturnRecheckTime = False, returnreturnSchoolYearID = False, returnreturnScreeningTime = False, returnreturnScreeningTimeDate = False, returnreturnScreeningTimeTime = False, returnreturnTreatmentDescriptionsListDisplay = False, returnreturnTreatments = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserIDVoidedBy = False, returnreturnVoidedTime = False, returnreturnVoidNote = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLog/" + str(DiabetesCareLogID), verb = "get", params_list = params_list)

	return(response)

def deleteDiabetesCareLog(DiabetesCareLogID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLog/" + str(DiabetesCareLogID), verb = "delete")

	return(response)

def getEveryDiabetesCareLogNote(EntityID = 1, page = 1, pageSize = 100, returnDiabetesCareLogNoteID = True, returnCreatedTime = False, returnDiabetesCareLogID = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLogNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDiabetesCareLogNote(DiabetesCareLogNoteID, EntityID = 1, returnreturnDiabetesCareLogNoteID = False, returnreturnCreatedTime = False, returnreturnDiabetesCareLogID = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLogNote/" + str(DiabetesCareLogNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteDiabetesCareLogNote(DiabetesCareLogNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLogNote/" + str(DiabetesCareLogNoteID), verb = "delete")

	return(response)

def getEveryDiabetesCareLogReferral(EntityID = 1, page = 1, pageSize = 100, returnDiabetesCareLogReferralID = True, returnCompletionDate = False, returnCreatedTime = False, returnDiabetesCareLogID = False, returnDiabetesGuardianNotificationID = False, returnDiabetesGuardianResponseID = False, returnDiabetesReferralReasonID = False, returnDiabetesReferralResultID = False, returnHealthProfessionalIDReferredBy = False, returnHealthProfessionalIDReferredTo = False, returnModifiedTime = False, returnReferralCompleted = False, returnReferralDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLogReferral/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDiabetesCareLogReferral(DiabetesCareLogReferralID, EntityID = 1, returnreturnDiabetesCareLogReferralID = False, returnreturnCompletionDate = False, returnreturnCreatedTime = False, returnreturnDiabetesCareLogID = False, returnreturnDiabetesGuardianNotificationID = False, returnreturnDiabetesGuardianResponseID = False, returnreturnDiabetesReferralReasonID = False, returnreturnDiabetesReferralResultID = False, returnreturnHealthProfessionalIDReferredBy = False, returnreturnHealthProfessionalIDReferredTo = False, returnreturnModifiedTime = False, returnreturnReferralCompleted = False, returnreturnReferralDate = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLogReferral/" + str(DiabetesCareLogReferralID), verb = "get", params_list = params_list)

	return(response)

def deleteDiabetesCareLogReferral(DiabetesCareLogReferralID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLogReferral/" + str(DiabetesCareLogReferralID), verb = "delete")

	return(response)

def getEveryDiabetesCareLogSecuredNote(EntityID = 1, page = 1, pageSize = 100, returnDiabetesCareLogSecuredNoteID = True, returnCreatedTime = False, returnDiabetesCareLogID = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLogSecuredNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDiabetesCareLogSecuredNote(DiabetesCareLogSecuredNoteID, EntityID = 1, returnreturnDiabetesCareLogSecuredNoteID = False, returnreturnCreatedTime = False, returnreturnDiabetesCareLogID = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLogSecuredNote/" + str(DiabetesCareLogSecuredNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteDiabetesCareLogSecuredNote(DiabetesCareLogSecuredNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLogSecuredNote/" + str(DiabetesCareLogSecuredNoteID), verb = "delete")

	return(response)

def getEveryDiabetesCareLogTreatment(EntityID = 1, page = 1, pageSize = 100, returnDiabetesCareLogTreatmentID = True, returnCreatedTime = False, returnDiabetesCareLogID = False, returnDiabetesTreatmentID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLogTreatment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDiabetesCareLogTreatment(DiabetesCareLogTreatmentID, EntityID = 1, returnreturnDiabetesCareLogTreatmentID = False, returnreturnCreatedTime = False, returnreturnDiabetesCareLogID = False, returnreturnDiabetesTreatmentID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLogTreatment/" + str(DiabetesCareLogTreatmentID), verb = "get", params_list = params_list)

	return(response)

def deleteDiabetesCareLogTreatment(DiabetesCareLogTreatmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLogTreatment/" + str(DiabetesCareLogTreatmentID), verb = "delete")

	return(response)

def getEveryDiabetesGuardianNotification(EntityID = 1, page = 1, pageSize = 100, returnDiabetesGuardianNotificationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesGuardianNotification/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDiabetesGuardianNotification(DiabetesGuardianNotificationID, EntityID = 1, returnreturnDiabetesGuardianNotificationID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesGuardianNotification/" + str(DiabetesGuardianNotificationID), verb = "get", params_list = params_list)

	return(response)

def deleteDiabetesGuardianNotification(DiabetesGuardianNotificationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesGuardianNotification/" + str(DiabetesGuardianNotificationID), verb = "delete")

	return(response)

def getEveryDiabetesGuardianResponse(EntityID = 1, page = 1, pageSize = 100, returnDiabetesGuardianResponseID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDiabetesGuardianResponse(DiabetesGuardianResponseID, EntityID = 1, returnreturnDiabetesGuardianResponseID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesGuardianResponse/" + str(DiabetesGuardianResponseID), verb = "get", params_list = params_list)

	return(response)

def deleteDiabetesGuardianResponse(DiabetesGuardianResponseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesGuardianResponse/" + str(DiabetesGuardianResponseID), verb = "delete")

	return(response)

def getEveryDiabetesKetoneResult(EntityID = 1, page = 1, pageSize = 100, returnDiabetesKetoneResultID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesKetoneResult/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDiabetesKetoneResult(DiabetesKetoneResultID, EntityID = 1, returnreturnDiabetesKetoneResultID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesKetoneResult/" + str(DiabetesKetoneResultID), verb = "get", params_list = params_list)

	return(response)

def deleteDiabetesKetoneResult(DiabetesKetoneResultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesKetoneResult/" + str(DiabetesKetoneResultID), verb = "delete")

	return(response)

def getEveryDiabetesReferralReason(EntityID = 1, page = 1, pageSize = 100, returnDiabetesReferralReasonID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesReferralReason/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDiabetesReferralReason(DiabetesReferralReasonID, EntityID = 1, returnreturnDiabetesReferralReasonID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesReferralReason/" + str(DiabetesReferralReasonID), verb = "get", params_list = params_list)

	return(response)

def deleteDiabetesReferralReason(DiabetesReferralReasonID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesReferralReason/" + str(DiabetesReferralReasonID), verb = "delete")

	return(response)

def getEveryDiabetesReferralResult(EntityID = 1, page = 1, pageSize = 100, returnDiabetesReferralResultID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesReferralResult/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDiabetesReferralResult(DiabetesReferralResultID, EntityID = 1, returnreturnDiabetesReferralResultID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesReferralResult/" + str(DiabetesReferralResultID), verb = "get", params_list = params_list)

	return(response)

def deleteDiabetesReferralResult(DiabetesReferralResultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesReferralResult/" + str(DiabetesReferralResultID), verb = "delete")

	return(response)

def getEveryDiabetesTreatment(EntityID = 1, page = 1, pageSize = 100, returnDiabetesTreatmentID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesTreatment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDiabetesTreatment(DiabetesTreatmentID, EntityID = 1, returnreturnDiabetesTreatmentID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesTreatment/" + str(DiabetesTreatmentID), verb = "get", params_list = params_list)

	return(response)

def deleteDiabetesTreatment(DiabetesTreatmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesTreatment/" + str(DiabetesTreatmentID), verb = "delete")

	return(response)

def getEveryDoseInterval(EntityID = 1, page = 1, pageSize = 100, returnDoseIntervalID = True, returnAgeHighMonths = False, returnAgeLowMonths = False, returnComplianceScheduleDetailID = False, returnCreatedTime = False, returnDoseHigh = False, returnDoseIntervalIDClonedFrom = False, returnDoseLow = False, returnGracePeriodDays = False, returnIntervalType = False, returnIntervalTypeCode = False, returnIntervalValue = False, returnIsConditionalInterval = False, returnIsDistrictDefined = False, returnIsRequired = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccineDateHigh = False, returnVaccineDateLow = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DoseInterval/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDoseInterval(DoseIntervalID, EntityID = 1, returnreturnDoseIntervalID = False, returnreturnAgeHighMonths = False, returnreturnAgeLowMonths = False, returnreturnComplianceScheduleDetailID = False, returnreturnCreatedTime = False, returnreturnDoseHigh = False, returnreturnDoseIntervalIDClonedFrom = False, returnreturnDoseLow = False, returnreturnGracePeriodDays = False, returnreturnIntervalType = False, returnreturnIntervalTypeCode = False, returnreturnIntervalValue = False, returnreturnIsConditionalInterval = False, returnreturnIsDistrictDefined = False, returnreturnIsRequired = False, returnreturnModifiedTime = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVaccineDateHigh = False, returnreturnVaccineDateLow = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DoseInterval/" + str(DoseIntervalID), verb = "get", params_list = params_list)

	return(response)

def deleteDoseInterval(DoseIntervalID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DoseInterval/" + str(DoseIntervalID), verb = "delete")

	return(response)

def getEveryDoseMinimumAge(EntityID = 1, page = 1, pageSize = 100, returnDoseMinimumAgeID = True, returnAge = False, returnAgeUnitType = False, returnAgeUnitTypeCode = False, returnComplianceScheduleDetailID = False, returnCreatedTime = False, returnDoseMinimumAgeIDClonedFrom = False, returnDoseNumber = False, returnGracePeriodType = False, returnGracePeriodTypeCode = False, returnGraceValue = False, returnIsDistrictDefined = False, returnIsRequired = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccineDateHigh = False, returnVaccineDateLow = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DoseMinimumAge/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDoseMinimumAge(DoseMinimumAgeID, EntityID = 1, returnreturnDoseMinimumAgeID = False, returnreturnAge = False, returnreturnAgeUnitType = False, returnreturnAgeUnitTypeCode = False, returnreturnComplianceScheduleDetailID = False, returnreturnCreatedTime = False, returnreturnDoseMinimumAgeIDClonedFrom = False, returnreturnDoseNumber = False, returnreturnGracePeriodType = False, returnreturnGracePeriodTypeCode = False, returnreturnGraceValue = False, returnreturnIsDistrictDefined = False, returnreturnIsRequired = False, returnreturnModifiedTime = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVaccineDateHigh = False, returnreturnVaccineDateLow = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DoseMinimumAge/" + str(DoseMinimumAgeID), verb = "get", params_list = params_list)

	return(response)

def deleteDoseMinimumAge(DoseMinimumAgeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DoseMinimumAge/" + str(DoseMinimumAgeID), verb = "delete")

	return(response)

def getEveryHealthAttachment(EntityID = 1, page = 1, pageSize = 100, returnHealthAttachmentID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDescription = False, returnIsVoid = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthAttachment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHealthAttachment(HealthAttachmentID, EntityID = 1, returnreturnHealthAttachmentID = False, returnreturnAttachmentCount = False, returnreturnAttachmentIndicatorColumn = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnIsVoid = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserIDVoidedBy = False, returnreturnVoidedTime = False, returnreturnVoidNote = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthAttachment/" + str(HealthAttachmentID), verb = "get", params_list = params_list)

	return(response)

def deleteHealthAttachment(HealthAttachmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthAttachment/" + str(HealthAttachmentID), verb = "delete")

	return(response)

def getEveryHealthCondition(EntityID = 1, page = 1, pageSize = 100, returnHealthConditionID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnIsSecuredIndicator = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationGroupContraindication = False, returnVaccinationGroupContraindicationCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthCondition/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHealthCondition(HealthConditionID, EntityID = 1, returnreturnHealthConditionID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnIsSecuredIndicator = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVaccinationGroupContraindication = False, returnreturnVaccinationGroupContraindicationCode = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthCondition/" + str(HealthConditionID), verb = "get", params_list = params_list)

	return(response)

def deleteHealthCondition(HealthConditionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthCondition/" + str(HealthConditionID), verb = "delete")

	return(response)

def getEveryHealthConditionComment(EntityID = 1, page = 1, pageSize = 100, returnHealthConditionCommentID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthConditionComment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHealthConditionComment(HealthConditionCommentID, EntityID = 1, returnreturnHealthConditionCommentID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthConditionComment/" + str(HealthConditionCommentID), verb = "get", params_list = params_list)

	return(response)

def deleteHealthConditionComment(HealthConditionCommentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthConditionComment/" + str(HealthConditionCommentID), verb = "delete")

	return(response)

def getEveryHealthConditionTreatment(EntityID = 1, page = 1, pageSize = 100, returnHealthConditionTreatmentID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthConditionTreatment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHealthConditionTreatment(HealthConditionTreatmentID, EntityID = 1, returnreturnHealthConditionTreatmentID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthConditionTreatment/" + str(HealthConditionTreatmentID), verb = "get", params_list = params_list)

	return(response)

def deleteHealthConditionTreatment(HealthConditionTreatmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthConditionTreatment/" + str(HealthConditionTreatmentID), verb = "delete")

	return(response)

def getEveryHealthProfessional(EntityID = 1, page = 1, pageSize = 100, returnHealthProfessionalID = True, returnCreatedTime = False, returnDistrictGroupKey = False, returnDistrictID = False, returnHealthProfessionalTypeID = False, returnIsActive = False, returnIsDentist = False, returnIsPrimaryPhysician = False, returnModifiedTime = False, returnNameEmailIDDisplayEmail = False, returnNameID = False, returnNamePhoneIDDisplayPhone = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthProfessional/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHealthProfessional(HealthProfessionalID, EntityID = 1, returnreturnHealthProfessionalID = False, returnreturnCreatedTime = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnHealthProfessionalTypeID = False, returnreturnIsActive = False, returnreturnIsDentist = False, returnreturnIsPrimaryPhysician = False, returnreturnModifiedTime = False, returnreturnNameEmailIDDisplayEmail = False, returnreturnNameID = False, returnreturnNamePhoneIDDisplayPhone = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthProfessional/" + str(HealthProfessionalID), verb = "get", params_list = params_list)

	return(response)

def deleteHealthProfessional(HealthProfessionalID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthProfessional/" + str(HealthProfessionalID), verb = "delete")

	return(response)

def getEveryHealthProfessionalType(EntityID = 1, page = 1, pageSize = 100, returnHealthProfessionalTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthProfessionalType/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHealthProfessionalType(HealthProfessionalTypeID, EntityID = 1, returnreturnHealthProfessionalTypeID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthProfessionalType/" + str(HealthProfessionalTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteHealthProfessionalType(HealthProfessionalTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthProfessionalType/" + str(HealthProfessionalTypeID), verb = "delete")

	return(response)

def getEveryHearingComment(EntityID = 1, page = 1, pageSize = 100, returnHearingCommentID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingComment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHearingComment(HearingCommentID, EntityID = 1, returnreturnHearingCommentID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingComment/" + str(HearingCommentID), verb = "get", params_list = params_list)

	return(response)

def deleteHearingComment(HearingCommentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingComment/" + str(HearingCommentID), verb = "delete")

	return(response)

def getEveryHearingDecibelLevel(EntityID = 1, page = 1, pageSize = 100, returnHearingDecibelLevelID = True, returnCode = False, returnCreatedTime = False, returnDecibelLevel = False, returnDescription = False, returnDistrictID = False, returnHearingDecibelLevelDefaultID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingDecibelLevel/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHearingDecibelLevel(HearingDecibelLevelID, EntityID = 1, returnreturnHearingDecibelLevelID = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnDecibelLevel = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnHearingDecibelLevelDefaultID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingDecibelLevel/" + str(HearingDecibelLevelID), verb = "get", params_list = params_list)

	return(response)

def deleteHearingDecibelLevel(HearingDecibelLevelID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingDecibelLevel/" + str(HearingDecibelLevelID), verb = "delete")

	return(response)

def getEveryHearingDecibelLevelDefault(EntityID = 1, page = 1, pageSize = 100, returnHearingDecibelLevelDefaultID = True, returnCode = False, returnCreatedTime = False, returnDecibelLevel = False, returnDescription = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingDecibelLevelDefault/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHearingDecibelLevelDefault(HearingDecibelLevelDefaultID, EntityID = 1, returnreturnHearingDecibelLevelDefaultID = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnDecibelLevel = False, returnreturnDescription = False, returnreturnModifiedTime = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingDecibelLevelDefault/" + str(HearingDecibelLevelDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteHearingDecibelLevelDefault(HearingDecibelLevelDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingDecibelLevelDefault/" + str(HearingDecibelLevelDefaultID), verb = "delete")

	return(response)

def getEveryHearingGuardianNotification(EntityID = 1, page = 1, pageSize = 100, returnHearingGuardianNotificationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingGuardianNotification/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHearingGuardianNotification(HearingGuardianNotificationID, EntityID = 1, returnreturnHearingGuardianNotificationID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingGuardianNotification/" + str(HearingGuardianNotificationID), verb = "get", params_list = params_list)

	return(response)

def deleteHearingGuardianNotification(HearingGuardianNotificationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingGuardianNotification/" + str(HearingGuardianNotificationID), verb = "delete")

	return(response)

def getEveryHearingGuardianResponse(EntityID = 1, page = 1, pageSize = 100, returnHearingGuardianResponseID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHearingGuardianResponse(HearingGuardianResponseID, EntityID = 1, returnreturnHearingGuardianResponseID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingGuardianResponse/" + str(HearingGuardianResponseID), verb = "get", params_list = params_list)

	return(response)

def deleteHearingGuardianResponse(HearingGuardianResponseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingGuardianResponse/" + str(HearingGuardianResponseID), verb = "delete")

	return(response)

def getEveryHearingHertzLevel(EntityID = 1, page = 1, pageSize = 100, returnHearingHertzLevelID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnHearingHertzLevelDefaultID = False, returnHertzLevel = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingHertzLevel/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHearingHertzLevel(HearingHertzLevelID, EntityID = 1, returnreturnHearingHertzLevelID = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnHearingHertzLevelDefaultID = False, returnreturnHertzLevel = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingHertzLevel/" + str(HearingHertzLevelID), verb = "get", params_list = params_list)

	return(response)

def deleteHearingHertzLevel(HearingHertzLevelID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingHertzLevel/" + str(HearingHertzLevelID), verb = "delete")

	return(response)

def getEveryHearingHertzLevelDefault(EntityID = 1, page = 1, pageSize = 100, returnHearingHertzLevelDefaultID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnHertzLevel = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingHertzLevelDefault/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHearingHertzLevelDefault(HearingHertzLevelDefaultID, EntityID = 1, returnreturnHearingHertzLevelDefaultID = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnHertzLevel = False, returnreturnModifiedTime = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingHertzLevelDefault/" + str(HearingHertzLevelDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteHearingHertzLevelDefault(HearingHertzLevelDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingHertzLevelDefault/" + str(HearingHertzLevelDefaultID), verb = "delete")

	return(response)

def getEveryHearingObservation(EntityID = 1, page = 1, pageSize = 100, returnHearingObservationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingObservation/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHearingObservation(HearingObservationID, EntityID = 1, returnreturnHearingObservationID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingObservation/" + str(HearingObservationID), verb = "get", params_list = params_list)

	return(response)

def deleteHearingObservation(HearingObservationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingObservation/" + str(HearingObservationID), verb = "delete")

	return(response)

def getEveryHearingReferralReason(EntityID = 1, page = 1, pageSize = 100, returnHearingReferralReasonID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingReferralReason/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHearingReferralReason(HearingReferralReasonID, EntityID = 1, returnreturnHearingReferralReasonID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingReferralReason/" + str(HearingReferralReasonID), verb = "get", params_list = params_list)

	return(response)

def deleteHearingReferralReason(HearingReferralReasonID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingReferralReason/" + str(HearingReferralReasonID), verb = "delete")

	return(response)

def getEveryHearingReferralResult(EntityID = 1, page = 1, pageSize = 100, returnHearingReferralResultID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingReferralResult/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHearingReferralResult(HearingReferralResultID, EntityID = 1, returnreturnHearingReferralResultID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingReferralResult/" + str(HearingReferralResultID), verb = "get", params_list = params_list)

	return(response)

def deleteHearingReferralResult(HearingReferralResultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingReferralResult/" + str(HearingReferralResultID), verb = "delete")

	return(response)

def getEveryHearingScreening(EntityID = 1, page = 1, pageSize = 100, returnHearingScreeningID = True, returnCombinedResult = False, returnCombinedResultCode = False, returnCreatedTime = False, returnDistrictID = False, returnGroupPercentLossLeftEar = False, returnGroupPercentLossRightEar = False, returnHealthProfessionalIDExaminedBy = False, returnIndividualPercentLossLeftEar = False, returnIndividualPercentLossRightEar = False, returnIsKnownCase = False, returnIsVoid = False, returnModifiedTime = False, returnNameID = False, returnNameOfficeVisitID = False, returnObservationDescriptionsListDisplay = False, returnReScreen = False, returnResultLeftEar = False, returnResultLeftEarCode = False, returnResultMiddleEar = False, returnResultMiddleEarCode = False, returnResultRightEar = False, returnResultRightEarCode = False, returnSchoolYearID = False, returnScreeningDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreening/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHearingScreening(HearingScreeningID, EntityID = 1, returnreturnHearingScreeningID = False, returnreturnCombinedResult = False, returnreturnCombinedResultCode = False, returnreturnCreatedTime = False, returnreturnDistrictID = False, returnreturnGroupPercentLossLeftEar = False, returnreturnGroupPercentLossRightEar = False, returnreturnHealthProfessionalIDExaminedBy = False, returnreturnIndividualPercentLossLeftEar = False, returnreturnIndividualPercentLossRightEar = False, returnreturnIsKnownCase = False, returnreturnIsVoid = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnNameOfficeVisitID = False, returnreturnObservationDescriptionsListDisplay = False, returnreturnReScreen = False, returnreturnResultLeftEar = False, returnreturnResultLeftEarCode = False, returnreturnResultMiddleEar = False, returnreturnResultMiddleEarCode = False, returnreturnResultRightEar = False, returnreturnResultRightEarCode = False, returnreturnSchoolYearID = False, returnreturnScreeningDate = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserIDVoidedBy = False, returnreturnVoidedTime = False, returnreturnVoidNote = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreening/" + str(HearingScreeningID), verb = "get", params_list = params_list)

	return(response)

def deleteHearingScreening(HearingScreeningID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreening/" + str(HearingScreeningID), verb = "delete")

	return(response)

def getEveryHearingScreeningComment(EntityID = 1, page = 1, pageSize = 100, returnHearingScreeningCommentID = True, returnCreatedTime = False, returnHearingCommentID = False, returnHearingScreeningID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningComment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHearingScreeningComment(HearingScreeningCommentID, EntityID = 1, returnreturnHearingScreeningCommentID = False, returnreturnCreatedTime = False, returnreturnHearingCommentID = False, returnreturnHearingScreeningID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningComment/" + str(HearingScreeningCommentID), verb = "get", params_list = params_list)

	return(response)

def deleteHearingScreeningComment(HearingScreeningCommentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningComment/" + str(HearingScreeningCommentID), verb = "delete")

	return(response)

def getEveryHearingScreeningNote(EntityID = 1, page = 1, pageSize = 100, returnHearingScreeningNoteID = True, returnCreatedTime = False, returnHearingScreeningID = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHearingScreeningNote(HearingScreeningNoteID, EntityID = 1, returnreturnHearingScreeningNoteID = False, returnreturnCreatedTime = False, returnreturnHearingScreeningID = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningNote/" + str(HearingScreeningNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteHearingScreeningNote(HearingScreeningNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningNote/" + str(HearingScreeningNoteID), verb = "delete")

	return(response)

def getEveryHearingScreeningObservation(EntityID = 1, page = 1, pageSize = 100, returnHearingScreeningObservationID = True, returnCreatedTime = False, returnHearingObservationID = False, returnHearingScreeningID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningObservation/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHearingScreeningObservation(HearingScreeningObservationID, EntityID = 1, returnreturnHearingScreeningObservationID = False, returnreturnCreatedTime = False, returnreturnHearingObservationID = False, returnreturnHearingScreeningID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningObservation/" + str(HearingScreeningObservationID), verb = "get", params_list = params_list)

	return(response)

def deleteHearingScreeningObservation(HearingScreeningObservationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningObservation/" + str(HearingScreeningObservationID), verb = "delete")

	return(response)

def getEveryHearingScreeningReferral(EntityID = 1, page = 1, pageSize = 100, returnHearingScreeningReferralID = True, returnCompletionDate = False, returnCreatedTime = False, returnHealthProfessionalIDReferredBy = False, returnHealthProfessionalIDReferredTo = False, returnHearingGuardianNotificationID = False, returnHearingGuardianResponseID = False, returnHearingReferralReasonID = False, returnHearingReferralResultID = False, returnHearingScreeningID = False, returnModifiedTime = False, returnReferralCompleted = False, returnReferralDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningReferral/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHearingScreeningReferral(HearingScreeningReferralID, EntityID = 1, returnreturnHearingScreeningReferralID = False, returnreturnCompletionDate = False, returnreturnCreatedTime = False, returnreturnHealthProfessionalIDReferredBy = False, returnreturnHealthProfessionalIDReferredTo = False, returnreturnHearingGuardianNotificationID = False, returnreturnHearingGuardianResponseID = False, returnreturnHearingReferralReasonID = False, returnreturnHearingReferralResultID = False, returnreturnHearingScreeningID = False, returnreturnModifiedTime = False, returnreturnReferralCompleted = False, returnreturnReferralDate = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningReferral/" + str(HearingScreeningReferralID), verb = "get", params_list = params_list)

	return(response)

def deleteHearingScreeningReferral(HearingScreeningReferralID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningReferral/" + str(HearingScreeningReferralID), verb = "delete")

	return(response)

def getEveryHearingScreeningSecuredNote(EntityID = 1, page = 1, pageSize = 100, returnHearingScreeningSecuredNoteID = True, returnCreatedTime = False, returnHearingScreeningID = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningSecuredNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHearingScreeningSecuredNote(HearingScreeningSecuredNoteID, EntityID = 1, returnreturnHearingScreeningSecuredNoteID = False, returnreturnCreatedTime = False, returnreturnHearingScreeningID = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningSecuredNote/" + str(HearingScreeningSecuredNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteHearingScreeningSecuredNote(HearingScreeningSecuredNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningSecuredNote/" + str(HearingScreeningSecuredNoteID), verb = "delete")

	return(response)

def getEveryHearingScreeningThreshold(EntityID = 1, page = 1, pageSize = 100, returnHearingScreeningThresholdID = True, returnCreatedTime = False, returnHearingDecibelLevelIDLeftEar = False, returnHearingDecibelLevelIDRightEar = False, returnHearingHertzLevelID = False, returnHearingScreeningID = False, returnLeftEarPassed = False, returnModifiedTime = False, returnRightEarPassed = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningThreshold/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHearingScreeningThreshold(HearingScreeningThresholdID, EntityID = 1, returnreturnHearingScreeningThresholdID = False, returnreturnCreatedTime = False, returnreturnHearingDecibelLevelIDLeftEar = False, returnreturnHearingDecibelLevelIDRightEar = False, returnreturnHearingHertzLevelID = False, returnreturnHearingScreeningID = False, returnreturnLeftEarPassed = False, returnreturnModifiedTime = False, returnreturnRightEarPassed = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningThreshold/" + str(HearingScreeningThresholdID), verb = "get", params_list = params_list)

	return(response)

def deleteHearingScreeningThreshold(HearingScreeningThresholdID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningThreshold/" + str(HearingScreeningThresholdID), verb = "delete")

	return(response)

def getEveryInjury(EntityID = 1, page = 1, pageSize = 100, returnInjuryID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Injury/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getInjury(InjuryID, EntityID = 1, returnreturnInjuryID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Injury/" + str(InjuryID), verb = "get", params_list = params_list)

	return(response)

def deleteInjury(InjuryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Injury/" + str(InjuryID), verb = "delete")

	return(response)

def getEveryInjuryOccurrence(EntityID = 1, page = 1, pageSize = 100, returnInjuryOccurrenceID = True, returnBodyParts = False, returnCreatedTime = False, returnDaysMissed = False, returnDistrictID = False, returnHealthProfessionalID = False, returnInjuryDateTime = False, returnInjuryDateTimeDate = False, returnInjuryDateTimeTime = False, returnIsImmediateCareRequired = False, returnIsVoid = False, returnLocationID = False, returnModifiedTime = False, returnNameID = False, returnNameIDReportedBy = False, returnNameIDRespondedBy = False, returnReportFileDate = False, returnSchoolID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrence/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getInjuryOccurrence(InjuryOccurrenceID, EntityID = 1, returnreturnInjuryOccurrenceID = False, returnreturnBodyParts = False, returnreturnCreatedTime = False, returnreturnDaysMissed = False, returnreturnDistrictID = False, returnreturnHealthProfessionalID = False, returnreturnInjuryDateTime = False, returnreturnInjuryDateTimeDate = False, returnreturnInjuryDateTimeTime = False, returnreturnIsImmediateCareRequired = False, returnreturnIsVoid = False, returnreturnLocationID = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnNameIDReportedBy = False, returnreturnNameIDRespondedBy = False, returnreturnReportFileDate = False, returnreturnSchoolID = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserIDVoidedBy = False, returnreturnVoidedTime = False, returnreturnVoidNote = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrence/" + str(InjuryOccurrenceID), verb = "get", params_list = params_list)

	return(response)

def deleteInjuryOccurrence(InjuryOccurrenceID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrence/" + str(InjuryOccurrenceID), verb = "delete")

	return(response)

def getEveryInjuryOccurrenceBodyPart(EntityID = 1, page = 1, pageSize = 100, returnInjuryOccurrenceBodyPartID = True, returnBodyPartID = False, returnCreatedTime = False, returnInjuryOccurrenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceBodyPart/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getInjuryOccurrenceBodyPart(InjuryOccurrenceBodyPartID, EntityID = 1, returnreturnInjuryOccurrenceBodyPartID = False, returnreturnBodyPartID = False, returnreturnCreatedTime = False, returnreturnInjuryOccurrenceID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceBodyPart/" + str(InjuryOccurrenceBodyPartID), verb = "get", params_list = params_list)

	return(response)

def deleteInjuryOccurrenceBodyPart(InjuryOccurrenceBodyPartID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceBodyPart/" + str(InjuryOccurrenceBodyPartID), verb = "delete")

	return(response)

def getEveryInjuryOccurrenceBodyPartInjury(EntityID = 1, page = 1, pageSize = 100, returnInjuryOccurrenceBodyPartInjuryID = True, returnCreatedTime = False, returnInjuryID = False, returnInjuryOccurrenceBodyPartID = False, returnModifiedTime = False, returnTreatments = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceBodyPartInjury/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getInjuryOccurrenceBodyPartInjury(InjuryOccurrenceBodyPartInjuryID, EntityID = 1, returnreturnInjuryOccurrenceBodyPartInjuryID = False, returnreturnCreatedTime = False, returnreturnInjuryID = False, returnreturnInjuryOccurrenceBodyPartID = False, returnreturnModifiedTime = False, returnreturnTreatments = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceBodyPartInjury/" + str(InjuryOccurrenceBodyPartInjuryID), verb = "get", params_list = params_list)

	return(response)

def deleteInjuryOccurrenceBodyPartInjury(InjuryOccurrenceBodyPartInjuryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceBodyPartInjury/" + str(InjuryOccurrenceBodyPartInjuryID), verb = "delete")

	return(response)

def getEveryInjuryOccurrenceBodyPartInjuryTreatment(EntityID = 1, page = 1, pageSize = 100, returnInjuryOccurrenceBodyPartInjuryTreatmentID = True, returnCreatedTime = False, returnInjuryOccurrenceBodyPartInjuryID = False, returnModifiedTime = False, returnOfficeVisitTreatmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceBodyPartInjuryTreatment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getInjuryOccurrenceBodyPartInjuryTreatment(InjuryOccurrenceBodyPartInjuryTreatmentID, EntityID = 1, returnreturnInjuryOccurrenceBodyPartInjuryTreatmentID = False, returnreturnCreatedTime = False, returnreturnInjuryOccurrenceBodyPartInjuryID = False, returnreturnModifiedTime = False, returnreturnOfficeVisitTreatmentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceBodyPartInjuryTreatment/" + str(InjuryOccurrenceBodyPartInjuryTreatmentID), verb = "get", params_list = params_list)

	return(response)

def deleteInjuryOccurrenceBodyPartInjuryTreatment(InjuryOccurrenceBodyPartInjuryTreatmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceBodyPartInjuryTreatment/" + str(InjuryOccurrenceBodyPartInjuryTreatmentID), verb = "delete")

	return(response)

def getEveryInjuryOccurrenceComment(EntityID = 1, page = 1, pageSize = 100, returnInjuryOccurrenceCommentID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceComment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getInjuryOccurrenceComment(InjuryOccurrenceCommentID, EntityID = 1, returnreturnInjuryOccurrenceCommentID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceComment/" + str(InjuryOccurrenceCommentID), verb = "get", params_list = params_list)

	return(response)

def deleteInjuryOccurrenceComment(InjuryOccurrenceCommentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceComment/" + str(InjuryOccurrenceCommentID), verb = "delete")

	return(response)

def getEveryInjuryOccurrenceGuardianNotification(EntityID = 1, page = 1, pageSize = 100, returnInjuryOccurrenceGuardianNotificationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceGuardianNotification/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getInjuryOccurrenceGuardianNotification(InjuryOccurrenceGuardianNotificationID, EntityID = 1, returnreturnInjuryOccurrenceGuardianNotificationID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceGuardianNotification/" + str(InjuryOccurrenceGuardianNotificationID), verb = "get", params_list = params_list)

	return(response)

def deleteInjuryOccurrenceGuardianNotification(InjuryOccurrenceGuardianNotificationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceGuardianNotification/" + str(InjuryOccurrenceGuardianNotificationID), verb = "delete")

	return(response)

def getEveryInjuryOccurrenceGuardianResponse(EntityID = 1, page = 1, pageSize = 100, returnInjuryOccurrenceGuardianResponseID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getInjuryOccurrenceGuardianResponse(InjuryOccurrenceGuardianResponseID, EntityID = 1, returnreturnInjuryOccurrenceGuardianResponseID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceGuardianResponse/" + str(InjuryOccurrenceGuardianResponseID), verb = "get", params_list = params_list)

	return(response)

def deleteInjuryOccurrenceGuardianResponse(InjuryOccurrenceGuardianResponseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceGuardianResponse/" + str(InjuryOccurrenceGuardianResponseID), verb = "delete")

	return(response)

def getEveryInjuryOccurrenceInjuryOccurrenceComment(EntityID = 1, page = 1, pageSize = 100, returnInjuryOccurrenceInjuryOccurrenceCommentID = True, returnCreatedTime = False, returnInjuryOccurrenceCommentID = False, returnInjuryOccurrenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceInjuryOccurrenceComment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getInjuryOccurrenceInjuryOccurrenceComment(InjuryOccurrenceInjuryOccurrenceCommentID, EntityID = 1, returnreturnInjuryOccurrenceInjuryOccurrenceCommentID = False, returnreturnCreatedTime = False, returnreturnInjuryOccurrenceCommentID = False, returnreturnInjuryOccurrenceID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceInjuryOccurrenceComment/" + str(InjuryOccurrenceInjuryOccurrenceCommentID), verb = "get", params_list = params_list)

	return(response)

def deleteInjuryOccurrenceInjuryOccurrenceComment(InjuryOccurrenceInjuryOccurrenceCommentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceInjuryOccurrenceComment/" + str(InjuryOccurrenceInjuryOccurrenceCommentID), verb = "delete")

	return(response)

def getEveryInjuryOccurrenceNote(EntityID = 1, page = 1, pageSize = 100, returnInjuryOccurrenceNoteID = True, returnCreatedTime = False, returnInjuryOccurrenceID = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getInjuryOccurrenceNote(InjuryOccurrenceNoteID, EntityID = 1, returnreturnInjuryOccurrenceNoteID = False, returnreturnCreatedTime = False, returnreturnInjuryOccurrenceID = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceNote/" + str(InjuryOccurrenceNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteInjuryOccurrenceNote(InjuryOccurrenceNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceNote/" + str(InjuryOccurrenceNoteID), verb = "delete")

	return(response)

def getEveryInjuryOccurrenceReferral(EntityID = 1, page = 1, pageSize = 100, returnInjuryOccurrenceReferralID = True, returnCompletionDate = False, returnCreatedTime = False, returnHealthProfessionalIDReferredBy = False, returnHealthProfessionalIDReferredTo = False, returnInjuryOccurrenceGuardianNotificationID = False, returnInjuryOccurrenceGuardianResponseID = False, returnInjuryOccurrenceID = False, returnInjuryOccurrenceReferralReasonID = False, returnInjuryOccurrenceReferralResultID = False, returnModifiedTime = False, returnReferralCompleted = False, returnReferralDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceReferral/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getInjuryOccurrenceReferral(InjuryOccurrenceReferralID, EntityID = 1, returnreturnInjuryOccurrenceReferralID = False, returnreturnCompletionDate = False, returnreturnCreatedTime = False, returnreturnHealthProfessionalIDReferredBy = False, returnreturnHealthProfessionalIDReferredTo = False, returnreturnInjuryOccurrenceGuardianNotificationID = False, returnreturnInjuryOccurrenceGuardianResponseID = False, returnreturnInjuryOccurrenceID = False, returnreturnInjuryOccurrenceReferralReasonID = False, returnreturnInjuryOccurrenceReferralResultID = False, returnreturnModifiedTime = False, returnreturnReferralCompleted = False, returnreturnReferralDate = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceReferral/" + str(InjuryOccurrenceReferralID), verb = "get", params_list = params_list)

	return(response)

def deleteInjuryOccurrenceReferral(InjuryOccurrenceReferralID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceReferral/" + str(InjuryOccurrenceReferralID), verb = "delete")

	return(response)

def getEveryInjuryOccurrenceReferralReason(EntityID = 1, page = 1, pageSize = 100, returnInjuryOccurrenceReferralReasonID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceReferralReason/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getInjuryOccurrenceReferralReason(InjuryOccurrenceReferralReasonID, EntityID = 1, returnreturnInjuryOccurrenceReferralReasonID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceReferralReason/" + str(InjuryOccurrenceReferralReasonID), verb = "get", params_list = params_list)

	return(response)

def deleteInjuryOccurrenceReferralReason(InjuryOccurrenceReferralReasonID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceReferralReason/" + str(InjuryOccurrenceReferralReasonID), verb = "delete")

	return(response)

def getEveryInjuryOccurrenceReferralResult(EntityID = 1, page = 1, pageSize = 100, returnInjuryOccurrenceReferralResultID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceReferralResult/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getInjuryOccurrenceReferralResult(InjuryOccurrenceReferralResultID, EntityID = 1, returnreturnInjuryOccurrenceReferralResultID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceReferralResult/" + str(InjuryOccurrenceReferralResultID), verb = "get", params_list = params_list)

	return(response)

def deleteInjuryOccurrenceReferralResult(InjuryOccurrenceReferralResultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceReferralResult/" + str(InjuryOccurrenceReferralResultID), verb = "delete")

	return(response)

def getEveryInjuryOccurrenceSecuredNote(EntityID = 1, page = 1, pageSize = 100, returnInjuryOccurrenceSecuredNoteID = True, returnCreatedTime = False, returnInjuryOccurrenceID = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceSecuredNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getInjuryOccurrenceSecuredNote(InjuryOccurrenceSecuredNoteID, EntityID = 1, returnreturnInjuryOccurrenceSecuredNoteID = False, returnreturnCreatedTime = False, returnreturnInjuryOccurrenceID = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceSecuredNote/" + str(InjuryOccurrenceSecuredNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteInjuryOccurrenceSecuredNote(InjuryOccurrenceSecuredNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceSecuredNote/" + str(InjuryOccurrenceSecuredNoteID), verb = "delete")

	return(response)

def getEveryLocation(EntityID = 1, page = 1, pageSize = 100, returnLocationID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Location/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getLocation(LocationID, EntityID = 1, returnreturnLocationID = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Location/" + str(LocationID), verb = "get", params_list = params_list)

	return(response)

def deleteLocation(LocationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Location/" + str(LocationID), verb = "delete")

	return(response)

def getEveryMedication(EntityID = 1, page = 1, pageSize = 100, returnMedicationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Medication/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getMedication(MedicationID, EntityID = 1, returnreturnMedicationID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Medication/" + str(MedicationID), verb = "get", params_list = params_list)

	return(response)

def deleteMedication(MedicationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Medication/" + str(MedicationID), verb = "delete")

	return(response)

def getEveryMedicationClassification(EntityID = 1, page = 1, pageSize = 100, returnMedicationClassificationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationClassification/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getMedicationClassification(MedicationClassificationID, EntityID = 1, returnreturnMedicationClassificationID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationClassification/" + str(MedicationClassificationID), verb = "get", params_list = params_list)

	return(response)

def deleteMedicationClassification(MedicationClassificationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationClassification/" + str(MedicationClassificationID), verb = "delete")

	return(response)

def getEveryMedicationClassificationMedication(EntityID = 1, page = 1, pageSize = 100, returnMedicationClassificationMedicationID = True, returnCreatedTime = False, returnMedicationClassificationID = False, returnMedicationID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationClassificationMedication/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getMedicationClassificationMedication(MedicationClassificationMedicationID, EntityID = 1, returnreturnMedicationClassificationMedicationID = False, returnreturnCreatedTime = False, returnreturnMedicationClassificationID = False, returnreturnMedicationID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationClassificationMedication/" + str(MedicationClassificationMedicationID), verb = "get", params_list = params_list)

	return(response)

def deleteMedicationClassificationMedication(MedicationClassificationMedicationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationClassificationMedication/" + str(MedicationClassificationMedicationID), verb = "delete")

	return(response)

def getEveryMedicationComment(EntityID = 1, page = 1, pageSize = 100, returnMedicationCommentID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationComment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getMedicationComment(MedicationCommentID, EntityID = 1, returnreturnMedicationCommentID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationComment/" + str(MedicationCommentID), verb = "get", params_list = params_list)

	return(response)

def deleteMedicationComment(MedicationCommentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationComment/" + str(MedicationCommentID), verb = "delete")

	return(response)

def getEveryMedicationDosageUnit(EntityID = 1, page = 1, pageSize = 100, returnMedicationDosageUnitID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnIsActive = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationDosageUnit/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getMedicationDosageUnit(MedicationDosageUnitID, EntityID = 1, returnreturnMedicationDosageUnitID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationDosageUnit/" + str(MedicationDosageUnitID), verb = "get", params_list = params_list)

	return(response)

def deleteMedicationDosageUnit(MedicationDosageUnitID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationDosageUnit/" + str(MedicationDosageUnitID), verb = "delete")

	return(response)

def getEveryMedicationRoute(EntityID = 1, page = 1, pageSize = 100, returnMedicationRouteID = True, returnCreatedTime = False, returnDescription = False, returnFDACode = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnNCIConceptCode = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationRoute/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getMedicationRoute(MedicationRouteID, EntityID = 1, returnreturnMedicationRouteID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnFDACode = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnNCIConceptCode = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationRoute/" + str(MedicationRouteID), verb = "get", params_list = params_list)

	return(response)

def deleteMedicationRoute(MedicationRouteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationRoute/" + str(MedicationRouteID), verb = "delete")

	return(response)

def getEveryNameMedication(EntityID = 1, page = 1, pageSize = 100, returnNameMedicationID = True, returnAdministrationInstruction = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDistributionType = False, returnDistributionTypeCode = False, returnEndDate = False, returnEndStatus = False, returnEndStatusCode = False, returnHealthProfessionalIDPrescribedBy = False, returnIsVoid = False, returnMaxDosesPerDay = False, returnMedicationDosageUnitID = False, returnMedicationID = False, returnMedicationRouteID = False, returnModifiedTime = False, returnNameID = False, returnOriginalEndDate = False, returnReceivedDoctorForm = False, returnReceivedParentReleaseForm = False, returnReceivedVerbalParentPermission = False, returnStartDate = False, returnUnitsPerDoseHigh = False, returnUnitsPerDoseLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedication/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameMedication(NameMedicationID, EntityID = 1, returnreturnNameMedicationID = False, returnreturnAdministrationInstruction = False, returnreturnAttachmentCount = False, returnreturnAttachmentIndicatorColumn = False, returnreturnCreatedTime = False, returnreturnDistributionType = False, returnreturnDistributionTypeCode = False, returnreturnEndDate = False, returnreturnEndStatus = False, returnreturnEndStatusCode = False, returnreturnHealthProfessionalIDPrescribedBy = False, returnreturnIsVoid = False, returnreturnMaxDosesPerDay = False, returnreturnMedicationDosageUnitID = False, returnreturnMedicationID = False, returnreturnMedicationRouteID = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnOriginalEndDate = False, returnreturnReceivedDoctorForm = False, returnreturnReceivedParentReleaseForm = False, returnreturnReceivedVerbalParentPermission = False, returnreturnStartDate = False, returnreturnUnitsPerDoseHigh = False, returnreturnUnitsPerDoseLow = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserIDVoidedBy = False, returnreturnVoidedTime = False, returnreturnVoidNote = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedication/" + str(NameMedicationID), verb = "get", params_list = params_list)

	return(response)

def deleteNameMedication(NameMedicationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedication/" + str(NameMedicationID), verb = "delete")

	return(response)

def getEveryNameMedicationComment(EntityID = 1, page = 1, pageSize = 100, returnNameMedicationCommentID = True, returnCreatedTime = False, returnMedicationCommentID = False, returnModifiedTime = False, returnNameMedicationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationComment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameMedicationComment(NameMedicationCommentID, EntityID = 1, returnreturnNameMedicationCommentID = False, returnreturnCreatedTime = False, returnreturnMedicationCommentID = False, returnreturnModifiedTime = False, returnreturnNameMedicationID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationComment/" + str(NameMedicationCommentID), verb = "get", params_list = params_list)

	return(response)

def deleteNameMedicationComment(NameMedicationCommentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationComment/" + str(NameMedicationCommentID), verb = "delete")

	return(response)

def getEveryNameMedicationNote(EntityID = 1, page = 1, pageSize = 100, returnNameMedicationNoteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameMedicationID = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameMedicationNote(NameMedicationNoteID, EntityID = 1, returnreturnNameMedicationNoteID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNameMedicationID = False, returnreturnNote = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationNote/" + str(NameMedicationNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteNameMedicationNote(NameMedicationNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationNote/" + str(NameMedicationNoteID), verb = "delete")

	return(response)

def getEveryNameMedicationPrescription(EntityID = 1, page = 1, pageSize = 100, returnNameMedicationPrescriptionID = True, returnCreatedTime = False, returnExpirationDate = False, returnIsVoid = False, returnModifiedTime = False, returnNameIDPharmacy = False, returnNameMedicationID = False, returnPrescriptionNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationPrescription/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameMedicationPrescription(NameMedicationPrescriptionID, EntityID = 1, returnreturnNameMedicationPrescriptionID = False, returnreturnCreatedTime = False, returnreturnExpirationDate = False, returnreturnIsVoid = False, returnreturnModifiedTime = False, returnreturnNameIDPharmacy = False, returnreturnNameMedicationID = False, returnreturnPrescriptionNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserIDVoidedBy = False, returnreturnVoidedTime = False, returnreturnVoidNote = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationPrescription/" + str(NameMedicationPrescriptionID), verb = "get", params_list = params_list)

	return(response)

def deleteNameMedicationPrescription(NameMedicationPrescriptionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationPrescription/" + str(NameMedicationPrescriptionID), verb = "delete")

	return(response)

def getEveryNameMedicationSchedule(EntityID = 1, page = 1, pageSize = 100, returnNameMedicationScheduleID = True, returnCreatedTime = False, returnEndDate = False, returnFriday = False, returnIsAdministrableAsOfSpecifiedDate = False, returnIsAdministrableAsOfToday = False, returnIsVoid = False, returnModifiedTime = False, returnMonday = False, returnNameMedicationID = False, returnSaturday = False, returnScheduledAdministrationTime = False, returnScheduledAdministrationTimeTime = False, returnStartDate = False, returnSunday = False, returnThursday = False, returnTuesday = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, returnWednesday = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationSchedule/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameMedicationSchedule(NameMedicationScheduleID, EntityID = 1, returnreturnNameMedicationScheduleID = False, returnreturnCreatedTime = False, returnreturnEndDate = False, returnreturnFriday = False, returnreturnIsAdministrableAsOfSpecifiedDate = False, returnreturnIsAdministrableAsOfToday = False, returnreturnIsVoid = False, returnreturnModifiedTime = False, returnreturnMonday = False, returnreturnNameMedicationID = False, returnreturnSaturday = False, returnreturnScheduledAdministrationTime = False, returnreturnScheduledAdministrationTimeTime = False, returnreturnStartDate = False, returnreturnSunday = False, returnreturnThursday = False, returnreturnTuesday = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserIDVoidedBy = False, returnreturnVoidedTime = False, returnreturnVoidNote = False, returnreturnWednesday = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationSchedule/" + str(NameMedicationScheduleID), verb = "get", params_list = params_list)

	return(response)

def deleteNameMedicationSchedule(NameMedicationScheduleID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationSchedule/" + str(NameMedicationScheduleID), verb = "delete")

	return(response)

def getEveryNameMedicationSecuredNote(EntityID = 1, page = 1, pageSize = 100, returnNameMedicationSecuredNoteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameMedicationID = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationSecuredNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameMedicationSecuredNote(NameMedicationSecuredNoteID, EntityID = 1, returnreturnNameMedicationSecuredNoteID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNameMedicationID = False, returnreturnNote = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationSecuredNote/" + str(NameMedicationSecuredNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteNameMedicationSecuredNote(NameMedicationSecuredNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationSecuredNote/" + str(NameMedicationSecuredNoteID), verb = "delete")

	return(response)

def getEveryNameOfficeVisit(EntityID = 1, page = 1, pageSize = 100, returnNameOfficeVisitID = True, returnCreatedTime = False, returnDisplayStatus = False, returnDocumentationIsComplete = False, returnEntityID = False, returnHasBeenReleased = False, returnHealthProfessionalIDExaminedBy = False, returnIsNameOfficeVisitToday = False, returnIsVoid = False, returnModifiedTime = False, returnNameID = False, returnNameOfficeVisitDispositionsListDisplay = False, returnNameOfficeVisitReasonsListDisplay = False, returnNameOfficeVisitTreatmentsListDisplay = False, returnOfficeVisitCommentID = False, returnSchoolID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisit/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameOfficeVisit(NameOfficeVisitID, EntityID = 1, returnreturnNameOfficeVisitID = False, returnreturnCreatedTime = False, returnreturnDisplayStatus = False, returnreturnDocumentationIsComplete = False, returnreturnEntityID = False, returnreturnHasBeenReleased = False, returnreturnHealthProfessionalIDExaminedBy = False, returnreturnIsNameOfficeVisitToday = False, returnreturnIsVoid = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnNameOfficeVisitDispositionsListDisplay = False, returnreturnNameOfficeVisitReasonsListDisplay = False, returnreturnNameOfficeVisitTreatmentsListDisplay = False, returnreturnOfficeVisitCommentID = False, returnreturnSchoolID = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserIDVoidedBy = False, returnreturnVoidedTime = False, returnreturnVoidNote = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisit/" + str(NameOfficeVisitID), verb = "get", params_list = params_list)

	return(response)

def deleteNameOfficeVisit(NameOfficeVisitID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisit/" + str(NameOfficeVisitID), verb = "delete")

	return(response)

def getEveryNameOfficeVisitDisposition(EntityID = 1, page = 1, pageSize = 100, returnNameOfficeVisitDispositionID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameOfficeVisitID = False, returnOfficeVisitDispositionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitDisposition/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameOfficeVisitDisposition(NameOfficeVisitDispositionID, EntityID = 1, returnreturnNameOfficeVisitDispositionID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNameOfficeVisitID = False, returnreturnOfficeVisitDispositionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitDisposition/" + str(NameOfficeVisitDispositionID), verb = "get", params_list = params_list)

	return(response)

def deleteNameOfficeVisitDisposition(NameOfficeVisitDispositionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitDisposition/" + str(NameOfficeVisitDispositionID), verb = "delete")

	return(response)

def getEveryNameOfficeVisitNote(EntityID = 1, page = 1, pageSize = 100, returnNameOfficeVisitNoteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameOfficeVisitID = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameOfficeVisitNote(NameOfficeVisitNoteID, EntityID = 1, returnreturnNameOfficeVisitNoteID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNameOfficeVisitID = False, returnreturnNote = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitNote/" + str(NameOfficeVisitNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteNameOfficeVisitNote(NameOfficeVisitNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitNote/" + str(NameOfficeVisitNoteID), verb = "delete")

	return(response)

def getEveryNameOfficeVisitNotification(EntityID = 1, page = 1, pageSize = 100, returnNameOfficeVisitNotificationID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNameOfficeVisitID = False, returnNote = False, returnNotificationMethodID = False, returnNotificationTime = False, returnNotificationTimeDate = False, returnNotificationTimeTime = False, returnOfficeVisitGuardianResponseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitNotification/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameOfficeVisitNotification(NameOfficeVisitNotificationID, EntityID = 1, returnreturnNameOfficeVisitNotificationID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnNameOfficeVisitID = False, returnreturnNote = False, returnreturnNotificationMethodID = False, returnreturnNotificationTime = False, returnreturnNotificationTimeDate = False, returnreturnNotificationTimeTime = False, returnreturnOfficeVisitGuardianResponseID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitNotification/" + str(NameOfficeVisitNotificationID), verb = "get", params_list = params_list)

	return(response)

def deleteNameOfficeVisitNotification(NameOfficeVisitNotificationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitNotification/" + str(NameOfficeVisitNotificationID), verb = "delete")

	return(response)

def getEveryNameOfficeVisitReason(EntityID = 1, page = 1, pageSize = 100, returnNameOfficeVisitReasonID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameOfficeVisitID = False, returnOfficeVisitReasonID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitReason/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameOfficeVisitReason(NameOfficeVisitReasonID, EntityID = 1, returnreturnNameOfficeVisitReasonID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNameOfficeVisitID = False, returnreturnOfficeVisitReasonID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitReason/" + str(NameOfficeVisitReasonID), verb = "get", params_list = params_list)

	return(response)

def deleteNameOfficeVisitReason(NameOfficeVisitReasonID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitReason/" + str(NameOfficeVisitReasonID), verb = "delete")

	return(response)

def getEveryNameOfficeVisitReferral(EntityID = 1, page = 1, pageSize = 100, returnNameOfficeVisitReferralID = True, returnCompletionDate = False, returnCreatedTime = False, returnHealthProfessionalIDReferredBy = False, returnHealthProfessionalIDReferredTo = False, returnModifiedTime = False, returnNameOfficeVisitID = False, returnOfficeVisitGuardianResponseID = False, returnOfficeVisitReferralReasonID = False, returnOfficeVisitReferralResultID = False, returnReferralCompleted = False, returnReferralDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitReferral/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameOfficeVisitReferral(NameOfficeVisitReferralID, EntityID = 1, returnreturnNameOfficeVisitReferralID = False, returnreturnCompletionDate = False, returnreturnCreatedTime = False, returnreturnHealthProfessionalIDReferredBy = False, returnreturnHealthProfessionalIDReferredTo = False, returnreturnModifiedTime = False, returnreturnNameOfficeVisitID = False, returnreturnOfficeVisitGuardianResponseID = False, returnreturnOfficeVisitReferralReasonID = False, returnreturnOfficeVisitReferralResultID = False, returnreturnReferralCompleted = False, returnreturnReferralDate = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitReferral/" + str(NameOfficeVisitReferralID), verb = "get", params_list = params_list)

	return(response)

def deleteNameOfficeVisitReferral(NameOfficeVisitReferralID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitReferral/" + str(NameOfficeVisitReferralID), verb = "delete")

	return(response)

def getEveryNameOfficeVisitSecuredNote(EntityID = 1, page = 1, pageSize = 100, returnNameOfficeVisitSecuredNoteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameOfficeVisitID = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitSecuredNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameOfficeVisitSecuredNote(NameOfficeVisitSecuredNoteID, EntityID = 1, returnreturnNameOfficeVisitSecuredNoteID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNameOfficeVisitID = False, returnreturnNote = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitSecuredNote/" + str(NameOfficeVisitSecuredNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteNameOfficeVisitSecuredNote(NameOfficeVisitSecuredNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitSecuredNote/" + str(NameOfficeVisitSecuredNoteID), verb = "delete")

	return(response)

def getEveryNameOfficeVisitTimeTransaction(EntityID = 1, page = 1, pageSize = 100, returnNameOfficeVisitTimeTransactionID = True, returnCreatedTime = False, returnDisplayDuration = False, returnDisplayOrder = False, returnDuration = False, returnEndTime = False, returnEndTimeDate = False, returnEndTimeTime = False, returnModifiedTime = False, returnNameOfficeVisitID = False, returnNote = False, returnStartTime = False, returnStartTimeDate = False, returnStartTimeTime = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitTimeTransaction/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameOfficeVisitTimeTransaction(NameOfficeVisitTimeTransactionID, EntityID = 1, returnreturnNameOfficeVisitTimeTransactionID = False, returnreturnCreatedTime = False, returnreturnDisplayDuration = False, returnreturnDisplayOrder = False, returnreturnDuration = False, returnreturnEndTime = False, returnreturnEndTimeDate = False, returnreturnEndTimeTime = False, returnreturnModifiedTime = False, returnreturnNameOfficeVisitID = False, returnreturnNote = False, returnreturnStartTime = False, returnreturnStartTimeDate = False, returnreturnStartTimeTime = False, returnreturnStatus = False, returnreturnStatusCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitTimeTransaction/" + str(NameOfficeVisitTimeTransactionID), verb = "get", params_list = params_list)

	return(response)

def deleteNameOfficeVisitTimeTransaction(NameOfficeVisitTimeTransactionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitTimeTransaction/" + str(NameOfficeVisitTimeTransactionID), verb = "delete")

	return(response)

def getEveryNameOfficeVisitTreatment(EntityID = 1, page = 1, pageSize = 100, returnNameOfficeVisitTreatmentID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameOfficeVisitID = False, returnOfficeVisitTreatmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitTreatment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameOfficeVisitTreatment(NameOfficeVisitTreatmentID, EntityID = 1, returnreturnNameOfficeVisitTreatmentID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNameOfficeVisitID = False, returnreturnOfficeVisitTreatmentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitTreatment/" + str(NameOfficeVisitTreatmentID), verb = "get", params_list = params_list)

	return(response)

def deleteNameOfficeVisitTreatment(NameOfficeVisitTreatmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitTreatment/" + str(NameOfficeVisitTreatmentID), verb = "delete")

	return(response)

def getEveryNameProcedure(EntityID = 1, page = 1, pageSize = 100, returnNameProcedureID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCanCreateOccurrenceAsOfDate = False, returnCreatedTime = False, returnDistributionType = False, returnDistributionTypeCode = False, returnEndDate = False, returnGreatestProcedureOccurrenceDate = False, returnIsActiveAsOfDate = False, returnIsVoid = False, returnModifiedTime = False, returnNameID = False, returnProcedureID = False, returnProcedureInstruction = False, returnReceivedParentReleaseForm = False, returnReceivedPhysicianDocumentation = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameProcedure/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameProcedure(NameProcedureID, EntityID = 1, returnreturnNameProcedureID = False, returnreturnAttachmentCount = False, returnreturnAttachmentIndicatorColumn = False, returnreturnCanCreateOccurrenceAsOfDate = False, returnreturnCreatedTime = False, returnreturnDistributionType = False, returnreturnDistributionTypeCode = False, returnreturnEndDate = False, returnreturnGreatestProcedureOccurrenceDate = False, returnreturnIsActiveAsOfDate = False, returnreturnIsVoid = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnProcedureID = False, returnreturnProcedureInstruction = False, returnreturnReceivedParentReleaseForm = False, returnreturnReceivedPhysicianDocumentation = False, returnreturnStartDate = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserIDVoidedBy = False, returnreturnVoidedTime = False, returnreturnVoidNote = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameProcedure/" + str(NameProcedureID), verb = "get", params_list = params_list)

	return(response)

def deleteNameProcedure(NameProcedureID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameProcedure/" + str(NameProcedureID), verb = "delete")

	return(response)

def getEveryNameProcedureNote(EntityID = 1, page = 1, pageSize = 100, returnNameProcedureNoteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameProcedureID = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameProcedureNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameProcedureNote(NameProcedureNoteID, EntityID = 1, returnreturnNameProcedureNoteID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNameProcedureID = False, returnreturnNote = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameProcedureNote/" + str(NameProcedureNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteNameProcedureNote(NameProcedureNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameProcedureNote/" + str(NameProcedureNoteID), verb = "delete")

	return(response)

def getEveryNameProcedureOccurrence(EntityID = 1, page = 1, pageSize = 100, returnNameProcedureOccurrenceID = True, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnFromOfficeVisit = False, returnHealthProfessionalIDPerformedBy = False, returnIsVoid = False, returnModifiedTime = False, returnNameOfficeVisitID = False, returnNameProcedureID = False, returnNote = False, returnNotPerformedReasonID = False, returnOccurrenceDate = False, returnOccurrenceType = False, returnOccurrenceTypeCode = False, returnProcedureInstructionDisplay = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameProcedureOccurrence/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameProcedureOccurrence(NameProcedureOccurrenceID, EntityID = 1, returnreturnNameProcedureOccurrenceID = False, returnreturnCreatedTime = False, returnreturnEndTime = False, returnreturnEntityID = False, returnreturnFromOfficeVisit = False, returnreturnHealthProfessionalIDPerformedBy = False, returnreturnIsVoid = False, returnreturnModifiedTime = False, returnreturnNameOfficeVisitID = False, returnreturnNameProcedureID = False, returnreturnNote = False, returnreturnNotPerformedReasonID = False, returnreturnOccurrenceDate = False, returnreturnOccurrenceType = False, returnreturnOccurrenceTypeCode = False, returnreturnProcedureInstructionDisplay = False, returnreturnStartTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserIDVoidedBy = False, returnreturnVoidedTime = False, returnreturnVoidNote = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameProcedureOccurrence/" + str(NameProcedureOccurrenceID), verb = "get", params_list = params_list)

	return(response)

def deleteNameProcedureOccurrence(NameProcedureOccurrenceID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameProcedureOccurrence/" + str(NameProcedureOccurrenceID), verb = "delete")

	return(response)

def getEveryNameProcedureSecuredNote(EntityID = 1, page = 1, pageSize = 100, returnNameProcedureSecuredNoteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameProcedureID = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameProcedureSecuredNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameProcedureSecuredNote(NameProcedureSecuredNoteID, EntityID = 1, returnreturnNameProcedureSecuredNoteID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNameProcedureID = False, returnreturnNote = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameProcedureSecuredNote/" + str(NameProcedureSecuredNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteNameProcedureSecuredNote(NameProcedureSecuredNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameProcedureSecuredNote/" + str(NameProcedureSecuredNoteID), verb = "delete")

	return(response)

def getEveryNotificationMethod(EntityID = 1, page = 1, pageSize = 100, returnNotificationMethodID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NotificationMethod/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNotificationMethod(NotificationMethodID, EntityID = 1, returnreturnNotificationMethodID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NotificationMethod/" + str(NotificationMethodID), verb = "get", params_list = params_list)

	return(response)

def deleteNotificationMethod(NotificationMethodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NotificationMethod/" + str(NotificationMethodID), verb = "delete")

	return(response)

def getEveryNotPerformedReason(EntityID = 1, page = 1, pageSize = 100, returnNotPerformedReasonID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NotPerformedReason/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNotPerformedReason(NotPerformedReasonID, EntityID = 1, returnreturnNotPerformedReasonID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NotPerformedReason/" + str(NotPerformedReasonID), verb = "get", params_list = params_list)

	return(response)

def deleteNotPerformedReason(NotPerformedReasonID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NotPerformedReason/" + str(NotPerformedReasonID), verb = "delete")

	return(response)

def getEveryOfficeVisitComment(EntityID = 1, page = 1, pageSize = 100, returnOfficeVisitCommentID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitComment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getOfficeVisitComment(OfficeVisitCommentID, EntityID = 1, returnreturnOfficeVisitCommentID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitComment/" + str(OfficeVisitCommentID), verb = "get", params_list = params_list)

	return(response)

def deleteOfficeVisitComment(OfficeVisitCommentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitComment/" + str(OfficeVisitCommentID), verb = "delete")

	return(response)

def getEveryOfficeVisitDisposition(EntityID = 1, page = 1, pageSize = 100, returnOfficeVisitDispositionID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitDisposition/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getOfficeVisitDisposition(OfficeVisitDispositionID, EntityID = 1, returnreturnOfficeVisitDispositionID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitDisposition/" + str(OfficeVisitDispositionID), verb = "get", params_list = params_list)

	return(response)

def deleteOfficeVisitDisposition(OfficeVisitDispositionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitDisposition/" + str(OfficeVisitDispositionID), verb = "delete")

	return(response)

def getEveryOfficeVisitGuardianResponse(EntityID = 1, page = 1, pageSize = 100, returnOfficeVisitGuardianResponseID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getOfficeVisitGuardianResponse(OfficeVisitGuardianResponseID, EntityID = 1, returnreturnOfficeVisitGuardianResponseID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitGuardianResponse/" + str(OfficeVisitGuardianResponseID), verb = "get", params_list = params_list)

	return(response)

def deleteOfficeVisitGuardianResponse(OfficeVisitGuardianResponseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitGuardianResponse/" + str(OfficeVisitGuardianResponseID), verb = "delete")

	return(response)

def getEveryOfficeVisitReason(EntityID = 1, page = 1, pageSize = 100, returnOfficeVisitReasonID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitReason/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getOfficeVisitReason(OfficeVisitReasonID, EntityID = 1, returnreturnOfficeVisitReasonID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitReason/" + str(OfficeVisitReasonID), verb = "get", params_list = params_list)

	return(response)

def deleteOfficeVisitReason(OfficeVisitReasonID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitReason/" + str(OfficeVisitReasonID), verb = "delete")

	return(response)

def getEveryOfficeVisitReferralReason(EntityID = 1, page = 1, pageSize = 100, returnOfficeVisitReferralReasonID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitReferralReason/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getOfficeVisitReferralReason(OfficeVisitReferralReasonID, EntityID = 1, returnreturnOfficeVisitReferralReasonID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitReferralReason/" + str(OfficeVisitReferralReasonID), verb = "get", params_list = params_list)

	return(response)

def deleteOfficeVisitReferralReason(OfficeVisitReferralReasonID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitReferralReason/" + str(OfficeVisitReferralReasonID), verb = "delete")

	return(response)

def getEveryOfficeVisitReferralResult(EntityID = 1, page = 1, pageSize = 100, returnOfficeVisitReferralResultID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitReferralResult/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getOfficeVisitReferralResult(OfficeVisitReferralResultID, EntityID = 1, returnreturnOfficeVisitReferralResultID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitReferralResult/" + str(OfficeVisitReferralResultID), verb = "get", params_list = params_list)

	return(response)

def deleteOfficeVisitReferralResult(OfficeVisitReferralResultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitReferralResult/" + str(OfficeVisitReferralResultID), verb = "delete")

	return(response)

def getEveryOfficeVisitTreatment(EntityID = 1, page = 1, pageSize = 100, returnOfficeVisitTreatmentID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitTreatment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getOfficeVisitTreatment(OfficeVisitTreatmentID, EntityID = 1, returnreturnOfficeVisitTreatmentID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitTreatment/" + str(OfficeVisitTreatmentID), verb = "get", params_list = params_list)

	return(response)

def deleteOfficeVisitTreatment(OfficeVisitTreatmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitTreatment/" + str(OfficeVisitTreatmentID), verb = "delete")

	return(response)

def getEveryPhysicalComment(EntityID = 1, page = 1, pageSize = 100, returnPhysicalCommentID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalComment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getPhysicalComment(PhysicalCommentID, EntityID = 1, returnreturnPhysicalCommentID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalComment/" + str(PhysicalCommentID), verb = "get", params_list = params_list)

	return(response)

def deletePhysicalComment(PhysicalCommentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalComment/" + str(PhysicalCommentID), verb = "delete")

	return(response)

def getEveryPhysicalGuardianNotification(EntityID = 1, page = 1, pageSize = 100, returnPhysicalGuardianNotificationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalGuardianNotification/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getPhysicalGuardianNotification(PhysicalGuardianNotificationID, EntityID = 1, returnreturnPhysicalGuardianNotificationID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalGuardianNotification/" + str(PhysicalGuardianNotificationID), verb = "get", params_list = params_list)

	return(response)

def deletePhysicalGuardianNotification(PhysicalGuardianNotificationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalGuardianNotification/" + str(PhysicalGuardianNotificationID), verb = "delete")

	return(response)

def getEveryPhysicalGuardianResponse(EntityID = 1, page = 1, pageSize = 100, returnPhysicalGuardianResponseID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getPhysicalGuardianResponse(PhysicalGuardianResponseID, EntityID = 1, returnreturnPhysicalGuardianResponseID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalGuardianResponse/" + str(PhysicalGuardianResponseID), verb = "get", params_list = params_list)

	return(response)

def deletePhysicalGuardianResponse(PhysicalGuardianResponseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalGuardianResponse/" + str(PhysicalGuardianResponseID), verb = "delete")

	return(response)

def getEveryPhysicalObservation(EntityID = 1, page = 1, pageSize = 100, returnPhysicalObservationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalObservation/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getPhysicalObservation(PhysicalObservationID, EntityID = 1, returnreturnPhysicalObservationID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalObservation/" + str(PhysicalObservationID), verb = "get", params_list = params_list)

	return(response)

def deletePhysicalObservation(PhysicalObservationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalObservation/" + str(PhysicalObservationID), verb = "delete")

	return(response)

def getEveryPhysicalReferralReason(EntityID = 1, page = 1, pageSize = 100, returnPhysicalReferralReasonID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalReferralReason/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getPhysicalReferralReason(PhysicalReferralReasonID, EntityID = 1, returnreturnPhysicalReferralReasonID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalReferralReason/" + str(PhysicalReferralReasonID), verb = "get", params_list = params_list)

	return(response)

def deletePhysicalReferralReason(PhysicalReferralReasonID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalReferralReason/" + str(PhysicalReferralReasonID), verb = "delete")

	return(response)

def getEveryPhysicalReferralResult(EntityID = 1, page = 1, pageSize = 100, returnPhysicalReferralResultID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalReferralResult/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getPhysicalReferralResult(PhysicalReferralResultID, EntityID = 1, returnreturnPhysicalReferralResultID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalReferralResult/" + str(PhysicalReferralResultID), verb = "get", params_list = params_list)

	return(response)

def deletePhysicalReferralResult(PhysicalReferralResultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalReferralResult/" + str(PhysicalReferralResultID), verb = "delete")

	return(response)

def getEveryPhysicalScreening(EntityID = 1, page = 1, pageSize = 100, returnPhysicalScreeningID = True, returnAtRiskForDiabetes = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnBodyMassIndex = False, returnBodyMassIndexPercentile = False, returnCreatedTime = False, returnDiabetesScreened = False, returnDisplayHeight = False, returnDistrictID = False, returnFirstBloodPressureReading = False, returnHealthProfessionalIDExaminedBy = False, returnHeight = False, returnHeightFeet = False, returnHeightInches = False, returnIsVoid = False, returnModifiedTime = False, returnNameID = False, returnNameOfficeVisitID = False, returnSchoolYearID = False, returnScreeningDate = False, returnSecondBloodPressureReading = False, returnSportsPhysical = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreening/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getPhysicalScreening(PhysicalScreeningID, EntityID = 1, returnreturnPhysicalScreeningID = False, returnreturnAtRiskForDiabetes = False, returnreturnAttachmentCount = False, returnreturnAttachmentIndicatorColumn = False, returnreturnBodyMassIndex = False, returnreturnBodyMassIndexPercentile = False, returnreturnCreatedTime = False, returnreturnDiabetesScreened = False, returnreturnDisplayHeight = False, returnreturnDistrictID = False, returnreturnFirstBloodPressureReading = False, returnreturnHealthProfessionalIDExaminedBy = False, returnreturnHeight = False, returnreturnHeightFeet = False, returnreturnHeightInches = False, returnreturnIsVoid = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnNameOfficeVisitID = False, returnreturnSchoolYearID = False, returnreturnScreeningDate = False, returnreturnSecondBloodPressureReading = False, returnreturnSportsPhysical = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserIDVoidedBy = False, returnreturnVoidedTime = False, returnreturnVoidNote = False, returnreturnWeight = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreening/" + str(PhysicalScreeningID), verb = "get", params_list = params_list)

	return(response)

def deletePhysicalScreening(PhysicalScreeningID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreening/" + str(PhysicalScreeningID), verb = "delete")

	return(response)

def getEveryPhysicalScreeningComment(EntityID = 1, page = 1, pageSize = 100, returnPhysicalScreeningCommentID = True, returnCreatedTime = False, returnModifiedTime = False, returnPhysicalCommentID = False, returnPhysicalScreeningID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningComment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getPhysicalScreeningComment(PhysicalScreeningCommentID, EntityID = 1, returnreturnPhysicalScreeningCommentID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnPhysicalCommentID = False, returnreturnPhysicalScreeningID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningComment/" + str(PhysicalScreeningCommentID), verb = "get", params_list = params_list)

	return(response)

def deletePhysicalScreeningComment(PhysicalScreeningCommentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningComment/" + str(PhysicalScreeningCommentID), verb = "delete")

	return(response)

def getEveryPhysicalScreeningNote(EntityID = 1, page = 1, pageSize = 100, returnPhysicalScreeningNoteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnPhysicalScreeningID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getPhysicalScreeningNote(PhysicalScreeningNoteID, EntityID = 1, returnreturnPhysicalScreeningNoteID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnPhysicalScreeningID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningNote/" + str(PhysicalScreeningNoteID), verb = "get", params_list = params_list)

	return(response)

def deletePhysicalScreeningNote(PhysicalScreeningNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningNote/" + str(PhysicalScreeningNoteID), verb = "delete")

	return(response)

def getEveryPhysicalScreeningObservation(EntityID = 1, page = 1, pageSize = 100, returnPhysicalScreeningObservationID = True, returnCreatedTime = False, returnModifiedTime = False, returnPhysicalObservationID = False, returnPhysicalScreeningID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningObservation/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getPhysicalScreeningObservation(PhysicalScreeningObservationID, EntityID = 1, returnreturnPhysicalScreeningObservationID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnPhysicalObservationID = False, returnreturnPhysicalScreeningID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningObservation/" + str(PhysicalScreeningObservationID), verb = "get", params_list = params_list)

	return(response)

def deletePhysicalScreeningObservation(PhysicalScreeningObservationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningObservation/" + str(PhysicalScreeningObservationID), verb = "delete")

	return(response)

def getEveryPhysicalScreeningReferral(EntityID = 1, page = 1, pageSize = 100, returnPhysicalScreeningReferralID = True, returnCompletionDate = False, returnCreatedTime = False, returnHealthProfessionalIDReferredBy = False, returnHealthProfessionalIDReferredTo = False, returnModifiedTime = False, returnPhysicalGuardianNotificationID = False, returnPhysicalGuardianResponseID = False, returnPhysicalReferralReasonID = False, returnPhysicalReferralResultID = False, returnPhysicalScreeningID = False, returnReferralCompleted = False, returnReferralDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningReferral/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getPhysicalScreeningReferral(PhysicalScreeningReferralID, EntityID = 1, returnreturnPhysicalScreeningReferralID = False, returnreturnCompletionDate = False, returnreturnCreatedTime = False, returnreturnHealthProfessionalIDReferredBy = False, returnreturnHealthProfessionalIDReferredTo = False, returnreturnModifiedTime = False, returnreturnPhysicalGuardianNotificationID = False, returnreturnPhysicalGuardianResponseID = False, returnreturnPhysicalReferralReasonID = False, returnreturnPhysicalReferralResultID = False, returnreturnPhysicalScreeningID = False, returnreturnReferralCompleted = False, returnreturnReferralDate = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningReferral/" + str(PhysicalScreeningReferralID), verb = "get", params_list = params_list)

	return(response)

def deletePhysicalScreeningReferral(PhysicalScreeningReferralID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningReferral/" + str(PhysicalScreeningReferralID), verb = "delete")

	return(response)

def getEveryPhysicalScreeningSecuredNote(EntityID = 1, page = 1, pageSize = 100, returnPhysicalScreeningSecuredNoteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnPhysicalScreeningID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningSecuredNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getPhysicalScreeningSecuredNote(PhysicalScreeningSecuredNoteID, EntityID = 1, returnreturnPhysicalScreeningSecuredNoteID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnPhysicalScreeningID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningSecuredNote/" + str(PhysicalScreeningSecuredNoteID), verb = "get", params_list = params_list)

	return(response)

def deletePhysicalScreeningSecuredNote(PhysicalScreeningSecuredNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningSecuredNote/" + str(PhysicalScreeningSecuredNoteID), verb = "delete")

	return(response)

def getEveryProcedure(EntityID = 1, page = 1, pageSize = 100, returnProcedureID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Procedure/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getProcedure(ProcedureID, EntityID = 1, returnreturnProcedureID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Procedure/" + str(ProcedureID), verb = "get", params_list = params_list)

	return(response)

def deleteProcedure(ProcedureID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Procedure/" + str(ProcedureID), verb = "delete")

	return(response)

def getEveryScoliosisComment(EntityID = 1, page = 1, pageSize = 100, returnScoliosisCommentID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisComment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getScoliosisComment(ScoliosisCommentID, EntityID = 1, returnreturnScoliosisCommentID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisComment/" + str(ScoliosisCommentID), verb = "get", params_list = params_list)

	return(response)

def deleteScoliosisComment(ScoliosisCommentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisComment/" + str(ScoliosisCommentID), verb = "delete")

	return(response)

def getEveryScoliosisGuardianNotification(EntityID = 1, page = 1, pageSize = 100, returnScoliosisGuardianNotificationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisGuardianNotification/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getScoliosisGuardianNotification(ScoliosisGuardianNotificationID, EntityID = 1, returnreturnScoliosisGuardianNotificationID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisGuardianNotification/" + str(ScoliosisGuardianNotificationID), verb = "get", params_list = params_list)

	return(response)

def deleteScoliosisGuardianNotification(ScoliosisGuardianNotificationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisGuardianNotification/" + str(ScoliosisGuardianNotificationID), verb = "delete")

	return(response)

def getEveryScoliosisGuardianResponse(EntityID = 1, page = 1, pageSize = 100, returnScoliosisGuardianResponseID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getScoliosisGuardianResponse(ScoliosisGuardianResponseID, EntityID = 1, returnreturnScoliosisGuardianResponseID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisGuardianResponse/" + str(ScoliosisGuardianResponseID), verb = "get", params_list = params_list)

	return(response)

def deleteScoliosisGuardianResponse(ScoliosisGuardianResponseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisGuardianResponse/" + str(ScoliosisGuardianResponseID), verb = "delete")

	return(response)

def getEveryScoliosisObservation(EntityID = 1, page = 1, pageSize = 100, returnScoliosisObservationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisObservation/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getScoliosisObservation(ScoliosisObservationID, EntityID = 1, returnreturnScoliosisObservationID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisObservation/" + str(ScoliosisObservationID), verb = "get", params_list = params_list)

	return(response)

def deleteScoliosisObservation(ScoliosisObservationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisObservation/" + str(ScoliosisObservationID), verb = "delete")

	return(response)

def getEveryScoliosisReferralReason(EntityID = 1, page = 1, pageSize = 100, returnScoliosisReferralReasonID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisReferralReason/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getScoliosisReferralReason(ScoliosisReferralReasonID, EntityID = 1, returnreturnScoliosisReferralReasonID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisReferralReason/" + str(ScoliosisReferralReasonID), verb = "get", params_list = params_list)

	return(response)

def deleteScoliosisReferralReason(ScoliosisReferralReasonID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisReferralReason/" + str(ScoliosisReferralReasonID), verb = "delete")

	return(response)

def getEveryScoliosisReferralResult(EntityID = 1, page = 1, pageSize = 100, returnScoliosisReferralResultID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisReferralResult/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getScoliosisReferralResult(ScoliosisReferralResultID, EntityID = 1, returnreturnScoliosisReferralResultID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisReferralResult/" + str(ScoliosisReferralResultID), verb = "get", params_list = params_list)

	return(response)

def deleteScoliosisReferralResult(ScoliosisReferralResultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisReferralResult/" + str(ScoliosisReferralResultID), verb = "delete")

	return(response)

def getEveryScoliosisResult(EntityID = 1, page = 1, pageSize = 100, returnScoliosisResultID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisResult/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getScoliosisResult(ScoliosisResultID, EntityID = 1, returnreturnScoliosisResultID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnType = False, returnreturnTypeCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisResult/" + str(ScoliosisResultID), verb = "get", params_list = params_list)

	return(response)

def deleteScoliosisResult(ScoliosisResultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisResult/" + str(ScoliosisResultID), verb = "delete")

	return(response)

def getEveryScoliosisScreening(EntityID = 1, page = 1, pageSize = 100, returnScoliosisScreeningID = True, returnCreatedTime = False, returnDistrictID = False, returnHealthProfessionalIDExaminedBy = False, returnIsVoid = False, returnLatestScoliosisScreeningReferral = False, returnModifiedTime = False, returnNameID = False, returnObservationDescriptionsListDisplay = False, returnRescreen = False, returnSchoolYearID = False, returnScoliosisResultID = False, returnScoliosisTreatmentID = False, returnScreeningDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreening/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getScoliosisScreening(ScoliosisScreeningID, EntityID = 1, returnreturnScoliosisScreeningID = False, returnreturnCreatedTime = False, returnreturnDistrictID = False, returnreturnHealthProfessionalIDExaminedBy = False, returnreturnIsVoid = False, returnreturnLatestScoliosisScreeningReferral = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnObservationDescriptionsListDisplay = False, returnreturnRescreen = False, returnreturnSchoolYearID = False, returnreturnScoliosisResultID = False, returnreturnScoliosisTreatmentID = False, returnreturnScreeningDate = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserIDVoidedBy = False, returnreturnVoidedTime = False, returnreturnVoidNote = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreening/" + str(ScoliosisScreeningID), verb = "get", params_list = params_list)

	return(response)

def deleteScoliosisScreening(ScoliosisScreeningID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreening/" + str(ScoliosisScreeningID), verb = "delete")

	return(response)

def getEveryScoliosisScreeningComment(EntityID = 1, page = 1, pageSize = 100, returnScoliosisScreeningCommentID = True, returnCreatedTime = False, returnModifiedTime = False, returnScoliosisCommentID = False, returnScoliosisScreeningID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningComment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getScoliosisScreeningComment(ScoliosisScreeningCommentID, EntityID = 1, returnreturnScoliosisScreeningCommentID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnScoliosisCommentID = False, returnreturnScoliosisScreeningID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningComment/" + str(ScoliosisScreeningCommentID), verb = "get", params_list = params_list)

	return(response)

def deleteScoliosisScreeningComment(ScoliosisScreeningCommentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningComment/" + str(ScoliosisScreeningCommentID), verb = "delete")

	return(response)

def getEveryScoliosisScreeningNote(EntityID = 1, page = 1, pageSize = 100, returnScoliosisScreeningNoteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnScoliosisScreeningID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getScoliosisScreeningNote(ScoliosisScreeningNoteID, EntityID = 1, returnreturnScoliosisScreeningNoteID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnScoliosisScreeningID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningNote/" + str(ScoliosisScreeningNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteScoliosisScreeningNote(ScoliosisScreeningNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningNote/" + str(ScoliosisScreeningNoteID), verb = "delete")

	return(response)

def getEveryScoliosisScreeningObservation(EntityID = 1, page = 1, pageSize = 100, returnScoliosisScreeningObservationID = True, returnCreatedTime = False, returnModifiedTime = False, returnScoliosisObservationID = False, returnScoliosisScreeningID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningObservation/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getScoliosisScreeningObservation(ScoliosisScreeningObservationID, EntityID = 1, returnreturnScoliosisScreeningObservationID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnScoliosisObservationID = False, returnreturnScoliosisScreeningID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningObservation/" + str(ScoliosisScreeningObservationID), verb = "get", params_list = params_list)

	return(response)

def deleteScoliosisScreeningObservation(ScoliosisScreeningObservationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningObservation/" + str(ScoliosisScreeningObservationID), verb = "delete")

	return(response)

def getEveryScoliosisScreeningReferral(EntityID = 1, page = 1, pageSize = 100, returnScoliosisScreeningReferralID = True, returnCompletionDate = False, returnCreatedTime = False, returnHealthProfessionalIDReferredBy = False, returnHealthProfessionalIDReferredTo = False, returnModifiedTime = False, returnReferralCompleted = False, returnReferralDate = False, returnScoliosisGuardianNotificationID = False, returnScoliosisGuardianResponseID = False, returnScoliosisReferralReasonID = False, returnScoliosisReferralResultID = False, returnScoliosisScreeningID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningReferral/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getScoliosisScreeningReferral(ScoliosisScreeningReferralID, EntityID = 1, returnreturnScoliosisScreeningReferralID = False, returnreturnCompletionDate = False, returnreturnCreatedTime = False, returnreturnHealthProfessionalIDReferredBy = False, returnreturnHealthProfessionalIDReferredTo = False, returnreturnModifiedTime = False, returnreturnReferralCompleted = False, returnreturnReferralDate = False, returnreturnScoliosisGuardianNotificationID = False, returnreturnScoliosisGuardianResponseID = False, returnreturnScoliosisReferralReasonID = False, returnreturnScoliosisReferralResultID = False, returnreturnScoliosisScreeningID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningReferral/" + str(ScoliosisScreeningReferralID), verb = "get", params_list = params_list)

	return(response)

def deleteScoliosisScreeningReferral(ScoliosisScreeningReferralID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningReferral/" + str(ScoliosisScreeningReferralID), verb = "delete")

	return(response)

def getEveryScoliosisScreeningSecuredNote(EntityID = 1, page = 1, pageSize = 100, returnScoliosisScreeningSecuredNoteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnScoliosisScreeningID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningSecuredNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getScoliosisScreeningSecuredNote(ScoliosisScreeningSecuredNoteID, EntityID = 1, returnreturnScoliosisScreeningSecuredNoteID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnScoliosisScreeningID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningSecuredNote/" + str(ScoliosisScreeningSecuredNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteScoliosisScreeningSecuredNote(ScoliosisScreeningSecuredNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningSecuredNote/" + str(ScoliosisScreeningSecuredNoteID), verb = "delete")

	return(response)

def getEveryScoliosisTreatment(EntityID = 1, page = 1, pageSize = 100, returnScoliosisTreatmentID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisTreatment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getScoliosisTreatment(ScoliosisTreatmentID, EntityID = 1, returnreturnScoliosisTreatmentID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisTreatment/" + str(ScoliosisTreatmentID), verb = "get", params_list = params_list)

	return(response)

def deleteScoliosisTreatment(ScoliosisTreatmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisTreatment/" + str(ScoliosisTreatmentID), verb = "delete")

	return(response)

def getEveryStudentChildhoodIllness(EntityID = 1, page = 1, pageSize = 100, returnStudentChildhoodIllnessID = True, returnAgeDiagnosed = False, returnChildhoodIllnessID = False, returnCreatedTime = False, returnDistrictID = False, returnHealthProfessionalIDExaminedBy = False, returnIsVoid = False, returnModifiedTime = False, returnObservationDescriptionsListDisplay = False, returnSchoolYearID = False, returnScreeningDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllness/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentChildhoodIllness(StudentChildhoodIllnessID, EntityID = 1, returnreturnStudentChildhoodIllnessID = False, returnreturnAgeDiagnosed = False, returnreturnChildhoodIllnessID = False, returnreturnCreatedTime = False, returnreturnDistrictID = False, returnreturnHealthProfessionalIDExaminedBy = False, returnreturnIsVoid = False, returnreturnModifiedTime = False, returnreturnObservationDescriptionsListDisplay = False, returnreturnSchoolYearID = False, returnreturnScreeningDate = False, returnreturnStudentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserIDVoidedBy = False, returnreturnVoidedTime = False, returnreturnVoidNote = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllness/" + str(StudentChildhoodIllnessID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentChildhoodIllness(StudentChildhoodIllnessID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllness/" + str(StudentChildhoodIllnessID), verb = "delete")

	return(response)

def getEveryStudentChildhoodIllnessComment(EntityID = 1, page = 1, pageSize = 100, returnStudentChildhoodIllnessCommentID = True, returnChildhoodIllnessCommentID = False, returnCreatedTime = False, returnModifiedTime = False, returnStudentChildhoodIllnessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessComment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentChildhoodIllnessComment(StudentChildhoodIllnessCommentID, EntityID = 1, returnreturnStudentChildhoodIllnessCommentID = False, returnreturnChildhoodIllnessCommentID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnStudentChildhoodIllnessID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessComment/" + str(StudentChildhoodIllnessCommentID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentChildhoodIllnessComment(StudentChildhoodIllnessCommentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessComment/" + str(StudentChildhoodIllnessCommentID), verb = "delete")

	return(response)

def getEveryStudentChildhoodIllnessNote(EntityID = 1, page = 1, pageSize = 100, returnStudentChildhoodIllnessNoteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnStudentChildhoodIllnessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentChildhoodIllnessNote(StudentChildhoodIllnessNoteID, EntityID = 1, returnreturnStudentChildhoodIllnessNoteID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnStudentChildhoodIllnessID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessNote/" + str(StudentChildhoodIllnessNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentChildhoodIllnessNote(StudentChildhoodIllnessNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessNote/" + str(StudentChildhoodIllnessNoteID), verb = "delete")

	return(response)

def getEveryStudentChildhoodIllnessObservation(EntityID = 1, page = 1, pageSize = 100, returnStudentChildhoodIllnessObservationID = True, returnChildhoodIllnessObservationID = False, returnCreatedTime = False, returnModifiedTime = False, returnStudentChildhoodIllnessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessObservation/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentChildhoodIllnessObservation(StudentChildhoodIllnessObservationID, EntityID = 1, returnreturnStudentChildhoodIllnessObservationID = False, returnreturnChildhoodIllnessObservationID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnStudentChildhoodIllnessID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessObservation/" + str(StudentChildhoodIllnessObservationID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentChildhoodIllnessObservation(StudentChildhoodIllnessObservationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessObservation/" + str(StudentChildhoodIllnessObservationID), verb = "delete")

	return(response)

def getEveryStudentChildhoodIllnessReferral(EntityID = 1, page = 1, pageSize = 100, returnStudentChildhoodIllnessReferralID = True, returnChildhoodIllnessGuardianNotificationID = False, returnChildhoodIllnessGuardianResponseID = False, returnChildhoodIllnessReferralReasonID = False, returnChildhoodIllnessReferralResultID = False, returnCompletionDate = False, returnCreatedTime = False, returnHealthProfessionalIDReferredBy = False, returnHealthProfessionalIDReferredTo = False, returnModifiedTime = False, returnReferralCompleted = False, returnReferralDate = False, returnStudentChildhoodIllnessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessReferral/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentChildhoodIllnessReferral(StudentChildhoodIllnessReferralID, EntityID = 1, returnreturnStudentChildhoodIllnessReferralID = False, returnreturnChildhoodIllnessGuardianNotificationID = False, returnreturnChildhoodIllnessGuardianResponseID = False, returnreturnChildhoodIllnessReferralReasonID = False, returnreturnChildhoodIllnessReferralResultID = False, returnreturnCompletionDate = False, returnreturnCreatedTime = False, returnreturnHealthProfessionalIDReferredBy = False, returnreturnHealthProfessionalIDReferredTo = False, returnreturnModifiedTime = False, returnreturnReferralCompleted = False, returnreturnReferralDate = False, returnreturnStudentChildhoodIllnessID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessReferral/" + str(StudentChildhoodIllnessReferralID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentChildhoodIllnessReferral(StudentChildhoodIllnessReferralID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessReferral/" + str(StudentChildhoodIllnessReferralID), verb = "delete")

	return(response)

def getEveryStudentChildhoodIllnessSecuredNote(EntityID = 1, page = 1, pageSize = 100, returnStudentChildhoodIllnessSecuredNoteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnStudentChildhoodIllnessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessSecuredNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentChildhoodIllnessSecuredNote(StudentChildhoodIllnessSecuredNoteID, EntityID = 1, returnreturnStudentChildhoodIllnessSecuredNoteID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnStudentChildhoodIllnessID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessSecuredNote/" + str(StudentChildhoodIllnessSecuredNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentChildhoodIllnessSecuredNote(StudentChildhoodIllnessSecuredNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessSecuredNote/" + str(StudentChildhoodIllnessSecuredNoteID), verb = "delete")

	return(response)

def getEveryStudentHealthCondition(EntityID = 1, page = 1, pageSize = 100, returnStudentHealthConditionID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnHealthConditionID = False, returnHealthConditionTreatmentID = False, returnHealthProfessionalIDExaminedBy = False, returnIsActive = False, returnIsVoid = False, returnModifiedTime = False, returnOriginalEndDate = False, returnStartDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentHealthCondition/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentHealthCondition(StudentHealthConditionID, EntityID = 1, returnreturnStudentHealthConditionID = False, returnreturnAttachmentCount = False, returnreturnAttachmentIndicatorColumn = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnEndDate = False, returnreturnHealthConditionID = False, returnreturnHealthConditionTreatmentID = False, returnreturnHealthProfessionalIDExaminedBy = False, returnreturnIsActive = False, returnreturnIsVoid = False, returnreturnModifiedTime = False, returnreturnOriginalEndDate = False, returnreturnStartDate = False, returnreturnStudentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserIDVoidedBy = False, returnreturnVoidedTime = False, returnreturnVoidNote = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentHealthCondition/" + str(StudentHealthConditionID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentHealthCondition(StudentHealthConditionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentHealthCondition/" + str(StudentHealthConditionID), verb = "delete")

	return(response)

def getEveryStudentHealthConditionComment(EntityID = 1, page = 1, pageSize = 100, returnStudentHealthConditionCommentID = True, returnCreatedTime = False, returnHealthConditionCommentID = False, returnModifiedTime = False, returnStudentHealthConditionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentHealthConditionComment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentHealthConditionComment(StudentHealthConditionCommentID, EntityID = 1, returnreturnStudentHealthConditionCommentID = False, returnreturnCreatedTime = False, returnreturnHealthConditionCommentID = False, returnreturnModifiedTime = False, returnreturnStudentHealthConditionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentHealthConditionComment/" + str(StudentHealthConditionCommentID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentHealthConditionComment(StudentHealthConditionCommentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentHealthConditionComment/" + str(StudentHealthConditionCommentID), verb = "delete")

	return(response)

def getEveryStudentHealthConditionNote(EntityID = 1, page = 1, pageSize = 100, returnStudentHealthConditionNoteID = True, returnCreatedTime = False, returnIsNoteEnteredByGuardian = False, returnModifiedTime = False, returnNote = False, returnNoteEnteredByType = False, returnNoteEnteredByTypeCode = False, returnNoteEnteredByTypeLabel = False, returnStudentHealthConditionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentHealthConditionNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentHealthConditionNote(StudentHealthConditionNoteID, EntityID = 1, returnreturnStudentHealthConditionNoteID = False, returnreturnCreatedTime = False, returnreturnIsNoteEnteredByGuardian = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnNoteEnteredByType = False, returnreturnNoteEnteredByTypeCode = False, returnreturnNoteEnteredByTypeLabel = False, returnreturnStudentHealthConditionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentHealthConditionNote/" + str(StudentHealthConditionNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentHealthConditionNote(StudentHealthConditionNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentHealthConditionNote/" + str(StudentHealthConditionNoteID), verb = "delete")

	return(response)

def getEveryStudentHealthConditionSecuredNote(EntityID = 1, page = 1, pageSize = 100, returnStudentHealthConditionSecuredNoteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnStudentHealthConditionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentHealthConditionSecuredNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentHealthConditionSecuredNote(StudentHealthConditionSecuredNoteID, EntityID = 1, returnreturnStudentHealthConditionSecuredNoteID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnStudentHealthConditionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentHealthConditionSecuredNote/" + str(StudentHealthConditionSecuredNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentHealthConditionSecuredNote(StudentHealthConditionSecuredNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentHealthConditionSecuredNote/" + str(StudentHealthConditionSecuredNoteID), verb = "delete")

	return(response)

def getEveryStudentIHP(EntityID = 1, page = 1, pageSize = 100, returnStudentIHPID = True, returnAttachmentComments = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnEndDate = False, returnFormDescription = False, returnIsActive = False, returnIsVoid = False, returnModifiedTime = False, returnStartDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentIHP/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentIHP(StudentIHPID, EntityID = 1, returnreturnStudentIHPID = False, returnreturnAttachmentComments = False, returnreturnAttachmentCount = False, returnreturnAttachmentIndicatorColumn = False, returnreturnCreatedTime = False, returnreturnEndDate = False, returnreturnFormDescription = False, returnreturnIsActive = False, returnreturnIsVoid = False, returnreturnModifiedTime = False, returnreturnStartDate = False, returnreturnStudentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserIDVoidedBy = False, returnreturnVoidedTime = False, returnreturnVoidNote = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentIHP/" + str(StudentIHPID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentIHP(StudentIHPID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentIHP/" + str(StudentIHPID), verb = "delete")

	return(response)

def getEveryStudentVaccinationWaiver(EntityID = 1, page = 1, pageSize = 100, returnStudentVaccinationWaiverID = True, returnClaimDate = False, returnCreatedTime = False, returnExpirationDate = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationWaiverID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccinationWaiver/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentVaccinationWaiver(StudentVaccinationWaiverID, EntityID = 1, returnreturnStudentVaccinationWaiverID = False, returnreturnClaimDate = False, returnreturnCreatedTime = False, returnreturnExpirationDate = False, returnreturnModifiedTime = False, returnreturnStudentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVaccinationWaiverID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccinationWaiver/" + str(StudentVaccinationWaiverID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentVaccinationWaiver(StudentVaccinationWaiverID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccinationWaiver/" + str(StudentVaccinationWaiverID), verb = "delete")

	return(response)

def getEveryStudentVaccinationYear(EntityID = 1, page = 1, pageSize = 100, returnStudentVaccinationYearID = True, returnCalculatedGradeCode = False, returnCalculatedGradeNumeric = False, returnCreatedTime = False, returnEffectiveDate = False, returnModifiedTime = False, returnStudentID = False, returnStudentVaccineCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationYearID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccinationYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentVaccinationYear(StudentVaccinationYearID, EntityID = 1, returnreturnStudentVaccinationYearID = False, returnreturnCalculatedGradeCode = False, returnreturnCalculatedGradeNumeric = False, returnreturnCreatedTime = False, returnreturnEffectiveDate = False, returnreturnModifiedTime = False, returnreturnStudentID = False, returnreturnStudentVaccineCount = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVaccinationYearID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccinationYear/" + str(StudentVaccinationYearID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentVaccinationYear(StudentVaccinationYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccinationYear/" + str(StudentVaccinationYearID), verb = "delete")

	return(response)

def getEveryStudentVaccinationYearStatus(EntityID = 1, page = 1, pageSize = 100, returnStudentVaccinationYearStatusID = True, returnAllDoseDates = False, returnComplianceScheduleDetailID = False, returnCreatedTime = False, returnEndDate = False, returnInvalidDoseDates = False, returnIsConditional = False, returnIsInComplianceByVaccines = False, returnIsOutOfCompliance = False, returnIsOutOfComplianceConditionalDisplay = False, returnIsProvisional = False, returnModifiedTime = False, returnReasonConditional = False, returnReasonOutOfCompliance = False, returnStartDate = False, returnStudentChildhoodIllnessID = False, returnStudentID = False, returnStudentVaccinationWaiverID = False, returnStudentVaccinationYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationYearComplianceScheduleID = False, returnValidDoseDates = False, returnValidDoses = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccinationYearStatus/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentVaccinationYearStatus(StudentVaccinationYearStatusID, EntityID = 1, returnreturnStudentVaccinationYearStatusID = False, returnreturnAllDoseDates = False, returnreturnComplianceScheduleDetailID = False, returnreturnCreatedTime = False, returnreturnEndDate = False, returnreturnInvalidDoseDates = False, returnreturnIsConditional = False, returnreturnIsInComplianceByVaccines = False, returnreturnIsOutOfCompliance = False, returnreturnIsOutOfComplianceConditionalDisplay = False, returnreturnIsProvisional = False, returnreturnModifiedTime = False, returnreturnReasonConditional = False, returnreturnReasonOutOfCompliance = False, returnreturnStartDate = False, returnreturnStudentChildhoodIllnessID = False, returnreturnStudentID = False, returnreturnStudentVaccinationWaiverID = False, returnreturnStudentVaccinationYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVaccinationYearComplianceScheduleID = False, returnreturnValidDoseDates = False, returnreturnValidDoses = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccinationYearStatus/" + str(StudentVaccinationYearStatusID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentVaccinationYearStatus(StudentVaccinationYearStatusID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccinationYearStatus/" + str(StudentVaccinationYearStatusID), verb = "delete")

	return(response)

def getEveryStudentVaccinationYearStatusStudentVaccine(EntityID = 1, page = 1, pageSize = 100, returnStudentVaccinationYearStatusStudentVaccineID = True, returnCreatedTime = False, returnInvalidDoseReason = False, returnIsValidDose = False, returnModifiedTime = False, returnStudentVaccinationYearStatusID = False, returnStudentVaccineID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccinationYearStatusStudentVaccine/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentVaccinationYearStatusStudentVaccine(StudentVaccinationYearStatusStudentVaccineID, EntityID = 1, returnreturnStudentVaccinationYearStatusStudentVaccineID = False, returnreturnCreatedTime = False, returnreturnInvalidDoseReason = False, returnreturnIsValidDose = False, returnreturnModifiedTime = False, returnreturnStudentVaccinationYearStatusID = False, returnreturnStudentVaccineID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccinationYearStatusStudentVaccine/" + str(StudentVaccinationYearStatusStudentVaccineID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentVaccinationYearStatusStudentVaccine(StudentVaccinationYearStatusStudentVaccineID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccinationYearStatusStudentVaccine/" + str(StudentVaccinationYearStatusStudentVaccineID), verb = "delete")

	return(response)

def getEveryStudentVaccine(EntityID = 1, page = 1, pageSize = 100, returnStudentVaccineID = True, returnCreatedTime = False, returnDate = False, returnLotNumber = False, returnModifiedTime = False, returnStudentID = False, returnStudentVaccineDates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccineID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccine/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentVaccine(StudentVaccineID, EntityID = 1, returnreturnStudentVaccineID = False, returnreturnCreatedTime = False, returnreturnDate = False, returnreturnLotNumber = False, returnreturnModifiedTime = False, returnreturnStudentID = False, returnreturnStudentVaccineDates = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVaccineID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccine/" + str(StudentVaccineID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentVaccine(StudentVaccineID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccine/" + str(StudentVaccineID), verb = "delete")

	return(response)

def getEveryStudentVaccineMaintenance(EntityID = 1, page = 1, pageSize = 100, returnVaccineID = True, returnDate1 = False, returnDate2 = False, returnDate3 = False, returnDate4 = False, returnDate5 = False, returnDate6 = False, returnDate7 = False, returnHasExistingStudentVaccines = False, returnLotNumber1 = False, returnLotNumber2 = False, returnLotNumber3 = False, returnLotNumber4 = False, returnLotNumber5 = False, returnLotNumber6 = False, returnLotNumber7 = False, returnStudentID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccineMaintenance/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentVaccineMaintenance(VaccineID, EntityID = 1, returnreturnVaccineID = False, returnreturnDate1 = False, returnreturnDate2 = False, returnreturnDate3 = False, returnreturnDate4 = False, returnreturnDate5 = False, returnreturnDate6 = False, returnreturnDate7 = False, returnreturnHasExistingStudentVaccines = False, returnreturnLotNumber1 = False, returnreturnLotNumber2 = False, returnreturnLotNumber3 = False, returnreturnLotNumber4 = False, returnreturnLotNumber5 = False, returnreturnLotNumber6 = False, returnreturnLotNumber7 = False, returnreturnStudentID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccineMaintenance/" + str(VaccineID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentVaccineMaintenance(VaccineID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccineMaintenance/" + str(VaccineID), verb = "delete")

	return(response)

def getEveryTempAdministerNameMedication(EntityID = 1, page = 1, pageSize = 100, returnTempAdministerNameMedicationID = True, returnAdministerNameMedicationID = False, returnAdministrationTime = False, returnCreatedTime = False, returnDosesAdministered = False, returnErrorMessage = False, returnMedicationCode = False, returnModifiedTime = False, returnName = False, returnNewDosesAdministered = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempAdministerNameMedication/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempAdministerNameMedication(TempAdministerNameMedicationID, EntityID = 1, returnreturnTempAdministerNameMedicationID = False, returnreturnAdministerNameMedicationID = False, returnreturnAdministrationTime = False, returnreturnCreatedTime = False, returnreturnDosesAdministered = False, returnreturnErrorMessage = False, returnreturnMedicationCode = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnNewDosesAdministered = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempAdministerNameMedication/" + str(TempAdministerNameMedicationID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAdministerNameMedication(TempAdministerNameMedicationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempAdministerNameMedication/" + str(TempAdministerNameMedicationID), verb = "delete")

	return(response)

def getEveryTempNameMedication(EntityID = 1, page = 1, pageSize = 100, returnTempNameMedicationID = True, returnCode = False, returnCreatedTime = False, returnMaxDosesPerDay = False, returnMedicationCode = False, returnMedicationDosageUnitID = False, returnMedicationRouteID = False, returnModifiedTime = False, returnName = False, returnNameMedicationID = False, returnNewCode = False, returnNewMaxDosesPerDay = False, returnNewMedicationDosageUnitID = False, returnNewMedicationRouteID = False, returnNewRouteName = False, returnNewUnitsPerDoseHigh = False, returnNewUnitsPerDoseLow = False, returnRouteName = False, returnUnitsPerDoseHigh = False, returnUnitsPerDoseLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempNameMedication/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempNameMedication(TempNameMedicationID, EntityID = 1, returnreturnTempNameMedicationID = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnMaxDosesPerDay = False, returnreturnMedicationCode = False, returnreturnMedicationDosageUnitID = False, returnreturnMedicationRouteID = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnNameMedicationID = False, returnreturnNewCode = False, returnreturnNewMaxDosesPerDay = False, returnreturnNewMedicationDosageUnitID = False, returnreturnNewMedicationRouteID = False, returnreturnNewRouteName = False, returnreturnNewUnitsPerDoseHigh = False, returnreturnNewUnitsPerDoseLow = False, returnreturnRouteName = False, returnreturnUnitsPerDoseHigh = False, returnreturnUnitsPerDoseLow = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempNameMedication/" + str(TempNameMedicationID), verb = "get", params_list = params_list)

	return(response)

def deleteTempNameMedication(TempNameMedicationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempNameMedication/" + str(TempNameMedicationID), verb = "delete")

	return(response)

def getEveryTempStudentChildhoodIllness(EntityID = 1, page = 1, pageSize = 100, returnTempStudentChildhoodIllnessID = True, returnAgeDiagnosed = False, returnChildhoodIllnessCode = False, returnChildhoodIllnessDescription = False, returnCreatedTime = False, returnIsVoid = False, returnModifiedTime = False, returnNewChildhoodIllnessCode = False, returnNewChildhoodIllnessDescription = False, returnNewChildhoodIllnessID = False, returnSchoolYear = False, returnScreeningDate = False, returnStudentChildhoodIllnessID = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempStudentChildhoodIllness/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempStudentChildhoodIllness(TempStudentChildhoodIllnessID, EntityID = 1, returnreturnTempStudentChildhoodIllnessID = False, returnreturnAgeDiagnosed = False, returnreturnChildhoodIllnessCode = False, returnreturnChildhoodIllnessDescription = False, returnreturnCreatedTime = False, returnreturnIsVoid = False, returnreturnModifiedTime = False, returnreturnNewChildhoodIllnessCode = False, returnreturnNewChildhoodIllnessDescription = False, returnreturnNewChildhoodIllnessID = False, returnreturnSchoolYear = False, returnreturnScreeningDate = False, returnreturnStudentChildhoodIllnessID = False, returnreturnStudentName = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempStudentChildhoodIllness/" + str(TempStudentChildhoodIllnessID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStudentChildhoodIllness(TempStudentChildhoodIllnessID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempStudentChildhoodIllness/" + str(TempStudentChildhoodIllnessID), verb = "delete")

	return(response)

def getEveryTempStudentVaccine(EntityID = 1, page = 1, pageSize = 100, returnTempStudentVaccineID = True, returnCreatedTime = False, returnCVXCode = False, returnDate = False, returnIsDuplicate = False, returnModifiedTime = False, returnNewCVXCode = False, returnNewVaccineCode = False, returnNewVaccineID = False, returnStudentName = False, returnStudentVaccineID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccineCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempStudentVaccine/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempStudentVaccine(TempStudentVaccineID, EntityID = 1, returnreturnTempStudentVaccineID = False, returnreturnCreatedTime = False, returnreturnCVXCode = False, returnreturnDate = False, returnreturnIsDuplicate = False, returnreturnModifiedTime = False, returnreturnNewCVXCode = False, returnreturnNewVaccineCode = False, returnreturnNewVaccineID = False, returnreturnStudentName = False, returnreturnStudentVaccineID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVaccineCode = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempStudentVaccine/" + str(TempStudentVaccineID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStudentVaccine(TempStudentVaccineID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempStudentVaccine/" + str(TempStudentVaccineID), verb = "delete")

	return(response)

def getEveryVaccination(EntityID = 1, page = 1, pageSize = 100, returnVaccinationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnIsDistrictDefined = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUsedByDistrict = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Vaccination/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVaccination(VaccinationID, EntityID = 1, returnreturnVaccinationID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDisplayOrder = False, returnreturnIsDistrictDefined = False, returnreturnModifiedTime = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUsedByDistrict = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Vaccination/" + str(VaccinationID), verb = "get", params_list = params_list)

	return(response)

def deleteVaccination(VaccinationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Vaccination/" + str(VaccinationID), verb = "delete")

	return(response)

def getEveryVaccinationChildhoodIllness(EntityID = 1, page = 1, pageSize = 100, returnVaccinationChildhoodIllnessID = True, returnChildhoodIllnessID = False, returnCreatedTime = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationChildhoodIllness/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVaccinationChildhoodIllness(VaccinationChildhoodIllnessID, EntityID = 1, returnreturnVaccinationChildhoodIllnessID = False, returnreturnChildhoodIllnessID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVaccinationID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationChildhoodIllness/" + str(VaccinationChildhoodIllnessID), verb = "get", params_list = params_list)

	return(response)

def deleteVaccinationChildhoodIllness(VaccinationChildhoodIllnessID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationChildhoodIllness/" + str(VaccinationChildhoodIllnessID), verb = "delete")

	return(response)

def getEveryVaccinationWaiver(EntityID = 1, page = 1, pageSize = 100, returnVaccinationWaiverID = True, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationID = False, returnWaiverID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationWaiver/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVaccinationWaiver(VaccinationWaiverID, EntityID = 1, returnreturnVaccinationWaiverID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVaccinationID = False, returnreturnWaiverID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationWaiver/" + str(VaccinationWaiverID), verb = "get", params_list = params_list)

	return(response)

def deleteVaccinationWaiver(VaccinationWaiverID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationWaiver/" + str(VaccinationWaiverID), verb = "delete")

	return(response)

def getEveryVaccinationYear(EntityID = 1, page = 1, pageSize = 100, returnVaccinationYearID = True, returnCreatedTime = False, returnIsDistrictDefined = False, returnIsLiveVaccination = False, returnLiveVaccinationDoseIntervalDays = False, returnLiveVaccinationGracePeriodDays = False, returnModifiedTime = False, returnProcessByType = False, returnProcessByTypeCode = False, returnRequiredAgeHigh = False, returnRequiredAgeHighDescription = False, returnRequiredAgeHighUnitType = False, returnRequiredAgeHighUnitTypeCode = False, returnRequiredAgeLow = False, returnRequiredAgeLowDescription = False, returnRequiredAgeLowUnitType = False, returnRequiredAgeLowUnitTypeCode = False, returnSchoolYearID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationID = False, returnVaccinationYearIDClonedFrom = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVaccinationYear(VaccinationYearID, EntityID = 1, returnreturnVaccinationYearID = False, returnreturnCreatedTime = False, returnreturnIsDistrictDefined = False, returnreturnIsLiveVaccination = False, returnreturnLiveVaccinationDoseIntervalDays = False, returnreturnLiveVaccinationGracePeriodDays = False, returnreturnModifiedTime = False, returnreturnProcessByType = False, returnreturnProcessByTypeCode = False, returnreturnRequiredAgeHigh = False, returnreturnRequiredAgeHighDescription = False, returnreturnRequiredAgeHighUnitType = False, returnreturnRequiredAgeHighUnitTypeCode = False, returnreturnRequiredAgeLow = False, returnreturnRequiredAgeLowDescription = False, returnreturnRequiredAgeLowUnitType = False, returnreturnRequiredAgeLowUnitTypeCode = False, returnreturnSchoolYearID = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVaccinationID = False, returnreturnVaccinationYearIDClonedFrom = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationYear/" + str(VaccinationYearID), verb = "get", params_list = params_list)

	return(response)

def deleteVaccinationYear(VaccinationYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationYear/" + str(VaccinationYearID), verb = "delete")

	return(response)

def getEveryVaccinationYearComplianceSchedule(EntityID = 1, page = 1, pageSize = 100, returnVaccinationYearComplianceScheduleID = True, returnComplianceScheduleID = False, returnCreatedTime = False, returnIsDistrictDefined = False, returnModifiedTime = False, returnRank = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationYearComplianceScheduleIDClonedFrom = False, returnVaccinationYearID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationYearComplianceSchedule/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVaccinationYearComplianceSchedule(VaccinationYearComplianceScheduleID, EntityID = 1, returnreturnVaccinationYearComplianceScheduleID = False, returnreturnComplianceScheduleID = False, returnreturnCreatedTime = False, returnreturnIsDistrictDefined = False, returnreturnModifiedTime = False, returnreturnRank = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVaccinationYearComplianceScheduleIDClonedFrom = False, returnreturnVaccinationYearID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationYearComplianceSchedule/" + str(VaccinationYearComplianceScheduleID), verb = "get", params_list = params_list)

	return(response)

def deleteVaccinationYearComplianceSchedule(VaccinationYearComplianceScheduleID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationYearComplianceSchedule/" + str(VaccinationYearComplianceScheduleID), verb = "delete")

	return(response)

def getEveryVaccinationYearComplianceScheduleRule(EntityID = 1, page = 1, pageSize = 100, returnVaccinationYearComplianceScheduleRuleID = True, returnComplianceScheduleRuleID = False, returnCreatedTime = False, returnDoseIntervalID = False, returnModifiedTime = False, returnRuleType = False, returnRuleTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationYearComplianceScheduleID = False, returnVaccinationYearComplianceScheduleRuleIDClonedFrom = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationYearComplianceScheduleRule/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVaccinationYearComplianceScheduleRule(VaccinationYearComplianceScheduleRuleID, EntityID = 1, returnreturnVaccinationYearComplianceScheduleRuleID = False, returnreturnComplianceScheduleRuleID = False, returnreturnCreatedTime = False, returnreturnDoseIntervalID = False, returnreturnModifiedTime = False, returnreturnRuleType = False, returnreturnRuleTypeCode = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVaccinationYearComplianceScheduleID = False, returnreturnVaccinationYearComplianceScheduleRuleIDClonedFrom = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationYearComplianceScheduleRule/" + str(VaccinationYearComplianceScheduleRuleID), verb = "get", params_list = params_list)

	return(response)

def deleteVaccinationYearComplianceScheduleRule(VaccinationYearComplianceScheduleRuleID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationYearComplianceScheduleRule/" + str(VaccinationYearComplianceScheduleRuleID), verb = "delete")

	return(response)

def getEveryVaccine(EntityID = 1, page = 1, pageSize = 100, returnVaccineID = True, returnCode = False, returnCPTCode = False, returnCPTDescription = False, returnCreatedTime = False, returnCVXCode = False, returnCVXFullName = False, returnCVXName = False, returnDescription = False, returnDisplayCode = False, returnDisplayDescription = False, returnDisplayOrder = False, returnIsLiveVaccine = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUsedByDistrict = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Vaccine/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVaccine(VaccineID, EntityID = 1, returnreturnVaccineID = False, returnreturnCode = False, returnreturnCPTCode = False, returnreturnCPTDescription = False, returnreturnCreatedTime = False, returnreturnCVXCode = False, returnreturnCVXFullName = False, returnreturnCVXName = False, returnreturnDescription = False, returnreturnDisplayCode = False, returnreturnDisplayDescription = False, returnreturnDisplayOrder = False, returnreturnIsLiveVaccine = False, returnreturnModifiedTime = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUsedByDistrict = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Vaccine/" + str(VaccineID), verb = "get", params_list = params_list)

	return(response)

def deleteVaccine(VaccineID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Vaccine/" + str(VaccineID), verb = "delete")

	return(response)

def getEveryVaccineContent(EntityID = 1, page = 1, pageSize = 100, returnVaccineContentID = True, returnCreatedTime = False, returnIsDistrictDefined = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationID = False, returnVaccineID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccineContent/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVaccineContent(VaccineContentID, EntityID = 1, returnreturnVaccineContentID = False, returnreturnCreatedTime = False, returnreturnIsDistrictDefined = False, returnreturnModifiedTime = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVaccinationID = False, returnreturnVaccineID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccineContent/" + str(VaccineContentID), verb = "get", params_list = params_list)

	return(response)

def deleteVaccineContent(VaccineContentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccineContent/" + str(VaccineContentID), verb = "delete")

	return(response)

def getEveryVisionComment(EntityID = 1, page = 1, pageSize = 100, returnVisionCommentID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionComment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVisionComment(VisionCommentID, EntityID = 1, returnreturnVisionCommentID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionComment/" + str(VisionCommentID), verb = "get", params_list = params_list)

	return(response)

def deleteVisionComment(VisionCommentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionComment/" + str(VisionCommentID), verb = "delete")

	return(response)

def getEveryVisionCorrectiveLens(EntityID = 1, page = 1, pageSize = 100, returnVisionCorrectiveLensID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionCorrectiveLens/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVisionCorrectiveLens(VisionCorrectiveLensID, EntityID = 1, returnreturnVisionCorrectiveLensID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionCorrectiveLens/" + str(VisionCorrectiveLensID), verb = "get", params_list = params_list)

	return(response)

def deleteVisionCorrectiveLens(VisionCorrectiveLensID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionCorrectiveLens/" + str(VisionCorrectiveLensID), verb = "delete")

	return(response)

def getEveryVisionGuardianNotification(EntityID = 1, page = 1, pageSize = 100, returnVisionGuardianNotificationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionGuardianNotification/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVisionGuardianNotification(VisionGuardianNotificationID, EntityID = 1, returnreturnVisionGuardianNotificationID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionGuardianNotification/" + str(VisionGuardianNotificationID), verb = "get", params_list = params_list)

	return(response)

def deleteVisionGuardianNotification(VisionGuardianNotificationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionGuardianNotification/" + str(VisionGuardianNotificationID), verb = "delete")

	return(response)

def getEveryVisionGuardianResponse(EntityID = 1, page = 1, pageSize = 100, returnVisionGuardianResponseID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVisionGuardianResponse(VisionGuardianResponseID, EntityID = 1, returnreturnVisionGuardianResponseID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionGuardianResponse/" + str(VisionGuardianResponseID), verb = "get", params_list = params_list)

	return(response)

def deleteVisionGuardianResponse(VisionGuardianResponseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionGuardianResponse/" + str(VisionGuardianResponseID), verb = "delete")

	return(response)

def getEveryVisionObservation(EntityID = 1, page = 1, pageSize = 100, returnVisionObservationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionObservation/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVisionObservation(VisionObservationID, EntityID = 1, returnreturnVisionObservationID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionObservation/" + str(VisionObservationID), verb = "get", params_list = params_list)

	return(response)

def deleteVisionObservation(VisionObservationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionObservation/" + str(VisionObservationID), verb = "delete")

	return(response)

def getEveryVisionReferralReason(EntityID = 1, page = 1, pageSize = 100, returnVisionReferralReasonID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionReferralReason/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVisionReferralReason(VisionReferralReasonID, EntityID = 1, returnreturnVisionReferralReasonID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionReferralReason/" + str(VisionReferralReasonID), verb = "get", params_list = params_list)

	return(response)

def deleteVisionReferralReason(VisionReferralReasonID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionReferralReason/" + str(VisionReferralReasonID), verb = "delete")

	return(response)

def getEveryVisionReferralResult(EntityID = 1, page = 1, pageSize = 100, returnVisionReferralResultID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionReferralResult/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVisionReferralResult(VisionReferralResultID, EntityID = 1, returnreturnVisionReferralResultID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionReferralResult/" + str(VisionReferralResultID), verb = "get", params_list = params_list)

	return(response)

def deleteVisionReferralResult(VisionReferralResultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionReferralResult/" + str(VisionReferralResultID), verb = "delete")

	return(response)

def getEveryVisionScreening(EntityID = 1, page = 1, pageSize = 100, returnVisionScreeningID = True, returnColorBlindnessTestResult = False, returnColorBlindnessTestResultCode = False, returnCreatedTime = False, returnDistrictID = False, returnFarVisionCorrectedLeftEye = False, returnFarVisionCorrectedRightEye = False, returnFarVisionScreeningDistance = False, returnFarVisionScreeningResult = False, returnFarVisionScreeningResultCode = False, returnFarVisionUncorrectedLeftEye = False, returnFarVisionUncorrectedRightEye = False, returnFittingDate = False, returnHealthProfessionalIDExaminedBy = False, returnIsVoid = False, returnModifiedTime = False, returnMuscleBalanceTestResult = False, returnMuscleBalanceTestResultCode = False, returnNameID = False, returnNameOfficeVisitID = False, returnNearVisionCorrectedLeftEye = False, returnNearVisionCorrectedRightEye = False, returnNearVisionScreeningDistance = False, returnNearVisionScreeningResult = False, returnNearVisionScreeningResultCode = False, returnNearVisionUncorrectedLeftEye = False, returnNearVisionUncorrectedRightEye = False, returnOverallScreeningResult = False, returnOverallScreeningResultCode = False, returnReScreen = False, returnSchoolYearID = False, returnScreeningDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVisionCorrectedPriorToExam = False, returnVisionCorrectiveLensID = False, returnVoidedTime = False, returnVoidNote = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreening/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVisionScreening(VisionScreeningID, EntityID = 1, returnreturnVisionScreeningID = False, returnreturnColorBlindnessTestResult = False, returnreturnColorBlindnessTestResultCode = False, returnreturnCreatedTime = False, returnreturnDistrictID = False, returnreturnFarVisionCorrectedLeftEye = False, returnreturnFarVisionCorrectedRightEye = False, returnreturnFarVisionScreeningDistance = False, returnreturnFarVisionScreeningResult = False, returnreturnFarVisionScreeningResultCode = False, returnreturnFarVisionUncorrectedLeftEye = False, returnreturnFarVisionUncorrectedRightEye = False, returnreturnFittingDate = False, returnreturnHealthProfessionalIDExaminedBy = False, returnreturnIsVoid = False, returnreturnModifiedTime = False, returnreturnMuscleBalanceTestResult = False, returnreturnMuscleBalanceTestResultCode = False, returnreturnNameID = False, returnreturnNameOfficeVisitID = False, returnreturnNearVisionCorrectedLeftEye = False, returnreturnNearVisionCorrectedRightEye = False, returnreturnNearVisionScreeningDistance = False, returnreturnNearVisionScreeningResult = False, returnreturnNearVisionScreeningResultCode = False, returnreturnNearVisionUncorrectedLeftEye = False, returnreturnNearVisionUncorrectedRightEye = False, returnreturnOverallScreeningResult = False, returnreturnOverallScreeningResultCode = False, returnreturnReScreen = False, returnreturnSchoolYearID = False, returnreturnScreeningDate = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserIDVoidedBy = False, returnreturnVisionCorrectedPriorToExam = False, returnreturnVisionCorrectiveLensID = False, returnreturnVoidedTime = False, returnreturnVoidNote = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreening/" + str(VisionScreeningID), verb = "get", params_list = params_list)

	return(response)

def deleteVisionScreening(VisionScreeningID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreening/" + str(VisionScreeningID), verb = "delete")

	return(response)

def getEveryVisionScreeningComment(EntityID = 1, page = 1, pageSize = 100, returnVisionScreeningCommentID = True, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVisionCommentID = False, returnVisionScreeningID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningComment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVisionScreeningComment(VisionScreeningCommentID, EntityID = 1, returnreturnVisionScreeningCommentID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVisionCommentID = False, returnreturnVisionScreeningID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningComment/" + str(VisionScreeningCommentID), verb = "get", params_list = params_list)

	return(response)

def deleteVisionScreeningComment(VisionScreeningCommentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningComment/" + str(VisionScreeningCommentID), verb = "delete")

	return(response)

def getEveryVisionScreeningNote(EntityID = 1, page = 1, pageSize = 100, returnVisionScreeningNoteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVisionScreeningID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVisionScreeningNote(VisionScreeningNoteID, EntityID = 1, returnreturnVisionScreeningNoteID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVisionScreeningID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningNote/" + str(VisionScreeningNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteVisionScreeningNote(VisionScreeningNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningNote/" + str(VisionScreeningNoteID), verb = "delete")

	return(response)

def getEveryVisionScreeningObservation(EntityID = 1, page = 1, pageSize = 100, returnVisionScreeningObservationID = True, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVisionObservationID = False, returnVisionScreeningID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningObservation/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVisionScreeningObservation(VisionScreeningObservationID, EntityID = 1, returnreturnVisionScreeningObservationID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVisionObservationID = False, returnreturnVisionScreeningID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningObservation/" + str(VisionScreeningObservationID), verb = "get", params_list = params_list)

	return(response)

def deleteVisionScreeningObservation(VisionScreeningObservationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningObservation/" + str(VisionScreeningObservationID), verb = "delete")

	return(response)

def getEveryVisionScreeningReferral(EntityID = 1, page = 1, pageSize = 100, returnVisionScreeningReferralID = True, returnCompletionDate = False, returnCreatedTime = False, returnHealthProfessionalIDReferredBy = False, returnHealthProfessionalIDReferredTo = False, returnModifiedTime = False, returnReferralCompleted = False, returnReferralDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVisionGuardianNotificationID = False, returnVisionGuardianResponseID = False, returnVisionReferralReasonID = False, returnVisionReferralResultID = False, returnVisionScreeningID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningReferral/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVisionScreeningReferral(VisionScreeningReferralID, EntityID = 1, returnreturnVisionScreeningReferralID = False, returnreturnCompletionDate = False, returnreturnCreatedTime = False, returnreturnHealthProfessionalIDReferredBy = False, returnreturnHealthProfessionalIDReferredTo = False, returnreturnModifiedTime = False, returnreturnReferralCompleted = False, returnreturnReferralDate = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVisionGuardianNotificationID = False, returnreturnVisionGuardianResponseID = False, returnreturnVisionReferralReasonID = False, returnreturnVisionReferralResultID = False, returnreturnVisionScreeningID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningReferral/" + str(VisionScreeningReferralID), verb = "get", params_list = params_list)

	return(response)

def deleteVisionScreeningReferral(VisionScreeningReferralID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningReferral/" + str(VisionScreeningReferralID), verb = "delete")

	return(response)

def getEveryVisionScreeningSecuredNote(EntityID = 1, page = 1, pageSize = 100, returnVisionScreeningSecuredNoteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVisionScreeningID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningSecuredNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVisionScreeningSecuredNote(VisionScreeningSecuredNoteID, EntityID = 1, returnreturnVisionScreeningSecuredNoteID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVisionScreeningID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningSecuredNote/" + str(VisionScreeningSecuredNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteVisionScreeningSecuredNote(VisionScreeningSecuredNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningSecuredNote/" + str(VisionScreeningSecuredNoteID), verb = "delete")

	return(response)

def getEveryVitalSign(EntityID = 1, page = 1, pageSize = 100, returnVitalSignID = True, returnBloodPressureDiastolic = False, returnBloodPressureSystolic = False, returnCreatedTime = False, returnModifiedTime = False, returnNameOfficeVisitID = False, returnPhysicalScreeningID = False, returnPulseRate = False, returnRespiration = False, returnSaturationOfPeripheralOxygen = False, returnTemperature = False, returnTimeTaken = False, returnTimeTakenDate = False, returnTimeTakenTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VitalSign/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVitalSign(VitalSignID, EntityID = 1, returnreturnVitalSignID = False, returnreturnBloodPressureDiastolic = False, returnreturnBloodPressureSystolic = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNameOfficeVisitID = False, returnreturnPhysicalScreeningID = False, returnreturnPulseRate = False, returnreturnRespiration = False, returnreturnSaturationOfPeripheralOxygen = False, returnreturnTemperature = False, returnreturnTimeTaken = False, returnreturnTimeTakenDate = False, returnreturnTimeTakenTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VitalSign/" + str(VitalSignID), verb = "get", params_list = params_list)

	return(response)

def deleteVitalSign(VitalSignID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VitalSign/" + str(VitalSignID), verb = "delete")

	return(response)

def getEveryWaiver(EntityID = 1, page = 1, pageSize = 100, returnWaiverID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnExpirationType = False, returnExpirationTypeCode = False, returnExpireUnit = False, returnExpireUnitCode = False, returnExpireValue = False, returnIsActive = False, returnModifiedTime = False, returnRestrictVaccinations = False, returnUseInStateReporting = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaiverType = False, returnWaiverTypeCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Waiver/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getWaiver(WaiverID, EntityID = 1, returnreturnWaiverID = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnExpirationType = False, returnreturnExpirationTypeCode = False, returnreturnExpireUnit = False, returnreturnExpireUnitCode = False, returnreturnExpireValue = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnRestrictVaccinations = False, returnreturnUseInStateReporting = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWaiverType = False, returnreturnWaiverTypeCode = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Waiver/" + str(WaiverID), verb = "get", params_list = params_list)

	return(response)

def deleteWaiver(WaiverID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Waiver/" + str(WaiverID), verb = "delete")

	return(response)