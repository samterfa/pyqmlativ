# This module contains District functions.

from .Utilities import make_request

import pandas as pd

import json

import re

def getEveryBuilding(EntityID = 1, page = 1, pageSize = 100, returnBuildingID = True, returnAccountDistributionString = False, returnAddressID = False, returnBuildingMNID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnFederalNCESSchoolID = False, returnMaximumStudentCount = False, returnMinimumStudentCount = False, returnModifiedTime = False, returnOptimumStudentCount = False, returnParcelNumber = False, returnSTARSchoolNumber = False, returnUnemploymentInsuranceUnitLocation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Building/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getBuilding(BuildingID, EntityID = 1, returnBuildingID = True, returnAccountDistributionString = False, returnAddressID = False, returnBuildingMNID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnFederalNCESSchoolID = False, returnMaximumStudentCount = False, returnMinimumStudentCount = False, returnModifiedTime = False, returnOptimumStudentCount = False, returnParcelNumber = False, returnSTARSchoolNumber = False, returnUnemploymentInsuranceUnitLocation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Building/" + str(BuildingID), verb = "get", return_params_list = return_params_list)

def modifyBuilding(BuildingID, EntityID = 1, setAddressID = None, setCode = None, setDescription = None, setDistrictID = None, setFederalNCESSchoolID = None, setMaximumStudentCount = None, setMinimumStudentCount = None, setOptimumStudentCount = None, setParcelNumber = None, setSTARSchoolNumber = None, setUnemploymentInsuranceUnitLocation = None, setRelationships = None, returnBuildingID = True, returnAccountDistributionString = False, returnAddressID = False, returnBuildingMNID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnFederalNCESSchoolID = False, returnMaximumStudentCount = False, returnMinimumStudentCount = False, returnModifiedTime = False, returnOptimumStudentCount = False, returnParcelNumber = False, returnSTARSchoolNumber = False, returnUnemploymentInsuranceUnitLocation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Building/" + str(BuildingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createBuilding(EntityID = 1, setAddressID = None, setCode = None, setDescription = None, setDistrictID = None, setFederalNCESSchoolID = None, setMaximumStudentCount = None, setMinimumStudentCount = None, setOptimumStudentCount = None, setParcelNumber = None, setSTARSchoolNumber = None, setUnemploymentInsuranceUnitLocation = None, setRelationships = None, returnBuildingID = True, returnAccountDistributionString = False, returnAddressID = False, returnBuildingMNID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnFederalNCESSchoolID = False, returnMaximumStudentCount = False, returnMinimumStudentCount = False, returnModifiedTime = False, returnOptimumStudentCount = False, returnParcelNumber = False, returnSTARSchoolNumber = False, returnUnemploymentInsuranceUnitLocation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Building/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteBuilding(BuildingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCalendarYear(EntityID = 1, page = 1, pageSize = 100, returnCalendarYearID = True, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnNumericYear = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/CalendarYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCalendarYear(CalendarYearID, EntityID = 1, returnCalendarYearID = True, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnNumericYear = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/CalendarYear/" + str(CalendarYearID), verb = "get", return_params_list = return_params_list)

def modifyCalendarYear(CalendarYearID, EntityID = 1, setDescription = None, setNumericYear = None, setRelationships = None, returnCalendarYearID = True, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnNumericYear = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/CalendarYear/" + str(CalendarYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCalendarYear(EntityID = 1, setDescription = None, setNumericYear = None, setRelationships = None, returnCalendarYearID = True, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnNumericYear = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/CalendarYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCalendarYear(CalendarYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigEntityYear(EntityID = 1, page = 1, pageSize = 100, returnConfigEntityYearID = True, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/ConfigEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigEntityYear(ConfigEntityYearID, EntityID = 1, returnConfigEntityYearID = True, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/ConfigEntityYear/" + str(ConfigEntityYearID), verb = "get", return_params_list = return_params_list)

def modifyConfigEntityYear(ConfigEntityYearID, EntityID = 1, setConfigEntityYearIDClonedFrom = None, setEntityID = None, setSchoolYearID = None, setRelationships = None, returnConfigEntityYearID = True, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/ConfigEntityYear/" + str(ConfigEntityYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigEntityYear(EntityID = 1, setConfigEntityYearIDClonedFrom = None, setEntityID = None, setSchoolYearID = None, setRelationships = None, returnConfigEntityYearID = True, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/ConfigEntityYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigEntityYear(ConfigEntityYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDistrictGroup(EntityID = 1, page = 1, pageSize = 100, returnDistrictGroupID = True, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDistrictGroup(DistrictGroupID, EntityID = 1, returnDistrictGroupID = True, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictGroup/" + str(DistrictGroupID), verb = "get", return_params_list = return_params_list)

def modifyDistrictGroup(DistrictGroupID, EntityID = 1, setName = None, setRelationships = None, returnDistrictGroupID = True, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictGroup/" + str(DistrictGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDistrictGroup(EntityID = 1, setName = None, setRelationships = None, returnDistrictGroupID = True, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDistrictGroup(DistrictGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDistrict(EntityID = 1, page = 1, pageSize = 100, returnDistrictID = True, returnBuildingID = False, returnCodeName = False, returnCreatedTime = False, returnDistrictCodeBySchoolYear = False, returnDistrictGroupID = False, returnDistrictMNID = False, returnDistrictNumber = False, returnFaxNumber = False, returnFaxNumberIsInternational = False, returnFormattedPhoneNumber = False, returnModifiedTime = False, returnName = False, returnNCESIDCode = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnRCDTCodeBySchoolYear = False, returnStaffIDSuperintendent = False, returnStateDistrictCode = False, returnStateDistrictMNID = False, returnStateDistrictTypeCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/District/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDistrict(DistrictID, EntityID = 1, returnDistrictID = True, returnBuildingID = False, returnCodeName = False, returnCreatedTime = False, returnDistrictCodeBySchoolYear = False, returnDistrictGroupID = False, returnDistrictMNID = False, returnDistrictNumber = False, returnFaxNumber = False, returnFaxNumberIsInternational = False, returnFormattedPhoneNumber = False, returnModifiedTime = False, returnName = False, returnNCESIDCode = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnRCDTCodeBySchoolYear = False, returnStaffIDSuperintendent = False, returnStateDistrictCode = False, returnStateDistrictMNID = False, returnStateDistrictTypeCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/District/" + str(DistrictID), verb = "get", return_params_list = return_params_list)

def modifyDistrict(DistrictID, EntityID = 1, setBuildingID = None, setDistrictGroupID = None, setDistrictNumber = None, setFaxNumber = None, setFaxNumberIsInternational = None, setName = None, setNCESIDCode = None, setPhoneNumber = None, setPhoneNumberIsInternational = None, setStaffIDSuperintendent = None, setStateDistrictMNID = None, setStateDistrictTypeCodeMNID = None, setRelationships = None, returnDistrictID = True, returnBuildingID = False, returnCodeName = False, returnCreatedTime = False, returnDistrictCodeBySchoolYear = False, returnDistrictGroupID = False, returnDistrictMNID = False, returnDistrictNumber = False, returnFaxNumber = False, returnFaxNumberIsInternational = False, returnFormattedPhoneNumber = False, returnModifiedTime = False, returnName = False, returnNCESIDCode = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnRCDTCodeBySchoolYear = False, returnStaffIDSuperintendent = False, returnStateDistrictCode = False, returnStateDistrictMNID = False, returnStateDistrictTypeCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/District/" + str(DistrictID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDistrict(EntityID = 1, setBuildingID = None, setDistrictGroupID = None, setDistrictNumber = None, setFaxNumber = None, setFaxNumberIsInternational = None, setName = None, setNCESIDCode = None, setPhoneNumber = None, setPhoneNumberIsInternational = None, setStaffIDSuperintendent = None, setStateDistrictMNID = None, setStateDistrictTypeCodeMNID = None, setRelationships = None, returnDistrictID = True, returnBuildingID = False, returnCodeName = False, returnCreatedTime = False, returnDistrictCodeBySchoolYear = False, returnDistrictGroupID = False, returnDistrictMNID = False, returnDistrictNumber = False, returnFaxNumber = False, returnFaxNumberIsInternational = False, returnFormattedPhoneNumber = False, returnModifiedTime = False, returnName = False, returnNCESIDCode = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnRCDTCodeBySchoolYear = False, returnStaffIDSuperintendent = False, returnStateDistrictCode = False, returnStateDistrictMNID = False, returnStateDistrictTypeCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/District/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDistrict(DistrictID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDistrictSchoolYear(EntityID = 1, page = 1, pageSize = 100, returnDistrictSchoolYearID = True, returnCreatedTime = False, returnDistrictID = False, returnDistrictSchoolYearIDClonedFrom = False, returnEdFiDistrictID = False, returnHarassmentPolicyWebLink = False, returnHasDesegregationPlan = False, returnHasDistanceEducation = False, returnHasEarlyChildhood = False, returnHasEarlyChildhoodNonIDEA = False, returnHasGEDPreparationProgram = False, returnHasHarassmentPolicy = False, returnHasKindergarten = False, returnHasKindergartenFullDayCost = False, returnHasKindergartenFullDayFree = False, returnHasKindergartenPartDayCost = False, returnHasKindergartenPartDayFree = False, returnHasPreschool = False, returnHasPreschoolAllChildren = False, returnHasPreschoolFullDayCost = False, returnHasPreschoolFullDayFree = False, returnHasPreschoolIDEA = False, returnHasPreschoolLowIncome = False, returnHasPreschoolPartDayCost = False, returnHasPreschoolPartDayFree = False, returnHasPreschoolTitleI = False, returnIsCRDCCollectedForSchoolYear = False, returnModifiedTime = False, returnNameIDDisability = False, returnNameIDRace = False, returnNameIDSex = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictSchoolYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDistrictSchoolYear(DistrictSchoolYearID, EntityID = 1, returnDistrictSchoolYearID = True, returnCreatedTime = False, returnDistrictID = False, returnDistrictSchoolYearIDClonedFrom = False, returnEdFiDistrictID = False, returnHarassmentPolicyWebLink = False, returnHasDesegregationPlan = False, returnHasDistanceEducation = False, returnHasEarlyChildhood = False, returnHasEarlyChildhoodNonIDEA = False, returnHasGEDPreparationProgram = False, returnHasHarassmentPolicy = False, returnHasKindergarten = False, returnHasKindergartenFullDayCost = False, returnHasKindergartenFullDayFree = False, returnHasKindergartenPartDayCost = False, returnHasKindergartenPartDayFree = False, returnHasPreschool = False, returnHasPreschoolAllChildren = False, returnHasPreschoolFullDayCost = False, returnHasPreschoolFullDayFree = False, returnHasPreschoolIDEA = False, returnHasPreschoolLowIncome = False, returnHasPreschoolPartDayCost = False, returnHasPreschoolPartDayFree = False, returnHasPreschoolTitleI = False, returnIsCRDCCollectedForSchoolYear = False, returnModifiedTime = False, returnNameIDDisability = False, returnNameIDRace = False, returnNameIDSex = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictSchoolYear/" + str(DistrictSchoolYearID), verb = "get", return_params_list = return_params_list)

def modifyDistrictSchoolYear(DistrictSchoolYearID, EntityID = 1, setDistrictID = None, setDistrictSchoolYearIDClonedFrom = None, setEdFiDistrictID = None, setHarassmentPolicyWebLink = None, setHasDesegregationPlan = None, setHasDistanceEducation = None, setHasEarlyChildhood = None, setHasEarlyChildhoodNonIDEA = None, setHasGEDPreparationProgram = None, setHasHarassmentPolicy = None, setHasKindergarten = None, setHasKindergartenFullDayCost = None, setHasKindergartenFullDayFree = None, setHasKindergartenPartDayCost = None, setHasKindergartenPartDayFree = None, setHasPreschool = None, setHasPreschoolAllChildren = None, setHasPreschoolFullDayCost = None, setHasPreschoolFullDayFree = None, setHasPreschoolIDEA = None, setHasPreschoolLowIncome = None, setHasPreschoolPartDayCost = None, setHasPreschoolPartDayFree = None, setHasPreschoolTitleI = None, setNameIDDisability = None, setNameIDRace = None, setNameIDSex = None, setSchoolYearID = None, setRelationships = None, returnDistrictSchoolYearID = True, returnCreatedTime = False, returnDistrictID = False, returnDistrictSchoolYearIDClonedFrom = False, returnEdFiDistrictID = False, returnHarassmentPolicyWebLink = False, returnHasDesegregationPlan = False, returnHasDistanceEducation = False, returnHasEarlyChildhood = False, returnHasEarlyChildhoodNonIDEA = False, returnHasGEDPreparationProgram = False, returnHasHarassmentPolicy = False, returnHasKindergarten = False, returnHasKindergartenFullDayCost = False, returnHasKindergartenFullDayFree = False, returnHasKindergartenPartDayCost = False, returnHasKindergartenPartDayFree = False, returnHasPreschool = False, returnHasPreschoolAllChildren = False, returnHasPreschoolFullDayCost = False, returnHasPreschoolFullDayFree = False, returnHasPreschoolIDEA = False, returnHasPreschoolLowIncome = False, returnHasPreschoolPartDayCost = False, returnHasPreschoolPartDayFree = False, returnHasPreschoolTitleI = False, returnIsCRDCCollectedForSchoolYear = False, returnModifiedTime = False, returnNameIDDisability = False, returnNameIDRace = False, returnNameIDSex = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictSchoolYear/" + str(DistrictSchoolYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDistrictSchoolYear(EntityID = 1, setDistrictID = None, setDistrictSchoolYearIDClonedFrom = None, setEdFiDistrictID = None, setHarassmentPolicyWebLink = None, setHasDesegregationPlan = None, setHasDistanceEducation = None, setHasEarlyChildhood = None, setHasEarlyChildhoodNonIDEA = None, setHasGEDPreparationProgram = None, setHasHarassmentPolicy = None, setHasKindergarten = None, setHasKindergartenFullDayCost = None, setHasKindergartenFullDayFree = None, setHasKindergartenPartDayCost = None, setHasKindergartenPartDayFree = None, setHasPreschool = None, setHasPreschoolAllChildren = None, setHasPreschoolFullDayCost = None, setHasPreschoolFullDayFree = None, setHasPreschoolIDEA = None, setHasPreschoolLowIncome = None, setHasPreschoolPartDayCost = None, setHasPreschoolPartDayFree = None, setHasPreschoolTitleI = None, setNameIDDisability = None, setNameIDRace = None, setNameIDSex = None, setSchoolYearID = None, setRelationships = None, returnDistrictSchoolYearID = True, returnCreatedTime = False, returnDistrictID = False, returnDistrictSchoolYearIDClonedFrom = False, returnEdFiDistrictID = False, returnHarassmentPolicyWebLink = False, returnHasDesegregationPlan = False, returnHasDistanceEducation = False, returnHasEarlyChildhood = False, returnHasEarlyChildhoodNonIDEA = False, returnHasGEDPreparationProgram = False, returnHasHarassmentPolicy = False, returnHasKindergarten = False, returnHasKindergartenFullDayCost = False, returnHasKindergartenFullDayFree = False, returnHasKindergartenPartDayCost = False, returnHasKindergartenPartDayFree = False, returnHasPreschool = False, returnHasPreschoolAllChildren = False, returnHasPreschoolFullDayCost = False, returnHasPreschoolFullDayFree = False, returnHasPreschoolIDEA = False, returnHasPreschoolLowIncome = False, returnHasPreschoolPartDayCost = False, returnHasPreschoolPartDayFree = False, returnHasPreschoolTitleI = False, returnIsCRDCCollectedForSchoolYear = False, returnModifiedTime = False, returnNameIDDisability = False, returnNameIDRace = False, returnNameIDSex = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictSchoolYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDistrictSchoolYear(DistrictSchoolYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEntityGroup(EntityID = 1, page = 1, pageSize = 100, returnEntityGroupID = True, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEntityGroup(EntityGroupID, EntityID = 1, returnEntityGroupID = True, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroup/" + str(EntityGroupID), verb = "get", return_params_list = return_params_list)

def modifyEntityGroup(EntityGroupID, EntityID = 1, setDistrictID = None, setName = None, setRelationships = None, returnEntityGroupID = True, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroup/" + str(EntityGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEntityGroup(EntityID = 1, setDistrictID = None, setName = None, setRelationships = None, returnEntityGroupID = True, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEntityGroup(EntityGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEntityGroupEntity(EntityID = 1, page = 1, pageSize = 100, returnEntityGroupEntityID = True, returnCreatedTime = False, returnEntityGroupID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEntityGroupEntity(EntityGroupEntityID, EntityID = 1, returnEntityGroupEntityID = True, returnCreatedTime = False, returnEntityGroupID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupEntity/" + str(EntityGroupEntityID), verb = "get", return_params_list = return_params_list)

def modifyEntityGroupEntity(EntityGroupEntityID, EntityID = 1, setEntityGroupID = None, setEntityID = None, setSchoolYearID = None, setRelationships = None, returnEntityGroupEntityID = True, returnCreatedTime = False, returnEntityGroupID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupEntity/" + str(EntityGroupEntityID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEntityGroupEntity(EntityID = 1, setEntityGroupID = None, setEntityID = None, setSchoolYearID = None, setRelationships = None, returnEntityGroupEntityID = True, returnCreatedTime = False, returnEntityGroupID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupEntity/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEntityGroupEntity(EntityGroupEntityID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEntityGroupSetup(EntityID = 1, page = 1, pageSize = 100, returnEntityGroupSetupID = True, returnCreatedTime = False, returnEffectiveGroupName = False, returnEntityGroupID = False, returnEntityIDPrimary = False, returnHasBeenProcessed = False, returnModifiedTime = False, returnNewGroupName = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEntityGroupSetup(EntityGroupSetupID, EntityID = 1, returnEntityGroupSetupID = True, returnCreatedTime = False, returnEffectiveGroupName = False, returnEntityGroupID = False, returnEntityIDPrimary = False, returnHasBeenProcessed = False, returnModifiedTime = False, returnNewGroupName = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetup/" + str(EntityGroupSetupID), verb = "get", return_params_list = return_params_list)

def modifyEntityGroupSetup(EntityGroupSetupID, EntityID = 1, setEntityGroupID = None, setEntityIDPrimary = None, setHasBeenProcessed = None, setNewGroupName = None, setSchoolYearID = None, setRelationships = None, returnEntityGroupSetupID = True, returnCreatedTime = False, returnEffectiveGroupName = False, returnEntityGroupID = False, returnEntityIDPrimary = False, returnHasBeenProcessed = False, returnModifiedTime = False, returnNewGroupName = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetup/" + str(EntityGroupSetupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEntityGroupSetup(EntityID = 1, setEntityGroupID = None, setEntityIDPrimary = None, setHasBeenProcessed = None, setNewGroupName = None, setSchoolYearID = None, setRelationships = None, returnEntityGroupSetupID = True, returnCreatedTime = False, returnEffectiveGroupName = False, returnEntityGroupID = False, returnEntityIDPrimary = False, returnHasBeenProcessed = False, returnModifiedTime = False, returnNewGroupName = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEntityGroupSetup(EntityGroupSetupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEntityGroupSetupEntity(EntityID = 1, page = 1, pageSize = 100, returnEntityGroupSetupEntityID = True, returnCreatedTime = False, returnEntityGroupSetupID = False, returnEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEntityGroupSetupEntity(EntityGroupSetupEntityID, EntityID = 1, returnEntityGroupSetupEntityID = True, returnCreatedTime = False, returnEntityGroupSetupID = False, returnEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupEntity/" + str(EntityGroupSetupEntityID), verb = "get", return_params_list = return_params_list)

def modifyEntityGroupSetupEntity(EntityGroupSetupEntityID, EntityID = 1, setEntityGroupSetupID = None, setEntityID = None, setRelationships = None, returnEntityGroupSetupEntityID = True, returnCreatedTime = False, returnEntityGroupSetupID = False, returnEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupEntity/" + str(EntityGroupSetupEntityID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEntityGroupSetupEntity(EntityID = 1, setEntityGroupSetupID = None, setEntityID = None, setRelationships = None, returnEntityGroupSetupEntityID = True, returnCreatedTime = False, returnEntityGroupSetupID = False, returnEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupEntity/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEntityGroupSetupEntity(EntityGroupSetupEntityID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEntityGroupSetupRun(EntityID = 1, page = 1, pageSize = 100, returnEntityGroupSetupRunID = True, returnCreatedTime = False, returnEntityGroupSetupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRun/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEntityGroupSetupRun(EntityGroupSetupRunID, EntityID = 1, returnEntityGroupSetupRunID = True, returnCreatedTime = False, returnEntityGroupSetupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRun/" + str(EntityGroupSetupRunID), verb = "get", return_params_list = return_params_list)

def modifyEntityGroupSetupRun(EntityGroupSetupRunID, EntityID = 1, setEntityGroupSetupID = None, setRelationships = None, returnEntityGroupSetupRunID = True, returnCreatedTime = False, returnEntityGroupSetupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRun/" + str(EntityGroupSetupRunID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEntityGroupSetupRun(EntityID = 1, setEntityGroupSetupID = None, setRelationships = None, returnEntityGroupSetupRunID = True, returnCreatedTime = False, returnEntityGroupSetupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRun/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEntityGroupSetupRun(EntityGroupSetupRunID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEntityGroupSetupRunDetail(EntityID = 1, page = 1, pageSize = 100, returnEntityGroupSetupRunDetailID = True, returnChangeType = False, returnChangeTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityGroupSetupRunID = False, returnEntityID = False, returnError = False, returnIdentifyingFields = False, returnIsProcessed = False, returnIsUpdated = False, returnModifiedTime = False, returnModule = False, returnNewFieldValues = False, returnNewValues = False, returnObject = False, returnObjectPrimaryKey = False, returnOriginalValues = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRunDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEntityGroupSetupRunDetail(EntityGroupSetupRunDetailID, EntityID = 1, returnEntityGroupSetupRunDetailID = True, returnChangeType = False, returnChangeTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityGroupSetupRunID = False, returnEntityID = False, returnError = False, returnIdentifyingFields = False, returnIsProcessed = False, returnIsUpdated = False, returnModifiedTime = False, returnModule = False, returnNewFieldValues = False, returnNewValues = False, returnObject = False, returnObjectPrimaryKey = False, returnOriginalValues = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRunDetail/" + str(EntityGroupSetupRunDetailID), verb = "get", return_params_list = return_params_list)

def modifyEntityGroupSetupRunDetail(EntityGroupSetupRunDetailID, EntityID = 1, setChangeType = None, setChangeTypeCode = None, setEntityGroupKey = None, setEntityGroupSetupRunID = None, setEntityID = None, setError = None, setIdentifyingFields = None, setIsProcessed = None, setIsUpdated = None, setModule = None, setNewFieldValues = None, setNewValues = None, setObject = None, setObjectPrimaryKey = None, setOriginalValues = None, setSchoolYearID = None, setRelationships = None, returnEntityGroupSetupRunDetailID = True, returnChangeType = False, returnChangeTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityGroupSetupRunID = False, returnEntityID = False, returnError = False, returnIdentifyingFields = False, returnIsProcessed = False, returnIsUpdated = False, returnModifiedTime = False, returnModule = False, returnNewFieldValues = False, returnNewValues = False, returnObject = False, returnObjectPrimaryKey = False, returnOriginalValues = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRunDetail/" + str(EntityGroupSetupRunDetailID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEntityGroupSetupRunDetail(EntityID = 1, setChangeType = None, setChangeTypeCode = None, setEntityGroupKey = None, setEntityGroupSetupRunID = None, setEntityID = None, setError = None, setIdentifyingFields = None, setIsProcessed = None, setIsUpdated = None, setModule = None, setNewFieldValues = None, setNewValues = None, setObject = None, setObjectPrimaryKey = None, setOriginalValues = None, setSchoolYearID = None, setRelationships = None, returnEntityGroupSetupRunDetailID = True, returnChangeType = False, returnChangeTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityGroupSetupRunID = False, returnEntityID = False, returnError = False, returnIdentifyingFields = False, returnIsProcessed = False, returnIsUpdated = False, returnModifiedTime = False, returnModule = False, returnNewFieldValues = False, returnNewValues = False, returnObject = False, returnObjectPrimaryKey = False, returnOriginalValues = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRunDetail/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEntityGroupSetupRunDetail(EntityGroupSetupRunDetailID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEntity(EntityID = 1, page = 1, pageSize = 100, returnEntityID = True, returnAllowDualEnrollment = False, returnCampusID = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnDistrictCodeEntityCode = False, returnDistrictID = False, returnEnforceAddressRangeDefaults = False, returnEntityCodeOrCombinedCodesFollettExport = False, returnEntityGroupCount = False, returnEntityIDHash = False, returnEntityMNID = False, returnExternalLinkEntityCount = False, returnIsDistrictWide = False, returnIsSystemWide = False, returnModifiedTime = False, returnName = False, returnReportToState = False, returnSchoolYearIDCurrent = False, returnTotalPlanEntityYears = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Entity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEntity(EntityID, EntityID = 1, returnEntityID = True, returnAllowDualEnrollment = False, returnCampusID = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnDistrictCodeEntityCode = False, returnDistrictID = False, returnEnforceAddressRangeDefaults = False, returnEntityCodeOrCombinedCodesFollettExport = False, returnEntityGroupCount = False, returnEntityIDHash = False, returnEntityMNID = False, returnExternalLinkEntityCount = False, returnIsDistrictWide = False, returnIsSystemWide = False, returnModifiedTime = False, returnName = False, returnReportToState = False, returnSchoolYearIDCurrent = False, returnTotalPlanEntityYears = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Entity/" + str(EntityID), verb = "get", return_params_list = return_params_list)

def modifyEntity(EntityID, EntityID = 1, setAllowDualEnrollment = None, setCode = None, setDistrictID = None, setEnforceAddressRangeDefaults = None, setIsDistrictWide = None, setIsSystemWide = None, setName = None, setReportToState = None, setSchoolYearIDCurrent = None, setRelationships = None, returnEntityID = True, returnAllowDualEnrollment = False, returnCampusID = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnDistrictCodeEntityCode = False, returnDistrictID = False, returnEnforceAddressRangeDefaults = False, returnEntityCodeOrCombinedCodesFollettExport = False, returnEntityGroupCount = False, returnEntityIDHash = False, returnEntityMNID = False, returnExternalLinkEntityCount = False, returnIsDistrictWide = False, returnIsSystemWide = False, returnModifiedTime = False, returnName = False, returnReportToState = False, returnSchoolYearIDCurrent = False, returnTotalPlanEntityYears = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Entity/" + str(EntityID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEntity(EntityID = 1, setAllowDualEnrollment = None, setCode = None, setDistrictID = None, setEnforceAddressRangeDefaults = None, setIsDistrictWide = None, setIsSystemWide = None, setName = None, setReportToState = None, setSchoolYearIDCurrent = None, setRelationships = None, returnEntityID = True, returnAllowDualEnrollment = False, returnCampusID = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnDistrictCodeEntityCode = False, returnDistrictID = False, returnEnforceAddressRangeDefaults = False, returnEntityCodeOrCombinedCodesFollettExport = False, returnEntityGroupCount = False, returnEntityIDHash = False, returnEntityMNID = False, returnExternalLinkEntityCount = False, returnIsDistrictWide = False, returnIsSystemWide = False, returnModifiedTime = False, returnName = False, returnReportToState = False, returnSchoolYearIDCurrent = False, returnTotalPlanEntityYears = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Entity/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEntity(EntityID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryFiscalYear(EntityID = 1, page = 1, pageSize = 100, returnFiscalYearID = True, returnConflictAccountingUpdates = False, returnConflictAccountsPayableRuns = False, returnConflictAdditionDisposals = False, returnConflictBudgetAmendments = False, returnConflictCashReceiptDeposits = False, returnConflictDepreciations = False, returnConflictInvoices = False, returnConflictJournalEntries = False, returnConflictPayrollRuns = False, returnConflictPurchaseOrders = False, returnConflictWarehouseRequests = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEndDate = False, returnIsClosed = False, returnIsLockedByHR = False, returnModifiedTime = False, returnNumericYear = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/FiscalYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getFiscalYear(FiscalYearID, EntityID = 1, returnFiscalYearID = True, returnConflictAccountingUpdates = False, returnConflictAccountsPayableRuns = False, returnConflictAdditionDisposals = False, returnConflictBudgetAmendments = False, returnConflictCashReceiptDeposits = False, returnConflictDepreciations = False, returnConflictInvoices = False, returnConflictJournalEntries = False, returnConflictPayrollRuns = False, returnConflictPurchaseOrders = False, returnConflictWarehouseRequests = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEndDate = False, returnIsClosed = False, returnIsLockedByHR = False, returnModifiedTime = False, returnNumericYear = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/FiscalYear/" + str(FiscalYearID), verb = "get", return_params_list = return_params_list)

def modifyFiscalYear(FiscalYearID, EntityID = 1, setDescription = None, setDistrictID = None, setEndDate = None, setIsLockedByHR = None, setStartDate = None, setRelationships = None, returnFiscalYearID = True, returnConflictAccountingUpdates = False, returnConflictAccountsPayableRuns = False, returnConflictAdditionDisposals = False, returnConflictBudgetAmendments = False, returnConflictCashReceiptDeposits = False, returnConflictDepreciations = False, returnConflictInvoices = False, returnConflictJournalEntries = False, returnConflictPayrollRuns = False, returnConflictPurchaseOrders = False, returnConflictWarehouseRequests = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEndDate = False, returnIsClosed = False, returnIsLockedByHR = False, returnModifiedTime = False, returnNumericYear = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/FiscalYear/" + str(FiscalYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createFiscalYear(EntityID = 1, setDescription = None, setDistrictID = None, setEndDate = None, setIsLockedByHR = None, setStartDate = None, setRelationships = None, returnFiscalYearID = True, returnConflictAccountingUpdates = False, returnConflictAccountsPayableRuns = False, returnConflictAdditionDisposals = False, returnConflictBudgetAmendments = False, returnConflictCashReceiptDeposits = False, returnConflictDepreciations = False, returnConflictInvoices = False, returnConflictJournalEntries = False, returnConflictPayrollRuns = False, returnConflictPurchaseOrders = False, returnConflictWarehouseRequests = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEndDate = False, returnIsClosed = False, returnIsLockedByHR = False, returnModifiedTime = False, returnNumericYear = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/FiscalYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteFiscalYear(FiscalYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryRoom(EntityID = 1, page = 1, pageSize = 100, returnRoomID = True, returnBuildingCodeRoomNumber = False, returnBuildingID = False, returnCreatedTime = False, returnDescription = False, returnFormattedPhoneNumber = False, returnMaxConcurrentSections = False, returnMaxSeats = False, returnModifiedTime = False, returnPhoneExtension = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnRoomNumber = False, returnRoomNumberDescription = False, returnRoomTypeID = False, returnSquareFootage = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Room/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getRoom(RoomID, EntityID = 1, returnRoomID = True, returnBuildingCodeRoomNumber = False, returnBuildingID = False, returnCreatedTime = False, returnDescription = False, returnFormattedPhoneNumber = False, returnMaxConcurrentSections = False, returnMaxSeats = False, returnModifiedTime = False, returnPhoneExtension = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnRoomNumber = False, returnRoomNumberDescription = False, returnRoomTypeID = False, returnSquareFootage = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Room/" + str(RoomID), verb = "get", return_params_list = return_params_list)

def modifyRoom(RoomID, EntityID = 1, setBuildingID = None, setDescription = None, setMaxConcurrentSections = None, setMaxSeats = None, setPhoneExtension = None, setPhoneNumber = None, setPhoneNumberIsInternational = None, setRoomNumber = None, setRoomTypeID = None, setSquareFootage = None, setRelationships = None, returnRoomID = True, returnBuildingCodeRoomNumber = False, returnBuildingID = False, returnCreatedTime = False, returnDescription = False, returnFormattedPhoneNumber = False, returnMaxConcurrentSections = False, returnMaxSeats = False, returnModifiedTime = False, returnPhoneExtension = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnRoomNumber = False, returnRoomNumberDescription = False, returnRoomTypeID = False, returnSquareFootage = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Room/" + str(RoomID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createRoom(EntityID = 1, setBuildingID = None, setDescription = None, setMaxConcurrentSections = None, setMaxSeats = None, setPhoneExtension = None, setPhoneNumber = None, setPhoneNumberIsInternational = None, setRoomNumber = None, setRoomTypeID = None, setSquareFootage = None, setRelationships = None, returnRoomID = True, returnBuildingCodeRoomNumber = False, returnBuildingID = False, returnCreatedTime = False, returnDescription = False, returnFormattedPhoneNumber = False, returnMaxConcurrentSections = False, returnMaxSeats = False, returnModifiedTime = False, returnPhoneExtension = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnRoomNumber = False, returnRoomNumberDescription = False, returnRoomTypeID = False, returnSquareFootage = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Room/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteRoom(RoomID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryRoomType(EntityID = 1, page = 1, pageSize = 100, returnRoomTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/RoomType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getRoomType(RoomTypeID, EntityID = 1, returnRoomTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/RoomType/" + str(RoomTypeID), verb = "get", return_params_list = return_params_list)

def modifyRoomType(RoomTypeID, EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setRelationships = None, returnRoomTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/RoomType/" + str(RoomTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createRoomType(EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setRelationships = None, returnRoomTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/RoomType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteRoomType(RoomTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySchoolYear(EntityID = 1, page = 1, pageSize = 100, returnSchoolYearID = True, returnCreatedTime = False, returnDescription = False, returnIsCurrentYearForProvidedEntity = False, returnIsUpcomingYearForProvidedEntity = False, returnModifiedTime = False, returnNextNumericYear = False, returnNumericYear = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/SchoolYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSchoolYear(SchoolYearID, EntityID = 1, returnSchoolYearID = True, returnCreatedTime = False, returnDescription = False, returnIsCurrentYearForProvidedEntity = False, returnIsUpcomingYearForProvidedEntity = False, returnModifiedTime = False, returnNextNumericYear = False, returnNumericYear = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/SchoolYear/" + str(SchoolYearID), verb = "get", return_params_list = return_params_list)

def modifySchoolYear(SchoolYearID, EntityID = 1, setDescription = None, setNumericYear = None, setRelationships = None, returnSchoolYearID = True, returnCreatedTime = False, returnDescription = False, returnIsCurrentYearForProvidedEntity = False, returnIsUpcomingYearForProvidedEntity = False, returnModifiedTime = False, returnNextNumericYear = False, returnNumericYear = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/SchoolYear/" + str(SchoolYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSchoolYear(EntityID = 1, setDescription = None, setNumericYear = None, setRelationships = None, returnSchoolYearID = True, returnCreatedTime = False, returnDescription = False, returnIsCurrentYearForProvidedEntity = False, returnIsUpcomingYearForProvidedEntity = False, returnModifiedTime = False, returnNextNumericYear = False, returnNumericYear = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/SchoolYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSchoolYear(SchoolYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStateDistrictMN(EntityID = 1, page = 1, pageSize = 100, returnStateDistrictMNID = True, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnStateDistrictTypeCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/StateDistrictMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStateDistrictMN(StateDistrictMNID, EntityID = 1, returnStateDistrictMNID = True, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnStateDistrictTypeCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/StateDistrictMN/" + str(StateDistrictMNID), verb = "get", return_params_list = return_params_list)

def modifyStateDistrictMN(StateDistrictMNID, EntityID = 1, setCode = None, setName = None, setStateDistrictTypeCodeMNID = None, setRelationships = None, returnStateDistrictMNID = True, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnStateDistrictTypeCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/StateDistrictMN/" + str(StateDistrictMNID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStateDistrictMN(EntityID = 1, setCode = None, setName = None, setStateDistrictTypeCodeMNID = None, setRelationships = None, returnStateDistrictMNID = True, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnStateDistrictTypeCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/StateDistrictMN/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStateDistrictMN(StateDistrictMNID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")