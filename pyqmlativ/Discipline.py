# This module contains Discipline functions.

def deleteActionAttendanceType(ActionAttendanceTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/ActionAttendanceType/" + ActionAttendanceTypeID, verb = "delete")

def deleteAction(ActionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/Action/" + ActionID, verb = "delete")

def deleteActionType(ActionTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/ActionType/" + ActionTypeID, verb = "delete")

def deleteConfigDistrictYear(ConfigDistrictYearID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/ConfigDistrictYear/" + ConfigDistrictYearID, verb = "delete")

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/ConfigEntityGroupYear/" + ConfigEntityGroupYearID, verb = "delete")

def deleteConfigEntityYear(ConfigEntityYearID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/ConfigEntityYear/" + ConfigEntityYearID, verb = "delete")

def deleteConfigSystem(ConfigSystemID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/ConfigSystem/" + ConfigSystemID, verb = "delete")

def deleteDisciplineLetterRunHistory(DisciplineLetterRunHistoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/DisciplineLetterRunHistory/" + DisciplineLetterRunHistoryID, verb = "delete")

def deleteDisciplineLetterRunHistoryAction(DisciplineLetterRunHistoryActionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/DisciplineLetterRunHistoryAction/" + DisciplineLetterRunHistoryActionID, verb = "delete")

def deleteDisciplineLetterRunHistoryOffense(DisciplineLetterRunHistoryOffenseID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/DisciplineLetterRunHistoryOffense/" + DisciplineLetterRunHistoryOffenseID, verb = "delete")

def deleteDisciplineLetterTemplate(DisciplineLetterTemplateID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/DisciplineLetterTemplate/" + DisciplineLetterTemplateID, verb = "delete")

def deleteDisciplineLetterTemplateEntity(DisciplineLetterTemplateEntityID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/DisciplineLetterTemplateEntity/" + DisciplineLetterTemplateEntityID, verb = "delete")

def deleteDisciplineLetterTemplateField(DisciplineLetterTemplateFieldID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/DisciplineLetterTemplateField/" + DisciplineLetterTemplateFieldID, verb = "delete")

def deleteDisciplineLetterTemplateHeaderColumn(DisciplineLetterTemplateHeaderColumnID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/DisciplineLetterTemplateHeaderColumn/" + DisciplineLetterTemplateHeaderColumnID, verb = "delete")

def deleteDisciplineLetterTemplateHeaderRow(DisciplineLetterTemplateHeaderRowID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/DisciplineLetterTemplateHeaderRow/" + DisciplineLetterTemplateHeaderRowID, verb = "delete")

def deleteDrug(DrugID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/Drug/" + DrugID, verb = "delete")

def deleteIncident(IncidentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/Incident/" + IncidentID, verb = "delete")

def deleteIncidentOffense(IncidentOffenseID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/IncidentOffense/" + IncidentOffenseID, verb = "delete")

def deleteIncidentOffenseNameActionDetail(IncidentOffenseNameActionDetailID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/IncidentOffenseNameActionDetail/" + IncidentOffenseNameActionDetailID, verb = "delete")

def deleteIncidentOffenseNameActionDetailPeriod(IncidentOffenseNameActionDetailPeriodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/IncidentOffenseNameActionDetailPeriod/" + IncidentOffenseNameActionDetailPeriodID, verb = "delete")

def deleteIncidentOffenseNameAction(IncidentOffenseNameActionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/IncidentOffenseNameAction/" + IncidentOffenseNameActionID, verb = "delete")

def deleteIncidentOffenseNameDrug(IncidentOffenseNameDrugID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/IncidentOffenseNameDrug/" + IncidentOffenseNameDrugID, verb = "delete")

def deleteIncidentOffenseName(IncidentOffenseNameID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/IncidentOffenseName/" + IncidentOffenseNameID, verb = "delete")

def deleteIncidentOffenseNameReportRunHistory(IncidentOffenseNameReportRunHistoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/IncidentOffenseNameReportRunHistory/" + IncidentOffenseNameReportRunHistoryID, verb = "delete")

def deleteIncidentOffenseNameWeapon(IncidentOffenseNameWeaponID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/IncidentOffenseNameWeapon/" + IncidentOffenseNameWeaponID, verb = "delete")

def deleteLocation(LocationID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/Location/" + LocationID, verb = "delete")

def deleteNextIncidentNumber(NextIncidentNumberID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/NextIncidentNumber/" + NextIncidentNumberID, verb = "delete")

def deleteOffense(OffenseID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/Offense/" + OffenseID, verb = "delete")

def deleteOffenseAction(OffenseActionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/OffenseAction/" + OffenseActionID, verb = "delete")

def deleteOffenseLevel(OffenseLevelID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/OffenseLevel/" + OffenseLevelID, verb = "delete")

def deletePerceivedMotivation(PerceivedMotivationID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/PerceivedMotivation/" + PerceivedMotivationID, verb = "delete")

def deleteTempIncidentOffenseNameAction(TempIncidentOffenseNameActionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/TempIncidentOffenseNameAction/" + TempIncidentOffenseNameActionID, verb = "delete")

def deleteTempIncidentOffenseNameActionDetail(TempIncidentOffenseNameActionDetailID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/TempIncidentOffenseNameActionDetail/" + TempIncidentOffenseNameActionDetailID, verb = "delete")

def deleteTempIncidentOffenseNameActionDetailRecord(TempIncidentOffenseNameActionDetailRecordID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/TempIncidentOffenseNameActionDetailRecord/" + TempIncidentOffenseNameActionDetailRecordID, verb = "delete")

def deleteTempIncidentOffenseNameReportRunHistoryRecord(TempIncidentOffenseNameReportRunHistoryRecordID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/TempIncidentOffenseNameReportRunHistoryRecord/" + TempIncidentOffenseNameReportRunHistoryRecordID, verb = "delete")

def deleteWeapon(WeaponID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Discipline/Weapon/" + WeaponID, verb = "delete")