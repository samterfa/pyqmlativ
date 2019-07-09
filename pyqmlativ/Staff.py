# This module contains Staff functions.

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Staff/ConfigEntityGroupYear/" + ConfigEntityGroupYearID, verb = "delete")

def deleteConfigSystem(ConfigSystemID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Staff/ConfigSystem/" + ConfigSystemID, verb = "delete")

def deleteDepartment(DepartmentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Staff/Department/" + DepartmentID, verb = "delete")

def deleteMassPrintStaffScheduleRunHistory(MassPrintStaffScheduleRunHistoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Staff/MassPrintStaffScheduleRunHistory/" + MassPrintStaffScheduleRunHistoryID, verb = "delete")

def deleteNextStaffNumber(NextStaffNumberID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Staff/NextStaffNumber/" + NextStaffNumberID, verb = "delete")

def deleteScheduleBlocker(ScheduleBlockerID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Staff/ScheduleBlocker/" + ScheduleBlockerID, verb = "delete")

def deleteScheduleBlockerDisplayPeriod(ScheduleBlockerDisplayPeriodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Staff/ScheduleBlockerDisplayPeriod/" + ScheduleBlockerDisplayPeriodID, verb = "delete")

def deleteStaffDepartment(StaffDepartmentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Staff/StaffDepartment/" + StaffDepartmentID, verb = "delete")

def deleteStaffEntityYear(StaffEntityYearID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Staff/StaffEntityYear/" + StaffEntityYearID, verb = "delete")

def deleteStaff(StaffID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Staff/Staff/" + StaffID, verb = "delete")

def deleteStaffStaffType(StaffStaffTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Staff/StaffStaffType/" + StaffStaffTypeID, verb = "delete")

def deleteStaffType(StaffTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Staff/StaffType/" + StaffTypeID, verb = "delete")