# This module contains District functions.

def deleteBuilding(BuildingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/District/Building/" + BuildingID, verb = "delete")

def deleteCalendarYear(CalendarYearID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/District/CalendarYear/" + CalendarYearID, verb = "delete")

def deleteConfigEntityYear(ConfigEntityYearID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/District/ConfigEntityYear/" + ConfigEntityYearID, verb = "delete")

def deleteDistrictGroup(DistrictGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/District/DistrictGroup/" + DistrictGroupID, verb = "delete")

def deleteDistrict(DistrictID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/District/District/" + DistrictID, verb = "delete")

def deleteDistrictSchoolYear(DistrictSchoolYearID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/District/DistrictSchoolYear/" + DistrictSchoolYearID, verb = "delete")

def deleteEntityGroup(EntityGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/District/EntityGroup/" + EntityGroupID, verb = "delete")

def deleteEntityGroupEntity(EntityGroupEntityID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/District/EntityGroupEntity/" + EntityGroupEntityID, verb = "delete")

def deleteEntityGroupSetup(EntityGroupSetupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/District/EntityGroupSetup/" + EntityGroupSetupID, verb = "delete")

def deleteEntityGroupSetupEntity(EntityGroupSetupEntityID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/District/EntityGroupSetupEntity/" + EntityGroupSetupEntityID, verb = "delete")

def deleteEntityGroupSetupRun(EntityGroupSetupRunID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/District/EntityGroupSetupRun/" + EntityGroupSetupRunID, verb = "delete")

def deleteEntityGroupSetupRunDetail(EntityGroupSetupRunDetailID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/District/EntityGroupSetupRunDetail/" + EntityGroupSetupRunDetailID, verb = "delete")

def deleteEntity(EntityID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/District/Entity/" + EntityID, verb = "delete")

def deleteFiscalYear(FiscalYearID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/District/FiscalYear/" + FiscalYearID, verb = "delete")

def deleteRoom(RoomID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/District/Room/" + RoomID, verb = "delete")

def deleteRoomType(RoomTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/District/RoomType/" + RoomTypeID, verb = "delete")

def deleteSchoolYear(SchoolYearID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/District/SchoolYear/" + SchoolYearID, verb = "delete")

def deleteStateDistrictMN(StateDistrictMNID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/District/StateDistrictMN/" + StateDistrictMNID, verb = "delete")