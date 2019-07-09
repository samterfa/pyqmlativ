# This module contains Enrollment functions.

def deleteAwardsListMA(AwardsListMAID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/AwardsListMA/" + AwardsListMAID, verb = "delete")

def deleteAwardsMA(AwardsMAID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/AwardsMA/" + AwardsMAID, verb = "delete")

def deleteConfigDistrict(ConfigDistrictID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/ConfigDistrict/" + ConfigDistrictID, verb = "delete")

def deleteConfigDistrictYear(ConfigDistrictYearID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/ConfigDistrictYear/" + ConfigDistrictYearID, verb = "delete")

def deleteConfigDistrictYearWithdrawalCode(ConfigDistrictYearWithdrawalCodeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/ConfigDistrictYearWithdrawalCode/" + ConfigDistrictYearWithdrawalCodeID, verb = "delete")

def deleteEntitySchool(EntitySchoolID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/EntitySchool/" + EntitySchoolID, verb = "delete")

def deleteEntitySchoolBuilding(EntitySchoolBuildingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/EntitySchoolBuilding/" + EntitySchoolBuildingID, verb = "delete")

def deleteEntryCode(EntryCodeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/EntryCode/" + EntryCodeID, verb = "delete")

def deleteEntryWithdrawal(EntryWithdrawalID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/EntryWithdrawal/" + EntryWithdrawalID, verb = "delete")

def deleteGradeLevel(GradeLevelID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/GradeLevel/" + GradeLevelID, verb = "delete")

def deleteGradeReference(GradeReferenceID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/GradeReference/" + GradeReferenceID, verb = "delete")

def deleteHomeroom(HomeroomID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/Homeroom/" + HomeroomID, verb = "delete")

def deletePaymentPlanMA(PaymentPlanMAID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/PaymentPlanMA/" + PaymentPlanMAID, verb = "delete")

def deletePermit(PermitID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/Permit/" + PermitID, verb = "delete")

def deleteSchool(SchoolID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/School/" + SchoolID, verb = "delete")

def deleteStudentAccountsMA(StudentAccountsMAID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/StudentAccountsMA/" + StudentAccountsMAID, verb = "delete")

def deleteStudentEntityYear(StudentEntityYearID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/StudentEntityYear/" + StudentEntityYearID, verb = "delete")

def deleteStudentType(StudentTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/StudentType/" + StudentTypeID, verb = "delete")

def deleteTempAffectedWithdrawalRecord(TempAffectedWithdrawalRecordID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/TempAffectedWithdrawalRecord/" + TempAffectedWithdrawalRecordID, verb = "delete")

def deleteTempHomeroomError(TempHomeroomErrorID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/TempHomeroomError/" + TempHomeroomErrorID, verb = "delete")

def deleteTempHomeroomRecord(TempHomeroomRecordID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/TempHomeroomRecord/" + TempHomeroomRecordID, verb = "delete")

def deleteTempNoShowEntryWithdrawal(TempNoShowEntryWithdrawalID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/TempNoShowEntryWithdrawal/" + TempNoShowEntryWithdrawalID, verb = "delete")

def deleteTempStudentEnrollmentRecord(TempStudentEnrollmentRecordID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/TempStudentEnrollmentRecord/" + TempStudentEnrollmentRecordID, verb = "delete")

def deleteTempStudentEntityYear(TempStudentEntityYearID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/TempStudentEntityYear/" + TempStudentEntityYearID, verb = "delete")

def deleteWithdrawalCode(WithdrawalCodeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Enrollment/WithdrawalCode/" + WithdrawalCodeID, verb = "delete")