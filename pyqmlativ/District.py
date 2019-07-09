# This module contains District functions.

from . import make_request

def getBuilding(BuildingID, EntityID = 1, returnAccountDistributionString = False, returnAddressID = False, returnBuildingMNID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnFederalNCESSchoolID = False, returnMaximumStudentCount = False, returnMinimumStudentCount = False, returnModifiedTime = False, returnOptimumStudentCount = False, returnParcelNumber = False, returnSTARSchoolNumber = False, returnUnemploymentInsuranceUnitLocation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Building/" + str(BuildingID), verb = "get", params_list = params_list)

	return(response)

def deleteBuilding(BuildingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Building/" + str(BuildingID), verb = "delete")

	return(response)

def getCalendarYear(CalendarYearID, EntityID = 1, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnNumericYear = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/CalendarYear/" + str(CalendarYearID), verb = "get", params_list = params_list)

	return(response)

def deleteCalendarYear(CalendarYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/CalendarYear/" + str(CalendarYearID), verb = "delete")

	return(response)

def getConfigEntityYear(ConfigEntityYearID, EntityID = 1, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/ConfigEntityYear/" + str(ConfigEntityYearID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigEntityYear(ConfigEntityYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/ConfigEntityYear/" + str(ConfigEntityYearID), verb = "delete")

	return(response)

def getDistrictGroup(DistrictGroupID, EntityID = 1, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictGroup/" + str(DistrictGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteDistrictGroup(DistrictGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictGroup/" + str(DistrictGroupID), verb = "delete")

	return(response)

def getDistrict(DistrictID, EntityID = 1, returnBuildingID = False, returnCodeName = False, returnCreatedTime = False, returnDistrictCodeBySchoolYear = False, returnDistrictGroupID = False, returnDistrictMNID = False, returnDistrictNumber = False, returnFaxNumber = False, returnFaxNumberIsInternational = False, returnFormattedPhoneNumber = False, returnModifiedTime = False, returnName = False, returnNCESIDCode = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnRCDTCodeBySchoolYear = False, returnStaffIDSuperintendent = False, returnStateDistrictCode = False, returnStateDistrictMNID = False, returnStateDistrictTypeCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/District/" + str(DistrictID), verb = "get", params_list = params_list)

	return(response)

def deleteDistrict(DistrictID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/District/" + str(DistrictID), verb = "delete")

	return(response)

def getDistrictSchoolYear(DistrictSchoolYearID, EntityID = 1, returnCreatedTime = False, returnDistrictID = False, returnDistrictSchoolYearIDClonedFrom = False, returnEdFiDistrictID = False, returnHarassmentPolicyWebLink = False, returnHasDesegregationPlan = False, returnHasDistanceEducation = False, returnHasEarlyChildhood = False, returnHasEarlyChildhoodNonIDEA = False, returnHasGEDPreparationProgram = False, returnHasHarassmentPolicy = False, returnHasKindergarten = False, returnHasKindergartenFullDayCost = False, returnHasKindergartenFullDayFree = False, returnHasKindergartenPartDayCost = False, returnHasKindergartenPartDayFree = False, returnHasPreschool = False, returnHasPreschoolAllChildren = False, returnHasPreschoolFullDayCost = False, returnHasPreschoolFullDayFree = False, returnHasPreschoolIDEA = False, returnHasPreschoolLowIncome = False, returnHasPreschoolPartDayCost = False, returnHasPreschoolPartDayFree = False, returnHasPreschoolTitleI = False, returnIsCRDCCollectedForSchoolYear = False, returnModifiedTime = False, returnNameIDDisability = False, returnNameIDRace = False, returnNameIDSex = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictSchoolYear/" + str(DistrictSchoolYearID), verb = "get", params_list = params_list)

	return(response)

def deleteDistrictSchoolYear(DistrictSchoolYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictSchoolYear/" + str(DistrictSchoolYearID), verb = "delete")

	return(response)

def getEntityGroup(EntityGroupID, EntityID = 1, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroup/" + str(EntityGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteEntityGroup(EntityGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroup/" + str(EntityGroupID), verb = "delete")

	return(response)

def getEntityGroupEntity(EntityGroupEntityID, EntityID = 1, returnCreatedTime = False, returnEntityGroupID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupEntity/" + str(EntityGroupEntityID), verb = "get", params_list = params_list)

	return(response)

def deleteEntityGroupEntity(EntityGroupEntityID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupEntity/" + str(EntityGroupEntityID), verb = "delete")

	return(response)

def getEntityGroupSetup(EntityGroupSetupID, EntityID = 1, returnCreatedTime = False, returnEffectiveGroupName = False, returnEntityGroupID = False, returnEntityIDPrimary = False, returnHasBeenProcessed = False, returnModifiedTime = False, returnNewGroupName = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetup/" + str(EntityGroupSetupID), verb = "get", params_list = params_list)

	return(response)

def deleteEntityGroupSetup(EntityGroupSetupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetup/" + str(EntityGroupSetupID), verb = "delete")

	return(response)

def getEntityGroupSetupEntity(EntityGroupSetupEntityID, EntityID = 1, returnCreatedTime = False, returnEntityGroupSetupID = False, returnEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupEntity/" + str(EntityGroupSetupEntityID), verb = "get", params_list = params_list)

	return(response)

def deleteEntityGroupSetupEntity(EntityGroupSetupEntityID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupEntity/" + str(EntityGroupSetupEntityID), verb = "delete")

	return(response)

def getEntityGroupSetupRun(EntityGroupSetupRunID, EntityID = 1, returnCreatedTime = False, returnEntityGroupSetupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRun/" + str(EntityGroupSetupRunID), verb = "get", params_list = params_list)

	return(response)

def deleteEntityGroupSetupRun(EntityGroupSetupRunID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRun/" + str(EntityGroupSetupRunID), verb = "delete")

	return(response)

def getEntityGroupSetupRunDetail(EntityGroupSetupRunDetailID, EntityID = 1, returnChangeType = False, returnChangeTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityGroupSetupRunID = False, returnEntityID = False, returnError = False, returnIdentifyingFields = False, returnIsProcessed = False, returnIsUpdated = False, returnModifiedTime = False, returnModule = False, returnNewFieldValues = False, returnNewValues = False, returnObject = False, returnObjectPrimaryKey = False, returnOriginalValues = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRunDetail/" + str(EntityGroupSetupRunDetailID), verb = "get", params_list = params_list)

	return(response)

def deleteEntityGroupSetupRunDetail(EntityGroupSetupRunDetailID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRunDetail/" + str(EntityGroupSetupRunDetailID), verb = "delete")

	return(response)

def getEntity(EntityID, EntityID = 1, returnAllowDualEnrollment = False, returnCampusID = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnDistrictCodeEntityCode = False, returnDistrictID = False, returnEnforceAddressRangeDefaults = False, returnEntityCodeOrCombinedCodesFollettExport = False, returnEntityGroupCount = False, returnEntityIDHash = False, returnEntityMNID = False, returnExternalLinkEntityCount = False, returnIsDistrictWide = False, returnIsSystemWide = False, returnModifiedTime = False, returnName = False, returnReportToState = False, returnSchoolYearIDCurrent = False, returnTotalPlanEntityYears = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Entity/" + str(EntityID), verb = "get", params_list = params_list)

	return(response)

def deleteEntity(EntityID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Entity/" + str(EntityID), verb = "delete")

	return(response)

def getFiscalYear(FiscalYearID, EntityID = 1, returnConflictAccountingUpdates = False, returnConflictAccountsPayableRuns = False, returnConflictAdditionDisposals = False, returnConflictBudgetAmendments = False, returnConflictCashReceiptDeposits = False, returnConflictDepreciations = False, returnConflictInvoices = False, returnConflictJournalEntries = False, returnConflictPayrollRuns = False, returnConflictPurchaseOrders = False, returnConflictWarehouseRequests = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEndDate = False, returnIsClosed = False, returnIsLockedByHR = False, returnModifiedTime = False, returnNumericYear = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/FiscalYear/" + str(FiscalYearID), verb = "get", params_list = params_list)

	return(response)

def deleteFiscalYear(FiscalYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/FiscalYear/" + str(FiscalYearID), verb = "delete")

	return(response)

def getRoom(RoomID, EntityID = 1, returnBuildingCodeRoomNumber = False, returnBuildingID = False, returnCreatedTime = False, returnDescription = False, returnFormattedPhoneNumber = False, returnMaxConcurrentSections = False, returnMaxSeats = False, returnModifiedTime = False, returnPhoneExtension = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnRoomNumber = False, returnRoomNumberDescription = False, returnRoomTypeID = False, returnSquareFootage = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Room/" + str(RoomID), verb = "get", params_list = params_list)

	return(response)

def deleteRoom(RoomID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Room/" + str(RoomID), verb = "delete")

	return(response)

def getRoomType(RoomTypeID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/RoomType/" + str(RoomTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteRoomType(RoomTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/RoomType/" + str(RoomTypeID), verb = "delete")

	return(response)

def getSchoolYear(SchoolYearID, EntityID = 1, returnCreatedTime = False, returnDescription = False, returnIsCurrentYearForProvidedEntity = False, returnIsUpcomingYearForProvidedEntity = False, returnModifiedTime = False, returnNextNumericYear = False, returnNumericYear = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/SchoolYear/" + str(SchoolYearID), verb = "get", params_list = params_list)

	return(response)

def deleteSchoolYear(SchoolYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/SchoolYear/" + str(SchoolYearID), verb = "delete")

	return(response)

def getStateDistrictMN(StateDistrictMNID, EntityID = 1, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnStateDistrictTypeCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/StateDistrictMN/" + str(StateDistrictMNID), verb = "get", params_list = params_list)

	return(response)

def deleteStateDistrictMN(StateDistrictMNID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/District/StateDistrictMN/" + str(StateDistrictMNID), verb = "delete")

	return(response)