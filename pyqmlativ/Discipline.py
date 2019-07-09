# This module contains Discipline functions.

from . import make_request

def getActionAttendanceType(ActionAttendanceTypeID, EntityID = 1, returnActionID = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionAttendanceType/" + str(ActionAttendanceTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteActionAttendanceType(ActionAttendanceTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionAttendanceType/" + str(ActionAttendanceTypeID), verb = "delete")

	return(response)

def getAction(ActionID, EntityID = 1, returnActionIDClonedFrom = False, returnActionMNID = False, returnActionTypeID = False, returnCode = False, returnCodeDescription = False, returnCreateAttendanceForActionDetail = False, returnCreatedTime = False, returnDefaultDuration = False, returnDefaultLocationID = False, returnDescription = False, returnDistrictID = False, returnDurationType = False, returnDurationTypeCode = False, returnFederalDisciplineCategoryID = False, returnModifiedTime = False, returnRestraintSeclusion = False, returnRestraintSeclusionCode = False, returnSchoolYearID = False, returnStateActionTypeMNID = False, returnSuppressCreationOfActionDetails = False, returnTransferToAlternativeSchool = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Action/" + str(ActionID), verb = "get", params_list = params_list)

	return(response)

def deleteAction(ActionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Action/" + str(ActionID), verb = "delete")

	return(response)

def getActionType(ActionTypeID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnIsInvalid = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValidYearHigh = False, returnValidYearLow = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionType/" + str(ActionTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteActionType(ActionTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionType/" + str(ActionTypeID), verb = "delete")

	return(response)

def getConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, returnAllowActionRecommendationsOnReferrals = False, returnAllowActionTypeUpdate = False, returnAllowDurationTypeUpdate = False, returnAllowOnlyOneOffensePerIncident = False, returnAllowUseOfWarning = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDaysToDelayDisplayOfIncidentsInFamilyAndStudentAccess = False, returnDefaultActionValueFromPreviousPerson = False, returnDefaultDisciplineScreenDateAndTimes = False, returnDefaultOffenseValueFromPreviousPerson = False, returnDisplayInvolvedPersonsFromAllEntities = False, returnDisplayStudentOffensesForAllEntities = False, returnDisplayWarningsInFamilyAndStudentAccess = False, returnDistrictID = False, returnModifiedTime = False, returnRestartIncidentNumberThisYear = False, returnSchoolYearID = False, returnUseIncidentBuildingAndRoom = False, returnUsePerceivedMotivation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigDistrictYear(ConfigDistrictYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "delete")

	return(response)

def getConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, returnActionStatusDefaultValue = False, returnActionStatusDefaultValueCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDefaultActionStatusCode = False, returnDetentionsOnFri = False, returnDetentionsOnMon = False, returnDetentionsOnSat = False, returnDetentionsOnSun = False, returnDetentionsOnThu = False, returnDetentionsOnTue = False, returnDetentionsOnWed = False, returnEntityGroupKey = False, returnEntityID = False, returnExpulsionsOnFri = False, returnExpulsionsOnMon = False, returnExpulsionsOnSat = False, returnExpulsionsOnSun = False, returnExpulsionsOnThu = False, returnExpulsionsOnTue = False, returnExpulsionsOnWed = False, returnIncludeDisciplinaryActionAndDetailsOnLetter = False, returnIncludeGradeLevelOnLetter = False, returnIncludeParentNameAndOrPhoneNumberOnLetter = False, returnIncludeSchoolOrCampusOnLetter = False, returnIncludeSignatureLineForOfficeOnLetter = False, returnIncludeSignatureLineForParentOnLetter = False, returnIncludeSignatureLineForStudentOnLetter = False, returnIncludeStudentNameAndOrNumberOnLetter = False, returnInSchoolSuspensionsOnFri = False, returnInSchoolSuspensionsOnMon = False, returnInSchoolSuspensionsOnSat = False, returnInSchoolSuspensionsOnSun = False, returnInSchoolSuspensionsOnThu = False, returnInSchoolSuspensionsOnTue = False, returnInSchoolSuspensionsOnWed = False, returnModifiedTime = False, returnOutOfSchoolSuspensionsOnFri = False, returnOutOfSchoolSuspensionsOnMon = False, returnOutOfSchoolSuspensionsOnSat = False, returnOutOfSchoolSuspensionsOnSun = False, returnOutOfSchoolSuspensionsOnThu = False, returnOutOfSchoolSuspensionsOnTue = False, returnOutOfSchoolSuspensionsOnWed = False, returnSchoolYearID = False, returnTardyKioskDisciplineSlipTitle = False, returnUseAlternateActionDetails = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "delete")

	return(response)

def getConfigEntityYear(ConfigEntityYearID, EntityID = 1, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityYear/" + str(ConfigEntityYearID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigEntityYear(ConfigEntityYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityYear/" + str(ConfigEntityYearID), verb = "delete")

	return(response)

def getConfigSystem(ConfigSystemID, EntityID = 1, returnAllowIncidentSuppression = False, returnCreatedTime = False, returnModifiedTime = False, returnReportIDDisciplineLetter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigSystem/" + str(ConfigSystemID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigSystem(ConfigSystemID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigSystem/" + str(ConfigSystemID), verb = "delete")

	return(response)

def getDisciplineLetterRunHistory(DisciplineLetterRunHistoryID, EntityID = 1, returnCreatedTime = False, returnDate = False, returnDisciplineLetterTemplateID = False, returnEndDate = False, returnEntityID = False, returnFilterType = False, returnFilterTypeCode = False, returnGracePeriod = False, returnIncidentType = False, returnIncidentTypeCode = False, returnIsActive = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnReportRunInfoID = False, returnRunDescription = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistory/" + str(DisciplineLetterRunHistoryID), verb = "get", params_list = params_list)

	return(response)

def deleteDisciplineLetterRunHistory(DisciplineLetterRunHistoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistory/" + str(DisciplineLetterRunHistoryID), verb = "delete")

	return(response)

def getDisciplineLetterRunHistoryAction(DisciplineLetterRunHistoryActionID, EntityID = 1, returnActionID = False, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryAction/" + str(DisciplineLetterRunHistoryActionID), verb = "get", params_list = params_list)

	return(response)

def deleteDisciplineLetterRunHistoryAction(DisciplineLetterRunHistoryActionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryAction/" + str(DisciplineLetterRunHistoryActionID), verb = "delete")

	return(response)

def getDisciplineLetterRunHistoryOffense(DisciplineLetterRunHistoryOffenseID, EntityID = 1, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryOffense/" + str(DisciplineLetterRunHistoryOffenseID), verb = "get", params_list = params_list)

	return(response)

def deleteDisciplineLetterRunHistoryOffense(DisciplineLetterRunHistoryOffenseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryOffense/" + str(DisciplineLetterRunHistoryOffenseID), verb = "delete")

	return(response)

def getDisciplineLetterTemplate(DisciplineLetterTemplateID, EntityID = 1, returnAdvisorNameFormat = False, returnAdvisorNameFormatCode = False, returnBody = False, returnColumnHeaderLabel1 = False, returnColumnHeaderLabel10 = False, returnColumnHeaderLabel2 = False, returnColumnHeaderLabel3 = False, returnColumnHeaderLabel4 = False, returnColumnHeaderLabel5 = False, returnColumnHeaderLabel6 = False, returnColumnHeaderLabel7 = False, returnColumnHeaderLabel8 = False, returnColumnHeaderLabel9 = False, returnCreatedTime = False, returnDescription = False, returnDisciplineLetterTemplateIDClonedFrom = False, returnDistrictID = False, returnFooter = False, returnForCurrentEntity = False, returnGuardianNameFormat = False, returnGuardianNameFormatCode = False, returnHasLogo = False, returnHeader = False, returnIsDefault = False, returnMediaIDLogo = False, returnModifiedTime = False, returnPrintSingleColumn1 = False, returnPrintSingleColumn10 = False, returnPrintSingleColumn2 = False, returnPrintSingleColumn3 = False, returnPrintSingleColumn4 = False, returnPrintSingleColumn5 = False, returnPrintSingleColumn6 = False, returnPrintSingleColumn7 = False, returnPrintSingleColumn8 = False, returnPrintSingleColumn9 = False, returnSchoolYearID = False, returnStudentNameFormat = False, returnStudentNameFormatCode = False, returnSuperintendentNameFormat = False, returnSuperintendentNameFormatCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplate/" + str(DisciplineLetterTemplateID), verb = "get", params_list = params_list)

	return(response)

def deleteDisciplineLetterTemplate(DisciplineLetterTemplateID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplate/" + str(DisciplineLetterTemplateID), verb = "delete")

	return(response)

def getDisciplineLetterTemplateEntity(DisciplineLetterTemplateEntityID, EntityID = 1, returnCreatedTime = False, returnDisciplineLetterTemplateID = False, returnEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateEntity/" + str(DisciplineLetterTemplateEntityID), verb = "get", params_list = params_list)

	return(response)

def deleteDisciplineLetterTemplateEntity(DisciplineLetterTemplateEntityID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateEntity/" + str(DisciplineLetterTemplateEntityID), verb = "delete")

	return(response)

def getDisciplineLetterTemplateField(DisciplineLetterTemplateFieldID, EntityID = 1, returnCreatedTime = False, returnDescription = False, returnFieldPath = False, returnFriendlyName = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateField/" + str(DisciplineLetterTemplateFieldID), verb = "get", params_list = params_list)

	return(response)

def deleteDisciplineLetterTemplateField(DisciplineLetterTemplateFieldID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateField/" + str(DisciplineLetterTemplateFieldID), verb = "delete")

	return(response)

def getDisciplineLetterTemplateHeaderColumn(DisciplineLetterTemplateHeaderColumnID, EntityID = 1, returnColumnNumber = False, returnCreatedTime = False, returnDisciplineLetterTemplateHeaderColumnIDClonedFrom = False, returnDisciplineLetterTemplateHeaderRowID = False, returnFieldType = False, returnFieldTypeCode = False, returnFreeformText = False, returnLabelOverride = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderColumn/" + str(DisciplineLetterTemplateHeaderColumnID), verb = "get", params_list = params_list)

	return(response)

def deleteDisciplineLetterTemplateHeaderColumn(DisciplineLetterTemplateHeaderColumnID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderColumn/" + str(DisciplineLetterTemplateHeaderColumnID), verb = "delete")

	return(response)

def getDisciplineLetterTemplateHeaderRow(DisciplineLetterTemplateHeaderRowID, EntityID = 1, returnColumnCount = False, returnCreatedTime = False, returnDisciplineLetterTemplateHeaderRowIDClonedFrom = False, returnDisciplineLetterTemplateID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderRow/" + str(DisciplineLetterTemplateHeaderRowID), verb = "get", params_list = params_list)

	return(response)

def deleteDisciplineLetterTemplateHeaderRow(DisciplineLetterTemplateHeaderRowID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderRow/" + str(DisciplineLetterTemplateHeaderRowID), verb = "delete")

	return(response)

def getDrug(DrugID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnDrugIDClonedFrom = False, returnDrugMNID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateDrugTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Drug/" + str(DrugID), verb = "get", params_list = params_list)

	return(response)

def deleteDrug(DrugID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Drug/" + str(DrugID), verb = "delete")

	return(response)

def getIncident(IncidentID, EntityID = 1, returnActionIDRecommended = False, returnBuildingID = False, returnCreatedTime = False, returnDamageCost = False, returnDateTime = False, returnDateTimeDate = False, returnDateTimeTime = False, returnDescription = False, returnDistrictID = False, returnEntityID = False, returnHasActions = False, returnHasActionsForOffenders = False, returnHasDrugs = False, returnHasOpenActions = False, returnHasOverdueActionDetails = False, returnHasWeapons = False, returnIncidentMNID = False, returnIncidentNumber = False, returnIncidentNumberValue = False, returnIsIncidentOrWarning = False, returnIsReferralOrWarning = False, returnIsSuppressed = False, returnLocationID = False, returnModifiedTime = False, returnNumberOfNonEnrolledOffenders = False, returnNumberOfNonEnrolledVictims = False, returnReferredByFreeformName = False, returnReferredByName = False, returnReferredByNameID = False, returnReferredByType = False, returnReferredByTypeCode = False, returnReportedToLawEnforcement = False, returnRoomID = False, returnSchoolYearID = False, returnStateDIRSTimeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Incident/" + str(IncidentID), verb = "get", params_list = params_list)

	return(response)

def deleteIncident(IncidentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Incident/" + str(IncidentID), verb = "delete")

	return(response)

def getIncidentOffense(IncidentOffenseID, EntityID = 1, returnCreatedTime = False, returnHasActions = False, returnHasDrugs = False, returnHasWeapons = False, returnIncidentID = False, returnIsPrimaryOffense = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffense/" + str(IncidentOffenseID), verb = "get", params_list = params_list)

	return(response)

def deleteIncidentOffense(IncidentOffenseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffense/" + str(IncidentOffenseID), verb = "delete")

	return(response)

def getIncidentOffenseNameActionDetail(IncidentOffenseNameActionDetailID, EntityID = 1, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationServed = False, returnDurationServedWithLabel = False, returnDurationToServe = False, returnDurationToServeWithLabel = False, returnIncidentOffenseNameActionID = False, returnIsAlternate = False, returnIsGuardianNotified = False, returnLastAlternate = False, returnLocationID = False, returnModifiedTime = False, returnOverdue = False, returnPartialDayPeriods = False, returnPrintComment = False, returnRenderReissueOption = False, returnRoomID = False, returnScheduledTime = False, returnScheduledTimeDate = False, returnScheduledTimeTime = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetail/" + str(IncidentOffenseNameActionDetailID), verb = "get", params_list = params_list)

	return(response)

def deleteIncidentOffenseNameActionDetail(IncidentOffenseNameActionDetailID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetail/" + str(IncidentOffenseNameActionDetailID), verb = "delete")

	return(response)

def getIncidentOffenseNameActionDetailPeriod(IncidentOffenseNameActionDetailPeriodID, EntityID = 1, returnAttendancePeriodID = False, returnCreatedTime = False, returnIncidentOffenseNameActionDetailID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetailPeriod/" + str(IncidentOffenseNameActionDetailPeriodID), verb = "get", params_list = params_list)

	return(response)

def deleteIncidentOffenseNameActionDetailPeriod(IncidentOffenseNameActionDetailPeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetailPeriod/" + str(IncidentOffenseNameActionDetailPeriodID), verb = "delete")

	return(response)

def getIncidentOffenseNameAction(IncidentOffenseNameActionID, EntityID = 1, returnActionID = False, returnActionTypeID = False, returnActualDurationServed = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateExpulsionExclusionEnds = False, returnDIRSActionExplanation = False, returnDurationServed = False, returnDurationServedOverride = False, returnDurationToServe = False, returnDurationToServeWithLabel = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnExclusionThroughYearEnd = False, returnExpulsionModified = False, returnExpulsionThroughYearEnd = False, returnFirstActionDetailDateNorthEastExport = False, returnIncidentOffenseNameActionMNID = False, returnIncidentOffenseNameID = False, returnIsGuardianNotified = False, returnLastActionDetailDateNorthEastExport = False, returnLocationID = False, returnModifiedTime = False, returnOrderedDate = False, returnOrderedDateAge = False, returnReturnBeforeYearEnd = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDFollowUpOfficer = False, returnStateDIRSAESTypeMNID = False, returnStatus = False, returnStatusCode = False, returnTotalDurationServed = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameAction/" + str(IncidentOffenseNameActionID), verb = "get", params_list = params_list)

	return(response)

def deleteIncidentOffenseNameAction(IncidentOffenseNameActionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameAction/" + str(IncidentOffenseNameActionID), verb = "delete")

	return(response)

def getIncidentOffenseNameDrug(IncidentOffenseNameDrugID, EntityID = 1, returnCreatedTime = False, returnDrugID = False, returnIncidentOffenseNameID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameDrug/" + str(IncidentOffenseNameDrugID), verb = "get", params_list = params_list)

	return(response)

def deleteIncidentOffenseNameDrug(IncidentOffenseNameDrugID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameDrug/" + str(IncidentOffenseNameDrugID), verb = "delete")

	return(response)

def getIncidentOffenseName(IncidentOffenseNameID, EntityID = 1, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnFirstDrugCodeforNorthEastExport = False, returnFreeformName = False, returnHasActions = False, returnHasDangerousWeapons = False, returnHasDrugs = False, returnHasOpenActions = False, returnHasOverdueActionDetails = False, returnHasWeapons = False, returnIncidentOffenseID = False, returnIncidentOffenseNameMNID = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInjuryOccured = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsGuardianNotified = False, returnIsPhysicalAssault = False, returnIsPhysicalAssaultState = False, returnIsStudentOffender = False, returnModifiedTime = False, returnNameID = False, returnNorthEastExportAttendancePeriods = False, returnNorthEastExportOffenseCodes = False, returnOffenderArrestedByLawEnforcement = False, returnOffenseLevelID = False, returnPerceivedMotivationID = False, returnPersonalName = False, returnReportedToLawEnforcement = False, returnStaffIDDisciplineOfficer = False, returnStatement = False, returnStateOffenderActivityMNID = False, returnStateVictimCostMNID = False, returnStateVictimTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWasSeriousBodilyInjury = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseName/" + str(IncidentOffenseNameID), verb = "get", params_list = params_list)

	return(response)

def deleteIncidentOffenseName(IncidentOffenseNameID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseName/" + str(IncidentOffenseNameID), verb = "delete")

	return(response)

def getIncidentOffenseNameReportRunHistory(IncidentOffenseNameReportRunHistoryID, EntityID = 1, returnAttachmentID = False, returnColumnHeaderData1 = False, returnColumnHeaderData10 = False, returnColumnHeaderData2 = False, returnColumnHeaderData3 = False, returnColumnHeaderData4 = False, returnColumnHeaderData5 = False, returnColumnHeaderData6 = False, returnColumnHeaderData7 = False, returnColumnHeaderData8 = False, returnColumnHeaderData9 = False, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnIncidentOffenseNameID = False, returnIsActive = False, returnModifiedTime = False, returnStudentID = False, returnUnboundBody = False, returnUnboundFooter = False, returnUnboundHeader = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameReportRunHistory/" + str(IncidentOffenseNameReportRunHistoryID), verb = "get", params_list = params_list)

	return(response)

def deleteIncidentOffenseNameReportRunHistory(IncidentOffenseNameReportRunHistoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameReportRunHistory/" + str(IncidentOffenseNameReportRunHistoryID), verb = "delete")

	return(response)

def getIncidentOffenseNameWeapon(IncidentOffenseNameWeaponID, EntityID = 1, returnCreatedTime = False, returnGunFoundInTrunk = False, returnGunWasInCase = False, returnGunWasLoaded = False, returnIncidentOffenseNameID = False, returnIncidentOffenseNameWeaponMNID = False, returnMeetsFederalStatuteOfDangerousWeapon = False, returnMeetsStateStatuteOfDangerousWeapon = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameWeapon/" + str(IncidentOffenseNameWeaponID), verb = "get", params_list = params_list)

	return(response)

def deleteIncidentOffenseNameWeapon(IncidentOffenseNameWeaponID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameWeapon/" + str(IncidentOffenseNameWeaponID), verb = "delete")

	return(response)

def getLocation(LocationID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEdFiIncidentLocationID = False, returnLocationMNID = False, returnModifiedTime = False, returnStateIncidentLocationMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Location/" + str(LocationID), verb = "get", params_list = params_list)

	return(response)

def deleteLocation(LocationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Location/" + str(LocationID), verb = "delete")

	return(response)

def getNextIncidentNumber(NextIncidentNumberID, EntityID = 1, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/NextIncidentNumber/" + str(NextIncidentNumberID), verb = "get", params_list = params_list)

	return(response)

def deleteNextIncidentNumber(NextIncidentNumberID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/NextIncidentNumber/" + str(NextIncidentNumberID), verb = "delete")

	return(response)

def getOffense(OffenseID, EntityID = 1, returnAllowActionRecommendations = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDefaultActionID = False, returnDescription = False, returnDistrictID = False, returnFederalOffenseCategoryID = False, returnHarassmentBullying = False, returnHarassmentBullyingCode = False, returnIsDrugRelated = False, returnIsInjuryThreat = False, returnIsWeaponRelated = False, returnModifiedTime = False, returnOffenseIDClonedFrom = False, returnOffenseLevelIDDefault = False, returnRestrictActions = False, returnSchoolYearID = False, returnUseForReferral = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Offense/" + str(OffenseID), verb = "get", params_list = params_list)

	return(response)

def deleteOffense(OffenseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Offense/" + str(OffenseID), verb = "delete")

	return(response)

def getOffenseAction(OffenseActionID, EntityID = 1, returnActionID = False, returnCreatedTime = False, returnIsReferralAction = False, returnModifiedTime = False, returnOffenseActionIDClonedFrom = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseAction/" + str(OffenseActionID), verb = "get", params_list = params_list)

	return(response)

def deleteOffenseAction(OffenseActionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseAction/" + str(OffenseActionID), verb = "delete")

	return(response)

def getOffenseLevel(OffenseLevelID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnOffenseLevelIDClonedFrom = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseLevel/" + str(OffenseLevelID), verb = "get", params_list = params_list)

	return(response)

def deleteOffenseLevel(OffenseLevelID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseLevel/" + str(OffenseLevelID), verb = "delete")

	return(response)

def getPerceivedMotivation(PerceivedMotivationID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnPerceivedMotivationIDClonedFrom = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/PerceivedMotivation/" + str(PerceivedMotivationID), verb = "get", params_list = params_list)

	return(response)

def deletePerceivedMotivation(PerceivedMotivationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/PerceivedMotivation/" + str(PerceivedMotivationID), verb = "delete")

	return(response)

def getTempIncidentOffenseNameAction(TempIncidentOffenseNameActionID, EntityID = 1, returnActionCodeDescription = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnFullName = False, returnInvolvementType = False, returnIsPrimaryOffense = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnStaffIDAuthorizedByName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameAction/" + str(TempIncidentOffenseNameActionID), verb = "get", params_list = params_list)

	return(response)

def deleteTempIncidentOffenseNameAction(TempIncidentOffenseNameActionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameAction/" + str(TempIncidentOffenseNameActionID), verb = "delete")

	return(response)

def getTempIncidentOffenseNameActionDetail(TempIncidentOffenseNameActionDetailID, EntityID = 1, returnActionCodeDescription = False, returnCreateAttendance = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnFullName = False, returnIncidentOffenseNameActionDetailID = False, returnInvolvementType = False, returnIsAlternate = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnNewStatus = False, returnNewStatusCode = False, returnOffenseCodeDescription = False, returnOldStatus = False, returnOldStatusCode = False, returnPartialDayPeriods = False, returnScheduledTime = False, returnTempIncidentOffenseNameActionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetail/" + str(TempIncidentOffenseNameActionDetailID), verb = "get", params_list = params_list)

	return(response)

def deleteTempIncidentOffenseNameActionDetail(TempIncidentOffenseNameActionDetailID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetail/" + str(TempIncidentOffenseNameActionDetailID), verb = "delete")

	return(response)

def getTempIncidentOffenseNameActionDetailRecord(TempIncidentOffenseNameActionDetailRecordID, EntityID = 1, returnBuilding = False, returnBuildingID = False, returnCreatedTime = False, returnDurationServed = False, returnDurationToServe = False, returnDurationType = False, returnIncidentOffenseNameActionID = False, returnIsAlternate = False, returnIsGuardianNotified = False, returnLocation = False, returnLocationID = False, returnModifiedTime = False, returnRoomID = False, returnRoomNumber = False, returnScheduledTime = False, returnStaffFollowUpOfficerName = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetailRecord/" + str(TempIncidentOffenseNameActionDetailRecordID), verb = "get", params_list = params_list)

	return(response)

def deleteTempIncidentOffenseNameActionDetailRecord(TempIncidentOffenseNameActionDetailRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetailRecord/" + str(TempIncidentOffenseNameActionDetailRecordID), verb = "delete")

	return(response)

def getTempIncidentOffenseNameReportRunHistoryRecord(TempIncidentOffenseNameReportRunHistoryRecordID, EntityID = 1, returnColumnHeader1 = False, returnColumnHeader10 = False, returnColumnHeader2 = False, returnColumnHeader3 = False, returnColumnHeader4 = False, returnColumnHeader5 = False, returnColumnHeader6 = False, returnColumnHeader7 = False, returnColumnHeader8 = False, returnColumnHeader9 = False, returnCreatedTime = False, returnDateTime = False, returnIncident = False, returnIncidentNumber = False, returnIncidentOffenseNameID = False, returnModifiedTime = False, returnOffense = False, returnStudentID = False, returnStudentName = False, returnUnboundBody = False, returnUnboundFooter = False, returnUnboundHeader = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameReportRunHistoryRecord/" + str(TempIncidentOffenseNameReportRunHistoryRecordID), verb = "get", params_list = params_list)

	return(response)

def deleteTempIncidentOffenseNameReportRunHistoryRecord(TempIncidentOffenseNameReportRunHistoryRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameReportRunHistoryRecord/" + str(TempIncidentOffenseNameReportRunHistoryRecordID), verb = "delete")

	return(response)

def getWeapon(WeaponID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStatePelletGunTypeMNID = False, returnStateWeaponTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponIDClonedFrom = False, returnWeaponMNID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Weapon/" + str(WeaponID), verb = "get", params_list = params_list)

	return(response)

def deleteWeapon(WeaponID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Weapon/" + str(WeaponID), verb = "delete")

	return(response)