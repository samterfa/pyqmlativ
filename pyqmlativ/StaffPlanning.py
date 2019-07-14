# This module contains StaffPlanning functions.

from .Utilities import make_request

import pandas as pd

import json

import re

def getEveryAssignmentTypePlanPositionDistributionSummary(EntityID = 1, page = 1, pageSize = 100, returnPlanPositionDistributionIDFirst = True, returnAssignmentTypeID = False, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/AssignmentTypePlanPositionDistributionSummary/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAssignmentTypePlanPositionDistributionSummary(PlanPositionDistributionIDFirst, EntityID = 1, returnPlanPositionDistributionIDFirst = True, returnAssignmentTypeID = False, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/AssignmentTypePlanPositionDistributionSummary/" + str(PlanPositionDistributionIDFirst), verb = "get", return_params_list = return_params_list)

def modifyAssignmentTypePlanPositionDistributionSummary(PlanPositionDistributionIDFirst, EntityID = 1, setPlanPositionDistributionIDFirst = None, setAssignmentTypeID = None, setPlanGroupID = None, setPositionTypeID = None, setRelationships = None, returnPlanPositionDistributionIDFirst = True, returnAssignmentTypeID = False, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/AssignmentTypePlanPositionDistributionSummary/" + str(PlanPositionDistributionIDFirst), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAssignmentTypePlanPositionDistributionSummary(EntityID = 1, setPlanPositionDistributionIDFirst = None, setAssignmentTypeID = None, setPlanGroupID = None, setPositionTypeID = None, setRelationships = None, returnPlanPositionDistributionIDFirst = True, returnAssignmentTypeID = False, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/AssignmentTypePlanPositionDistributionSummary/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAssignmentTypePlanPositionDistributionSummary(PlanPositionDistributionIDFirst, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryBuildingPlanPositionDistributionSummary(EntityID = 1, page = 1, pageSize = 100, returnPlanPositionDistributionIDFirst = True, returnBuildingID = False, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/BuildingPlanPositionDistributionSummary/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getBuildingPlanPositionDistributionSummary(PlanPositionDistributionIDFirst, EntityID = 1, returnPlanPositionDistributionIDFirst = True, returnBuildingID = False, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/BuildingPlanPositionDistributionSummary/" + str(PlanPositionDistributionIDFirst), verb = "get", return_params_list = return_params_list)

def modifyBuildingPlanPositionDistributionSummary(PlanPositionDistributionIDFirst, EntityID = 1, setPlanPositionDistributionIDFirst = None, setBuildingID = None, setPlanGroupID = None, setPositionTypeID = None, setRelationships = None, returnPlanPositionDistributionIDFirst = True, returnBuildingID = False, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/BuildingPlanPositionDistributionSummary/" + str(PlanPositionDistributionIDFirst), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createBuildingPlanPositionDistributionSummary(EntityID = 1, setPlanPositionDistributionIDFirst = None, setBuildingID = None, setPlanGroupID = None, setPositionTypeID = None, setRelationships = None, returnPlanPositionDistributionIDFirst = True, returnBuildingID = False, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/BuildingPlanPositionDistributionSummary/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteBuildingPlanPositionDistributionSummary(PlanPositionDistributionIDFirst, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPlan(EntityID = 1, page = 1, pageSize = 100, returnPlanID = True, returnCalculationStatus = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnDistrictID = False, returnFiscalYearID = False, returnModifiedTime = False, returnNumberOfOccupiedPositions = False, returnNumberOfVacantPositions = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/Plan/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPlan(PlanID, EntityID = 1, returnPlanID = True, returnCalculationStatus = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnDistrictID = False, returnFiscalYearID = False, returnModifiedTime = False, returnNumberOfOccupiedPositions = False, returnNumberOfVacantPositions = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/Plan/" + str(PlanID), verb = "get", return_params_list = return_params_list)

def modifyPlan(PlanID, EntityID = 1, setDescription = None, setDistrictID = None, setFiscalYearID = None, setRelationships = None, returnPlanID = True, returnCalculationStatus = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnDistrictID = False, returnFiscalYearID = False, returnModifiedTime = False, returnNumberOfOccupiedPositions = False, returnNumberOfVacantPositions = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/Plan/" + str(PlanID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPlan(EntityID = 1, setDescription = None, setDistrictID = None, setFiscalYearID = None, setRelationships = None, returnPlanID = True, returnCalculationStatus = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnDistrictID = False, returnFiscalYearID = False, returnModifiedTime = False, returnNumberOfOccupiedPositions = False, returnNumberOfVacantPositions = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/Plan/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePlan(PlanID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPlanEmployee(EntityID = 1, page = 1, pageSize = 100, returnPlanEmployeeID = True, returnAssignedFTE = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnEmployeeID = False, returnModifiedTime = False, returnPlanID = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanEmployee/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPlanEmployee(PlanEmployeeID, EntityID = 1, returnPlanEmployeeID = True, returnAssignedFTE = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnEmployeeID = False, returnModifiedTime = False, returnPlanID = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanEmployee/" + str(PlanEmployeeID), verb = "get", return_params_list = return_params_list)

def modifyPlanEmployee(PlanEmployeeID, EntityID = 1, setEmployeeID = None, setPlanID = None, setRelationships = None, returnPlanEmployeeID = True, returnAssignedFTE = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnEmployeeID = False, returnModifiedTime = False, returnPlanID = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanEmployee/" + str(PlanEmployeeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPlanEmployee(EntityID = 1, setEmployeeID = None, setPlanID = None, setRelationships = None, returnPlanEmployeeID = True, returnAssignedFTE = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnEmployeeID = False, returnModifiedTime = False, returnPlanID = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanEmployee/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePlanEmployee(PlanEmployeeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPlanGroup(EntityID = 1, page = 1, pageSize = 100, returnPlanGroupID = True, returnAssignedFTE = False, returnAvailableFTE = False, returnBudgetedFTE = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnIsUnassigned = False, returnModifiedTime = False, returnNumberOfOccupiedPositions = False, returnNumberOfVacantPositions = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPlanGroup(PlanGroupID, EntityID = 1, returnPlanGroupID = True, returnAssignedFTE = False, returnAvailableFTE = False, returnBudgetedFTE = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnIsUnassigned = False, returnModifiedTime = False, returnNumberOfOccupiedPositions = False, returnNumberOfVacantPositions = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroup/" + str(PlanGroupID), verb = "get", return_params_list = return_params_list)

def modifyPlanGroup(PlanGroupID, EntityID = 1, setBudgetedFTE = None, setCode = None, setDescription = None, setIsUnassigned = None, setPlanID = None, setRelationships = None, returnPlanGroupID = True, returnAssignedFTE = False, returnAvailableFTE = False, returnBudgetedFTE = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnIsUnassigned = False, returnModifiedTime = False, returnNumberOfOccupiedPositions = False, returnNumberOfVacantPositions = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroup/" + str(PlanGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPlanGroup(EntityID = 1, setBudgetedFTE = None, setCode = None, setDescription = None, setIsUnassigned = None, setPlanID = None, setRelationships = None, returnPlanGroupID = True, returnAssignedFTE = False, returnAvailableFTE = False, returnBudgetedFTE = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnIsUnassigned = False, returnModifiedTime = False, returnNumberOfOccupiedPositions = False, returnNumberOfVacantPositions = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePlanGroup(PlanGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPlanGroupAssignmentType(EntityID = 1, page = 1, pageSize = 100, returnPlanGroupAssignmentTypeID = True, returnAssignmentTypeID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupAssignmentType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPlanGroupAssignmentType(PlanGroupAssignmentTypeID, EntityID = 1, returnPlanGroupAssignmentTypeID = True, returnAssignmentTypeID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupAssignmentType/" + str(PlanGroupAssignmentTypeID), verb = "get", return_params_list = return_params_list)

def modifyPlanGroupAssignmentType(PlanGroupAssignmentTypeID, EntityID = 1, setAssignmentTypeID = None, setPlanGroupID = None, setRelationships = None, returnPlanGroupAssignmentTypeID = True, returnAssignmentTypeID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupAssignmentType/" + str(PlanGroupAssignmentTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPlanGroupAssignmentType(EntityID = 1, setAssignmentTypeID = None, setPlanGroupID = None, setRelationships = None, returnPlanGroupAssignmentTypeID = True, returnAssignmentTypeID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupAssignmentType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePlanGroupAssignmentType(PlanGroupAssignmentTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPlanGroupBuilding(EntityID = 1, page = 1, pageSize = 100, returnPlanGroupBuildingID = True, returnBuildingID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupBuilding/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPlanGroupBuilding(PlanGroupBuildingID, EntityID = 1, returnPlanGroupBuildingID = True, returnBuildingID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupBuilding/" + str(PlanGroupBuildingID), verb = "get", return_params_list = return_params_list)

def modifyPlanGroupBuilding(PlanGroupBuildingID, EntityID = 1, setBuildingID = None, setPlanGroupID = None, setRelationships = None, returnPlanGroupBuildingID = True, returnBuildingID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupBuilding/" + str(PlanGroupBuildingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPlanGroupBuilding(EntityID = 1, setBuildingID = None, setPlanGroupID = None, setRelationships = None, returnPlanGroupBuildingID = True, returnBuildingID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupBuilding/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePlanGroupBuilding(PlanGroupBuildingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPlanGroupClearance(EntityID = 1, page = 1, pageSize = 100, returnPlanGroupClearanceID = True, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnSecurityGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupClearance/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPlanGroupClearance(PlanGroupClearanceID, EntityID = 1, returnPlanGroupClearanceID = True, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnSecurityGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupClearance/" + str(PlanGroupClearanceID), verb = "get", return_params_list = return_params_list)

def modifyPlanGroupClearance(PlanGroupClearanceID, EntityID = 1, setPlanGroupID = None, setSecurityGroupID = None, setRelationships = None, returnPlanGroupClearanceID = True, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnSecurityGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupClearance/" + str(PlanGroupClearanceID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPlanGroupClearance(EntityID = 1, setPlanGroupID = None, setSecurityGroupID = None, setRelationships = None, returnPlanGroupClearanceID = True, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnSecurityGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupClearance/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePlanGroupClearance(PlanGroupClearanceID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPlanGroupPositionType(EntityID = 1, page = 1, pageSize = 100, returnPlanGroupPositionTypeID = True, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnPositionTypeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupPositionType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPlanGroupPositionType(PlanGroupPositionTypeID, EntityID = 1, returnPlanGroupPositionTypeID = True, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnPositionTypeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupPositionType/" + str(PlanGroupPositionTypeID), verb = "get", return_params_list = return_params_list)

def modifyPlanGroupPositionType(PlanGroupPositionTypeID, EntityID = 1, setPlanGroupID = None, setPositionTypeID = None, setRelationships = None, returnPlanGroupPositionTypeID = True, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnPositionTypeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupPositionType/" + str(PlanGroupPositionTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPlanGroupPositionType(EntityID = 1, setPlanGroupID = None, setPositionTypeID = None, setRelationships = None, returnPlanGroupPositionTypeID = True, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnPositionTypeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupPositionType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePlanGroupPositionType(PlanGroupPositionTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPlanPosition(EntityID = 1, page = 1, pageSize = 100, returnPlanPositionID = True, returnAnnualPay = False, returnAssignedFTE = False, returnAvailableFTE = False, returnBudgetedFTE = False, returnCalculationStatus = False, returnCalculationStatusCode = False, returnCalendarID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnEmployeePlacementDescription = False, returnEmployeePlacementID = False, returnFormattedFullPaySecondsPerDay = False, returnFormattedFullPaySecondsPerDayDecimal = False, returnFullPaidDays = False, returnFullPaySecondsPerDay = False, returnJobTypeID = False, returnLaneID = False, returnMatrixID = False, returnModifiedTime = False, returnPlacementID = False, returnPlacementType = False, returnPlacementTypeCode = False, returnPlanEmployeeID = False, returnPlanID = False, returnPlanPositionDistributionsAssignmentTypeCodes = False, returnPlanPositionDistributionsAssignmentTypeDescriptions = False, returnPlanPositionDistributionsBuildingCodes = False, returnPlanPositionDistributionsBuildingDescriptions = False, returnPlanPositionDistributionsDepartmentCodes = False, returnPlanPositionDistributionsDepartmentDescriptions = False, returnPlanPositionDistributionsFTEGroupCodes = False, returnPlanPositionDistributionsFTEGroupDescriptions = False, returnPositionGroupID = False, returnPositionIDClonedFrom = False, returnPositionIdentifier = False, returnPositionNumberID = False, returnPositionTypeID = False, returnRate = False, returnRequiredCredits = False, returnSalaryCalculationMethodID = False, returnStepNumber = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPosition/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPlanPosition(PlanPositionID, EntityID = 1, returnPlanPositionID = True, returnAnnualPay = False, returnAssignedFTE = False, returnAvailableFTE = False, returnBudgetedFTE = False, returnCalculationStatus = False, returnCalculationStatusCode = False, returnCalendarID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnEmployeePlacementDescription = False, returnEmployeePlacementID = False, returnFormattedFullPaySecondsPerDay = False, returnFormattedFullPaySecondsPerDayDecimal = False, returnFullPaidDays = False, returnFullPaySecondsPerDay = False, returnJobTypeID = False, returnLaneID = False, returnMatrixID = False, returnModifiedTime = False, returnPlacementID = False, returnPlacementType = False, returnPlacementTypeCode = False, returnPlanEmployeeID = False, returnPlanID = False, returnPlanPositionDistributionsAssignmentTypeCodes = False, returnPlanPositionDistributionsAssignmentTypeDescriptions = False, returnPlanPositionDistributionsBuildingCodes = False, returnPlanPositionDistributionsBuildingDescriptions = False, returnPlanPositionDistributionsDepartmentCodes = False, returnPlanPositionDistributionsDepartmentDescriptions = False, returnPlanPositionDistributionsFTEGroupCodes = False, returnPlanPositionDistributionsFTEGroupDescriptions = False, returnPositionGroupID = False, returnPositionIDClonedFrom = False, returnPositionIdentifier = False, returnPositionNumberID = False, returnPositionTypeID = False, returnRate = False, returnRequiredCredits = False, returnSalaryCalculationMethodID = False, returnStepNumber = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPosition/" + str(PlanPositionID), verb = "get", return_params_list = return_params_list)

def modifyPlanPosition(PlanPositionID, EntityID = 1, setAnnualPay = None, setBudgetedFTE = None, setCalculationStatus = None, setCalculationStatusCode = None, setCalendarID = None, setDescription = None, setEmployeePlacementDescription = None, setEmployeePlacementID = None, setFormattedFullPaySecondsPerDay = None, setFullPaidDays = None, setFullPaySecondsPerDay = None, setJobTypeID = None, setLaneID = None, setMatrixID = None, setPlacementID = None, setPlacementType = None, setPlacementTypeCode = None, setPlanEmployeeID = None, setPlanID = None, setPositionGroupID = None, setPositionIDClonedFrom = None, setPositionNumberID = None, setPositionTypeID = None, setRate = None, setRequiredCredits = None, setSalaryCalculationMethodID = None, setStepNumber = None, setRelationships = None, returnPlanPositionID = True, returnAnnualPay = False, returnAssignedFTE = False, returnAvailableFTE = False, returnBudgetedFTE = False, returnCalculationStatus = False, returnCalculationStatusCode = False, returnCalendarID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnEmployeePlacementDescription = False, returnEmployeePlacementID = False, returnFormattedFullPaySecondsPerDay = False, returnFormattedFullPaySecondsPerDayDecimal = False, returnFullPaidDays = False, returnFullPaySecondsPerDay = False, returnJobTypeID = False, returnLaneID = False, returnMatrixID = False, returnModifiedTime = False, returnPlacementID = False, returnPlacementType = False, returnPlacementTypeCode = False, returnPlanEmployeeID = False, returnPlanID = False, returnPlanPositionDistributionsAssignmentTypeCodes = False, returnPlanPositionDistributionsAssignmentTypeDescriptions = False, returnPlanPositionDistributionsBuildingCodes = False, returnPlanPositionDistributionsBuildingDescriptions = False, returnPlanPositionDistributionsDepartmentCodes = False, returnPlanPositionDistributionsDepartmentDescriptions = False, returnPlanPositionDistributionsFTEGroupCodes = False, returnPlanPositionDistributionsFTEGroupDescriptions = False, returnPositionGroupID = False, returnPositionIDClonedFrom = False, returnPositionIdentifier = False, returnPositionNumberID = False, returnPositionTypeID = False, returnRate = False, returnRequiredCredits = False, returnSalaryCalculationMethodID = False, returnStepNumber = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPosition/" + str(PlanPositionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPlanPosition(EntityID = 1, setAnnualPay = None, setBudgetedFTE = None, setCalculationStatus = None, setCalculationStatusCode = None, setCalendarID = None, setDescription = None, setEmployeePlacementDescription = None, setEmployeePlacementID = None, setFormattedFullPaySecondsPerDay = None, setFullPaidDays = None, setFullPaySecondsPerDay = None, setJobTypeID = None, setLaneID = None, setMatrixID = None, setPlacementID = None, setPlacementType = None, setPlacementTypeCode = None, setPlanEmployeeID = None, setPlanID = None, setPositionGroupID = None, setPositionIDClonedFrom = None, setPositionNumberID = None, setPositionTypeID = None, setRate = None, setRequiredCredits = None, setSalaryCalculationMethodID = None, setStepNumber = None, setRelationships = None, returnPlanPositionID = True, returnAnnualPay = False, returnAssignedFTE = False, returnAvailableFTE = False, returnBudgetedFTE = False, returnCalculationStatus = False, returnCalculationStatusCode = False, returnCalendarID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnEmployeePlacementDescription = False, returnEmployeePlacementID = False, returnFormattedFullPaySecondsPerDay = False, returnFormattedFullPaySecondsPerDayDecimal = False, returnFullPaidDays = False, returnFullPaySecondsPerDay = False, returnJobTypeID = False, returnLaneID = False, returnMatrixID = False, returnModifiedTime = False, returnPlacementID = False, returnPlacementType = False, returnPlacementTypeCode = False, returnPlanEmployeeID = False, returnPlanID = False, returnPlanPositionDistributionsAssignmentTypeCodes = False, returnPlanPositionDistributionsAssignmentTypeDescriptions = False, returnPlanPositionDistributionsBuildingCodes = False, returnPlanPositionDistributionsBuildingDescriptions = False, returnPlanPositionDistributionsDepartmentCodes = False, returnPlanPositionDistributionsDepartmentDescriptions = False, returnPlanPositionDistributionsFTEGroupCodes = False, returnPlanPositionDistributionsFTEGroupDescriptions = False, returnPositionGroupID = False, returnPositionIDClonedFrom = False, returnPositionIdentifier = False, returnPositionNumberID = False, returnPositionTypeID = False, returnRate = False, returnRequiredCredits = False, returnSalaryCalculationMethodID = False, returnStepNumber = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPosition/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePlanPosition(PlanPositionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPlanPositionBenefit(EntityID = 1, page = 1, pageSize = 100, returnPlanPositionBenefitID = True, returnBenefitID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionID = False, returnTotalAnnualAmountCalculated = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionBenefit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPlanPositionBenefit(PlanPositionBenefitID, EntityID = 1, returnPlanPositionBenefitID = True, returnBenefitID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionID = False, returnTotalAnnualAmountCalculated = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionBenefit/" + str(PlanPositionBenefitID), verb = "get", return_params_list = return_params_list)

def modifyPlanPositionBenefit(PlanPositionBenefitID, EntityID = 1, setBenefitID = None, setCalculationType = None, setCalculationTypeCode = None, setPlanPositionID = None, setValue = None, setRelationships = None, returnPlanPositionBenefitID = True, returnBenefitID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionID = False, returnTotalAnnualAmountCalculated = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionBenefit/" + str(PlanPositionBenefitID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPlanPositionBenefit(EntityID = 1, setBenefitID = None, setCalculationType = None, setCalculationTypeCode = None, setPlanPositionID = None, setValue = None, setRelationships = None, returnPlanPositionBenefitID = True, returnBenefitID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionID = False, returnTotalAnnualAmountCalculated = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionBenefit/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePlanPositionBenefit(PlanPositionBenefitID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPlanPositionDistribution(EntityID = 1, page = 1, pageSize = 100, returnPlanPositionDistributionID = True, returnAssignmentTypeID = False, returnBuildingID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDepartmentID = False, returnFTE = False, returnFTEGroupID = False, returnModifiedTime = False, returnPlanGroupID = False, returnPlanPositionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionDistribution/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPlanPositionDistribution(PlanPositionDistributionID, EntityID = 1, returnPlanPositionDistributionID = True, returnAssignmentTypeID = False, returnBuildingID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDepartmentID = False, returnFTE = False, returnFTEGroupID = False, returnModifiedTime = False, returnPlanGroupID = False, returnPlanPositionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionDistribution/" + str(PlanPositionDistributionID), verb = "get", return_params_list = return_params_list)

def modifyPlanPositionDistribution(PlanPositionDistributionID, EntityID = 1, setAssignmentTypeID = None, setBuildingID = None, setDepartmentID = None, setFTE = None, setFTEGroupID = None, setPlanGroupID = None, setPlanPositionID = None, setRelationships = None, returnPlanPositionDistributionID = True, returnAssignmentTypeID = False, returnBuildingID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDepartmentID = False, returnFTE = False, returnFTEGroupID = False, returnModifiedTime = False, returnPlanGroupID = False, returnPlanPositionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionDistribution/" + str(PlanPositionDistributionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPlanPositionDistribution(EntityID = 1, setAssignmentTypeID = None, setBuildingID = None, setDepartmentID = None, setFTE = None, setFTEGroupID = None, setPlanGroupID = None, setPlanPositionID = None, setRelationships = None, returnPlanPositionDistributionID = True, returnAssignmentTypeID = False, returnBuildingID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDepartmentID = False, returnFTE = False, returnFTEGroupID = False, returnModifiedTime = False, returnPlanGroupID = False, returnPlanPositionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionDistribution/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePlanPositionDistribution(PlanPositionDistributionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPlanPositionPay(EntityID = 1, page = 1, pageSize = 100, returnPlanPositionPayID = True, returnAccountDistributionString = False, returnCreatedTime = False, returnModifiedTime = False, returnPayScheduleID = False, returnPayTypeID = False, returnPlanPositionID = False, returnStipendAmount = False, returnTotalAnnualAmountCalculated = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPay/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPlanPositionPay(PlanPositionPayID, EntityID = 1, returnPlanPositionPayID = True, returnAccountDistributionString = False, returnCreatedTime = False, returnModifiedTime = False, returnPayScheduleID = False, returnPayTypeID = False, returnPlanPositionID = False, returnStipendAmount = False, returnTotalAnnualAmountCalculated = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPay/" + str(PlanPositionPayID), verb = "get", return_params_list = return_params_list)

def modifyPlanPositionPay(PlanPositionPayID, EntityID = 1, setAccountDistributionString = None, setPayScheduleID = None, setPayTypeID = None, setPlanPositionID = None, setStipendAmount = None, setType = None, setTypeCode = None, setRelationships = None, returnPlanPositionPayID = True, returnAccountDistributionString = False, returnCreatedTime = False, returnModifiedTime = False, returnPayScheduleID = False, returnPayTypeID = False, returnPlanPositionID = False, returnStipendAmount = False, returnTotalAnnualAmountCalculated = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPay/" + str(PlanPositionPayID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPlanPositionPay(EntityID = 1, setAccountDistributionString = None, setPayScheduleID = None, setPayTypeID = None, setPlanPositionID = None, setStipendAmount = None, setType = None, setTypeCode = None, setRelationships = None, returnPlanPositionPayID = True, returnAccountDistributionString = False, returnCreatedTime = False, returnModifiedTime = False, returnPayScheduleID = False, returnPayTypeID = False, returnPlanPositionID = False, returnStipendAmount = False, returnTotalAnnualAmountCalculated = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPay/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePlanPositionPay(PlanPositionPayID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPlanPositionPayAccountCalculation(EntityID = 1, page = 1, pageSize = 100, returnPlanPositionPayAccountCalculationID = True, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayAccountCalculation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPlanPositionPayAccountCalculation(PlanPositionPayAccountCalculationID, EntityID = 1, returnPlanPositionPayAccountCalculationID = True, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayAccountCalculation/" + str(PlanPositionPayAccountCalculationID), verb = "get", return_params_list = return_params_list)

def modifyPlanPositionPayAccountCalculation(PlanPositionPayAccountCalculationID, EntityID = 1, setAnnualAmount = None, setPlanPositionPayAccountDistributionID = None, setRelationships = None, returnPlanPositionPayAccountCalculationID = True, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayAccountCalculation/" + str(PlanPositionPayAccountCalculationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPlanPositionPayAccountCalculation(EntityID = 1, setAnnualAmount = None, setPlanPositionPayAccountDistributionID = None, setRelationships = None, returnPlanPositionPayAccountCalculationID = True, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayAccountCalculation/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePlanPositionPayAccountCalculation(PlanPositionPayAccountCalculationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPlanPositionPayAccountDistribution(EntityID = 1, page = 1, pageSize = 100, returnPlanPositionPayAccountDistributionID = True, returnAccountID = False, returnCreatedTime = False, returnDistributionPercent = False, returnModifiedTime = False, returnPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayAccountDistribution/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPlanPositionPayAccountDistribution(PlanPositionPayAccountDistributionID, EntityID = 1, returnPlanPositionPayAccountDistributionID = True, returnAccountID = False, returnCreatedTime = False, returnDistributionPercent = False, returnModifiedTime = False, returnPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayAccountDistribution/" + str(PlanPositionPayAccountDistributionID), verb = "get", return_params_list = return_params_list)

def modifyPlanPositionPayAccountDistribution(PlanPositionPayAccountDistributionID, EntityID = 1, setAccountID = None, setDistributionPercent = None, setPlanPositionPayID = None, setRelationships = None, returnPlanPositionPayAccountDistributionID = True, returnAccountID = False, returnCreatedTime = False, returnDistributionPercent = False, returnModifiedTime = False, returnPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayAccountDistribution/" + str(PlanPositionPayAccountDistributionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPlanPositionPayAccountDistribution(EntityID = 1, setAccountID = None, setDistributionPercent = None, setPlanPositionPayID = None, setRelationships = None, returnPlanPositionPayAccountDistributionID = True, returnAccountID = False, returnCreatedTime = False, returnDistributionPercent = False, returnModifiedTime = False, returnPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayAccountDistribution/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePlanPositionPayAccountDistribution(PlanPositionPayAccountDistributionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPlanPositionPayBenefit(EntityID = 1, page = 1, pageSize = 100, returnPlanPositionPayBenefitID = True, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionBenefitID = False, returnPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayBenefit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPlanPositionPayBenefit(PlanPositionPayBenefitID, EntityID = 1, returnPlanPositionPayBenefitID = True, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionBenefitID = False, returnPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayBenefit/" + str(PlanPositionPayBenefitID), verb = "get", return_params_list = return_params_list)

def modifyPlanPositionPayBenefit(PlanPositionPayBenefitID, EntityID = 1, setPlanPositionBenefitID = None, setPlanPositionPayID = None, setRelationships = None, returnPlanPositionPayBenefitID = True, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionBenefitID = False, returnPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayBenefit/" + str(PlanPositionPayBenefitID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPlanPositionPayBenefit(EntityID = 1, setPlanPositionBenefitID = None, setPlanPositionPayID = None, setRelationships = None, returnPlanPositionPayBenefitID = True, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionBenefitID = False, returnPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayBenefit/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePlanPositionPayBenefit(PlanPositionPayBenefitID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPlanPositionPayBenefitAccount(EntityID = 1, page = 1, pageSize = 100, returnPlanPositionPayBenefitAccountID = True, returnAccountID = False, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnPlanPositionPayBenefitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayBenefitAccount/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPlanPositionPayBenefitAccount(PlanPositionPayBenefitAccountID, EntityID = 1, returnPlanPositionPayBenefitAccountID = True, returnAccountID = False, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnPlanPositionPayBenefitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayBenefitAccount/" + str(PlanPositionPayBenefitAccountID), verb = "get", return_params_list = return_params_list)

def modifyPlanPositionPayBenefitAccount(PlanPositionPayBenefitAccountID, EntityID = 1, setAccountID = None, setAnnualAmount = None, setPlanPositionPayAccountDistributionID = None, setPlanPositionPayBenefitID = None, setRelationships = None, returnPlanPositionPayBenefitAccountID = True, returnAccountID = False, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnPlanPositionPayBenefitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayBenefitAccount/" + str(PlanPositionPayBenefitAccountID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPlanPositionPayBenefitAccount(EntityID = 1, setAccountID = None, setAnnualAmount = None, setPlanPositionPayAccountDistributionID = None, setPlanPositionPayBenefitID = None, setRelationships = None, returnPlanPositionPayBenefitAccountID = True, returnAccountID = False, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnPlanPositionPayBenefitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayBenefitAccount/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePlanPositionPayBenefitAccount(PlanPositionPayBenefitAccountID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPlanPositionSupplement(EntityID = 1, page = 1, pageSize = 100, returnPlanPositionSupplementID = True, returnAnnualPay = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionID = False, returnRate = False, returnSupplementTypeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionSupplement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPlanPositionSupplement(PlanPositionSupplementID, EntityID = 1, returnPlanPositionSupplementID = True, returnAnnualPay = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionID = False, returnRate = False, returnSupplementTypeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionSupplement/" + str(PlanPositionSupplementID), verb = "get", return_params_list = return_params_list)

def modifyPlanPositionSupplement(PlanPositionSupplementID, EntityID = 1, setAnnualPay = None, setPlanPositionID = None, setRate = None, setSupplementTypeID = None, setRelationships = None, returnPlanPositionSupplementID = True, returnAnnualPay = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionID = False, returnRate = False, returnSupplementTypeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionSupplement/" + str(PlanPositionSupplementID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPlanPositionSupplement(EntityID = 1, setAnnualPay = None, setPlanPositionID = None, setRate = None, setSupplementTypeID = None, setRelationships = None, returnPlanPositionSupplementID = True, returnAnnualPay = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionID = False, returnRate = False, returnSupplementTypeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionSupplement/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePlanPositionSupplement(PlanPositionSupplementID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPositionTypePlanPositionDistributionSummary(EntityID = 1, page = 1, pageSize = 100, returnPlanPositionDistributionIDFirst = True, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PositionTypePlanPositionDistributionSummary/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPositionTypePlanPositionDistributionSummary(PlanPositionDistributionIDFirst, EntityID = 1, returnPlanPositionDistributionIDFirst = True, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PositionTypePlanPositionDistributionSummary/" + str(PlanPositionDistributionIDFirst), verb = "get", return_params_list = return_params_list)

def modifyPositionTypePlanPositionDistributionSummary(PlanPositionDistributionIDFirst, EntityID = 1, setPlanPositionDistributionIDFirst = None, setPlanGroupID = None, setPositionTypeID = None, setRelationships = None, returnPlanPositionDistributionIDFirst = True, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PositionTypePlanPositionDistributionSummary/" + str(PlanPositionDistributionIDFirst), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPositionTypePlanPositionDistributionSummary(EntityID = 1, setPlanPositionDistributionIDFirst = None, setPlanGroupID = None, setPositionTypeID = None, setRelationships = None, returnPlanPositionDistributionIDFirst = True, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PositionTypePlanPositionDistributionSummary/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePositionTypePlanPositionDistributionSummary(PlanPositionDistributionIDFirst, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempException(EntityID = 1, page = 1, pageSize = 100, returnTempExceptionID = True, returnCreatedTime = False, returnError = False, returnErroredObjectID = False, returnErrorField = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempException(TempExceptionID, EntityID = 1, returnTempExceptionID = True, returnCreatedTime = False, returnError = False, returnErroredObjectID = False, returnErrorField = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempException/" + str(TempExceptionID), verb = "get", return_params_list = return_params_list)

def modifyTempException(TempExceptionID, EntityID = 1, setError = None, setErroredObjectID = None, setErrorField = None, setRelationships = None, returnTempExceptionID = True, returnCreatedTime = False, returnError = False, returnErroredObjectID = False, returnErrorField = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempException/" + str(TempExceptionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempException(EntityID = 1, setError = None, setErroredObjectID = None, setErrorField = None, setRelationships = None, returnTempExceptionID = True, returnCreatedTime = False, returnError = False, returnErroredObjectID = False, returnErrorField = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempException/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempException(TempExceptionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempPlanPositionBenefit(EntityID = 1, page = 1, pageSize = 100, returnTempPlanPositionBenefitID = True, returnBenefitCodeDescription = False, returnBenefitID = False, returnBenefitTypeTX = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnErrorCount = False, returnModifiedTime = False, returnNewValue = False, returnPlanPositionBenefitID = False, returnPlanPositionEmployeeName = False, returnPlanPositionEmployeeNumber = False, returnPlanPositionID = False, returnPositionNumber = False, returnPositionTypeDescription = False, returnStateBenefitTXID = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionBenefit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempPlanPositionBenefit(TempPlanPositionBenefitID, EntityID = 1, returnTempPlanPositionBenefitID = True, returnBenefitCodeDescription = False, returnBenefitID = False, returnBenefitTypeTX = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnErrorCount = False, returnModifiedTime = False, returnNewValue = False, returnPlanPositionBenefitID = False, returnPlanPositionEmployeeName = False, returnPlanPositionEmployeeNumber = False, returnPlanPositionID = False, returnPositionNumber = False, returnPositionTypeDescription = False, returnStateBenefitTXID = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionBenefit/" + str(TempPlanPositionBenefitID), verb = "get", return_params_list = return_params_list)

def modifyTempPlanPositionBenefit(TempPlanPositionBenefitID, EntityID = 1, setBenefitCodeDescription = None, setBenefitID = None, setBenefitTypeTX = None, setCalculationType = None, setCalculationTypeCode = None, setErrorCount = None, setNewValue = None, setPlanPositionBenefitID = None, setPlanPositionEmployeeName = None, setPlanPositionEmployeeNumber = None, setPlanPositionID = None, setPositionNumber = None, setPositionTypeDescription = None, setStateBenefitTXID = None, setTempPlanPositionEmployeeID = None, setValue = None, setRelationships = None, returnTempPlanPositionBenefitID = True, returnBenefitCodeDescription = False, returnBenefitID = False, returnBenefitTypeTX = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnErrorCount = False, returnModifiedTime = False, returnNewValue = False, returnPlanPositionBenefitID = False, returnPlanPositionEmployeeName = False, returnPlanPositionEmployeeNumber = False, returnPlanPositionID = False, returnPositionNumber = False, returnPositionTypeDescription = False, returnStateBenefitTXID = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionBenefit/" + str(TempPlanPositionBenefitID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempPlanPositionBenefit(EntityID = 1, setBenefitCodeDescription = None, setBenefitID = None, setBenefitTypeTX = None, setCalculationType = None, setCalculationTypeCode = None, setErrorCount = None, setNewValue = None, setPlanPositionBenefitID = None, setPlanPositionEmployeeName = None, setPlanPositionEmployeeNumber = None, setPlanPositionID = None, setPositionNumber = None, setPositionTypeDescription = None, setStateBenefitTXID = None, setTempPlanPositionEmployeeID = None, setValue = None, setRelationships = None, returnTempPlanPositionBenefitID = True, returnBenefitCodeDescription = False, returnBenefitID = False, returnBenefitTypeTX = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnErrorCount = False, returnModifiedTime = False, returnNewValue = False, returnPlanPositionBenefitID = False, returnPlanPositionEmployeeName = False, returnPlanPositionEmployeeNumber = False, returnPlanPositionID = False, returnPositionNumber = False, returnPositionTypeDescription = False, returnStateBenefitTXID = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionBenefit/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempPlanPositionBenefit(TempPlanPositionBenefitID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempPlanPositionDistribution(EntityID = 1, page = 1, pageSize = 100, returnTempPlanPositionDistributionID = True, returnAssignmentTypeID = False, returnBuildingID = False, returnCreatedTime = False, returnDepartmentID = False, returnFTE = False, returnFTEGroupID = False, returnModifiedTime = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionDistribution/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempPlanPositionDistribution(TempPlanPositionDistributionID, EntityID = 1, returnTempPlanPositionDistributionID = True, returnAssignmentTypeID = False, returnBuildingID = False, returnCreatedTime = False, returnDepartmentID = False, returnFTE = False, returnFTEGroupID = False, returnModifiedTime = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionDistribution/" + str(TempPlanPositionDistributionID), verb = "get", return_params_list = return_params_list)

def modifyTempPlanPositionDistribution(TempPlanPositionDistributionID, EntityID = 1, setAssignmentTypeID = None, setBuildingID = None, setDepartmentID = None, setFTE = None, setFTEGroupID = None, setTempPlanPositionEmployeeID = None, setRelationships = None, returnTempPlanPositionDistributionID = True, returnAssignmentTypeID = False, returnBuildingID = False, returnCreatedTime = False, returnDepartmentID = False, returnFTE = False, returnFTEGroupID = False, returnModifiedTime = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionDistribution/" + str(TempPlanPositionDistributionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempPlanPositionDistribution(EntityID = 1, setAssignmentTypeID = None, setBuildingID = None, setDepartmentID = None, setFTE = None, setFTEGroupID = None, setTempPlanPositionEmployeeID = None, setRelationships = None, returnTempPlanPositionDistributionID = True, returnAssignmentTypeID = False, returnBuildingID = False, returnCreatedTime = False, returnDepartmentID = False, returnFTE = False, returnFTEGroupID = False, returnModifiedTime = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionDistribution/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempPlanPositionDistribution(TempPlanPositionDistributionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempPlanPositionEmployee(EntityID = 1, page = 1, pageSize = 100, returnTempPlanPositionEmployeeID = True, returnAmountType = False, returnAmountTypeCode = False, returnAnnualPay = False, returnAssignmentTypeCodes = False, returnAssignmentTypeDescriptions = False, returnBudgetedFTE = False, returnBuildingCodes = False, returnBuildingDescriptions = False, returnCalendarCode = False, returnCalendarID = False, returnCappedAtMaximumRate = False, returnConfigFiscalYearTRSStateBaseStepID = False, returnConfigFiscalYearTRSStateBaseStepLaneCodeStepNumber = False, returnCreatedTime = False, returnDescription = False, returnEmployeeFullNameLFM = False, returnEmployeeID = False, returnEmployeeNumber = False, returnEmployeePlacementDescription = False, returnEmployeePlacementID = False, returnErrorMessage = False, returnFormattedFullPaySecondsPerDay = False, returnFullPaidDays = False, returnFullPaySecondsPerDay = False, returnHasFatalException = False, returnJobTypeID = False, returnLaneCode = False, returnLaneID = False, returnMatrixCode = False, returnMatrixID = False, returnMidpointGroup = False, returnMidpointGroupCodeDescription = False, returnMidpointGroupID = False, returnModifiedTime = False, returnOldAnnualPay = False, returnOldBudgetedFTE = False, returnOldCalendarCode = False, returnOldEmployeePlacementDescription = False, returnOldFormattedFullPaySecondsPerDay = False, returnOldFullPaySecondsPerDay = False, returnOldLaneCode = False, returnOldMatrixCode = False, returnOldMidpointGroup = False, returnOldPlacementCode = False, returnOldPlacementType = False, returnOldPlacementTypeCode = False, returnOldRate = False, returnOldRequiredCredits = False, returnOldSalaryCalculationMethodCode = False, returnOldStepNumber = False, returnOldTRSStateBaseStep = False, returnOldTRSStateBaseStepAmount = False, returnPlacementCode = False, returnPlacementID = False, returnPlacementType = False, returnPlacementTypeCode = False, returnPlanPositionID = False, returnPositionGroupID = False, returnPositionIDClonedFrom = False, returnPositionIdentifier = False, returnPositionNumberCode = False, returnPositionNumberID = False, returnPositionTypeCodeDescription = False, returnPositionTypeID = False, returnRate = False, returnRequiredCredits = False, returnSalaryCalculationMethodCode = False, returnSalaryCalculationMethodID = False, returnStepNumber = False, returnTRSStateBaseStep = False, returnTRSStateBaseStepAmount = False, returnTRSStateBaseStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionEmployee/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempPlanPositionEmployee(TempPlanPositionEmployeeID, EntityID = 1, returnTempPlanPositionEmployeeID = True, returnAmountType = False, returnAmountTypeCode = False, returnAnnualPay = False, returnAssignmentTypeCodes = False, returnAssignmentTypeDescriptions = False, returnBudgetedFTE = False, returnBuildingCodes = False, returnBuildingDescriptions = False, returnCalendarCode = False, returnCalendarID = False, returnCappedAtMaximumRate = False, returnConfigFiscalYearTRSStateBaseStepID = False, returnConfigFiscalYearTRSStateBaseStepLaneCodeStepNumber = False, returnCreatedTime = False, returnDescription = False, returnEmployeeFullNameLFM = False, returnEmployeeID = False, returnEmployeeNumber = False, returnEmployeePlacementDescription = False, returnEmployeePlacementID = False, returnErrorMessage = False, returnFormattedFullPaySecondsPerDay = False, returnFullPaidDays = False, returnFullPaySecondsPerDay = False, returnHasFatalException = False, returnJobTypeID = False, returnLaneCode = False, returnLaneID = False, returnMatrixCode = False, returnMatrixID = False, returnMidpointGroup = False, returnMidpointGroupCodeDescription = False, returnMidpointGroupID = False, returnModifiedTime = False, returnOldAnnualPay = False, returnOldBudgetedFTE = False, returnOldCalendarCode = False, returnOldEmployeePlacementDescription = False, returnOldFormattedFullPaySecondsPerDay = False, returnOldFullPaySecondsPerDay = False, returnOldLaneCode = False, returnOldMatrixCode = False, returnOldMidpointGroup = False, returnOldPlacementCode = False, returnOldPlacementType = False, returnOldPlacementTypeCode = False, returnOldRate = False, returnOldRequiredCredits = False, returnOldSalaryCalculationMethodCode = False, returnOldStepNumber = False, returnOldTRSStateBaseStep = False, returnOldTRSStateBaseStepAmount = False, returnPlacementCode = False, returnPlacementID = False, returnPlacementType = False, returnPlacementTypeCode = False, returnPlanPositionID = False, returnPositionGroupID = False, returnPositionIDClonedFrom = False, returnPositionIdentifier = False, returnPositionNumberCode = False, returnPositionNumberID = False, returnPositionTypeCodeDescription = False, returnPositionTypeID = False, returnRate = False, returnRequiredCredits = False, returnSalaryCalculationMethodCode = False, returnSalaryCalculationMethodID = False, returnStepNumber = False, returnTRSStateBaseStep = False, returnTRSStateBaseStepAmount = False, returnTRSStateBaseStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionEmployee/" + str(TempPlanPositionEmployeeID), verb = "get", return_params_list = return_params_list)

def modifyTempPlanPositionEmployee(TempPlanPositionEmployeeID, EntityID = 1, setAmountType = None, setAmountTypeCode = None, setAnnualPay = None, setAssignmentTypeCodes = None, setAssignmentTypeDescriptions = None, setBudgetedFTE = None, setBuildingCodes = None, setBuildingDescriptions = None, setCalendarCode = None, setCalendarID = None, setCappedAtMaximumRate = None, setConfigFiscalYearTRSStateBaseStepID = None, setConfigFiscalYearTRSStateBaseStepLaneCodeStepNumber = None, setDescription = None, setEmployeeFullNameLFM = None, setEmployeeID = None, setEmployeeNumber = None, setEmployeePlacementDescription = None, setEmployeePlacementID = None, setErrorMessage = None, setFormattedFullPaySecondsPerDay = None, setFullPaidDays = None, setFullPaySecondsPerDay = None, setHasFatalException = None, setJobTypeID = None, setLaneCode = None, setLaneID = None, setMatrixCode = None, setMatrixID = None, setMidpointGroup = None, setMidpointGroupCodeDescription = None, setMidpointGroupID = None, setOldAnnualPay = None, setOldBudgetedFTE = None, setOldCalendarCode = None, setOldEmployeePlacementDescription = None, setOldFormattedFullPaySecondsPerDay = None, setOldFullPaySecondsPerDay = None, setOldLaneCode = None, setOldMatrixCode = None, setOldMidpointGroup = None, setOldPlacementCode = None, setOldPlacementType = None, setOldPlacementTypeCode = None, setOldRate = None, setOldRequiredCredits = None, setOldSalaryCalculationMethodCode = None, setOldStepNumber = None, setOldTRSStateBaseStep = None, setOldTRSStateBaseStepAmount = None, setPlacementCode = None, setPlacementID = None, setPlacementType = None, setPlacementTypeCode = None, setPlanPositionID = None, setPositionGroupID = None, setPositionIDClonedFrom = None, setPositionIdentifier = None, setPositionNumberCode = None, setPositionNumberID = None, setPositionTypeCodeDescription = None, setPositionTypeID = None, setRate = None, setRequiredCredits = None, setSalaryCalculationMethodCode = None, setSalaryCalculationMethodID = None, setStepNumber = None, setTRSStateBaseStep = None, setTRSStateBaseStepAmount = None, setTRSStateBaseStepID = None, setRelationships = None, returnTempPlanPositionEmployeeID = True, returnAmountType = False, returnAmountTypeCode = False, returnAnnualPay = False, returnAssignmentTypeCodes = False, returnAssignmentTypeDescriptions = False, returnBudgetedFTE = False, returnBuildingCodes = False, returnBuildingDescriptions = False, returnCalendarCode = False, returnCalendarID = False, returnCappedAtMaximumRate = False, returnConfigFiscalYearTRSStateBaseStepID = False, returnConfigFiscalYearTRSStateBaseStepLaneCodeStepNumber = False, returnCreatedTime = False, returnDescription = False, returnEmployeeFullNameLFM = False, returnEmployeeID = False, returnEmployeeNumber = False, returnEmployeePlacementDescription = False, returnEmployeePlacementID = False, returnErrorMessage = False, returnFormattedFullPaySecondsPerDay = False, returnFullPaidDays = False, returnFullPaySecondsPerDay = False, returnHasFatalException = False, returnJobTypeID = False, returnLaneCode = False, returnLaneID = False, returnMatrixCode = False, returnMatrixID = False, returnMidpointGroup = False, returnMidpointGroupCodeDescription = False, returnMidpointGroupID = False, returnModifiedTime = False, returnOldAnnualPay = False, returnOldBudgetedFTE = False, returnOldCalendarCode = False, returnOldEmployeePlacementDescription = False, returnOldFormattedFullPaySecondsPerDay = False, returnOldFullPaySecondsPerDay = False, returnOldLaneCode = False, returnOldMatrixCode = False, returnOldMidpointGroup = False, returnOldPlacementCode = False, returnOldPlacementType = False, returnOldPlacementTypeCode = False, returnOldRate = False, returnOldRequiredCredits = False, returnOldSalaryCalculationMethodCode = False, returnOldStepNumber = False, returnOldTRSStateBaseStep = False, returnOldTRSStateBaseStepAmount = False, returnPlacementCode = False, returnPlacementID = False, returnPlacementType = False, returnPlacementTypeCode = False, returnPlanPositionID = False, returnPositionGroupID = False, returnPositionIDClonedFrom = False, returnPositionIdentifier = False, returnPositionNumberCode = False, returnPositionNumberID = False, returnPositionTypeCodeDescription = False, returnPositionTypeID = False, returnRate = False, returnRequiredCredits = False, returnSalaryCalculationMethodCode = False, returnSalaryCalculationMethodID = False, returnStepNumber = False, returnTRSStateBaseStep = False, returnTRSStateBaseStepAmount = False, returnTRSStateBaseStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionEmployee/" + str(TempPlanPositionEmployeeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempPlanPositionEmployee(EntityID = 1, setAmountType = None, setAmountTypeCode = None, setAnnualPay = None, setAssignmentTypeCodes = None, setAssignmentTypeDescriptions = None, setBudgetedFTE = None, setBuildingCodes = None, setBuildingDescriptions = None, setCalendarCode = None, setCalendarID = None, setCappedAtMaximumRate = None, setConfigFiscalYearTRSStateBaseStepID = None, setConfigFiscalYearTRSStateBaseStepLaneCodeStepNumber = None, setDescription = None, setEmployeeFullNameLFM = None, setEmployeeID = None, setEmployeeNumber = None, setEmployeePlacementDescription = None, setEmployeePlacementID = None, setErrorMessage = None, setFormattedFullPaySecondsPerDay = None, setFullPaidDays = None, setFullPaySecondsPerDay = None, setHasFatalException = None, setJobTypeID = None, setLaneCode = None, setLaneID = None, setMatrixCode = None, setMatrixID = None, setMidpointGroup = None, setMidpointGroupCodeDescription = None, setMidpointGroupID = None, setOldAnnualPay = None, setOldBudgetedFTE = None, setOldCalendarCode = None, setOldEmployeePlacementDescription = None, setOldFormattedFullPaySecondsPerDay = None, setOldFullPaySecondsPerDay = None, setOldLaneCode = None, setOldMatrixCode = None, setOldMidpointGroup = None, setOldPlacementCode = None, setOldPlacementType = None, setOldPlacementTypeCode = None, setOldRate = None, setOldRequiredCredits = None, setOldSalaryCalculationMethodCode = None, setOldStepNumber = None, setOldTRSStateBaseStep = None, setOldTRSStateBaseStepAmount = None, setPlacementCode = None, setPlacementID = None, setPlacementType = None, setPlacementTypeCode = None, setPlanPositionID = None, setPositionGroupID = None, setPositionIDClonedFrom = None, setPositionIdentifier = None, setPositionNumberCode = None, setPositionNumberID = None, setPositionTypeCodeDescription = None, setPositionTypeID = None, setRate = None, setRequiredCredits = None, setSalaryCalculationMethodCode = None, setSalaryCalculationMethodID = None, setStepNumber = None, setTRSStateBaseStep = None, setTRSStateBaseStepAmount = None, setTRSStateBaseStepID = None, setRelationships = None, returnTempPlanPositionEmployeeID = True, returnAmountType = False, returnAmountTypeCode = False, returnAnnualPay = False, returnAssignmentTypeCodes = False, returnAssignmentTypeDescriptions = False, returnBudgetedFTE = False, returnBuildingCodes = False, returnBuildingDescriptions = False, returnCalendarCode = False, returnCalendarID = False, returnCappedAtMaximumRate = False, returnConfigFiscalYearTRSStateBaseStepID = False, returnConfigFiscalYearTRSStateBaseStepLaneCodeStepNumber = False, returnCreatedTime = False, returnDescription = False, returnEmployeeFullNameLFM = False, returnEmployeeID = False, returnEmployeeNumber = False, returnEmployeePlacementDescription = False, returnEmployeePlacementID = False, returnErrorMessage = False, returnFormattedFullPaySecondsPerDay = False, returnFullPaidDays = False, returnFullPaySecondsPerDay = False, returnHasFatalException = False, returnJobTypeID = False, returnLaneCode = False, returnLaneID = False, returnMatrixCode = False, returnMatrixID = False, returnMidpointGroup = False, returnMidpointGroupCodeDescription = False, returnMidpointGroupID = False, returnModifiedTime = False, returnOldAnnualPay = False, returnOldBudgetedFTE = False, returnOldCalendarCode = False, returnOldEmployeePlacementDescription = False, returnOldFormattedFullPaySecondsPerDay = False, returnOldFullPaySecondsPerDay = False, returnOldLaneCode = False, returnOldMatrixCode = False, returnOldMidpointGroup = False, returnOldPlacementCode = False, returnOldPlacementType = False, returnOldPlacementTypeCode = False, returnOldRate = False, returnOldRequiredCredits = False, returnOldSalaryCalculationMethodCode = False, returnOldStepNumber = False, returnOldTRSStateBaseStep = False, returnOldTRSStateBaseStepAmount = False, returnPlacementCode = False, returnPlacementID = False, returnPlacementType = False, returnPlacementTypeCode = False, returnPlanPositionID = False, returnPositionGroupID = False, returnPositionIDClonedFrom = False, returnPositionIdentifier = False, returnPositionNumberCode = False, returnPositionNumberID = False, returnPositionTypeCodeDescription = False, returnPositionTypeID = False, returnRate = False, returnRequiredCredits = False, returnSalaryCalculationMethodCode = False, returnSalaryCalculationMethodID = False, returnStepNumber = False, returnTRSStateBaseStep = False, returnTRSStateBaseStepAmount = False, returnTRSStateBaseStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionEmployee/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempPlanPositionEmployee(TempPlanPositionEmployeeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempPlanPositionException(EntityID = 1, page = 1, pageSize = 100, returnTempPlanPositionExceptionID = True, returnCreatedTime = False, returnDescription = False, returnError = False, returnErrorType = False, returnErrorTypeCode = False, returnModifiedTime = False, returnPositionIdentifier = False, returnPositionNumberCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempPlanPositionException(TempPlanPositionExceptionID, EntityID = 1, returnTempPlanPositionExceptionID = True, returnCreatedTime = False, returnDescription = False, returnError = False, returnErrorType = False, returnErrorTypeCode = False, returnModifiedTime = False, returnPositionIdentifier = False, returnPositionNumberCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionException/" + str(TempPlanPositionExceptionID), verb = "get", return_params_list = return_params_list)

def modifyTempPlanPositionException(TempPlanPositionExceptionID, EntityID = 1, setDescription = None, setError = None, setErrorType = None, setErrorTypeCode = None, setPositionIdentifier = None, setPositionNumberCode = None, setRelationships = None, returnTempPlanPositionExceptionID = True, returnCreatedTime = False, returnDescription = False, returnError = False, returnErrorType = False, returnErrorTypeCode = False, returnModifiedTime = False, returnPositionIdentifier = False, returnPositionNumberCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionException/" + str(TempPlanPositionExceptionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempPlanPositionException(EntityID = 1, setDescription = None, setError = None, setErrorType = None, setErrorTypeCode = None, setPositionIdentifier = None, setPositionNumberCode = None, setRelationships = None, returnTempPlanPositionExceptionID = True, returnCreatedTime = False, returnDescription = False, returnError = False, returnErrorType = False, returnErrorTypeCode = False, returnModifiedTime = False, returnPositionIdentifier = False, returnPositionNumberCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionException/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempPlanPositionException(TempPlanPositionExceptionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempPlanPositionPay(EntityID = 1, page = 1, pageSize = 100, returnTempPlanPositionPayID = True, returnAccountDistributionString = False, returnAssignmentTypeCodes = False, returnAssignmentTypeDescriptions = False, returnBuildingCodes = False, returnBuildingDescriptions = False, returnCreatedTime = False, returnEmployeeFullNameLFM = False, returnEmployeeNumber = False, returnErrorCount = False, returnMatchingExpenditureEligibility = False, returnMatchingExpenditureEligibilityCode = False, returnModifiedTime = False, returnNewDisplayAccount = False, returnNewMatchingExpenditureEligibility = False, returnNewMatchingExpenditureEligibilityCode = False, returnOldDisplayAccount = False, returnPayScheduleCodeDescription = False, returnPayScheduleID = False, returnPayTypeCodeDescription = False, returnPayTypeID = False, returnPlanPositionPayID = False, returnPositionTypeCodeDescription = False, returnStipendAmount = False, returnTempPlanPositionEmployeeID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPay/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempPlanPositionPay(TempPlanPositionPayID, EntityID = 1, returnTempPlanPositionPayID = True, returnAccountDistributionString = False, returnAssignmentTypeCodes = False, returnAssignmentTypeDescriptions = False, returnBuildingCodes = False, returnBuildingDescriptions = False, returnCreatedTime = False, returnEmployeeFullNameLFM = False, returnEmployeeNumber = False, returnErrorCount = False, returnMatchingExpenditureEligibility = False, returnMatchingExpenditureEligibilityCode = False, returnModifiedTime = False, returnNewDisplayAccount = False, returnNewMatchingExpenditureEligibility = False, returnNewMatchingExpenditureEligibilityCode = False, returnOldDisplayAccount = False, returnPayScheduleCodeDescription = False, returnPayScheduleID = False, returnPayTypeCodeDescription = False, returnPayTypeID = False, returnPlanPositionPayID = False, returnPositionTypeCodeDescription = False, returnStipendAmount = False, returnTempPlanPositionEmployeeID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPay/" + str(TempPlanPositionPayID), verb = "get", return_params_list = return_params_list)

def modifyTempPlanPositionPay(TempPlanPositionPayID, EntityID = 1, setAccountDistributionString = None, setAssignmentTypeCodes = None, setAssignmentTypeDescriptions = None, setBuildingCodes = None, setBuildingDescriptions = None, setEmployeeFullNameLFM = None, setEmployeeNumber = None, setErrorCount = None, setMatchingExpenditureEligibility = None, setMatchingExpenditureEligibilityCode = None, setNewDisplayAccount = None, setNewMatchingExpenditureEligibility = None, setNewMatchingExpenditureEligibilityCode = None, setOldDisplayAccount = None, setPayScheduleCodeDescription = None, setPayScheduleID = None, setPayTypeCodeDescription = None, setPayTypeID = None, setPlanPositionPayID = None, setPositionTypeCodeDescription = None, setStipendAmount = None, setTempPlanPositionEmployeeID = None, setType = None, setTypeCode = None, setRelationships = None, returnTempPlanPositionPayID = True, returnAccountDistributionString = False, returnAssignmentTypeCodes = False, returnAssignmentTypeDescriptions = False, returnBuildingCodes = False, returnBuildingDescriptions = False, returnCreatedTime = False, returnEmployeeFullNameLFM = False, returnEmployeeNumber = False, returnErrorCount = False, returnMatchingExpenditureEligibility = False, returnMatchingExpenditureEligibilityCode = False, returnModifiedTime = False, returnNewDisplayAccount = False, returnNewMatchingExpenditureEligibility = False, returnNewMatchingExpenditureEligibilityCode = False, returnOldDisplayAccount = False, returnPayScheduleCodeDescription = False, returnPayScheduleID = False, returnPayTypeCodeDescription = False, returnPayTypeID = False, returnPlanPositionPayID = False, returnPositionTypeCodeDescription = False, returnStipendAmount = False, returnTempPlanPositionEmployeeID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPay/" + str(TempPlanPositionPayID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempPlanPositionPay(EntityID = 1, setAccountDistributionString = None, setAssignmentTypeCodes = None, setAssignmentTypeDescriptions = None, setBuildingCodes = None, setBuildingDescriptions = None, setEmployeeFullNameLFM = None, setEmployeeNumber = None, setErrorCount = None, setMatchingExpenditureEligibility = None, setMatchingExpenditureEligibilityCode = None, setNewDisplayAccount = None, setNewMatchingExpenditureEligibility = None, setNewMatchingExpenditureEligibilityCode = None, setOldDisplayAccount = None, setPayScheduleCodeDescription = None, setPayScheduleID = None, setPayTypeCodeDescription = None, setPayTypeID = None, setPlanPositionPayID = None, setPositionTypeCodeDescription = None, setStipendAmount = None, setTempPlanPositionEmployeeID = None, setType = None, setTypeCode = None, setRelationships = None, returnTempPlanPositionPayID = True, returnAccountDistributionString = False, returnAssignmentTypeCodes = False, returnAssignmentTypeDescriptions = False, returnBuildingCodes = False, returnBuildingDescriptions = False, returnCreatedTime = False, returnEmployeeFullNameLFM = False, returnEmployeeNumber = False, returnErrorCount = False, returnMatchingExpenditureEligibility = False, returnMatchingExpenditureEligibilityCode = False, returnModifiedTime = False, returnNewDisplayAccount = False, returnNewMatchingExpenditureEligibility = False, returnNewMatchingExpenditureEligibilityCode = False, returnOldDisplayAccount = False, returnPayScheduleCodeDescription = False, returnPayScheduleID = False, returnPayTypeCodeDescription = False, returnPayTypeID = False, returnPlanPositionPayID = False, returnPositionTypeCodeDescription = False, returnStipendAmount = False, returnTempPlanPositionEmployeeID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPay/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempPlanPositionPay(TempPlanPositionPayID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempPlanPositionPayAccountCalculation(EntityID = 1, page = 1, pageSize = 100, returnTempPlanPositionPayAccountCalculationID = True, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayAccountCalculation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempPlanPositionPayAccountCalculation(TempPlanPositionPayAccountCalculationID, EntityID = 1, returnTempPlanPositionPayAccountCalculationID = True, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayAccountCalculation/" + str(TempPlanPositionPayAccountCalculationID), verb = "get", return_params_list = return_params_list)

def modifyTempPlanPositionPayAccountCalculation(TempPlanPositionPayAccountCalculationID, EntityID = 1, setAnnualAmount = None, setPlanPositionPayAccountDistributionID = None, setRelationships = None, returnTempPlanPositionPayAccountCalculationID = True, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayAccountCalculation/" + str(TempPlanPositionPayAccountCalculationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempPlanPositionPayAccountCalculation(EntityID = 1, setAnnualAmount = None, setPlanPositionPayAccountDistributionID = None, setRelationships = None, returnTempPlanPositionPayAccountCalculationID = True, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayAccountCalculation/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempPlanPositionPayAccountCalculation(TempPlanPositionPayAccountCalculationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempPlanPositionPayAccountDistribution(EntityID = 1, page = 1, pageSize = 100, returnTempPlanPositionPayAccountDistributionID = True, returnAccountID = False, returnCreatedTime = False, returnDisplayAccount = False, returnDistributionPercent = False, returnModifiedTime = False, returnPlanPositionPayID = False, returnTempPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayAccountDistribution/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempPlanPositionPayAccountDistribution(TempPlanPositionPayAccountDistributionID, EntityID = 1, returnTempPlanPositionPayAccountDistributionID = True, returnAccountID = False, returnCreatedTime = False, returnDisplayAccount = False, returnDistributionPercent = False, returnModifiedTime = False, returnPlanPositionPayID = False, returnTempPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayAccountDistribution/" + str(TempPlanPositionPayAccountDistributionID), verb = "get", return_params_list = return_params_list)

def modifyTempPlanPositionPayAccountDistribution(TempPlanPositionPayAccountDistributionID, EntityID = 1, setAccountID = None, setDisplayAccount = None, setDistributionPercent = None, setPlanPositionPayID = None, setTempPlanPositionPayID = None, setRelationships = None, returnTempPlanPositionPayAccountDistributionID = True, returnAccountID = False, returnCreatedTime = False, returnDisplayAccount = False, returnDistributionPercent = False, returnModifiedTime = False, returnPlanPositionPayID = False, returnTempPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayAccountDistribution/" + str(TempPlanPositionPayAccountDistributionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempPlanPositionPayAccountDistribution(EntityID = 1, setAccountID = None, setDisplayAccount = None, setDistributionPercent = None, setPlanPositionPayID = None, setTempPlanPositionPayID = None, setRelationships = None, returnTempPlanPositionPayAccountDistributionID = True, returnAccountID = False, returnCreatedTime = False, returnDisplayAccount = False, returnDistributionPercent = False, returnModifiedTime = False, returnPlanPositionPayID = False, returnTempPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayAccountDistribution/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempPlanPositionPayAccountDistribution(TempPlanPositionPayAccountDistributionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempPlanPositionPayBenefit(EntityID = 1, page = 1, pageSize = 100, returnTempPlanPositionPayBenefitID = True, returnBenefitCodeDescription = False, returnCreatedTime = False, returnEmployeeNumber = False, returnErrorCount = False, returnModifiedTime = False, returnPayScheduleCodeDescription = False, returnPayTypeCodeDescription = False, returnPlanPositionEmployeeName = False, returnPlanPositionPayBenefitID = False, returnPlanPositionPayID = False, returnPositionTypeDescription = False, returnTempPlanPositionBenefitID = False, returnTempPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayBenefit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempPlanPositionPayBenefit(TempPlanPositionPayBenefitID, EntityID = 1, returnTempPlanPositionPayBenefitID = True, returnBenefitCodeDescription = False, returnCreatedTime = False, returnEmployeeNumber = False, returnErrorCount = False, returnModifiedTime = False, returnPayScheduleCodeDescription = False, returnPayTypeCodeDescription = False, returnPlanPositionEmployeeName = False, returnPlanPositionPayBenefitID = False, returnPlanPositionPayID = False, returnPositionTypeDescription = False, returnTempPlanPositionBenefitID = False, returnTempPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayBenefit/" + str(TempPlanPositionPayBenefitID), verb = "get", return_params_list = return_params_list)

def modifyTempPlanPositionPayBenefit(TempPlanPositionPayBenefitID, EntityID = 1, setBenefitCodeDescription = None, setEmployeeNumber = None, setErrorCount = None, setPayScheduleCodeDescription = None, setPayTypeCodeDescription = None, setPlanPositionEmployeeName = None, setPlanPositionPayBenefitID = None, setPlanPositionPayID = None, setPositionTypeDescription = None, setTempPlanPositionBenefitID = None, setTempPlanPositionPayID = None, setRelationships = None, returnTempPlanPositionPayBenefitID = True, returnBenefitCodeDescription = False, returnCreatedTime = False, returnEmployeeNumber = False, returnErrorCount = False, returnModifiedTime = False, returnPayScheduleCodeDescription = False, returnPayTypeCodeDescription = False, returnPlanPositionEmployeeName = False, returnPlanPositionPayBenefitID = False, returnPlanPositionPayID = False, returnPositionTypeDescription = False, returnTempPlanPositionBenefitID = False, returnTempPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayBenefit/" + str(TempPlanPositionPayBenefitID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempPlanPositionPayBenefit(EntityID = 1, setBenefitCodeDescription = None, setEmployeeNumber = None, setErrorCount = None, setPayScheduleCodeDescription = None, setPayTypeCodeDescription = None, setPlanPositionEmployeeName = None, setPlanPositionPayBenefitID = None, setPlanPositionPayID = None, setPositionTypeDescription = None, setTempPlanPositionBenefitID = None, setTempPlanPositionPayID = None, setRelationships = None, returnTempPlanPositionPayBenefitID = True, returnBenefitCodeDescription = False, returnCreatedTime = False, returnEmployeeNumber = False, returnErrorCount = False, returnModifiedTime = False, returnPayScheduleCodeDescription = False, returnPayTypeCodeDescription = False, returnPlanPositionEmployeeName = False, returnPlanPositionPayBenefitID = False, returnPlanPositionPayID = False, returnPositionTypeDescription = False, returnTempPlanPositionBenefitID = False, returnTempPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayBenefit/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempPlanPositionPayBenefit(TempPlanPositionPayBenefitID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempPlanPositionPayBenefitAccount(EntityID = 1, page = 1, pageSize = 100, returnTempPlanPositionPayBenefitAccountID = True, returnAccountID = False, returnAnnualAmount = False, returnCreatedTime = False, returnDisplayAccount = False, returnIsAccountPreviouslyCreated = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnPlanPositionPayBenefitID = False, returnTempPlanPositionPayBenefitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayBenefitAccount/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempPlanPositionPayBenefitAccount(TempPlanPositionPayBenefitAccountID, EntityID = 1, returnTempPlanPositionPayBenefitAccountID = True, returnAccountID = False, returnAnnualAmount = False, returnCreatedTime = False, returnDisplayAccount = False, returnIsAccountPreviouslyCreated = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnPlanPositionPayBenefitID = False, returnTempPlanPositionPayBenefitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayBenefitAccount/" + str(TempPlanPositionPayBenefitAccountID), verb = "get", return_params_list = return_params_list)

def modifyTempPlanPositionPayBenefitAccount(TempPlanPositionPayBenefitAccountID, EntityID = 1, setAccountID = None, setAnnualAmount = None, setDisplayAccount = None, setIsAccountPreviouslyCreated = None, setPlanPositionPayAccountDistributionID = None, setPlanPositionPayBenefitID = None, setTempPlanPositionPayBenefitID = None, setRelationships = None, returnTempPlanPositionPayBenefitAccountID = True, returnAccountID = False, returnAnnualAmount = False, returnCreatedTime = False, returnDisplayAccount = False, returnIsAccountPreviouslyCreated = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnPlanPositionPayBenefitID = False, returnTempPlanPositionPayBenefitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayBenefitAccount/" + str(TempPlanPositionPayBenefitAccountID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempPlanPositionPayBenefitAccount(EntityID = 1, setAccountID = None, setAnnualAmount = None, setDisplayAccount = None, setIsAccountPreviouslyCreated = None, setPlanPositionPayAccountDistributionID = None, setPlanPositionPayBenefitID = None, setTempPlanPositionPayBenefitID = None, setRelationships = None, returnTempPlanPositionPayBenefitAccountID = True, returnAccountID = False, returnAnnualAmount = False, returnCreatedTime = False, returnDisplayAccount = False, returnIsAccountPreviouslyCreated = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnPlanPositionPayBenefitID = False, returnTempPlanPositionPayBenefitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayBenefitAccount/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempPlanPositionPayBenefitAccount(TempPlanPositionPayBenefitAccountID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempPlanPositionSupplement(EntityID = 1, page = 1, pageSize = 100, returnTempPlanPositionSupplementID = True, returnAnnualPay = False, returnCreatedTime = False, returnErrorCount = False, returnModifiedTime = False, returnOldAnnualPay = False, returnOldRate = False, returnOldSupplementTypeAmountType = False, returnOldSupplementTypeCodeDescription = False, returnPlanPositionDistributionsAssignmentTypeCodes = False, returnPlanPositionDistributionsBuildingCodes = False, returnPlanPositionEmployeeName = False, returnPlanPositionEmployeeNumber = False, returnPlanPositionID = False, returnPlanPositionNewAnnualPay = False, returnPlanPositionOldAnnualPay = False, returnPlanPositionPositionTypeCodeDescription = False, returnPlanPositionSupplementID = False, returnRate = False, returnSupplementTypeAmountType = False, returnSupplementTypeCodeDescription = False, returnSupplementTypeID = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionSupplement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempPlanPositionSupplement(TempPlanPositionSupplementID, EntityID = 1, returnTempPlanPositionSupplementID = True, returnAnnualPay = False, returnCreatedTime = False, returnErrorCount = False, returnModifiedTime = False, returnOldAnnualPay = False, returnOldRate = False, returnOldSupplementTypeAmountType = False, returnOldSupplementTypeCodeDescription = False, returnPlanPositionDistributionsAssignmentTypeCodes = False, returnPlanPositionDistributionsBuildingCodes = False, returnPlanPositionEmployeeName = False, returnPlanPositionEmployeeNumber = False, returnPlanPositionID = False, returnPlanPositionNewAnnualPay = False, returnPlanPositionOldAnnualPay = False, returnPlanPositionPositionTypeCodeDescription = False, returnPlanPositionSupplementID = False, returnRate = False, returnSupplementTypeAmountType = False, returnSupplementTypeCodeDescription = False, returnSupplementTypeID = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionSupplement/" + str(TempPlanPositionSupplementID), verb = "get", return_params_list = return_params_list)

def modifyTempPlanPositionSupplement(TempPlanPositionSupplementID, EntityID = 1, setAnnualPay = None, setErrorCount = None, setOldAnnualPay = None, setOldRate = None, setOldSupplementTypeAmountType = None, setOldSupplementTypeCodeDescription = None, setPlanPositionDistributionsAssignmentTypeCodes = None, setPlanPositionDistributionsBuildingCodes = None, setPlanPositionEmployeeName = None, setPlanPositionEmployeeNumber = None, setPlanPositionID = None, setPlanPositionNewAnnualPay = None, setPlanPositionOldAnnualPay = None, setPlanPositionPositionTypeCodeDescription = None, setPlanPositionSupplementID = None, setRate = None, setSupplementTypeAmountType = None, setSupplementTypeCodeDescription = None, setSupplementTypeID = None, setTempPlanPositionEmployeeID = None, setRelationships = None, returnTempPlanPositionSupplementID = True, returnAnnualPay = False, returnCreatedTime = False, returnErrorCount = False, returnModifiedTime = False, returnOldAnnualPay = False, returnOldRate = False, returnOldSupplementTypeAmountType = False, returnOldSupplementTypeCodeDescription = False, returnPlanPositionDistributionsAssignmentTypeCodes = False, returnPlanPositionDistributionsBuildingCodes = False, returnPlanPositionEmployeeName = False, returnPlanPositionEmployeeNumber = False, returnPlanPositionID = False, returnPlanPositionNewAnnualPay = False, returnPlanPositionOldAnnualPay = False, returnPlanPositionPositionTypeCodeDescription = False, returnPlanPositionSupplementID = False, returnRate = False, returnSupplementTypeAmountType = False, returnSupplementTypeCodeDescription = False, returnSupplementTypeID = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionSupplement/" + str(TempPlanPositionSupplementID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempPlanPositionSupplement(EntityID = 1, setAnnualPay = None, setErrorCount = None, setOldAnnualPay = None, setOldRate = None, setOldSupplementTypeAmountType = None, setOldSupplementTypeCodeDescription = None, setPlanPositionDistributionsAssignmentTypeCodes = None, setPlanPositionDistributionsBuildingCodes = None, setPlanPositionEmployeeName = None, setPlanPositionEmployeeNumber = None, setPlanPositionID = None, setPlanPositionNewAnnualPay = None, setPlanPositionOldAnnualPay = None, setPlanPositionPositionTypeCodeDescription = None, setPlanPositionSupplementID = None, setRate = None, setSupplementTypeAmountType = None, setSupplementTypeCodeDescription = None, setSupplementTypeID = None, setTempPlanPositionEmployeeID = None, setRelationships = None, returnTempPlanPositionSupplementID = True, returnAnnualPay = False, returnCreatedTime = False, returnErrorCount = False, returnModifiedTime = False, returnOldAnnualPay = False, returnOldRate = False, returnOldSupplementTypeAmountType = False, returnOldSupplementTypeCodeDescription = False, returnPlanPositionDistributionsAssignmentTypeCodes = False, returnPlanPositionDistributionsBuildingCodes = False, returnPlanPositionEmployeeName = False, returnPlanPositionEmployeeNumber = False, returnPlanPositionID = False, returnPlanPositionNewAnnualPay = False, returnPlanPositionOldAnnualPay = False, returnPlanPositionPositionTypeCodeDescription = False, returnPlanPositionSupplementID = False, returnRate = False, returnSupplementTypeAmountType = False, returnSupplementTypeCodeDescription = False, returnSupplementTypeID = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionSupplement/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempPlanPositionSupplement(TempPlanPositionSupplementID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")