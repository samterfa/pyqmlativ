# This module contains GraduationRequirements functions.

from .Utilities import make_request

import pandas as pd

import json

import re

def getEveryArea(EntityID = 1, page = 1, pageSize = 100, returnAreaID = True, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnElectiveSubAreaID = False, returnGradReqRankGPARequiredCourseRuleOverride = False, returnGradReqRankGPARequiredCourseRuleOverrideCode = False, returnIsElective = False, returnIsNotElective = False, returnIsNotSystemArea = False, returnIsSystemArea = False, returnModifiedTime = False, returnNonElectiveCreditTotal = False, returnPlanID = False, returnSkywardHash = False, returnSkywardID = False, returnTotalCredits = False, returnUseGradReqSubjectType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Area/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getArea(AreaID, EntityID = 1, returnAreaID = True, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnElectiveSubAreaID = False, returnGradReqRankGPARequiredCourseRuleOverride = False, returnGradReqRankGPARequiredCourseRuleOverrideCode = False, returnIsElective = False, returnIsNotElective = False, returnIsNotSystemArea = False, returnIsSystemArea = False, returnModifiedTime = False, returnNonElectiveCreditTotal = False, returnPlanID = False, returnSkywardHash = False, returnSkywardID = False, returnTotalCredits = False, returnUseGradReqSubjectType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Area/" + str(AreaID), verb = "get", return_params_list = return_params_list)

def modifyArea(AreaID, EntityID = 1, setDescription = None, setDisplayOrder = None, setGradReqRankGPARequiredCourseRuleOverride = None, setGradReqRankGPARequiredCourseRuleOverrideCode = None, setIsElective = None, setPlanID = None, setSkywardHash = None, setSkywardID = None, setTotalCredits = None, setUseGradReqSubjectType = None, setRelationships = None, returnAreaID = True, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnElectiveSubAreaID = False, returnGradReqRankGPARequiredCourseRuleOverride = False, returnGradReqRankGPARequiredCourseRuleOverrideCode = False, returnIsElective = False, returnIsNotElective = False, returnIsNotSystemArea = False, returnIsSystemArea = False, returnModifiedTime = False, returnNonElectiveCreditTotal = False, returnPlanID = False, returnSkywardHash = False, returnSkywardID = False, returnTotalCredits = False, returnUseGradReqSubjectType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Area/" + str(AreaID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createArea(EntityID = 1, setDescription = None, setDisplayOrder = None, setGradReqRankGPARequiredCourseRuleOverride = None, setGradReqRankGPARequiredCourseRuleOverrideCode = None, setIsElective = None, setPlanID = None, setSkywardHash = None, setSkywardID = None, setTotalCredits = None, setUseGradReqSubjectType = None, setRelationships = None, returnAreaID = True, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnElectiveSubAreaID = False, returnGradReqRankGPARequiredCourseRuleOverride = False, returnGradReqRankGPARequiredCourseRuleOverrideCode = False, returnIsElective = False, returnIsNotElective = False, returnIsNotSystemArea = False, returnIsSystemArea = False, returnModifiedTime = False, returnNonElectiveCreditTotal = False, returnPlanID = False, returnSkywardHash = False, returnSkywardID = False, returnTotalCredits = False, returnUseGradReqSubjectType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Area/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteArea(AreaID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCareerPlanDeclarationTimePeriod(EntityID = 1, page = 1, pageSize = 100, returnCareerPlanDeclarationTimePeriodID = True, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnFilterOption = False, returnFilterOptionCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCareerPlanDeclarationTimePeriod(CareerPlanDeclarationTimePeriodID, EntityID = 1, returnCareerPlanDeclarationTimePeriodID = True, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnFilterOption = False, returnFilterOptionCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriod/" + str(CareerPlanDeclarationTimePeriodID), verb = "get", return_params_list = return_params_list)

def modifyCareerPlanDeclarationTimePeriod(CareerPlanDeclarationTimePeriodID, EntityID = 1, setEndTime = None, setEntityID = None, setFilterOption = None, setFilterOptionCode = None, setSchoolYearID = None, setStartTime = None, setRelationships = None, returnCareerPlanDeclarationTimePeriodID = True, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnFilterOption = False, returnFilterOptionCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriod/" + str(CareerPlanDeclarationTimePeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCareerPlanDeclarationTimePeriod(EntityID = 1, setEndTime = None, setEntityID = None, setFilterOption = None, setFilterOptionCode = None, setSchoolYearID = None, setStartTime = None, setRelationships = None, returnCareerPlanDeclarationTimePeriodID = True, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnFilterOption = False, returnFilterOptionCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCareerPlanDeclarationTimePeriod(CareerPlanDeclarationTimePeriodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCareerPlanDeclarationTimePeriodGradeReference(EntityID = 1, page = 1, pageSize = 100, returnCareerPlanDeclarationTimePeriodGradeReferenceID = True, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodGradeReference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCareerPlanDeclarationTimePeriodGradeReference(CareerPlanDeclarationTimePeriodGradeReferenceID, EntityID = 1, returnCareerPlanDeclarationTimePeriodGradeReferenceID = True, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodGradeReference/" + str(CareerPlanDeclarationTimePeriodGradeReferenceID), verb = "get", return_params_list = return_params_list)

def modifyCareerPlanDeclarationTimePeriodGradeReference(CareerPlanDeclarationTimePeriodGradeReferenceID, EntityID = 1, setCareerPlanDeclarationTimePeriodID = None, setGradeReferenceID = None, setRelationships = None, returnCareerPlanDeclarationTimePeriodGradeReferenceID = True, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodGradeReference/" + str(CareerPlanDeclarationTimePeriodGradeReferenceID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCareerPlanDeclarationTimePeriodGradeReference(EntityID = 1, setCareerPlanDeclarationTimePeriodID = None, setGradeReferenceID = None, setRelationships = None, returnCareerPlanDeclarationTimePeriodGradeReferenceID = True, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodGradeReference/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCareerPlanDeclarationTimePeriodGradeReference(CareerPlanDeclarationTimePeriodGradeReferenceID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCareerPlanDeclarationTimePeriodStudentEntityYear(EntityID = 1, page = 1, pageSize = 100, returnCareerPlanDeclarationTimePeriodStudentEntityYearID = True, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnModifiedTime = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodStudentEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCareerPlanDeclarationTimePeriodStudentEntityYear(CareerPlanDeclarationTimePeriodStudentEntityYearID, EntityID = 1, returnCareerPlanDeclarationTimePeriodStudentEntityYearID = True, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnModifiedTime = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodStudentEntityYear/" + str(CareerPlanDeclarationTimePeriodStudentEntityYearID), verb = "get", return_params_list = return_params_list)

def modifyCareerPlanDeclarationTimePeriodStudentEntityYear(CareerPlanDeclarationTimePeriodStudentEntityYearID, EntityID = 1, setCareerPlanDeclarationTimePeriodID = None, setStudentEntityYearID = None, setRelationships = None, returnCareerPlanDeclarationTimePeriodStudentEntityYearID = True, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnModifiedTime = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodStudentEntityYear/" + str(CareerPlanDeclarationTimePeriodStudentEntityYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCareerPlanDeclarationTimePeriodStudentEntityYear(EntityID = 1, setCareerPlanDeclarationTimePeriodID = None, setStudentEntityYearID = None, setRelationships = None, returnCareerPlanDeclarationTimePeriodStudentEntityYearID = True, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnModifiedTime = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodStudentEntityYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCareerPlanDeclarationTimePeriodStudentEntityYear(CareerPlanDeclarationTimePeriodStudentEntityYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCareerPlanGradeLevel(EntityID = 1, page = 1, pageSize = 100, returnCareerPlanGradeLevelID = True, returnConfigDistrictID = False, returnCreatedTime = False, returnDisplayName = False, returnGradeLevelID = False, returnIsPriorLevel = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanGradeLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCareerPlanGradeLevel(CareerPlanGradeLevelID, EntityID = 1, returnCareerPlanGradeLevelID = True, returnConfigDistrictID = False, returnCreatedTime = False, returnDisplayName = False, returnGradeLevelID = False, returnIsPriorLevel = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanGradeLevel/" + str(CareerPlanGradeLevelID), verb = "get", return_params_list = return_params_list)

def modifyCareerPlanGradeLevel(CareerPlanGradeLevelID, EntityID = 1, setConfigDistrictID = None, setGradeLevelID = None, setIsPriorLevel = None, setRelationships = None, returnCareerPlanGradeLevelID = True, returnConfigDistrictID = False, returnCreatedTime = False, returnDisplayName = False, returnGradeLevelID = False, returnIsPriorLevel = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanGradeLevel/" + str(CareerPlanGradeLevelID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCareerPlanGradeLevel(EntityID = 1, setConfigDistrictID = None, setGradeLevelID = None, setIsPriorLevel = None, setRelationships = None, returnCareerPlanGradeLevelID = True, returnConfigDistrictID = False, returnCreatedTime = False, returnDisplayName = False, returnGradeLevelID = False, returnIsPriorLevel = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanGradeLevel/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCareerPlanGradeLevel(CareerPlanGradeLevelID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigDistrict(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictID = True, returnCourseWorkAppliedByType = False, returnCourseWorkAppliedByTypeCode = False, returnCreatedTime = False, returnDistrictID = False, returnGradingPeriodEndDateLastCheckedDate = False, returnIncludeFutureCredit = False, returnIncludeInProgressCredit = False, returnModifiedTime = False, returnTurnOffAutomaticCalculation = False, returnTurnOffAutomaticEndorsementCalculation = False, returnUsePriorToLastGradeLevel = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigDistrict(ConfigDistrictID, EntityID = 1, returnConfigDistrictID = True, returnCourseWorkAppliedByType = False, returnCourseWorkAppliedByTypeCode = False, returnCreatedTime = False, returnDistrictID = False, returnGradingPeriodEndDateLastCheckedDate = False, returnIncludeFutureCredit = False, returnIncludeInProgressCredit = False, returnModifiedTime = False, returnTurnOffAutomaticCalculation = False, returnTurnOffAutomaticEndorsementCalculation = False, returnUsePriorToLastGradeLevel = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/ConfigDistrict/" + str(ConfigDistrictID), verb = "get", return_params_list = return_params_list)

def modifyConfigDistrict(ConfigDistrictID, EntityID = 1, setCourseWorkAppliedByType = None, setCourseWorkAppliedByTypeCode = None, setDistrictID = None, setGradingPeriodEndDateLastCheckedDate = None, setIncludeFutureCredit = None, setIncludeInProgressCredit = None, setTurnOffAutomaticCalculation = None, setTurnOffAutomaticEndorsementCalculation = None, setUsePriorToLastGradeLevel = None, setRelationships = None, returnConfigDistrictID = True, returnCourseWorkAppliedByType = False, returnCourseWorkAppliedByTypeCode = False, returnCreatedTime = False, returnDistrictID = False, returnGradingPeriodEndDateLastCheckedDate = False, returnIncludeFutureCredit = False, returnIncludeInProgressCredit = False, returnModifiedTime = False, returnTurnOffAutomaticCalculation = False, returnTurnOffAutomaticEndorsementCalculation = False, returnUsePriorToLastGradeLevel = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/ConfigDistrict/" + str(ConfigDistrictID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigDistrict(EntityID = 1, setCourseWorkAppliedByType = None, setCourseWorkAppliedByTypeCode = None, setDistrictID = None, setGradingPeriodEndDateLastCheckedDate = None, setIncludeFutureCredit = None, setIncludeInProgressCredit = None, setTurnOffAutomaticCalculation = None, setTurnOffAutomaticEndorsementCalculation = None, setUsePriorToLastGradeLevel = None, setRelationships = None, returnConfigDistrictID = True, returnCourseWorkAppliedByType = False, returnCourseWorkAppliedByTypeCode = False, returnCreatedTime = False, returnDistrictID = False, returnGradingPeriodEndDateLastCheckedDate = False, returnIncludeFutureCredit = False, returnIncludeInProgressCredit = False, returnModifiedTime = False, returnTurnOffAutomaticCalculation = False, returnTurnOffAutomaticEndorsementCalculation = False, returnUsePriorToLastGradeLevel = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/ConfigDistrict/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigDistrict(ConfigDistrictID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCurriculumCluster(EntityID = 1, page = 1, pageSize = 100, returnCurriculumClusterID = True, returnCreatedTime = False, returnCurriculumClusterDefaultID = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumCluster/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCurriculumCluster(CurriculumClusterID, EntityID = 1, returnCurriculumClusterID = True, returnCreatedTime = False, returnCurriculumClusterDefaultID = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumCluster/" + str(CurriculumClusterID), verb = "get", return_params_list = return_params_list)

def modifyCurriculumCluster(CurriculumClusterID, EntityID = 1, setCurriculumClusterDefaultID = None, setDescription = None, setDistrictID = None, setRelationships = None, returnCurriculumClusterID = True, returnCreatedTime = False, returnCurriculumClusterDefaultID = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumCluster/" + str(CurriculumClusterID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCurriculumCluster(EntityID = 1, setCurriculumClusterDefaultID = None, setDescription = None, setDistrictID = None, setRelationships = None, returnCurriculumClusterID = True, returnCreatedTime = False, returnCurriculumClusterDefaultID = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumCluster/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCurriculumCluster(CurriculumClusterID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCurriculumClusterCurriculum(EntityID = 1, page = 1, pageSize = 100, returnCurriculumClusterCurriculumID = True, returnCreatedTime = False, returnCurriculumClusterID = False, returnCurriculumID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsAdvancedCredit = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterCurriculum/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCurriculumClusterCurriculum(CurriculumClusterCurriculumID, EntityID = 1, returnCurriculumClusterCurriculumID = True, returnCreatedTime = False, returnCurriculumClusterID = False, returnCurriculumID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsAdvancedCredit = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterCurriculum/" + str(CurriculumClusterCurriculumID), verb = "get", return_params_list = return_params_list)

def modifyCurriculumClusterCurriculum(CurriculumClusterCurriculumID, EntityID = 1, setCurriculumClusterID = None, setCurriculumID = None, setGradYearHigh = None, setGradYearLow = None, setIsAdvancedCredit = None, setRelationships = None, returnCurriculumClusterCurriculumID = True, returnCreatedTime = False, returnCurriculumClusterID = False, returnCurriculumID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsAdvancedCredit = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterCurriculum/" + str(CurriculumClusterCurriculumID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCurriculumClusterCurriculum(EntityID = 1, setCurriculumClusterID = None, setCurriculumID = None, setGradYearHigh = None, setGradYearLow = None, setIsAdvancedCredit = None, setRelationships = None, returnCurriculumClusterCurriculumID = True, returnCreatedTime = False, returnCurriculumClusterID = False, returnCurriculumID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsAdvancedCredit = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterCurriculum/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCurriculumClusterCurriculum(CurriculumClusterCurriculumID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCurriculumClusterDefault(EntityID = 1, page = 1, pageSize = 100, returnCurriculumClusterDefaultID = True, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCurriculumClusterDefault(CurriculumClusterDefaultID, EntityID = 1, returnCurriculumClusterDefaultID = True, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterDefault/" + str(CurriculumClusterDefaultID), verb = "get", return_params_list = return_params_list)

def modifyCurriculumClusterDefault(CurriculumClusterDefaultID, EntityID = 1, setDescription = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnCurriculumClusterDefaultID = True, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterDefault/" + str(CurriculumClusterDefaultID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCurriculumClusterDefault(EntityID = 1, setDescription = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnCurriculumClusterDefaultID = True, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterDefault/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCurriculumClusterDefault(CurriculumClusterDefaultID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCurriculumSubArea(EntityID = 1, page = 1, pageSize = 100, returnCurriculumSubAreaID = True, returnAllowReuseOfPreviouslyAppliedCredits = False, returnApplicationOrder = False, returnCreatedTime = False, returnCurriculumID = False, returnIsCustomCurriculumSubAreaWithStudentID = False, returnIsGradReqRankGPAWaiver = False, returnMaximumPercentOfCourseCredit = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnStudentID = False, returnSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumSubArea/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCurriculumSubArea(CurriculumSubAreaID, EntityID = 1, returnCurriculumSubAreaID = True, returnAllowReuseOfPreviouslyAppliedCredits = False, returnApplicationOrder = False, returnCreatedTime = False, returnCurriculumID = False, returnIsCustomCurriculumSubAreaWithStudentID = False, returnIsGradReqRankGPAWaiver = False, returnMaximumPercentOfCourseCredit = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnStudentID = False, returnSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumSubArea/" + str(CurriculumSubAreaID), verb = "get", return_params_list = return_params_list)

def modifyCurriculumSubArea(CurriculumSubAreaID, EntityID = 1, setAllowReuseOfPreviouslyAppliedCredits = None, setApplicationOrder = None, setCurriculumID = None, setIsGradReqRankGPAWaiver = None, setMaximumPercentOfCourseCredit = None, setSchoolYearHigh = None, setSchoolYearLow = None, setStudentID = None, setSubAreaID = None, setRelationships = None, returnCurriculumSubAreaID = True, returnAllowReuseOfPreviouslyAppliedCredits = False, returnApplicationOrder = False, returnCreatedTime = False, returnCurriculumID = False, returnIsCustomCurriculumSubAreaWithStudentID = False, returnIsGradReqRankGPAWaiver = False, returnMaximumPercentOfCourseCredit = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnStudentID = False, returnSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumSubArea/" + str(CurriculumSubAreaID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCurriculumSubArea(EntityID = 1, setAllowReuseOfPreviouslyAppliedCredits = None, setApplicationOrder = None, setCurriculumID = None, setIsGradReqRankGPAWaiver = None, setMaximumPercentOfCourseCredit = None, setSchoolYearHigh = None, setSchoolYearLow = None, setStudentID = None, setSubAreaID = None, setRelationships = None, returnCurriculumSubAreaID = True, returnAllowReuseOfPreviouslyAppliedCredits = False, returnApplicationOrder = False, returnCreatedTime = False, returnCurriculumID = False, returnIsCustomCurriculumSubAreaWithStudentID = False, returnIsGradReqRankGPAWaiver = False, returnMaximumPercentOfCourseCredit = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnStudentID = False, returnSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumSubArea/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCurriculumSubArea(CurriculumSubAreaID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEndorsement(EntityID = 1, page = 1, pageSize = 100, returnEndorsementID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEndorsementDefaultID = False, returnHasEndorsementOptions = False, returnIsActive = False, returnIsDeclarable = False, returnIsPreviouslyLoaded = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Endorsement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEndorsement(EndorsementID, EntityID = 1, returnEndorsementID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEndorsementDefaultID = False, returnHasEndorsementOptions = False, returnIsActive = False, returnIsDeclarable = False, returnIsPreviouslyLoaded = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Endorsement/" + str(EndorsementID), verb = "get", return_params_list = return_params_list)

def modifyEndorsement(EndorsementID, EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setEndorsementDefaultID = None, setIsActive = None, setIsDeclarable = None, setIsPreviouslyLoaded = None, setPrintOnTranscript = None, setRelationships = None, returnEndorsementID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEndorsementDefaultID = False, returnHasEndorsementOptions = False, returnIsActive = False, returnIsDeclarable = False, returnIsPreviouslyLoaded = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Endorsement/" + str(EndorsementID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEndorsement(EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setEndorsementDefaultID = None, setIsActive = None, setIsDeclarable = None, setIsPreviouslyLoaded = None, setPrintOnTranscript = None, setRelationships = None, returnEndorsementID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEndorsementDefaultID = False, returnHasEndorsementOptions = False, returnIsActive = False, returnIsDeclarable = False, returnIsPreviouslyLoaded = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Endorsement/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEndorsement(EndorsementID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEndorsementDeclarationTimePeriod(EntityID = 1, page = 1, pageSize = 100, returnEndorsementDeclarationTimePeriodID = True, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnFilterOption = False, returnFilterOptionCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEndorsementDeclarationTimePeriod(EndorsementDeclarationTimePeriodID, EntityID = 1, returnEndorsementDeclarationTimePeriodID = True, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnFilterOption = False, returnFilterOptionCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriod/" + str(EndorsementDeclarationTimePeriodID), verb = "get", return_params_list = return_params_list)

def modifyEndorsementDeclarationTimePeriod(EndorsementDeclarationTimePeriodID, EntityID = 1, setEndTime = None, setEntityID = None, setFilterOption = None, setFilterOptionCode = None, setSchoolYearID = None, setStartTime = None, setRelationships = None, returnEndorsementDeclarationTimePeriodID = True, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnFilterOption = False, returnFilterOptionCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriod/" + str(EndorsementDeclarationTimePeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEndorsementDeclarationTimePeriod(EntityID = 1, setEndTime = None, setEntityID = None, setFilterOption = None, setFilterOptionCode = None, setSchoolYearID = None, setStartTime = None, setRelationships = None, returnEndorsementDeclarationTimePeriodID = True, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnFilterOption = False, returnFilterOptionCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEndorsementDeclarationTimePeriod(EndorsementDeclarationTimePeriodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEndorsementDeclarationTimePeriodGradeReference(EntityID = 1, page = 1, pageSize = 100, returnEndorsementDeclarationTimePeriodGradeReferenceID = True, returnCreatedTime = False, returnEndorsementDeclarationTimePeriodID = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodGradeReference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEndorsementDeclarationTimePeriodGradeReference(EndorsementDeclarationTimePeriodGradeReferenceID, EntityID = 1, returnEndorsementDeclarationTimePeriodGradeReferenceID = True, returnCreatedTime = False, returnEndorsementDeclarationTimePeriodID = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodGradeReference/" + str(EndorsementDeclarationTimePeriodGradeReferenceID), verb = "get", return_params_list = return_params_list)

def modifyEndorsementDeclarationTimePeriodGradeReference(EndorsementDeclarationTimePeriodGradeReferenceID, EntityID = 1, setEndorsementDeclarationTimePeriodID = None, setGradeReferenceID = None, setRelationships = None, returnEndorsementDeclarationTimePeriodGradeReferenceID = True, returnCreatedTime = False, returnEndorsementDeclarationTimePeriodID = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodGradeReference/" + str(EndorsementDeclarationTimePeriodGradeReferenceID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEndorsementDeclarationTimePeriodGradeReference(EntityID = 1, setEndorsementDeclarationTimePeriodID = None, setGradeReferenceID = None, setRelationships = None, returnEndorsementDeclarationTimePeriodGradeReferenceID = True, returnCreatedTime = False, returnEndorsementDeclarationTimePeriodID = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodGradeReference/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEndorsementDeclarationTimePeriodGradeReference(EndorsementDeclarationTimePeriodGradeReferenceID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEndorsementDeclarationTimePeriodStudentEntityYear(EntityID = 1, page = 1, pageSize = 100, returnEndorsementDeclarationTimePeriodStudentEntityYearID = True, returnCreatedTime = False, returnEndorsementDeclarationTimePeriodID = False, returnModifiedTime = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodStudentEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEndorsementDeclarationTimePeriodStudentEntityYear(EndorsementDeclarationTimePeriodStudentEntityYearID, EntityID = 1, returnEndorsementDeclarationTimePeriodStudentEntityYearID = True, returnCreatedTime = False, returnEndorsementDeclarationTimePeriodID = False, returnModifiedTime = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodStudentEntityYear/" + str(EndorsementDeclarationTimePeriodStudentEntityYearID), verb = "get", return_params_list = return_params_list)

def modifyEndorsementDeclarationTimePeriodStudentEntityYear(EndorsementDeclarationTimePeriodStudentEntityYearID, EntityID = 1, setEndorsementDeclarationTimePeriodID = None, setStudentEntityYearID = None, setRelationships = None, returnEndorsementDeclarationTimePeriodStudentEntityYearID = True, returnCreatedTime = False, returnEndorsementDeclarationTimePeriodID = False, returnModifiedTime = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodStudentEntityYear/" + str(EndorsementDeclarationTimePeriodStudentEntityYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEndorsementDeclarationTimePeriodStudentEntityYear(EntityID = 1, setEndorsementDeclarationTimePeriodID = None, setStudentEntityYearID = None, setRelationships = None, returnEndorsementDeclarationTimePeriodStudentEntityYearID = True, returnCreatedTime = False, returnEndorsementDeclarationTimePeriodID = False, returnModifiedTime = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodStudentEntityYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEndorsementDeclarationTimePeriodStudentEntityYear(EndorsementDeclarationTimePeriodStudentEntityYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEndorsementDefault(EntityID = 1, page = 1, pageSize = 100, returnEndorsementDefaultID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnIsActive = False, returnIsDeclarable = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEndorsementDefault(EndorsementDefaultID, EntityID = 1, returnEndorsementDefaultID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnIsActive = False, returnIsDeclarable = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDefault/" + str(EndorsementDefaultID), verb = "get", return_params_list = return_params_list)

def modifyEndorsementDefault(EndorsementDefaultID, EntityID = 1, setCode = None, setDescription = None, setIsActive = None, setIsDeclarable = None, setPrintOnTranscript = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnEndorsementDefaultID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnIsActive = False, returnIsDeclarable = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDefault/" + str(EndorsementDefaultID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEndorsementDefault(EntityID = 1, setCode = None, setDescription = None, setIsActive = None, setIsDeclarable = None, setPrintOnTranscript = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnEndorsementDefaultID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnIsActive = False, returnIsDeclarable = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDefault/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEndorsementDefault(EndorsementDefaultID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEndorsementOption(EntityID = 1, page = 1, pageSize = 100, returnEndorsementOptionID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEndorsementID = False, returnEndorsementOptionDefaultID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnMustCompleteGradPlan = False, returnOrderNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOption/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEndorsementOption(EndorsementOptionID, EntityID = 1, returnEndorsementOptionID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEndorsementID = False, returnEndorsementOptionDefaultID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnMustCompleteGradPlan = False, returnOrderNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOption/" + str(EndorsementOptionID), verb = "get", return_params_list = return_params_list)

def modifyEndorsementOption(EndorsementOptionID, EntityID = 1, setCode = None, setDescription = None, setEndorsementID = None, setEndorsementOptionDefaultID = None, setGradYearHigh = None, setGradYearLow = None, setMustCompleteGradPlan = None, setOrderNumber = None, setRelationships = None, returnEndorsementOptionID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEndorsementID = False, returnEndorsementOptionDefaultID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnMustCompleteGradPlan = False, returnOrderNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOption/" + str(EndorsementOptionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEndorsementOption(EntityID = 1, setCode = None, setDescription = None, setEndorsementID = None, setEndorsementOptionDefaultID = None, setGradYearHigh = None, setGradYearLow = None, setMustCompleteGradPlan = None, setOrderNumber = None, setRelationships = None, returnEndorsementOptionID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEndorsementID = False, returnEndorsementOptionDefaultID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnMustCompleteGradPlan = False, returnOrderNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOption/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEndorsementOption(EndorsementOptionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEndorsementOptionDefault(EntityID = 1, page = 1, pageSize = 100, returnEndorsementOptionDefaultID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEndorsementDefaultID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnMustCompleteGradPlan = False, returnOrderNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOptionDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEndorsementOptionDefault(EndorsementOptionDefaultID, EntityID = 1, returnEndorsementOptionDefaultID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEndorsementDefaultID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnMustCompleteGradPlan = False, returnOrderNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOptionDefault/" + str(EndorsementOptionDefaultID), verb = "get", return_params_list = return_params_list)

def modifyEndorsementOptionDefault(EndorsementOptionDefaultID, EntityID = 1, setCode = None, setDescription = None, setEndorsementDefaultID = None, setGradYearHigh = None, setGradYearLow = None, setMustCompleteGradPlan = None, setOrderNumber = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnEndorsementOptionDefaultID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEndorsementDefaultID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnMustCompleteGradPlan = False, returnOrderNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOptionDefault/" + str(EndorsementOptionDefaultID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEndorsementOptionDefault(EntityID = 1, setCode = None, setDescription = None, setEndorsementDefaultID = None, setGradYearHigh = None, setGradYearLow = None, setMustCompleteGradPlan = None, setOrderNumber = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnEndorsementOptionDefaultID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEndorsementDefaultID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnMustCompleteGradPlan = False, returnOrderNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOptionDefault/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEndorsementOptionDefault(EndorsementOptionDefaultID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEndorsementRequirement(EntityID = 1, page = 1, pageSize = 100, returnEndorsementRequirementID = True, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnDescription = False, returnEndorsementOptionID = False, returnEndorsementRequirementDefaultID = False, returnMaximumClusterLimit = False, returnMinimumClusterLimit = False, returnModifiedTime = False, returnMustFulfillAllCurriculumClusters = False, returnOrderNumber = False, returnOverallCreditsRequired = False, returnRequirementAssessmentType = False, returnRequirementAssessmentTypeCode = False, returnRequirementType = False, returnRequirementTypeCode = False, returnUseMaximumClusterLimit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEndorsementRequirement(EndorsementRequirementID, EntityID = 1, returnEndorsementRequirementID = True, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnDescription = False, returnEndorsementOptionID = False, returnEndorsementRequirementDefaultID = False, returnMaximumClusterLimit = False, returnMinimumClusterLimit = False, returnModifiedTime = False, returnMustFulfillAllCurriculumClusters = False, returnOrderNumber = False, returnOverallCreditsRequired = False, returnRequirementAssessmentType = False, returnRequirementAssessmentTypeCode = False, returnRequirementType = False, returnRequirementTypeCode = False, returnUseMaximumClusterLimit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirement/" + str(EndorsementRequirementID), verb = "get", return_params_list = return_params_list)

def modifyEndorsementRequirement(EndorsementRequirementID, EntityID = 1, setAdvancedCreditsRequired = None, setDescription = None, setEndorsementOptionID = None, setEndorsementRequirementDefaultID = None, setMaximumClusterLimit = None, setMinimumClusterLimit = None, setMustFulfillAllCurriculumClusters = None, setOrderNumber = None, setOverallCreditsRequired = None, setRequirementAssessmentType = None, setRequirementAssessmentTypeCode = None, setRequirementType = None, setRequirementTypeCode = None, setUseMaximumClusterLimit = None, setRelationships = None, returnEndorsementRequirementID = True, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnDescription = False, returnEndorsementOptionID = False, returnEndorsementRequirementDefaultID = False, returnMaximumClusterLimit = False, returnMinimumClusterLimit = False, returnModifiedTime = False, returnMustFulfillAllCurriculumClusters = False, returnOrderNumber = False, returnOverallCreditsRequired = False, returnRequirementAssessmentType = False, returnRequirementAssessmentTypeCode = False, returnRequirementType = False, returnRequirementTypeCode = False, returnUseMaximumClusterLimit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirement/" + str(EndorsementRequirementID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEndorsementRequirement(EntityID = 1, setAdvancedCreditsRequired = None, setDescription = None, setEndorsementOptionID = None, setEndorsementRequirementDefaultID = None, setMaximumClusterLimit = None, setMinimumClusterLimit = None, setMustFulfillAllCurriculumClusters = None, setOrderNumber = None, setOverallCreditsRequired = None, setRequirementAssessmentType = None, setRequirementAssessmentTypeCode = None, setRequirementType = None, setRequirementTypeCode = None, setUseMaximumClusterLimit = None, setRelationships = None, returnEndorsementRequirementID = True, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnDescription = False, returnEndorsementOptionID = False, returnEndorsementRequirementDefaultID = False, returnMaximumClusterLimit = False, returnMinimumClusterLimit = False, returnModifiedTime = False, returnMustFulfillAllCurriculumClusters = False, returnOrderNumber = False, returnOverallCreditsRequired = False, returnRequirementAssessmentType = False, returnRequirementAssessmentTypeCode = False, returnRequirementType = False, returnRequirementTypeCode = False, returnUseMaximumClusterLimit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirement/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEndorsementRequirement(EndorsementRequirementID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEndorsementRequirementAssessment(EntityID = 1, page = 1, pageSize = 100, returnEndorsementRequirementAssessmentID = True, returnClusterType = False, returnClusterTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentDefaultID = False, returnEndorsementRequirementID = False, returnModifiedTime = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEndorsementRequirementAssessment(EndorsementRequirementAssessmentID, EntityID = 1, returnEndorsementRequirementAssessmentID = True, returnClusterType = False, returnClusterTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentDefaultID = False, returnEndorsementRequirementID = False, returnModifiedTime = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessment/" + str(EndorsementRequirementAssessmentID), verb = "get", return_params_list = return_params_list)

def modifyEndorsementRequirementAssessment(EndorsementRequirementAssessmentID, EntityID = 1, setClusterType = None, setClusterTypeCode = None, setEndorsementRequirementAssessmentDefaultID = None, setEndorsementRequirementID = None, setTestType = None, setTestTypeCode = None, setTestVersion = None, setTestVersionCode = None, setRelationships = None, returnEndorsementRequirementAssessmentID = True, returnClusterType = False, returnClusterTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentDefaultID = False, returnEndorsementRequirementID = False, returnModifiedTime = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessment/" + str(EndorsementRequirementAssessmentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEndorsementRequirementAssessment(EntityID = 1, setClusterType = None, setClusterTypeCode = None, setEndorsementRequirementAssessmentDefaultID = None, setEndorsementRequirementID = None, setTestType = None, setTestTypeCode = None, setTestVersion = None, setTestVersionCode = None, setRelationships = None, returnEndorsementRequirementAssessmentID = True, returnClusterType = False, returnClusterTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentDefaultID = False, returnEndorsementRequirementID = False, returnModifiedTime = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessment/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEndorsementRequirementAssessment(EndorsementRequirementAssessmentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEndorsementRequirementAssessmentCluster(EntityID = 1, page = 1, pageSize = 100, returnEndorsementRequirementAssessmentClusterID = True, returnClusterScoreType = False, returnClusterScoreTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnEndorsementRequirementAssessmentID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentCluster/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEndorsementRequirementAssessmentCluster(EndorsementRequirementAssessmentClusterID, EntityID = 1, returnEndorsementRequirementAssessmentClusterID = True, returnClusterScoreType = False, returnClusterScoreTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnEndorsementRequirementAssessmentID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentCluster/" + str(EndorsementRequirementAssessmentClusterID), verb = "get", return_params_list = return_params_list)

def modifyEndorsementRequirementAssessmentCluster(EndorsementRequirementAssessmentClusterID, EntityID = 1, setClusterScoreType = None, setClusterScoreTypeCode = None, setEndorsementRequirementAssessmentClusterDefaultID = None, setEndorsementRequirementAssessmentID = None, setRelationships = None, returnEndorsementRequirementAssessmentClusterID = True, returnClusterScoreType = False, returnClusterScoreTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnEndorsementRequirementAssessmentID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentCluster/" + str(EndorsementRequirementAssessmentClusterID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEndorsementRequirementAssessmentCluster(EntityID = 1, setClusterScoreType = None, setClusterScoreTypeCode = None, setEndorsementRequirementAssessmentClusterDefaultID = None, setEndorsementRequirementAssessmentID = None, setRelationships = None, returnEndorsementRequirementAssessmentClusterID = True, returnClusterScoreType = False, returnClusterScoreTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnEndorsementRequirementAssessmentID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentCluster/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEndorsementRequirementAssessmentCluster(EndorsementRequirementAssessmentClusterID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEndorsementRequirementAssessmentClusterDefault(EntityID = 1, page = 1, pageSize = 100, returnEndorsementRequirementAssessmentClusterDefaultID = True, returnClusterScoreType = False, returnClusterScoreTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentClusterDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEndorsementRequirementAssessmentClusterDefault(EndorsementRequirementAssessmentClusterDefaultID, EntityID = 1, returnEndorsementRequirementAssessmentClusterDefaultID = True, returnClusterScoreType = False, returnClusterScoreTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentClusterDefault/" + str(EndorsementRequirementAssessmentClusterDefaultID), verb = "get", return_params_list = return_params_list)

def modifyEndorsementRequirementAssessmentClusterDefault(EndorsementRequirementAssessmentClusterDefaultID, EntityID = 1, setClusterScoreType = None, setClusterScoreTypeCode = None, setEndorsementRequirementAssessmentDefaultID = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnEndorsementRequirementAssessmentClusterDefaultID = True, returnClusterScoreType = False, returnClusterScoreTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentClusterDefault/" + str(EndorsementRequirementAssessmentClusterDefaultID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEndorsementRequirementAssessmentClusterDefault(EntityID = 1, setClusterScoreType = None, setClusterScoreTypeCode = None, setEndorsementRequirementAssessmentDefaultID = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnEndorsementRequirementAssessmentClusterDefaultID = True, returnClusterScoreType = False, returnClusterScoreTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentClusterDefault/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEndorsementRequirementAssessmentClusterDefault(EndorsementRequirementAssessmentClusterDefaultID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEndorsementRequirementAssessmentDefault(EntityID = 1, page = 1, pageSize = 100, returnEndorsementRequirementAssessmentDefaultID = True, returnClusterType = False, returnClusterTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEndorsementRequirementAssessmentDefault(EndorsementRequirementAssessmentDefaultID, EntityID = 1, returnEndorsementRequirementAssessmentDefaultID = True, returnClusterType = False, returnClusterTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentDefault/" + str(EndorsementRequirementAssessmentDefaultID), verb = "get", return_params_list = return_params_list)

def modifyEndorsementRequirementAssessmentDefault(EndorsementRequirementAssessmentDefaultID, EntityID = 1, setClusterType = None, setClusterTypeCode = None, setEndorsementRequirementDefaultID = None, setSkywardHash = None, setSkywardID = None, setTestType = None, setTestTypeCode = None, setTestVersion = None, setTestVersionCode = None, setRelationships = None, returnEndorsementRequirementAssessmentDefaultID = True, returnClusterType = False, returnClusterTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentDefault/" + str(EndorsementRequirementAssessmentDefaultID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEndorsementRequirementAssessmentDefault(EntityID = 1, setClusterType = None, setClusterTypeCode = None, setEndorsementRequirementDefaultID = None, setSkywardHash = None, setSkywardID = None, setTestType = None, setTestTypeCode = None, setTestVersion = None, setTestVersionCode = None, setRelationships = None, returnEndorsementRequirementAssessmentDefaultID = True, returnClusterType = False, returnClusterTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentDefault/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEndorsementRequirementAssessmentDefault(EndorsementRequirementAssessmentDefaultID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEndorsementRequirementAssessmentScore(EntityID = 1, page = 1, pageSize = 100, returnEndorsementRequirementAssessmentScoreID = True, returnAssessmentScoreColumn = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterID = False, returnEndorsementRequirementAssessmentScoreDefaultID = False, returnModifiedTime = False, returnPassingScore = False, returnPassingScoreHigh = False, returnPassingScoreLow = False, returnScoreLocation = False, returnScoreType = False, returnScoreTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScore/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEndorsementRequirementAssessmentScore(EndorsementRequirementAssessmentScoreID, EntityID = 1, returnEndorsementRequirementAssessmentScoreID = True, returnAssessmentScoreColumn = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterID = False, returnEndorsementRequirementAssessmentScoreDefaultID = False, returnModifiedTime = False, returnPassingScore = False, returnPassingScoreHigh = False, returnPassingScoreLow = False, returnScoreLocation = False, returnScoreType = False, returnScoreTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScore/" + str(EndorsementRequirementAssessmentScoreID), verb = "get", return_params_list = return_params_list)

def modifyEndorsementRequirementAssessmentScore(EndorsementRequirementAssessmentScoreID, EntityID = 1, setEndorsementRequirementAssessmentClusterID = None, setEndorsementRequirementAssessmentScoreDefaultID = None, setPassingScore = None, setPassingScoreHigh = None, setPassingScoreLow = None, setScoreLocation = None, setScoreType = None, setScoreTypeCode = None, setRelationships = None, returnEndorsementRequirementAssessmentScoreID = True, returnAssessmentScoreColumn = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterID = False, returnEndorsementRequirementAssessmentScoreDefaultID = False, returnModifiedTime = False, returnPassingScore = False, returnPassingScoreHigh = False, returnPassingScoreLow = False, returnScoreLocation = False, returnScoreType = False, returnScoreTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScore/" + str(EndorsementRequirementAssessmentScoreID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEndorsementRequirementAssessmentScore(EntityID = 1, setEndorsementRequirementAssessmentClusterID = None, setEndorsementRequirementAssessmentScoreDefaultID = None, setPassingScore = None, setPassingScoreHigh = None, setPassingScoreLow = None, setScoreLocation = None, setScoreType = None, setScoreTypeCode = None, setRelationships = None, returnEndorsementRequirementAssessmentScoreID = True, returnAssessmentScoreColumn = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterID = False, returnEndorsementRequirementAssessmentScoreDefaultID = False, returnModifiedTime = False, returnPassingScore = False, returnPassingScoreHigh = False, returnPassingScoreLow = False, returnScoreLocation = False, returnScoreType = False, returnScoreTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScore/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEndorsementRequirementAssessmentScore(EndorsementRequirementAssessmentScoreID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEndorsementRequirementAssessmentScoreDefault(EntityID = 1, page = 1, pageSize = 100, returnEndorsementRequirementAssessmentScoreDefaultID = True, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnModifiedTime = False, returnPassingScore = False, returnPassingScoreHigh = False, returnPassingScoreLow = False, returnScoreLocation = False, returnScoreType = False, returnScoreTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScoreDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEndorsementRequirementAssessmentScoreDefault(EndorsementRequirementAssessmentScoreDefaultID, EntityID = 1, returnEndorsementRequirementAssessmentScoreDefaultID = True, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnModifiedTime = False, returnPassingScore = False, returnPassingScoreHigh = False, returnPassingScoreLow = False, returnScoreLocation = False, returnScoreType = False, returnScoreTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScoreDefault/" + str(EndorsementRequirementAssessmentScoreDefaultID), verb = "get", return_params_list = return_params_list)

def modifyEndorsementRequirementAssessmentScoreDefault(EndorsementRequirementAssessmentScoreDefaultID, EntityID = 1, setEndorsementRequirementAssessmentClusterDefaultID = None, setPassingScore = None, setPassingScoreHigh = None, setPassingScoreLow = None, setScoreLocation = None, setScoreType = None, setScoreTypeCode = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnEndorsementRequirementAssessmentScoreDefaultID = True, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnModifiedTime = False, returnPassingScore = False, returnPassingScoreHigh = False, returnPassingScoreLow = False, returnScoreLocation = False, returnScoreType = False, returnScoreTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScoreDefault/" + str(EndorsementRequirementAssessmentScoreDefaultID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEndorsementRequirementAssessmentScoreDefault(EntityID = 1, setEndorsementRequirementAssessmentClusterDefaultID = None, setPassingScore = None, setPassingScoreHigh = None, setPassingScoreLow = None, setScoreLocation = None, setScoreType = None, setScoreTypeCode = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnEndorsementRequirementAssessmentScoreDefaultID = True, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnModifiedTime = False, returnPassingScore = False, returnPassingScoreHigh = False, returnPassingScoreLow = False, returnScoreLocation = False, returnScoreType = False, returnScoreTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScoreDefault/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEndorsementRequirementAssessmentScoreDefault(EndorsementRequirementAssessmentScoreDefaultID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEndorsementRequirementCurriculum(EntityID = 1, page = 1, pageSize = 100, returnEndorsementRequirementCurriculumID = True, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnCreditsRequired = False, returnCurriculumClusterID = False, returnEndorsementRequirementCurriculumDefaultID = False, returnEndorsementRequirementID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculum/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEndorsementRequirementCurriculum(EndorsementRequirementCurriculumID, EntityID = 1, returnEndorsementRequirementCurriculumID = True, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnCreditsRequired = False, returnCurriculumClusterID = False, returnEndorsementRequirementCurriculumDefaultID = False, returnEndorsementRequirementID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculum/" + str(EndorsementRequirementCurriculumID), verb = "get", return_params_list = return_params_list)

def modifyEndorsementRequirementCurriculum(EndorsementRequirementCurriculumID, EntityID = 1, setAdvancedCreditsRequired = None, setCreditsRequired = None, setCurriculumClusterID = None, setEndorsementRequirementCurriculumDefaultID = None, setEndorsementRequirementID = None, setRelationships = None, returnEndorsementRequirementCurriculumID = True, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnCreditsRequired = False, returnCurriculumClusterID = False, returnEndorsementRequirementCurriculumDefaultID = False, returnEndorsementRequirementID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculum/" + str(EndorsementRequirementCurriculumID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEndorsementRequirementCurriculum(EntityID = 1, setAdvancedCreditsRequired = None, setCreditsRequired = None, setCurriculumClusterID = None, setEndorsementRequirementCurriculumDefaultID = None, setEndorsementRequirementID = None, setRelationships = None, returnEndorsementRequirementCurriculumID = True, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnCreditsRequired = False, returnCurriculumClusterID = False, returnEndorsementRequirementCurriculumDefaultID = False, returnEndorsementRequirementID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculum/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEndorsementRequirementCurriculum(EndorsementRequirementCurriculumID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEndorsementRequirementCurriculumDefault(EntityID = 1, page = 1, pageSize = 100, returnEndorsementRequirementCurriculumDefaultID = True, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnCreditsRequired = False, returnCurriculumClusterDefaultID = False, returnEndorsementRequirementDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculumDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEndorsementRequirementCurriculumDefault(EndorsementRequirementCurriculumDefaultID, EntityID = 1, returnEndorsementRequirementCurriculumDefaultID = True, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnCreditsRequired = False, returnCurriculumClusterDefaultID = False, returnEndorsementRequirementDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculumDefault/" + str(EndorsementRequirementCurriculumDefaultID), verb = "get", return_params_list = return_params_list)

def modifyEndorsementRequirementCurriculumDefault(EndorsementRequirementCurriculumDefaultID, EntityID = 1, setAdvancedCreditsRequired = None, setCreditsRequired = None, setCurriculumClusterDefaultID = None, setEndorsementRequirementDefaultID = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnEndorsementRequirementCurriculumDefaultID = True, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnCreditsRequired = False, returnCurriculumClusterDefaultID = False, returnEndorsementRequirementDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculumDefault/" + str(EndorsementRequirementCurriculumDefaultID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEndorsementRequirementCurriculumDefault(EntityID = 1, setAdvancedCreditsRequired = None, setCreditsRequired = None, setCurriculumClusterDefaultID = None, setEndorsementRequirementDefaultID = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnEndorsementRequirementCurriculumDefaultID = True, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnCreditsRequired = False, returnCurriculumClusterDefaultID = False, returnEndorsementRequirementDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculumDefault/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEndorsementRequirementCurriculumDefault(EndorsementRequirementCurriculumDefaultID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEndorsementRequirementDefault(EntityID = 1, page = 1, pageSize = 100, returnEndorsementRequirementDefaultID = True, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnDescription = False, returnEndorsementOptionDefaultID = False, returnMaximumClusterLimit = False, returnMinimumClusterLimit = False, returnModifiedTime = False, returnMustFulfillAllCurriculumClusters = False, returnOrderNumber = False, returnOverallCreditsRequired = False, returnRequirementAssessmentType = False, returnRequirementAssessmentTypeCode = False, returnRequirementType = False, returnRequirementTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnUseMaximumClusterLimit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEndorsementRequirementDefault(EndorsementRequirementDefaultID, EntityID = 1, returnEndorsementRequirementDefaultID = True, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnDescription = False, returnEndorsementOptionDefaultID = False, returnMaximumClusterLimit = False, returnMinimumClusterLimit = False, returnModifiedTime = False, returnMustFulfillAllCurriculumClusters = False, returnOrderNumber = False, returnOverallCreditsRequired = False, returnRequirementAssessmentType = False, returnRequirementAssessmentTypeCode = False, returnRequirementType = False, returnRequirementTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnUseMaximumClusterLimit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementDefault/" + str(EndorsementRequirementDefaultID), verb = "get", return_params_list = return_params_list)

def modifyEndorsementRequirementDefault(EndorsementRequirementDefaultID, EntityID = 1, setAdvancedCreditsRequired = None, setDescription = None, setEndorsementOptionDefaultID = None, setMaximumClusterLimit = None, setMinimumClusterLimit = None, setMustFulfillAllCurriculumClusters = None, setOrderNumber = None, setOverallCreditsRequired = None, setRequirementAssessmentType = None, setRequirementAssessmentTypeCode = None, setRequirementType = None, setRequirementTypeCode = None, setSkywardHash = None, setSkywardID = None, setUseMaximumClusterLimit = None, setRelationships = None, returnEndorsementRequirementDefaultID = True, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnDescription = False, returnEndorsementOptionDefaultID = False, returnMaximumClusterLimit = False, returnMinimumClusterLimit = False, returnModifiedTime = False, returnMustFulfillAllCurriculumClusters = False, returnOrderNumber = False, returnOverallCreditsRequired = False, returnRequirementAssessmentType = False, returnRequirementAssessmentTypeCode = False, returnRequirementType = False, returnRequirementTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnUseMaximumClusterLimit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementDefault/" + str(EndorsementRequirementDefaultID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEndorsementRequirementDefault(EntityID = 1, setAdvancedCreditsRequired = None, setDescription = None, setEndorsementOptionDefaultID = None, setMaximumClusterLimit = None, setMinimumClusterLimit = None, setMustFulfillAllCurriculumClusters = None, setOrderNumber = None, setOverallCreditsRequired = None, setRequirementAssessmentType = None, setRequirementAssessmentTypeCode = None, setRequirementType = None, setRequirementTypeCode = None, setSkywardHash = None, setSkywardID = None, setUseMaximumClusterLimit = None, setRelationships = None, returnEndorsementRequirementDefaultID = True, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnDescription = False, returnEndorsementOptionDefaultID = False, returnMaximumClusterLimit = False, returnMinimumClusterLimit = False, returnModifiedTime = False, returnMustFulfillAllCurriculumClusters = False, returnOrderNumber = False, returnOverallCreditsRequired = False, returnRequirementAssessmentType = False, returnRequirementAssessmentTypeCode = False, returnRequirementType = False, returnRequirementTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnUseMaximumClusterLimit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementDefault/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEndorsementRequirementDefault(EndorsementRequirementDefaultID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPlan(EntityID = 1, page = 1, pageSize = 100, returnPlanID = True, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEdFiGraduationPlanID = False, returnGeneralElectiveSubAreaID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsNotSystemPlan = False, returnIsSystemPlan = False, returnModifiedTime = False, returnNonElectiveCreditTotal = False, returnNumberOfSubAreasForCurriculum = False, returnSkywardHash = False, returnSkywardID = False, returnTotalCredits = False, returnTotalYears = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Plan/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPlan(PlanID, EntityID = 1, returnPlanID = True, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEdFiGraduationPlanID = False, returnGeneralElectiveSubAreaID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsNotSystemPlan = False, returnIsSystemPlan = False, returnModifiedTime = False, returnNonElectiveCreditTotal = False, returnNumberOfSubAreasForCurriculum = False, returnSkywardHash = False, returnSkywardID = False, returnTotalCredits = False, returnTotalYears = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Plan/" + str(PlanID), verb = "get", return_params_list = return_params_list)

def modifyPlan(PlanID, EntityID = 1, setDescription = None, setDistrictID = None, setEdFiGraduationPlanID = None, setGradYearHigh = None, setGradYearLow = None, setSkywardHash = None, setSkywardID = None, setTotalCredits = None, setRelationships = None, returnPlanID = True, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEdFiGraduationPlanID = False, returnGeneralElectiveSubAreaID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsNotSystemPlan = False, returnIsSystemPlan = False, returnModifiedTime = False, returnNonElectiveCreditTotal = False, returnNumberOfSubAreasForCurriculum = False, returnSkywardHash = False, returnSkywardID = False, returnTotalCredits = False, returnTotalYears = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Plan/" + str(PlanID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPlan(EntityID = 1, setDescription = None, setDistrictID = None, setEdFiGraduationPlanID = None, setGradYearHigh = None, setGradYearLow = None, setSkywardHash = None, setSkywardID = None, setTotalCredits = None, setRelationships = None, returnPlanID = True, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEdFiGraduationPlanID = False, returnGeneralElectiveSubAreaID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsNotSystemPlan = False, returnIsSystemPlan = False, returnModifiedTime = False, returnNonElectiveCreditTotal = False, returnNumberOfSubAreasForCurriculum = False, returnSkywardHash = False, returnSkywardID = False, returnTotalCredits = False, returnTotalYears = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Plan/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePlan(PlanID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPlanDefault(EntityID = 1, page = 1, pageSize = 100, returnPlanDefaultID = True, returnCreatedTime = False, returnEntityID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPlanDefault(PlanDefaultID, EntityID = 1, returnPlanDefaultID = True, returnCreatedTime = False, returnEntityID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanDefault/" + str(PlanDefaultID), verb = "get", return_params_list = return_params_list)

def modifyPlanDefault(PlanDefaultID, EntityID = 1, setEntityID = None, setGradYearHigh = None, setGradYearLow = None, setPlanID = None, setRelationships = None, returnPlanDefaultID = True, returnCreatedTime = False, returnEntityID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanDefault/" + str(PlanDefaultID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPlanDefault(EntityID = 1, setEntityID = None, setGradYearHigh = None, setGradYearLow = None, setPlanID = None, setRelationships = None, returnPlanDefaultID = True, returnCreatedTime = False, returnEntityID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanDefault/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePlanDefault(PlanDefaultID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPlanEntity(EntityID = 1, page = 1, pageSize = 100, returnPlanEntityID = True, returnCreatedTime = False, returnEntityID = False, returnGradYearHigh = False, returnGradYearLow = False, returnGradYearRange = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPlanEntity(PlanEntityID, EntityID = 1, returnPlanEntityID = True, returnCreatedTime = False, returnEntityID = False, returnGradYearHigh = False, returnGradYearLow = False, returnGradYearRange = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanEntity/" + str(PlanEntityID), verb = "get", return_params_list = return_params_list)

def modifyPlanEntity(PlanEntityID, EntityID = 1, setEntityID = None, setGradYearHigh = None, setGradYearLow = None, setPlanID = None, setRelationships = None, returnPlanEntityID = True, returnCreatedTime = False, returnEntityID = False, returnGradYearHigh = False, returnGradYearLow = False, returnGradYearRange = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanEntity/" + str(PlanEntityID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPlanEntity(EntityID = 1, setEntityID = None, setGradYearHigh = None, setGradYearLow = None, setPlanID = None, setRelationships = None, returnPlanEntityID = True, returnCreatedTime = False, returnEntityID = False, returnGradYearHigh = False, returnGradYearLow = False, returnGradYearRange = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanEntity/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePlanEntity(PlanEntityID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryQueuedGraduationPlanRecalcTrigger(EntityID = 1, page = 1, pageSize = 100, returnQueuedGraduationPlanRecalcTriggerID = True, returnCreatedTime = False, returnModifiedTime = False, returnSourceID = False, returnSourceObject = False, returnSourceObjectCode = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedGraduationPlanRecalcTrigger/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getQueuedGraduationPlanRecalcTrigger(QueuedGraduationPlanRecalcTriggerID, EntityID = 1, returnQueuedGraduationPlanRecalcTriggerID = True, returnCreatedTime = False, returnModifiedTime = False, returnSourceID = False, returnSourceObject = False, returnSourceObjectCode = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedGraduationPlanRecalcTrigger/" + str(QueuedGraduationPlanRecalcTriggerID), verb = "get", return_params_list = return_params_list)

def modifyQueuedGraduationPlanRecalcTrigger(QueuedGraduationPlanRecalcTriggerID, EntityID = 1, setSourceID = None, setSourceObject = None, setStatus = None, setRelationships = None, returnQueuedGraduationPlanRecalcTriggerID = True, returnCreatedTime = False, returnModifiedTime = False, returnSourceID = False, returnSourceObject = False, returnSourceObjectCode = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedGraduationPlanRecalcTrigger/" + str(QueuedGraduationPlanRecalcTriggerID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createQueuedGraduationPlanRecalcTrigger(EntityID = 1, setSourceID = None, setSourceObject = None, setStatus = None, setRelationships = None, returnQueuedGraduationPlanRecalcTriggerID = True, returnCreatedTime = False, returnModifiedTime = False, returnSourceID = False, returnSourceObject = False, returnSourceObjectCode = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedGraduationPlanRecalcTrigger/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteQueuedGraduationPlanRecalcTrigger(QueuedGraduationPlanRecalcTriggerID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryQueuedStudentPlanCourseworkApplication(EntityID = 1, page = 1, pageSize = 100, returnQueuedStudentPlanCourseworkApplicationID = True, returnCreatedTime = False, returnDistrictID = False, returnEndTime = False, returnHostName = False, returnModifiedTime = False, returnProcessID = False, returnRecalculationStatusDetails = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnStudentPlanID = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentPlanCourseworkApplication/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getQueuedStudentPlanCourseworkApplication(QueuedStudentPlanCourseworkApplicationID, EntityID = 1, returnQueuedStudentPlanCourseworkApplicationID = True, returnCreatedTime = False, returnDistrictID = False, returnEndTime = False, returnHostName = False, returnModifiedTime = False, returnProcessID = False, returnRecalculationStatusDetails = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnStudentPlanID = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentPlanCourseworkApplication/" + str(QueuedStudentPlanCourseworkApplicationID), verb = "get", return_params_list = return_params_list)

def modifyQueuedStudentPlanCourseworkApplication(QueuedStudentPlanCourseworkApplicationID, EntityID = 1, setDistrictID = None, setEndTime = None, setHostName = None, setProcessID = None, setStartTime = None, setStatus = None, setStudentPlanID = None, setThreadName = None, setUserIDImpersonator = None, setRelationships = None, returnQueuedStudentPlanCourseworkApplicationID = True, returnCreatedTime = False, returnDistrictID = False, returnEndTime = False, returnHostName = False, returnModifiedTime = False, returnProcessID = False, returnRecalculationStatusDetails = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnStudentPlanID = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentPlanCourseworkApplication/" + str(QueuedStudentPlanCourseworkApplicationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createQueuedStudentPlanCourseworkApplication(EntityID = 1, setDistrictID = None, setEndTime = None, setHostName = None, setProcessID = None, setStartTime = None, setStatus = None, setStudentPlanID = None, setThreadName = None, setUserIDImpersonator = None, setRelationships = None, returnQueuedStudentPlanCourseworkApplicationID = True, returnCreatedTime = False, returnDistrictID = False, returnEndTime = False, returnHostName = False, returnModifiedTime = False, returnProcessID = False, returnRecalculationStatusDetails = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnStudentPlanID = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentPlanCourseworkApplication/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteQueuedStudentPlanCourseworkApplication(QueuedStudentPlanCourseworkApplicationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentArea(EntityID = 1, page = 1, pageSize = 100, returnStudentAreaID = True, returnAreaID = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsFulfilledInPlan = False, returnModifiedTime = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentArea/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentArea(StudentAreaID, EntityID = 1, returnStudentAreaID = True, returnAreaID = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsFulfilledInPlan = False, returnModifiedTime = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentArea/" + str(StudentAreaID), verb = "get", return_params_list = return_params_list)

def modifyStudentArea(StudentAreaID, EntityID = 1, setAreaID = None, setStudentPlanID = None, setRelationships = None, returnStudentAreaID = True, returnAreaID = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsFulfilledInPlan = False, returnModifiedTime = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentArea/" + str(StudentAreaID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentArea(EntityID = 1, setAreaID = None, setStudentPlanID = None, setRelationships = None, returnStudentAreaID = True, returnAreaID = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsFulfilledInPlan = False, returnModifiedTime = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentArea/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentArea(StudentAreaID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentCareerPlan(EntityID = 1, page = 1, pageSize = 100, returnStudentCareerPlanID = True, returnCareerPlanGradeLevelID = False, returnCreatedTime = False, returnCredits = False, returnCurriculumID = False, returnGradeListDisplay = False, returnIsStudentPermittedToChangeGradeLevel = False, returnIsStudentPermittedToDelete = False, returnModifiedTime = False, returnStudentCourseRequestID = False, returnStudentID = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentCareerPlan/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentCareerPlan(StudentCareerPlanID, EntityID = 1, returnStudentCareerPlanID = True, returnCareerPlanGradeLevelID = False, returnCreatedTime = False, returnCredits = False, returnCurriculumID = False, returnGradeListDisplay = False, returnIsStudentPermittedToChangeGradeLevel = False, returnIsStudentPermittedToDelete = False, returnModifiedTime = False, returnStudentCourseRequestID = False, returnStudentID = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentCareerPlan/" + str(StudentCareerPlanID), verb = "get", return_params_list = return_params_list)

def modifyStudentCareerPlan(StudentCareerPlanID, EntityID = 1, setCareerPlanGradeLevelID = None, setCredits = None, setCurriculumID = None, setIsStudentPermittedToChangeGradeLevel = None, setIsStudentPermittedToDelete = None, setStudentCourseRequestID = None, setStudentID = None, setStudentSubAreaID = None, setRelationships = None, returnStudentCareerPlanID = True, returnCareerPlanGradeLevelID = False, returnCreatedTime = False, returnCredits = False, returnCurriculumID = False, returnGradeListDisplay = False, returnIsStudentPermittedToChangeGradeLevel = False, returnIsStudentPermittedToDelete = False, returnModifiedTime = False, returnStudentCourseRequestID = False, returnStudentID = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentCareerPlan/" + str(StudentCareerPlanID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentCareerPlan(EntityID = 1, setCareerPlanGradeLevelID = None, setCredits = None, setCurriculumID = None, setIsStudentPermittedToChangeGradeLevel = None, setIsStudentPermittedToDelete = None, setStudentCourseRequestID = None, setStudentID = None, setStudentSubAreaID = None, setRelationships = None, returnStudentCareerPlanID = True, returnCareerPlanGradeLevelID = False, returnCreatedTime = False, returnCredits = False, returnCurriculumID = False, returnGradeListDisplay = False, returnIsStudentPermittedToChangeGradeLevel = False, returnIsStudentPermittedToDelete = False, returnModifiedTime = False, returnStudentCourseRequestID = False, returnStudentID = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentCareerPlan/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentCareerPlan(StudentCareerPlanID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentEndorsement(EntityID = 1, page = 1, pageSize = 100, returnStudentEndorsementID = True, returnAttachmentComments = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCompletionMethod = False, returnCreatedTime = False, returnDistrictID = False, returnEndorsementID = False, returnGuardianSignedTime = False, returnHasDeclaredEndorsementOptions = False, returnHasEndorsementOptions = False, returnHasEndorsementOptionsToAddOrDeclare = False, returnIsAdminAdded = False, returnIsComplete = False, returnIsDeclared = False, returnIsReceived = False, returnIsSignedByGuardian = False, returnIsSignedByStudent = False, returnModifiedTime = False, returnNameIDGuardianSignedBy = False, returnStudentID = False, returnStudentSignedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentEndorsement(StudentEndorsementID, EntityID = 1, returnStudentEndorsementID = True, returnAttachmentComments = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCompletionMethod = False, returnCreatedTime = False, returnDistrictID = False, returnEndorsementID = False, returnGuardianSignedTime = False, returnHasDeclaredEndorsementOptions = False, returnHasEndorsementOptions = False, returnHasEndorsementOptionsToAddOrDeclare = False, returnIsAdminAdded = False, returnIsComplete = False, returnIsDeclared = False, returnIsReceived = False, returnIsSignedByGuardian = False, returnIsSignedByStudent = False, returnModifiedTime = False, returnNameIDGuardianSignedBy = False, returnStudentID = False, returnStudentSignedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsement/" + str(StudentEndorsementID), verb = "get", return_params_list = return_params_list)

def modifyStudentEndorsement(StudentEndorsementID, EntityID = 1, setDistrictID = None, setEndorsementID = None, setGuardianSignedTime = None, setIsAdminAdded = None, setIsDeclared = None, setIsReceived = None, setIsSignedByGuardian = None, setIsSignedByStudent = None, setNameIDGuardianSignedBy = None, setStudentID = None, setStudentSignedTime = None, setRelationships = None, returnStudentEndorsementID = True, returnAttachmentComments = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCompletionMethod = False, returnCreatedTime = False, returnDistrictID = False, returnEndorsementID = False, returnGuardianSignedTime = False, returnHasDeclaredEndorsementOptions = False, returnHasEndorsementOptions = False, returnHasEndorsementOptionsToAddOrDeclare = False, returnIsAdminAdded = False, returnIsComplete = False, returnIsDeclared = False, returnIsReceived = False, returnIsSignedByGuardian = False, returnIsSignedByStudent = False, returnModifiedTime = False, returnNameIDGuardianSignedBy = False, returnStudentID = False, returnStudentSignedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsement/" + str(StudentEndorsementID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentEndorsement(EntityID = 1, setDistrictID = None, setEndorsementID = None, setGuardianSignedTime = None, setIsAdminAdded = None, setIsDeclared = None, setIsReceived = None, setIsSignedByGuardian = None, setIsSignedByStudent = None, setNameIDGuardianSignedBy = None, setStudentID = None, setStudentSignedTime = None, setRelationships = None, returnStudentEndorsementID = True, returnAttachmentComments = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCompletionMethod = False, returnCreatedTime = False, returnDistrictID = False, returnEndorsementID = False, returnGuardianSignedTime = False, returnHasDeclaredEndorsementOptions = False, returnHasEndorsementOptions = False, returnHasEndorsementOptionsToAddOrDeclare = False, returnIsAdminAdded = False, returnIsComplete = False, returnIsDeclared = False, returnIsReceived = False, returnIsSignedByGuardian = False, returnIsSignedByStudent = False, returnModifiedTime = False, returnNameIDGuardianSignedBy = False, returnStudentID = False, returnStudentSignedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsement/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentEndorsement(StudentEndorsementID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentEndorsementOption(EntityID = 1, page = 1, pageSize = 100, returnStudentEndorsementOptionID = True, returnAdminAdded = False, returnCreatedTime = False, returnEndorsementOptionID = False, returnGradPlanInProgress = False, returnIsComplete = False, returnIsDeclared = False, returnIsReceived = False, returnModifiedTime = False, returnOverallCreditsRequired = False, returnStudentEndorsementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementOption/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentEndorsementOption(StudentEndorsementOptionID, EntityID = 1, returnStudentEndorsementOptionID = True, returnAdminAdded = False, returnCreatedTime = False, returnEndorsementOptionID = False, returnGradPlanInProgress = False, returnIsComplete = False, returnIsDeclared = False, returnIsReceived = False, returnModifiedTime = False, returnOverallCreditsRequired = False, returnStudentEndorsementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementOption/" + str(StudentEndorsementOptionID), verb = "get", return_params_list = return_params_list)

def modifyStudentEndorsementOption(StudentEndorsementOptionID, EntityID = 1, setAdminAdded = None, setEndorsementOptionID = None, setIsComplete = None, setIsDeclared = None, setIsReceived = None, setStudentEndorsementID = None, setRelationships = None, returnStudentEndorsementOptionID = True, returnAdminAdded = False, returnCreatedTime = False, returnEndorsementOptionID = False, returnGradPlanInProgress = False, returnIsComplete = False, returnIsDeclared = False, returnIsReceived = False, returnModifiedTime = False, returnOverallCreditsRequired = False, returnStudentEndorsementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementOption/" + str(StudentEndorsementOptionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentEndorsementOption(EntityID = 1, setAdminAdded = None, setEndorsementOptionID = None, setIsComplete = None, setIsDeclared = None, setIsReceived = None, setStudentEndorsementID = None, setRelationships = None, returnStudentEndorsementOptionID = True, returnAdminAdded = False, returnCreatedTime = False, returnEndorsementOptionID = False, returnGradPlanInProgress = False, returnIsComplete = False, returnIsDeclared = False, returnIsReceived = False, returnModifiedTime = False, returnOverallCreditsRequired = False, returnStudentEndorsementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementOption/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentEndorsementOption(StudentEndorsementOptionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentEndorsementRequirement(EntityID = 1, page = 1, pageSize = 100, returnStudentEndorsementRequirementID = True, returnAdvancedCreditsApplied = False, returnCreatedTime = False, returnEndorsementRequirementID = False, returnIsComplete = False, returnModifiedTime = False, returnOverallCreditsApplied = False, returnStudentEndorsementOptionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentEndorsementRequirement(StudentEndorsementRequirementID, EntityID = 1, returnStudentEndorsementRequirementID = True, returnAdvancedCreditsApplied = False, returnCreatedTime = False, returnEndorsementRequirementID = False, returnIsComplete = False, returnModifiedTime = False, returnOverallCreditsApplied = False, returnStudentEndorsementOptionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirement/" + str(StudentEndorsementRequirementID), verb = "get", return_params_list = return_params_list)

def modifyStudentEndorsementRequirement(StudentEndorsementRequirementID, EntityID = 1, setEndorsementRequirementID = None, setIsComplete = None, setStudentEndorsementOptionID = None, setRelationships = None, returnStudentEndorsementRequirementID = True, returnAdvancedCreditsApplied = False, returnCreatedTime = False, returnEndorsementRequirementID = False, returnIsComplete = False, returnModifiedTime = False, returnOverallCreditsApplied = False, returnStudentEndorsementOptionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirement/" + str(StudentEndorsementRequirementID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentEndorsementRequirement(EntityID = 1, setEndorsementRequirementID = None, setIsComplete = None, setStudentEndorsementOptionID = None, setRelationships = None, returnStudentEndorsementRequirementID = True, returnAdvancedCreditsApplied = False, returnCreatedTime = False, returnEndorsementRequirementID = False, returnIsComplete = False, returnModifiedTime = False, returnOverallCreditsApplied = False, returnStudentEndorsementOptionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirement/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentEndorsementRequirement(StudentEndorsementRequirementID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentEndorsementRequirementAssessment(EntityID = 1, page = 1, pageSize = 100, returnStudentEndorsementRequirementAssessmentID = True, returnCreatedTime = False, returnEndorsementRequirementAssessmentID = False, returnIsComplete = False, returnModifiedTime = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentEndorsementRequirementAssessment(StudentEndorsementRequirementAssessmentID, EntityID = 1, returnStudentEndorsementRequirementAssessmentID = True, returnCreatedTime = False, returnEndorsementRequirementAssessmentID = False, returnIsComplete = False, returnModifiedTime = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessment/" + str(StudentEndorsementRequirementAssessmentID), verb = "get", return_params_list = return_params_list)

def modifyStudentEndorsementRequirementAssessment(StudentEndorsementRequirementAssessmentID, EntityID = 1, setEndorsementRequirementAssessmentID = None, setIsComplete = None, setStudentEndorsementRequirementID = None, setRelationships = None, returnStudentEndorsementRequirementAssessmentID = True, returnCreatedTime = False, returnEndorsementRequirementAssessmentID = False, returnIsComplete = False, returnModifiedTime = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessment/" + str(StudentEndorsementRequirementAssessmentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentEndorsementRequirementAssessment(EntityID = 1, setEndorsementRequirementAssessmentID = None, setIsComplete = None, setStudentEndorsementRequirementID = None, setRelationships = None, returnStudentEndorsementRequirementAssessmentID = True, returnCreatedTime = False, returnEndorsementRequirementAssessmentID = False, returnIsComplete = False, returnModifiedTime = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessment/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentEndorsementRequirementAssessment(StudentEndorsementRequirementAssessmentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentEndorsementRequirementAssessmentScore(EntityID = 1, page = 1, pageSize = 100, returnStudentEndorsementRequirementAssessmentScoreID = True, returnAssessmentScore = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentScoreID = False, returnIsPassingScore = False, returnModifiedTime = False, returnStudentEndorsementRequirementAssessmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessmentScore/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentEndorsementRequirementAssessmentScore(StudentEndorsementRequirementAssessmentScoreID, EntityID = 1, returnStudentEndorsementRequirementAssessmentScoreID = True, returnAssessmentScore = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentScoreID = False, returnIsPassingScore = False, returnModifiedTime = False, returnStudentEndorsementRequirementAssessmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessmentScore/" + str(StudentEndorsementRequirementAssessmentScoreID), verb = "get", return_params_list = return_params_list)

def modifyStudentEndorsementRequirementAssessmentScore(StudentEndorsementRequirementAssessmentScoreID, EntityID = 1, setAssessmentScore = None, setEndorsementRequirementAssessmentScoreID = None, setIsPassingScore = None, setStudentEndorsementRequirementAssessmentID = None, setRelationships = None, returnStudentEndorsementRequirementAssessmentScoreID = True, returnAssessmentScore = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentScoreID = False, returnIsPassingScore = False, returnModifiedTime = False, returnStudentEndorsementRequirementAssessmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessmentScore/" + str(StudentEndorsementRequirementAssessmentScoreID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentEndorsementRequirementAssessmentScore(EntityID = 1, setAssessmentScore = None, setEndorsementRequirementAssessmentScoreID = None, setIsPassingScore = None, setStudentEndorsementRequirementAssessmentID = None, setRelationships = None, returnStudentEndorsementRequirementAssessmentScoreID = True, returnAssessmentScore = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentScoreID = False, returnIsPassingScore = False, returnModifiedTime = False, returnStudentEndorsementRequirementAssessmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessmentScore/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentEndorsementRequirementAssessmentScore(StudentEndorsementRequirementAssessmentScoreID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentEndorsementRequirementCourseRequest(EntityID = 1, page = 1, pageSize = 100, returnStudentEndorsementRequirementCourseRequestID = True, returnAppliedAdvancedCredits = False, returnAppliedOverallCredits = False, returnApplyToType = False, returnApplyToTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementCurriculumID = False, returnModifiedTime = False, returnStudentCourseRequestID = False, returnStudentEndorsementRequirementCurriculumID = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCourseRequest/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentEndorsementRequirementCourseRequest(StudentEndorsementRequirementCourseRequestID, EntityID = 1, returnStudentEndorsementRequirementCourseRequestID = True, returnAppliedAdvancedCredits = False, returnAppliedOverallCredits = False, returnApplyToType = False, returnApplyToTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementCurriculumID = False, returnModifiedTime = False, returnStudentCourseRequestID = False, returnStudentEndorsementRequirementCurriculumID = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCourseRequest/" + str(StudentEndorsementRequirementCourseRequestID), verb = "get", return_params_list = return_params_list)

def modifyStudentEndorsementRequirementCourseRequest(StudentEndorsementRequirementCourseRequestID, EntityID = 1, setAppliedAdvancedCredits = None, setAppliedOverallCredits = None, setApplyToType = None, setApplyToTypeCode = None, setEndorsementRequirementCurriculumID = None, setStudentCourseRequestID = None, setStudentEndorsementRequirementCurriculumID = None, setStudentEndorsementRequirementID = None, setRelationships = None, returnStudentEndorsementRequirementCourseRequestID = True, returnAppliedAdvancedCredits = False, returnAppliedOverallCredits = False, returnApplyToType = False, returnApplyToTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementCurriculumID = False, returnModifiedTime = False, returnStudentCourseRequestID = False, returnStudentEndorsementRequirementCurriculumID = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCourseRequest/" + str(StudentEndorsementRequirementCourseRequestID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentEndorsementRequirementCourseRequest(EntityID = 1, setAppliedAdvancedCredits = None, setAppliedOverallCredits = None, setApplyToType = None, setApplyToTypeCode = None, setEndorsementRequirementCurriculumID = None, setStudentCourseRequestID = None, setStudentEndorsementRequirementCurriculumID = None, setStudentEndorsementRequirementID = None, setRelationships = None, returnStudentEndorsementRequirementCourseRequestID = True, returnAppliedAdvancedCredits = False, returnAppliedOverallCredits = False, returnApplyToType = False, returnApplyToTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementCurriculumID = False, returnModifiedTime = False, returnStudentCourseRequestID = False, returnStudentEndorsementRequirementCurriculumID = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCourseRequest/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentEndorsementRequirementCourseRequest(StudentEndorsementRequirementCourseRequestID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentEndorsementRequirementCurriculum(EntityID = 1, page = 1, pageSize = 100, returnStudentEndorsementRequirementCurriculumID = True, returnAdvancedCreditsApplied = False, returnCreatedTime = False, returnEndorsementRequirementCurriculumID = False, returnIsComplete = False, returnModifiedTime = False, returnOverallCreditsApplied = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCurriculum/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentEndorsementRequirementCurriculum(StudentEndorsementRequirementCurriculumID, EntityID = 1, returnStudentEndorsementRequirementCurriculumID = True, returnAdvancedCreditsApplied = False, returnCreatedTime = False, returnEndorsementRequirementCurriculumID = False, returnIsComplete = False, returnModifiedTime = False, returnOverallCreditsApplied = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCurriculum/" + str(StudentEndorsementRequirementCurriculumID), verb = "get", return_params_list = return_params_list)

def modifyStudentEndorsementRequirementCurriculum(StudentEndorsementRequirementCurriculumID, EntityID = 1, setEndorsementRequirementCurriculumID = None, setIsComplete = None, setStudentEndorsementRequirementID = None, setRelationships = None, returnStudentEndorsementRequirementCurriculumID = True, returnAdvancedCreditsApplied = False, returnCreatedTime = False, returnEndorsementRequirementCurriculumID = False, returnIsComplete = False, returnModifiedTime = False, returnOverallCreditsApplied = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCurriculum/" + str(StudentEndorsementRequirementCurriculumID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentEndorsementRequirementCurriculum(EntityID = 1, setEndorsementRequirementCurriculumID = None, setIsComplete = None, setStudentEndorsementRequirementID = None, setRelationships = None, returnStudentEndorsementRequirementCurriculumID = True, returnAdvancedCreditsApplied = False, returnCreatedTime = False, returnEndorsementRequirementCurriculumID = False, returnIsComplete = False, returnModifiedTime = False, returnOverallCreditsApplied = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCurriculum/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentEndorsementRequirementCurriculum(StudentEndorsementRequirementCurriculumID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentPlan(EntityID = 1, page = 1, pageSize = 100, returnStudentPlanID = True, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsCurrent = False, returnModifiedTime = False, returnPlanID = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlan/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentPlan(StudentPlanID, EntityID = 1, returnStudentPlanID = True, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsCurrent = False, returnModifiedTime = False, returnPlanID = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlan/" + str(StudentPlanID), verb = "get", return_params_list = return_params_list)

def modifyStudentPlan(StudentPlanID, EntityID = 1, setAttemptedCredits = None, setFutureCredits = None, setInProgressCredits = None, setIsCurrent = None, setPlanID = None, setPlannedCredits = None, setRemainingCredits = None, setStudentID = None, setWaivedCredits = None, setRelationships = None, returnStudentPlanID = True, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsCurrent = False, returnModifiedTime = False, returnPlanID = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlan/" + str(StudentPlanID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentPlan(EntityID = 1, setAttemptedCredits = None, setFutureCredits = None, setInProgressCredits = None, setIsCurrent = None, setPlanID = None, setPlannedCredits = None, setRemainingCredits = None, setStudentID = None, setWaivedCredits = None, setRelationships = None, returnStudentPlanID = True, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsCurrent = False, returnModifiedTime = False, returnPlanID = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlan/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentPlan(StudentPlanID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentPlanThreadLock(EntityID = 1, page = 1, pageSize = 100, returnStudentPlanThreadLockID = True, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnStudentPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlanThreadLock/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentPlanThreadLock(StudentPlanThreadLockID, EntityID = 1, returnStudentPlanThreadLockID = True, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnStudentPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlanThreadLock/" + str(StudentPlanThreadLockID), verb = "get", return_params_list = return_params_list)

def modifyStudentPlanThreadLock(StudentPlanThreadLockID, EntityID = 1, setDistrictID = None, setStudentPlanID = None, setRelationships = None, returnStudentPlanThreadLockID = True, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnStudentPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlanThreadLock/" + str(StudentPlanThreadLockID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentPlanThreadLock(EntityID = 1, setDistrictID = None, setStudentPlanID = None, setRelationships = None, returnStudentPlanThreadLockID = True, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnStudentPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlanThreadLock/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentPlanThreadLock(StudentPlanThreadLockID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentSubArea(EntityID = 1, page = 1, pageSize = 100, returnStudentSubAreaID = True, returnAttemptedCredits = False, returnCanAddManualStudentSubAreaCurriculumSubArea = False, returnCanAddWaiver = False, returnCanHaveWaiver = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsFulfilledInPlan = False, returnModifiedTime = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentAreaID = False, returnStudentPlanID = False, returnSubAreaID = False, returnTotalManualCredits = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubArea/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentSubArea(StudentSubAreaID, EntityID = 1, returnStudentSubAreaID = True, returnAttemptedCredits = False, returnCanAddManualStudentSubAreaCurriculumSubArea = False, returnCanAddWaiver = False, returnCanHaveWaiver = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsFulfilledInPlan = False, returnModifiedTime = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentAreaID = False, returnStudentPlanID = False, returnSubAreaID = False, returnTotalManualCredits = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubArea/" + str(StudentSubAreaID), verb = "get", return_params_list = return_params_list)

def modifyStudentSubArea(StudentSubAreaID, EntityID = 1, setStudentAreaID = None, setStudentPlanID = None, setSubAreaID = None, setRelationships = None, returnStudentSubAreaID = True, returnAttemptedCredits = False, returnCanAddManualStudentSubAreaCurriculumSubArea = False, returnCanAddWaiver = False, returnCanHaveWaiver = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsFulfilledInPlan = False, returnModifiedTime = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentAreaID = False, returnStudentPlanID = False, returnSubAreaID = False, returnTotalManualCredits = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubArea/" + str(StudentSubAreaID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentSubArea(EntityID = 1, setStudentAreaID = None, setStudentPlanID = None, setSubAreaID = None, setRelationships = None, returnStudentSubAreaID = True, returnAttemptedCredits = False, returnCanAddManualStudentSubAreaCurriculumSubArea = False, returnCanAddWaiver = False, returnCanHaveWaiver = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsFulfilledInPlan = False, returnModifiedTime = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentAreaID = False, returnStudentPlanID = False, returnSubAreaID = False, returnTotalManualCredits = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubArea/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentSubArea(StudentSubAreaID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentSubAreaCurriculumSubArea(EntityID = 1, page = 1, pageSize = 100, returnStudentSubAreaCurriculumSubAreaID = True, returnAppliedOrder = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnEntryMethod = False, returnEntryMethodCode = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsAutomatic = False, returnModifiedTime = False, returnPlannedCredits = False, returnStudentCourseRequestID = False, returnStudentSubAreaID = False, returnTotalCredits = False, returnTotalNonAttemptedCredits = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaCurriculumSubArea/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentSubAreaCurriculumSubArea(StudentSubAreaCurriculumSubAreaID, EntityID = 1, returnStudentSubAreaCurriculumSubAreaID = True, returnAppliedOrder = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnEntryMethod = False, returnEntryMethodCode = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsAutomatic = False, returnModifiedTime = False, returnPlannedCredits = False, returnStudentCourseRequestID = False, returnStudentSubAreaID = False, returnTotalCredits = False, returnTotalNonAttemptedCredits = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaCurriculumSubArea/" + str(StudentSubAreaCurriculumSubAreaID), verb = "get", return_params_list = return_params_list)

def modifyStudentSubAreaCurriculumSubArea(StudentSubAreaCurriculumSubAreaID, EntityID = 1, setAppliedOrder = None, setAttemptedCredits = None, setCompletedCredits = None, setCurriculumSubAreaID = None, setEntryMethod = None, setEntryMethodCode = None, setFutureCredits = None, setInProgressCredits = None, setPlannedCredits = None, setStudentCourseRequestID = None, setStudentSubAreaID = None, setRelationships = None, returnStudentSubAreaCurriculumSubAreaID = True, returnAppliedOrder = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnEntryMethod = False, returnEntryMethodCode = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsAutomatic = False, returnModifiedTime = False, returnPlannedCredits = False, returnStudentCourseRequestID = False, returnStudentSubAreaID = False, returnTotalCredits = False, returnTotalNonAttemptedCredits = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaCurriculumSubArea/" + str(StudentSubAreaCurriculumSubAreaID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentSubAreaCurriculumSubArea(EntityID = 1, setAppliedOrder = None, setAttemptedCredits = None, setCompletedCredits = None, setCurriculumSubAreaID = None, setEntryMethod = None, setEntryMethodCode = None, setFutureCredits = None, setInProgressCredits = None, setPlannedCredits = None, setStudentCourseRequestID = None, setStudentSubAreaID = None, setRelationships = None, returnStudentSubAreaCurriculumSubAreaID = True, returnAppliedOrder = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnEntryMethod = False, returnEntryMethodCode = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsAutomatic = False, returnModifiedTime = False, returnPlannedCredits = False, returnStudentCourseRequestID = False, returnStudentSubAreaID = False, returnTotalCredits = False, returnTotalNonAttemptedCredits = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaCurriculumSubArea/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentSubAreaCurriculumSubArea(StudentSubAreaCurriculumSubAreaID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentSubAreaWaiver(EntityID = 1, page = 1, pageSize = 100, returnStudentSubAreaWaiverID = True, returnComment = False, returnCreatedTime = False, returnCredits = False, returnModifiedTime = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaWaiver/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentSubAreaWaiver(StudentSubAreaWaiverID, EntityID = 1, returnStudentSubAreaWaiverID = True, returnComment = False, returnCreatedTime = False, returnCredits = False, returnModifiedTime = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaWaiver/" + str(StudentSubAreaWaiverID), verb = "get", return_params_list = return_params_list)

def modifyStudentSubAreaWaiver(StudentSubAreaWaiverID, EntityID = 1, setComment = None, setCredits = None, setStudentSubAreaID = None, setRelationships = None, returnStudentSubAreaWaiverID = True, returnComment = False, returnCreatedTime = False, returnCredits = False, returnModifiedTime = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaWaiver/" + str(StudentSubAreaWaiverID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentSubAreaWaiver(EntityID = 1, setComment = None, setCredits = None, setStudentSubAreaID = None, setRelationships = None, returnStudentSubAreaWaiverID = True, returnComment = False, returnCreatedTime = False, returnCredits = False, returnModifiedTime = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaWaiver/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentSubAreaWaiver(StudentSubAreaWaiverID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySubArea(EntityID = 1, page = 1, pageSize = 100, returnSubAreaID = True, returnAreaID = False, returnAreaSubAreaDescription = False, returnCreatedTime = False, returnCredits = False, returnCurriculumSubAreaExistsForNonStudentCurriculum = False, returnDescription = False, returnDisplayOrder = False, returnGradReqRankGPARequiredCourseRuleOverride = False, returnGradReqRankGPARequiredCourseRuleOverrideCode = False, returnHasSkywardID = False, returnIsElective = False, returnIsSystemSubArea = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubArea/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSubArea(SubAreaID, EntityID = 1, returnSubAreaID = True, returnAreaID = False, returnAreaSubAreaDescription = False, returnCreatedTime = False, returnCredits = False, returnCurriculumSubAreaExistsForNonStudentCurriculum = False, returnDescription = False, returnDisplayOrder = False, returnGradReqRankGPARequiredCourseRuleOverride = False, returnGradReqRankGPARequiredCourseRuleOverrideCode = False, returnHasSkywardID = False, returnIsElective = False, returnIsSystemSubArea = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubArea/" + str(SubAreaID), verb = "get", return_params_list = return_params_list)

def modifySubArea(SubAreaID, EntityID = 1, setAreaID = None, setCredits = None, setDescription = None, setDisplayOrder = None, setGradReqRankGPARequiredCourseRuleOverride = None, setGradReqRankGPARequiredCourseRuleOverrideCode = None, setIsElective = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnSubAreaID = True, returnAreaID = False, returnAreaSubAreaDescription = False, returnCreatedTime = False, returnCredits = False, returnCurriculumSubAreaExistsForNonStudentCurriculum = False, returnDescription = False, returnDisplayOrder = False, returnGradReqRankGPARequiredCourseRuleOverride = False, returnGradReqRankGPARequiredCourseRuleOverrideCode = False, returnHasSkywardID = False, returnIsElective = False, returnIsSystemSubArea = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubArea/" + str(SubAreaID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSubArea(EntityID = 1, setAreaID = None, setCredits = None, setDescription = None, setDisplayOrder = None, setGradReqRankGPARequiredCourseRuleOverride = None, setGradReqRankGPARequiredCourseRuleOverrideCode = None, setIsElective = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnSubAreaID = True, returnAreaID = False, returnAreaSubAreaDescription = False, returnCreatedTime = False, returnCredits = False, returnCurriculumSubAreaExistsForNonStudentCurriculum = False, returnDescription = False, returnDisplayOrder = False, returnGradReqRankGPARequiredCourseRuleOverride = False, returnGradReqRankGPARequiredCourseRuleOverrideCode = False, returnHasSkywardID = False, returnIsElective = False, returnIsSystemSubArea = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubArea/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSubArea(SubAreaID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySubAreaLimitGroup(EntityID = 1, page = 1, pageSize = 100, returnSubAreaLimitGroupID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCreditLimit = False, returnDescription = False, returnModifiedTime = False, returnSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSubAreaLimitGroup(SubAreaLimitGroupID, EntityID = 1, returnSubAreaLimitGroupID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCreditLimit = False, returnDescription = False, returnModifiedTime = False, returnSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroup/" + str(SubAreaLimitGroupID), verb = "get", return_params_list = return_params_list)

def modifySubAreaLimitGroup(SubAreaLimitGroupID, EntityID = 1, setCode = None, setCreditLimit = None, setDescription = None, setSubAreaID = None, setRelationships = None, returnSubAreaLimitGroupID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCreditLimit = False, returnDescription = False, returnModifiedTime = False, returnSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroup/" + str(SubAreaLimitGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSubAreaLimitGroup(EntityID = 1, setCode = None, setCreditLimit = None, setDescription = None, setSubAreaID = None, setRelationships = None, returnSubAreaLimitGroupID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCreditLimit = False, returnDescription = False, returnModifiedTime = False, returnSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSubAreaLimitGroup(SubAreaLimitGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySubAreaLimitGroupCurriculumSubArea(EntityID = 1, page = 1, pageSize = 100, returnSubAreaLimitGroupCurriculumSubAreaID = True, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnModifiedTime = False, returnSubAreaLimitGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroupCurriculumSubArea/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSubAreaLimitGroupCurriculumSubArea(SubAreaLimitGroupCurriculumSubAreaID, EntityID = 1, returnSubAreaLimitGroupCurriculumSubAreaID = True, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnModifiedTime = False, returnSubAreaLimitGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroupCurriculumSubArea/" + str(SubAreaLimitGroupCurriculumSubAreaID), verb = "get", return_params_list = return_params_list)

def modifySubAreaLimitGroupCurriculumSubArea(SubAreaLimitGroupCurriculumSubAreaID, EntityID = 1, setCurriculumSubAreaID = None, setSubAreaLimitGroupID = None, setRelationships = None, returnSubAreaLimitGroupCurriculumSubAreaID = True, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnModifiedTime = False, returnSubAreaLimitGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroupCurriculumSubArea/" + str(SubAreaLimitGroupCurriculumSubAreaID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSubAreaLimitGroupCurriculumSubArea(EntityID = 1, setCurriculumSubAreaID = None, setSubAreaLimitGroupID = None, setRelationships = None, returnSubAreaLimitGroupCurriculumSubAreaID = True, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnModifiedTime = False, returnSubAreaLimitGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroupCurriculumSubArea/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSubAreaLimitGroupCurriculumSubArea(SubAreaLimitGroupCurriculumSubAreaID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempEndorsementDefault(EntityID = 1, page = 1, pageSize = 100, returnTempEndorsementDefaultID = True, returnActionType = False, returnActionTypeCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndorsementDefaultID = False, returnEndorsementID = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivable = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempEndorsementDefault(TempEndorsementDefaultID, EntityID = 1, returnTempEndorsementDefaultID = True, returnActionType = False, returnActionTypeCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndorsementDefaultID = False, returnEndorsementID = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivable = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementDefault/" + str(TempEndorsementDefaultID), verb = "get", return_params_list = return_params_list)

def modifyTempEndorsementDefault(TempEndorsementDefaultID, EntityID = 1, setActionType = None, setActionTypeCode = None, setCodeDescription = None, setEndorsementDefaultID = None, setEndorsementID = None, setPrintOnTranscript = None, setWaivable = None, setRelationships = None, returnTempEndorsementDefaultID = True, returnActionType = False, returnActionTypeCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndorsementDefaultID = False, returnEndorsementID = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivable = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementDefault/" + str(TempEndorsementDefaultID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempEndorsementDefault(EntityID = 1, setActionType = None, setActionTypeCode = None, setCodeDescription = None, setEndorsementDefaultID = None, setEndorsementID = None, setPrintOnTranscript = None, setWaivable = None, setRelationships = None, returnTempEndorsementDefaultID = True, returnActionType = False, returnActionTypeCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndorsementDefaultID = False, returnEndorsementID = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivable = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementDefault/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempEndorsementDefault(TempEndorsementDefaultID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempEndorsementImportError(EntityID = 1, page = 1, pageSize = 100, returnTempEndorsementImportErrorID = True, returnCodeDescription = False, returnCreatedTime = False, returnErrorString = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementImportError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempEndorsementImportError(TempEndorsementImportErrorID, EntityID = 1, returnTempEndorsementImportErrorID = True, returnCodeDescription = False, returnCreatedTime = False, returnErrorString = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementImportError/" + str(TempEndorsementImportErrorID), verb = "get", return_params_list = return_params_list)

def modifyTempEndorsementImportError(TempEndorsementImportErrorID, EntityID = 1, setCodeDescription = None, setErrorString = None, setRelationships = None, returnTempEndorsementImportErrorID = True, returnCodeDescription = False, returnCreatedTime = False, returnErrorString = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementImportError/" + str(TempEndorsementImportErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempEndorsementImportError(EntityID = 1, setCodeDescription = None, setErrorString = None, setRelationships = None, returnTempEndorsementImportErrorID = True, returnCodeDescription = False, returnCreatedTime = False, returnErrorString = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementImportError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempEndorsementImportError(TempEndorsementImportErrorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempFailedStudentSubAreaCurriculumSubArea(EntityID = 1, page = 1, pageSize = 100, returnTempFailedStudentSubAreaCurriculumSubAreaID = True, returnActionType = False, returnAppliedOrder = False, returnAreaSubAreaDescription = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnEntityCode = False, returnFutureCredits = False, returnInProgressCredits = False, returnModifiedTime = False, returnNote = False, returnSchoolYearDescription = False, returnSectionCode = False, returnStudentCourseRequestID = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaCurriculumSubArea/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempFailedStudentSubAreaCurriculumSubArea(TempFailedStudentSubAreaCurriculumSubAreaID, EntityID = 1, returnTempFailedStudentSubAreaCurriculumSubAreaID = True, returnActionType = False, returnAppliedOrder = False, returnAreaSubAreaDescription = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnEntityCode = False, returnFutureCredits = False, returnInProgressCredits = False, returnModifiedTime = False, returnNote = False, returnSchoolYearDescription = False, returnSectionCode = False, returnStudentCourseRequestID = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaCurriculumSubArea/" + str(TempFailedStudentSubAreaCurriculumSubAreaID), verb = "get", return_params_list = return_params_list)

def modifyTempFailedStudentSubAreaCurriculumSubArea(TempFailedStudentSubAreaCurriculumSubAreaID, EntityID = 1, setActionType = None, setAppliedOrder = None, setAreaSubAreaDescription = None, setAttemptedCredits = None, setCompletedCredits = None, setCourseCode = None, setCourseDescription = None, setCurriculumSubAreaID = None, setEntityCode = None, setFutureCredits = None, setInProgressCredits = None, setNote = None, setSchoolYearDescription = None, setSectionCode = None, setStudentCourseRequestID = None, setStudentSubAreaID = None, setRelationships = None, returnTempFailedStudentSubAreaCurriculumSubAreaID = True, returnActionType = False, returnAppliedOrder = False, returnAreaSubAreaDescription = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnEntityCode = False, returnFutureCredits = False, returnInProgressCredits = False, returnModifiedTime = False, returnNote = False, returnSchoolYearDescription = False, returnSectionCode = False, returnStudentCourseRequestID = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaCurriculumSubArea/" + str(TempFailedStudentSubAreaCurriculumSubAreaID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempFailedStudentSubAreaCurriculumSubArea(EntityID = 1, setActionType = None, setAppliedOrder = None, setAreaSubAreaDescription = None, setAttemptedCredits = None, setCompletedCredits = None, setCourseCode = None, setCourseDescription = None, setCurriculumSubAreaID = None, setEntityCode = None, setFutureCredits = None, setInProgressCredits = None, setNote = None, setSchoolYearDescription = None, setSectionCode = None, setStudentCourseRequestID = None, setStudentSubAreaID = None, setRelationships = None, returnTempFailedStudentSubAreaCurriculumSubAreaID = True, returnActionType = False, returnAppliedOrder = False, returnAreaSubAreaDescription = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnEntityCode = False, returnFutureCredits = False, returnInProgressCredits = False, returnModifiedTime = False, returnNote = False, returnSchoolYearDescription = False, returnSectionCode = False, returnStudentCourseRequestID = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaCurriculumSubArea/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempFailedStudentSubAreaCurriculumSubArea(TempFailedStudentSubAreaCurriculumSubAreaID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempFailedStudentSubAreaWaiver(EntityID = 1, page = 1, pageSize = 100, returnTempFailedStudentSubAreaWaiverID = True, returnActionType = False, returnAreaSubAreaDescription = False, returnCreatedTime = False, returnCredits = False, returnModifiedTime = False, returnNote = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaWaiver/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempFailedStudentSubAreaWaiver(TempFailedStudentSubAreaWaiverID, EntityID = 1, returnTempFailedStudentSubAreaWaiverID = True, returnActionType = False, returnAreaSubAreaDescription = False, returnCreatedTime = False, returnCredits = False, returnModifiedTime = False, returnNote = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaWaiver/" + str(TempFailedStudentSubAreaWaiverID), verb = "get", return_params_list = return_params_list)

def modifyTempFailedStudentSubAreaWaiver(TempFailedStudentSubAreaWaiverID, EntityID = 1, setActionType = None, setAreaSubAreaDescription = None, setCredits = None, setNote = None, setStudentSubAreaID = None, setRelationships = None, returnTempFailedStudentSubAreaWaiverID = True, returnActionType = False, returnAreaSubAreaDescription = False, returnCreatedTime = False, returnCredits = False, returnModifiedTime = False, returnNote = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaWaiver/" + str(TempFailedStudentSubAreaWaiverID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempFailedStudentSubAreaWaiver(EntityID = 1, setActionType = None, setAreaSubAreaDescription = None, setCredits = None, setNote = None, setStudentSubAreaID = None, setRelationships = None, returnTempFailedStudentSubAreaWaiverID = True, returnActionType = False, returnAreaSubAreaDescription = False, returnCreatedTime = False, returnCredits = False, returnModifiedTime = False, returnNote = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaWaiver/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempFailedStudentSubAreaWaiver(TempFailedStudentSubAreaWaiverID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")