# This module contains Health functions.

from . import make_request

def deleteAdministerNameMedication(AdministerNameMedicationID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/AdministerNameMedication/" + AdministerNameMedicationID, verb = "delete")

def deleteBodyMassIndexPercentile(BodyMassIndexPercentileID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/BodyMassIndexPercentile/" + BodyMassIndexPercentileID, verb = "delete")

def deleteBodyPart(BodyPartID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/BodyPart/" + BodyPartID, verb = "delete")

def deleteChildhoodIllness(ChildhoodIllnessID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/ChildhoodIllness/" + ChildhoodIllnessID, verb = "delete")

def deleteChildhoodIllnessComment(ChildhoodIllnessCommentID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/ChildhoodIllnessComment/" + ChildhoodIllnessCommentID, verb = "delete")

def deleteChildhoodIllnessGuardianNotification(ChildhoodIllnessGuardianNotificationID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/ChildhoodIllnessGuardianNotification/" + ChildhoodIllnessGuardianNotificationID, verb = "delete")

def deleteChildhoodIllnessGuardianResponse(ChildhoodIllnessGuardianResponseID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/ChildhoodIllnessGuardianResponse/" + ChildhoodIllnessGuardianResponseID, verb = "delete")

def deleteChildhoodIllnessObservation(ChildhoodIllnessObservationID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/ChildhoodIllnessObservation/" + ChildhoodIllnessObservationID, verb = "delete")

def deleteChildhoodIllnessReferralReason(ChildhoodIllnessReferralReasonID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/ChildhoodIllnessReferralReason/" + ChildhoodIllnessReferralReasonID, verb = "delete")

def deleteChildhoodIllnessReferralResult(ChildhoodIllnessReferralResultID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/ChildhoodIllnessReferralResult/" + ChildhoodIllnessReferralResultID, verb = "delete")

def deleteComplianceSchedule(ComplianceScheduleID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/ComplianceSchedule/" + ComplianceScheduleID, verb = "delete")

def deleteComplianceScheduleDetail(ComplianceScheduleDetailID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/ComplianceScheduleDetail/" + ComplianceScheduleDetailID, verb = "delete")

def deleteComplianceScheduleDetailBooster(ComplianceScheduleDetailBoosterID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/ComplianceScheduleDetailBooster/" + ComplianceScheduleDetailBoosterID, verb = "delete")

def deleteComplianceScheduleRule(ComplianceScheduleRuleID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/ComplianceScheduleRule/" + ComplianceScheduleRuleID, verb = "delete")

def deleteConfigDistrictGroup(ConfigDistrictGroupID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/ConfigDistrictGroup/" + ConfigDistrictGroupID, verb = "delete")

def deleteConfigDistrictYear(ConfigDistrictYearID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/ConfigDistrictYear/" + ConfigDistrictYearID, verb = "delete")

def deleteConfigEntity(ConfigEntityID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/ConfigEntity/" + ConfigEntityID, verb = "delete")

def deleteDentalComment(DentalCommentID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/DentalComment/" + DentalCommentID, verb = "delete")

def deleteDentalGuardianNotification(DentalGuardianNotificationID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/DentalGuardianNotification/" + DentalGuardianNotificationID, verb = "delete")

def deleteDentalGuardianResponse(DentalGuardianResponseID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/DentalGuardianResponse/" + DentalGuardianResponseID, verb = "delete")

def deleteDentalReferralReason(DentalReferralReasonID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/DentalReferralReason/" + DentalReferralReasonID, verb = "delete")

def deleteDentalReferralResult(DentalReferralResultID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/DentalReferralResult/" + DentalReferralResultID, verb = "delete")

def deleteDentalScreening(DentalScreeningID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/DentalScreening/" + DentalScreeningID, verb = "delete")

def deleteDentalScreeningComment(DentalScreeningCommentID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/DentalScreeningComment/" + DentalScreeningCommentID, verb = "delete")

def deleteDentalScreeningNote(DentalScreeningNoteID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/DentalScreeningNote/" + DentalScreeningNoteID, verb = "delete")

def deleteDentalScreeningReferral(DentalScreeningReferralID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/DentalScreeningReferral/" + DentalScreeningReferralID, verb = "delete")

def deleteDentalScreeningResult(DentalScreeningResultID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/DentalScreeningResult/" + DentalScreeningResultID, verb = "delete")

def deleteDentalScreeningSecuredNote(DentalScreeningSecuredNoteID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/DentalScreeningSecuredNote/" + DentalScreeningSecuredNoteID, verb = "delete")

def deleteDentalTreatment(DentalTreatmentID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/DentalTreatment/" + DentalTreatmentID, verb = "delete")

def deleteDiabetesCareLog(DiabetesCareLogID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/DiabetesCareLog/" + DiabetesCareLogID, verb = "delete")

def deleteDiabetesCareLogNote(DiabetesCareLogNoteID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/DiabetesCareLogNote/" + DiabetesCareLogNoteID, verb = "delete")

def deleteDiabetesCareLogReferral(DiabetesCareLogReferralID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/DiabetesCareLogReferral/" + DiabetesCareLogReferralID, verb = "delete")

def deleteDiabetesCareLogSecuredNote(DiabetesCareLogSecuredNoteID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/DiabetesCareLogSecuredNote/" + DiabetesCareLogSecuredNoteID, verb = "delete")

def deleteDiabetesCareLogTreatment(DiabetesCareLogTreatmentID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/DiabetesCareLogTreatment/" + DiabetesCareLogTreatmentID, verb = "delete")

def deleteDiabetesGuardianNotification(DiabetesGuardianNotificationID, EntityID = 1):

	make_request(endpoint = "/Generic/" + EntityID + "/Health/DiabetesGuardianNotification/" + DiabetesGuardianNotificationID, verb = "delete")