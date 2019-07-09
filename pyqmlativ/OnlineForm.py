# This module contains OnlineForm functions.

def deleteElement(ElementID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/Element/" + ElementID, verb = "delete")

def deleteElementGroup(ElementGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/ElementGroup/" + ElementGroupID, verb = "delete")

def deleteElementGroupTemplate(ElementGroupTemplateID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/ElementGroupTemplate/" + ElementGroupTemplateID, verb = "delete")

def deleteElementStatus(ElementStatusID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/ElementStatus/" + ElementStatusID, verb = "delete")

def deleteElementStatusSurveyAnswer(ElementStatusSurveyAnswerID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/ElementStatusSurveyAnswer/" + ElementStatusSurveyAnswerID, verb = "delete")

def deleteMassPrintHistory(MassPrintHistoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/MassPrintHistory/" + MassPrintHistoryID, verb = "delete")

def deleteNewStudentEnrollmentGuardianData(NewStudentEnrollmentGuardianDataID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/NewStudentEnrollmentGuardianData/" + NewStudentEnrollmentGuardianDataID, verb = "delete")

def deleteNewStudentEnrollmentUserData(NewStudentEnrollmentUserDataID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/NewStudentEnrollmentUserData/" + NewStudentEnrollmentUserDataID, verb = "delete")

def deleteOnlineForm(OnlineFormID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/OnlineForm/" + OnlineFormID, verb = "delete")

def deleteOnlineFormClearance(OnlineFormClearanceID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/OnlineFormClearance/" + OnlineFormClearanceID, verb = "delete")

def deleteOnlineFormDateException(OnlineFormDateExceptionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/OnlineFormDateException/" + OnlineFormDateExceptionID, verb = "delete")

def deleteOnlineFormEntity(OnlineFormEntityID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/OnlineFormEntity/" + OnlineFormEntityID, verb = "delete")

def deleteOnlineFormStatus(OnlineFormStatusID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/OnlineFormStatus/" + OnlineFormStatusID, verb = "delete")

def deleteOnlineFormStatusName(OnlineFormStatusNameID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/OnlineFormStatusName/" + OnlineFormStatusNameID, verb = "delete")

def deleteOnlineFormType(OnlineFormTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/OnlineFormType/" + OnlineFormTypeID, verb = "delete")

def deleteSharedElementStatus(SharedElementStatusID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/SharedElementStatus/" + SharedElementStatusID, verb = "delete")

def deleteStaffContact(StaffContactID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/StaffContact/" + StaffContactID, verb = "delete")

def deleteStep(StepID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/Step/" + StepID, verb = "delete")

def deleteStepStatus(StepStatusID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/StepStatus/" + StepStatusID, verb = "delete")

def deleteTeacherOnlineForm(OnlineFormEntityID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/TeacherOnlineForm/" + OnlineFormEntityID, verb = "delete")

def deleteTempCertification(TempCertificationID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/TempCertification/" + TempCertificationID, verb = "delete")

def deleteTempDataGridRow(TempDataGridRowID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/TempDataGridRow/" + TempDataGridRowID, verb = "delete")

def deleteTempDegree(TempDegreeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/TempDegree/" + TempDegreeID, verb = "delete")

def deleteTempDependent(TempDependentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/TempDependent/" + TempDependentID, verb = "delete")

def deleteTempEmergencyContact(TempEmergencyContactID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/TempEmergencyContact/" + TempEmergencyContactID, verb = "delete")

def deleteTempError(TempErrorID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/TempError/" + TempErrorID, verb = "delete")

def deleteTempNewStudentEnrollmentGuardianEmail(TempNewStudentEnrollmentGuardianEmailID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/TempNewStudentEnrollmentGuardianEmail/" + TempNewStudentEnrollmentGuardianEmailID, verb = "delete")

def deleteTempNewStudentEnrollmentGuardianPhone(TempNewStudentEnrollmentGuardianPhoneID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/TempNewStudentEnrollmentGuardianPhone/" + TempNewStudentEnrollmentGuardianPhoneID, verb = "delete")

def deleteTempStep(TempStepID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/TempStep/" + TempStepID, verb = "delete")

def deleteTempStudentHealthCondition(TempStudentHealthConditionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/OnlineForm/TempStudentHealthCondition/" + TempStudentHealthConditionID, verb = "delete")