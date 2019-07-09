# This module contains Family functions.

def deleteChangeRequest(ChangeRequestID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Family/ChangeRequest/" + ChangeRequestID, verb = "delete")

def deleteChangeRequestApprovalTask(ChangeRequestApprovalTaskID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Family/ChangeRequestApprovalTask/" + ChangeRequestApprovalTaskID, verb = "delete")

def deleteChangeRequestApprovalTaskSecurityGroup(ChangeRequestApprovalTaskSecurityGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Family/ChangeRequestApprovalTaskSecurityGroup/" + ChangeRequestApprovalTaskSecurityGroupID, verb = "delete")

def deleteChangeRequestDetail(ChangeRequestDetailID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Family/ChangeRequestDetail/" + ChangeRequestDetailID, verb = "delete")

def deleteChangeRequestDetailApproval(ChangeRequestDetailApprovalID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Family/ChangeRequestDetailApproval/" + ChangeRequestDetailApprovalID, verb = "delete")

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Family/ConfigEntityGroupYear/" + ConfigEntityGroupYearID, verb = "delete")

def deleteConfigSystem(ConfigSystemID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Family/ConfigSystem/" + ConfigSystemID, verb = "delete")

def deleteFamily(FamilyID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Family/Family/" + FamilyID, verb = "delete")

def deleteFamilyGuardian(FamilyGuardianID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Family/FamilyGuardian/" + FamilyGuardianID, verb = "delete")

def deleteStudentFamily(StudentFamilyID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Family/StudentFamily/" + StudentFamilyID, verb = "delete")

def deleteStudentGuardian(StudentGuardianID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Family/StudentGuardian/" + StudentGuardianID, verb = "delete")

def deleteStudentGuardianRestrictedAccess(StudentGuardianRestrictedAccessID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Family/StudentGuardianRestrictedAccess/" + StudentGuardianRestrictedAccessID, verb = "delete")

def deleteTempFamilyGuardian(TempFamilyGuardianID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Family/TempFamilyGuardian/" + TempFamilyGuardianID, verb = "delete")