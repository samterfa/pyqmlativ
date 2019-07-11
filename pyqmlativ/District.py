# This module contains District functions.

from .Utilities import make_request

import pandas as pd

def getEveryBuilding(EntityID = 1, page = 1, pageSize = 100, returnBuildingID = True, returnAccountDistributionString = False, returnAddressID = False, returnBuildingMNID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnFederalNCESSchoolID = False, returnMaximumStudentCount = False, returnMinimumStudentCount = False, returnModifiedTime = False, returnOptimumStudentCount = False, returnParcelNumber = False, returnSTARSchoolNumber = False, returnUnemploymentInsuranceUnitLocation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Building/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getBuilding(BuildingID, EntityID = 1, returnreturnBuildingID = False, returnreturnAccountDistributionString = False, returnreturnAddressID = False, returnreturnBuildingMNID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnFederalNCESSchoolID = False, returnreturnMaximumStudentCount = False, returnreturnMinimumStudentCount = False, returnreturnModifiedTime = False, returnreturnOptimumStudentCount = False, returnreturnParcelNumber = False, returnreturnSTARSchoolNumber = False, returnreturnUnemploymentInsuranceUnitLocation = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Building/" + str(BuildingID), verb = "get", params_list = params_list)

	return(response)

def deleteBuilding(BuildingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Building/" + str(BuildingID), verb = "delete")

	return(response)

def getEveryCalendarYear(EntityID = 1, page = 1, pageSize = 100, returnCalendarYearID = True, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnNumericYear = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/CalendarYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCalendarYear(CalendarYearID, EntityID = 1, returnreturnCalendarYearID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnModifiedTime = False, returnreturnNumericYear = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/CalendarYear/" + str(CalendarYearID), verb = "get", params_list = params_list)

	return(response)

def deleteCalendarYear(CalendarYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/CalendarYear/" + str(CalendarYearID), verb = "delete")

	return(response)

def getEveryConfigEntityYear(EntityID = 1, page = 1, pageSize = 100, returnConfigEntityYearID = True, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/ConfigEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigEntityYear(ConfigEntityYearID, EntityID = 1, returnreturnConfigEntityYearID = False, returnreturnConfigEntityYearIDClonedFrom = False, returnreturnCreatedTime = False, returnreturnEntityID = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/ConfigEntityYear/" + str(ConfigEntityYearID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigEntityYear(ConfigEntityYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/ConfigEntityYear/" + str(ConfigEntityYearID), verb = "delete")

	return(response)

def getEveryDistrictGroup(EntityID = 1, page = 1, pageSize = 100, returnDistrictGroupID = True, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDistrictGroup(DistrictGroupID, EntityID = 1, returnreturnDistrictGroupID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictGroup/" + str(DistrictGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteDistrictGroup(DistrictGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictGroup/" + str(DistrictGroupID), verb = "delete")

	return(response)

def getEveryDistrict(EntityID = 1, page = 1, pageSize = 100, returnDistrictID = True, returnBuildingID = False, returnCodeName = False, returnCreatedTime = False, returnDistrictCodeBySchoolYear = False, returnDistrictGroupID = False, returnDistrictMNID = False, returnDistrictNumber = False, returnFaxNumber = False, returnFaxNumberIsInternational = False, returnFormattedPhoneNumber = False, returnModifiedTime = False, returnName = False, returnNCESIDCode = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnRCDTCodeBySchoolYear = False, returnStaffIDSuperintendent = False, returnStateDistrictCode = False, returnStateDistrictMNID = False, returnStateDistrictTypeCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/District/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDistrict(DistrictID, EntityID = 1, returnreturnDistrictID = False, returnreturnBuildingID = False, returnreturnCodeName = False, returnreturnCreatedTime = False, returnreturnDistrictCodeBySchoolYear = False, returnreturnDistrictGroupID = False, returnreturnDistrictMNID = False, returnreturnDistrictNumber = False, returnreturnFaxNumber = False, returnreturnFaxNumberIsInternational = False, returnreturnFormattedPhoneNumber = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnNCESIDCode = False, returnreturnPhoneNumber = False, returnreturnPhoneNumberIsInternational = False, returnreturnRCDTCodeBySchoolYear = False, returnreturnStaffIDSuperintendent = False, returnreturnStateDistrictCode = False, returnreturnStateDistrictMNID = False, returnreturnStateDistrictTypeCodeMNID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/District/" + str(DistrictID), verb = "get", params_list = params_list)

	return(response)

def deleteDistrict(DistrictID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/District/" + str(DistrictID), verb = "delete")

	return(response)

def getEveryDistrictSchoolYear(EntityID = 1, page = 1, pageSize = 100, returnDistrictSchoolYearID = True, returnCreatedTime = False, returnDistrictID = False, returnDistrictSchoolYearIDClonedFrom = False, returnEdFiDistrictID = False, returnHarassmentPolicyWebLink = False, returnHasDesegregationPlan = False, returnHasDistanceEducation = False, returnHasEarlyChildhood = False, returnHasEarlyChildhoodNonIDEA = False, returnHasGEDPreparationProgram = False, returnHasHarassmentPolicy = False, returnHasKindergarten = False, returnHasKindergartenFullDayCost = False, returnHasKindergartenFullDayFree = False, returnHasKindergartenPartDayCost = False, returnHasKindergartenPartDayFree = False, returnHasPreschool = False, returnHasPreschoolAllChildren = False, returnHasPreschoolFullDayCost = False, returnHasPreschoolFullDayFree = False, returnHasPreschoolIDEA = False, returnHasPreschoolLowIncome = False, returnHasPreschoolPartDayCost = False, returnHasPreschoolPartDayFree = False, returnHasPreschoolTitleI = False, returnIsCRDCCollectedForSchoolYear = False, returnModifiedTime = False, returnNameIDDisability = False, returnNameIDRace = False, returnNameIDSex = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictSchoolYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDistrictSchoolYear(DistrictSchoolYearID, EntityID = 1, returnreturnDistrictSchoolYearID = False, returnreturnCreatedTime = False, returnreturnDistrictID = False, returnreturnDistrictSchoolYearIDClonedFrom = False, returnreturnEdFiDistrictID = False, returnreturnHarassmentPolicyWebLink = False, returnreturnHasDesegregationPlan = False, returnreturnHasDistanceEducation = False, returnreturnHasEarlyChildhood = False, returnreturnHasEarlyChildhoodNonIDEA = False, returnreturnHasGEDPreparationProgram = False, returnreturnHasHarassmentPolicy = False, returnreturnHasKindergarten = False, returnreturnHasKindergartenFullDayCost = False, returnreturnHasKindergartenFullDayFree = False, returnreturnHasKindergartenPartDayCost = False, returnreturnHasKindergartenPartDayFree = False, returnreturnHasPreschool = False, returnreturnHasPreschoolAllChildren = False, returnreturnHasPreschoolFullDayCost = False, returnreturnHasPreschoolFullDayFree = False, returnreturnHasPreschoolIDEA = False, returnreturnHasPreschoolLowIncome = False, returnreturnHasPreschoolPartDayCost = False, returnreturnHasPreschoolPartDayFree = False, returnreturnHasPreschoolTitleI = False, returnreturnIsCRDCCollectedForSchoolYear = False, returnreturnModifiedTime = False, returnreturnNameIDDisability = False, returnreturnNameIDRace = False, returnreturnNameIDSex = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictSchoolYear/" + str(DistrictSchoolYearID), verb = "get", params_list = params_list)

	return(response)

def deleteDistrictSchoolYear(DistrictSchoolYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictSchoolYear/" + str(DistrictSchoolYearID), verb = "delete")

	return(response)

def getEveryEntityGroup(EntityID = 1, page = 1, pageSize = 100, returnEntityGroupID = True, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEntityGroup(EntityGroupID, EntityID = 1, returnreturnEntityGroupID = False, returnreturnCreatedTime = False, returnreturnDistrictID = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroup/" + str(EntityGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteEntityGroup(EntityGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroup/" + str(EntityGroupID), verb = "delete")

	return(response)

def getEveryEntityGroupEntity(EntityID = 1, page = 1, pageSize = 100, returnEntityGroupEntityID = True, returnCreatedTime = False, returnEntityGroupID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupEntity/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEntityGroupEntity(EntityGroupEntityID, EntityID = 1, returnreturnEntityGroupEntityID = False, returnreturnCreatedTime = False, returnreturnEntityGroupID = False, returnreturnEntityID = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupEntity/" + str(EntityGroupEntityID), verb = "get", params_list = params_list)

	return(response)

def deleteEntityGroupEntity(EntityGroupEntityID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupEntity/" + str(EntityGroupEntityID), verb = "delete")

	return(response)

def getEveryEntityGroupSetup(EntityID = 1, page = 1, pageSize = 100, returnEntityGroupSetupID = True, returnCreatedTime = False, returnEffectiveGroupName = False, returnEntityGroupID = False, returnEntityIDPrimary = False, returnHasBeenProcessed = False, returnModifiedTime = False, returnNewGroupName = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEntityGroupSetup(EntityGroupSetupID, EntityID = 1, returnreturnEntityGroupSetupID = False, returnreturnCreatedTime = False, returnreturnEffectiveGroupName = False, returnreturnEntityGroupID = False, returnreturnEntityIDPrimary = False, returnreturnHasBeenProcessed = False, returnreturnModifiedTime = False, returnreturnNewGroupName = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetup/" + str(EntityGroupSetupID), verb = "get", params_list = params_list)

	return(response)

def deleteEntityGroupSetup(EntityGroupSetupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetup/" + str(EntityGroupSetupID), verb = "delete")

	return(response)

def getEveryEntityGroupSetupEntity(EntityID = 1, page = 1, pageSize = 100, returnEntityGroupSetupEntityID = True, returnCreatedTime = False, returnEntityGroupSetupID = False, returnEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupEntity/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEntityGroupSetupEntity(EntityGroupSetupEntityID, EntityID = 1, returnreturnEntityGroupSetupEntityID = False, returnreturnCreatedTime = False, returnreturnEntityGroupSetupID = False, returnreturnEntityID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupEntity/" + str(EntityGroupSetupEntityID), verb = "get", params_list = params_list)

	return(response)

def deleteEntityGroupSetupEntity(EntityGroupSetupEntityID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupEntity/" + str(EntityGroupSetupEntityID), verb = "delete")

	return(response)

def getEveryEntityGroupSetupRun(EntityID = 1, page = 1, pageSize = 100, returnEntityGroupSetupRunID = True, returnCreatedTime = False, returnEntityGroupSetupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRun/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEntityGroupSetupRun(EntityGroupSetupRunID, EntityID = 1, returnreturnEntityGroupSetupRunID = False, returnreturnCreatedTime = False, returnreturnEntityGroupSetupID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRun/" + str(EntityGroupSetupRunID), verb = "get", params_list = params_list)

	return(response)

def deleteEntityGroupSetupRun(EntityGroupSetupRunID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRun/" + str(EntityGroupSetupRunID), verb = "delete")

	return(response)

def getEveryEntityGroupSetupRunDetail(EntityID = 1, page = 1, pageSize = 100, returnEntityGroupSetupRunDetailID = True, returnChangeType = False, returnChangeTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityGroupSetupRunID = False, returnEntityID = False, returnError = False, returnIdentifyingFields = False, returnIsProcessed = False, returnIsUpdated = False, returnModifiedTime = False, returnModule = False, returnNewFieldValues = False, returnNewValues = False, returnObject = False, returnObjectPrimaryKey = False, returnOriginalValues = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRunDetail/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEntityGroupSetupRunDetail(EntityGroupSetupRunDetailID, EntityID = 1, returnreturnEntityGroupSetupRunDetailID = False, returnreturnChangeType = False, returnreturnChangeTypeCode = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnEntityGroupSetupRunID = False, returnreturnEntityID = False, returnreturnError = False, returnreturnIdentifyingFields = False, returnreturnIsProcessed = False, returnreturnIsUpdated = False, returnreturnModifiedTime = False, returnreturnModule = False, returnreturnNewFieldValues = False, returnreturnNewValues = False, returnreturnObject = False, returnreturnObjectPrimaryKey = False, returnreturnOriginalValues = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRunDetail/" + str(EntityGroupSetupRunDetailID), verb = "get", params_list = params_list)

	return(response)

def deleteEntityGroupSetupRunDetail(EntityGroupSetupRunDetailID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRunDetail/" + str(EntityGroupSetupRunDetailID), verb = "delete")

	return(response)

def getEveryEntity(EntityID = 1, page = 1, pageSize = 100, returnEntityID = True, returnAllowDualEnrollment = False, returnCampusID = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnDistrictCodeEntityCode = False, returnDistrictID = False, returnEnforceAddressRangeDefaults = False, returnEntityCodeOrCombinedCodesFollettExport = False, returnEntityGroupCount = False, returnEntityIDHash = False, returnEntityMNID = False, returnExternalLinkEntityCount = False, returnIsDistrictWide = False, returnIsSystemWide = False, returnModifiedTime = False, returnName = False, returnReportToState = False, returnSchoolYearIDCurrent = False, returnTotalPlanEntityYears = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Entity/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEntity(EntityID, EntityID = 1, returnreturnEntityID = False, returnreturnAllowDualEnrollment = False, returnreturnCampusID = False, returnreturnCode = False, returnreturnCodeName = False, returnreturnCreatedTime = False, returnreturnDistrictCodeEntityCode = False, returnreturnDistrictID = False, returnreturnEnforceAddressRangeDefaults = False, returnreturnEntityCodeOrCombinedCodesFollettExport = False, returnreturnEntityGroupCount = False, returnreturnEntityIDHash = False, returnreturnEntityMNID = False, returnreturnExternalLinkEntityCount = False, returnreturnIsDistrictWide = False, returnreturnIsSystemWide = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnReportToState = False, returnreturnSchoolYearIDCurrent = False, returnreturnTotalPlanEntityYears = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Entity/" + str(EntityID), verb = "get", params_list = params_list)

	return(response)

def deleteEntity(EntityID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Entity/" + str(EntityID), verb = "delete")

	return(response)

def getEveryFiscalYear(EntityID = 1, page = 1, pageSize = 100, returnFiscalYearID = True, returnConflictAccountingUpdates = False, returnConflictAccountsPayableRuns = False, returnConflictAdditionDisposals = False, returnConflictBudgetAmendments = False, returnConflictCashReceiptDeposits = False, returnConflictDepreciations = False, returnConflictInvoices = False, returnConflictJournalEntries = False, returnConflictPayrollRuns = False, returnConflictPurchaseOrders = False, returnConflictWarehouseRequests = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEndDate = False, returnIsClosed = False, returnIsLockedByHR = False, returnModifiedTime = False, returnNumericYear = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/FiscalYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getFiscalYear(FiscalYearID, EntityID = 1, returnreturnFiscalYearID = False, returnreturnConflictAccountingUpdates = False, returnreturnConflictAccountsPayableRuns = False, returnreturnConflictAdditionDisposals = False, returnreturnConflictBudgetAmendments = False, returnreturnConflictCashReceiptDeposits = False, returnreturnConflictDepreciations = False, returnreturnConflictInvoices = False, returnreturnConflictJournalEntries = False, returnreturnConflictPayrollRuns = False, returnreturnConflictPurchaseOrders = False, returnreturnConflictWarehouseRequests = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnEndDate = False, returnreturnIsClosed = False, returnreturnIsLockedByHR = False, returnreturnModifiedTime = False, returnreturnNumericYear = False, returnreturnStartDate = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/FiscalYear/" + str(FiscalYearID), verb = "get", params_list = params_list)

	return(response)

def deleteFiscalYear(FiscalYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/FiscalYear/" + str(FiscalYearID), verb = "delete")

	return(response)

def getEveryRoom(EntityID = 1, page = 1, pageSize = 100, returnRoomID = True, returnBuildingCodeRoomNumber = False, returnBuildingID = False, returnCreatedTime = False, returnDescription = False, returnFormattedPhoneNumber = False, returnMaxConcurrentSections = False, returnMaxSeats = False, returnModifiedTime = False, returnPhoneExtension = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnRoomNumber = False, returnRoomNumberDescription = False, returnRoomTypeID = False, returnSquareFootage = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Room/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getRoom(RoomID, EntityID = 1, returnreturnRoomID = False, returnreturnBuildingCodeRoomNumber = False, returnreturnBuildingID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnFormattedPhoneNumber = False, returnreturnMaxConcurrentSections = False, returnreturnMaxSeats = False, returnreturnModifiedTime = False, returnreturnPhoneExtension = False, returnreturnPhoneNumber = False, returnreturnPhoneNumberIsInternational = False, returnreturnRoomNumber = False, returnreturnRoomNumberDescription = False, returnreturnRoomTypeID = False, returnreturnSquareFootage = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Room/" + str(RoomID), verb = "get", params_list = params_list)

	return(response)

def deleteRoom(RoomID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Room/" + str(RoomID), verb = "delete")

	return(response)

def getEveryRoomType(EntityID = 1, page = 1, pageSize = 100, returnRoomTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/RoomType/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getRoomType(RoomTypeID, EntityID = 1, returnreturnRoomTypeID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/RoomType/" + str(RoomTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteRoomType(RoomTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/RoomType/" + str(RoomTypeID), verb = "delete")

	return(response)

def getEverySchoolYear(EntityID = 1, page = 1, pageSize = 100, returnSchoolYearID = True, returnCreatedTime = False, returnDescription = False, returnIsCurrentYearForProvidedEntity = False, returnIsUpcomingYearForProvidedEntity = False, returnModifiedTime = False, returnNextNumericYear = False, returnNumericYear = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/SchoolYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getSchoolYear(SchoolYearID, EntityID = 1, returnreturnSchoolYearID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnIsCurrentYearForProvidedEntity = False, returnreturnIsUpcomingYearForProvidedEntity = False, returnreturnModifiedTime = False, returnreturnNextNumericYear = False, returnreturnNumericYear = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/SchoolYear/" + str(SchoolYearID), verb = "get", params_list = params_list)

	return(response)

def deleteSchoolYear(SchoolYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/SchoolYear/" + str(SchoolYearID), verb = "delete")

	return(response)

def getEveryStateDistrictMN(EntityID = 1, page = 1, pageSize = 100, returnStateDistrictMNID = True, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnStateDistrictTypeCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/StateDistrictMN/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStateDistrictMN(StateDistrictMNID, EntityID = 1, returnreturnStateDistrictMNID = False, returnreturnCode = False, returnreturnCodeName = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnStateDistrictTypeCodeMNID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/StateDistrictMN/" + str(StateDistrictMNID), verb = "get", params_list = params_list)

	return(response)

def deleteStateDistrictMN(StateDistrictMNID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/StateDistrictMN/" + str(StateDistrictMNID), verb = "delete")

	return(response)