# This module contains Discipline functions.

def deleteActionAttendanceType(ActionAttendanceTypeID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/ActionAttendanceType/" + ActionAttendanceTypeID, verb = "delete")

def deleteAction(ActionID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/Action/" + ActionID, verb = "delete")

def deleteActionType(ActionTypeID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/ActionType/" + ActionTypeID, verb = "delete")

def deleteConfigDistrictYear(ConfigDistrictYearID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/ConfigDistrictYear/" + ConfigDistrictYearID, verb = "delete")

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/ConfigEntityGroupYear/" + ConfigEntityGroupYearID, verb = "delete")

def deleteConfigEntityYear(ConfigEntityYearID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/ConfigEntityYear/" + ConfigEntityYearID, verb = "delete")

def deleteConfigSystem(ConfigSystemID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/ConfigSystem/" + ConfigSystemID, verb = "delete")

def deleteDisciplineLetterRunHistory(DisciplineLetterRunHistoryID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/DisciplineLetterRunHistory/" + DisciplineLetterRunHistoryID, verb = "delete")

def deleteDisciplineLetterRunHistoryAction(DisciplineLetterRunHistoryActionID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/DisciplineLetterRunHistoryAction/" + DisciplineLetterRunHistoryActionID, verb = "delete")

def deleteDisciplineLetterRunHistoryOffense(DisciplineLetterRunHistoryOffenseID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/DisciplineLetterRunHistoryOffense/" + DisciplineLetterRunHistoryOffenseID, verb = "delete")

def deleteDisciplineLetterTemplate(DisciplineLetterTemplateID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/DisciplineLetterTemplate/" + DisciplineLetterTemplateID, verb = "delete")

def deleteDisciplineLetterTemplateEntity(DisciplineLetterTemplateEntityID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/DisciplineLetterTemplateEntity/" + DisciplineLetterTemplateEntityID, verb = "delete")

def deleteDisciplineLetterTemplateField(DisciplineLetterTemplateFieldID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/DisciplineLetterTemplateField/" + DisciplineLetterTemplateFieldID, verb = "delete")

def deleteDisciplineLetterTemplateHeaderColumn(DisciplineLetterTemplateHeaderColumnID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/DisciplineLetterTemplateHeaderColumn/" + DisciplineLetterTemplateHeaderColumnID, verb = "delete")

def deleteDisciplineLetterTemplateHeaderRow(DisciplineLetterTemplateHeaderRowID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/DisciplineLetterTemplateHeaderRow/" + DisciplineLetterTemplateHeaderRowID, verb = "delete")

def deleteDrug(DrugID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/Drug/" + DrugID, verb = "delete")

def deleteIncident(IncidentID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/Incident/" + IncidentID, verb = "delete")

def deleteIncidentOffense(IncidentOffenseID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/IncidentOffense/" + IncidentOffenseID, verb = "delete")

def deleteIncidentOffenseNameActionDetail(IncidentOffenseNameActionDetailID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/IncidentOffenseNameActionDetail/" + IncidentOffenseNameActionDetailID, verb = "delete")

def deleteIncidentOffenseNameActionDetailPeriod(IncidentOffenseNameActionDetailPeriodID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/IncidentOffenseNameActionDetailPeriod/" + IncidentOffenseNameActionDetailPeriodID, verb = "delete")

def deleteIncidentOffenseNameAction(IncidentOffenseNameActionID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/IncidentOffenseNameAction/" + IncidentOffenseNameActionID, verb = "delete")

def deleteIncidentOffenseNameDrug(IncidentOffenseNameDrugID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/IncidentOffenseNameDrug/" + IncidentOffenseNameDrugID, verb = "delete")

def deleteIncidentOffenseName(IncidentOffenseNameID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/IncidentOffenseName/" + IncidentOffenseNameID, verb = "delete")

def deleteIncidentOffenseNameReportRunHistory(IncidentOffenseNameReportRunHistoryID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/IncidentOffenseNameReportRunHistory/" + IncidentOffenseNameReportRunHistoryID, verb = "delete")

def deleteIncidentOffenseNameWeapon(IncidentOffenseNameWeaponID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/IncidentOffenseNameWeapon/" + IncidentOffenseNameWeaponID, verb = "delete")

def deleteLocation(LocationID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/Location/" + LocationID, verb = "delete")

def deleteNextIncidentNumber(NextIncidentNumberID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/NextIncidentNumber/" + NextIncidentNumberID, verb = "delete")

def deleteOffense(OffenseID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/Offense/" + OffenseID, verb = "delete")

def deleteOffenseAction(OffenseActionID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/OffenseAction/" + OffenseActionID, verb = "delete")

def deleteOffenseLevel(OffenseLevelID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/OffenseLevel/" + OffenseLevelID, verb = "delete")

def deletePerceivedMotivation(PerceivedMotivationID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/PerceivedMotivation/" + PerceivedMotivationID, verb = "delete")

def deleteTempIncidentOffenseNameAction(TempIncidentOffenseNameActionID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/TempIncidentOffenseNameAction/" + TempIncidentOffenseNameActionID, verb = "delete")

def deleteTempIncidentOffenseNameActionDetail(TempIncidentOffenseNameActionDetailID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/TempIncidentOffenseNameActionDetail/" + TempIncidentOffenseNameActionDetailID, verb = "delete")

def deleteTempIncidentOffenseNameActionDetailRecord(TempIncidentOffenseNameActionDetailRecordID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/TempIncidentOffenseNameActionDetailRecord/" + TempIncidentOffenseNameActionDetailRecordID, verb = "delete")

def deleteTempIncidentOffenseNameReportRunHistoryRecord(TempIncidentOffenseNameReportRunHistoryRecordID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/TempIncidentOffenseNameReportRunHistoryRecord/" + TempIncidentOffenseNameReportRunHistoryRecordID, verb = "delete")

def deleteWeapon(WeaponID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Discipline/Weapon/" + WeaponID, verb = "delete")